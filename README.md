<<<<<<< HEAD
Object Detection-low visibility traffic scene
========

![language](https://img.shields.io/badge/language-python-blue)![demo](https://img.shields.io/badge/demo-gradio-yellow)



## Introduction

This project is based **on [YOLO]([ultralytics/ultralytics: NEW - YOLOv8 🚀 in PyTorch > ONNX > OpenVINO > CoreML > TFLite (github.com)](https://github.com/ultralytics/ultralytics?tab=readme-ov-file))and [DETR]([facebookresearch/detr: End-to-End Object Detection with Transformers (github.com)](https://github.com/facebookresearch/detr))** ,using  the Exdark data set for fine-tuning training. It is used to predict objects in traffic scenes (especially in low visibility). The repositories contains data set format processing files, running scripts and code to build **[gradio]([gradio-app/gradio: Build and share delightful machine learning apps, all in Python. 🌟 Star to support our work! (github.com)](https://github.com/gradio-app/gradio))**.

****

![](.\scripts\example_images\contract.png)

## Structure

**DETR**

![DETR](./scripts\example_images\DETR.png)

**YOLOv8**

![](.\scripts\example_images\yolov8.jpeg)



## Models

We provide finetune DETR and yolov8n models, and plan to include more in future.
mAP50 and mAP50-95 computing on part of val Exdark datasets.

<table>
  <thead>
    <tr style="text-align: right;">
      <th>name</th>
      <th>backbone</th>
      <th>epochs</th>
      <th>mAP50(B)</th>
      <th>mAP50-95(B)</th>
      <th>Download</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>YOLOv8</td>
      <td>CSPLayer_2Conv</td>
      <td>158</td>
      <td>0.718</td>
      <td>0.46</td>
      <td><a href="https://pan.baidu.com/s/1t5CTDUvvdEZBXc_f6ROFmw?pwd=v3vx ">baidu</a>&nbsp;|&nbsp;<a href="https://drive.google.com/file/d/1IemApstuHSndT6GugK0Wdq6lUMJq46gX/view">google</a></td>
      <td>5.96Mb</td>
           <tr>
      <td>DERT</td>
      <td>ResNet50</td>
      <td>40</td>
      <td>0.706</td>
      <td>0.394</td>
      <td><a href="https://pan.baidu.com/s/17pmrh4fo7UDCX4zyI7egdw?pwd=w8jg ">baidu</a>&nbsp;|&nbsp;<a href="https://drive.google.com/file/d/1jJNxdWadHs6WEwW8vraBcFHFMv7qeNss/view?usp=drive_link">google</a></td>
      <td>474Mb</td>
  </tbody>
</table>



## DataSet Perparation

[Exdark Datasets]([cs-chan/Exclusively-Dark-Image-Dataset: Exclusively Dark (ExDARK) dataset which to the best of our knowledge, is the largest collection of low-light images taken in very low-light environments to twilight (i.e 10 different conditions) to-date with image class and object level annotations. (github.com)](https://github.com/cs-chan/Exclusively-Dark-Image-Dataset))

In the original ExDark data set, there are a total of 12 categories, but our research is to identify driving road condition detection in outdoor situations, so we deleted the unnecessary data and only retained Bicycle, Bus, Car, and Motorbike. , People and Animal these 6 categories. Among them, Animal is merged from the two classes Cat and Dog in the original data set.

First, we read in the seven categories (**Bicycle, Bus, Car, Motorbike, People, Cat, Dog**) in the original data set, and after segmentation, there were **4465** pictures containing the target category. Secondly, further filtering was carried out to select only the labels of outdoor scenes, a total of **3468** images, and the cat and dog data sets were merged into the Animal data set.



# Usage

## Environment

We recommand you use conda to install environments.

```shell
conda create -n od python=3.9
# essential package in requirements.txt
cd od
conda install --yes --file requirements.txt
```



or use pip to install some important package.

```shell
pip install ultralytics
```



**(optional)**for use gradio, you also need to install gradio.

```shell
pip install gradio
```



### Data format

if you want to train on yolov8,use [Exdark2yolo.py](./scripts/Exdark2yolo.py),and chage the path in this file.

```python
parser.add_argument('--annotations-dir', type=str,default="../data/Exdark_Annno/" , help="ExDark annotations directory.")
    parser.add_argument('--images-dir', default='../data/Exdark/',type=str, help="ExDark images directory.")
    parser.add_argument('--ratio', type=str, default='8:1:1', help="Ratio between train/test/val, default 8:1:1.")
    parser.add_argument('--output-dir', type=str, default="../datasets/Exdark", help="Images and converted YOLO annotations output directory.")              
```

elif convert yolo format to coco, use [yolo2coco](./scripts/Exdark2yolo.py),and chage the path in this file.

```python
coco_format_save_path='../datasets/Exdark_json/val'    
yolo_format_classes_path='./classes.txt'
yolo_format_annotation_path='../datasets/Exdark/labels/val'     
img_pathDir='../datasets/Exdark/images/val'         
```



### Predict

First, download our model or use your own model,place it in **checkpoints** folder,rename it to best_yolo.py or best_detr.pth.

**YOLOv8**:use [yolov8_predict.py](./scripts/yolov8_predict.py),change the pic to your own.

**DETR:**use [detr_predict.py](./scripts/detr_predict.py),change the pic to your own.

**LightValue:**use [lightValuePredict.py](./scripts/lightValuePredict.py)



### Gradio

**before using, please ensure you have installed gradio.**

```
cd scripts
python main.py
```

![gradio](D:\python_code\od\scripts\example_images\gradio.png)

# Contributing
We actively welcome your pull requests! If you have any question, you send mail to 615792775@qq.com or contact we by github :)
=======
# object-dection-low-visibility
This project is based on YOLO and DETR ,using the Exdark datasets for fine-tuning training. It is used to predict objects in traffic scenes (especially in low visibility). The repositories contains data set format processing files, running scripts and code to build gradio.
>>>>>>> 0f3b03101c34905089d8cd16b124e4a6d689373b
