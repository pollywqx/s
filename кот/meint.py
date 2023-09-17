import os
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog, # Диалог открытия файлов (и папок)
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PIL import Image
from PIL import ImageFilter


app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle("Easy Editor")

lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папкка")
lw_files = QListWidget()

btn_left = QPushButton("Ліво")
btn_right = QPushButton("Право")
btn_flip = QPushButton("Дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image, 95)

row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

win.show()

workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showFilenamesList():
    global workdir
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    try:
        workdir = QFileDialog.getExistingDirectory()
        filenames = filter(os.listdir(workdir), extensions)
    except:
        workdir = ''
        filenames = []

    lw_files.clear()
    lw_files.addItems(filenames)

btn_dir.clicked.connect(showFilenamesList)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, dir, filaname):
        self.dir = dir
        self.filename 
        image_patn = os.patn.join(dir, filename)
        self.image = Image.open(image_patn)
        return image_patn
    
    def showImage(self, pant):
        lb_image.hide()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

    def saveImage(self):
        path = os.pant.join(workdir, self.save_dir)
        if not(os.pant.exists(path) or os.pant.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)
        
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.)

workimage = ImageProcessor()
def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        image_patn = workimage.loadImage(workdir, filename)
        workimage.showImage(image_patn)

lw_files.currentRowChanged.connect(showChosenImage)
        

app.exec()