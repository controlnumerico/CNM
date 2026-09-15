# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'float_keyboard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLayout, QSizePolicy, QVBoxLayout, QWidget)

from qtpyvcp.widgets.virtual_keyboards.vkb_key import VKBKey
import probe_basic_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.resize(320, 400)
        Dialog.setFocusPolicy(Qt.NoFocus)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(320, 400))
        self.frame.setMaximumSize(QSize(320, 400))
        self.frame.setStyleSheet(u"QFrame{\n"
"    border-style: solid;\n"
"    border-width: 4px;\n"
"    border-color: rgb(65, 84, 255);\n"
"    border-radius: 0px;\n"
"    background: rgb(216, 217, 218);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.np7 = VKBKey(self.frame)
        self.np7.setObjectName(u"np7")
        sizePolicy.setHeightForWidth(self.np7.sizePolicy().hasHeightForWidth())
        self.np7.setSizePolicy(sizePolicy)
        self.np7.setMinimumSize(QSize(60, 60))
        self.np7.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setFamilies([u"Probe Basic Bebas Mono"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.np7.setFont(font)
        self.np7.setFocusPolicy(Qt.NoFocus)
        self.np7.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.np7)

        self.np8 = VKBKey(self.frame)
        self.np8.setObjectName(u"np8")
        sizePolicy.setHeightForWidth(self.np8.sizePolicy().hasHeightForWidth())
        self.np8.setSizePolicy(sizePolicy)
        self.np8.setMinimumSize(QSize(60, 60))
        self.np8.setMaximumSize(QSize(60, 60))
        self.np8.setFont(font)
        self.np8.setFocusPolicy(Qt.NoFocus)
        self.np8.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.np8)

        self.np9 = VKBKey(self.frame)
        self.np9.setObjectName(u"np9")
        sizePolicy.setHeightForWidth(self.np9.sizePolicy().hasHeightForWidth())
        self.np9.setSizePolicy(sizePolicy)
        self.np9.setMinimumSize(QSize(60, 60))
        self.np9.setMaximumSize(QSize(60, 60))
        self.np9.setFont(font)
        self.np9.setFocusPolicy(Qt.NoFocus)
        self.np9.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.np9)

        self.esc = VKBKey(self.frame)
        self.esc.setObjectName(u"esc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.esc.sizePolicy().hasHeightForWidth())
        self.esc.setSizePolicy(sizePolicy1)
        self.esc.setMinimumSize(QSize(60, 60))
        self.esc.setSizeIncrement(QSize(0, 0))
        self.esc.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Probe Basic Bebas Mono"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.esc.setFont(font1)
        self.esc.setFocusPolicy(Qt.NoFocus)
        self.esc.setStyleSheet(u"font: 14pt \"Probe Basic Bebas Mono\";")

        self.horizontalLayout_2.addWidget(self.esc)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.np4 = VKBKey(self.frame)
        self.np4.setObjectName(u"np4")
        sizePolicy.setHeightForWidth(self.np4.sizePolicy().hasHeightForWidth())
        self.np4.setSizePolicy(sizePolicy)
        self.np4.setMinimumSize(QSize(60, 60))
        self.np4.setMaximumSize(QSize(60, 60))
        self.np4.setFont(font)
        self.np4.setFocusPolicy(Qt.NoFocus)
        self.np4.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.np4)

        self.np5 = VKBKey(self.frame)
        self.np5.setObjectName(u"np5")
        sizePolicy.setHeightForWidth(self.np5.sizePolicy().hasHeightForWidth())
        self.np5.setSizePolicy(sizePolicy)
        self.np5.setMinimumSize(QSize(60, 60))
        self.np5.setMaximumSize(QSize(60, 60))
        self.np5.setFont(font)
        self.np5.setFocusPolicy(Qt.NoFocus)
        self.np5.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.np5)

        self.np6 = VKBKey(self.frame)
        self.np6.setObjectName(u"np6")
        sizePolicy.setHeightForWidth(self.np6.sizePolicy().hasHeightForWidth())
        self.np6.setSizePolicy(sizePolicy)
        self.np6.setMinimumSize(QSize(60, 60))
        self.np6.setMaximumSize(QSize(60, 60))
        self.np6.setFont(font)
        self.np6.setFocusPolicy(Qt.NoFocus)
        self.np6.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.np6)

        self.left_arrow = VKBKey(self.frame)
        self.left_arrow.setObjectName(u"left_arrow")
        sizePolicy1.setHeightForWidth(self.left_arrow.sizePolicy().hasHeightForWidth())
        self.left_arrow.setSizePolicy(sizePolicy1)
        self.left_arrow.setMinimumSize(QSize(60, 60))
        font2 = QFont()
        font2.setFamilies([u"Probe Basic Bebas Mono"])
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setItalic(False)
        self.left_arrow.setFont(font2)
        self.left_arrow.setFocusPolicy(Qt.NoFocus)
        self.left_arrow.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/left_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.left_arrow.setIcon(icon)
        self.left_arrow.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.left_arrow)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.np1 = VKBKey(self.frame)
        self.np1.setObjectName(u"np1")
        sizePolicy.setHeightForWidth(self.np1.sizePolicy().hasHeightForWidth())
        self.np1.setSizePolicy(sizePolicy)
        self.np1.setMinimumSize(QSize(60, 60))
        self.np1.setMaximumSize(QSize(60, 60))
        self.np1.setFont(font)
        self.np1.setFocusPolicy(Qt.NoFocus)
        self.np1.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.np1)

        self.np2 = VKBKey(self.frame)
        self.np2.setObjectName(u"np2")
        sizePolicy.setHeightForWidth(self.np2.sizePolicy().hasHeightForWidth())
        self.np2.setSizePolicy(sizePolicy)
        self.np2.setMinimumSize(QSize(60, 60))
        self.np2.setMaximumSize(QSize(60, 60))
        self.np2.setFont(font)
        self.np2.setFocusPolicy(Qt.NoFocus)
        self.np2.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.np2)

        self.np3 = VKBKey(self.frame)
        self.np3.setObjectName(u"np3")
        sizePolicy.setHeightForWidth(self.np3.sizePolicy().hasHeightForWidth())
        self.np3.setSizePolicy(sizePolicy)
        self.np3.setMinimumSize(QSize(60, 60))
        self.np3.setMaximumSize(QSize(60, 60))
        self.np3.setFont(font)
        self.np3.setFocusPolicy(Qt.NoFocus)
        self.np3.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.np3)

        self.right_arrow = VKBKey(self.frame)
        self.right_arrow.setObjectName(u"right_arrow")
        sizePolicy1.setHeightForWidth(self.right_arrow.sizePolicy().hasHeightForWidth())
        self.right_arrow.setSizePolicy(sizePolicy1)
        self.right_arrow.setMinimumSize(QSize(60, 60))
        self.right_arrow.setFont(font2)
        self.right_arrow.setFocusPolicy(Qt.NoFocus)
        self.right_arrow.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/right_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.right_arrow.setIcon(icon1)
        self.right_arrow.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.right_arrow)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.dlt = VKBKey(self.frame)
        self.dlt.setObjectName(u"dlt")
        sizePolicy.setHeightForWidth(self.dlt.sizePolicy().hasHeightForWidth())
        self.dlt.setSizePolicy(sizePolicy)
        self.dlt.setMinimumSize(QSize(60, 60))
        self.dlt.setMaximumSize(QSize(60, 60))
        self.dlt.setSizeIncrement(QSize(0, 0))
        self.dlt.setBaseSize(QSize(0, 0))
        self.dlt.setFont(font1)
        self.dlt.setFocusPolicy(Qt.NoFocus)
        self.dlt.setStyleSheet(u"font: 14pt \"Probe Basic Bebas Mono\";")

        self.horizontalLayout_5.addWidget(self.dlt)

        self.np0 = VKBKey(self.frame)
        self.np0.setObjectName(u"np0")
        sizePolicy.setHeightForWidth(self.np0.sizePolicy().hasHeightForWidth())
        self.np0.setSizePolicy(sizePolicy)
        self.np0.setMinimumSize(QSize(60, 60))
        self.np0.setMaximumSize(QSize(60, 60))
        self.np0.setFont(font)
        self.np0.setFocusPolicy(Qt.NoFocus)
        self.np0.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.np0)

        self.decimal = VKBKey(self.frame)
        self.decimal.setObjectName(u"decimal")
        sizePolicy.setHeightForWidth(self.decimal.sizePolicy().hasHeightForWidth())
        self.decimal.setSizePolicy(sizePolicy)
        self.decimal.setMinimumSize(QSize(60, 60))
        self.decimal.setMaximumSize(QSize(60, 60))
        font3 = QFont()
        font3.setFamilies([u"Probe Basic Bebas Mono"])
        font3.setPointSize(20)
        self.decimal.setFont(font3)
        self.decimal.setFocusPolicy(Qt.NoFocus)
        self.decimal.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.decimal)

        self.backspace = VKBKey(self.frame)
        self.backspace.setObjectName(u"backspace")
        sizePolicy1.setHeightForWidth(self.backspace.sizePolicy().hasHeightForWidth())
        self.backspace.setSizePolicy(sizePolicy1)
        self.backspace.setMinimumSize(QSize(60, 60))
        self.backspace.setFont(font3)
        self.backspace.setFocusPolicy(Qt.NoFocus)
        self.backspace.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/images/backspace.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backspace.setIcon(icon2)
        self.backspace.setIconSize(QSize(45, 45))
        self.backspace.setAutoRepeat(True)

        self.horizontalLayout_5.addWidget(self.backspace)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.select_all = VKBKey(self.frame)
        self.select_all.setObjectName(u"select_all")
        sizePolicy1.setHeightForWidth(self.select_all.sizePolicy().hasHeightForWidth())
        self.select_all.setSizePolicy(sizePolicy1)
        self.select_all.setMinimumSize(QSize(60, 60))
        self.select_all.setSizeIncrement(QSize(0, 0))
        self.select_all.setBaseSize(QSize(0, 0))
        self.select_all.setFont(font1)
        self.select_all.setFocusPolicy(Qt.NoFocus)
        self.select_all.setStyleSheet(u"font: 14pt \"Probe Basic Bebas Mono\";")

        self.horizontalLayout_6.addWidget(self.select_all)

        self.enter = VKBKey(self.frame)
        self.enter.setObjectName(u"enter")
        sizePolicy1.setHeightForWidth(self.enter.sizePolicy().hasHeightForWidth())
        self.enter.setSizePolicy(sizePolicy1)
        self.enter.setMinimumSize(QSize(127, 60))
        self.enter.setFont(font1)
        self.enter.setFocusPolicy(Qt.NoFocus)
        self.enter.setStyleSheet(u"font: 14pt \"Probe Basic Bebas Mono\";")

        self.horizontalLayout_6.addWidget(self.enter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.np7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.np7.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.np8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.np8.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.np9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.np9.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.esc.setText(QCoreApplication.translate("Dialog", u"ESC", None))
        self.esc.setProperty(u"key", QCoreApplication.translate("Dialog", u"Esc", None))
        self.np4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.np4.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.np5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.np5.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.np6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.np6.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.left_arrow.setText("")
        self.left_arrow.setProperty(u"key", QCoreApplication.translate("Dialog", u"Left", None))
        self.left_arrow.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"blue_white", None))
        self.np1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.np1.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.np2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.np2.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.np3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.np3.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.right_arrow.setText("")
        self.right_arrow.setProperty(u"key", QCoreApplication.translate("Dialog", u"Right", None))
        self.right_arrow.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"blue_white", None))
        self.dlt.setText(QCoreApplication.translate("Dialog", u"DEL", None))
        self.dlt.setProperty(u"key", QCoreApplication.translate("Dialog", u"Del", None))
        self.np0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.np0.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.decimal.setText(QCoreApplication.translate("Dialog", u".", None))
        self.backspace.setText("")
        self.backspace.setProperty(u"key", QCoreApplication.translate("Dialog", u"Backspace", None))
        self.select_all.setText(QCoreApplication.translate("Dialog", u"SELECT ALL", None))
        self.select_all.setProperty(u"key", QCoreApplication.translate("Dialog", u"Ctrl+A", None))
        self.enter.setText(QCoreApplication.translate("Dialog", u"ENTER", None))
        self.enter.setProperty(u"key", QCoreApplication.translate("Dialog", u"Return", None))
    # retranslateUi

