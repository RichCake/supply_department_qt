# Form implementation generated from reading ui file '/Users/arsenijkarpov/Documents/Колледж/3 курс/Курсовые/project/interfaces/user_registry_widget.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_User_registry(object):
    def setupUi(self, User_registry):
        User_registry.setObjectName("User_registry")
        User_registry.resize(534, 381)
        self.verticalLayout = QtWidgets.QVBoxLayout(User_registry)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.refresh_btn = QtWidgets.QPushButton(parent=User_registry)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout.addWidget(self.refresh_btn)
        self.create_btn = QtWidgets.QPushButton(parent=User_registry)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout.addWidget(self.create_btn)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.close_btn = QtWidgets.QPushButton(parent=User_registry)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.user_list = QtWidgets.QTableView(parent=User_registry)
        self.user_list.setObjectName("user_list")
        self.verticalLayout.addWidget(self.user_list)

        self.retranslateUi(User_registry)
        QtCore.QMetaObject.connectSlotsByName(User_registry)

    def retranslateUi(self, User_registry):
        _translate = QtCore.QCoreApplication.translate
        User_registry.setWindowTitle(_translate("User_registry", "Form"))
        self.refresh_btn.setText(_translate("User_registry", "Обновить"))
        self.create_btn.setText(_translate("User_registry", "Создать"))
        self.close_btn.setText(_translate("User_registry", "Закрыть"))
