import os
import shutil
import gradio as gr
from PIL import Image
import cv2
from lightValuePredict import *

def image_predict(image_path, model_name='DETR'):
    test_image_path = './images/test.jpg'
    save_image_path = './runs/detect/predict/test.jpg'

    if (os.path.exists(test_image_path)):
        os.remove(test_image_path)

    if (os.path.exists('./runs/detect')):
        shutil.rmtree('./runs/detect', ignore_errors=True)
    # print(type(image_path))
    image = Image.open(image_path)
    image.save('./images/test.jpg')

    if(model_name=='YOLOv8'):
        os.system(f'python yolov8_predict.py --type=image')
    
    elif(model_name=='DETR'):
        os.system(f'python detr_predict.py')
    
    light_level = light_predict('./images/test.jpg')
    return [Image.open(save_image_path), light_level]

def video_predict(video):

    shutil.copyfile(video, './videos/test.mp4')
    if (os.path.exists('./runs/detect')):
        shutil.rmtree('./runs/detect', ignore_errors=True)
    os.system(f'python yolov8_predict.py --type=video')
    return gr.Video('./runs/detect/predict/test.avi')

def light_predict(image_path):

    predicted_light_values = analyze_brightness(image_path)
    return predicted_light_values


if __name__ == '__main__':
    with gr.Blocks() as inf:
        with gr.Tab("图片处理"):
            with gr.Row():
                with gr.Column():
                # 输入图片
                    image = gr.components.Image(type="filepath")
                # 下拉框选择
                    target = gr.Dropdown(["YOLOv8", "DETR"], label="模型选择", value="YOLOv8")
                # 单项选择
                    radio = gr.Radio(["是", "否"], label="是否显示能见度", value="是")
                image_output = gr.Image()
                light_output = gr.Textbox(label="光照条件检测")
            image_button = gr.Button("提交")

        with gr.Tab("视频处理"):
            with gr.Row():
                # 获取视频路径
                video_input = gr.Video(sources="upload")
                video_output = gr.Video(label="Blurred Video")
                video_button = gr.Button("提交")

        image_button.click(image_predict, inputs=[image, target], outputs=[image_output, light_output])
        video_button.click(video_predict, inputs=video_input, outputs=video_output)

    inf.launch(share=True)