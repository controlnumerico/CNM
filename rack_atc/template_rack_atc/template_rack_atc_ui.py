# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_rack_atc.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QScrollArea,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.input_widgets.line_edit import VCPLineEdit
from qtpyvcp.widgets.input_widgets.mdientry_widget import MDIEntry
from qtpyvcp.widgets.input_widgets.setting_slider import VCPSettingsLineEdit
from widgets.rack_atc_widget.rack_atc import RackATC
import probe_basic_rc
import probe_basic_rc
import probe_basic_rc

class Ui_RACK_ATC(object):
    def setupUi(self, RACK_ATC):
        if not RACK_ATC.objectName():
            RACK_ATC.setObjectName(u"RACK_ATC")
        RACK_ATC.resize(1521, 625)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RACK_ATC.sizePolicy().hasHeightForWidth())
        RACK_ATC.setSizePolicy(sizePolicy)
        RACK_ATC.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(RACK_ATC)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.rack_tab_widget = QTabWidget(RACK_ATC)
        self.rack_tab_widget.setObjectName(u"rack_tab_widget")
        self.rack_tab_widget.setStyleSheet(u"#rack_tab_widget::pane {\n"
"    border: none;\n"
"}\n"
"\n"
"#rack_tab_widget QTabBar::tab{\n"
"    margin-top: 0px;\n"
"    margin-right: 6px;\n"
"    margin-bottom:0px;\n"
"    min-width: 25px;\n"
"    min-height: 120px;\n"
"    font: 16pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"\n"
"#rack_tab_widget QTabBar::tab:first {\n"
"    margin-top: 20px;\n"
"    border-left-width: 2px;\n"
"    border-bottom-width: 1px;\n"
"    border-right-width: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"#rack_tab_widget QTabBar::tab:last {\n"
"    border-left-width: 2px;\n"
"    border-top-width: 1px;\n"
"    border-right-width: 2px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"#rack_tab_widget QTabBar::tab:only-one {\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"}")
        self.rack_tab_widget.setTabPosition(QTabWidget.TabPosition.West)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 12, 40, 10)
        self.widget_5 = QWidget(self.tab)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_5)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(0, 450))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.user_tab_widget = QTabWidget(self.widget)
        self.user_tab_widget.setObjectName(u"user_tab_widget")
        sizePolicy.setHeightForWidth(self.user_tab_widget.sizePolicy().hasHeightForWidth())
        self.user_tab_widget.setSizePolicy(sizePolicy)
        self.user_tab_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.user_tab_widget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: none;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"    margin-top: 0px;\n"
