# PyQT5 imports
from PyQt5 import QtGui, QtCore, QtOpenGL, QtWidgets
from PyQt5.QtOpenGL import QGLWidget
from ctypes import *
from src.gl_manager import gl_manager
import numpy as np
import numpy.random as rnd

# define a QT window with an OpenGL widget inside it
class Renderer(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Renderer, self).__init__(parent)
        self.data = np.array([
            [ -0.90, -0.90 ],
            [  0.85, -0.90 ],
            [ -0.90,  0.85 ],
            [  0.70, -0.85 ],
            [  0.90,  0.90 ],
            [ -0.85,  0.90 ]
        ], dtype = np.float32)
        # initialize the GL widget
        glformat = QtOpenGL.QGLFormat()
        glformat.setVersion(4, 1)
        glformat.setProfile(QtOpenGL.QGLFormat.CoreProfile)
        glformat.setSampleBuffers( True )
        self.widget = gl_manager(glformat)
        self.widget.set_data(self.data)
        # put the window at the screen position (100, 100)
        self.setGeometry(100, 100, self.widget.width, self.widget.height)
        self.setCentralWidget(self.widget)
        self.show()
