# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'l:\interfaces\usuario.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_creacion_usuario(object):
    def setupUi(self, creacion_usuario):
        creacion_usuario.setObjectName("creacion_usuario")
        creacion_usuario.resize(400, 126)
        self.lineEdit = QtWidgets.QLineEdit(creacion_usuario)
        self.lineEdit.setGeometry(QtCore.QRect(152, 30, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(creacion_usuario)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 60, 201, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btn_guardar = QtWidgets.QPushButton(creacion_usuario)
        self.btn_guardar.setGeometry(QtCore.QRect(150, 90, 75, 23))
        self.btn_guardar.setObjectName("btn_guardar")
        self.label = QtWidgets.QLabel(creacion_usuario)
        self.label.setGeometry(QtCore.QRect(70, 30, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(creacion_usuario)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.btn_cancelar = QtWidgets.QPushButton(creacion_usuario)
        self.btn_cancelar.setGeometry(QtCore.QRect(280, 90, 75, 23))
        self.btn_cancelar.setObjectName("btn_cancelar")

        self.retranslateUi(creacion_usuario)
        QtCore.QMetaObject.connectSlotsByName(creacion_usuario)

    def retranslateUi(self, creacion_usuario):
        _translate = QtCore.QCoreApplication.translate
        creacion_usuario.setWindowTitle(_translate("creacion_usuario", "Crear Usuario"))
        self.btn_guardar.setText(_translate("creacion_usuario", "Guardar"))
        self.label.setText(_translate("creacion_usuario", "Usuario"))
        self.label_2.setText(_translate("creacion_usuario", "Contraseña"))
        self.btn_cancelar.setText(_translate("creacion_usuario", "Cancelar"))

