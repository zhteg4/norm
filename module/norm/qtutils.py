from PyQt6 import QtWidgets, QtCore, QtGui
from matplotlib.backends import backend_qtagg


class VBoxLayout(QtWidgets.QVBoxLayout):

    def __init__(self, *args, layout=None, **kwargs):
        super().__init__(*args, **kwargs)
        if layout is not None:
            layout.addLayout(self)


class HBoxLayout(QtWidgets.QHBoxLayout):

    def __init__(self, *args, layout=None, **kwargs):
        super().__init__(*args, **kwargs)
        if layout is not None:
            layout.addLayout(self)


class LineEdit(QtWidgets.QLineEdit):
    Type = None
    Validator = None
    def __init__(self,
                 *args,
                 label=None,
                 default=None,
                 layout=None,
                 minw=40,
                 rng=(),
                 eFin=None,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default
        self.setMinimumWidth(minw)
        if not label:
            if layout is not None:
                layout.addWidget(self)
            return
        hlayout = HBoxLayout(layout=layout)
        lb = QtWidgets.QLabel(label)
        hlayout.addWidget(lb)
        hlayout.addWidget(self)
        self.reset()
        if eFin:
            self.editingFinished.connect(eFin)
        if self.Validator:
            self.setValidator(self.Validator(*rng))

    def reset(self):
        if self.default is not None:
            self.setText(self.default)

    @property
    def value(self):
        txt = self.text()
        if self.Type is not None:
            txt = self.Type(self.text())
        return txt

class ILineEdit(LineEdit):
    Type = int
    Validator = QtGui.QIntValidator

class FLineEdit(LineEdit):
    Type = float
    Validator = QtGui.QDoubleValidator


class FigureCanvas(backend_qtagg.FigureCanvas):

    def __init__(self, *args, msize=None, layout=None, parent=None, **kwargs):
        super().__init__(*args, **kwargs)
        if msize is not None:
            self.setMinimumWidth(msize[0])
            self.setMinimumHeight(msize[1])
        if layout is not None:
            layout.addWidget(self)
        if parent is None:
            return
        toolbar = backend_qtagg.NavigationToolbar2QT(self, parent)
        toolbar.setIconSize(QtCore.QSize(20, 20))
        if layout is not None:
            layout.addWidget(toolbar)
