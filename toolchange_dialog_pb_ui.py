# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toolchange_dialog_pb.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        Dialog.resize(421, 284)
        Dialog.setModal(True)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u".QFrame {\n"
"    color: white;\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
".QLabel {\n"
"    color: white;\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 18pt;    \n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.lblToolRemark = QLabel(self.frame)
        self.lblToolRemark.setObjectName(u"lblToolRemark")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblToolRemark.sizePolicy().hasHeightForWidth())
        self.lblToolRemark.setSizePolicy(sizePolicy)
        self.lblToolRemark.setMinimumSize(QSize(0, 60))
        self.lblToolRemark.setFrameShape(QFrame.Shape.Box)
        self.lblToolRemark.setFrameShadow(QFrame.Shadow.Plain)
        self.lblToolRemark.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.lblToolRemark, 3, 1, 1, 2)

        self.label_1 = QLabel(self.frame)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setFamilies([u"Probe Basic Bebas Mono"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.label_1.setFont(font)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)

        self.lblToolNumber = QLabel(self.frame)
        self.lblToolNumber.setObjectName(u"lblToolNumber")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblToolNumber.sizePolicy().hasHeightForWidth())
        self.lblToolNumber.setSizePolicy(sizePolicy1)
        self.lblToolNumber.setMinimumSize(QSize(80, 50))
        self.lblToolNumber.setMaximumSize(QSize(100, 16777215))
        self.lblToolNumber.setFont(font)
        self.lblToolNumber.setStyleSheet(u"")
        self.lblToolNumber.setFrameShape(QFrame.Shape.Box)
        self.lblToolNumber.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lblToolNumber, 0, 2, 1, 1)

        self.btnDone = QPushButton(self.frame)
        self.btnDone.setObjectName(u"btnDone")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnDone.sizePolicy().hasHeightForWidth())
        self.btnDone.setSizePolicy(sizePolicy2)
        self.btnDone.setMinimumSize(QSize(0, 55))
        self.btnDone.setMaximumSize(QSize(16777215, 55))
        self.btnDone.setStyleSheet(u"font: 75 17pt \"Probe Basic Bebas Mono\";")

        self.gridLayout.addWidget(self.btnDone, 4, 1, 1, 2)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)
        self.btnDone.clicked.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Manual Tool Change", None))
        self.lblToolRemark.setText(QCoreApplication.translate("Dialog", u"Remarks", None))
        self.lblToolRemark.setProperty(u"styleSet", QCoreApplication.translate("Dialog", u"dataField17", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"Tool Change Requested, Insert tool", None))
        self.lblToolNumber.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.lblToolNumber.setProperty(u"styleSet", QCoreApplication.translate("Dialog", u"dataField17", None))
        self.btnDone.setText(QCoreApplication.translate("Dialog", u"ONCE TOOL IS LOADED - PRESS TO RESUME", None))
    # retranslateUi

