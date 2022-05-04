import sys

from PyQt5.QtWidgets import QApplication

from view import View
from controller import Controller
from model import Model



app = QApplication(sys.argv)

view = View()
view.show()

model = Model()

Controller(model, view)

sys.exit(app.exec_())
