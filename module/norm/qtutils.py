from PyQt6 import QtWidgets, QtCore
from matplotlib.backends import backend_qtagg


class QVBoxLayout(QtWidgets.QVBoxLayout):

    def __init__(self, *args, layout=None, **kwargs):
        super().__init__(*args, **kwargs)
        if layout is not None:
            layout.addLayout(self)


class QHBoxLayout(QtWidgets.QHBoxLayout):

    def __init__(self, *args, layout=None, **kwargs):
        super().__init__(*args, **kwargs)
        if layout is not None:
            layout.addLayout(self)


class QLineEdit(QtWidgets.QLineEdit):

    def __init__(self,
                 *args,
                 label=None,
                 default=None,
                 layout=None,
                 minw=40,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default
        self.setMinimumWidth(minw)
        if not label:
            if layout is not None:
                layout.addWidget(self)
            return
        hlayout = QHBoxLayout(layout=layout)
        lb = QtWidgets.QLabel(label)
        hlayout.addWidget(lb)
        hlayout.addWidget(self)
        self.reset()

    def reset(self):
        if self.default is not None:
            self.setText(self.default)


class FigureCanvas(backend_qtagg.FigureCanvas):

    def __init__(self, *args, msize=None, layout=None, parent=None, **kwargs):
        super().__init__(*args, **kwargs)
        if msize is not None:
            self.setMinimumWidth(msize[0])
            self.setMinimumHeight(msize[1])
        if layout is not None:
            layout.addWidget(self)
        if parent is not None:
            toolbar = backend_qtagg.NavigationToolbar2QT(self, parent)
            toolbar.setIconSize(QtCore.QSize(20, 20))
            if layout is not None:
                layout.addWidget(toolbar)
