from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFileDialog,
    QMessageBox,
)
from PyQt5.QtGui import (
    QImage,
    QPixmap,
)
from functools import partial

import cv2 as cv



class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        
        self._conSignals()
    
    def _conSignals(self):
        # fileMenu Actions
        self._view.openAction.triggered.connect(partial(self.openImage))
        self._view.exitAction.triggered.connect(partial(self.closeProgram, self._view))
        
            
    def openImage(self):
        imageFile, _ = QFileDialog.getOpenFileName(
            self._view.imgLabel, "Open Image", 
            "", 
            "PNG Files (*.png);;JPG Files (*.jpeg *.jpg );;Bitmap Files (*.bmp);;GIF Files (*.gif)"
        )
        
        self.img = QImage(imageFile)
        self._w = self.img.width()
        self._h = self.img.height()
        print(self._w, self._h)
        self._view.imgLabel.setPixmap(
            QPixmap().fromImage(self.img).scaled(self._view.imgLabel.size(), Qt.KeepAspectRatio)
        )
        print(imageFile)
        self._model._img = cv.imread(imageFile)
        
        
    def closeProgram(self, event):
        msg = 'Are you sure to quit?'
        reply = QMessageBox.question(
            self._view,
            'Message',
            msg,
            QMessageBox.Yes,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            event.close()
        
        
        
        