"    margin-right: 0px;\n"
"    margin-bottom:0px;\n"
"    min-width: 150px;\n"
"    min-height: 30px;\n"
"    font: 16pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    margin-top: 0px;\n"
"    border-left-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 0px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    border-left-width: 2px;\n"
"    border-top-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 4px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"}")
        self.user_tab_widget.setTabPosition(QTabWidget.TabPosition.North)
        self.program_tools_tab = QWidget()
        self.program_tools_tab.setObjectName(u"program_tools_tab")
        self.verticalLayout_11 = QVBoxLayout(self.program_tools_tab)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, -1, 9, 0)
        self.current_tools_frame = QFrame(self.program_tools_tab)
        self.current_tools_frame.setObjectName(u"current_tools_frame")
        sizePolicy.setHeightForWidth(self.current_tools_frame.sizePolicy().hasHeightForWidth())
        self.current_tools_frame.setSizePolicy(sizePolicy)
        self.current_tools_frame.setMinimumSize(QSize(300, 0))
        self.current_tools_frame.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_65 = QVBoxLayout(self.current_tools_frame)
        self.verticalLayout_65.setSpacing(16)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(22, 18, 22, 14)
        self.current_tools_layout_top = QHBoxLayout()
        self.current_tools_layout_top.setObjectName(u"current_tools_layout_top")
        self.current_tools_layout_top.setContentsMargins(2, 2, 2, 2)
        self.current_tools_header = QLabel(self.current_tools_frame)
        self.current_tools_header.setObjectName(u"current_tools_header")
        self.current_tools_header.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.current_tools_header.sizePolicy().hasHeightForWidth())
        self.current_tools_header.setSizePolicy(sizePolicy2)
        self.current_tools_header.setMinimumSize(QSize(0, 38))
        self.current_tools_header.setMaximumSize(QSize(16777215, 38))
        self.current_tools_header.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.current_tools_header.setFrameShape(QFrame.Shape.NoFrame)
        self.current_tools_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.current_tools_header.setWordWrap(True)
        self.current_tools_header.setIndent(0)

        self.current_tools_layout_top.addWidget(self.current_tools_header)


        self.verticalLayout_65.addLayout(self.current_tools_layout_top)

        self.scrollArea = QScrollArea(self.current_tools_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 232, 783))
        self.verticalLayout_70 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.widget_6.setStyleSheet(u"border: none;\n"
"border-radius: 0px;\n"
"background-color: rgb(46, 52, 54);\n"
"")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_33.setSpacing(20)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(30, 6, 0, 0)
        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy4)
        self.widget_9.setMinimumSize(QSize(30, 0))
        self.verticalLayout_67 = QVBoxLayout(self.widget_9)
        self.verticalLayout_67.setSpacing(13)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(-1, 6, 3, 0)
        self.checkBox = QCheckBox(self.widget_9)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_67.addWidget(self.checkBox)

        self.checkBox_4 = QCheckBox(self.widget_9)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_67.addWidget(self.checkBox_4)

        self.checkBox_2 = QCheckBox(self.widget_9)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_67.addWidget(self.checkBox_2)

        self.checkBox_41 = QCheckBox(self.widget_9)
        self.checkBox_41.setObjectName(u"checkBox_41")

        self.verticalLayout_67.addWidget(self.checkBox_41)

        self.checkBox_3 = QCheckBox(self.widget_9)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_67.addWidget(self.checkBox_3)

        self.checkBox_34 = QCheckBox(self.widget_9)
        self.checkBox_34.setObjectName(u"checkBox_34")

        self.verticalLayout_67.addWidget(self.checkBox_34)

        self.checkBox_6 = QCheckBox(self.widget_9)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_67.addWidget(self.checkBox_6)

        self.checkBox_31 = QCheckBox(self.widget_9)
        self.checkBox_31.setObjectName(u"checkBox_31")

        self.verticalLayout_67.addWidget(self.checkBox_31)

        self.checkBox_5 = QCheckBox(self.widget_9)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_67.addWidget(self.checkBox_5)

        self.checkBox_39 = QCheckBox(self.widget_9)
        self.checkBox_39.setObjectName(u"checkBox_39")

        self.verticalLayout_67.addWidget(self.checkBox_39)

        self.checkBox_9 = QCheckBox(self.widget_9)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.verticalLayout_67.addWidget(self.checkBox_9)

        self.checkBox_38 = QCheckBox(self.widget_9)
        self.checkBox_38.setObjectName(u"checkBox_38")

        self.verticalLayout_67.addWidget(self.checkBox_38)

        self.checkBox_7 = QCheckBox(self.widget_9)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_67.addWidget(self.checkBox_7)

        self.checkBox_37 = QCheckBox(self.widget_9)
        self.checkBox_37.setObjectName(u"checkBox_37")

        self.verticalLayout_67.addWidget(self.checkBox_37)

        self.checkBox_8 = QCheckBox(self.widget_9)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout_67.addWidget(self.checkBox_8)

        self.checkBox_33 = QCheckBox(self.widget_9)
        self.checkBox_33.setObjectName(u"checkBox_33")

        self.verticalLayout_67.addWidget(self.checkBox_33)

        self.checkBox_10 = QCheckBox(self.widget_9)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.verticalLayout_67.addWidget(self.checkBox_10)

        self.checkBox_40 = QCheckBox(self.widget_9)
        self.checkBox_40.setObjectName(u"checkBox_40")

        self.verticalLayout_67.addWidget(self.checkBox_40)

        self.checkBox_11 = QCheckBox(self.widget_9)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.verticalLayout_67.addWidget(self.checkBox_11)

        self.checkBox_35 = QCheckBox(self.widget_9)
        self.checkBox_35.setObjectName(u"checkBox_35")

        self.verticalLayout_67.addWidget(self.checkBox_35)

        self.checkBox_12 = QCheckBox(self.widget_9)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.verticalLayout_67.addWidget(self.checkBox_12)

        self.checkBox_30 = QCheckBox(self.widget_9)
        self.checkBox_30.setObjectName(u"checkBox_30")

        self.verticalLayout_67.addWidget(self.checkBox_30)

        self.checkBox_13 = QCheckBox(self.widget_9)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.verticalLayout_67.addWidget(self.checkBox_13)

        self.checkBox_32 = QCheckBox(self.widget_9)
        self.checkBox_32.setObjectName(u"checkBox_32")

        self.verticalLayout_67.addWidget(self.checkBox_32)

        self.checkBox_14 = QCheckBox(self.widget_9)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.verticalLayout_67.addWidget(self.checkBox_14)

        self.checkBox_42 = QCheckBox(self.widget_9)
        self.checkBox_42.setObjectName(u"checkBox_42")

        self.verticalLayout_67.addWidget(self.checkBox_42)

        self.checkBox_36 = QCheckBox(self.widget_9)
        self.checkBox_36.setObjectName(u"checkBox_36")

        self.verticalLayout_67.addWidget(self.checkBox_36)

        self.checkBox_29 = QCheckBox(self.widget_9)
        self.checkBox_29.setObjectName(u"checkBox_29")

        self.verticalLayout_67.addWidget(self.checkBox_29)

        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.verticalLayout_67.addWidget(self.label_5)


        self.horizontalLayout_33.addWidget(self.widget_9)

        self.statuslabel = StatusLabel(self.widget_6)
        self.statuslabel.setObjectName(u"statuslabel")
        sizePolicy3.setHeightForWidth(self.statuslabel.sizePolicy().hasHeightForWidth())
        self.statuslabel.setSizePolicy(sizePolicy3)
        self.statuslabel.setLineWidth(3)
        self.statuslabel.setMidLineWidth(2)
        self.statuslabel.setTextFormat(Qt.TextFormat.AutoText)
        self.statuslabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.statuslabel.setWordWrap(True)

        self.horizontalLayout_33.addWidget(self.statuslabel)


        self.verticalLayout_70.addWidget(self.widget_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_65.addWidget(self.scrollArea)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setSpacing(15)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(2, 2, 2, 2)
        self.reference_carousel_2 = MDIButton(self.current_tools_frame)
        self.reference_carousel_2.setObjectName(u"reference_carousel_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.reference_carousel_2.sizePolicy().hasHeightForWidth())
        self.reference_carousel_2.setSizePolicy(sizePolicy5)
        self.reference_carousel_2.setMinimumSize(QSize(125, 45))
        self.reference_carousel_2.setMaximumSize(QSize(16777215, 45))
        self.reference_carousel_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.reference_carousel_2.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.reference_carousel_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_159.addWidget(self.reference_carousel_2)


        self.verticalLayout_65.addLayout(self.horizontalLayout_159)


        self.verticalLayout_11.addWidget(self.current_tools_frame)

        self.user_tab_widget.addTab(self.program_tools_tab, "")
        self.manual_atc_tab = QWidget()
        self.manual_atc_tab.setObjectName(u"manual_atc_tab")
        self.verticalLayout_12 = QVBoxLayout(self.manual_atc_tab)
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, -1, 9, 0)
        self.user_rack_atc_buttons_layout = QVBoxLayout()
        self.user_rack_atc_buttons_layout.setSpacing(0)
        self.user_rack_atc_buttons_layout.setObjectName(u"user_rack_atc_buttons_layout")

        self.verticalLayout_12.addLayout(self.user_rack_atc_buttons_layout)

        self.user_tab_widget.addTab(self.manual_atc_tab, "")

        self.verticalLayout_9.addWidget(self.user_tab_widget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.widget_21 = QWidget(self.widget)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy6)
        self.widget_21.setMinimumSize(QSize(172, 0))
        self.widget_21.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.widget_21)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.widget_21)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(2)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy7)
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
        self.tool_information_rack = StatusLabel(self.frame_40)
        self.tool_information_rack.setObjectName(u"tool_information_rack")
        sizePolicy.setHeightForWidth(self.tool_information_rack.sizePolicy().hasHeightForWidth())
        self.tool_information_rack.setSizePolicy(sizePolicy)
        self.tool_information_rack.setMinimumSize(QSize(70, 40))
        self.tool_information_rack.setMaximumSize(QSize(16777215, 40))
        self.tool_information_rack.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.tool_information_rack.setWordWrap(True)
        self.tool_information_rack.setIndent(4)

        self.horizontalLayout_133.addWidget(self.tool_information_rack)


        self.horizontalLayout_132.addLayout(self.horizontalLayout_133)


        self.verticalLayout_14.addWidget(self.frame_40)

        self.widget_8 = QWidget(self.widget_21)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy8)
        self.widget_8.setMinimumSize(QSize(0, 5))

        self.verticalLayout_14.addWidget(self.widget_8)

        self.widget_11 = QWidget(self.widget_21)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy9)
        self.widget_11.setMinimumSize(QSize(294, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.spacer_widget_left_rack = QWidget(self.widget_11)
        self.spacer_widget_left_rack.setObjectName(u"spacer_widget_left_rack")
        self.spacer_widget_left_rack.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.spacer_widget_left_rack)

        self.widget_3 = QWidget(self.widget_11)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(1)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy10)
        self.widget_3.setMinimumSize(QSize(171, 280))
        self.widget_3.setMaximumSize(QSize(170, 16777215))
        self.spindle_image_label = QLabel(self.widget_3)
        self.spindle_image_label.setObjectName(u"spindle_image_label")
        self.spindle_image_label.setGeometry(QRect(1, -1, 169, 274))
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.spindle_image_label.sizePolicy().hasHeightForWidth())
        self.spindle_image_label.setSizePolicy(sizePolicy11)
        self.spindle_image_label.setStyleSheet(u"image: url(:/images/atc_spindle_tool.png);")
        self.spindle_image_label.setScaledContents(True)
        self.spindle_image_label.setIndent(0)
        self.loaded_spindle_tool_number = StatusLabel(self.widget_3)
        self.loaded_spindle_tool_number.setObjectName(u"loaded_spindle_tool_number")
        self.loaded_spindle_tool_number.setGeometry(QRect(61, 130, 50, 30))
        sizePolicy10.setHeightForWidth(self.loaded_spindle_tool_number.sizePolicy().hasHeightForWidth())
        self.loaded_spindle_tool_number.setSizePolicy(sizePolicy10)
        self.loaded_spindle_tool_number.setMinimumSize(QSize(50, 30))
        self.loaded_spindle_tool_number.setMaximumSize(QSize(50, 30))
        self.loaded_spindle_tool_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.widget_3)

        self.spacer_widget_right_rack = QWidget(self.widget_11)
        self.spacer_widget_right_rack.setObjectName(u"spacer_widget_right_rack")

        self.horizontalLayout_4.addWidget(self.spacer_widget_right_rack)


        self.verticalLayout_14.addWidget(self.widget_11)

        self.widget_4 = QWidget(self.widget_21)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy9.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy9)
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.mdi_entry_box_rack_tab = MDIEntry(self.widget_4)
        self.mdi_entry_box_rack_tab.setObjectName(u"mdi_entry_box_rack_tab")
        self.mdi_entry_box_rack_tab.setMinimumSize(QSize(0, 42))
        self.mdi_entry_box_rack_tab.setMaximumSize(QSize(16777215, 42))
        font = QFont()
        font.setFamilies([u"Probe Basic Bebas Mono"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.mdi_entry_box_rack_tab.setFont(font)
        self.mdi_entry_box_rack_tab.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_4.addWidget(self.mdi_entry_box_rack_tab)


        self.verticalLayout_14.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.widget_21)

        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_2 = QVBoxLayout(self.widget_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rack_atc_load_frame = QFrame(self.widget_7)
        self.rack_atc_load_frame.setObjectName(u"rack_atc_load_frame")
        sizePolicy.setHeightForWidth(self.rack_atc_load_frame.sizePolicy().hasHeightForWidth())
        self.rack_atc_load_frame.setSizePolicy(sizePolicy)
        self.rack_atc_load_frame.setStyleSheet(u".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.rack_atc_load_frame)
        self.verticalLayout_10.setSpacing(16)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 18, 20, 18)
        self.atc_loading_panel_header = QLabel(self.rack_atc_load_frame)
        self.atc_loading_panel_header.setObjectName(u"atc_loading_panel_header")
        self.atc_loading_panel_header.setMinimumSize(QSize(0, 38))
        self.atc_loading_panel_header.setMaximumSize(QSize(16777215, 38))
        self.atc_loading_panel_header.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.atc_loading_panel_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.atc_loading_panel_header)

        self.rack_load_tool_layout = QHBoxLayout()
        self.rack_load_tool_layout.setSpacing(15)
        self.rack_load_tool_layout.setObjectName(u"rack_load_tool_layout")
        self.rack_load_tool_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.rack_load_tool_layout.setContentsMargins(4, 2, 2, 2)
        self.load_spindle_tool_number = VCPLineEdit(self.rack_atc_load_frame)
        self.load_spindle_tool_number.setObjectName(u"load_spindle_tool_number")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(200)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.load_spindle_tool_number.sizePolicy().hasHeightForWidth())
        self.load_spindle_tool_number.setSizePolicy(sizePolicy12)
        self.load_spindle_tool_number.setMinimumSize(QSize(0, 43))
        self.load_spindle_tool_number.setMaximumSize(QSize(16777215, 43))
        self.load_spindle_tool_number.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.load_spindle_tool_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.rack_load_tool_layout.addWidget(self.load_spindle_tool_number)

        self.load_spindle_button = SubCallButton(self.rack_atc_load_frame)
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

        self.rack_load_tool_layout.addWidget(self.load_spindle_button)


        self.verticalLayout_10.addLayout(self.rack_load_tool_layout)

        self.rack_unload_layout = QHBoxLayout()
        self.rack_unload_layout.setSpacing(0)
        self.rack_unload_layout.setObjectName(u"rack_unload_layout")
        self.rack_unload_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.rack_unload_layout.setContentsMargins(2, 2, 2, 2)
        self.remove_tool_button = SubCallButton(self.rack_atc_load_frame)
        self.remove_tool_button.setObjectName(u"remove_tool_button")
        self.remove_tool_button.setMinimumSize(QSize(125, 45))
        self.remove_tool_button.setMaximumSize(QSize(16777215, 45))
        self.remove_tool_button.setStyleSheet(u"QPushButton {\n"
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

        self.rack_unload_layout.addWidget(self.remove_tool_button)


        self.verticalLayout_10.addLayout(self.rack_unload_layout)

        self.rack_store_layout = QHBoxLayout()
        self.rack_store_layout.setSpacing(0)
        self.rack_store_layout.setObjectName(u"rack_store_layout")
        self.rack_store_layout.setContentsMargins(2, 2, 2, 2)
        self.store_tool_in_spindle = SubCallButton(self.rack_atc_load_frame)
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

        self.rack_store_layout.addWidget(self.store_tool_in_spindle)


        self.verticalLayout_10.addLayout(self.rack_store_layout)

        self.rack_change_layout = QHBoxLayout()
        self.rack_change_layout.setSpacing(15)
        self.rack_change_layout.setObjectName(u"rack_change_layout")
        self.rack_change_layout.setContentsMargins(4, 2, 2, 2)
        self.tool_number_entry_atc_page = VCPLineEdit(self.rack_atc_load_frame)
        self.tool_number_entry_atc_page.setObjectName(u"tool_number_entry_atc_page")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy13.setHorizontalStretch(200)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.tool_number_entry_atc_page.sizePolicy().hasHeightForWidth())
        self.tool_number_entry_atc_page.setSizePolicy(sizePolicy13)
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

        self.rack_change_layout.addWidget(self.tool_number_entry_atc_page)

        self.m6_tool_call_button_atc_page = SubCallButton(self.rack_atc_load_frame)
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

        self.rack_change_layout.addWidget(self.m6_tool_call_button_atc_page)


        self.verticalLayout_10.addLayout(self.rack_change_layout)

        self.widget_2 = QWidget(self.rack_atc_load_frame)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_10.addWidget(self.widget_2)

        self.racl_touch_off_layout = QHBoxLayout()
        self.racl_touch_off_layout.setSpacing(0)
        self.racl_touch_off_layout.setObjectName(u"racl_touch_off_layout")
        self.racl_touch_off_layout.setContentsMargins(2, 2, 2, 2)
        self.tool_touch_off_button_atc = SubCallButton(self.rack_atc_load_frame)
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

        self.racl_touch_off_layout.addWidget(self.tool_touch_off_button_atc)


        self.verticalLayout_10.addLayout(self.racl_touch_off_layout)


        self.verticalLayout_2.addWidget(self.rack_atc_load_frame)


        self.horizontalLayout_2.addWidget(self.widget_7)


        self.verticalLayout.addWidget(self.widget)

        self.rackatc = RackATC(self.widget_5)
        self.rackatc.setObjectName(u"rackatc")
        self.rackatc.setMinimumSize(QSize(0, 129))
        self.rackatc.setMaximumSize(QSize(16777215, 129))
        self.rackatc.setProperty(u"backgroundColor", QColor(146, 150, 149))

        self.verticalLayout.addWidget(self.rackatc)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.rack_tab_widget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, 3, -1, 0)
        self.widget_16 = QWidget(self.tab_2)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy14)
        self.widget_16.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget_16)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 1)
        self.rack_param_widget = QWidget(self.widget_16)
        self.rack_param_widget.setObjectName(u"rack_param_widget")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(1)
        sizePolicy15.setHeightForWidth(self.rack_param_widget.sizePolicy().hasHeightForWidth())
        self.rack_param_widget.setSizePolicy(sizePolicy15)
        self.rack_param_widget.setMaximumSize(QSize(300, 16777215))
        self.rack_param_widget.setStyleSheet(u".QWidget {\n"
"    background-color: #929695;;\n"
"}")
        self.verticalLayout_48 = QVBoxLayout(self.rack_param_widget)
        self.verticalLayout_48.setSpacing(5)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(9, 5, 6, 8)
        self.rack_param_header = QLabel(self.rack_param_widget)
        self.rack_param_header.setObjectName(u"rack_param_header")
        self.rack_param_header.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.rack_param_header.sizePolicy().hasHeightForWidth())
        self.rack_param_header.setSizePolicy(sizePolicy2)
        self.rack_param_header.setMinimumSize(QSize(0, 30))
        self.rack_param_header.setMaximumSize(QSize(16777215, 30))
        self.rack_param_header.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.rack_param_header.setFrameShape(QFrame.Shape.NoFrame)
        self.rack_param_header.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.rack_param_header.setWordWrap(True)
        self.rack_param_header.setIndent(10)

        self.verticalLayout_48.addWidget(self.rack_param_header)

        self.widget_52 = QWidget(self.rack_param_widget)
        self.widget_52.setObjectName(u"widget_52")
        sizePolicy.setHeightForWidth(self.widget_52.sizePolicy().hasHeightForWidth())
        self.widget_52.setSizePolicy(sizePolicy)
        self.widget_52.setStyleSheet(u".QFrame{\n"
"    background-color: #929695;\n"
"}\n"
"")
        self.verticalLayout_72 = QVBoxLayout(self.widget_52)
        self.verticalLayout_72.setSpacing(20)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 12, 0, 10)
        self.horizontalLayout_180 = QHBoxLayout()
        self.horizontalLayout_180.setSpacing(12)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(12, 1, 20, 1)
        self.label_15 = QLabel(self.widget_52)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMinimumSize(QSize(0, 38))
        self.label_15.setMaximumSize(QSize(16777215, 38))
        self.label_15.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Probe Basic Bebas Mono\";\n"
