import cv2
import numpy as np


def calculate_brightness(image_path):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    avg_brightness = np.mean(gray_img)
    return avg_brightness


def analyze_brightness(image_path):
    brightness = calculate_brightness(image_path)
    brightness_intervals = [i * 15 for i in range(10)]  # Update intervals based on 0-255 scale

    for i in range(len(brightness_intervals) - 1):
        if brightness_intervals[i] <= brightness < brightness_intervals[i + 1]:            
            return i + 1
    else:
        return 10


image_path = './images/test.jpg'

predicted_light_values = analyze_brightness(image_path)


