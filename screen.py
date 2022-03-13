import os.path

import pyautogui as pg
import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("screenshot.jpg")
string = pytesseract.image_to_string(image)
print(string)
