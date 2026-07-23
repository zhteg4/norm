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
        vlayout = qtutils.VBoxLayout(layout=hlayout)

        self.canvas = qtutils.FigureCanvas(msize=(400, 300),
                                           layout=vlayout,
                                           parent=self)

        self.ax = self.canvas.figure.subplots()

        vlayout = qtutils.VBoxLayout(layout=hlayout)
        self.loc_le = qtutils.FLineEdit(label='loc:',
                                        default='40',
                                        tFin=self.plot,
                                        layout=vlayout)
        self.scale_le = qtutils.FLineEdit(label='scale:',
                                          default='1.5',
                                          tFin=self.plot,
                                          layout=vlayout)
        self.size_le = qtutils.ILineEdit(label='size:',
                                         default='200',
                                         tFin=self.plot,
                                         layout=vlayout)
        vlayout.addStretch(1)

        reset_bn = QtWidgets.QPushButton("Reset")
        reset_bn.clicked.connect(self.reset)
        vlayout.addWidget(reset_bn)
        self.reset()

    def reset(self):
        self.loc_le.reset()
        self.scale_le.reset()
        self.size_le.reset()
        self.plot()

    def plot(self):
        rng = np.random.default_rng()
        samples = rng.normal(loc=self.loc_le.value,
                             scale=self.scale_le.value,
                             size=self.size_le.value)
        self.ax.clear()
        self.ax.hist(samples, edgecolor="white")
        self.canvas.draw()


if __name__ == "__main__":
    qapp = QtWidgets.QApplication([])
    app = ApplicationWindow()
    app.show()
    qapp.exec()
