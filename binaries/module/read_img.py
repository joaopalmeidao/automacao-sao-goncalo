import cv2
import pytesseract

import os

class Read_img():
    def __init__(self, directory) -> None:
        self.directory = directory

    def all_img_files(self):
        return [os.path.join(self.directory, file) for file in os.listdir(self.directory)
                if file.lower().endswith('.jpeg') or file.lower().endswith('.jpg') or file.lower().endswith('.png')]

    def img_data(self, img):
        file_name = img

        img = cv2.imread(img)

        data = []

        path = 'C:\Program Files\Tesseract-OCR'

        pytesseract.pytesseract.tesseract_cmd = path + r'\\tesseract.exe'

        text = pytesseract.image_to_string(img, lang='por')

        info = (
            text,
            file_name,
        )

        data.append(info)

        return data


if __name__ == '__main__':
    img = Read_img(r'arquivos\\')
    all = img.all_img_files()
    for i in all:
        result = img.img_data(i)
        print(result)