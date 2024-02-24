from PIL import *
from PIL import Image
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