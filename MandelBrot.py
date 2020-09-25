from src.gl_manager import gl_manager
from src.renderer import Renderer
from PyQt5 import QtWidgets
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Renderer()
    window.show()
    app.exec_()
    # app