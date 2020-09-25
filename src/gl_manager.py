# PyOpenGL imports
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLUT import *
from PyQt5.QtOpenGL import QGLWidget

class gl_manager(QGLWidget):
    # default window size
    width, height = 600, 600

    def __init__(self, format = None):
        super(gl_manager, self).__init__(format, None)

    def set_data(self, data):
        self.data = data
        self.count = self.data.nbytes
        self.numVAOs = 2
        self.VAOs = [0] * self.numVAOs
        self.numVBOs = 2
        self.VBOs = [0] * self.numVBOs
        self.shader = None
        self.vPositionLocation = 0

    def initializeGL(self):

        glClearColor(0.0, 0.0, 0.0, 1.0)

        self.VAOs = glGenVertexArrays(self.numVAOs)
        glBindVertexArray(self.VAOs[0])

        self.VBOs = glGenBuffers(self.numVBOs)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBOs[0])
        glBufferData(GL_ARRAY_BUFFER, self.count, self.data, GL_STATIC_DRAW)

        VERTEX_SHADER = compileShader("""
            #version 410 core
            layout(location = 0) in vec4 vPosition;
            void main() {
                gl_Position = vPosition;
            }
        """, GL_VERTEX_SHADER)

        FRAGMENT_SHADER = compileShader("""
            #version 410 core
            out vec4 fColor;
            void main() {
                fColor = vec4(1.0, 1.0, 0.0, 1.0);
            }
        """, GL_FRAGMENT_SHADER)

        self.shader = compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)
        glUseProgram(self.shader)

        glVertexAttribPointer(self.vPositionLocation, 2, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(self.vPositionLocation)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glBindVertexArray(self.VAOs[0])
        glDrawArrays(GL_TRIANGLES, 0, self.count)

        glFlush()
