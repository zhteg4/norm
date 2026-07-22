import numpy as np

from matplotlib.backends import backend_qtagg
from PyQt6 import QtWidgets, QtCore

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setCentralWidget(QtWidgets.QWidget())
        layout = QtWidgets.QVBoxLayout(self.centralWidget())

        canvas = backend_qtagg.FigureCanvas()
        layout.addWidget(canvas)

        toolbar = backend_qtagg.NavigationToolbar2QT(canvas, self)
        toolbar.setIconSize(QtCore.QSize(20, 20))
        layout.addWidget(toolbar)

        self.ax = canvas.figure.subplots()
        rng = np.random.default_rng()
        samples = rng.normal(loc=40, scale=1.5, size=200)
        self.ax.hist(samples, edgecolor="white")


if __name__ == "__main__":
    qapp = QtWidgets.QApplication([])
    app = ApplicationWindow()
    app.show()
    qapp.exec()