"color: white;\n"
"}")
        self.label_15.setLineWidth(0)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_15.setIndent(0)

        self.horizontalLayout_180.addWidget(self.label_15)

        self.atc_rack_id = VCPSettingsLineEdit(self.widget_52)
        self.atc_rack_id.setObjectName(u"atc_rack_id")
        sizePolicy11.setHeightForWidth(self.atc_rack_id.sizePolicy().hasHeightForWidth())
        self.atc_rack_id.setSizePolicy(sizePolicy11)
        self.atc_rack_id.setMinimumSize(QSize(100, 31))
        self.atc_rack_id.setMaximumSize(QSize(100, 31))
        self.atc_rack_id.setFont(font)
        self.atc_rack_id.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.atc_rack_id.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.atc_rack_id.setReadOnly(True)

        self.horizontalLayout_180.addWidget(self.atc_rack_id)


        self.verticalLayout_72.addLayout(self.horizontalLayout_180)

        self.horizontalLayout_181 = QHBoxLayout()
        self.horizontalLayout_181.setSpacing(12)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(12, 1, 20, 1)
        self.label_120 = QLabel(self.widget_52)
        self.label_120.setObjectName(u"label_120")
        sizePolicy2.setHeightForWidth(self.label_120.sizePolicy().hasHeightForWidth())
        self.label_120.setSizePolicy(sizePolicy2)
        self.label_120.setMinimumSize(QSize(0, 38))
        self.label_120.setMaximumSize(QSize(16777215, 38))
        self.label_120.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Probe Basic Bebas Mono\";\n"
