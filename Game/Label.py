# Does not work for now

# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class LabelDialog(object):
#     def __init__(self, dialog, label_text):
#         self.Dialog = dialog
#         self.label_txt = label_text
#         self.button = QtWidgets.QPushButton(dialog)
#         self.label = QtWidgets.QLabel(dialog)
#         self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
#         self.label_txt = label_text
#
#     def setupUi(self):
#         self.Dialog.setObjectName("Message")
#         self.Dialog.resize(200, 100)
#         self.buttonBox.setGeometry(QtCore.QRect(10, 270, 221, 41))
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName("buttonBox")
#         self.label.setGeometry(QtCore.QRect(0, 0, 201, 101))
#         self.label.setScaledContents(False)
#         self.label.setAlignment(QtCore.Qt.AlignCenter)
#         self.label.setWordWrap(False)
#         self.label.setObjectName("label")
#         self.button.setGeometry(QtCore.QRect(119, 72, 71, 21))
#         self.button.setObjectName("button")
#
#         self.retranslateUi()
#         self.buttonBox.accepted.connect(self.Dialog.accept)
#         self.buttonBox.rejected.connect(self.Dialog.reject)
#         QtCore.QMetaObject.connectSlotsByName(self.Dialog)
#
#     def retranslateUi(self):
#         _translate = QtCore.QCoreApplication.translate
#         self.Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         self.label.setText(_translate("Dialog", self.label_txt))
#         self.button.setText(_translate("Dialog", self.label_txt))
#
#
# def label_win():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     dialog = QtWidgets.QDialog()
#     ui = LabelDialog(dialog, 'HAI VINTO!')
#     ui.setupUi()
#     dialog.show()
#     sys.exit(app.exec_())
#
#
# def label_lose():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     dialog = QtWidgets.QDialog()
#     ui = LabelDialog(dialog, 'HAI PERSO!')
#     ui.setupUi()
#     dialog.show()
#     sys.exit(app.exec_())
