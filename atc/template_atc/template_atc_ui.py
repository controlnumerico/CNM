# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_atc.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QScrollArea, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.input_widgets.line_edit import VCPLineEdit
from qtpyvcp.widgets.input_widgets.mdientry_widget import MDIEntry
from widgets import DynATC
import probe_basic_rc

class Ui_ATC(object):
    def setupUi(self, ATC):
        if not ATC.objectName():
            ATC.setObjectName(u"ATC")
        ATC.resize(1012, 588)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ATC.sizePolicy().hasHeightForWidth())
        ATC.setSizePolicy(sizePolicy)
        ATC.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(ATC)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 17, 0, 5)
        self.tabWidget_33 = QTabWidget(ATC)
        self.tabWidget_33.setObjectName(u"tabWidget_33")
        sizePolicy.setHeightForWidth(self.tabWidget_33.sizePolicy().hasHeightForWidth())
        self.tabWidget_33.setSizePolicy(sizePolicy)
        self.tabWidget_33.setStyleSheet(u"QTabWidget::pane {\n"
"    border: none;\n"
"}\n"
"\n"
"QTabWidget QTabBar::tab {\n"
"    min-width: 150px;\n"
"    min-height: 30px;\n"
"	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tabWidget_33.setTabPosition(QTabWidget.TabPosition.North)
        self.program_tools_tab = QWidget()
        self.program_tools_tab.setObjectName(u"program_tools_tab")
        self.verticalLayout = QVBoxLayout(self.program_tools_tab)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, 9, -1)
        self.frame_65 = QFrame(self.program_tools_tab)
        self.frame_65.setObjectName(u"frame_65")
        sizePolicy.setHeightForWidth(self.frame_65.sizePolicy().hasHeightForWidth())
        self.frame_65.setSizePolicy(sizePolicy)
        self.frame_65.setMinimumSize(QSize(300, 0))
        self.frame_65.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_65 = QVBoxLayout(self.frame_65)
        self.verticalLayout_65.setSpacing(16)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(20, 18, 20, 18)
        self.horizontalLayout_176 = QHBoxLayout()
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(2, 2, 2, 2)
        self.work_column_header_7 = QLabel(self.frame_65)
        self.work_column_header_7.setObjectName(u"work_column_header_7")
        self.work_column_header_7.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.work_column_header_7.sizePolicy().hasHeightForWidth())
        self.work_column_header_7.setSizePolicy(sizePolicy1)
        self.work_column_header_7.setMinimumSize(QSize(0, 38))
        self.work_column_header_7.setMaximumSize(QSize(16777215, 38))
        self.work_column_header_7.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.work_column_header_7.setFrameShape(QFrame.Shape.NoFrame)
        self.work_column_header_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.work_column_header_7.setWordWrap(True)
        self.work_column_header_7.setIndent(0)

        self.horizontalLayout_176.addWidget(self.work_column_header_7)


        self.verticalLayout_65.addLayout(self.horizontalLayout_176)

        self.scrollArea = QScrollArea(self.frame_65)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 256, 294))
        self.verticalLayout_70 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy2)
        self.widget_6.setAutoFillBackground(False)
        self.widget_6.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_33.setSpacing(20)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(30, 6, 0, 0)
        self.tools_check_list = StatusLabel(self.widget_6)
        self.tools_check_list.setObjectName(u"tools_check_list")
        sizePolicy2.setHeightForWidth(self.tools_check_list.sizePolicy().hasHeightForWidth())
        self.tools_check_list.setSizePolicy(sizePolicy2)
        self.tools_check_list.setStyleSheet(u"QLabel {\n"
"    font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tools_check_list.setLineWidth(3)
        self.tools_check_list.setMidLineWidth(2)
        self.tools_check_list.setTextFormat(Qt.TextFormat.AutoText)
        self.tools_check_list.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.tools_check_list.setWordWrap(True)

        self.horizontalLayout_33.addWidget(self.tools_check_list)


        self.verticalLayout_70.addWidget(self.widget_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_65.addWidget(self.scrollArea)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setSpacing(15)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(2, 2, 2, 2)
        self.reference_carousel_2 = MDIButton(self.frame_65)
        self.reference_carousel_2.setObjectName(u"reference_carousel_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.reference_carousel_2.sizePolicy().hasHeightForWidth())
        self.reference_carousel_2.setSizePolicy(sizePolicy3)
        self.reference_carousel_2.setMinimumSize(QSize(125, 45))
        self.reference_carousel_2.setMaximumSize(QSize(16777215, 45))
        self.reference_carousel_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.reference_carousel_2.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.reference_carousel_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_159.addWidget(self.reference_carousel_2)


        self.verticalLayout_65.addLayout(self.horizontalLayout_159)


        self.verticalLayout.addWidget(self.frame_65)

        self.tabWidget_33.addTab(self.program_tools_tab, "")
        self.manual_atc_tab = QWidget()
        self.manual_atc_tab.setObjectName(u"manual_atc_tab")
        self.verticalLayout_2 = QVBoxLayout(self.manual_atc_tab)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, 9, -1)
        self.user_atc_buttons_layout = QVBoxLayout()
        self.user_atc_buttons_layout.setSpacing(0)
        self.user_atc_buttons_layout.setObjectName(u"user_atc_buttons_layout")

        self.verticalLayout_2.addLayout(self.user_atc_buttons_layout)

        self.tabWidget_33.addTab(self.manual_atc_tab, "")

        self.verticalLayout_7.addWidget(self.tabWidget_33)

        self.mdi_entry_box_3 = MDIEntry(ATC)
        self.mdi_entry_box_3.setObjectName(u"mdi_entry_box_3")
        sizePolicy1.setHeightForWidth(self.mdi_entry_box_3.sizePolicy().hasHeightForWidth())
        self.mdi_entry_box_3.setSizePolicy(sizePolicy1)
        self.mdi_entry_box_3.setMinimumSize(QSize(0, 40))
        self.mdi_entry_box_3.setMaximumSize(QSize(320, 40))
        font = QFont()
        font.setFamilies([u"Probe Basic Bebas Mono"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.mdi_entry_box_3.setFont(font)
        self.mdi_entry_box_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_7.addWidget(self.mdi_entry_box_3)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setSpacing(0)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.dynatc = DynATC(ATC)
        self.dynatc.setObjectName(u"dynatc")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.dynatc.sizePolicy().hasHeightForWidth())
        self.dynatc.setSizePolicy(sizePolicy4)
        self.dynatc.setProperty(u"backgroundColor", QColor(146, 150, 149))

        self.horizontalLayout_127.addWidget(self.dynatc)


        self.horizontalLayout.addLayout(self.horizontalLayout_127)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.widget_21 = QWidget(ATC)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy5)
        self.widget_21.setMinimumSize(QSize(350, 0))
        self.widget_21.setMaximumSize(QSize(350, 16777215))
        self.widget_21.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.widget_21)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 12, 0, 20)
        self.frame_40 = QFrame(self.widget_21)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy6)
        self.frame_40.setMinimumSize(QSize(0, 60))
        self.frame_40.setStyleSheet(u".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"    border-radius: 7px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"}")
        self.horizontalLayout_132 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setSpacing(3)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.tool_length_10 = StatusLabel(self.frame_40)
        self.tool_length_10.setObjectName(u"tool_length_10")
        sizePolicy.setHeightForWidth(self.tool_length_10.sizePolicy().hasHeightForWidth())
        self.tool_length_10.setSizePolicy(sizePolicy)
        self.tool_length_10.setMinimumSize(QSize(70, 40))
        self.tool_length_10.setMaximumSize(QSize(16777215, 40))
        self.tool_length_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.tool_length_10.setWordWrap(True)
        self.tool_length_10.setIndent(4)

        self.horizontalLayout_133.addWidget(self.tool_length_10)


        self.horizontalLayout_132.addLayout(self.horizontalLayout_133)


        self.verticalLayout_14.addWidget(self.frame_40)

        self.widget_3 = QWidget(self.widget_21)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy6.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy6)
        self.widget_3.setMinimumSize(QSize(0, 280))
        self.widget_3.setMaximumSize(QSize(16777215, 280))
        self.label_89 = QLabel(self.widget_3)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(40, 4, 169, 274))
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy7)
        self.label_89.setMinimumSize(QSize(169, 274))
        self.label_89.setMaximumSize(QSize(169, 274))
        self.label_89.setStyleSheet(u"image: url(:/images/atc_spindle_tool.png);")
        self.label_89.setScaledContents(True)
        self.label_89.setIndent(0)
        self.loaded_spindle_tool_number = StatusLabel(self.widget_3)
        self.loaded_spindle_tool_number.setObjectName(u"loaded_spindle_tool_number")
        self.loaded_spindle_tool_number.setGeometry(QRect(100, 135, 50, 30))
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.loaded_spindle_tool_number.sizePolicy().hasHeightForWidth())
        self.loaded_spindle_tool_number.setSizePolicy(sizePolicy8)
        self.loaded_spindle_tool_number.setMinimumSize(QSize(50, 30))
        self.loaded_spindle_tool_number.setMaximumSize(QSize(50, 30))
        self.loaded_spindle_tool_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_21)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy6.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy6)
        self.widget_4.setMinimumSize(QSize(0, 202))
        self.widget_4.setMaximumSize(QSize(16777215, 202))
        self.label_38 = QLabel(self.widget_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(110, 0, 240, 200))
        self.label_38.setMinimumSize(QSize(240, 200))
        self.label_38.setMaximumSize(QSize(240, 200))
        self.label_38.setStyleSheet(u"image: url(:/images/tool_probe.png);")
        self.label_38.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.widget_4)


        self.horizontalLayout_50.addWidget(self.widget_21)


        self.horizontalLayout.addLayout(self.horizontalLayout_50)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(24)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 20, 9, 30)
        self.frame_6 = QFrame(ATC)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy7.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy7)
        self.frame_6.setMinimumSize(QSize(300, 380))
        self.frame_6.setMaximumSize(QSize(300, 380))
        self.frame_6.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(19, 9, 19, 9)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 2, 0, 2)
        self.machine_column_header_3 = QLabel(self.frame_6)
        self.machine_column_header_3.setObjectName(u"machine_column_header_3")
        self.machine_column_header_3.setMinimumSize(QSize(0, 45))
        self.machine_column_header_3.setMaximumSize(QSize(16777215, 45))
        self.machine_column_header_3.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.machine_column_header_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_26.setContentsMargins(4, 2, 2, 2)
        self.load_spindle_tool_number = VCPLineEdit(self.frame_6)
        self.load_spindle_tool_number.setObjectName(u"load_spindle_tool_number")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(200)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.load_spindle_tool_number.sizePolicy().hasHeightForWidth())
        self.load_spindle_tool_number.setSizePolicy(sizePolicy9)
        self.load_spindle_tool_number.setMinimumSize(QSize(0, 43))
        self.load_spindle_tool_number.setMaximumSize(QSize(16777215, 43))
        self.load_spindle_tool_number.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.load_spindle_tool_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_26.addWidget(self.load_spindle_tool_number)

        self.load_spindle_button = SubCallButton(self.frame_6)
        self.load_spindle_button.setObjectName(u"load_spindle_button")
        self.load_spindle_button.setMinimumSize(QSize(125, 45))
        self.load_spindle_button.setMaximumSize(QSize(16777215, 45))
        self.load_spindle_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255"
                        "));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_26.addWidget(self.load_spindle_button)


        self.verticalLayout_10.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.remove_tool = SubCallButton(self.frame_6)
        self.remove_tool.setObjectName(u"remove_tool")
        self.remove_tool.setMinimumSize(QSize(125, 45))
        self.remove_tool.setMaximumSize(QSize(16777215, 45))
        self.remove_tool.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255"
                        "));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.remove_tool)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.store_tool_in_spindle = SubCallButton(self.frame_6)
        self.store_tool_in_spindle.setObjectName(u"store_tool_in_spindle")
        self.store_tool_in_spindle.setMinimumSize(QSize(125, 45))
        self.store_tool_in_spindle.setMaximumSize(QSize(16777215, 45))
        self.store_tool_in_spindle.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255"
                        "));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.store_tool_in_spindle)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setSpacing(15)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(4, 2, 2, 2)
        self.tool_number_entry_atc_page = VCPLineEdit(self.frame_6)
        self.tool_number_entry_atc_page.setObjectName(u"tool_number_entry_atc_page")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(200)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.tool_number_entry_atc_page.sizePolicy().hasHeightForWidth())
        self.tool_number_entry_atc_page.setSizePolicy(sizePolicy10)
        self.tool_number_entry_atc_page.setMinimumSize(QSize(0, 43))
        self.tool_number_entry_atc_page.setSizeIncrement(QSize(0, 40))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(108, 108, 108, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(65, 84, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tool_number_entry_atc_page.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Probe Basic Bebas Mono"])
        font1.setPointSize(17)
        font1.setBold(False)
        font1.setItalic(False)
        self.tool_number_entry_atc_page.setFont(font1)
        self.tool_number_entry_atc_page.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.tool_number_entry_atc_page.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.tool_number_entry_atc_page.setFrame(True)
        self.tool_number_entry_atc_page.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_134.addWidget(self.tool_number_entry_atc_page)

        self.m6_tool_call_button_atc_page = SubCallButton(self.frame_6)
        self.m6_tool_call_button_atc_page.setObjectName(u"m6_tool_call_button_atc_page")
        self.m6_tool_call_button_atc_page.setMinimumSize(QSize(125, 45))
        self.m6_tool_call_button_atc_page.setMaximumSize(QSize(16777215, 45))
        self.m6_tool_call_button_atc_page.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255"
                        "));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_134.addWidget(self.m6_tool_call_button_atc_page)


        self.verticalLayout_10.addLayout(self.horizontalLayout_134)


        self.verticalLayout_17.addWidget(self.frame_6)

        self.frame_7 = QFrame(ATC)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(1)
        sizePolicy11.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy11)
        self.frame_7.setMinimumSize(QSize(300, 0))
        self.frame_7.setMaximumSize(QSize(300, 200))
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(19, 3, 19, 6)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 2, 0, 2)
        self.machine_column_header_2 = QLabel(self.frame_7)
        self.machine_column_header_2.setObjectName(u"machine_column_header_2")
        self.machine_column_header_2.setMinimumSize(QSize(0, 45))
        self.machine_column_header_2.setMaximumSize(QSize(16777215, 45))
        self.machine_column_header_2.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.machine_column_header_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(2, 2, 2, 2)
        self.tool_touch_off_button_atc = SubCallButton(self.frame_7)
        self.tool_touch_off_button_atc.setObjectName(u"tool_touch_off_button_atc")
        sizePolicy.setHeightForWidth(self.tool_touch_off_button_atc.sizePolicy().hasHeightForWidth())
        self.tool_touch_off_button_atc.setSizePolicy(sizePolicy)
        self.tool_touch_off_button_atc.setMinimumSize(QSize(250, 45))
        self.tool_touch_off_button_atc.setMaximumSize(QSize(16777215, 45))
        self.tool_touch_off_button_atc.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tool_touch_off_button_atc.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255"
                        "));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_23.addWidget(self.tool_touch_off_button_atc)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)


        self.verticalLayout_17.addWidget(self.frame_7)


        self.horizontalLayout.addLayout(self.verticalLayout_17)


        self.retranslateUi(ATC)
        self.load_spindle_tool_number.returnPressed.connect(self.load_spindle_button.click)
        self.tool_number_entry_atc_page.returnPressed.connect(self.m6_tool_call_button_atc_page.click)

        self.tabWidget_33.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ATC)
    # setupUi

    def retranslateUi(self, ATC):
        ATC.setWindowTitle(QCoreApplication.translate("ATC", u"atc", None))
        self.work_column_header_7.setText(QCoreApplication.translate("ATC", u"CURRENT PROGRAM TOOLS", None))
        self.tools_check_list.setText("")
        self.tools_check_list.setProperty(u"rules", QCoreApplication.translate("ATC", u"[{\"name\": \"program_tool_list\", \"property\": \"Text\", \"expression\": \"(lambda atc: \\\"<html>\\\"+\\\"<br/>\\\".join(f\\\"<span style='color:{\\\"#7298ff\\\" if int(ch[1][x][0]) in atc else \\\"#ffffff\\\"}'>T{int(ch[1][x][0])}</span>\\\" for x in ch[0])+\\\"</html>\\\")({int(param(p,0)) for p in range(4001,4025) if int(param(p,0))>0})\", \"channels\": [{\"url\": \"gcode_properties:tools\", \"trigger\": true}, {\"url\": \"status:tool_table\", \"trigger\": false}]}]", None))
