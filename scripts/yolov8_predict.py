from ultralytics import YOLO
from PIL import Image
import argparse
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--type", type=str)
args = parser.parse_args()

model = YOLO("./checkpoints/best_yolo.pt")
# image
if (args.type == "image"):
    im1 = Image.open("./images/test.jpg")
    results = model.predict(source=im1, save=True,conf =0.35)  # save plotted images
elif (args.type == "video"):
    results = model.predict(source='./videos/test.mp4', save=True,conf=0.35)