"color: white;\n"
"}")
        self.label_120.setLineWidth(0)
        self.label_120.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_120.setIndent(0)

        self.horizontalLayout_181.addWidget(self.label_120)

        self.rack_pocket_count = VCPSettingsLineEdit(self.widget_52)
        self.rack_pocket_count.setObjectName(u"rack_pocket_count")
        sizePolicy11.setHeightForWidth(self.rack_pocket_count.sizePolicy().hasHeightForWidth())
        self.rack_pocket_count.setSizePolicy(sizePolicy11)
        self.rack_pocket_count.setMinimumSize(QSize(100, 31))
        self.rack_pocket_count.setMaximumSize(QSize(100, 31))
        self.rack_pocket_count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.rack_pocket_count.setReadOnly(True)

        self.horizontalLayout_181.addWidget(self.rack_pocket_count)


        self.verticalLayout_72.addLayout(self.horizontalLayout_181)

        self.horizontalLayout_179 = QHBoxLayout()
        self.horizontalLayout_179.setSpacing(12)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.horizontalLayout_179.setContentsMargins(12, 1, 20, 1)
        self.label_135 = QLabel(self.widget_52)
        self.label_135.setObjectName(u"label_135")
        sizePolicy2.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy2)
        self.label_135.setMinimumSize(QSize(0, 38))
        self.label_135.setMaximumSize(QSize(16777215, 38))
        self.label_135.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Probe Basic Bebas Mono\";\n"
