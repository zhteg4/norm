import numpy as np

from matplotlib.backends import backend_qtagg
from PyQt6 import QtWidgets, QtCore
from norm import qtutils


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Normal Distribution")
        self.resize(600, 500)
        self.setCentralWidget(QtWidgets.QWidget())
        hlayout = QtWidgets.QHBoxLayout(self.centralWidget())
        vlayout = qtutils.QVBoxLayout(layout=hlayout)

        canvas = qtutils.FigureCanvas(msize=(400, 300),
                                      layout=vlayout,
                                      parent=self)

        self.ax = canvas.figure.subplots()
        rng = np.random.default_rng()
        samples = rng.normal(loc=40, scale=1.5, size=200)
        self.ax.hist(samples, edgecolor="white")

        vlayout = qtutils.QVBoxLayout(layout=hlayout)
        self.loc_le = qtutils.QLineEdit(label='loc:',
                                        default='40',
                                        layout=vlayout)
        self.scale_le = qtutils.QLineEdit(label='scale:',
                                          default='1.5',
                                          layout=vlayout)
        self.size_le = qtutils.QLineEdit(label='size:',
                                         default='200',
                                         layout=vlayout)
        vlayout.addStretch(1)

        reset_bn = QtWidgets.QPushButton("Reset")
        reset_bn.clicked.connect(self.reset)
        vlayout.addWidget(reset_bn)

    def reset(self):
        self.loc_le.reset()
        self.scale_le.reset()
        self.size_le.reset()


if __name__ == "__main__":
    qapp = QtWidgets.QApplication([])
    app = ApplicationWindow()
    app.show()
    qapp.exec()
