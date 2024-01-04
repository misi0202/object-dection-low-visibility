import os
from PIL import Image
import argparse
import shutil

# 从中读入目标标签 Cat和Dog后面处理成一类animal
labels = ['Bicycle', 'Bus', 'Car', 'Motorbike', 'People','Cat','Dog']


def ExDark2Yolo(txts_dir: str, imgs_dir: str, ratio: str, output_dir: str):
    ratios = ratio.split(':')
    ratio_train, ratio_test, ratio_val = int(ratios[0]), int(ratios[1]), int(ratios[2])
    ratio_sum = ratio_train + ratio_test + ratio_val
    dataset_perc = {'train': ratio_train / ratio_sum, 'test': ratio_test / ratio_sum, 'val': ratio_val / ratio_sum}

    for t in dataset_perc:
        if(not os.path.exists('/'.join([output_dir, 'images', t]))):
            os.makedirs('/'.join([output_dir, 'images', t]))
        if(not os.path.exists('/'.join([output_dir, 'images', t]))):    
            os.makedirs('/'.join([output_dir, 'labels', t]))

    for label in labels:
        print('Processing {}...'.format(label))
        filenames = os.listdir('/'.join([txts_dir, label]))
        cur_idx = 0
        files_num = len(filenames)

        for filename in filenames:
            cur_idx += 1
            filename_no_ext = '.'.join(filename.split('.')[:-2])
            if cur_idx < dataset_perc.get('train') * files_num:
                set_type = 'train'
            elif cur_idx < (dataset_perc.get('train') + dataset_perc.get('test')) * files_num:
                set_type = 'test'
            else:
                set_type = 'val'
            output_label_path = '/'.join([output_dir, 'labels', set_type, filename_no_ext + '.txt'])
            yolo_output_file = open(output_label_path, 'a')

            name_split = filename.split('.')
            img_path = '/'.join([imgs_dir, label, '.'.join(filename.split('.')[:-1])])
            try:
                img = Image.open(img_path)
            except FileNotFoundError:
                img_path = '/'.join([imgs_dir, label, ''.join(name_split[:-2]) + '.' + name_split[-2].upper()])
                img = Image.open(img_path)

            output_img_path = '/'.join([output_dir, 'images', set_type])
            shutil.copy(img_path, output_img_path)

            width, height = img.size
            txt = open('/'.join([txts_dir, label, filename]), 'r')
            txt.readline()  # ignore first line
            line = txt.readline()

            while line != '':
                datas = line.strip().split()
                if(not datas[0] in labels):break
                class_idx = labels.index(datas[0])
                x0, y0, w0, h0 = int(datas[1]), int(datas[2]), int(datas[3]), int(datas[4])
                x = (x0 + w0/2) / width
                y = (y0 + h0/2) / height

                w = w0 / width
                h = h0 / height

                yolo_output_file.write(' '.join([str(class_idx),
                                                 format(x, '.6f'),
                                                 format(y, '.6f'),
                                                 format(w, '.6f'),
                                                 format(h, '.6f'),
                                                 ]) + '\n')
                line = txt.readline()

            yolo_output_file.close()

# 室内图片删除
def Remain_Outdoor(images_dir='../datasets/Exdark/images/', labels_dir='../datasets/Exdark/labels/',txt_path='../data/imageclasslist.txt'):
    txt = open(txt_path, 'r')
    lines = txt.readlines()
    image = ""
    for line in lines:
        columns = line.split()
        name = columns[0]
        target_column = columns[3]
        splitname = name.split('.')[0]
        splitname = splitname + '.txt'
        for diff in os.listdir(labels_dir):
            labels_diff = os.path.join(labels_dir, diff)
            anno = os.path.join(labels_diff, splitname)
            images_diff = os.path.join(images_dir, diff)
            image = os.path.join(images_diff, name)
            if(target_column=="1" and os.path.exists(anno)):
                # os.system(f"attrib -r {diff}")
                os.remove(anno)
                os.remove(image)
                    # print(target_column,image)
        
        
    txt.close()
    print("delete indoor image")
    return

# 将多列标签整合为一列
def combine_labels(first_label="5", second_label="6",labels_dir='../datasets/Exdark/labels/'):
    for diff in os.listdir(labels_dir):
        labels_diff = os.path.join(labels_dir, diff)
        for f in os.listdir(labels_diff):
            w = ""
            txt = open(os.path.join(labels_diff, f), 'r')
            lines = txt.readlines()
            
            for line in lines:
                columns = line.split()
                if columns[0] == '5' or columns[0] == '6':
                    columns[0] = '5'

                w += columns[0] 
                w += ' '
                w += columns[1]
                w += ' '
                w += columns[2]
                w += ' '
                w += columns[3]
                w += ' '
                w += columns[4]
                w += '\n'

            txt = open(os.path.join(labels_diff, f), 'w')
            txt.writelines(w)
            txt.close()
    print("combine finish")






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--annotations-dir', type=str,default="../data/Exdark_Annno/" , help="ExDark annotations directory.")
    parser.add_argument('--images-dir', default='../data/Exdark/',type=str, help="ExDark images directory.")
    parser.add_argument('--ratio', type=str, default='8:1:1', help="Ratio between train/test/val, default 8:1:1.")
    parser.add_argument('--output-dir', type=str, default="../datasets/Exdark", help="Images and converted YOLO annotations output directory.")
    args = parser.parse_args()
    ExDark2Yolo(args.annotations_dir, args.images_dir, args.ratio,  args.output_dir)
    Remain_Outdoor()
    combine_labels()