"color: white;\n"
"}")
        self.label_135.setLineWidth(0)
        self.label_135.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_135.setIndent(0)

        self.horizontalLayout_179.addWidget(self.label_135)

        self.rack_traverse_speed_3980 = VCPSettingsLineEdit(self.widget_52)
        self.rack_traverse_speed_3980.setObjectName(u"rack_traverse_speed_3980")
        self.rack_traverse_speed_3980.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_traverse_speed_3980.sizePolicy().hasHeightForWidth())
        self.rack_traverse_speed_3980.setSizePolicy(sizePolicy11)
        self.rack_traverse_speed_3980.setMinimumSize(QSize(100, 31))
        self.rack_traverse_speed_3980.setMaximumSize(QSize(100, 31))
        self.rack_traverse_speed_3980.setFont(font)
        self.rack_traverse_speed_3980.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_traverse_speed_3980.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_179.addWidget(self.rack_traverse_speed_3980)


        self.verticalLayout_72.addLayout(self.horizontalLayout_179)

        self.horizontalLayout_194 = QHBoxLayout()
        self.horizontalLayout_194.setSpacing(12)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(12, 1, 20, 1)
        self.rack_atc_user_1 = VCPSettingsLineEdit(self.widget_52)
        self.rack_atc_user_1.setObjectName(u"rack_atc_user_1")
        self.rack_atc_user_1.setEnabled(True)
        self.rack_atc_user_1.setMinimumSize(QSize(0, 38))
        self.rack_atc_user_1.setMaximumSize(QSize(16777215, 38))
        self.rack_atc_user_1.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_atc_user_1.setStyleSheet(u"font: 15pt \"Probe Basic Bebas Mono\";\n"
"color: white;\n"
"background-color: #929695;\n"
"border: none;")
        self.rack_atc_user_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_194.addWidget(self.rack_atc_user_1)

        self.rack_atc_user_1_3974 = VCPSettingsLineEdit(self.widget_52)
        self.rack_atc_user_1_3974.setObjectName(u"rack_atc_user_1_3974")
        self.rack_atc_user_1_3974.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_atc_user_1_3974.sizePolicy().hasHeightForWidth())
        self.rack_atc_user_1_3974.setSizePolicy(sizePolicy11)
        self.rack_atc_user_1_3974.setMinimumSize(QSize(100, 31))
        self.rack_atc_user_1_3974.setMaximumSize(QSize(100, 31))
        self.rack_atc_user_1_3974.setFont(font)
        self.rack_atc_user_1_3974.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_atc_user_1_3974.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_194.addWidget(self.rack_atc_user_1_3974)


        self.verticalLayout_72.addLayout(self.horizontalLayout_194)

        self.horizontalLayout_183 = QHBoxLayout()
        self.horizontalLayout_183.setSpacing(12)
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.horizontalLayout_183.setContentsMargins(12, 1, 20, 1)
        self.rack_atc_user_2 = VCPSettingsLineEdit(self.widget_52)
        self.rack_atc_user_2.setObjectName(u"rack_atc_user_2")
        self.rack_atc_user_2.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.rack_atc_user_2.sizePolicy().hasHeightForWidth())
        self.rack_atc_user_2.setSizePolicy(sizePolicy2)
        self.rack_atc_user_2.setMinimumSize(QSize(0, 38))
        self.rack_atc_user_2.setMaximumSize(QSize(16777215, 38))
        self.rack_atc_user_2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_atc_user_2.setStyleSheet(u"font: 15pt \"Probe Basic Bebas Mono\";\n"
"color: white;\n"
"background-color: #929695;\n"
"border: none;")
        self.rack_atc_user_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_183.addWidget(self.rack_atc_user_2)

        self.rack_atc_user_2_3975 = VCPSettingsLineEdit(self.widget_52)
        self.rack_atc_user_2_3975.setObjectName(u"rack_atc_user_2_3975")
        self.rack_atc_user_2_3975.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_atc_user_2_3975.sizePolicy().hasHeightForWidth())
        self.rack_atc_user_2_3975.setSizePolicy(sizePolicy11)
        self.rack_atc_user_2_3975.setMinimumSize(QSize(100, 31))
        self.rack_atc_user_2_3975.setMaximumSize(QSize(100, 31))
        self.rack_atc_user_2_3975.setFont(font)
        self.rack_atc_user_2_3975.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_atc_user_2_3975.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_183.addWidget(self.rack_atc_user_2_3975)


        self.verticalLayout_72.addLayout(self.horizontalLayout_183)

        self.horizontalLayout_182 = QHBoxLayout()
        self.horizontalLayout_182.setSpacing(12)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(12, 1, 20, 1)
        self.rack_atc_user_3 = VCPSettingsLineEdit(self.widget_52)
        self.rack_atc_user_3.setObjectName(u"rack_atc_user_3")
        self.rack_atc_user_3.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.rack_atc_user_3.sizePolicy().hasHeightForWidth())
        self.rack_atc_user_3.setSizePolicy(sizePolicy2)
        self.rack_atc_user_3.setMinimumSize(QSize(0, 38))
        self.rack_atc_user_3.setMaximumSize(QSize(16777215, 38))
        self.rack_atc_user_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_atc_user_3.setStyleSheet(u"font: 15pt \"Probe Basic Bebas Mono\";\n"
"color: white;\n"
"background-color: #929695;\n"
"border: none;")
        self.rack_atc_user_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_182.addWidget(self.rack_atc_user_3)

        self.rack_atc_user_3_3976 = VCPSettingsLineEdit(self.widget_52)
        self.rack_atc_user_3_3976.setObjectName(u"rack_atc_user_3_3976")
        self.rack_atc_user_3_3976.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_atc_user_3_3976.sizePolicy().hasHeightForWidth())
        self.rack_atc_user_3_3976.setSizePolicy(sizePolicy11)
        self.rack_atc_user_3_3976.setMinimumSize(QSize(100, 31))
        self.rack_atc_user_3_3976.setMaximumSize(QSize(100, 31))
        self.rack_atc_user_3_3976.setFont(font)
        self.rack_atc_user_3_3976.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_atc_user_3_3976.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_182.addWidget(self.rack_atc_user_3_3976)


        self.verticalLayout_72.addLayout(self.horizontalLayout_182)

        self.horizontalLayout_187 = QHBoxLayout()
        self.horizontalLayout_187.setSpacing(12)
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalLayout_187.setContentsMargins(12, 1, 20, 1)
        self.rack_atc_user_4 = VCPSettingsLineEdit(self.widget_52)
        self.rack_atc_user_4.setObjectName(u"rack_atc_user_4")
        self.rack_atc_user_4.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.rack_atc_user_4.sizePolicy().hasHeightForWidth())
        self.rack_atc_user_4.setSizePolicy(sizePolicy2)
        self.rack_atc_user_4.setMinimumSize(QSize(0, 38))
        self.rack_atc_user_4.setMaximumSize(QSize(16777215, 38))
        self.rack_atc_user_4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_atc_user_4.setStyleSheet(u"font: 15pt \"Probe Basic Bebas Mono\";\n"
"color: white;\n"
"background-color: #929695;\n"
"border: none;")
        self.rack_atc_user_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_187.addWidget(self.rack_atc_user_4)

        self.rack_atc_user_4_3977 = VCPSettingsLineEdit(self.widget_52)
        self.rack_atc_user_4_3977.setObjectName(u"rack_atc_user_4_3977")
        self.rack_atc_user_4_3977.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_atc_user_4_3977.sizePolicy().hasHeightForWidth())
        self.rack_atc_user_4_3977.setSizePolicy(sizePolicy11)
        self.rack_atc_user_4_3977.setMinimumSize(QSize(100, 31))
        self.rack_atc_user_4_3977.setMaximumSize(QSize(100, 31))
        self.rack_atc_user_4_3977.setFont(font)
        self.rack_atc_user_4_3977.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_atc_user_4_3977.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_187.addWidget(self.rack_atc_user_4_3977)


        self.verticalLayout_72.addLayout(self.horizontalLayout_187)

        self.horizontalLayout_188 = QHBoxLayout()
        self.horizontalLayout_188.setSpacing(12)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.horizontalLayout_188.setContentsMargins(12, 1, 20, 1)
        self.rack_atc_user_5 = VCPSettingsLineEdit(self.widget_52)
        self.rack_atc_user_5.setObjectName(u"rack_atc_user_5")
        self.rack_atc_user_5.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.rack_atc_user_5.sizePolicy().hasHeightForWidth())
        self.rack_atc_user_5.setSizePolicy(sizePolicy2)
        self.rack_atc_user_5.setMinimumSize(QSize(0, 38))
        self.rack_atc_user_5.setMaximumSize(QSize(16777215, 38))
        self.rack_atc_user_5.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_atc_user_5.setStyleSheet(u"font: 15pt \"Probe Basic Bebas Mono\";\n"
"color: white;\n"
"background-color: #929695;\n"
"border: none;")
        self.rack_atc_user_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_188.addWidget(self.rack_atc_user_5)

        self.rack_atc_user_5_3978 = VCPSettingsLineEdit(self.widget_52)
        self.rack_atc_user_5_3978.setObjectName(u"rack_atc_user_5_3978")
        self.rack_atc_user_5_3978.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_atc_user_5_3978.sizePolicy().hasHeightForWidth())
        self.rack_atc_user_5_3978.setSizePolicy(sizePolicy11)
        self.rack_atc_user_5_3978.setMinimumSize(QSize(100, 31))
        self.rack_atc_user_5_3978.setMaximumSize(QSize(100, 31))
        self.rack_atc_user_5_3978.setFont(font)
        self.rack_atc_user_5_3978.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_atc_user_5_3978.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_188.addWidget(self.rack_atc_user_5_3978)


        self.verticalLayout_72.addLayout(self.horizontalLayout_188)

        self.rack_param_bottom_spacer_widget = QWidget(self.widget_52)
        self.rack_param_bottom_spacer_widget.setObjectName(u"rack_param_bottom_spacer_widget")

        self.verticalLayout_72.addWidget(self.rack_param_bottom_spacer_widget)


        self.verticalLayout_48.addWidget(self.widget_52)

        self.rack_id_update_subcallbutton = SubCallButton(self.rack_param_widget)
        self.rack_id_update_subcallbutton.setObjectName(u"rack_id_update_subcallbutton")
        sizePolicy6.setHeightForWidth(self.rack_id_update_subcallbutton.sizePolicy().hasHeightForWidth())
        self.rack_id_update_subcallbutton.setSizePolicy(sizePolicy6)
        self.rack_id_update_subcallbutton.setMaximumSize(QSize(16777215, 42))

        self.verticalLayout_48.addWidget(self.rack_id_update_subcallbutton)


        self.verticalLayout_5.addWidget(self.rack_param_widget)


        self.horizontalLayout_7.addWidget(self.widget_16)

        self.widget_14 = QWidget(self.tab_2)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(481, 0))
        self.widget_14.setMaximumSize(QSize(481, 16777215))
        self.spindle_tool_graphic_label = QLabel(self.widget_14)
        self.spindle_tool_graphic_label.setObjectName(u"spindle_tool_graphic_label")
        self.spindle_tool_graphic_label.setGeometry(QRect(70, 24, 300, 557))
        sizePolicy11.setHeightForWidth(self.spindle_tool_graphic_label.sizePolicy().hasHeightForWidth())
        self.spindle_tool_graphic_label.setSizePolicy(sizePolicy11)
        self.spindle_tool_graphic_label.setMinimumSize(QSize(300, 557))
        self.spindle_tool_graphic_label.setMaximumSize(QSize(300, 557))
        self.spindle_tool_graphic_label.setPixmap(QPixmap(u":/images/fork_heights.png"))
        self.spindle_tool_graphic_label.setScaledContents(True)
        self.widget_19 = QWidget(self.widget_14)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setGeometry(QRect(22, 224, 111, 81))
        self.widget_19.setStyleSheet(u".QWidget {\n"
"    background-color: #929695;\n"
"}")
        self.gridLayout = QGridLayout(self.widget_19)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.rack_safe_z_height_3982 = VCPSettingsLineEdit(self.widget_19)
        self.rack_safe_z_height_3982.setObjectName(u"rack_safe_z_height_3982")
        self.rack_safe_z_height_3982.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_safe_z_height_3982.sizePolicy().hasHeightForWidth())
        self.rack_safe_z_height_3982.setSizePolicy(sizePolicy11)
        self.rack_safe_z_height_3982.setMinimumSize(QSize(100, 31))
        self.rack_safe_z_height_3982.setMaximumSize(QSize(100, 31))
        self.rack_safe_z_height_3982.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_safe_z_height_3982.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.rack_safe_z_height_3982, 1, 0, 1, 1)

        self.label_safe_z = QLabel(self.widget_19)
        self.label_safe_z.setObjectName(u"label_safe_z")
        sizePolicy2.setHeightForWidth(self.label_safe_z.sizePolicy().hasHeightForWidth())
        self.label_safe_z.setSizePolicy(sizePolicy2)
        self.label_safe_z.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_safe_z.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_safe_z.setWordWrap(True)

        self.gridLayout.addWidget(self.label_safe_z, 0, 0, 1, 1)

        self.label_35 = QLabel(self.widget_14)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(117, 11, 201, 31))
        sizePolicy11.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy11)
        self.label_35.setStyleSheet(u"QLabel {\n"
"    background-color: #929695;\n"
"    color: white;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_35.setWordWrap(True)
        self.widget_20 = QWidget(self.widget_14)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setGeometry(QRect(308, 404, 111, 81))
        sizePolicy2.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy2)
        self.widget_20.setStyleSheet(u".QWidget {\n"
"    background-color: #929695;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget_20)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label_34 = QLabel(self.widget_20)
        self.label_34.setObjectName(u"label_34")
        sizePolicy2.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy2)
        self.label_34.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_34.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_34, 0, 0, 1, 1)

        self.rack_z_load_height_3981 = VCPSettingsLineEdit(self.widget_20)
        self.rack_z_load_height_3981.setObjectName(u"rack_z_load_height_3981")
        self.rack_z_load_height_3981.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_z_load_height_3981.sizePolicy().hasHeightForWidth())
        self.rack_z_load_height_3981.setSizePolicy(sizePolicy11)
        self.rack_z_load_height_3981.setMinimumSize(QSize(100, 31))
        self.rack_z_load_height_3981.setMaximumSize(QSize(100, 31))
        self.rack_z_load_height_3981.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_z_load_height_3981.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.rack_z_load_height_3981, 1, 0, 1, 1)

        self.line = QFrame(self.widget_14)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(76, 185, 3, 41))
        self.line.setStyleSheet(u"border: 3px solid white;\n"
"color: white;")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line_2 = QFrame(self.widget_14)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(361, 372, 3, 41))
        self.line_2.setStyleSheet(u"border: 3px solid white;\n"
"color: white;")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.spindle_tool_graphic_label.raise_()
        self.label_35.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.widget_20.raise_()
        self.widget_19.raise_()

        self.horizontalLayout_7.addWidget(self.widget_14)

        self.widget_17 = QWidget(self.tab_2)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy6.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy6)
        self.verticalLayout_3 = QVBoxLayout(self.widget_17)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 9)
        self.widget_15 = QWidget(self.widget_17)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy14.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy14)
        self.widget_15.setMinimumSize(QSize(650, 400))
        self.widget_15.setMaximumSize(QSize(650, 400))
        self.label_17 = QLabel(self.widget_15)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(149, 27, 353, 300))
        sizePolicy11.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy11)
        self.label_17.setPixmap(QPixmap(u":/images/fork_points.png"))
        self.rack_xy_widget = QWidget(self.widget_15)
        self.rack_xy_widget.setObjectName(u"rack_xy_widget")
        self.rack_xy_widget.setGeometry(QRect(18, 215, 130, 90))
        sizePolicy11.setHeightForWidth(self.rack_xy_widget.sizePolicy().hasHeightForWidth())
        self.rack_xy_widget.setSizePolicy(sizePolicy11)
        self.rack_xy_widget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.rack_xy_widget.setStyleSheet(u".QWidget {\n"
"    background-color: #929695;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.rack_xy_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 6, 0, 6)
        self.widget_26 = QWidget(self.rack_xy_widget)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.rack_x_widget = QLabel(self.widget_26)
        self.rack_x_widget.setObjectName(u"rack_x_widget")
        sizePolicy11.setHeightForWidth(self.rack_x_widget.sizePolicy().hasHeightForWidth())
        self.rack_x_widget.setSizePolicy(sizePolicy11)
        self.rack_x_widget.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.rack_x_widget)

        self.rack_pocket_1_x_3983 = VCPSettingsLineEdit(self.widget_26)
        self.rack_pocket_1_x_3983.setObjectName(u"rack_pocket_1_x_3983")
        self.rack_pocket_1_x_3983.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_pocket_1_x_3983.sizePolicy().hasHeightForWidth())
        self.rack_pocket_1_x_3983.setSizePolicy(sizePolicy11)
        self.rack_pocket_1_x_3983.setMinimumSize(QSize(100, 31))
        self.rack_pocket_1_x_3983.setMaximumSize(QSize(100, 31))
        self.rack_pocket_1_x_3983.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_pocket_1_x_3983.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.rack_pocket_1_x_3983)


        self.verticalLayout_6.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.rack_xy_widget)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rack_y_widget = QLabel(self.widget_27)
        self.rack_y_widget.setObjectName(u"rack_y_widget")
        sizePolicy11.setHeightForWidth(self.rack_y_widget.sizePolicy().hasHeightForWidth())
        self.rack_y_widget.setSizePolicy(sizePolicy11)
        self.rack_y_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.rack_y_widget.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_11.addWidget(self.rack_y_widget)

        self.rack_pocket_1_y_3984 = VCPSettingsLineEdit(self.widget_27)
        self.rack_pocket_1_y_3984.setObjectName(u"rack_pocket_1_y_3984")
        self.rack_pocket_1_y_3984.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_pocket_1_y_3984.sizePolicy().hasHeightForWidth())
        self.rack_pocket_1_y_3984.setSizePolicy(sizePolicy11)
        self.rack_pocket_1_y_3984.setMinimumSize(QSize(100, 31))
        self.rack_pocket_1_y_3984.setMaximumSize(QSize(100, 31))
        self.rack_pocket_1_y_3984.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_pocket_1_y_3984.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.rack_pocket_1_y_3984)


        self.verticalLayout_6.addWidget(self.widget_27)

        self.widget_25 = QWidget(self.widget_15)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setGeometry(QRect(290, 280, 130, 90))
        sizePolicy11.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy11)
        self.widget_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.widget_25.setStyleSheet(u".QWidget {\n"
"    background-color: #929695;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.widget_25)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 6, 0, 6)
        self.widget_28 = QWidget(self.widget_25)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.widget_28)
        self.label_43.setObjectName(u"label_43")
        sizePolicy11.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy11)
        self.label_43.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.label_43)

        self.pocket_1_x_clearance_3987 = VCPSettingsLineEdit(self.widget_28)
        self.pocket_1_x_clearance_3987.setObjectName(u"pocket_1_x_clearance_3987")
        self.pocket_1_x_clearance_3987.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.pocket_1_x_clearance_3987.sizePolicy().hasHeightForWidth())
        self.pocket_1_x_clearance_3987.setSizePolicy(sizePolicy11)
        self.pocket_1_x_clearance_3987.setMinimumSize(QSize(100, 31))
        self.pocket_1_x_clearance_3987.setMaximumSize(QSize(100, 31))
        self.pocket_1_x_clearance_3987.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pocket_1_x_clearance_3987.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.pocket_1_x_clearance_3987)


        self.verticalLayout_7.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_25)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.widget_29)
        self.label_44.setObjectName(u"label_44")
        sizePolicy11.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy11)
        self.label_44.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_44.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_13.addWidget(self.label_44)

        self.pocket_1_y_clearance_3988 = VCPSettingsLineEdit(self.widget_29)
        self.pocket_1_y_clearance_3988.setObjectName(u"pocket_1_y_clearance_3988")
        self.pocket_1_y_clearance_3988.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.pocket_1_y_clearance_3988.sizePolicy().hasHeightForWidth())
        self.pocket_1_y_clearance_3988.setSizePolicy(sizePolicy11)
        self.pocket_1_y_clearance_3988.setMinimumSize(QSize(100, 31))
        self.pocket_1_y_clearance_3988.setMaximumSize(QSize(100, 31))
        self.pocket_1_y_clearance_3988.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pocket_1_y_clearance_3988.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.pocket_1_y_clearance_3988)


        self.verticalLayout_7.addWidget(self.widget_29)

        self.widget_32 = QWidget(self.widget_15)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setGeometry(QRect(504, 215, 130, 90))
        sizePolicy11.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy11)
        self.widget_32.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.widget_32.setStyleSheet(u".QWidget {\n"
"    background-color: #929695;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.widget_32)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 6, 0, 6)
        self.widget_30 = QWidget(self.widget_32)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.widget_30)
        self.label_46.setObjectName(u"label_46")
        sizePolicy11.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy11)
        self.label_46.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_15.addWidget(self.label_46)

        self.rack_pocket_2_x_3985 = VCPSettingsLineEdit(self.widget_30)
        self.rack_pocket_2_x_3985.setObjectName(u"rack_pocket_2_x_3985")
        self.rack_pocket_2_x_3985.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_pocket_2_x_3985.sizePolicy().hasHeightForWidth())
        self.rack_pocket_2_x_3985.setSizePolicy(sizePolicy11)
        self.rack_pocket_2_x_3985.setMinimumSize(QSize(100, 31))
        self.rack_pocket_2_x_3985.setMaximumSize(QSize(100, 31))
        self.rack_pocket_2_x_3985.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_pocket_2_x_3985.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.rack_pocket_2_x_3985)


        self.verticalLayout_8.addWidget(self.widget_30)

        self.widget_31 = QWidget(self.widget_32)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.widget_31)
        self.label_47.setObjectName(u"label_47")
        sizePolicy11.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy11)
        self.label_47.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_47.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_16.addWidget(self.label_47)

        self.rack_pocket_2_y_3986 = VCPSettingsLineEdit(self.widget_31)
        self.rack_pocket_2_y_3986.setObjectName(u"rack_pocket_2_y_3986")
        self.rack_pocket_2_y_3986.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.rack_pocket_2_y_3986.sizePolicy().hasHeightForWidth())
        self.rack_pocket_2_y_3986.setSizePolicy(sizePolicy11)
        self.rack_pocket_2_y_3986.setMinimumSize(QSize(100, 31))
        self.rack_pocket_2_y_3986.setMaximumSize(QSize(100, 31))
        self.rack_pocket_2_y_3986.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.rack_pocket_2_y_3986.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.rack_pocket_2_y_3986)


        self.verticalLayout_8.addWidget(self.widget_31)

        self.label_36 = QLabel(self.widget_15)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(19, 160, 130, 51))
        sizePolicy2.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy2)
        self.label_36.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_36.setWordWrap(True)
        self.label_37 = QLabel(self.widget_15)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(290, 227, 130, 51))
        sizePolicy2.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy2)
        self.label_37.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_37.setWordWrap(True)
        self.label_39 = QLabel(self.widget_15)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(504, 160, 130, 51))
        sizePolicy2.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy2)
        self.label_39.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_39.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.widget_15)

        self.widget_18 = QWidget(self.widget_17)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy14.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy14)
        self.widget_18.setMaximumSize(QSize(650, 16777215))

        self.verticalLayout_3.addWidget(self.widget_18)

        self.rack_mdi_2 = MDIEntry(self.widget_17)
        self.rack_mdi_2.setObjectName(u"rack_mdi_2")
        self.rack_mdi_2.setMinimumSize(QSize(0, 42))
        self.rack_mdi_2.setMaximumSize(QSize(16777215, 42))
        self.rack_mdi_2.setFont(font)
        self.rack_mdi_2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_3.addWidget(self.rack_mdi_2)


        self.horizontalLayout_7.addWidget(self.widget_17)

        self.rack_tab_widget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.rack_tab_widget)


        self.retranslateUi(RACK_ATC)
        self.tool_number_entry_atc_page.returnPressed.connect(self.m6_tool_call_button_atc_page.click)
        self.load_spindle_tool_number.returnPressed.connect(self.load_spindle_button.click)
        self.rack_pocket_1_x_3983.editingFinished.connect(self.rack_id_update_subcallbutton.click)
        self.rack_pocket_1_y_3984.editingFinished.connect(self.rack_id_update_subcallbutton.click)
        self.rack_safe_z_height_3982.editingFinished.connect(self.rack_id_update_subcallbutton.click)
        self.rack_z_load_height_3981.editingFinished.connect(self.rack_id_update_subcallbutton.click)
        self.pocket_1_x_clearance_3987.editingFinished.connect(self.rack_id_update_subcallbutton.click)
        self.pocket_1_y_clearance_3988.editingFinished.connect(self.rack_id_update_subcallbutton.click)
        self.rack_pocket_2_x_3985.editingFinished.connect(self.rack_id_update_subcallbutton.click)
        self.rack_pocket_2_y_3986.editingFinished.connect(self.rack_id_update_subcallbutton.click)
        self.rack_traverse_speed_3980.editingFinished.connect(self.rack_id_update_subcallbutton.click)

        self.rack_tab_widget.setCurrentIndex(0)
        self.user_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RACK_ATC)
    # setupUi

    def retranslateUi(self, RACK_ATC):
        RACK_ATC.setWindowTitle(QCoreApplication.translate("RACK_ATC", u"rack_atc", None))
        self.current_tools_header.setText(QCoreApplication.translate("RACK_ATC", u"CURRENT PROGRAM TOOLS", None))
        self.checkBox.setText("")
        self.checkBox_4.setText("")
        self.checkBox_2.setText("")
        self.checkBox_41.setText("")
        self.checkBox_3.setText("")
        self.checkBox_34.setText("")
        self.checkBox_6.setText("")
        self.checkBox_31.setText("")
        self.checkBox_5.setText("")
        self.checkBox_39.setText("")
        self.checkBox_9.setText("")
        self.checkBox_38.setText("")
        self.checkBox_7.setText("")
        self.checkBox_37.setText("")
        self.checkBox_8.setText("")
        self.checkBox_33.setText("")
        self.checkBox_10.setText("")
        self.checkBox_40.setText("")
        self.checkBox_11.setText("")
        self.checkBox_35.setText("")
        self.checkBox_12.setText("")
        self.checkBox_30.setText("")
        self.checkBox_13.setText("")
        self.checkBox_32.setText("")
        self.checkBox_14.setText("")
        self.checkBox_42.setText("")
        self.checkBox_36.setText("")
        self.checkBox_29.setText("")
        self.label_5.setText("")
        self.statuslabel.setText("")
        self.statuslabel.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"program_tool_list\", \"property\": \"Text\", \"expression\": \"\\\"\\\\n\\\".join(f\\\"T{ch[1][x][0]}\\\" for\\nx in ch[0])\", \"channels\": [{\"url\": \"gcode_properties:tools\", \"trigger\": true}, {\"url\": \"status:tool_table\", \"trigger\": false}]}]", None))
