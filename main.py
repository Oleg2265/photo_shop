import os

from PIL import *
from PIL import Image
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
work_with_photo = WorkWithPhoto()

def show_directory():
    work_with_photo.folder = QFileDialog.getExistingDirectory()
    list_files= os.listdir(work_with_photo.folder)

    for file in list_files:
        if file.endswith("png"):
            info_list.addItem(file)

def show_photo():
    image_name = info_list.currentItem().text()
    print(image_name)
    work_with_photo.image_name = image_name
    work_with_photo.load()
    work_with_photo.show_image()

info_list.currentRowChanged.connect(show_photo)
open_papk.clicked.connect(show_directory)



V1.addWidget(open_papk)
V1.addWidget(info_list)

V2.addWidget(photo)
V2.addLayout(H2)
H2.addWidget(filter_1)
H2.addWidget(filter_2)
H2.addWidget(filter_3)
H2.addWidget(filter_4)
H2.addWidget(filter_5)

open_papk.setObjectName("papk")
window.setLayout(H1)




app.exec()