#if QT_CONFIG(tooltip)
        self.reference_carousel_2.setToolTip(QCoreApplication.translate("ATC", u"M13 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.reference_carousel_2.setText(QCoreApplication.translate("ATC", u"REF CAROUSEL", None))
        self.reference_carousel_2.setProperty(u"MDICommand", QCoreApplication.translate("ATC", u"M13", None))
        self.tabWidget_33.setTabText(self.tabWidget_33.indexOf(self.program_tools_tab), QCoreApplication.translate("ATC", u"PROGRAM TOOLS", None))
        self.tabWidget_33.setTabText(self.tabWidget_33.indexOf(self.manual_atc_tab), QCoreApplication.translate("ATC", u"MANUAL ATC", None))
        self.mdi_entry_box_3.setPlaceholderText(QCoreApplication.translate("ATC", u"MDI", None))
        self.mdi_entry_box_3.setProperty(u"styleSet", QCoreApplication.translate("ATC", u"dataField15", None))
        self.tool_length_10.setText(QCoreApplication.translate("ATC", u"No Tool Loaded", None))
        self.tool_length_10.setProperty(u"format", QCoreApplication.translate("ATC", u"{:.3f}", None))
        self.tool_length_10.setProperty(u"rules", QCoreApplication.translate("ATC", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?remark\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Tool Comment\"}]", None))
        self.tool_length_10.setProperty(u"styleSet", QCoreApplication.translate("ATC", u"dataField14", None))
        self.label_89.setText("")
        self.loaded_spindle_tool_number.setText(QCoreApplication.translate("ATC", u"T0", None))
        self.loaded_spindle_tool_number.setProperty(u"format", QCoreApplication.translate("ATC", u"{:.3f}", None))
        self.loaded_spindle_tool_number.setProperty(u"rules", QCoreApplication.translate("ATC", u"[{\"channels\": [{\"url\": \"status:tool_in_spindle?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"'T' + ch[0]\", \"name\": \"current tool\"}]", None))
        self.loaded_spindle_tool_number.setProperty(u"statusItem", QCoreApplication.translate("ATC", u"tool_offset.3", None))
        self.loaded_spindle_tool_number.setProperty(u"styleSet", QCoreApplication.translate("ATC", u"dataField16", None))
        self.label_38.setText("")
        self.machine_column_header_3.setText(QCoreApplication.translate("ATC", u"ATC AUTOMATIC CONTROL PANEL", None))
        self.load_spindle_tool_number.setPlaceholderText(QCoreApplication.translate("ATC", u"0", None))
        self.load_spindle_tool_number.setProperty(u"rules", QCoreApplication.translate("ATC", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(0)\", \"name\": \"update tool num\"}, {\"channels\": [{\"url\": \"status:task_state?text\", \"trigger\": true}, {\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] == 'On' and ch[1] == 'Idle'\", \"name\": \"enable/disable\"}]", None))
        self.load_spindle_tool_number.setProperty(u"styleSet", QCoreApplication.translate("ATC", u"dataField17", None))
        self.load_spindle_button.setText(QCoreApplication.translate("ATC", u"LOAD SPINDLE", None))
        self.load_spindle_button.setProperty(u"filename", QCoreApplication.translate("ATC", u"load_spindle_safety.ngc", None))
        self.remove_tool.setText(QCoreApplication.translate("ATC", u"UNLOAD SPINDLE", None))
        self.remove_tool.setProperty(u"filename", QCoreApplication.translate("ATC", u"unload_spindle.ngc", None))
        self.store_tool_in_spindle.setText(QCoreApplication.translate("ATC", u"Store Tool IN CAROUSEL", None))
        self.store_tool_in_spindle.setProperty(u"filename", QCoreApplication.translate("ATC", u"store_tool_in_carousel.ngc", None))
        self.tool_number_entry_atc_page.setPlaceholderText(QCoreApplication.translate("ATC", u"0", None))
        self.tool_number_entry_atc_page.setProperty(u"rules", QCoreApplication.translate("ATC", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(ch[0])\", \"name\": \"update tool num\"}, {\"channels\": [{\"url\": \"status:task_state?text\", \"trigger\": true}, {\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] == 'On' and ch[1] == 'Idle'\", \"name\": \"enable/disable\"}]", None))
        self.tool_number_entry_atc_page.setProperty(u"styleSet", QCoreApplication.translate("ATC", u"dataField17", None))
        self.m6_tool_call_button_atc_page.setText(QCoreApplication.translate("ATC", u"M6 G43", None))
        self.m6_tool_call_button_atc_page.setProperty(u"filename", QCoreApplication.translate("ATC", u"m6_tool_call_atc_page.ngc", None))
        self.machine_column_header_2.setText(QCoreApplication.translate("ATC", u"ELECTRONIC TOOL SETTER", None))
        self.tool_touch_off_button_atc.setText(QCoreApplication.translate("ATC", u"TOUCH OFF CURRENT TOOL", None))
        self.tool_touch_off_button_atc.setProperty(u"filename", QCoreApplication.translate("ATC", u"tool_touch_off.ngc", None))
    # retranslateUi

