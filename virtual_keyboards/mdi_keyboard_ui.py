# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mdi_keyboard.ui'
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
    QLayout, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

from qtpyvcp.widgets.virtual_keyboards.vkb_key import VKBKey
import probe_basic_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.resize(470, 520)
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
        self.frame.setMinimumSize(QSize(470, 520))
        self.frame.setMaximumSize(QSize(470, 520))
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
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 45))
        self.lineEdit.setMaximumSize(QSize(16777215, 45))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.G = VKBKey(self.frame)
        self.G.setObjectName(u"G")
        sizePolicy.setHeightForWidth(self.G.sizePolicy().hasHeightForWidth())
        self.G.setSizePolicy(sizePolicy)
        self.G.setMinimumSize(QSize(60, 60))
        self.G.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setFamilies([u"Probe Basic Bebas Mono"])
        font.setPointSize(15)
        self.G.setFont(font)
        self.G.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.G)

        self.X = VKBKey(self.frame)
        self.X.setObjectName(u"X")
        sizePolicy.setHeightForWidth(self.X.sizePolicy().hasHeightForWidth())
        self.X.setSizePolicy(sizePolicy)
        self.X.setMinimumSize(QSize(60, 60))
        self.X.setMaximumSize(QSize(60, 60))
        self.X.setFont(font)
        self.X.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.X)

        self.NP7 = VKBKey(self.frame)
        self.NP7.setObjectName(u"NP7")
        sizePolicy.setHeightForWidth(self.NP7.sizePolicy().hasHeightForWidth())
        self.NP7.setSizePolicy(sizePolicy)
        self.NP7.setMinimumSize(QSize(60, 60))
        self.NP7.setMaximumSize(QSize(60, 60))
        font1 = QFont()
        font1.setFamilies([u"Probe Basic Bebas Mono"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.NP7.setFont(font1)
        self.NP7.setFocusPolicy(Qt.NoFocus)
        self.NP7.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.NP7)

        self.NP8 = VKBKey(self.frame)
        self.NP8.setObjectName(u"NP8")
        sizePolicy.setHeightForWidth(self.NP8.sizePolicy().hasHeightForWidth())
        self.NP8.setSizePolicy(sizePolicy)
        self.NP8.setMinimumSize(QSize(60, 60))
        self.NP8.setMaximumSize(QSize(60, 60))
        self.NP8.setFont(font1)
        self.NP8.setFocusPolicy(Qt.NoFocus)
        self.NP8.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.NP8)

        self.NP9 = VKBKey(self.frame)
        self.NP9.setObjectName(u"NP9")
        sizePolicy.setHeightForWidth(self.NP9.sizePolicy().hasHeightForWidth())
        self.NP9.setSizePolicy(sizePolicy)
        self.NP9.setMinimumSize(QSize(60, 60))
        self.NP9.setMaximumSize(QSize(60, 60))
        self.NP9.setFont(font1)
        self.NP9.setFocusPolicy(Qt.NoFocus)
        self.NP9.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.NP9)

        self.divide = VKBKey(self.frame)
        self.divide.setObjectName(u"divide")
        sizePolicy.setHeightForWidth(self.divide.sizePolicy().hasHeightForWidth())
        self.divide.setSizePolicy(sizePolicy)
        self.divide.setMinimumSize(QSize(60, 60))
        self.divide.setMaximumSize(QSize(60, 60))
        self.divide.setFont(font1)
        self.divide.setFocusPolicy(Qt.NoFocus)
        self.divide.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.divide)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.T = VKBKey(self.frame)
        self.T.setObjectName(u"T")
        sizePolicy.setHeightForWidth(self.T.sizePolicy().hasHeightForWidth())
        self.T.setSizePolicy(sizePolicy)
        self.T.setMinimumSize(QSize(60, 60))
        self.T.setMaximumSize(QSize(60, 60))
        self.T.setFont(font)
        self.T.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.T)

        self.Y = VKBKey(self.frame)
        self.Y.setObjectName(u"Y")
        sizePolicy.setHeightForWidth(self.Y.sizePolicy().hasHeightForWidth())
        self.Y.setSizePolicy(sizePolicy)
        self.Y.setMinimumSize(QSize(60, 60))
        self.Y.setMaximumSize(QSize(60, 60))
        self.Y.setFont(font)
        self.Y.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.Y)

        self.NP4 = VKBKey(self.frame)
        self.NP4.setObjectName(u"NP4")
        sizePolicy.setHeightForWidth(self.NP4.sizePolicy().hasHeightForWidth())
        self.NP4.setSizePolicy(sizePolicy)
        self.NP4.setMinimumSize(QSize(60, 60))
        self.NP4.setMaximumSize(QSize(60, 60))
        self.NP4.setFont(font1)
        self.NP4.setFocusPolicy(Qt.NoFocus)
        self.NP4.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.NP4)

        self.NP5 = VKBKey(self.frame)
        self.NP5.setObjectName(u"NP5")
        sizePolicy.setHeightForWidth(self.NP5.sizePolicy().hasHeightForWidth())
        self.NP5.setSizePolicy(sizePolicy)
        self.NP5.setMinimumSize(QSize(60, 60))
        self.NP5.setMaximumSize(QSize(60, 60))
        self.NP5.setFont(font1)
        self.NP5.setFocusPolicy(Qt.NoFocus)
        self.NP5.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.NP5)

        self.NP6 = VKBKey(self.frame)
        self.NP6.setObjectName(u"NP6")
        sizePolicy.setHeightForWidth(self.NP6.sizePolicy().hasHeightForWidth())
        self.NP6.setSizePolicy(sizePolicy)
        self.NP6.setMinimumSize(QSize(60, 60))
        self.NP6.setMaximumSize(QSize(60, 60))
        self.NP6.setFont(font1)
        self.NP6.setFocusPolicy(Qt.NoFocus)
        self.NP6.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.NP6)

        self.multiply = VKBKey(self.frame)
        self.multiply.setObjectName(u"multiply")
        sizePolicy.setHeightForWidth(self.multiply.sizePolicy().hasHeightForWidth())
        self.multiply.setSizePolicy(sizePolicy)
        self.multiply.setMinimumSize(QSize(60, 60))
        self.multiply.setMaximumSize(QSize(60, 60))
        self.multiply.setFont(font1)
        self.multiply.setFocusPolicy(Qt.NoFocus)
        self.multiply.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.multiply)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.M = VKBKey(self.frame)
        self.M.setObjectName(u"M")
        sizePolicy.setHeightForWidth(self.M.sizePolicy().hasHeightForWidth())
        self.M.setSizePolicy(sizePolicy)
        self.M.setMinimumSize(QSize(60, 60))
        self.M.setMaximumSize(QSize(60, 60))
        self.M.setFont(font)
        self.M.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.M)

        self.Z = VKBKey(self.frame)
        self.Z.setObjectName(u"Z")
        sizePolicy.setHeightForWidth(self.Z.sizePolicy().hasHeightForWidth())
        self.Z.setSizePolicy(sizePolicy)
        self.Z.setMinimumSize(QSize(60, 60))
        self.Z.setMaximumSize(QSize(60, 60))
        self.Z.setFont(font)
        self.Z.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.Z)

        self.NP1 = VKBKey(self.frame)
        self.NP1.setObjectName(u"NP1")
        sizePolicy.setHeightForWidth(self.NP1.sizePolicy().hasHeightForWidth())
        self.NP1.setSizePolicy(sizePolicy)
        self.NP1.setMinimumSize(QSize(60, 60))
        self.NP1.setMaximumSize(QSize(60, 60))
        self.NP1.setFont(font1)
        self.NP1.setFocusPolicy(Qt.NoFocus)
        self.NP1.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.NP1)

        self.NP2 = VKBKey(self.frame)
        self.NP2.setObjectName(u"NP2")
        sizePolicy.setHeightForWidth(self.NP2.sizePolicy().hasHeightForWidth())
        self.NP2.setSizePolicy(sizePolicy)
        self.NP2.setMinimumSize(QSize(60, 60))
        self.NP2.setMaximumSize(QSize(60, 60))
        self.NP2.setFont(font1)
        self.NP2.setFocusPolicy(Qt.NoFocus)
        self.NP2.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.NP2)

        self.NP3 = VKBKey(self.frame)
        self.NP3.setObjectName(u"NP3")
        sizePolicy.setHeightForWidth(self.NP3.sizePolicy().hasHeightForWidth())
        self.NP3.setSizePolicy(sizePolicy)
        self.NP3.setMinimumSize(QSize(60, 60))
        self.NP3.setMaximumSize(QSize(60, 60))
        self.NP3.setFont(font1)
        self.NP3.setFocusPolicy(Qt.NoFocus)
        self.NP3.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.NP3)

        self.subtract = VKBKey(self.frame)
        self.subtract.setObjectName(u"subtract")
        sizePolicy.setHeightForWidth(self.subtract.sizePolicy().hasHeightForWidth())
        self.subtract.setSizePolicy(sizePolicy)
        self.subtract.setMinimumSize(QSize(60, 60))
        self.subtract.setMaximumSize(QSize(60, 60))
        self.subtract.setFont(font1)
        self.subtract.setFocusPolicy(Qt.NoFocus)
        self.subtract.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.subtract)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.S = VKBKey(self.frame)
        self.S.setObjectName(u"S")
        sizePolicy.setHeightForWidth(self.S.sizePolicy().hasHeightForWidth())
        self.S.setSizePolicy(sizePolicy)
        self.S.setMinimumSize(QSize(60, 60))
        self.S.setMaximumSize(QSize(60, 60))
        self.S.setFont(font)
        self.S.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_5.addWidget(self.S)

        self.A = VKBKey(self.frame)
        self.A.setObjectName(u"A")
        sizePolicy.setHeightForWidth(self.A.sizePolicy().hasHeightForWidth())
        self.A.setSizePolicy(sizePolicy)
        self.A.setMinimumSize(QSize(60, 60))
        self.A.setMaximumSize(QSize(60, 60))
        self.A.setFont(font)
        self.A.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_5.addWidget(self.A)

        self.decimal = VKBKey(self.frame)
        self.decimal.setObjectName(u"decimal")
        sizePolicy.setHeightForWidth(self.decimal.sizePolicy().hasHeightForWidth())
        self.decimal.setSizePolicy(sizePolicy)
        self.decimal.setMinimumSize(QSize(60, 60))
        self.decimal.setMaximumSize(QSize(60, 60))
        self.decimal.setFont(font)
        self.decimal.setFocusPolicy(Qt.NoFocus)
        self.decimal.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.decimal)

        self.NP0 = VKBKey(self.frame)
        self.NP0.setObjectName(u"NP0")
        sizePolicy.setHeightForWidth(self.NP0.sizePolicy().hasHeightForWidth())
        self.NP0.setSizePolicy(sizePolicy)
        self.NP0.setMinimumSize(QSize(60, 60))
        self.NP0.setMaximumSize(QSize(60, 60))
        self.NP0.setFont(font1)
        self.NP0.setFocusPolicy(Qt.NoFocus)
        self.NP0.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.NP0)

        self.space = VKBKey(self.frame)
        self.space.setObjectName(u"space")
        sizePolicy.setHeightForWidth(self.space.sizePolicy().hasHeightForWidth())
        self.space.setSizePolicy(sizePolicy)
        self.space.setMinimumSize(QSize(60, 60))
        self.space.setMaximumSize(QSize(60, 60))
        font2 = QFont()
        font2.setFamilies([u"Probe Basic Bebas Mono"])
        font2.setPointSize(17)
        font2.setBold(False)
        font2.setItalic(False)
        self.space.setFont(font2)
        self.space.setFocusPolicy(Qt.NoFocus)
        self.space.setStyleSheet(u"font: 17pt \"Probe Basic Bebas Mono\";")

        self.horizontalLayout_5.addWidget(self.space)

        self.add = VKBKey(self.frame)
        self.add.setObjectName(u"add")
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setMinimumSize(QSize(60, 60))
        self.add.setMaximumSize(QSize(60, 60))
        self.add.setFont(font1)
        self.add.setFocusPolicy(Qt.NoFocus)
        self.add.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.add)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.F = VKBKey(self.frame)
        self.F.setObjectName(u"F")
        sizePolicy.setHeightForWidth(self.F.sizePolicy().hasHeightForWidth())
        self.F.setSizePolicy(sizePolicy)
        self.F.setMinimumSize(QSize(60, 60))
        self.F.setMaximumSize(QSize(60, 60))
        self.F.setFont(font)
        self.F.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_6.addWidget(self.F)

        self.B = VKBKey(self.frame)
        self.B.setObjectName(u"B")
        sizePolicy.setHeightForWidth(self.B.sizePolicy().hasHeightForWidth())
        self.B.setSizePolicy(sizePolicy)
        self.B.setMinimumSize(QSize(60, 60))
        self.B.setMaximumSize(QSize(60, 60))
        self.B.setFont(font)
        self.B.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_6.addWidget(self.B)

        self.up_arrow = VKBKey(self.frame)
        self.up_arrow.setObjectName(u"up_arrow")
        sizePolicy.setHeightForWidth(self.up_arrow.sizePolicy().hasHeightForWidth())
        self.up_arrow.setSizePolicy(sizePolicy)
        self.up_arrow.setMinimumSize(QSize(60, 60))
        self.up_arrow.setMaximumSize(QSize(60, 60))
        font3 = QFont()
        font3.setFamilies([u"Probe Basic Bebas Mono"])
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        self.up_arrow.setFont(font3)
        self.up_arrow.setFocusPolicy(Qt.NoFocus)
        self.up_arrow.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/up_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.up_arrow.setIcon(icon)
        self.up_arrow.setIconSize(QSize(35, 35))

        self.horizontalLayout_6.addWidget(self.up_arrow)

        self.pushButton_20 = VKBKey(self.frame)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setMinimumSize(QSize(60, 60))
        self.pushButton_20.setMaximumSize(QSize(60, 60))
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setFocusPolicy(Qt.NoFocus)
        self.pushButton_20.setStyleSheet(u"font: 17pt \"Probe Basic Bebas Mono\";")

        self.horizontalLayout_6.addWidget(self.pushButton_20)

        self.backspace = VKBKey(self.frame)
        self.backspace.setObjectName(u"backspace")
        sizePolicy.setHeightForWidth(self.backspace.sizePolicy().hasHeightForWidth())
        self.backspace.setSizePolicy(sizePolicy)
        self.backspace.setMinimumSize(QSize(60, 60))
        self.backspace.setMaximumSize(QSize(60, 60))
        self.backspace.setFont(font)
        self.backspace.setFocusPolicy(Qt.NoFocus)
        self.backspace.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/backspace.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backspace.setIcon(icon1)
        self.backspace.setIconSize(QSize(45, 45))

        self.horizontalLayout_6.addWidget(self.backspace)

        self.dlt = VKBKey(self.frame)
        self.dlt.setObjectName(u"dlt")
        sizePolicy.setHeightForWidth(self.dlt.sizePolicy().hasHeightForWidth())
        self.dlt.setSizePolicy(sizePolicy)
        self.dlt.setMinimumSize(QSize(60, 60))
        self.dlt.setMaximumSize(QSize(60, 60))
        self.dlt.setSizeIncrement(QSize(0, 0))
        self.dlt.setBaseSize(QSize(0, 0))
        self.dlt.setFont(font2)
        self.dlt.setFocusPolicy(Qt.NoFocus)
        self.dlt.setStyleSheet(u"font: 17pt \"Probe Basic Bebas Mono\";")

        self.horizontalLayout_6.addWidget(self.dlt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.P = VKBKey(self.frame)
        self.P.setObjectName(u"P")
        sizePolicy.setHeightForWidth(self.P.sizePolicy().hasHeightForWidth())
        self.P.setSizePolicy(sizePolicy)
        self.P.setMinimumSize(QSize(60, 60))
        self.P.setMaximumSize(QSize(60, 60))
        self.P.setFont(font)
        self.P.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_7.addWidget(self.P)

        self.left_arrow = VKBKey(self.frame)
        self.left_arrow.setObjectName(u"left_arrow")
        sizePolicy.setHeightForWidth(self.left_arrow.sizePolicy().hasHeightForWidth())
        self.left_arrow.setSizePolicy(sizePolicy)
        self.left_arrow.setMinimumSize(QSize(60, 60))
        self.left_arrow.setMaximumSize(QSize(60, 60))
        self.left_arrow.setFont(font3)
        self.left_arrow.setFocusPolicy(Qt.NoFocus)
        self.left_arrow.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/images/left_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.left_arrow.setIcon(icon2)
        self.left_arrow.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.left_arrow)

        self.down_arrow = VKBKey(self.frame)
        self.down_arrow.setObjectName(u"down_arrow")
        sizePolicy.setHeightForWidth(self.down_arrow.sizePolicy().hasHeightForWidth())
        self.down_arrow.setSizePolicy(sizePolicy)
        self.down_arrow.setMinimumSize(QSize(60, 60))
        self.down_arrow.setMaximumSize(QSize(60, 60))
        self.down_arrow.setFont(font3)
        self.down_arrow.setFocusPolicy(Qt.NoFocus)
        self.down_arrow.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/images/down_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.down_arrow.setIcon(icon3)
        self.down_arrow.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.down_arrow)

        self.right_arrow = VKBKey(self.frame)
        self.right_arrow.setObjectName(u"right_arrow")
        sizePolicy.setHeightForWidth(self.right_arrow.sizePolicy().hasHeightForWidth())
        self.right_arrow.setSizePolicy(sizePolicy)
        self.right_arrow.setMinimumSize(QSize(60, 60))
        self.right_arrow.setMaximumSize(QSize(60, 60))
        self.right_arrow.setFont(font3)
        self.right_arrow.setFocusPolicy(Qt.NoFocus)
        self.right_arrow.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/images/right_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.right_arrow.setIcon(icon4)
        self.right_arrow.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.right_arrow)

        self.esc = VKBKey(self.frame)
        self.esc.setObjectName(u"esc")
        sizePolicy.setHeightForWidth(self.esc.sizePolicy().hasHeightForWidth())
        self.esc.setSizePolicy(sizePolicy)
        self.esc.setMinimumSize(QSize(60, 60))
        self.esc.setMaximumSize(QSize(60, 60))
        self.esc.setSizeIncrement(QSize(0, 0))
        self.esc.setBaseSize(QSize(0, 0))
        self.esc.setFont(font2)
        self.esc.setFocusPolicy(Qt.NoFocus)
        self.esc.setStyleSheet(u"font: 17pt \"Probe Basic Bebas Mono\";")

        self.horizontalLayout_7.addWidget(self.esc)

        self.enter = VKBKey(self.frame)
        self.enter.setObjectName(u"enter")
        sizePolicy.setHeightForWidth(self.enter.sizePolicy().hasHeightForWidth())
        self.enter.setSizePolicy(sizePolicy)
        self.enter.setMinimumSize(QSize(60, 60))
        self.enter.setMaximumSize(QSize(60, 60))
        self.enter.setFont(font2)
        self.enter.setFocusPolicy(Qt.NoFocus)
        self.enter.setStyleSheet(u"font: 17pt \"Probe Basic Bebas Mono\";")

        self.horizontalLayout_7.addWidget(self.enter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.G.setText(QCoreApplication.translate("Dialog", u"G", None))
        self.G.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.X.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.X.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.NP7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.NP7.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.NP8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.NP8.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.NP9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.NP9.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.divide.setText(QCoreApplication.translate("Dialog", u"/", None))
        self.divide.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"symbols", None))
        self.T.setText(QCoreApplication.translate("Dialog", u"T", None))
        self.T.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.Y.setText(QCoreApplication.translate("Dialog", u"Y", None))
        self.Y.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.NP4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.NP4.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.NP5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.NP5.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.NP6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.NP6.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.multiply.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.multiply.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"symbols", None))
        self.M.setText(QCoreApplication.translate("Dialog", u"M", None))
        self.M.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.Z.setText(QCoreApplication.translate("Dialog", u"Z", None))
        self.Z.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.NP1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.NP1.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.NP2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.NP2.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.NP3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.NP3.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.subtract.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.subtract.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"symbols", None))
        self.S.setText(QCoreApplication.translate("Dialog", u"S", None))
        self.S.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.A.setText(QCoreApplication.translate("Dialog", u"A", None))
        self.A.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.decimal.setText(QCoreApplication.translate("Dialog", u".", None))
        self.decimal.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.NP0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.NP0.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.space.setText(QCoreApplication.translate("Dialog", u"SPACE", None))
        self.space.setProperty(u"key", QCoreApplication.translate("Dialog", u"Space", None))
        self.space.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"light_white", None))
        self.add.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.add.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"symbols", None))
        self.F.setText(QCoreApplication.translate("Dialog", u"F", None))
        self.F.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.B.setText(QCoreApplication.translate("Dialog", u"B", None))
        self.B.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.up_arrow.setText("")
        self.up_arrow.setProperty(u"key", QCoreApplication.translate("Dialog", u"Up", None))
        self.up_arrow.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"blue_white", None))
        self.pushButton_20.setText(QCoreApplication.translate("Dialog", u"in/mm", None))
        self.pushButton_20.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.backspace.setText("")
        self.backspace.setProperty(u"key", QCoreApplication.translate("Dialog", u"Backspace", None))
        self.backspace.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.dlt.setText(QCoreApplication.translate("Dialog", u"DEL", None))
        self.dlt.setProperty(u"key", QCoreApplication.translate("Dialog", u"Del", None))
        self.dlt.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.P.setText(QCoreApplication.translate("Dialog", u"P", None))
        self.P.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.left_arrow.setText("")
        self.left_arrow.setProperty(u"key", QCoreApplication.translate("Dialog", u"Left", None))
        self.left_arrow.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"blue_white", None))
        self.down_arrow.setText("")
        self.down_arrow.setProperty(u"key", QCoreApplication.translate("Dialog", u"Down", None))
        self.down_arrow.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"blue_white", None))
        self.right_arrow.setText("")
        self.right_arrow.setProperty(u"key", QCoreApplication.translate("Dialog", u"Right", None))
        self.right_arrow.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"blue_white", None))
        self.esc.setText(QCoreApplication.translate("Dialog", u"ESC", None))
        self.esc.setProperty(u"key", QCoreApplication.translate("Dialog", u"Esc", None))
        self.esc.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
        self.enter.setText(QCoreApplication.translate("Dialog", u"ENTER", None))
        self.enter.setProperty(u"key", QCoreApplication.translate("Dialog", u"Return", None))
        self.enter.setProperty(u"buttonColorGroup", QCoreApplication.translate("Dialog", u"dark_grey", None))
    # retranslateUi

