# Set the level to play and the scaling of the sprites
from PyQt5 import QtWidgets, QtCore

LEVEL = None


class UiDialog(object):
    def __init__(self, Dialog):
        self.cb_selection = QtWidgets.QComboBox(Dialog)
        self.lbl_selection = QtWidgets.QLabel(Dialog)
        self.Dialog = Dialog
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)

    def setupUi(self):
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(240, 240)
        self.buttonBox.setGeometry(QtCore.QRect(10, 190, 221, 40))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lbl_selection.setGeometry(QtCore.QRect(0, 50, 241, 20))
        self.lbl_selection.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_selection.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_selection.setObjectName("lbl_selection")
        self.cb_selection.setGeometry(QtCore.QRect(60, 110, 120, 25))
        self.cb_selection.setObjectName("cb_selection")
        self.cb_selection.addItem("")
        self.cb_selection.addItem("")
        self.cb_selection.addItem("")
        self.retranslateUi(self.Dialog)
        self.buttonBox.rejected.connect(self.Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
        self.buttonBox.accepted.connect(self.save_status)

    def save_status(self):
        global LEVEL
        LEVEL = 1 if self.cb_selection.currentText() == 'Easy' else 2 if \
            self.cb_selection.currentText() == 'Medium' else 3
        self.Dialog.accept()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_selection.setText(_translate("Dialog", "Seleziona diffcoltà"))
        self.cb_selection.setItemText(0, _translate("Dialog", "Easy"))
        self.cb_selection.setItemText(1, _translate("Dialog", "Medium"))
        self.cb_selection.setItemText(2, _translate("Dialog", "Hard"))


def start_ui():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = UiDialog(dialog)
    ui.setupUi()
    dialog.show()
    app.exec_()
    return LEVEL
