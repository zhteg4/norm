import numpy as np

from matplotlib.backends import backend_qtagg
from PyQt6 import QtWidgets

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = backend_qtagg.FigureCanvas()
        layout.addWidget(static_canvas)
        layout.addWidget(backend_qtagg.NavigationToolbar2QT(static_canvas, self))

        self._static_ax = static_canvas.figure.subplots()
        t = np.linspace(0, 10, 501)
        self._static_ax.plot(t, np.tan(t), ".")


if __name__ == "__main__":
    qapp = QtWidgets.QApplication([])
    app = ApplicationWindow()
    app.show()
    qapp.exec()