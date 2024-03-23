import os
from time import sleep

from PIL import *
from PIL import Image, ImageFilter
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
app = QApplication([])

app.setStyleSheet("""
        QPushButton {
            color:#35374B;
        background-color: red;
        }
        
        QPushButton#papk {
            color:#8E7AB5;
            background-color: #78A083;
            border-color:#436850;
            border-width: 9px;
            padding: 12px;
        }

        QPushButton#lamat {
            color:#00000;
            background-color: #FF0A0E;
            border-color:#B30B0E;
            border-width: 9px;
            padding: 12px;
        }
        QPushButton
        {
            background-color: #ffb600;
            border-style: groove;
            border-color:#FFF67E;
            border-width: 7px;
            font-size: 17px;
            font-family: Roboto;
            min-width: 6em;
            padding: 7px;
        }

    """)




def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap








window = QWidget()
window.resize(700,500)

app.setStyle('Windows')








window.show()



open_papk = QPushButton("Папка")
info_list = QListWidget()
photo = QLabel()
filter_1 = QPushButton("Фільтер 1")
filter_2 = QPushButton("Фільтер 2")
filter_3 = QPushButton("Фільтер 3")
filter_4 = QPushButton("Фільтер 4")
filter_5 = QPushButton("Фільтер 5")
filter_6 = QPushButton("Фільтер 6")
filter_7 = QPushButton("Фільтер 7")
knopka_yzhas = QPushButton("НЕ НАЖИМАЙ!")
destroy_button = QPushButton("взламати программе")



H1 = QHBoxLayout()
H2 = QHBoxLayout()
V1 = QVBoxLayout()
V2 = QVBoxLayout()


H1.addLayout(V1)
H1.addLayout(V2)

class WorkWithPhoto:
    def __init__(self):
        self.image = None
        self.Folder = None
        self.image_name = None
    def show_image(self):
        pass

    def load(self):
        full_path = os.path.join(self.folder, self.image_name)
        self.image = Image.open(full_path)


    def show_image(self):
        pixel = pil2pixmap(self.image)
        photo.setPixmap(pixel)


    def rozmit(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.show_image()

    def emo_kaktus(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.show_image()

    def contor(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.show_image()

    def smmothj(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.show_image()

    def DETALNIST(self):
        self.image = self.image.filter(ImageFilter.DETAIL)
        self.show_image()

    def open_ima(self):
        self.image = Image.open("Мега Секретне Фото.png")
        self.show_image()
    def enchance(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.show_image()

    def KVADRAT(self):
        self.image = self.image.filter(ImageFilter.BoxBlur)
        self.show_image()
work_with_photo = WorkWithPhoto()


def mega_destroy():
    window.hide()
    for i in range(15):
        print("твоя программа вернеться через 4 секунди!")
    sleep(4)
    window.show()



def show_directory():
    work_with_photo.folder = QFileDialog.getExistingDirectory()
    list_files= os.listdir(work_with_photo.folder)

    for file in list_files:
        if file.endswith("png"):
            info_list.addItem(file)


def knopka_yzhasa():
    image_name = ""
    print(image_name)

    image_name.load()
    image_name.show_image()

def show_photo():
    image_name = info_list.currentItem().text()
    print(image_name)
    work_with_photo.image_name = image_name
    work_with_photo.load()
    work_with_photo.show_image()

info_list.currentRowChanged.connect(show_photo)
open_papk.clicked.connect(show_directory)
filter_1.clicked.connect(work_with_photo.rozmit)
filter_2.clicked.connect(work_with_photo.emo_kaktus)
filter_3.clicked.connect(work_with_photo.contor)
filter_4.clicked.connect(work_with_photo.smmothj)
filter_5.clicked.connect(work_with_photo.DETALNIST)
knopka_yzhas.clicked.connect(work_with_photo.open_ima)
filter_6.clicked.connect(work_with_photo.enchance)
filter_7.clicked.connect(work_with_photo.KVADRAT)
destroy_button.clicked.connect(mega_destroy)
V1.addWidget(open_papk)
V1.addWidget(info_list)

V2.addWidget(photo)
V2.addLayout(H2)
H2.addWidget(filter_1)
H2.addWidget(filter_2)
H2.addWidget(filter_3)
H2.addWidget(filter_4)
H2.addWidget(filter_5)
H2.addWidget(filter_6)
H2.addWidget(filter_7)
V2.addWidget(destroy_button)
H2.addWidget(knopka_yzhas)
open_papk.setObjectName("papk")
destroy_button.setObjectName("lamat")
window.setLayout(H1)




app.exec()