#if QT_CONFIG(tooltip)
        self.reference_carousel_2.setToolTip(QCoreApplication.translate("RACK_ATC", u"M13 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.reference_carousel_2.setText(QCoreApplication.translate("RACK_ATC", u"REF RACK DATA", None))
        self.reference_carousel_2.setProperty(u"MDICommand", QCoreApplication.translate("RACK_ATC", u"M13", None))
        self.user_tab_widget.setTabText(self.user_tab_widget.indexOf(self.program_tools_tab), QCoreApplication.translate("RACK_ATC", u"PROGRAM TOOLS", None))
        self.user_tab_widget.setTabText(self.user_tab_widget.indexOf(self.manual_atc_tab), QCoreApplication.translate("RACK_ATC", u"MANUAL ATC", None))
        self.tool_information_rack.setText(QCoreApplication.translate("RACK_ATC", u"No Tool Loaded", None))
        self.tool_information_rack.setProperty(u"format", QCoreApplication.translate("RACK_ATC", u"{:.3f}", None))
        self.tool_information_rack.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?remark\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Tool Comment\"}]", None))
        self.tool_information_rack.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField14", None))
        self.spindle_image_label.setText("")
        self.loaded_spindle_tool_number.setText(QCoreApplication.translate("RACK_ATC", u"T0", None))
        self.loaded_spindle_tool_number.setProperty(u"format", QCoreApplication.translate("RACK_ATC", u"{:.3f}", None))
        self.loaded_spindle_tool_number.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"channels\": [{\"url\": \"status:tool_in_spindle?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"'T' + ch[0]\", \"name\": \"current tool\"}]", None))
        self.loaded_spindle_tool_number.setProperty(u"statusItem", QCoreApplication.translate("RACK_ATC", u"tool_offset.3", None))
        self.loaded_spindle_tool_number.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField16", None))
        self.mdi_entry_box_rack_tab.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"MDI", None))
        self.mdi_entry_box_rack_tab.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField15", None))
        self.atc_loading_panel_header.setText(QCoreApplication.translate("RACK_ATC", u"ATC AUTOMATIC CONTROL PANEL", None))
        self.load_spindle_tool_number.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.load_spindle_tool_number.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(0)\", \"name\": \"update tool num\"}, {\"channels\": [{\"url\": \"status:task_state?text\", \"trigger\": true}, {\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] == 'On' and ch[1] == 'Idle'\", \"name\": \"enable/disable\"}]", None))
        self.load_spindle_tool_number.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField17", None))
        self.load_spindle_button.setText(QCoreApplication.translate("RACK_ATC", u"LOAD SPINDLE", None))
        self.load_spindle_button.setProperty(u"filename", QCoreApplication.translate("RACK_ATC", u"load_spindle_safety.ngc", None))
        self.remove_tool_button.setText(QCoreApplication.translate("RACK_ATC", u"UNLOAD SPINDLE", None))
        self.remove_tool_button.setProperty(u"filename", QCoreApplication.translate("RACK_ATC", u"unload_spindle.ngc", None))
        self.store_tool_in_spindle.setText(QCoreApplication.translate("RACK_ATC", u"STORE TOOL IN RACK", None))
        self.store_tool_in_spindle.setProperty(u"filename", QCoreApplication.translate("RACK_ATC", u"store_tool_in_carousel.ngc", None))
        self.tool_number_entry_atc_page.setText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.tool_number_entry_atc_page.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(ch[0])\", \"name\": \"update tool num\"}, {\"channels\": [{\"url\": \"status:task_state?text\", \"trigger\": true}, {\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] == 'On' and ch[1] == 'Idle'\", \"name\": \"enable/disable\"}]", None))
        self.tool_number_entry_atc_page.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField17", None))
        self.m6_tool_call_button_atc_page.setText(QCoreApplication.translate("RACK_ATC", u"M6 G43", None))
        self.m6_tool_call_button_atc_page.setProperty(u"filename", QCoreApplication.translate("RACK_ATC", u"m6_tool_call_atc_page.ngc", None))
        self.tool_touch_off_button_atc.setText(QCoreApplication.translate("RACK_ATC", u"TOUCH OFF CURRENT TOOL", None))
        self.tool_touch_off_button_atc.setProperty(u"filename", QCoreApplication.translate("RACK_ATC", u"tool_touch_off.ngc", None))
        self.rack_tab_widget.setTabText(self.rack_tab_widget.indexOf(self.tab), QCoreApplication.translate("RACK_ATC", u"RACK ATC", None))
        self.rack_param_header.setText(QCoreApplication.translate("RACK_ATC", u"RACK ATC PARAMETERS", None))
        self.label_15.setText(QCoreApplication.translate("RACK_ATC", u"ATC RACK ID", None))
        self.atc_rack_id.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.atc_rack_id.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.0f}", None))
        self.atc_rack_id.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.rack-id", None))
        self.atc_rack_id.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.atc_rack_id.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField15", None))
        self.label_120.setText(QCoreApplication.translate("RACK_ATC", u"POCKET COUNT", None))
        self.rack_pocket_count.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_pocket_count.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.0f}", None))
        self.rack_pocket_count.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.pocket-count", None))
        self.rack_pocket_count.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField15", None))
        self.label_135.setText(QCoreApplication.translate("RACK_ATC", u"ATC TRAVERSE FR", None))
        self.rack_traverse_speed_3980.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_traverse_speed_3980.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.0f}", None))
        self.rack_traverse_speed_3980.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.rack-traverse-speed", None))
        self.rack_traverse_speed_3980.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_traverse_speed_3980.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField15", None))
        self.rack_atc_user_1.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.user-param-1", None))
        self.rack_atc_user_1_3974.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_atc_user_1_3974.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_atc_user_1_3974.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.user-1-param", None))
        self.rack_atc_user_1_3974.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_atc_user_1_3974.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField15", None))
        self.rack_atc_user_2.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.user-param-2", None))
        self.rack_atc_user_2_3975.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_atc_user_2_3975.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_atc_user_2_3975.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.user-2-param", None))
        self.rack_atc_user_2_3975.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_atc_user_2_3975.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField15", None))
        self.rack_atc_user_3.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.user-param-3", None))
        self.rack_atc_user_3_3976.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_atc_user_3_3976.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_atc_user_3_3976.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.user-3-param", None))
        self.rack_atc_user_3_3976.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_atc_user_3_3976.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField15", None))
        self.rack_atc_user_4.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.user-param-4", None))
        self.rack_atc_user_4_3977.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_atc_user_4_3977.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_atc_user_4_3977.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.user-4-param", None))
        self.rack_atc_user_4_3977.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_atc_user_4_3977.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField15", None))
        self.rack_atc_user_5.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.user-param-5", None))
        self.rack_atc_user_5_3978.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_atc_user_5_3978.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_atc_user_5_3978.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.user-5-param", None))
        self.rack_atc_user_5_3978.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_atc_user_5_3978.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField15", None))
        self.rack_id_update_subcallbutton.setText(QCoreApplication.translate("RACK_ATC", u"UPDATE RACK ATC PARAMETERS", None))
        self.rack_id_update_subcallbutton.setProperty(u"filename", QCoreApplication.translate("RACK_ATC", u"rack_id_calc.ngc", None))
        self.spindle_tool_graphic_label.setText("")
        self.rack_safe_z_height_3982.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_safe_z_height_3982.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_safe_z_height_3982.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.safe-z-height", None))
        self.rack_safe_z_height_3982.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_safe_z_height_3982.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField17", None))
        self.label_safe_z.setText(QCoreApplication.translate("RACK_ATC", u"SAFE Z", None))
        self.label_35.setText(QCoreApplication.translate("RACK_ATC", u"HOME Z AXIS ZERO POSITION", None))
        self.label_34.setText(QCoreApplication.translate("RACK_ATC", u"LOAD HEIGHT", None))
        self.rack_z_load_height_3981.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_z_load_height_3981.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_z_load_height_3981.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.z-load-height", None))
        self.rack_z_load_height_3981.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_z_load_height_3981.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField17", None))
        self.rack_x_widget.setText(QCoreApplication.translate("RACK_ATC", u"X", None))
        self.rack_pocket_1_x_3983.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_pocket_1_x_3983.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_pocket_1_x_3983.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.pocket-1-x", None))
        self.rack_pocket_1_x_3983.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_pocket_1_x_3983.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField17", None))
        self.rack_y_widget.setText(QCoreApplication.translate("RACK_ATC", u"Y", None))
        self.rack_pocket_1_y_3984.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_pocket_1_y_3984.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_pocket_1_y_3984.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.pocket-1-y", None))
        self.rack_pocket_1_y_3984.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_pocket_1_y_3984.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField17", None))
        self.label_43.setText(QCoreApplication.translate("RACK_ATC", u"X", None))
        self.pocket_1_x_clearance_3987.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.pocket_1_x_clearance_3987.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.pocket_1_x_clearance_3987.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.pocket-1-x-clearance", None))
        self.pocket_1_x_clearance_3987.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.pocket_1_x_clearance_3987.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField17", None))
        self.label_44.setText(QCoreApplication.translate("RACK_ATC", u"Y", None))
        self.pocket_1_y_clearance_3988.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.pocket_1_y_clearance_3988.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.pocket_1_y_clearance_3988.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.pocket-1-y-clearance", None))
        self.pocket_1_y_clearance_3988.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.pocket_1_y_clearance_3988.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField17", None))
        self.label_46.setText(QCoreApplication.translate("RACK_ATC", u"X", None))
        self.rack_pocket_2_x_3985.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_pocket_2_x_3985.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_pocket_2_x_3985.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.pocket-2-x", None))
        self.rack_pocket_2_x_3985.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_pocket_2_x_3985.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField17", None))
        self.label_47.setText(QCoreApplication.translate("RACK_ATC", u"Y", None))
        self.rack_pocket_2_y_3986.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"0", None))
        self.rack_pocket_2_y_3986.setProperty(u"textFormat", QCoreApplication.translate("RACK_ATC", u"{:.4f}", None))
        self.rack_pocket_2_y_3986.setProperty(u"settingName", QCoreApplication.translate("RACK_ATC", u"rack-atc-setup.pocket-2-y", None))
        self.rack_pocket_2_y_3986.setProperty(u"rules", QCoreApplication.translate("RACK_ATC", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.rack_pocket_2_y_3986.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField17", None))
        self.label_36.setText(QCoreApplication.translate("RACK_ATC", u"P1 MACHINE POSITION", None))
        self.label_37.setText(QCoreApplication.translate("RACK_ATC", u"P1 CLEARANCE MACHINE POS", None))
        self.label_39.setText(QCoreApplication.translate("RACK_ATC", u"P2 MACHINE POSITION", None))
        self.rack_mdi_2.setPlaceholderText(QCoreApplication.translate("RACK_ATC", u"MDI", None))
        self.rack_mdi_2.setProperty(u"styleSet", QCoreApplication.translate("RACK_ATC", u"dataField15", None))
        self.rack_tab_widget.setTabText(self.rack_tab_widget.indexOf(self.tab_2), QCoreApplication.translate("RACK_ATC", u"RACK SETUP", None))
    # retranslateUi

