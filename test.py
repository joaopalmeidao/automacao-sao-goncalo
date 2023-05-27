import cv2
from pytesseract import image_to_string,pytesseract
import os

path = os.path.join(r'C:\Program Files\Tesseract-OCR','tesseract.exe')

pytesseract.tesseract_cmd = path

img = cv2.imread('6a0120a85dcdae970b012877702a86970c-pi.png')


gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = gry.shape[:2]
gry = cv2.resize(gry, (w*2, h*2))
cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None)
thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
txt = image_to_string(thr)
print(txt)