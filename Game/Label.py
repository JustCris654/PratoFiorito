from PyQt5 import QtCore, QtGui, QtWidgets


class LabelDialog(object):
    def setupUi(self, Dialog, label_text):
        self.label_txt = label_text
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 100)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 270, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 201, 101))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.button = QtWidgets.QPushButton(Dialog)
        self.button.setGeometry(QtCore.QRect(119, 72, 71, 21))
        self.button.setObjectName("button")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", self.label_txt))
        self.button.setText(_translate("Dialog", self.label_txt))


def label_win():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LabelDialog()
    ui.setupUi(Dialog, 'HAI VINTO!')
    Dialog.show()
    sys.exit(app.exec_())


def label_lose():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LabelDialog()
    ui.setupUi(Dialog, 'HAI PERSO!')
    Dialog.show()
    sys.exit(app.exec_())
