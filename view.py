from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QGroupBox,
    QSlider,
    QFormLayout,
    QTabWidget,
    QToolBar,
    QAction,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect

import cv2 as cv




class View(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(1000, 600)
        self.setWindowTitle('Sotoshop')
        
        self._gnrLayout = QHBoxLayout()
        self._cntWidget = QWidget()
        
        self.setCentralWidget(self._cntWidget)
        self._cntWidget.setLayout(self._gnrLayout)
        
        self._createMenu()
        self._createMain()
        
    def _createMenu(self):
        self.mainMenu = self.menuBar()
        
        self.fileMenu = self.mainMenu.addMenu('&File')
        
        self.openAction = QAction('Open')
        self.saveAction = QAction('Save')
        self.exitAction = QAction('Exit')
        
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.exitAction)
        
        self.editMenu = self.mainMenu.addMenu('&Edit')
        
        self.undoAction = QAction('Undo')
        self.redoAction = QAction('Redo')
        self.transformAction = QAction('Transform')
        
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addAction(self.transformAction)
        
        self.imageMenu = self.mainMenu.addMenu('&Image')
        self.modAction = QAction('Mode')
        self.aTonAction = QAction('Auto Tone')
        self.aConAction = QAction('Auto Contrast')
        self.aColAction = QAction('Auto Color')
        
        self.imageMenu.addAction(self.modAction)
        self.imageMenu.addAction(self.aTonAction)
        self.imageMenu.addAction(self.aConAction)
        self.imageMenu.addAction(self.aColAction)
    
    def _createMain(self):
        '''Left Side'''
        # Image layout.
        self.imgLayout = QVBoxLayout()
        
        # Tampilan gambar.
        self.imgLabel = QLabel('Your Image\nGoes Here')
        self.imgLabel.setAlignment(Qt.AlignCenter)
        self.imgLabel.setFixedWidth(600)
        
        # Configure layout.
        self.imgLayout.addWidget(self.imgLabel)
        self._gnrLayout.addLayout(self.imgLayout)
        
        '''Right Side'''
        # Right layout.
        self.editingLayout = QVBoxLayout()
        
        # Tab layout.
        self.editingTabs = QTabWidget()
        self.editingTabs.setFixedHeight(300)
        # Adjustments tab.
        self.adjTab = QWidget()
        self.editingTabs.addTab(self.adjTab, 'Adjustments')
        # Operations tab.
        self.opeTab = QWidget()
        self.editingTabs.addTab(self.opeTab, 'Operations')
        # # Filter tab.
        # self.filTab = QWidget()
        # self.editingTabs.addTab(self.filTab, 'Filter')
        
        # Adjustments layout.
        self.adjLayout = QFormLayout()
        # Operations layout.
        self.opeLayout = QGridLayout()
        self.opeLayout.setAlignment(Qt.AlignTop)
        # Filter layout.
        
        '''Adjustments'''
        # Brightness slider.
        self.briSlider = QSlider(Qt.Horizontal)
        self.briSlider.setValue(50)
        
        # Contrast slider.
        self.conSlider = QSlider(Qt.Horizontal)
        self.conSlider.setValue(50)
        
        # Exposure slider.
        self.expSlider = QSlider(Qt.Horizontal)
        self.expSlider.setValue(50)
        
        # Highlight slider.
        self.higSlider = QSlider(Qt.Horizontal)
        self.higSlider.setValue(50)
        
        # Shadow slider.
        self.shaSlider = QSlider(Qt.Horizontal)
        self.shaSlider.setValue(50)
        
        # Saturation slider.
        self.satSlider = QSlider(Qt.Horizontal)
        self.satSlider.setValue(50)
        
        # Tint slider.
        self.tinSlider = QSlider(Qt.Horizontal)
        self.tinSlider.setValue(50)
        
        # Temperature slider.
        self.temSlider = QSlider(Qt.Horizontal)
        self.temSlider.setValue(50)
        
        '''Operations'''
        # Straighten label.
        self.strLabel = QLabel('Straighten')
        self.strLabel.setAlignment(Qt.AlignCenter)
        # Straighten slider.
        self.strSlider = QSlider(Qt.Horizontal)
        self.strSlider.setMinimum(-45)
        self.strSlider.setMaximum(45)
        self.strSlider.setValue(0)
        
        # Subtract button.
        self.sutButton = QPushButton('Subtract')
        # Subjoin button.
        self.sujButton = QPushButton('Subjoin')
        
        # Boolean "and" button.
        self.andButton = QPushButton('and')
        # Boolean "or" button.
        self.orrButton = QPushButton('or')
        # Boolean "not" button.
        self.notButton = QPushButton('not')
        # Boolean "xor" button.
        self.xorButton = QPushButton('xor')
        
        # Rotate button.
        self.rotButton = QPushButton('Rotate')
        # Flip button.
        self.fliButton = QPushButton('Flip')
        
        # Crop button.
        self.croButton = QPushButton('Crop')
        
        # Histogram
        self.hisLabel = QLabel('Histogram')
        self.hisLabel.adjustSize()
        self.hisLabel.setAlignment(Qt.AlignCenter)
        self.hisLabel.setStyleSheet('QLabel{background-color: white;}')
        
        # Configure layout.
        self.adjLayout.addRow('Brightness', self.briSlider)
        self.adjLayout.addRow('Contrast', self.conSlider)
        self.adjLayout.addRow('Exposure', self.expSlider)
        self.adjLayout.addRow('Highlight', self.higSlider)
        self.adjLayout.addRow('Shadow', self.shaSlider)
        self.adjLayout.addRow('Saturation', self.satSlider)
        self.adjLayout.addRow('Tint', self.tinSlider)
        self.adjLayout.addRow('Temperature', self.temSlider)
        
        self.opeLayout.addWidget(self.strLabel, 0, 0, 1, 2)
        self.opeLayout.addWidget(self.strSlider, 1, 0, 1, 2)
        self.opeLayout.addWidget(self.sutButton, 2, 0)
        self.opeLayout.addWidget(self.sujButton, 2, 1)
        self.opeLayout.addWidget(self.andButton, 3, 0)
        self.opeLayout.addWidget(self.orrButton, 3, 1)
        self.opeLayout.addWidget(self.notButton, 4, 0)
        self.opeLayout.addWidget(self.xorButton, 4, 1)
        
        self.opeLayout.addWidget(self.rotButton, 5, 0)
        self.opeLayout.addWidget(self.fliButton, 5, 1)
        
        self.opeLayout.addWidget(self.croButton, 6, 0, 1, 2)
        
        self.adjTab.setLayout(self.adjLayout)
        self.opeTab.setLayout(self.opeLayout)
        
        self.editingLayout.addWidget(self.editingTabs)
        self.editingLayout.addWidget(self.hisLabel)
        
        self._gnrLayout.addLayout(self.editingLayout)
        
