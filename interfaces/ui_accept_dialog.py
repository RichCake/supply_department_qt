# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accept_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_Accept_dialog(object):
    def setupUi(self, Accept_dialog):
        if not Accept_dialog.objectName():
            Accept_dialog.setObjectName(u"Accept_dialog")
        Accept_dialog.resize(1055, 535)
        self.verticalLayout_2 = QVBoxLayout(Accept_dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(Accept_dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.type_combo_box = QComboBox(Accept_dialog)
        self.type_combo_box.addItem("")
        self.type_combo_box.addItem("")
        self.type_combo_box.setObjectName(u"type_combo_box")
        self.type_combo_box.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.type_combo_box)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.user_table = QTableView(Accept_dialog)
        self.user_table.setObjectName(u"user_table")

        self.horizontalLayout.addWidget(self.user_table)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.add_btn = QPushButton(Accept_dialog)
        self.add_btn.setObjectName(u"add_btn")

        self.verticalLayout.addWidget(self.add_btn)

        self.remove_btn = QPushButton(Accept_dialog)
        self.remove_btn.setObjectName(u"remove_btn")

        self.verticalLayout.addWidget(self.remove_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.accept_table = QTableView(Accept_dialog)
        self.accept_table.setObjectName(u"accept_table")

        self.horizontalLayout.addWidget(self.accept_table)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.up_btn = QPushButton(Accept_dialog)
        self.up_btn.setObjectName(u"up_btn")

        self.verticalLayout_3.addWidget(self.up_btn)

        self.down_btn = QPushButton(Accept_dialog)
        self.down_btn.setObjectName(u"down_btn")

        self.verticalLayout_3.addWidget(self.down_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Accept_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Accept_dialog)
        self.buttonBox.accepted.connect(Accept_dialog.accept)
        self.buttonBox.rejected.connect(Accept_dialog.reject)

        QMetaObject.connectSlotsByName(Accept_dialog)
    # setupUi

    def retranslateUi(self, Accept_dialog):
        Accept_dialog.setWindowTitle(QCoreApplication.translate("Accept_dialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u0441\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("Accept_dialog", u"\u0422\u0438\u043f \u0441\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.type_combo_box.setItemText(0, QCoreApplication.translate("Accept_dialog", u"\u0412\u0441\u0435\u043c \u0441\u0440\u0430\u0437\u0443", None))
        self.type_combo_box.setItemText(1, QCoreApplication.translate("Accept_dialog", u"\u041f\u043e \u043e\u0447\u0435\u0440\u0435\u0434\u0438", None))

        self.add_btn.setText(QCoreApplication.translate("Accept_dialog", u">", None))
        self.remove_btn.setText(QCoreApplication.translate("Accept_dialog", u"<", None))
        self.up_btn.setText(QCoreApplication.translate("Accept_dialog", u"/\\", None))
        self.down_btn.setText(QCoreApplication.translate("Accept_dialog", u"\\/", None))
    # retranslateUi

