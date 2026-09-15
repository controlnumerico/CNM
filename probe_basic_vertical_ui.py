# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'probe_basic_vertical.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton
from qtpyvcp.widgets.display_widgets.gcode_backplot.gcode_backplot import GcodeBackplot
from qtpyvcp.widgets.display_widgets.load_meter import LoadMeter
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.widgets.input_widgets.action_slider import ActionSlider
from qtpyvcp.widgets.input_widgets.file_system import (FileSystemTable, RemovableDeviceComboBox)
from qtpyvcp.widgets.input_widgets.gcode_editor import GcodeEditor
from qtpyvcp.widgets.input_widgets.jog_increment import JogIncrementWidget
from qtpyvcp.widgets.input_widgets.mdientry_widget import MDIEntry
from qtpyvcp.widgets.input_widgets.recent_file_combobox import RecentFileComboBox
from qtpyvcp.widgets.input_widgets.tool_table import ToolTable
import probe_basic_rc
import probe_basic_rc
import probe_basic_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1924, 1083)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Probe Basic Bebas Mono"])
        font.setPointSize(11)
        Form.setFont(font)
        Form.setToolTipDuration(-1)
        Form.setStyleSheet(u"Form {\n"
"bottom-margin: 0px;\n"
"}")
        Form.setDocumentMode(False)
        Form.setProperty(u"promptAtExit", False)
        Form.setProperty(u"promot_on_exit", False)
        self.actionExit = QAction(Form)
        self.actionExit.setObjectName(u"actionExit")
        self.actionOpen = QAction(Form)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(Form)
        self.actionClose.setObjectName(u"actionClose")
        self.actionReload = QAction(Form)
        self.actionReload.setObjectName(u"actionReload")
        self.actionSave_As = QAction(Form)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionHome_X = QAction(Form)
        self.actionHome_X.setObjectName(u"actionHome_X")
        self.actionHome_Y = QAction(Form)
        self.actionHome_Y.setObjectName(u"actionHome_Y")
        self.actionHome_Z = QAction(Form)
        self.actionHome_Z.setObjectName(u"actionHome_Z")
        self.action_EmergencyStop_toggle = QAction(Form)
        self.action_EmergencyStop_toggle.setObjectName(u"action_EmergencyStop_toggle")
        self.action_MachinePower_toggle = QAction(Form)
        self.action_MachinePower_toggle.setObjectName(u"action_MachinePower_toggle")
        self.action_MachinePower_toggle.setProperty(u"_axis", 2)
        self.actionHome_All = QAction(Form)
        self.actionHome_All.setObjectName(u"actionHome_All")
        self.actionRun_Program = QAction(Form)
        self.actionRun_Program.setObjectName(u"actionRun_Program")
        self.actionFile1 = QAction(Form)
        self.actionFile1.setObjectName(u"actionFile1")
        self.actionReport_Actual_Position = QAction(Form)
        self.actionReport_Actual_Position.setObjectName(u"actionReport_Actual_Position")
        self.actionReport_Actual_Position.setCheckable(True)
        self.actionTest = QAction(Form)
        self.actionTest.setObjectName(u"actionTest")
        self.action_Mist_toggle = QAction(Form)
        self.action_Mist_toggle.setObjectName(u"action_Mist_toggle")
        self.action_Mist_toggle.setCheckable(True)
        self.action_Flood_toggle = QAction(Form)
        self.action_Flood_toggle.setObjectName(u"action_Flood_toggle")
        self.action_Flood_toggle.setCheckable(True)
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_31 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(-1, -1, 0, 3)
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, -1, 0, -1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(129, 133, 132, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(85, 255, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush2 = QBrush(QColor(145, 141, 126, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        self.tabWidget.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Probe Basic Bebas Mono"])
        font1.setPointSize(15)
        self.tabWidget.setFont(font1)
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_24 = QFrame(self.tab_2)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy2)
        self.frame_24.setMinimumSize(QSize(1, 0))
        self.frame_24.setMaximumSize(QSize(1, 16777215))
        self.frame_24.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"background-color: transparent;\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_24)

        self.splitter = QSplitter(self.tab_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFocusPolicy(Qt.NoFocus)
        self.splitter.setLineWidth(2)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setFocusPolicy(Qt.NoFocus)
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.recentfilecombobox = RecentFileComboBox(self.verticalLayoutWidget)
        self.recentfilecombobox.setObjectName(u"recentfilecombobox")
        self.recentfilecombobox.setMinimumSize(QSize(148, 30))
        self.recentfilecombobox.setFocusPolicy(Qt.NoFocus)
        self.recentfilecombobox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	padding: 1px 23px 1px 3px;\n"
"	min-width: 6em;\n"
"	color: #ffffff;\n"
"    font: 12pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" 	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"    font: 12pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"QComboBox::down-arrow {\n"
"     image: url(:/images/combobox-arrow.png);\n"
"}\n"
" \n"
"QComboBox QAbstractItemView{\n"
"	background-color: #4f4f4f;\n"
"	color: #999999;\n"
" 	selection-background-color: #999999;\n"
"	selection-color: #4f4f4f;\n"
"}")

        self.verticalLayout_2.addWidget(self.recentfilecombobox)

        self.gcodeeditor = GcodeEditor(self.verticalLayoutWidget)
        self.gcodeeditor.setObjectName(u"gcodeeditor")
        self.gcodeeditor.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.gcodeeditor)

        self.mdi_entry_box = MDIEntry(self.verticalLayoutWidget)
        self.mdi_entry_box.setObjectName(u"mdi_entry_box")
        self.mdi_entry_box.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"Probe Basic Bebas Mono"])
        font2.setPointSize(14)
        self.mdi_entry_box.setFont(font2)
        self.mdi_entry_box.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_2.addWidget(self.mdi_entry_box)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.gcodebackplot = GcodeBackplot(self.splitter)
        self.gcodebackplot.setObjectName(u"gcodebackplot")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gcodebackplot.sizePolicy().hasHeightForWidth())
        self.gcodebackplot.setSizePolicy(sizePolicy3)
        self.gcodebackplot.setFocusPolicy(Qt.NoFocus)
        self.gcodebackplot.setProperty(u"renderProgramAlpha", True)
        self.gcodebackplot.setBackgroundColor(QColor(0, 0, 0))
        self.splitter.addWidget(self.gcodebackplot)

        self.horizontalLayout.addWidget(self.splitter)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.verticalLayout_5 = QVBoxLayout(self.tab_15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setSpacing(15)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_120.setContentsMargins(15, 20, 15, 20)
        self.frame_35 = QFrame(self.tab_15)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy2.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy2)
        self.frame_35.setMinimumSize(QSize(500, 0))
        self.frame_35.setMaximumSize(QSize(500, 16777215))
        self.frame_35.setStyleSheet(u"QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_35)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(5, -1, 5, -1)
        self.x_axis_button_30 = QPushButton(self.frame_35)
        self.x_axis_button_30.setObjectName(u"x_axis_button_30")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.x_axis_button_30.sizePolicy().hasHeightForWidth())
        self.x_axis_button_30.setSizePolicy(sizePolicy4)
        self.x_axis_button_30.setMinimumSize(QSize(110, 30))
        self.x_axis_button_30.setMaximumSize(QSize(110, 30))
        self.x_axis_button_30.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_30.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/folder_up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.x_axis_button_30.setIcon(icon)
        self.x_axis_button_30.setIconSize(QSize(30, 17))

        self.horizontalLayout_124.addWidget(self.x_axis_button_30)

        self.removabledevicecombobox = RemovableDeviceComboBox(self.frame_35)
        self.removabledevicecombobox.setObjectName(u"removabledevicecombobox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.removabledevicecombobox.sizePolicy().hasHeightForWidth())
        self.removabledevicecombobox.setSizePolicy(sizePolicy5)
        self.removabledevicecombobox.setMinimumSize(QSize(0, 30))
        self.removabledevicecombobox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_124.addWidget(self.removabledevicecombobox)

        self.x_axis_button_32 = QPushButton(self.frame_35)
        self.x_axis_button_32.setObjectName(u"x_axis_button_32")
        sizePolicy4.setHeightForWidth(self.x_axis_button_32.sizePolicy().hasHeightForWidth())
        self.x_axis_button_32.setSizePolicy(sizePolicy4)
        self.x_axis_button_32.setMinimumSize(QSize(100, 30))
        self.x_axis_button_32.setMaximumSize(QSize(100, 30))
        self.x_axis_button_32.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_32.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_124.addWidget(self.x_axis_button_32)


        self.verticalLayout_37.addLayout(self.horizontalLayout_124)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.filesystemtable_2 = FileSystemTable(self.frame_35)
        self.filesystemtable_2.setObjectName(u"filesystemtable_2")
        self.filesystemtable_2.setFocusPolicy(Qt.ClickFocus)
        self.filesystemtable_2.setStyleSheet(u"FileSystemTable {\n"
"	color: black;\n"
"   	border: 4px;\n"
"	border-color: rgb(120, 120, 120);\n"
"	border-style: solid;\n"
"	background-color: rgb(238, 238, 236);\n"
"    font: 12pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: rgb(220, 220, 220);\n"
"	color: black;\n"
"    border: none;\n"
"	border-radius:none;\n"
"	border-style: none;\n"
"	font: 13pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.filesystemtable_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.filesystemtable_2.setShowGrid(False)

        self.horizontalLayout_125.addWidget(self.filesystemtable_2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_125)

        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.x_axis_button_33 = QPushButton(self.frame_35)
        self.x_axis_button_33.setObjectName(u"x_axis_button_33")
        sizePolicy4.setHeightForWidth(self.x_axis_button_33.sizePolicy().hasHeightForWidth())
        self.x_axis_button_33.setSizePolicy(sizePolicy4)
        self.x_axis_button_33.setMinimumSize(QSize(90, 30))
        self.x_axis_button_33.setMaximumSize(QSize(90, 30))
        self.x_axis_button_33.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_33.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.x_axis_button_33.setIcon(icon1)
        self.x_axis_button_33.setIconSize(QSize(14, 14))

        self.horizontalLayout_126.addWidget(self.x_axis_button_33)

        self.x_axis_button_37 = QPushButton(self.frame_35)
        self.x_axis_button_37.setObjectName(u"x_axis_button_37")
        sizePolicy4.setHeightForWidth(self.x_axis_button_37.sizePolicy().hasHeightForWidth())
        self.x_axis_button_37.setSizePolicy(sizePolicy4)
        self.x_axis_button_37.setMinimumSize(QSize(100, 30))
        self.x_axis_button_37.setMaximumSize(QSize(100, 30))
        self.x_axis_button_37.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_37.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/images/new_file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.x_axis_button_37.setIcon(icon2)
        self.x_axis_button_37.setIconSize(QSize(12, 16))

        self.horizontalLayout_126.addWidget(self.x_axis_button_37)

        self.x_axis_button_35 = QPushButton(self.frame_35)
        self.x_axis_button_35.setObjectName(u"x_axis_button_35")
        sizePolicy4.setHeightForWidth(self.x_axis_button_35.sizePolicy().hasHeightForWidth())
        self.x_axis_button_35.setSizePolicy(sizePolicy4)
        self.x_axis_button_35.setMinimumSize(QSize(125, 30))
        self.x_axis_button_35.setMaximumSize(QSize(125, 30))
        self.x_axis_button_35.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_35.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/new_folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.x_axis_button_35.setIcon(icon3)
        self.x_axis_button_35.setIconSize(QSize(28, 15))

        self.horizontalLayout_126.addWidget(self.x_axis_button_35)

        self.x_axis_button_34 = QPushButton(self.frame_35)
        self.x_axis_button_34.setObjectName(u"x_axis_button_34")
        sizePolicy4.setHeightForWidth(self.x_axis_button_34.sizePolicy().hasHeightForWidth())
        self.x_axis_button_34.setSizePolicy(sizePolicy4)
        self.x_axis_button_34.setMinimumSize(QSize(90, 30))
        self.x_axis_button_34.setMaximumSize(QSize(90, 30))
        self.x_axis_button_34.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_34.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_126.addWidget(self.x_axis_button_34)


        self.verticalLayout_37.addLayout(self.horizontalLayout_126)


        self.horizontalLayout_120.addWidget(self.frame_35)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setSpacing(15)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_36.setContentsMargins(0, 110, 0, 100)
        self.copy_from_usb_2 = QPushButton(self.tab_15)
        self.copy_from_usb_2.setObjectName(u"copy_from_usb_2")
        sizePolicy4.setHeightForWidth(self.copy_from_usb_2.sizePolicy().hasHeightForWidth())
        self.copy_from_usb_2.setSizePolicy(sizePolicy4)
        self.copy_from_usb_2.setMinimumSize(QSize(60, 90))
        self.copy_from_usb_2.setMaximumSize(QSize(60, 90))
        self.copy_from_usb_2.setFocusPolicy(Qt.NoFocus)
        self.copy_from_usb_2.setLayoutDirection(Qt.RightToLeft)
        self.copy_from_usb_2.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 4px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/images/tall_right_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.copy_from_usb_2.setIcon(icon4)
        self.copy_from_usb_2.setIconSize(QSize(18, 60))

        self.verticalLayout_36.addWidget(self.copy_from_usb_2)

        self.copy_to_usb_2 = QPushButton(self.tab_15)
        self.copy_to_usb_2.setObjectName(u"copy_to_usb_2")
        sizePolicy4.setHeightForWidth(self.copy_to_usb_2.sizePolicy().hasHeightForWidth())
        self.copy_to_usb_2.setSizePolicy(sizePolicy4)
        self.copy_to_usb_2.setMinimumSize(QSize(60, 90))
        self.copy_to_usb_2.setMaximumSize(QSize(60, 90))
        self.copy_to_usb_2.setFocusPolicy(Qt.NoFocus)
        self.copy_to_usb_2.setLayoutDirection(Qt.LeftToRight)
        self.copy_to_usb_2.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 8px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/tall_left_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.copy_to_usb_2.setIcon(icon5)
        self.copy_to_usb_2.setIconSize(QSize(28, 60))

        self.verticalLayout_36.addWidget(self.copy_to_usb_2)


        self.horizontalLayout_120.addLayout(self.verticalLayout_36)

        self.frame_34 = QFrame(self.tab_15)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy2.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy2)
        self.frame_34.setMinimumSize(QSize(500, 0))
        self.frame_34.setMaximumSize(QSize(500, 16777215))
        self.frame_34.setStyleSheet(u"QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_34)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(5, -1, 5, -1)
        self.x_axis_button_23 = QPushButton(self.frame_34)
        self.x_axis_button_23.setObjectName(u"x_axis_button_23")
        sizePolicy4.setHeightForWidth(self.x_axis_button_23.sizePolicy().hasHeightForWidth())
        self.x_axis_button_23.setSizePolicy(sizePolicy4)
        self.x_axis_button_23.setMinimumSize(QSize(110, 30))
        self.x_axis_button_23.setMaximumSize(QSize(110, 30))
        self.x_axis_button_23.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_23.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_axis_button_23.setIcon(icon)
        self.x_axis_button_23.setIconSize(QSize(30, 17))

        self.horizontalLayout_121.addWidget(self.x_axis_button_23)

        self.recentfilecombobox_2 = RecentFileComboBox(self.frame_34)
        self.recentfilecombobox_2.setObjectName(u"recentfilecombobox_2")
        sizePolicy5.setHeightForWidth(self.recentfilecombobox_2.sizePolicy().hasHeightForWidth())
        self.recentfilecombobox_2.setSizePolicy(sizePolicy5)
        self.recentfilecombobox_2.setMinimumSize(QSize(0, 30))
        self.recentfilecombobox_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_121.addWidget(self.recentfilecombobox_2)

        self.x_axis_button_26 = QPushButton(self.frame_34)
        self.x_axis_button_26.setObjectName(u"x_axis_button_26")
        sizePolicy4.setHeightForWidth(self.x_axis_button_26.sizePolicy().hasHeightForWidth())
        self.x_axis_button_26.setSizePolicy(sizePolicy4)
        self.x_axis_button_26.setMinimumSize(QSize(100, 30))
        self.x_axis_button_26.setMaximumSize(QSize(100, 30))
        self.x_axis_button_26.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_26.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_121.addWidget(self.x_axis_button_26)


        self.verticalLayout_35.addLayout(self.horizontalLayout_121)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.filesystemtable = FileSystemTable(self.frame_34)
        self.filesystemtable.setObjectName(u"filesystemtable")
        self.filesystemtable.setFocusPolicy(Qt.ClickFocus)
        self.filesystemtable.setStyleSheet(u"FileSystemTable {\n"
"	color: black;\n"
"   	border: 4px;\n"
"	border-color: rgb(120, 120, 120);\n"
"	border-style: solid;\n"
"	background-color: rgb(238, 238, 236);\n"
"    font: 12pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: rgb(220, 220, 220);\n"
"	color: black;\n"
"    border: none;\n"
"	border-radius:none;\n"
"	border-style: none;\n"
"	font: 13pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.filesystemtable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.filesystemtable.setShowGrid(False)

        self.horizontalLayout_122.addWidget(self.filesystemtable)


        self.verticalLayout_35.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.x_axis_button_27 = QPushButton(self.frame_34)
        self.x_axis_button_27.setObjectName(u"x_axis_button_27")
        sizePolicy4.setHeightForWidth(self.x_axis_button_27.sizePolicy().hasHeightForWidth())
        self.x_axis_button_27.setSizePolicy(sizePolicy4)
        self.x_axis_button_27.setMinimumSize(QSize(90, 30))
        self.x_axis_button_27.setMaximumSize(QSize(90, 30))
        self.x_axis_button_27.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_27.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_axis_button_27.setIcon(icon1)
        self.x_axis_button_27.setIconSize(QSize(14, 14))

        self.horizontalLayout_123.addWidget(self.x_axis_button_27)

        self.x_axis_button_31 = QPushButton(self.frame_34)
        self.x_axis_button_31.setObjectName(u"x_axis_button_31")
        sizePolicy4.setHeightForWidth(self.x_axis_button_31.sizePolicy().hasHeightForWidth())
        self.x_axis_button_31.setSizePolicy(sizePolicy4)
        self.x_axis_button_31.setMinimumSize(QSize(100, 30))
        self.x_axis_button_31.setMaximumSize(QSize(100, 30))
        self.x_axis_button_31.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_31.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_axis_button_31.setIcon(icon2)
        self.x_axis_button_31.setIconSize(QSize(12, 16))

        self.horizontalLayout_123.addWidget(self.x_axis_button_31)

        self.x_axis_button_29 = QPushButton(self.frame_34)
        self.x_axis_button_29.setObjectName(u"x_axis_button_29")
        sizePolicy4.setHeightForWidth(self.x_axis_button_29.sizePolicy().hasHeightForWidth())
        self.x_axis_button_29.setSizePolicy(sizePolicy4)
        self.x_axis_button_29.setMinimumSize(QSize(125, 30))
        self.x_axis_button_29.setMaximumSize(QSize(125, 30))
        self.x_axis_button_29.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_29.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_axis_button_29.setIcon(icon3)
        self.x_axis_button_29.setIconSize(QSize(28, 15))

        self.horizontalLayout_123.addWidget(self.x_axis_button_29)

        self.x_axis_button_28 = QPushButton(self.frame_34)
        self.x_axis_button_28.setObjectName(u"x_axis_button_28")
        sizePolicy4.setHeightForWidth(self.x_axis_button_28.sizePolicy().hasHeightForWidth())
        self.x_axis_button_28.setSizePolicy(sizePolicy4)
        self.x_axis_button_28.setMinimumSize(QSize(90, 30))
        self.x_axis_button_28.setMaximumSize(QSize(90, 30))
        self.x_axis_button_28.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_28.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_123.addWidget(self.x_axis_button_28)


        self.verticalLayout_35.addLayout(self.horizontalLayout_123)


        self.horizontalLayout_120.addWidget(self.frame_34)

        self.frame_36 = QFrame(self.tab_15)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy1.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy1)
        self.frame_36.setStyleSheet(u"QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_36)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.work_column_header_8 = QLabel(self.frame_36)
        self.work_column_header_8.setObjectName(u"work_column_header_8")
        self.work_column_header_8.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.work_column_header_8.sizePolicy().hasHeightForWidth())
        self.work_column_header_8.setSizePolicy(sizePolicy4)
        self.work_column_header_8.setMinimumSize(QSize(200, 30))
        self.work_column_header_8.setMaximumSize(QSize(200, 30))
        self.work_column_header_8.setStyleSheet(u"QLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(238, 238, 236);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(46, 52, 54);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.work_column_header_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_127.addWidget(self.work_column_header_8)


        self.verticalLayout_38.addLayout(self.horizontalLayout_127)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.plainTextEdit = QPlainTextEdit(self.frame_36)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font3 = QFont()
        font3.setFamilies([u"Probe Basic Bebas Mono"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.plainTextEdit.setFont(font3)
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	color: black;\n"
"   	border: 4px;\n"
"	border-color: rgb(120, 120, 120);\n"
"	border-style: solid;\n"
"	background-color: rgb(238, 238, 236);\n"
"    font: 12pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_128.addWidget(self.plainTextEdit)


        self.verticalLayout_38.addLayout(self.horizontalLayout_128)

        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.x_axis_button_36 = QPushButton(self.frame_36)
        self.x_axis_button_36.setObjectName(u"x_axis_button_36")
        sizePolicy4.setHeightForWidth(self.x_axis_button_36.sizePolicy().hasHeightForWidth())
        self.x_axis_button_36.setSizePolicy(sizePolicy4)
        self.x_axis_button_36.setMinimumSize(QSize(150, 30))
        self.x_axis_button_36.setMaximumSize(QSize(150, 30))
        self.x_axis_button_36.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_36.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_129.addWidget(self.x_axis_button_36)


        self.verticalLayout_38.addLayout(self.horizontalLayout_129)


        self.horizontalLayout_120.addWidget(self.frame_36)


        self.verticalLayout_5.addLayout(self.horizontalLayout_120)

        self.tabWidget.addTab(self.tab_15, "")
        self.status_tab = QWidget()
        self.status_tab.setObjectName(u"status_tab")
        self.horizontalLayout_36 = QHBoxLayout(self.status_tab)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(12, -1, -1, -1)
        self.frame_33 = QFrame(self.status_tab)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy4.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy4)
        self.frame_33.setMinimumSize(QSize(360, 550))
        self.frame_33.setMaximumSize(QSize(360, 550))
        self.frame_33.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"padding-top: 0px;\n"
"padding-bottom: 0px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.frame_33)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setSpacing(0)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.machine_column_header_9 = QLabel(self.frame_33)
        self.machine_column_header_9.setObjectName(u"machine_column_header_9")
        self.machine_column_header_9.setMinimumSize(QSize(0, 50))
        self.machine_column_header_9.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_9.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_113.addWidget(self.machine_column_header_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_113)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.lineEdit_3 = QLineEdit(self.frame_33)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(100)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy6)
        self.lineEdit_3.setMinimumSize(QSize(130, 40))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lineEdit_3)

        self.m01_break_button_4 = ActionButton(self.frame_33)
        self.m01_break_button_4.setObjectName(u"m01_break_button_4")
        sizePolicy6.setHeightForWidth(self.m01_break_button_4.sizePolicy().hasHeightForWidth())
        self.m01_break_button_4.setSizePolicy(sizePolicy6)
        self.m01_break_button_4.setMinimumSize(QSize(130, 45))
        self.m01_break_button_4.setMaximumSize(QSize(16777215, 45))
        self.m01_break_button_4.setFocusPolicy(Qt.NoFocus)
        self.m01_break_button_4.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_11.addWidget(self.m01_break_button_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setSpacing(15)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_114.setContentsMargins(2, 2, 2, 2)
        self.m01_break_button_8 = ActionButton(self.frame_33)
        self.m01_break_button_8.setObjectName(u"m01_break_button_8")
        sizePolicy6.setHeightForWidth(self.m01_break_button_8.sizePolicy().hasHeightForWidth())
        self.m01_break_button_8.setSizePolicy(sizePolicy6)
        self.m01_break_button_8.setMinimumSize(QSize(130, 45))
        self.m01_break_button_8.setMaximumSize(QSize(16777215, 45))
        self.m01_break_button_8.setFocusPolicy(Qt.NoFocus)
        self.m01_break_button_8.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_114.addWidget(self.m01_break_button_8)

        self.m01_break_button_9 = ActionButton(self.frame_33)
        self.m01_break_button_9.setObjectName(u"m01_break_button_9")
        sizePolicy6.setHeightForWidth(self.m01_break_button_9.sizePolicy().hasHeightForWidth())
        self.m01_break_button_9.setSizePolicy(sizePolicy6)
        self.m01_break_button_9.setMinimumSize(QSize(130, 45))
        self.m01_break_button_9.setMaximumSize(QSize(16777215, 45))
        self.m01_break_button_9.setFocusPolicy(Qt.NoFocus)
        self.m01_break_button_9.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_114.addWidget(self.m01_break_button_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_114)

        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setSpacing(15)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_115.setContentsMargins(2, 2, 2, 2)
        self.subcallbutton_9 = SubCallButton(self.frame_33)
        self.subcallbutton_9.setObjectName(u"subcallbutton_9")
        sizePolicy5.setHeightForWidth(self.subcallbutton_9.sizePolicy().hasHeightForWidth())
        self.subcallbutton_9.setSizePolicy(sizePolicy5)
        self.subcallbutton_9.setMinimumSize(QSize(130, 45))
        self.subcallbutton_9.setMaximumSize(QSize(16777215, 45))
        self.subcallbutton_9.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/images/ccw_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.subcallbutton_9.setIcon(icon6)
        self.subcallbutton_9.setIconSize(QSize(20, 20))

        self.horizontalLayout_115.addWidget(self.subcallbutton_9)

        self.subcallbutton_3 = SubCallButton(self.frame_33)
        self.subcallbutton_3.setObjectName(u"subcallbutton_3")
        sizePolicy5.setHeightForWidth(self.subcallbutton_3.sizePolicy().hasHeightForWidth())
        self.subcallbutton_3.setSizePolicy(sizePolicy5)
        self.subcallbutton_3.setMinimumSize(QSize(130, 45))
        self.subcallbutton_3.setMaximumSize(QSize(16777215, 45))
        self.subcallbutton_3.setLayoutDirection(Qt.RightToLeft)
        self.subcallbutton_3.setStyleSheet(u"SubCallButton {\n"
"    text-align: right;\n"
"    padding-right: 28px;\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/images/cw_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.subcallbutton_3.setIcon(icon7)
        self.subcallbutton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_115.addWidget(self.subcallbutton_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setSpacing(15)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_116.setContentsMargins(2, 2, 2, 2)
        self.subcallbutton_10 = SubCallButton(self.frame_33)
        self.subcallbutton_10.setObjectName(u"subcallbutton_10")
        sizePolicy5.setHeightForWidth(self.subcallbutton_10.sizePolicy().hasHeightForWidth())
        self.subcallbutton_10.setSizePolicy(sizePolicy5)
        self.subcallbutton_10.setMinimumSize(QSize(10, 45))
        self.subcallbutton_10.setMaximumSize(QSize(16777215, 45))
        self.subcallbutton_10.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/images/left_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.subcallbutton_10.setIcon(icon8)

        self.horizontalLayout_116.addWidget(self.subcallbutton_10)

        self.subcallbutton_11 = SubCallButton(self.frame_33)
        self.subcallbutton_11.setObjectName(u"subcallbutton_11")
        sizePolicy5.setHeightForWidth(self.subcallbutton_11.sizePolicy().hasHeightForWidth())
        self.subcallbutton_11.setSizePolicy(sizePolicy5)
        self.subcallbutton_11.setMinimumSize(QSize(10, 45))
        self.subcallbutton_11.setMaximumSize(QSize(16777215, 45))
        self.subcallbutton_11.setLayoutDirection(Qt.RightToLeft)
        self.subcallbutton_11.setStyleSheet(u"SubCallButton {\n"
"    text-align: right;\n"
"    padding-right: 22px;\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/images/right_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.subcallbutton_11.setIcon(icon9)

        self.horizontalLayout_116.addWidget(self.subcallbutton_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_116)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setSpacing(15)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(2, 2, 2, 2)
        self.subcallbutton_12 = SubCallButton(self.frame_33)
        self.subcallbutton_12.setObjectName(u"subcallbutton_12")
        sizePolicy5.setHeightForWidth(self.subcallbutton_12.sizePolicy().hasHeightForWidth())
        self.subcallbutton_12.setSizePolicy(sizePolicy5)
        self.subcallbutton_12.setMinimumSize(QSize(130, 45))
        self.subcallbutton_12.setMaximumSize(QSize(16777215, 45))
        self.subcallbutton_12.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_117.addWidget(self.subcallbutton_12)

        self.subcallbutton_13 = SubCallButton(self.frame_33)
        self.subcallbutton_13.setObjectName(u"subcallbutton_13")
        sizePolicy5.setHeightForWidth(self.subcallbutton_13.sizePolicy().hasHeightForWidth())
        self.subcallbutton_13.setSizePolicy(sizePolicy5)
        self.subcallbutton_13.setMinimumSize(QSize(130, 45))
        self.subcallbutton_13.setMaximumSize(QSize(16777215, 45))
        self.subcallbutton_13.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_117.addWidget(self.subcallbutton_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_117)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setSpacing(15)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(2, 2, 2, 2)
        self.m01_break_button_10 = ActionButton(self.frame_33)
        self.m01_break_button_10.setObjectName(u"m01_break_button_10")
        sizePolicy6.setHeightForWidth(self.m01_break_button_10.sizePolicy().hasHeightForWidth())
        self.m01_break_button_10.setSizePolicy(sizePolicy6)
        self.m01_break_button_10.setMinimumSize(QSize(130, 45))
        self.m01_break_button_10.setMaximumSize(QSize(16777215, 45))
        self.m01_break_button_10.setFocusPolicy(Qt.NoFocus)
        self.m01_break_button_10.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_118.addWidget(self.m01_break_button_10)

        self.m01_break_button_27 = ActionButton(self.frame_33)
        self.m01_break_button_27.setObjectName(u"m01_break_button_27")
        sizePolicy6.setHeightForWidth(self.m01_break_button_27.sizePolicy().hasHeightForWidth())
        self.m01_break_button_27.setSizePolicy(sizePolicy6)
        self.m01_break_button_27.setMinimumSize(QSize(130, 45))
        self.m01_break_button_27.setMaximumSize(QSize(16777215, 45))
        self.m01_break_button_27.setFocusPolicy(Qt.NoFocus)
        self.m01_break_button_27.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_118.addWidget(self.m01_break_button_27)


        self.verticalLayout_7.addLayout(self.horizontalLayout_118)

        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setSpacing(15)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(2, 2, 2, 2)
        self.subcallbutton_14 = SubCallButton(self.frame_33)
        self.subcallbutton_14.setObjectName(u"subcallbutton_14")
        sizePolicy5.setHeightForWidth(self.subcallbutton_14.sizePolicy().hasHeightForWidth())
        self.subcallbutton_14.setSizePolicy(sizePolicy5)
        self.subcallbutton_14.setMinimumSize(QSize(135, 45))
        self.subcallbutton_14.setMaximumSize(QSize(16777215, 45))
        self.subcallbutton_14.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_119.addWidget(self.subcallbutton_14)

        self.m01_break_button_14 = ActionButton(self.frame_33)
        self.m01_break_button_14.setObjectName(u"m01_break_button_14")
        sizePolicy6.setHeightForWidth(self.m01_break_button_14.sizePolicy().hasHeightForWidth())
        self.m01_break_button_14.setSizePolicy(sizePolicy6)
        self.m01_break_button_14.setMinimumSize(QSize(60, 45))
        self.m01_break_button_14.setMaximumSize(QSize(16777215, 45))
        self.m01_break_button_14.setFocusPolicy(Qt.NoFocus)
        self.m01_break_button_14.setStyleSheet(u"QPushButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_119.addWidget(self.m01_break_button_14)

        self.m01_break_button_15 = ActionButton(self.frame_33)
        self.m01_break_button_15.setObjectName(u"m01_break_button_15")
        sizePolicy6.setHeightForWidth(self.m01_break_button_15.sizePolicy().hasHeightForWidth())
        self.m01_break_button_15.setSizePolicy(sizePolicy6)
        self.m01_break_button_15.setMinimumSize(QSize(60, 45))
        self.m01_break_button_15.setMaximumSize(QSize(16777215, 45))
        self.m01_break_button_15.setFocusPolicy(Qt.NoFocus)
        self.m01_break_button_15.setStyleSheet(u"QPushButton {\n"
"   	font: 20pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_119.addWidget(self.m01_break_button_15)


        self.verticalLayout_7.addLayout(self.horizontalLayout_119)


        self.verticalLayout_18.addWidget(self.frame_33)

        self.mdi_entry_box_3 = MDIEntry(self.status_tab)
        self.mdi_entry_box_3.setObjectName(u"mdi_entry_box_3")
        self.mdi_entry_box_3.setMinimumSize(QSize(0, 40))
        self.mdi_entry_box_3.setFont(font2)
        self.mdi_entry_box_3.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_18.addWidget(self.mdi_entry_box_3)


        self.horizontalLayout_36.addLayout(self.verticalLayout_18)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.frame_22 = QFrame(self.status_tab)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy7)
        self.frame_22.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_49.addWidget(self.frame_22)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_49)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_4 = QFrame(self.status_tab)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setMinimumSize(QSize(863, 521))
        self.frame_4.setMaximumSize(QSize(883, 521))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"border-color: Transparent;\n"
"background-color:transparent;\n"
"border-width: 2px;\n"
"border-radius: 8px;\n"
"}")
        self.widget_3 = QWidget(self.frame_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 9, 500, 500))
        self.label_53 = QLabel(self.widget_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(3, 3, 500, 500))
        self.label_53.setStyleSheet(u"image: url(:/images/carousel_12.png);")
        self.label_53.setScaledContents(True)
        self.label_53.setIndent(0)
        self.label_60 = QLabel(self.widget_3)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(158, 353, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy4)
        self.label_60.setMinimumSize(QSize(0, 0))
        self.label_60.setMaximumSize(QSize(100, 100))
        self.label_60.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_60.setAlignment(Qt.AlignCenter)
        self.label_60.setIndent(0)
        self.label_61 = QLabel(self.widget_3)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(112, 34, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy4)
        self.label_61.setMinimumSize(QSize(0, 0))
        self.label_61.setMaximumSize(QSize(100, 100))
        self.label_61.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_61.setAlignment(Qt.AlignCenter)
        self.label_61.setIndent(0)
        self.label_67 = QLabel(self.widget_3)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(403, 112, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy4)
        self.label_67.setMinimumSize(QSize(0, 0))
        self.label_67.setMaximumSize(QSize(100, 100))
        self.label_67.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_67.setAlignment(Qt.AlignCenter)
        self.label_67.setIndent(0)
        self.label_68 = QLabel(self.widget_3)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(33, 324, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy4)
        self.label_68.setMinimumSize(QSize(0, 0))
        self.label_68.setMaximumSize(QSize(100, 100))
        self.label_68.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_68.setAlignment(Qt.AlignCenter)
        self.label_68.setIndent(0)
        self.label_69 = QLabel(self.widget_3)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(353, 158, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy4)
        self.label_69.setMinimumSize(QSize(0, 0))
        self.label_69.setMaximumSize(QSize(100, 100))
        self.label_69.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_69.setAlignment(Qt.AlignCenter)
        self.label_69.setIndent(0)
        self.label_70 = QLabel(self.widget_3)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(302, 108, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy4)
        self.label_70.setMinimumSize(QSize(0, 0))
        self.label_70.setMaximumSize(QSize(100, 100))
        self.label_70.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_70.setAlignment(Qt.AlignCenter)
        self.label_70.setIndent(0)
        self.label_71 = QLabel(self.widget_3)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(218, 429, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy4)
        self.label_71.setMinimumSize(QSize(0, 0))
        self.label_71.setMaximumSize(QSize(100, 100))
        self.label_71.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_71.setAlignment(Qt.AlignCenter)
        self.label_71.setIndent(0)
        self.label_72 = QLabel(self.widget_3)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(304, 353, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy4)
        self.label_72.setMinimumSize(QSize(0, 0))
        self.label_72.setMaximumSize(QSize(100, 100))
        self.label_72.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_72.setAlignment(Qt.AlignCenter)
        self.label_72.setIndent(0)
        self.label_73 = QLabel(self.widget_3)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(218, 6, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy4)
        self.label_73.setMinimumSize(QSize(0, 0))
        self.label_73.setMaximumSize(QSize(100, 100))
        self.label_73.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_73.setAlignment(Qt.AlignCenter)
        self.label_73.setIndent(0)
        self.label_74 = QLabel(self.widget_3)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(162, 107, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy4)
        self.label_74.setMinimumSize(QSize(0, 0))
        self.label_74.setMaximumSize(QSize(100, 100))
        self.label_74.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_74.setAlignment(Qt.AlignCenter)
        self.label_74.setIndent(0)
        self.label_75 = QLabel(self.widget_3)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(373, 229, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy4)
        self.label_75.setMinimumSize(QSize(0, 0))
        self.label_75.setMaximumSize(QSize(100, 100))
        self.label_75.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_75.setAlignment(Qt.AlignCenter)
        self.label_75.setIndent(0)
        self.label_76 = QLabel(self.widget_3)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(109, 158, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy4)
        self.label_76.setMinimumSize(QSize(0, 0))
        self.label_76.setMaximumSize(QSize(100, 100))
        self.label_76.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_76.setAlignment(Qt.AlignCenter)
        self.label_76.setIndent(0)
        self.label_77 = QLabel(self.widget_3)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(324, 35, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy4)
        self.label_77.setMinimumSize(QSize(0, 0))
        self.label_77.setMaximumSize(QSize(100, 100))
        self.label_77.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_77.setAlignment(Qt.AlignCenter)
        self.label_77.setIndent(0)
        self.label_78 = QLabel(self.widget_3)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(430, 217, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy4)
        self.label_78.setMinimumSize(QSize(0, 0))
        self.label_78.setMaximumSize(QSize(100, 100))
        self.label_78.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_78.setAlignment(Qt.AlignCenter)
        self.label_78.setIndent(0)
        self.label_79 = QLabel(self.widget_3)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(34, 112, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy4)
        self.label_79.setMinimumSize(QSize(0, 0))
        self.label_79.setMaximumSize(QSize(100, 100))
        self.label_79.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_79.setAlignment(Qt.AlignCenter)
        self.label_79.setIndent(0)
        self.label_80 = QLabel(self.widget_3)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(231, 89, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy4)
        self.label_80.setMinimumSize(QSize(0, 0))
        self.label_80.setMaximumSize(QSize(100, 100))
        self.label_80.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_80.setAlignment(Qt.AlignCenter)
        self.label_80.setIndent(0)
        self.label_81 = QLabel(self.widget_3)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(112, 401, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy4)
        self.label_81.setMinimumSize(QSize(0, 0))
        self.label_81.setMaximumSize(QSize(100, 100))
        self.label_81.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_81.setAlignment(Qt.AlignCenter)
        self.label_81.setIndent(0)
        self.label_82 = QLabel(self.widget_3)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(108, 301, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy4)
        self.label_82.setMinimumSize(QSize(0, 0))
        self.label_82.setMaximumSize(QSize(100, 100))
        self.label_82.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_82.setAlignment(Qt.AlignCenter)
        self.label_82.setIndent(0)
        self.label_83 = QLabel(self.widget_3)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(324, 402, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy4)
        self.label_83.setMinimumSize(QSize(0, 0))
        self.label_83.setMaximumSize(QSize(100, 100))
        self.label_83.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_83.setAlignment(Qt.AlignCenter)
        self.label_83.setIndent(0)
        self.label_84 = QLabel(self.widget_3)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(90, 231, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy4)
        self.label_84.setMinimumSize(QSize(0, 0))
        self.label_84.setMaximumSize(QSize(100, 100))
        self.label_84.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_84.setAlignment(Qt.AlignCenter)
        self.label_84.setIndent(0)
        self.label_85 = QLabel(self.widget_3)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(402, 323, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy4)
        self.label_85.setMinimumSize(QSize(0, 0))
        self.label_85.setMaximumSize(QSize(100, 100))
        self.label_85.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_85.setAlignment(Qt.AlignCenter)
        self.label_85.setIndent(0)
        self.label_86 = QLabel(self.widget_3)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(232, 373, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy4)
        self.label_86.setMinimumSize(QSize(0, 0))
        self.label_86.setMaximumSize(QSize(100, 100))
        self.label_86.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_86.setAlignment(Qt.AlignCenter)
        self.label_86.setIndent(0)
        self.label_87 = QLabel(self.widget_3)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(355, 301, 44, 44))
        sizePolicy4.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy4)
        self.label_87.setMinimumSize(QSize(0, 0))
        self.label_87.setMaximumSize(QSize(100, 100))
        self.label_87.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_87.setAlignment(Qt.AlignCenter)
        self.label_87.setIndent(0)
        self.label_88 = QLabel(self.widget_3)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(5, 218, 70, 70))
        sizePolicy4.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy4)
        self.label_88.setMinimumSize(QSize(0, 0))
        self.label_88.setMaximumSize(QSize(100, 100))
        self.label_88.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_88.setAlignment(Qt.AlignCenter)
        self.label_88.setIndent(0)
        self.widget_4 = QWidget(self.frame_4)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(534, 4, 176, 291))
        self.label_89 = QLabel(self.widget_4)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(4, 3, 169, 300))
        self.label_89.setStyleSheet(u"image: url(:/images/atc_spindle_tool.png);")
        self.label_89.setScaledContents(True)
        self.label_89.setIndent(0)
        self.tool_length_8 = StatusLabel(self.widget_4)
        self.tool_length_8.setObjectName(u"tool_length_8")
        self.tool_length_8.setGeometry(QRect(64, 139, 50, 33))
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.tool_length_8.sizePolicy().hasHeightForWidth())
        self.tool_length_8.setSizePolicy(sizePolicy8)
        self.tool_length_8.setMinimumSize(QSize(50, 33))
        self.tool_length_8.setMaximumSize(QSize(50, 33))
        self.tool_length_8.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_length_8.setAlignment(Qt.AlignCenter)
        self.label_38 = QLabel(self.frame_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(610, 317, 240, 200))
        self.label_38.setStyleSheet(u"image: url(:/images/tool_probe.png);")
        self.label_38.setScaledContents(True)
        self.widget_4.raise_()
        self.label_38.raise_()
        self.widget_3.raise_()

        self.verticalLayout_19.addWidget(self.frame_4)


        self.horizontalLayout_36.addLayout(self.verticalLayout_19)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.frame_21 = QFrame(self.status_tab)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy7.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy7)
        self.frame_21.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_50.addWidget(self.frame_21)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_50)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(35)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, 16, 20)
        self.frame_6 = QFrame(self.status_tab)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setMinimumSize(QSize(340, 320))
        self.frame_6.setMaximumSize(QSize(340, 320))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"border-radius: 6px;\n"
"padding-top: 0px;\n"
"padding-bottom: 0px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.machine_column_header_3 = QLabel(self.frame_6)
        self.machine_column_header_3.setObjectName(u"machine_column_header_3")
        self.machine_column_header_3.setMinimumSize(QSize(0, 50))
        self.machine_column_header_3.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_3.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.machine_column_header_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_26.setContentsMargins(2, 2, 2, 2)
        self.load_spindle_tool_number = QLineEdit(self.frame_6)
        self.load_spindle_tool_number.setObjectName(u"load_spindle_tool_number")
        self.load_spindle_tool_number.setEnabled(True)
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(200)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.load_spindle_tool_number.sizePolicy().hasHeightForWidth())
        self.load_spindle_tool_number.setSizePolicy(sizePolicy9)
        self.load_spindle_tool_number.setMinimumSize(QSize(130, 40))
        self.load_spindle_tool_number.setMaximumSize(QSize(16777215, 40))
        self.load_spindle_tool_number.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.load_spindle_tool_number.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.load_spindle_tool_number)

        self.load_current_tool = MDIButton(self.frame_6)
        self.load_current_tool.setObjectName(u"load_current_tool")
        self.load_current_tool.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.load_current_tool.sizePolicy().hasHeightForWidth())
        self.load_current_tool.setSizePolicy(sizePolicy9)
        self.load_current_tool.setMinimumSize(QSize(130, 45))
        self.load_current_tool.setMaximumSize(QSize(16777215, 45))
        self.load_current_tool.setStyleSheet(u"MDIButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.load_current_tool.setCheckable(False)
        self.load_current_tool.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.load_current_tool)


        self.verticalLayout_10.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.remove_current_tool = MDIButton(self.frame_6)
        self.remove_current_tool.setObjectName(u"remove_current_tool")
        self.remove_current_tool.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.remove_current_tool.sizePolicy().hasHeightForWidth())
        self.remove_current_tool.setSizePolicy(sizePolicy9)
        self.remove_current_tool.setMinimumSize(QSize(130, 45))
        self.remove_current_tool.setMaximumSize(QSize(16777215, 45))
        self.remove_current_tool.setStyleSheet(u"MDIButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.remove_current_tool.setCheckable(False)
        self.remove_current_tool.setAutoExclusive(True)

        self.horizontalLayout_14.addWidget(self.remove_current_tool)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.subcallbutton_15 = SubCallButton(self.frame_6)
        self.subcallbutton_15.setObjectName(u"subcallbutton_15")
        sizePolicy5.setHeightForWidth(self.subcallbutton_15.sizePolicy().hasHeightForWidth())
        self.subcallbutton_15.setSizePolicy(sizePolicy5)
        self.subcallbutton_15.setMinimumSize(QSize(130, 45))
        self.subcallbutton_15.setMaximumSize(QSize(16777215, 45))
        self.subcallbutton_15.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.subcallbutton_15.setIcon(icon6)
        self.subcallbutton_15.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.subcallbutton_15)

        self.subcallbutton_4 = SubCallButton(self.frame_6)
        self.subcallbutton_4.setObjectName(u"subcallbutton_4")
        sizePolicy5.setHeightForWidth(self.subcallbutton_4.sizePolicy().hasHeightForWidth())
        self.subcallbutton_4.setSizePolicy(sizePolicy5)
        self.subcallbutton_4.setMinimumSize(QSize(130, 45))
        self.subcallbutton_4.setMaximumSize(QSize(16777215, 45))
        self.subcallbutton_4.setLayoutDirection(Qt.RightToLeft)
        self.subcallbutton_4.setStyleSheet(u"SubCallButton {\n"
"    text-align: right;\n"
"    padding-right: 28px;\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"")
        self.subcallbutton_4.setIcon(icon7)
        self.subcallbutton_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.subcallbutton_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(2)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.store_current_tool = MDIButton(self.frame_6)
        self.store_current_tool.setObjectName(u"store_current_tool")
        self.store_current_tool.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.store_current_tool.sizePolicy().hasHeightForWidth())
        self.store_current_tool.setSizePolicy(sizePolicy9)
        self.store_current_tool.setMinimumSize(QSize(130, 45))
        self.store_current_tool.setMaximumSize(QSize(16777215, 45))
        self.store_current_tool.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.store_current_tool.setCheckable(False)
        self.store_current_tool.setAutoExclusive(True)

        self.horizontalLayout_21.addWidget(self.store_current_tool)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)


        self.verticalLayout_17.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.status_tab)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(1)
        sizePolicy10.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy10)
        self.frame_7.setMinimumSize(QSize(340, 215))
        self.frame_7.setMaximumSize(QSize(340, 215))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"border-radius: 6px;\n"
"padding-top: 0px;\n"
"padding-bottom: 0px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.machine_column_header_2 = QLabel(self.frame_7)
        self.machine_column_header_2.setObjectName(u"machine_column_header_2")
        self.machine_column_header_2.setMinimumSize(QSize(0, 50))
        self.machine_column_header_2.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_2.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.machine_column_header_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.m01_break_button_24 = ActionButton(self.frame_7)
        self.m01_break_button_24.setObjectName(u"m01_break_button_24")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(30)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.m01_break_button_24.sizePolicy().hasHeightForWidth())
        self.m01_break_button_24.setSizePolicy(sizePolicy11)
        self.m01_break_button_24.setMinimumSize(QSize(250, 45))
        self.m01_break_button_24.setMaximumSize(QSize(16777215, 45))
        self.m01_break_button_24.setFocusPolicy(Qt.NoFocus)
        self.m01_break_button_24.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_19.addWidget(self.m01_break_button_24)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(2, 5, 2, 5)
        self.m01_break_button_25 = ActionButton(self.frame_7)
        self.m01_break_button_25.setObjectName(u"m01_break_button_25")
        sizePolicy11.setHeightForWidth(self.m01_break_button_25.sizePolicy().hasHeightForWidth())
        self.m01_break_button_25.setSizePolicy(sizePolicy11)
        self.m01_break_button_25.setMinimumSize(QSize(250, 45))
        self.m01_break_button_25.setMaximumSize(QSize(16777215, 45))
        self.m01_break_button_25.setFocusPolicy(Qt.NoFocus)
        self.m01_break_button_25.setStyleSheet(u"QPushButton {\n"
"   	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_23.addWidget(self.m01_break_button_25)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)


        self.verticalLayout_17.addWidget(self.frame_7)


        self.horizontalLayout_36.addLayout(self.verticalLayout_17)

        self.tabWidget.addTab(self.status_tab, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_16)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 18, 5, 18)
        self.frame_37 = QFrame(self.tab_16)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy4.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy4)
        self.frame_37.setMinimumSize(QSize(560, 500))
        self.frame_37.setMaximumSize(QSize(520, 500))
        self.frame_37.setStyleSheet(u"QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.verticalLayout_39 = QVBoxLayout(self.frame_37)
        self.verticalLayout_39.setSpacing(6)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(-1, 5, -1, 5)
        self.tableWidget_3 = QTableWidget(self.frame_37)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        font4 = QFont()
        font4.setFamilies([u"Probe Basic Bebas Mono"])
        font4.setPointSize(16)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font4);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font4);
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget_3.rowCount() < 9):
            self.tableWidget_3.setRowCount(9)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font1);
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font1);
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font1);
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font1);
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font1);
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font1);
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font1);
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font1);
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font1);
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem14)
        font5 = QFont()
        font5.setFamilies([u"Probe Basic Bebas Mono"])
        font5.setPointSize(17)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font5);
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem15)
        font6 = QFont()
        font6.setFamilies([u"Probe Basic Bebas Mono"])
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem16.setFont(font6);
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem17.setFont(font6);
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(0, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(0, 4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(0, 5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font5);
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem22.setFont(font6);
        self.tableWidget_3.setItem(1, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem23.setFont(font6);
        self.tableWidget_3.setItem(1, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(1, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(1, 4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(1, 5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem27.setFont(font5);
        self.tableWidget_3.setItem(2, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem28.setFont(font6);
        self.tableWidget_3.setItem(2, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem29.setFont(font6);
        self.tableWidget_3.setItem(2, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(2, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(2, 4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(2, 5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFont(font5);
        self.tableWidget_3.setItem(3, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem34.setFont(font6);
        self.tableWidget_3.setItem(3, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem35.setFont(font6);
        self.tableWidget_3.setItem(3, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(3, 3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(3, 4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(3, 5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem39.setFont(font5);
        self.tableWidget_3.setItem(4, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem40.setFont(font6);
        self.tableWidget_3.setItem(4, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem41.setFont(font6);
        self.tableWidget_3.setItem(4, 2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(4, 3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(4, 4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(4, 5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem45.setFont(font5);
        self.tableWidget_3.setItem(5, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem46.setFont(font6);
        self.tableWidget_3.setItem(5, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(5, 2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(5, 3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(5, 4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(5, 5, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem51.setFont(font5);
        self.tableWidget_3.setItem(6, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem52.setFont(font6);
        self.tableWidget_3.setItem(6, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(6, 2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(6, 3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(6, 4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(6, 5, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem57.setFont(font5);
        self.tableWidget_3.setItem(7, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem58.setFont(font6);
        self.tableWidget_3.setItem(7, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(7, 2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(7, 3, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(7, 4, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(7, 5, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem63.setFont(font5);
        self.tableWidget_3.setItem(8, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem64.setFont(font6);
        self.tableWidget_3.setItem(8, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(8, 2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(8, 3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(8, 4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_3.setItem(8, 5, __qtablewidgetitem68)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        palette1 = QPalette()
        brush3 = QBrush(QColor(235, 235, 237, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush5 = QBrush(QColor(90, 90, 90, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        self.tableWidget_3.setPalette(palette1)
        font7 = QFont()
        font7.setFamilies([u"Probe Basic Bebas Mono"])
        font7.setPointSize(16)
        font7.setBold(False)
        font7.setItalic(False)
        self.tableWidget_3.setFont(font7)
        self.tableWidget_3.setStyleSheet(u"QTableView {\n"
"	color: rgb(235, 235, 237);\n"
"   	border-top: 8px rgb(120, 120, 120);\n"
"	border-left: 4px  rgb(120, 120, 120);\n"
"	border-bottom: 1px rgb(120, 120, 120);\n"
"	border-right: 4px rgb(120, 120, 120);\n"
"	border-radius: 5px;\n"
"	border-color: rgb(120, 120, 120);\n"
"	border-style: solid;\n"
"	background-color: rgb(120, 120, 120);\n"
"    gridline-color: rgb(203, 203, 203);\n"
"	alternate-background-color: rgb(90, 90, 90);\n"
"    font: 16pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"\n"
"QHeaderView {\n"
"    font: 16pt \"Probe Basic Bebas Mono\";\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: black;\n"
"    border: none;\n"
"}")
        self.tableWidget_3.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_3.setFrameShadow(QFrame.Sunken)
        self.tableWidget_3.setLineWidth(6)
        self.tableWidget_3.setMidLineWidth(4)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(87)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(86)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(42)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(42)
        self.tableWidget_3.verticalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_47.addWidget(self.tableWidget_3)


        self.verticalLayout_39.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(-1, 5, -1, 5)
        self.x_axis_button_10 = QPushButton(self.frame_37)
        self.x_axis_button_10.setObjectName(u"x_axis_button_10")
        sizePolicy4.setHeightForWidth(self.x_axis_button_10.sizePolicy().hasHeightForWidth())
        self.x_axis_button_10.setSizePolicy(sizePolicy4)
        self.x_axis_button_10.setMinimumSize(QSize(108, 33))
        self.x_axis_button_10.setMaximumSize(QSize(108, 33))
        self.x_axis_button_10.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_10.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_axis_button_10.setCheckable(True)

        self.horizontalLayout_130.addWidget(self.x_axis_button_10)

        self.x_axis_button_12 = QPushButton(self.frame_37)
        self.x_axis_button_12.setObjectName(u"x_axis_button_12")
        sizePolicy4.setHeightForWidth(self.x_axis_button_12.sizePolicy().hasHeightForWidth())
        self.x_axis_button_12.setSizePolicy(sizePolicy4)
        self.x_axis_button_12.setMinimumSize(QSize(108, 33))
        self.x_axis_button_12.setMaximumSize(QSize(108, 33))
        self.x_axis_button_12.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_12.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_axis_button_12.setCheckable(True)

        self.horizontalLayout_130.addWidget(self.x_axis_button_12)

        self.x_axis_button_13 = QPushButton(self.frame_37)
        self.x_axis_button_13.setObjectName(u"x_axis_button_13")
        sizePolicy4.setHeightForWidth(self.x_axis_button_13.sizePolicy().hasHeightForWidth())
        self.x_axis_button_13.setSizePolicy(sizePolicy4)
        self.x_axis_button_13.setMinimumSize(QSize(108, 33))
        self.x_axis_button_13.setMaximumSize(QSize(108, 33))
        self.x_axis_button_13.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_13.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_axis_button_13.setCheckable(True)

        self.horizontalLayout_130.addWidget(self.x_axis_button_13)

        self.x_axis_button_14 = QPushButton(self.frame_37)
        self.x_axis_button_14.setObjectName(u"x_axis_button_14")
        sizePolicy4.setHeightForWidth(self.x_axis_button_14.sizePolicy().hasHeightForWidth())
        self.x_axis_button_14.setSizePolicy(sizePolicy4)
        self.x_axis_button_14.setMinimumSize(QSize(130, 33))
        self.x_axis_button_14.setMaximumSize(QSize(130, 33))
        self.x_axis_button_14.setFocusPolicy(Qt.NoFocus)
        self.x_axis_button_14.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_axis_button_14.setCheckable(True)

        self.horizontalLayout_130.addWidget(self.x_axis_button_14)


        self.verticalLayout_39.addLayout(self.horizontalLayout_130)


        self.verticalLayout_11.addWidget(self.frame_37)

        self.mdi_entry_box_6 = MDIEntry(self.tab_16)
        self.mdi_entry_box_6.setObjectName(u"mdi_entry_box_6")
        sizePolicy4.setHeightForWidth(self.mdi_entry_box_6.sizePolicy().hasHeightForWidth())
        self.mdi_entry_box_6.setSizePolicy(sizePolicy4)
        self.mdi_entry_box_6.setMinimumSize(QSize(560, 40))
        self.mdi_entry_box_6.setMaximumSize(QSize(560, 40))
        self.mdi_entry_box_6.setFont(font2)
        self.mdi_entry_box_6.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_11.addWidget(self.mdi_entry_box_6)


        self.horizontalLayout_8.addLayout(self.verticalLayout_11)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, -1, 0, 0)
        self.frame_15 = QFrame(self.tab_16)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy4.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy4)
        self.frame_15.setMinimumSize(QSize(700, 560))
        self.frame_15.setMaximumSize(QSize(650, 560))
        self.frame_15.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.frame_15)
        self.verticalLayout_33.setSpacing(15)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, 5, -1, 9)
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_12.setHorizontalSpacing(31)
        self.gridLayout_12.setVerticalSpacing(12)
        self.gridLayout_12.setContentsMargins(-1, 5, -1, -1)
        self.machine_column_header_4 = QLabel(self.frame_15)
        self.machine_column_header_4.setObjectName(u"machine_column_header_4")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.machine_column_header_4.sizePolicy().hasHeightForWidth())
        self.machine_column_header_4.setSizePolicy(sizePolicy12)
        self.machine_column_header_4.setMinimumSize(QSize(675, 55))
        self.machine_column_header_4.setMaximumSize(QSize(16777215, 55))
        self.machine_column_header_4.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(90, 90, 90);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.machine_column_header_4, 0, 0, 1, 5)

        self.actionbutton_g54_2 = ActionButton(self.frame_15)
        self.actionbutton_g54_2.setObjectName(u"actionbutton_g54_2")
        self.actionbutton_g54_2.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.actionbutton_g54_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g54_2.setSizePolicy(sizePolicy4)
        self.actionbutton_g54_2.setMinimumSize(QSize(110, 38))
        self.actionbutton_g54_2.setMaximumSize(QSize(110, 38))
        self.actionbutton_g54_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_g54_2.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g54_2, 1, 0, 1, 1)

        self.actionbutton_g55_2 = ActionButton(self.frame_15)
        self.actionbutton_g55_2.setObjectName(u"actionbutton_g55_2")
        self.actionbutton_g55_2.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.actionbutton_g55_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g55_2.setSizePolicy(sizePolicy4)
        self.actionbutton_g55_2.setMinimumSize(QSize(110, 38))
        self.actionbutton_g55_2.setMaximumSize(QSize(110, 38))
        self.actionbutton_g55_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_g55_2.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g55_2, 1, 1, 1, 1)

        self.actionbutton_g56_2 = ActionButton(self.frame_15)
        self.actionbutton_g56_2.setObjectName(u"actionbutton_g56_2")
        self.actionbutton_g56_2.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.actionbutton_g56_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g56_2.setSizePolicy(sizePolicy4)
        self.actionbutton_g56_2.setMinimumSize(QSize(110, 38))
        self.actionbutton_g56_2.setMaximumSize(QSize(110, 38))
        self.actionbutton_g56_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_g56_2.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g56_2, 1, 2, 1, 1)

        self.actionbutton_g57_2 = ActionButton(self.frame_15)
        self.actionbutton_g57_2.setObjectName(u"actionbutton_g57_2")
        self.actionbutton_g57_2.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.actionbutton_g57_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g57_2.setSizePolicy(sizePolicy4)
        self.actionbutton_g57_2.setMinimumSize(QSize(110, 38))
        self.actionbutton_g57_2.setMaximumSize(QSize(110, 38))
        self.actionbutton_g57_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_g57_2.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g57_2, 1, 3, 1, 1)

        self.actionbutton_g58_2 = ActionButton(self.frame_15)
        self.actionbutton_g58_2.setObjectName(u"actionbutton_g58_2")
        self.actionbutton_g58_2.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.actionbutton_g58_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g58_2.setSizePolicy(sizePolicy4)
        self.actionbutton_g58_2.setMinimumSize(QSize(110, 38))
        self.actionbutton_g58_2.setMaximumSize(QSize(110, 38))
        self.actionbutton_g58_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_g58_2.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g58_2, 1, 4, 1, 1)

        self.actionbutton_g59_4 = ActionButton(self.frame_15)
        self.actionbutton_g59_4.setObjectName(u"actionbutton_g59_4")
        self.actionbutton_g59_4.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.actionbutton_g59_4.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_4.setSizePolicy(sizePolicy4)
        self.actionbutton_g59_4.setMinimumSize(QSize(110, 38))
        self.actionbutton_g59_4.setMaximumSize(QSize(110, 38))
        self.actionbutton_g59_4.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_g59_4.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g59_4, 2, 1, 1, 1)

        self.actionbutton_g59_5 = ActionButton(self.frame_15)
        self.actionbutton_g59_5.setObjectName(u"actionbutton_g59_5")
        self.actionbutton_g59_5.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.actionbutton_g59_5.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_5.setSizePolicy(sizePolicy4)
        self.actionbutton_g59_5.setMinimumSize(QSize(110, 38))
        self.actionbutton_g59_5.setMaximumSize(QSize(110, 38))
        self.actionbutton_g59_5.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_g59_5.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g59_5, 2, 2, 1, 1)

        self.actionbutton_g59_6 = ActionButton(self.frame_15)
        self.actionbutton_g59_6.setObjectName(u"actionbutton_g59_6")
        self.actionbutton_g59_6.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.actionbutton_g59_6.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_6.setSizePolicy(sizePolicy4)
        self.actionbutton_g59_6.setMinimumSize(QSize(110, 38))
        self.actionbutton_g59_6.setMaximumSize(QSize(110, 38))
        self.actionbutton_g59_6.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_g59_6.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g59_6, 2, 3, 1, 1)

        self.actionbutton_g59_7 = ActionButton(self.frame_15)
        self.actionbutton_g59_7.setObjectName(u"actionbutton_g59_7")
        self.actionbutton_g59_7.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.actionbutton_g59_7.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_7.setSizePolicy(sizePolicy4)
        self.actionbutton_g59_7.setMinimumSize(QSize(110, 38))
        self.actionbutton_g59_7.setMaximumSize(QSize(110, 38))
        self.actionbutton_g59_7.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_g59_7.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g59_7, 2, 4, 1, 1)


        self.verticalLayout_33.addLayout(self.gridLayout_12)

        self.frame_31 = QFrame(self.frame_15)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"QFrame{\n"
"    border: none;\n"
"}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.verticalLayout_33.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_15)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy12.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy12)
        self.frame_32.setMaximumSize(QSize(16777215, 70))
        self.frame_32.setStyleSheet(u"QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(176, 179,172);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"background-color: rgb(90, 90, 90);\n"
"padding: -5px;\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_32)
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(10, -1, 11, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.axis_column_header_9 = QLabel(self.frame_32)
        self.axis_column_header_9.setObjectName(u"axis_column_header_9")
        sizePolicy1.setHeightForWidth(self.axis_column_header_9.sizePolicy().hasHeightForWidth())
        self.axis_column_header_9.setSizePolicy(sizePolicy1)
        self.axis_column_header_9.setMinimumSize(QSize(55, 50))
        self.axis_column_header_9.setMaximumSize(QSize(55, 50))
        self.axis_column_header_9.setStyleSheet(u"QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_column_header_9.setAlignment(Qt.AlignCenter)
        self.axis_column_header_9.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.axis_column_header_9)

        self.axis_column_header_10 = QLabel(self.frame_32)
        self.axis_column_header_10.setObjectName(u"axis_column_header_10")
        sizePolicy1.setHeightForWidth(self.axis_column_header_10.sizePolicy().hasHeightForWidth())
        self.axis_column_header_10.setSizePolicy(sizePolicy1)
        self.axis_column_header_10.setMinimumSize(QSize(45, 50))
        self.axis_column_header_10.setMaximumSize(QSize(45, 50))
        self.axis_column_header_10.setStyleSheet(u"QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_column_header_10.setAlignment(Qt.AlignCenter)
        self.axis_column_header_10.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.axis_column_header_10)

        self.machine_column_header_10 = QLabel(self.frame_32)
        self.machine_column_header_10.setObjectName(u"machine_column_header_10")
        sizePolicy1.setHeightForWidth(self.machine_column_header_10.sizePolicy().hasHeightForWidth())
        self.machine_column_header_10.setSizePolicy(sizePolicy1)
        self.machine_column_header_10.setMinimumSize(QSize(88, 50))
        self.machine_column_header_10.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_10.setStyleSheet(u"QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header_10.setAlignment(Qt.AlignCenter)
        self.machine_column_header_10.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.machine_column_header_10)

        self.machine_column_header_11 = QLabel(self.frame_32)
        self.machine_column_header_11.setObjectName(u"machine_column_header_11")
        sizePolicy1.setHeightForWidth(self.machine_column_header_11.sizePolicy().hasHeightForWidth())
        self.machine_column_header_11.setSizePolicy(sizePolicy1)
        self.machine_column_header_11.setMinimumSize(QSize(85, 50))
        self.machine_column_header_11.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_11.setStyleSheet(u"QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header_11.setAlignment(Qt.AlignCenter)
        self.machine_column_header_11.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.machine_column_header_11)

        self.machine_column_header_12 = QLabel(self.frame_32)
        self.machine_column_header_12.setObjectName(u"machine_column_header_12")
        sizePolicy1.setHeightForWidth(self.machine_column_header_12.sizePolicy().hasHeightForWidth())
        self.machine_column_header_12.setSizePolicy(sizePolicy1)
        self.machine_column_header_12.setMinimumSize(QSize(60, 50))
        self.machine_column_header_12.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_12.setStyleSheet(u"QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header_12.setAlignment(Qt.AlignCenter)
        self.machine_column_header_12.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.machine_column_header_12)

        self.ref_coilumn_header_4 = QLabel(self.frame_32)
        self.ref_coilumn_header_4.setObjectName(u"ref_coilumn_header_4")
        sizePolicy12.setHeightForWidth(self.ref_coilumn_header_4.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_4.setSizePolicy(sizePolicy12)
        self.ref_coilumn_header_4.setMinimumSize(QSize(65, 50))
        self.ref_coilumn_header_4.setMaximumSize(QSize(16777215, 50))
        self.ref_coilumn_header_4.setStyleSheet(u"QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_4.setAlignment(Qt.AlignCenter)
        self.ref_coilumn_header_4.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.ref_coilumn_header_4)

        self.machine_column_header_13 = QLabel(self.frame_32)
        self.machine_column_header_13.setObjectName(u"machine_column_header_13")
        sizePolicy1.setHeightForWidth(self.machine_column_header_13.sizePolicy().hasHeightForWidth())
        self.machine_column_header_13.setSizePolicy(sizePolicy1)
        self.machine_column_header_13.setMinimumSize(QSize(65, 50))
        self.machine_column_header_13.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_13.setStyleSheet(u"QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header_13.setAlignment(Qt.AlignCenter)
        self.machine_column_header_13.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.machine_column_header_13)


        self.verticalLayout_34.addLayout(self.horizontalLayout_7)


        self.verticalLayout_33.addWidget(self.frame_32)

        self.dro_qvboxlayout_3 = QVBoxLayout()
        self.dro_qvboxlayout_3.setSpacing(15)
        self.dro_qvboxlayout_3.setObjectName(u"dro_qvboxlayout_3")
        self.dro_qvboxlayout_3.setContentsMargins(6, 0, 6, 5)
        self.x_axis_dro_layout_3 = QHBoxLayout()
        self.x_axis_dro_layout_3.setSpacing(12)
        self.x_axis_dro_layout_3.setObjectName(u"x_axis_dro_layout_3")
        self.x_axis_dro_layout_3.setContentsMargins(-1, 1, -1, 1)
        self.zero_x_button_2 = MDIButton(self.frame_15)
        self.zero_x_button_2.setObjectName(u"zero_x_button_2")
        self.zero_x_button_2.setEnabled(False)
        self.zero_x_button_2.setMinimumSize(QSize(55, 38))
        self.zero_x_button_2.setMaximumSize(QSize(55, 38))
        self.zero_x_button_2.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.x_axis_dro_layout_3.addWidget(self.zero_x_button_2)

        self.axis_column_header_11 = QLabel(self.frame_15)
        self.axis_column_header_11.setObjectName(u"axis_column_header_11")
        sizePolicy1.setHeightForWidth(self.axis_column_header_11.sizePolicy().hasHeightForWidth())
        self.axis_column_header_11.setSizePolicy(sizePolicy1)
        self.axis_column_header_11.setMinimumSize(QSize(45, 35))
        self.axis_column_header_11.setMaximumSize(QSize(45, 35))
        self.axis_column_header_11.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_column_header_11.setAlignment(Qt.AlignCenter)

        self.x_axis_dro_layout_3.addWidget(self.axis_column_header_11)

        self.statuslabel_50 = StatusLabel(self.frame_15)
        self.statuslabel_50.setObjectName(u"statuslabel_50")
        self.statuslabel_50.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.x_axis_dro_layout_3.addWidget(self.statuslabel_50)

        self.statuslabel_51 = StatusLabel(self.frame_15)
        self.statuslabel_51.setObjectName(u"statuslabel_51")
        self.statuslabel_51.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.x_axis_dro_layout_3.addWidget(self.statuslabel_51)

        self.statuslabel_52 = StatusLabel(self.frame_15)
        self.statuslabel_52.setObjectName(u"statuslabel_52")
        self.statuslabel_52.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.x_axis_dro_layout_3.addWidget(self.statuslabel_52)

        self.statuslabel_53 = StatusLabel(self.frame_15)
        self.statuslabel_53.setObjectName(u"statuslabel_53")
        self.statuslabel_53.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.x_axis_dro_layout_3.addWidget(self.statuslabel_53)

        self.statuslabel_54 = StatusLabel(self.frame_15)
        self.statuslabel_54.setObjectName(u"statuslabel_54")
        self.statuslabel_54.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_54.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.x_axis_dro_layout_3.addWidget(self.statuslabel_54)


        self.dro_qvboxlayout_3.addLayout(self.x_axis_dro_layout_3)

        self.y_axis_dro_layout_3 = QHBoxLayout()
        self.y_axis_dro_layout_3.setSpacing(12)
        self.y_axis_dro_layout_3.setObjectName(u"y_axis_dro_layout_3")
        self.y_axis_dro_layout_3.setContentsMargins(-1, 1, -1, 1)
        self.zero_y_button_2 = MDIButton(self.frame_15)
        self.zero_y_button_2.setObjectName(u"zero_y_button_2")
        self.zero_y_button_2.setEnabled(False)
        self.zero_y_button_2.setMinimumSize(QSize(55, 38))
        self.zero_y_button_2.setMaximumSize(QSize(55, 38))
        self.zero_y_button_2.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.y_axis_dro_layout_3.addWidget(self.zero_y_button_2)

        self.axis_column_header_12 = QLabel(self.frame_15)
        self.axis_column_header_12.setObjectName(u"axis_column_header_12")
        self.axis_column_header_12.setMinimumSize(QSize(45, 35))
        self.axis_column_header_12.setMaximumSize(QSize(45, 35))
        self.axis_column_header_12.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_column_header_12.setAlignment(Qt.AlignCenter)

        self.y_axis_dro_layout_3.addWidget(self.axis_column_header_12)

        self.statuslabel_55 = StatusLabel(self.frame_15)
        self.statuslabel_55.setObjectName(u"statuslabel_55")
        self.statuslabel_55.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_55.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.y_axis_dro_layout_3.addWidget(self.statuslabel_55)

        self.statuslabel_56 = StatusLabel(self.frame_15)
        self.statuslabel_56.setObjectName(u"statuslabel_56")
        self.statuslabel_56.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_56.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.y_axis_dro_layout_3.addWidget(self.statuslabel_56)

        self.statuslabel_57 = StatusLabel(self.frame_15)
        self.statuslabel_57.setObjectName(u"statuslabel_57")
        self.statuslabel_57.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_57.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.y_axis_dro_layout_3.addWidget(self.statuslabel_57)

        self.statuslabel_58 = StatusLabel(self.frame_15)
        self.statuslabel_58.setObjectName(u"statuslabel_58")
        self.statuslabel_58.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_58.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.y_axis_dro_layout_3.addWidget(self.statuslabel_58)

        self.statuslabel_59 = StatusLabel(self.frame_15)
        self.statuslabel_59.setObjectName(u"statuslabel_59")
        self.statuslabel_59.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.y_axis_dro_layout_3.addWidget(self.statuslabel_59)


        self.dro_qvboxlayout_3.addLayout(self.y_axis_dro_layout_3)

        self.z_axis_dro_layout_3 = QHBoxLayout()
        self.z_axis_dro_layout_3.setSpacing(12)
        self.z_axis_dro_layout_3.setObjectName(u"z_axis_dro_layout_3")
        self.z_axis_dro_layout_3.setContentsMargins(-1, 1, -1, 1)
        self.zero_z_button_2 = MDIButton(self.frame_15)
        self.zero_z_button_2.setObjectName(u"zero_z_button_2")
        self.zero_z_button_2.setEnabled(False)
        self.zero_z_button_2.setMinimumSize(QSize(55, 38))
        self.zero_z_button_2.setMaximumSize(QSize(55, 38))
        self.zero_z_button_2.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.z_axis_dro_layout_3.addWidget(self.zero_z_button_2)

        self.axis_column_header_13 = QLabel(self.frame_15)
        self.axis_column_header_13.setObjectName(u"axis_column_header_13")
        self.axis_column_header_13.setMinimumSize(QSize(45, 35))
        self.axis_column_header_13.setMaximumSize(QSize(45, 35))
        self.axis_column_header_13.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_column_header_13.setAlignment(Qt.AlignCenter)

        self.z_axis_dro_layout_3.addWidget(self.axis_column_header_13)

        self.statuslabel_60 = StatusLabel(self.frame_15)
        self.statuslabel_60.setObjectName(u"statuslabel_60")
        self.statuslabel_60.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.z_axis_dro_layout_3.addWidget(self.statuslabel_60)

        self.statuslabel_61 = StatusLabel(self.frame_15)
        self.statuslabel_61.setObjectName(u"statuslabel_61")
        self.statuslabel_61.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.z_axis_dro_layout_3.addWidget(self.statuslabel_61)

        self.statuslabel_62 = StatusLabel(self.frame_15)
        self.statuslabel_62.setObjectName(u"statuslabel_62")
        self.statuslabel_62.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_62.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.z_axis_dro_layout_3.addWidget(self.statuslabel_62)

        self.statuslabel_63 = StatusLabel(self.frame_15)
        self.statuslabel_63.setObjectName(u"statuslabel_63")
        self.statuslabel_63.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.z_axis_dro_layout_3.addWidget(self.statuslabel_63)

        self.statuslabel_64 = StatusLabel(self.frame_15)
        self.statuslabel_64.setObjectName(u"statuslabel_64")
        self.statuslabel_64.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.z_axis_dro_layout_3.addWidget(self.statuslabel_64)


        self.dro_qvboxlayout_3.addLayout(self.z_axis_dro_layout_3)

        self.a_axis_dro_layout_3 = QHBoxLayout()
        self.a_axis_dro_layout_3.setSpacing(12)
        self.a_axis_dro_layout_3.setObjectName(u"a_axis_dro_layout_3")
        self.a_axis_dro_layout_3.setContentsMargins(-1, 1, -1, 1)
        self.zero_a_button_2 = MDIButton(self.frame_15)
        self.zero_a_button_2.setObjectName(u"zero_a_button_2")
        self.zero_a_button_2.setEnabled(False)
        self.zero_a_button_2.setMinimumSize(QSize(55, 38))
        self.zero_a_button_2.setMaximumSize(QSize(55, 38))
        self.zero_a_button_2.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.a_axis_dro_layout_3.addWidget(self.zero_a_button_2)

        self.axis_column_header_14 = QLabel(self.frame_15)
        self.axis_column_header_14.setObjectName(u"axis_column_header_14")
        self.axis_column_header_14.setMinimumSize(QSize(45, 35))
        self.axis_column_header_14.setMaximumSize(QSize(45, 35))
        self.axis_column_header_14.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_column_header_14.setAlignment(Qt.AlignCenter)

        self.a_axis_dro_layout_3.addWidget(self.axis_column_header_14)

        self.statuslabel_65 = StatusLabel(self.frame_15)
        self.statuslabel_65.setObjectName(u"statuslabel_65")
        self.statuslabel_65.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.a_axis_dro_layout_3.addWidget(self.statuslabel_65)

        self.statuslabel_66 = StatusLabel(self.frame_15)
        self.statuslabel_66.setObjectName(u"statuslabel_66")
        self.statuslabel_66.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_66.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.a_axis_dro_layout_3.addWidget(self.statuslabel_66)

        self.statuslabel_67 = StatusLabel(self.frame_15)
        self.statuslabel_67.setObjectName(u"statuslabel_67")
        self.statuslabel_67.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_67.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.a_axis_dro_layout_3.addWidget(self.statuslabel_67)

        self.statuslabel_68 = StatusLabel(self.frame_15)
        self.statuslabel_68.setObjectName(u"statuslabel_68")
        self.statuslabel_68.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_68.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.a_axis_dro_layout_3.addWidget(self.statuslabel_68)

        self.statuslabel_69 = StatusLabel(self.frame_15)
        self.statuslabel_69.setObjectName(u"statuslabel_69")
        self.statuslabel_69.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_69.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.a_axis_dro_layout_3.addWidget(self.statuslabel_69)


        self.dro_qvboxlayout_3.addLayout(self.a_axis_dro_layout_3)

        self.b_axis_dro_layout_4 = QHBoxLayout()
        self.b_axis_dro_layout_4.setSpacing(12)
        self.b_axis_dro_layout_4.setObjectName(u"b_axis_dro_layout_4")
        self.b_axis_dro_layout_4.setContentsMargins(-1, 1, -1, 1)
        self.zero_b_button_2 = MDIButton(self.frame_15)
        self.zero_b_button_2.setObjectName(u"zero_b_button_2")
        self.zero_b_button_2.setEnabled(False)
        self.zero_b_button_2.setMinimumSize(QSize(55, 38))
        self.zero_b_button_2.setMaximumSize(QSize(55, 38))
        self.zero_b_button_2.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.b_axis_dro_layout_4.addWidget(self.zero_b_button_2)

        self.axis_column_header_15 = QLabel(self.frame_15)
        self.axis_column_header_15.setObjectName(u"axis_column_header_15")
        self.axis_column_header_15.setMinimumSize(QSize(45, 35))
        self.axis_column_header_15.setMaximumSize(QSize(45, 35))
        self.axis_column_header_15.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_column_header_15.setAlignment(Qt.AlignCenter)

        self.b_axis_dro_layout_4.addWidget(self.axis_column_header_15)

        self.statuslabel_70 = StatusLabel(self.frame_15)
        self.statuslabel_70.setObjectName(u"statuslabel_70")
        self.statuslabel_70.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_70.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.b_axis_dro_layout_4.addWidget(self.statuslabel_70)

        self.statuslabel_71 = StatusLabel(self.frame_15)
        self.statuslabel_71.setObjectName(u"statuslabel_71")
        self.statuslabel_71.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_71.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.b_axis_dro_layout_4.addWidget(self.statuslabel_71)

        self.statuslabel_72 = StatusLabel(self.frame_15)
        self.statuslabel_72.setObjectName(u"statuslabel_72")
        self.statuslabel_72.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_72.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.b_axis_dro_layout_4.addWidget(self.statuslabel_72)

        self.statuslabel_73 = StatusLabel(self.frame_15)
        self.statuslabel_73.setObjectName(u"statuslabel_73")
        self.statuslabel_73.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_73.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.b_axis_dro_layout_4.addWidget(self.statuslabel_73)

        self.statuslabel_74 = StatusLabel(self.frame_15)
        self.statuslabel_74.setObjectName(u"statuslabel_74")
        self.statuslabel_74.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_74.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.b_axis_dro_layout_4.addWidget(self.statuslabel_74)


        self.dro_qvboxlayout_3.addLayout(self.b_axis_dro_layout_4)


        self.verticalLayout_33.addLayout(self.dro_qvboxlayout_3)


        self.horizontalLayout_51.addWidget(self.frame_15)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(-1, -1, 0, -1)
        self.frame_38 = QFrame(self.tab_16)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy4.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy4)
        self.frame_38.setMinimumSize(QSize(345, 560))
        self.frame_38.setMaximumSize(QSize(345, 560))
        self.frame_38.setStyleSheet(u"QFrame{\n"
"border-style: none;\n"
"border-color: transparent;\n"
"background-color: transparent;\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.label_47 = QLabel(self.frame_38)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(120, 250, 200, 167))
        self.label_47.setStyleSheet(u"image: url(:/images/tool_probe.png);")
        self.label_47.setScaledContents(True)
        self.label_51 = QLabel(self.frame_38)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(61, 0, 140, 231))
        self.label_51.setStyleSheet(u"image: url(:/images/atc_spindle_tool.png);")
        self.label_51.setScaledContents(True)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setGeometry(QRect(2, 440, 340, 120))
        self.frame_39.setMinimumSize(QSize(340, 120))
        self.frame_39.setMaximumSize(QSize(330, 120))
        self.frame_39.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.verticalLayoutWidget_6 = QWidget(self.frame_39)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(3, 10, 334, 93))
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_13.setSpacing(12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, 2, 5, 2)
        self.set_tool_touch_off_position_button_2 = MDIButton(self.verticalLayoutWidget_6)
        self.set_tool_touch_off_position_button_2.setObjectName(u"set_tool_touch_off_position_button_2")
        self.set_tool_touch_off_position_button_2.setEnabled(False)
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.set_tool_touch_off_position_button_2.sizePolicy().hasHeightForWidth())
        self.set_tool_touch_off_position_button_2.setSizePolicy(sizePolicy13)
        self.set_tool_touch_off_position_button_2.setMinimumSize(QSize(280, 40))
        self.set_tool_touch_off_position_button_2.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_22.addWidget(self.set_tool_touch_off_position_button_2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(2)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_55 = QLabel(self.verticalLayoutWidget_6)
        self.label_55.setObjectName(u"label_55")
        sizePolicy4.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy4)
        self.label_55.setMinimumSize(QSize(23, 33))
        self.label_55.setMaximumSize(QSize(23, 33))
        self.label_55.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"background: transparent;\n"
"font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_55)

        self.tool_length_2 = StatusLabel(self.verticalLayoutWidget_6)
        self.tool_length_2.setObjectName(u"tool_length_2")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(1)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.tool_length_2.sizePolicy().hasHeightForWidth())
        self.tool_length_2.setSizePolicy(sizePolicy14)
        self.tool_length_2.setMinimumSize(QSize(75, 33))
        self.tool_length_2.setMaximumSize(QSize(70, 33))
        self.tool_length_2.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_length_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.tool_length_2)

        self.label_57 = QLabel(self.verticalLayoutWidget_6)
        self.label_57.setObjectName(u"label_57")
        sizePolicy4.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy4)
        self.label_57.setMinimumSize(QSize(23, 33))
        self.label_57.setMaximumSize(QSize(23, 33))
        self.label_57.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"background: transparent;\n"
"font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_57)

        self.tool_length_4 = StatusLabel(self.verticalLayoutWidget_6)
        self.tool_length_4.setObjectName(u"tool_length_4")
        sizePolicy14.setHeightForWidth(self.tool_length_4.sizePolicy().hasHeightForWidth())
        self.tool_length_4.setSizePolicy(sizePolicy14)
        self.tool_length_4.setMinimumSize(QSize(75, 33))
        self.tool_length_4.setMaximumSize(QSize(70, 33))
        self.tool_length_4.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_length_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.tool_length_4)

        self.label_58 = QLabel(self.verticalLayoutWidget_6)
        self.label_58.setObjectName(u"label_58")
        sizePolicy4.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy4)
        self.label_58.setMinimumSize(QSize(23, 33))
        self.label_58.setMaximumSize(QSize(23, 33))
        self.label_58.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"background: transparent;\n"
"font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_58)

        self.tool_length_3 = StatusLabel(self.verticalLayoutWidget_6)
        self.tool_length_3.setObjectName(u"tool_length_3")
        sizePolicy14.setHeightForWidth(self.tool_length_3.sizePolicy().hasHeightForWidth())
        self.tool_length_3.setSizePolicy(sizePolicy14)
        self.tool_length_3.setMinimumSize(QSize(75, 33))
        self.tool_length_3.setMaximumSize(QSize(70, 33))
        self.tool_length_3.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_length_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.tool_length_3)


        self.verticalLayout_13.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_131.addWidget(self.frame_38)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_131)

        self.tabWidget.addTab(self.tab_16, "")
        self.tooling_tab = QWidget()
        self.tooling_tab.setObjectName(u"tooling_tab")
        self.horizontalLayout_41 = QHBoxLayout(self.tooling_tab)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(15, 25, -1, 25)
        self.frame_13 = QFrame(self.tooling_tab)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.frame_13)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(5, 5, 5, -1)
        self.tableWidget_2 = ToolTable(self.frame_13)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        palette2 = QPalette()
        brush6 = QBrush(QColor(235, 235, 238, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        self.tableWidget_2.setPalette(palette2)
        font8 = QFont()
        font8.setFamilies([u"Probe Basic Bebas Mono"])
        font8.setPointSize(15)
        font8.setBold(False)
        font8.setItalic(False)
        self.tableWidget_2.setFont(font8)
        self.tableWidget_2.setStyleSheet(u"TootTable,\n"
"QHeaderView {\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"	background-color: rgb(220, 220, 220);\n"
"	color: black;\n"
"    border: none;\n"
"}\n"
"\n"
"ToolTable {\n"
"   	border-top: 8px rgb(120, 120, 120);\n"
"	border-left: 4px  rgb(120, 120, 120);\n"
"	border-bottom: 5px rgb(120, 120, 120);\n"
"	border-right: 4px rgb(120, 120, 120);\n"
"	border-radius: 5px;\n"
"	border-color: rgb(120, 120, 120);\n"
"	border-style: solid;\n"
"	background-color: rgb(120, 120, 120);\n"
"    gridline-color: rgb(203, 203, 203);\n"
"	alternate-background-color: rgb(90, 90, 90);\n"
"}")
        self.tableWidget_2.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_2.setFrameShadow(QFrame.Sunken)
        self.tableWidget_2.setLineWidth(3)
        self.tableWidget_2.setMidLineWidth(3)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableWidget_2.setProperty(u"showDropIndicator", True)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(90)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)

        self.horizontalLayout_38.addWidget(self.tableWidget_2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.tool_table_delete_button = QPushButton(self.frame_13)
        self.tool_table_delete_button.setObjectName(u"tool_table_delete_button")
        sizePolicy4.setHeightForWidth(self.tool_table_delete_button.sizePolicy().hasHeightForWidth())
        self.tool_table_delete_button.setSizePolicy(sizePolicy4)
        self.tool_table_delete_button.setMinimumSize(QSize(120, 33))
        self.tool_table_delete_button.setMaximumSize(QSize(120, 33))
        self.tool_table_delete_button.setFocusPolicy(Qt.NoFocus)
        self.tool_table_delete_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_37.addWidget(self.tool_table_delete_button)

        self.tool_table_add_tool_button = QPushButton(self.frame_13)
        self.tool_table_add_tool_button.setObjectName(u"tool_table_add_tool_button")
        sizePolicy4.setHeightForWidth(self.tool_table_add_tool_button.sizePolicy().hasHeightForWidth())
        self.tool_table_add_tool_button.setSizePolicy(sizePolicy4)
        self.tool_table_add_tool_button.setMinimumSize(QSize(120, 33))
        self.tool_table_add_tool_button.setMaximumSize(QSize(120, 33))
        self.tool_table_add_tool_button.setFocusPolicy(Qt.NoFocus)
        self.tool_table_add_tool_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_37.addWidget(self.tool_table_add_tool_button)

        self.tool_table_reread_button = QPushButton(self.frame_13)
        self.tool_table_reread_button.setObjectName(u"tool_table_reread_button")
        sizePolicy4.setHeightForWidth(self.tool_table_reread_button.sizePolicy().hasHeightForWidth())
        self.tool_table_reread_button.setSizePolicy(sizePolicy4)
        self.tool_table_reread_button.setMinimumSize(QSize(120, 33))
        self.tool_table_reread_button.setMaximumSize(QSize(120, 33))
        self.tool_table_reread_button.setFocusPolicy(Qt.NoFocus)
        self.tool_table_reread_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_37.addWidget(self.tool_table_reread_button)

        self.tool_table_save_button = QPushButton(self.frame_13)
        self.tool_table_save_button.setObjectName(u"tool_table_save_button")
        sizePolicy4.setHeightForWidth(self.tool_table_save_button.sizePolicy().hasHeightForWidth())
        self.tool_table_save_button.setSizePolicy(sizePolicy4)
        self.tool_table_save_button.setMinimumSize(QSize(120, 33))
        self.tool_table_save_button.setMaximumSize(QSize(120, 33))
        self.tool_table_save_button.setFocusPolicy(Qt.NoFocus)
        self.tool_table_save_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_37.addWidget(self.tool_table_save_button)

        self.tool_table_reload_button = QPushButton(self.frame_13)
        self.tool_table_reload_button.setObjectName(u"tool_table_reload_button")
        sizePolicy4.setHeightForWidth(self.tool_table_reload_button.sizePolicy().hasHeightForWidth())
        self.tool_table_reload_button.setSizePolicy(sizePolicy4)
        self.tool_table_reload_button.setMinimumSize(QSize(140, 33))
        self.tool_table_reload_button.setMaximumSize(QSize(140, 33))
        self.tool_table_reload_button.setFocusPolicy(Qt.NoFocus)
        self.tool_table_reload_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_37.addWidget(self.tool_table_reload_button)


        self.verticalLayout_20.addLayout(self.horizontalLayout_37)


        self.horizontalLayout_40.addWidget(self.frame_13)


        self.horizontalLayout_41.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, -1, 10, -1)
        self.frame_10 = QFrame(self.tooling_tab)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy4.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy4)
        self.frame_10.setMinimumSize(QSize(580, 590))
        self.frame_10.setMaximumSize(QSize(580, 590))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"border-style: none;\n"
"border-color: transparent;\n"
"background-color: transparent;\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.label_43 = QLabel(self.frame_10)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(195, 78, 250, 403))
        self.label_43.setStyleSheet(u"image: url(:/images/atc_spindle_tool_dimensioned.png);")
        self.label_43.setPixmap(QPixmap(u":/images/atc_spindle_tool_dimensioned.png"))
        self.label_43.setScaledContents(True)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(122, 267, 145, 60))
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setMinimumSize(QSize(100, 60))
        self.frame_11.setMaximumSize(QSize(16777215, 58))
        self.frame_11.setStyleSheet(u"QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.horizontalLayout_98 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_48 = QLabel(self.frame_11)
        self.label_48.setObjectName(u"label_48")
        sizePolicy4.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy4)
        self.label_48.setMinimumSize(QSize(48, 33))
        self.label_48.setMaximumSize(QSize(48, 33))
        self.label_48.setStyleSheet(u"QLabel{\n"
"font: 75 13pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 0px;\n"
"padding-left: 0px;\n"
"border-style: none;\n"
"}")
        self.label_48.setAlignment(Qt.AlignCenter)
        self.label_48.setWordWrap(True)

        self.horizontalLayout_17.addWidget(self.label_48)

        self.tool_length_5 = StatusLabel(self.frame_11)
        self.tool_length_5.setObjectName(u"tool_length_5")
        sizePolicy8.setHeightForWidth(self.tool_length_5.sizePolicy().hasHeightForWidth())
        self.tool_length_5.setSizePolicy(sizePolicy8)
        self.tool_length_5.setMinimumSize(QSize(70, 33))
        self.tool_length_5.setMaximumSize(QSize(70, 33))
        self.tool_length_5.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_length_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.tool_length_5)


        self.horizontalLayout_98.addLayout(self.horizontalLayout_17)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(180, 446, 132, 60))
        sizePolicy4.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy4)
        self.frame_12.setMinimumSize(QSize(100, 60))
        self.frame_12.setMaximumSize(QSize(16777215, 60))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.horizontalLayout_99 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_49 = QLabel(self.frame_12)
        self.label_49.setObjectName(u"label_49")
        sizePolicy4.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy4)
        self.label_49.setMinimumSize(QSize(35, 33))
        self.label_49.setMaximumSize(QSize(35, 33))
        self.label_49.setStyleSheet(u"QLabel{\n"
"font: 75 13pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 0px;\n"
"padding-left: 0px;\n"
"border-style: none;\n"
"}")
        self.label_49.setAlignment(Qt.AlignCenter)
        self.label_49.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.label_49)

        self.tool_diameter_2 = StatusLabel(self.frame_12)
        self.tool_diameter_2.setObjectName(u"tool_diameter_2")
        sizePolicy8.setHeightForWidth(self.tool_diameter_2.sizePolicy().hasHeightForWidth())
        self.tool_diameter_2.setSizePolicy(sizePolicy8)
        self.tool_diameter_2.setMinimumSize(QSize(70, 33))
        self.tool_diameter_2.setMaximumSize(QSize(70, 33))
        self.tool_diameter_2.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_diameter_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.tool_diameter_2)


        self.horizontalLayout_99.addLayout(self.horizontalLayout_18)

        self.frame_28 = QFrame(self.frame_10)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(4, 0, 570, 60))
        sizePolicy4.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy4)
        self.frame_28.setMinimumSize(QSize(570, 60))
        self.frame_28.setMaximumSize(QSize(570, 58))
        self.frame_28.setStyleSheet(u"QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.horizontalLayout_108 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setSpacing(3)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.label_56 = QLabel(self.frame_28)
        self.label_56.setObjectName(u"label_56")
        sizePolicy4.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy4)
        self.label_56.setMinimumSize(QSize(60, 33))
        self.label_56.setMaximumSize(QSize(60, 33))
        self.label_56.setStyleSheet(u"QLabel{\n"
"font: 75 13pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 0px;\n"
"padding-left: 0px;\n"
"border-style: none;\n"
"}")
        self.label_56.setAlignment(Qt.AlignCenter)
        self.label_56.setWordWrap(True)

        self.horizontalLayout_109.addWidget(self.label_56)

        self.tool_length_7 = StatusLabel(self.frame_28)
        self.tool_length_7.setObjectName(u"tool_length_7")
        sizePolicy1.setHeightForWidth(self.tool_length_7.sizePolicy().hasHeightForWidth())
        self.tool_length_7.setSizePolicy(sizePolicy1)
        self.tool_length_7.setMinimumSize(QSize(70, 33))
        self.tool_length_7.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_length_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tool_length_7.setIndent(4)

        self.horizontalLayout_109.addWidget(self.tool_length_7)


        self.horizontalLayout_108.addLayout(self.horizontalLayout_109)

        self.mdi_entry_box_4 = MDIEntry(self.frame_10)
        self.mdi_entry_box_4.setObjectName(u"mdi_entry_box_4")
        self.mdi_entry_box_4.setGeometry(QRect(4, 550, 570, 40))
        sizePolicy4.setHeightForWidth(self.mdi_entry_box_4.sizePolicy().hasHeightForWidth())
        self.mdi_entry_box_4.setSizePolicy(sizePolicy4)
        self.mdi_entry_box_4.setMinimumSize(QSize(570, 40))
        self.mdi_entry_box_4.setMaximumSize(QSize(570, 40))
        self.mdi_entry_box_4.setFont(font2)
        self.mdi_entry_box_4.setFocusPolicy(Qt.ClickFocus)
        self.tool_length_6 = StatusLabel(self.frame_10)
        self.tool_length_6.setObjectName(u"tool_length_6")
        self.tool_length_6.setGeometry(QRect(330, 227, 50, 33))
        sizePolicy8.setHeightForWidth(self.tool_length_6.sizePolicy().hasHeightForWidth())
        self.tool_length_6.setSizePolicy(sizePolicy8)
        self.tool_length_6.setMinimumSize(QSize(50, 33))
        self.tool_length_6.setMaximumSize(QSize(50, 33))
        self.tool_length_6.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_length_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.frame_10)


        self.horizontalLayout_41.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tooling_tab, "")
        self.probing_tab = QWidget()
        self.probing_tab.setObjectName(u"probing_tab")
        self.horizontalLayout_70 = QHBoxLayout(self.probing_tab)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.frame_20 = QFrame(self.probing_tab)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy2.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy2)
        self.frame_20.setMinimumSize(QSize(530, 0))
        self.frame_20.setMaximumSize(QSize(530, 16777215))
        self.frame_20.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Plain)
        self.frame_20.setLineWidth(0)
        self.verticalLayout_26 = QVBoxLayout(self.frame_20)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 0, 5, 5)
        self.label_24 = QLabel(self.frame_20)
        self.label_24.setObjectName(u"label_24")
        sizePolicy12.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy12)
        self.label_24.setMinimumSize(QSize(0, 27))
        self.label_24.setMaximumSize(QSize(16777215, 27))
        font9 = QFont()
        font9.setFamilies([u"Probe Basic Bebas Mono"])
        font9.setPointSize(14)
        font9.setBold(False)
        font9.setItalic(False)
        self.label_24.setFont(font9)
        self.label_24.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.label_24)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(6)
        self.gridLayout_8.setContentsMargins(-1, 3, -1, -1)
        self.actionbutton_11 = ActionButton(self.frame_20)
        self.actionbutton_11.setObjectName(u"actionbutton_11")
        sizePolicy4.setHeightForWidth(self.actionbutton_11.sizePolicy().hasHeightForWidth())
        self.actionbutton_11.setSizePolicy(sizePolicy4)
        self.actionbutton_11.setMinimumSize(QSize(120, 32))
        self.actionbutton_11.setMaximumSize(QSize(120, 38))
        self.actionbutton_11.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_11.setAutoExclusive(True)

        self.gridLayout_8.addWidget(self.actionbutton_11, 0, 0, 1, 1)

        self.actionbutton_14 = ActionButton(self.frame_20)
        self.actionbutton_14.setObjectName(u"actionbutton_14")
        sizePolicy4.setHeightForWidth(self.actionbutton_14.sizePolicy().hasHeightForWidth())
        self.actionbutton_14.setSizePolicy(sizePolicy4)
        self.actionbutton_14.setMinimumSize(QSize(120, 32))
        self.actionbutton_14.setMaximumSize(QSize(120, 38))
        self.actionbutton_14.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_14.setAutoExclusive(True)

        self.gridLayout_8.addWidget(self.actionbutton_14, 0, 1, 1, 1)

        self.actionbutton_15 = ActionButton(self.frame_20)
        self.actionbutton_15.setObjectName(u"actionbutton_15")
        sizePolicy4.setHeightForWidth(self.actionbutton_15.sizePolicy().hasHeightForWidth())
        self.actionbutton_15.setSizePolicy(sizePolicy4)
        self.actionbutton_15.setMinimumSize(QSize(120, 32))
        self.actionbutton_15.setMaximumSize(QSize(120, 38))
        self.actionbutton_15.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_15.setAutoExclusive(True)

        self.gridLayout_8.addWidget(self.actionbutton_15, 0, 2, 1, 1)

        self.actionbutton_17 = ActionButton(self.frame_20)
        self.actionbutton_17.setObjectName(u"actionbutton_17")
        sizePolicy4.setHeightForWidth(self.actionbutton_17.sizePolicy().hasHeightForWidth())
        self.actionbutton_17.setSizePolicy(sizePolicy4)
        self.actionbutton_17.setMinimumSize(QSize(120, 32))
        self.actionbutton_17.setMaximumSize(QSize(120, 38))
        self.actionbutton_17.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_17.setAutoExclusive(True)

        self.gridLayout_8.addWidget(self.actionbutton_17, 1, 2, 1, 1)

        self.actionbutton_16 = ActionButton(self.frame_20)
        self.actionbutton_16.setObjectName(u"actionbutton_16")
        sizePolicy4.setHeightForWidth(self.actionbutton_16.sizePolicy().hasHeightForWidth())
        self.actionbutton_16.setSizePolicy(sizePolicy4)
        self.actionbutton_16.setMinimumSize(QSize(120, 32))
        self.actionbutton_16.setMaximumSize(QSize(120, 38))
        self.actionbutton_16.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_16.setAutoExclusive(True)

        self.gridLayout_8.addWidget(self.actionbutton_16, 2, 2, 1, 1)

        self.actionbutton_12 = ActionButton(self.frame_20)
        self.actionbutton_12.setObjectName(u"actionbutton_12")
        sizePolicy4.setHeightForWidth(self.actionbutton_12.sizePolicy().hasHeightForWidth())
        self.actionbutton_12.setSizePolicy(sizePolicy4)
        self.actionbutton_12.setMinimumSize(QSize(120, 32))
        self.actionbutton_12.setMaximumSize(QSize(120, 38))
        self.actionbutton_12.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_12.setAutoExclusive(True)

        self.gridLayout_8.addWidget(self.actionbutton_12, 1, 1, 1, 1)

        self.actionbutton_13 = ActionButton(self.frame_20)
        self.actionbutton_13.setObjectName(u"actionbutton_13")
        sizePolicy4.setHeightForWidth(self.actionbutton_13.sizePolicy().hasHeightForWidth())
        self.actionbutton_13.setSizePolicy(sizePolicy4)
        self.actionbutton_13.setMinimumSize(QSize(120, 32))
        self.actionbutton_13.setMaximumSize(QSize(120, 38))
        self.actionbutton_13.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_13.setAutoExclusive(True)

        self.gridLayout_8.addWidget(self.actionbutton_13, 2, 1, 1, 1)

        self.actionbutton_4 = ActionButton(self.frame_20)
        self.actionbutton_4.setObjectName(u"actionbutton_4")
        sizePolicy4.setHeightForWidth(self.actionbutton_4.sizePolicy().hasHeightForWidth())
        self.actionbutton_4.setSizePolicy(sizePolicy4)
        self.actionbutton_4.setMinimumSize(QSize(120, 32))
        self.actionbutton_4.setMaximumSize(QSize(120, 38))
        self.actionbutton_4.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_4.setAutoExclusive(True)

        self.gridLayout_8.addWidget(self.actionbutton_4, 1, 0, 1, 1)

        self.actionbutton_18 = ActionButton(self.frame_20)
        self.actionbutton_18.setObjectName(u"actionbutton_18")
        sizePolicy4.setHeightForWidth(self.actionbutton_18.sizePolicy().hasHeightForWidth())
        self.actionbutton_18.setSizePolicy(sizePolicy4)
        self.actionbutton_18.setMinimumSize(QSize(120, 32))
        self.actionbutton_18.setMaximumSize(QSize(120, 38))
        self.actionbutton_18.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_18.setAutoExclusive(True)

        self.gridLayout_8.addWidget(self.actionbutton_18, 2, 0, 1, 1)


        self.verticalLayout_26.addLayout(self.gridLayout_8)

        self.label_23 = QLabel(self.frame_20)
        self.label_23.setObjectName(u"label_23")
        sizePolicy12.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy12)
        self.label_23.setMinimumSize(QSize(0, 27))
        self.label_23.setMaximumSize(QSize(16777215, 27))
        self.label_23.setFont(font9)
        self.label_23.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.verticalLayout_26.addWidget(self.label_23)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, 5, -1)
        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.ref_coilumn_header_12 = QLabel(self.frame_20)
        self.ref_coilumn_header_12.setObjectName(u"ref_coilumn_header_12")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_12.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_12.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_12.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_82.addWidget(self.ref_coilumn_header_12)

        self.label_22 = QLabel(self.frame_20)
        self.label_22.setObjectName(u"label_22")
        sizePolicy4.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy4)
        self.label_22.setMinimumSize(QSize(150, 30))
        self.label_22.setMaximumSize(QSize(150, 30))
        self.label_22.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_22.setLineWidth(0)
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_22.setIndent(0)

        self.horizontalLayout_82.addWidget(self.label_22)

        self.probe_tool_number = QLineEdit(self.frame_20)
        self.probe_tool_number.setObjectName(u"probe_tool_number")
        sizePolicy4.setHeightForWidth(self.probe_tool_number.sizePolicy().hasHeightForWidth())
        self.probe_tool_number.setSizePolicy(sizePolicy4)
        self.probe_tool_number.setMinimumSize(QSize(100, 30))
        self.probe_tool_number.setMaximumSize(QSize(100, 30))
        self.probe_tool_number.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.probe_tool_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_82.addWidget(self.probe_tool_number)

        self.label_5 = QLabel(self.frame_20)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMinimumSize(QSize(130, 30))
        self.label_5.setMaximumSize(QSize(130, 30))
        self.label_5.setBaseSize(QSize(140, 30))
        self.label_5.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_5.setLineWidth(0)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5.setIndent(0)

        self.horizontalLayout_82.addWidget(self.label_5)

        self.step_off_width = QLineEdit(self.frame_20)
        self.step_off_width.setObjectName(u"step_off_width")
        sizePolicy4.setHeightForWidth(self.step_off_width.sizePolicy().hasHeightForWidth())
        self.step_off_width.setSizePolicy(sizePolicy4)
        self.step_off_width.setMinimumSize(QSize(100, 30))
        self.step_off_width.setMaximumSize(QSize(100, 30))
        self.step_off_width.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.step_off_width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_82.addWidget(self.step_off_width)


        self.verticalLayout_16.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.ref_coilumn_header_11 = QLabel(self.frame_20)
        self.ref_coilumn_header_11.setObjectName(u"ref_coilumn_header_11")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_11.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_11.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_11.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_80.addWidget(self.ref_coilumn_header_11)

        self.label_6 = QLabel(self.frame_20)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setMinimumSize(QSize(150, 30))
        self.label_6.setMaximumSize(QSize(150, 30))
        self.label_6.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_6.setLineWidth(0)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6.setIndent(0)

        self.horizontalLayout_80.addWidget(self.label_6)

        self.probe_fast_fr = QLineEdit(self.frame_20)
        self.probe_fast_fr.setObjectName(u"probe_fast_fr")
        sizePolicy4.setHeightForWidth(self.probe_fast_fr.sizePolicy().hasHeightForWidth())
        self.probe_fast_fr.setSizePolicy(sizePolicy4)
        self.probe_fast_fr.setMinimumSize(QSize(100, 30))
        self.probe_fast_fr.setMaximumSize(QSize(100, 30))
        self.probe_fast_fr.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.probe_fast_fr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_80.addWidget(self.probe_fast_fr)

        self.label_7 = QLabel(self.frame_20)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(130, 30))
        self.label_7.setMaximumSize(QSize(130, 30))
        self.label_7.setBaseSize(QSize(140, 30))
        self.label_7.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_7.setLineWidth(0)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7.setIndent(0)

        self.horizontalLayout_80.addWidget(self.label_7)

        self.probe_slow_fr = QLineEdit(self.frame_20)
        self.probe_slow_fr.setObjectName(u"probe_slow_fr")
        sizePolicy4.setHeightForWidth(self.probe_slow_fr.sizePolicy().hasHeightForWidth())
        self.probe_slow_fr.setSizePolicy(sizePolicy4)
        self.probe_slow_fr.setMinimumSize(QSize(100, 30))
        self.probe_slow_fr.setMaximumSize(QSize(100, 30))
        self.probe_slow_fr.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.probe_slow_fr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_80.addWidget(self.probe_slow_fr)


        self.verticalLayout_16.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.ref_coilumn_header_10 = QLabel(self.frame_20)
        self.ref_coilumn_header_10.setObjectName(u"ref_coilumn_header_10")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_10.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_10.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_10.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_81.addWidget(self.ref_coilumn_header_10)

        self.label_11 = QLabel(self.frame_20)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setMinimumSize(QSize(150, 30))
        self.label_11.setMaximumSize(QSize(150, 30))
        self.label_11.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_11.setLineWidth(0)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_11.setIndent(0)

        self.horizontalLayout_81.addWidget(self.label_11)

        self.max_xy_distance = QLineEdit(self.frame_20)
        self.max_xy_distance.setObjectName(u"max_xy_distance")
        sizePolicy4.setHeightForWidth(self.max_xy_distance.sizePolicy().hasHeightForWidth())
        self.max_xy_distance.setSizePolicy(sizePolicy4)
        self.max_xy_distance.setMinimumSize(QSize(100, 30))
        self.max_xy_distance.setMaximumSize(QSize(100, 30))
        self.max_xy_distance.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.max_xy_distance.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_81.addWidget(self.max_xy_distance)

        self.label_8 = QLabel(self.frame_20)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMinimumSize(QSize(130, 30))
        self.label_8.setMaximumSize(QSize(130, 30))
        self.label_8.setBaseSize(QSize(140, 30))
        self.label_8.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_8.setLineWidth(0)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8.setIndent(0)

        self.horizontalLayout_81.addWidget(self.label_8)

        self.xy_clearance = QLineEdit(self.frame_20)
        self.xy_clearance.setObjectName(u"xy_clearance")
        sizePolicy4.setHeightForWidth(self.xy_clearance.sizePolicy().hasHeightForWidth())
        self.xy_clearance.setSizePolicy(sizePolicy4)
        self.xy_clearance.setMinimumSize(QSize(100, 30))
        self.xy_clearance.setMaximumSize(QSize(100, 30))
        self.xy_clearance.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.xy_clearance.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_81.addWidget(self.xy_clearance)


        self.verticalLayout_16.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.ref_coilumn_header_9 = QLabel(self.frame_20)
        self.ref_coilumn_header_9.setObjectName(u"ref_coilumn_header_9")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_9.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_9.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_9.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.ref_coilumn_header_9)

        self.label_10 = QLabel(self.frame_20)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setMinimumSize(QSize(150, 30))
        self.label_10.setMaximumSize(QSize(150, 30))
        self.label_10.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_10.setLineWidth(0)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_10.setIndent(0)

        self.horizontalLayout_79.addWidget(self.label_10)

        self.max_z_distance = QLineEdit(self.frame_20)
        self.max_z_distance.setObjectName(u"max_z_distance")
        sizePolicy4.setHeightForWidth(self.max_z_distance.sizePolicy().hasHeightForWidth())
        self.max_z_distance.setSizePolicy(sizePolicy4)
        self.max_z_distance.setMinimumSize(QSize(100, 30))
        self.max_z_distance.setMaximumSize(QSize(100, 30))
        self.max_z_distance.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.max_z_distance.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_79.addWidget(self.max_z_distance)

        self.label_9 = QLabel(self.frame_20)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setMinimumSize(QSize(130, 30))
        self.label_9.setMaximumSize(QSize(130, 30))
        self.label_9.setBaseSize(QSize(140, 30))
        self.label_9.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_9.setLineWidth(0)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9.setIndent(0)

        self.horizontalLayout_79.addWidget(self.label_9)

        self.z_clearance = QLineEdit(self.frame_20)
        self.z_clearance.setObjectName(u"z_clearance")
        sizePolicy4.setHeightForWidth(self.z_clearance.sizePolicy().hasHeightForWidth())
        self.z_clearance.setSizePolicy(sizePolicy4)
        self.z_clearance.setMinimumSize(QSize(100, 30))
        self.z_clearance.setMaximumSize(QSize(100, 30))
        self.z_clearance.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.z_clearance.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_79.addWidget(self.z_clearance)


        self.verticalLayout_16.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.ref_coilumn_header_8 = QLabel(self.frame_20)
        self.ref_coilumn_header_8.setObjectName(u"ref_coilumn_header_8")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_8.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_8.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_8.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.ref_coilumn_header_8)

        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        self.label_12.setMinimumSize(QSize(150, 30))
        self.label_12.setMaximumSize(QSize(150, 30))
        self.label_12.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_12.setLineWidth(0)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_12.setIndent(0)

        self.horizontalLayout_78.addWidget(self.label_12)

        self.extra_probe_depth = QLineEdit(self.frame_20)
        self.extra_probe_depth.setObjectName(u"extra_probe_depth")
        sizePolicy4.setHeightForWidth(self.extra_probe_depth.sizePolicy().hasHeightForWidth())
        self.extra_probe_depth.setSizePolicy(sizePolicy4)
        self.extra_probe_depth.setMinimumSize(QSize(100, 30))
        self.extra_probe_depth.setMaximumSize(QSize(100, 30))
        self.extra_probe_depth.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.extra_probe_depth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_78.addWidget(self.extra_probe_depth)

        self.label_13 = QLabel(self.frame_20)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)
        self.label_13.setMinimumSize(QSize(130, 30))
        self.label_13.setMaximumSize(QSize(130, 30))
        self.label_13.setBaseSize(QSize(140, 30))
        self.label_13.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_13.setLineWidth(0)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_13.setIndent(0)

        self.horizontalLayout_78.addWidget(self.label_13)

        self.calibration_dia = QLineEdit(self.frame_20)
        self.calibration_dia.setObjectName(u"calibration_dia")
        sizePolicy4.setHeightForWidth(self.calibration_dia.sizePolicy().hasHeightForWidth())
        self.calibration_dia.setSizePolicy(sizePolicy4)
        self.calibration_dia.setMinimumSize(QSize(100, 30))
        self.calibration_dia.setMaximumSize(QSize(100, 30))
        self.calibration_dia.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.calibration_dia.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_78.addWidget(self.calibration_dia)


        self.verticalLayout_16.addLayout(self.horizontalLayout_78)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.ref_coilumn_header_7 = QLabel(self.frame_20)
        self.ref_coilumn_header_7.setObjectName(u"ref_coilumn_header_7")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_7.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_7.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_7.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.ref_coilumn_header_7)

        self.label_54 = QLabel(self.frame_20)
        self.label_54.setObjectName(u"label_54")
        sizePolicy4.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy4)
        self.label_54.setMinimumSize(QSize(130, 30))
        self.label_54.setMaximumSize(QSize(130, 30))
        self.label_54.setBaseSize(QSize(140, 30))
        self.label_54.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_54.setLineWidth(0)
        self.label_54.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_54.setIndent(0)

        self.horizontalLayout_102.addWidget(self.label_54)

        self.step_off_width_2 = QLineEdit(self.frame_20)
        self.step_off_width_2.setObjectName(u"step_off_width_2")
        sizePolicy4.setHeightForWidth(self.step_off_width_2.sizePolicy().hasHeightForWidth())
        self.step_off_width_2.setSizePolicy(sizePolicy4)
        self.step_off_width_2.setMinimumSize(QSize(100, 30))
        self.step_off_width_2.setMaximumSize(QSize(100, 30))
        self.step_off_width_2.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.step_off_width_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_102.addWidget(self.step_off_width_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_102)


        self.verticalLayout_26.addLayout(self.verticalLayout_16)

        self.label_25 = QLabel(self.frame_20)
        self.label_25.setObjectName(u"label_25")
        sizePolicy12.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy12)
        self.label_25.setMinimumSize(QSize(0, 27))
        self.label_25.setMaximumSize(QSize(16777215, 27))
        self.label_25.setFont(font9)
        self.label_25.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.verticalLayout_26.addWidget(self.label_25)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 0, 5, -1)
        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_52 = QLabel(self.frame_20)
        self.label_52.setObjectName(u"label_52")
        sizePolicy12.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy12)
        self.label_52.setMinimumSize(QSize(0, 30))
        self.label_52.setMaximumSize(QSize(130, 30))
        self.label_52.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_52.setLineWidth(0)
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_52.setIndent(0)

        self.horizontalLayout_77.addWidget(self.label_52)

        self.probed_diameter_2 = QLineEdit(self.frame_20)
        self.probed_diameter_2.setObjectName(u"probed_diameter_2")
        sizePolicy4.setHeightForWidth(self.probed_diameter_2.sizePolicy().hasHeightForWidth())
        self.probed_diameter_2.setSizePolicy(sizePolicy4)
        self.probed_diameter_2.setMinimumSize(QSize(80, 30))
        self.probed_diameter_2.setMaximumSize(QSize(80, 30))
        self.probed_diameter_2.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.probed_diameter_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.probed_diameter_2.setReadOnly(True)

        self.horizontalLayout_77.addWidget(self.probed_diameter_2)

        self.label_15 = QLabel(self.frame_20)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        self.label_15.setMinimumSize(QSize(60, 30))
        self.label_15.setMaximumSize(QSize(60, 30))
        self.label_15.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_15.setLineWidth(0)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_15.setIndent(0)

        self.horizontalLayout_77.addWidget(self.label_15)

        self.x_probed_width = QLineEdit(self.frame_20)
        self.x_probed_width.setObjectName(u"x_probed_width")
        sizePolicy4.setHeightForWidth(self.x_probed_width.sizePolicy().hasHeightForWidth())
        self.x_probed_width.setSizePolicy(sizePolicy4)
        self.x_probed_width.setMinimumSize(QSize(80, 30))
        self.x_probed_width.setMaximumSize(QSize(80, 30))
        self.x_probed_width.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_probed_width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.x_probed_width.setReadOnly(True)

        self.horizontalLayout_77.addWidget(self.x_probed_width)

        self.label_14 = QLabel(self.frame_20)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)
        self.label_14.setMinimumSize(QSize(95, 30))
        self.label_14.setMaximumSize(QSize(95, 30))
        self.label_14.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_14.setFrameShape(QFrame.NoFrame)
        self.label_14.setLineWidth(0)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_14.setIndent(0)

        self.horizontalLayout_77.addWidget(self.label_14)

        self.x_probed_pos = QLineEdit(self.frame_20)
        self.x_probed_pos.setObjectName(u"x_probed_pos")
        sizePolicy4.setHeightForWidth(self.x_probed_pos.sizePolicy().hasHeightForWidth())
        self.x_probed_pos.setSizePolicy(sizePolicy4)
        self.x_probed_pos.setMinimumSize(QSize(80, 30))
        self.x_probed_pos.setMaximumSize(QSize(80, 30))
        self.x_probed_pos.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_probed_pos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.x_probed_pos.setReadOnly(True)

        self.horizontalLayout_77.addWidget(self.x_probed_pos)


        self.verticalLayout_25.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_30 = QLabel(self.frame_20)
        self.label_30.setObjectName(u"label_30")
        sizePolicy12.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy12)
        self.label_30.setMinimumSize(QSize(0, 30))
        self.label_30.setMaximumSize(QSize(130, 30))
        self.label_30.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_30.setLineWidth(0)
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_30.setIndent(0)

        self.horizontalLayout_5.addWidget(self.label_30)

        self.x_probed_width_2 = QLineEdit(self.frame_20)
        self.x_probed_width_2.setObjectName(u"x_probed_width_2")
        sizePolicy4.setHeightForWidth(self.x_probed_width_2.sizePolicy().hasHeightForWidth())
        self.x_probed_width_2.setSizePolicy(sizePolicy4)
        self.x_probed_width_2.setMinimumSize(QSize(80, 30))
        self.x_probed_width_2.setMaximumSize(QSize(80, 30))
        self.x_probed_width_2.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_probed_width_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.x_probed_width_2.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.x_probed_width_2)

        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setMinimumSize(QSize(60, 30))
        self.label_17.setMaximumSize(QSize(60, 30))
        self.label_17.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_17.setLineWidth(0)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_17.setIndent(0)

        self.horizontalLayout_5.addWidget(self.label_17)

        self.probed_diameter = QLineEdit(self.frame_20)
        self.probed_diameter.setObjectName(u"probed_diameter")
        sizePolicy4.setHeightForWidth(self.probed_diameter.sizePolicy().hasHeightForWidth())
        self.probed_diameter.setSizePolicy(sizePolicy4)
        self.probed_diameter.setMinimumSize(QSize(80, 30))
        self.probed_diameter.setMaximumSize(QSize(80, 30))
        self.probed_diameter.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.probed_diameter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.probed_diameter.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.probed_diameter)

        self.label_16 = QLabel(self.frame_20)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setMinimumSize(QSize(95, 30))
        self.label_16.setMaximumSize(QSize(95, 30))
        self.label_16.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_16.setLineWidth(0)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_16.setIndent(0)

        self.horizontalLayout_5.addWidget(self.label_16)

        self.z_probed_pos = QLineEdit(self.frame_20)
        self.z_probed_pos.setObjectName(u"z_probed_pos")
        sizePolicy4.setHeightForWidth(self.z_probed_pos.sizePolicy().hasHeightForWidth())
        self.z_probed_pos.setSizePolicy(sizePolicy4)
        self.z_probed_pos.setMinimumSize(QSize(80, 30))
        self.z_probed_pos.setMaximumSize(QSize(80, 30))
        self.z_probed_pos.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.z_probed_pos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.z_probed_pos.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.z_probed_pos)


        self.verticalLayout_25.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.ref_coilumn_header = QLabel(self.frame_20)
        self.ref_coilumn_header.setObjectName(u"ref_coilumn_header")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.ref_coilumn_header)

        self.label_50 = QLabel(self.frame_20)
        self.label_50.setObjectName(u"label_50")
        sizePolicy4.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy4)
        self.label_50.setMinimumSize(QSize(60, 30))
        self.label_50.setMaximumSize(QSize(60, 30))
        self.label_50.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_50.setLineWidth(0)
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_50.setIndent(0)

        self.horizontalLayout_76.addWidget(self.label_50)

        self.y_probed_width = QLineEdit(self.frame_20)
        self.y_probed_width.setObjectName(u"y_probed_width")
        sizePolicy4.setHeightForWidth(self.y_probed_width.sizePolicy().hasHeightForWidth())
        self.y_probed_width.setSizePolicy(sizePolicy4)
        self.y_probed_width.setMinimumSize(QSize(80, 30))
        self.y_probed_width.setMaximumSize(QSize(80, 30))
        self.y_probed_width.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.y_probed_width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.y_probed_width.setReadOnly(True)

        self.horizontalLayout_76.addWidget(self.y_probed_width)

        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        self.label_18.setMinimumSize(QSize(95, 30))
        self.label_18.setMaximumSize(QSize(95, 30))
        self.label_18.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_18.setLineWidth(0)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_18.setIndent(0)

        self.horizontalLayout_76.addWidget(self.label_18)

        self.y_probed_pos = QLineEdit(self.frame_20)
        self.y_probed_pos.setObjectName(u"y_probed_pos")
        sizePolicy4.setHeightForWidth(self.y_probed_pos.sizePolicy().hasHeightForWidth())
        self.y_probed_pos.setSizePolicy(sizePolicy4)
        self.y_probed_pos.setMinimumSize(QSize(80, 30))
        self.y_probed_pos.setMaximumSize(QSize(80, 30))
        self.y_probed_pos.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.y_probed_pos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.y_probed_pos.setReadOnly(True)

        self.horizontalLayout_76.addWidget(self.y_probed_pos)


        self.verticalLayout_25.addLayout(self.horizontalLayout_76)


        self.verticalLayout_26.addLayout(self.verticalLayout_25)

        self.mdi_entry_box_2 = MDIEntry(self.frame_20)
        self.mdi_entry_box_2.setObjectName(u"mdi_entry_box_2")
        self.mdi_entry_box_2.setMinimumSize(QSize(0, 35))
        self.mdi_entry_box_2.setMaximumSize(QSize(16777215, 35))
        self.mdi_entry_box_2.setFont(font2)
        self.mdi_entry_box_2.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_26.addWidget(self.mdi_entry_box_2)


        self.horizontalLayout_70.addWidget(self.frame_20)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.frame_23 = QFrame(self.probing_tab)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy7.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy7)
        self.frame_23.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_100.addWidget(self.frame_23)


        self.horizontalLayout_70.addLayout(self.horizontalLayout_100)

        self.probe_tab_widget = QTabWidget(self.probing_tab)
        self.probe_tab_widget.setObjectName(u"probe_tab_widget")
        sizePolicy.setHeightForWidth(self.probe_tab_widget.sizePolicy().hasHeightForWidth())
        self.probe_tab_widget.setSizePolicy(sizePolicy)
        self.probe_tab_widget.setMinimumSize(QSize(1079, 0))
        font10 = QFont()
        font10.setFamilies([u"Probe Basic Bebas Mono"])
        font10.setPointSize(13)
        self.probe_tab_widget.setFont(font10)
        self.probe_tab_widget.setTabPosition(QTabWidget.North)
        self.probe_tab_widget.setTabShape(QTabWidget.Rounded)
        self.probe_tab_widget.setIconSize(QSize(25, 16))
        self.outside_corners_tab = QWidget()
        self.outside_corners_tab.setObjectName(u"outside_corners_tab")
        self.horizontalLayout_63 = QHBoxLayout(self.outside_corners_tab)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(30, -1, -1, -1)
        self.frame_16 = QFrame(self.outside_corners_tab)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy4.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy4)
        self.frame_16.setMinimumSize(QSize(465, 465))
        self.frame_16.setMaximumSize(QSize(465, 465))
        self.frame_16.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.frame_16.setLineWidth(0)
        self.gridLayoutWidget_2 = QWidget(self.frame_16)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(2, 2, 461, 461))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = SubCallButton(self.gridLayoutWidget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy4.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy4)
        self.pushButton_10.setMinimumSize(QSize(140, 140))
        self.pushButton_10.setMaximumSize(QSize(140, 140))
        self.pushButton_10.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/images/front_middle_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon10)
        self.pushButton_10.setIconSize(QSize(130, 130))

        self.gridLayout_2.addWidget(self.pushButton_10, 2, 1, 1, 1)

        self.pushButton_14 = SubCallButton(self.gridLayoutWidget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy4.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy4)
        self.pushButton_14.setMinimumSize(QSize(140, 140))
        self.pushButton_14.setMaximumSize(QSize(140, 140))
        self.pushButton_14.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/images/left_side_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon11)
        self.pushButton_14.setIconSize(QSize(130, 130))

        self.gridLayout_2.addWidget(self.pushButton_14, 1, 0, 1, 1)

        self.pushButton_12 = SubCallButton(self.gridLayoutWidget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy4.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy4)
        self.pushButton_12.setMinimumSize(QSize(140, 140))
        self.pushButton_12.setMaximumSize(QSize(140, 140))
        self.pushButton_12.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/images/front_left_outside_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon12)
        self.pushButton_12.setIconSize(QSize(130, 130))

        self.gridLayout_2.addWidget(self.pushButton_12, 2, 0, 1, 1)

        self.pushButton_13 = SubCallButton(self.gridLayoutWidget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy4.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy4)
        self.pushButton_13.setMinimumSize(QSize(140, 140))
        self.pushButton_13.setMaximumSize(QSize(140, 140))
        self.pushButton_13.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/images/back_right_outside_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon13)
        self.pushButton_13.setIconSize(QSize(130, 130))

        self.gridLayout_2.addWidget(self.pushButton_13, 0, 2, 1, 1)

        self.pushButton_11 = SubCallButton(self.gridLayoutWidget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy4.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy4)
        self.pushButton_11.setMinimumSize(QSize(140, 140))
        self.pushButton_11.setMaximumSize(QSize(140, 140))
        self.pushButton_11.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/images/front_right_outside_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon14)
        self.pushButton_11.setIconSize(QSize(130, 130))

        self.gridLayout_2.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.pushButton_15 = SubCallButton(self.gridLayoutWidget_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy4.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy4)
        self.pushButton_15.setMinimumSize(QSize(140, 140))
        self.pushButton_15.setMaximumSize(QSize(140, 140))
        self.pushButton_15.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/images/z_top.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_15.setIcon(icon15)
        self.pushButton_15.setIconSize(QSize(130, 130))

        self.gridLayout_2.addWidget(self.pushButton_15, 1, 1, 1, 1)

        self.pushButton_17 = SubCallButton(self.gridLayoutWidget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy4.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy4)
        self.pushButton_17.setMinimumSize(QSize(140, 140))
        self.pushButton_17.setMaximumSize(QSize(140, 140))
        self.pushButton_17.setStyleSheet(u"")
        icon16 = QIcon()
        icon16.addFile(u":/images/back_middle_outside_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_17.setIcon(icon16)
        self.pushButton_17.setIconSize(QSize(130, 130))

        self.gridLayout_2.addWidget(self.pushButton_17, 0, 1, 1, 1)

        self.pushButton_18 = SubCallButton(self.gridLayoutWidget_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy4.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy4)
        self.pushButton_18.setMinimumSize(QSize(140, 140))
        self.pushButton_18.setMaximumSize(QSize(140, 140))
        self.pushButton_18.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/images/right_side_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon17.addFile(u":/images/right_side_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_18.setIcon(icon17)
        self.pushButton_18.setIconSize(QSize(130, 130))

        self.gridLayout_2.addWidget(self.pushButton_18, 1, 2, 1, 1)

        self.probe_front_left_top_corner = SubCallButton(self.gridLayoutWidget_2)
        self.probe_front_left_top_corner.setObjectName(u"probe_front_left_top_corner")
        sizePolicy4.setHeightForWidth(self.probe_front_left_top_corner.sizePolicy().hasHeightForWidth())
        self.probe_front_left_top_corner.setSizePolicy(sizePolicy4)
        self.probe_front_left_top_corner.setMinimumSize(QSize(140, 140))
        icon18 = QIcon()
        icon18.addFile(u":/images/back_left_outside_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_front_left_top_corner.setIcon(icon18)
        self.probe_front_left_top_corner.setIconSize(QSize(130, 130))

        self.gridLayout_2.addWidget(self.probe_front_left_top_corner, 0, 0, 1, 1)


        self.horizontalLayout_61.addWidget(self.frame_16)


        self.horizontalLayout_63.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, -1, -1, 170)
        self.label_36 = QLabel(self.outside_corners_tab)
        self.label_36.setObjectName(u"label_36")
        sizePolicy4.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy4)
        self.label_36.setMinimumSize(QSize(441, 311))
        self.label_36.setMaximumSize(QSize(441, 311))
        self.label_36.setStyleSheet(u"image: url(:/images/probe_corner_group_3d_images.png);")
        self.label_36.setScaledContents(True)
        self.label_36.setIndent(0)

        self.horizontalLayout_62.addWidget(self.label_36)


        self.horizontalLayout_63.addLayout(self.horizontalLayout_62)

        self.probe_tab_widget.addTab(self.outside_corners_tab, "")
        self.inside_corners_tab = QWidget()
        self.inside_corners_tab.setObjectName(u"inside_corners_tab")
        self.horizontalLayout_66 = QHBoxLayout(self.inside_corners_tab)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(30, -1, -1, -1)
        self.frame_17 = QFrame(self.inside_corners_tab)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy4.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy4)
        self.frame_17.setMinimumSize(QSize(465, 465))
        self.frame_17.setMaximumSize(QSize(465, 465))
        self.frame_17.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.frame_17)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(7, 7, 451, 451))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_19 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(140, 140))
        self.pushButton_19.setMaximumSize(QSize(140, 140))
        icon19 = QIcon()
        icon19.addFile(u":/images/y_minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_19.setIcon(icon19)
        self.pushButton_19.setIconSize(QSize(125, 125))

        self.gridLayout_3.addWidget(self.pushButton_19, 2, 1, 1, 1)

        self.pushButton_25 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(140, 140))
        self.pushButton_25.setMaximumSize(QSize(140, 140))
        icon20 = QIcon()
        icon20.addFile(u":/images/inside_back_left_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_25.setIcon(icon20)
        self.pushButton_25.setIconSize(QSize(125, 125))

        self.gridLayout_3.addWidget(self.pushButton_25, 0, 0, 1, 1)

        self.pushButton_22 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(140, 140))
        self.pushButton_22.setMaximumSize(QSize(140, 140))
        icon21 = QIcon()
        icon21.addFile(u":/images/inside_back_right_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_22.setIcon(icon21)
        self.pushButton_22.setIconSize(QSize(125, 125))

        self.gridLayout_3.addWidget(self.pushButton_22, 0, 2, 1, 1)

        self.pushButton_21 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(140, 140))
        self.pushButton_21.setMaximumSize(QSize(140, 140))
        icon22 = QIcon()
        icon22.addFile(u":/images/inside_front_left_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_21.setIcon(icon22)
        self.pushButton_21.setIconSize(QSize(125, 125))

        self.gridLayout_3.addWidget(self.pushButton_21, 2, 0, 1, 1)

        self.pushButton_20 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(140, 140))
        self.pushButton_20.setMaximumSize(QSize(140, 140))
        icon23 = QIcon()
        icon23.addFile(u":/images/inside_front_right_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_20.setIcon(icon23)
        self.pushButton_20.setIconSize(QSize(125, 125))

        self.gridLayout_3.addWidget(self.pushButton_20, 2, 2, 1, 1)

        self.pushButton_24 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(140, 140))
        self.pushButton_24.setMaximumSize(QSize(140, 140))
        self.pushButton_24.setIcon(icon15)
        self.pushButton_24.setIconSize(QSize(125, 125))

        self.gridLayout_3.addWidget(self.pushButton_24, 1, 1, 1, 1)

        self.pushButton_23 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(140, 140))
        self.pushButton_23.setMaximumSize(QSize(140, 140))
        icon24 = QIcon()
        icon24.addFile(u":/images/x_minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_23.setIcon(icon24)
        self.pushButton_23.setIconSize(QSize(125, 125))

        self.gridLayout_3.addWidget(self.pushButton_23, 1, 0, 1, 1)

        self.pushButton_26 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(140, 140))
        self.pushButton_26.setMaximumSize(QSize(140, 140))
        icon25 = QIcon()
        icon25.addFile(u":/images/y_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_26.setIcon(icon25)
        self.pushButton_26.setIconSize(QSize(125, 125))

        self.gridLayout_3.addWidget(self.pushButton_26, 0, 1, 1, 1)

        self.pushButton_27 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(140, 140))
        self.pushButton_27.setMaximumSize(QSize(140, 140))
        icon26 = QIcon()
        icon26.addFile(u":/images/x_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_27.setIcon(icon26)
        self.pushButton_27.setIconSize(QSize(125, 125))

        self.gridLayout_3.addWidget(self.pushButton_27, 1, 2, 1, 1)


        self.horizontalLayout_65.addWidget(self.frame_17)


        self.horizontalLayout_66.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, -1, -1, 170)
        self.label_35 = QLabel(self.inside_corners_tab)
        self.label_35.setObjectName(u"label_35")
        sizePolicy4.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy4)
        self.label_35.setMinimumSize(QSize(441, 301))
        self.label_35.setMaximumSize(QSize(441, 301))
        self.label_35.setStyleSheet(u"image: url(:/images/inside_corners_3d_image.png);")
        self.label_35.setScaledContents(True)
        self.label_35.setIndent(0)

        self.horizontalLayout_64.addWidget(self.label_35)


        self.horizontalLayout_66.addLayout(self.horizontalLayout_64)

        self.probe_tab_widget.addTab(self.inside_corners_tab, "")
        self.boss_and_pocket_tab = QWidget()
        self.boss_and_pocket_tab.setObjectName(u"boss_and_pocket_tab")
        self.horizontalLayout_69 = QHBoxLayout(self.boss_and_pocket_tab)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(50, -1, -1, -1)
        self.frame_18 = QFrame(self.boss_and_pocket_tab)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy4.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy4)
        self.frame_18.setMinimumSize(QSize(506, 461))
        self.frame_18.setMaximumSize(QSize(506, 461))
        self.frame_18.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_4 = QWidget(self.frame_18)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(68, 3, 371, 372))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_35 = SubCallButton(self.gridLayoutWidget_4)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(170, 170))
        self.pushButton_35.setMaximumSize(QSize(170, 170))
        self.pushButton_35.setStyleSheet(u"")
        icon27 = QIcon()
        icon27.addFile(u":/images/round_pocket.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_35.setIcon(icon27)
        self.pushButton_35.setIconSize(QSize(145, 145))

        self.gridLayout_4.addWidget(self.pushButton_35, 0, 1, 1, 1)

        self.pushButton_33 = SubCallButton(self.gridLayoutWidget_4)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(170, 170))
        self.pushButton_33.setMaximumSize(QSize(170, 170))
        self.pushButton_33.setStyleSheet(u"")
        icon28 = QIcon()
        icon28.addFile(u":/images/rect_pocket.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_33.setIcon(icon28)
        self.pushButton_33.setIconSize(QSize(145, 145))

        self.gridLayout_4.addWidget(self.pushButton_33, 1, 1, 1, 1)

        self.pushButton_34 = SubCallButton(self.gridLayoutWidget_4)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(170, 170))
        self.pushButton_34.setMaximumSize(QSize(170, 170))
        self.pushButton_34.setStyleSheet(u"")
        icon29 = QIcon()
        icon29.addFile(u":/images/boss_round.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_34.setIcon(icon29)
        self.pushButton_34.setIconSize(QSize(170, 170))

        self.gridLayout_4.addWidget(self.pushButton_34, 0, 0, 1, 1)

        self.pushButton_32 = SubCallButton(self.gridLayoutWidget_4)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(170, 170))
        self.pushButton_32.setMaximumSize(QSize(170, 170))
        self.pushButton_32.setStyleSheet(u"")
        icon30 = QIcon()
        icon30.addFile(u":/images/rect_boss.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_32.setIcon(icon30)
        self.pushButton_32.setIconSize(QSize(170, 170))

        self.gridLayout_4.addWidget(self.pushButton_32, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_18)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(3, 393, 500, 65))
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setMinimumSize(QSize(500, 65))
        self.frame_3.setMaximumSize(QSize(500, 65))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: black;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.horizontalLayout_46 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.step_increment_label_4 = QLabel(self.frame_3)
        self.step_increment_label_4.setObjectName(u"step_increment_label_4")
        self.step_increment_label_4.setMinimumSize(QSize(60, 40))
        self.step_increment_label_4.setMaximumSize(QSize(60, 40))
        self.step_increment_label_4.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(191, 191, 191);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.step_increment_label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.step_increment_label_4)

        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(80, 0))
        self.label_33.setMaximumSize(QSize(30, 16777215))
        self.label_33.setStyleSheet(u"QLabel{\n"
"font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"border: transparent;\n"
"Background:transparent;\n"
"}")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_33.setIndent(0)

        self.horizontalLayout_3.addWidget(self.label_33)

        self.diameter_hint_2 = QLineEdit(self.frame_3)
        self.diameter_hint_2.setObjectName(u"diameter_hint_2")
        self.diameter_hint_2.setMinimumSize(QSize(80, 40))
        self.diameter_hint_2.setMaximumSize(QSize(80, 40))
        self.diameter_hint_2.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.diameter_hint_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.diameter_hint_2)

        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(40, 0))
        self.label_21.setMaximumSize(QSize(40, 16777215))
        self.label_21.setStyleSheet(u"QLabel{\n"
"font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"border: transparent;\n"
"Background:transparent;\n"
"}")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_21.setIndent(0)

        self.horizontalLayout_3.addWidget(self.label_21)

        self.x_hint_2 = QLineEdit(self.frame_3)
        self.x_hint_2.setObjectName(u"x_hint_2")
        self.x_hint_2.setMinimumSize(QSize(80, 40))
        self.x_hint_2.setMaximumSize(QSize(80, 40))
        self.x_hint_2.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_hint_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.x_hint_2)

        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(40, 0))
        self.label_34.setMaximumSize(QSize(40, 16777215))
        self.label_34.setStyleSheet(u"QLabel{\n"
"font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"border: transparent;\n"
"Background:transparent;\n"
"}")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_34.setIndent(0)

        self.horizontalLayout_3.addWidget(self.label_34)

        self.y_hint_2 = QLineEdit(self.frame_3)
        self.y_hint_2.setObjectName(u"y_hint_2")
        self.y_hint_2.setMinimumSize(QSize(80, 40))
        self.y_hint_2.setMaximumSize(QSize(80, 40))
        self.y_hint_2.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.y_hint_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.y_hint_2)


        self.horizontalLayout_46.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_67.addWidget(self.frame_18)


        self.horizontalLayout_69.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, -1, -1, 170)
        self.label_31 = QLabel(self.boss_and_pocket_tab)
        self.label_31.setObjectName(u"label_31")
        sizePolicy4.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy4)
        self.label_31.setMinimumSize(QSize(441, 281))
        self.label_31.setMaximumSize(QSize(441, 281))
        self.label_31.setStyleSheet(u"image: url(:/images/boss_pocket_3d_image.png);")
        self.label_31.setScaledContents(True)
        self.label_31.setIndent(0)

        self.horizontalLayout_68.addWidget(self.label_31)


        self.horizontalLayout_69.addLayout(self.horizontalLayout_68)

        self.probe_tab_widget.addTab(self.boss_and_pocket_tab, "")
        self.valley_and_ridge_tab = QWidget()
        self.valley_and_ridge_tab.setObjectName(u"valley_and_ridge_tab")
        self.horizontalLayout_74 = QHBoxLayout(self.valley_and_ridge_tab)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(70, -1, -1, -1)
        self.frame_19 = QFrame(self.valley_and_ridge_tab)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy4.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy4)
        self.frame_19.setMinimumSize(QSize(405, 465))
        self.frame_19.setMaximumSize(QSize(405, 465))
        self.frame_19.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_19)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(19, 3, 371, 372))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_36 = SubCallButton(self.gridLayoutWidget_5)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(170, 170))
        self.pushButton_36.setMaximumSize(QSize(170, 170))
        self.pushButton_36.setStyleSheet(u"")
        icon31 = QIcon()
        icon31.addFile(u":/images/probe_y_valley.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_36.setIcon(icon31)
        self.pushButton_36.setIconSize(QSize(150, 150))

        self.gridLayout_5.addWidget(self.pushButton_36, 0, 1, 1, 1)

        self.pushButton_39 = SubCallButton(self.gridLayoutWidget_5)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(170, 170))
        self.pushButton_39.setMaximumSize(QSize(170, 170))
        self.pushButton_39.setStyleSheet(u"")
        icon32 = QIcon()
        icon32.addFile(u":/images/probe_y_ridge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_39.setIcon(icon32)
        self.pushButton_39.setIconSize(QSize(150, 150))

        self.gridLayout_5.addWidget(self.pushButton_39, 1, 1, 1, 1)

        self.pushButton_37 = SubCallButton(self.gridLayoutWidget_5)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(170, 170))
        self.pushButton_37.setMaximumSize(QSize(170, 170))
        self.pushButton_37.setStyleSheet(u"")
        icon33 = QIcon()
        icon33.addFile(u":/images/probe_x_valley.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_37.setIcon(icon33)
        self.pushButton_37.setIconSize(QSize(150, 150))

        self.gridLayout_5.addWidget(self.pushButton_37, 0, 0, 1, 1)

        self.pushButton_38 = SubCallButton(self.gridLayoutWidget_5)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMinimumSize(QSize(170, 170))
        self.pushButton_38.setMaximumSize(QSize(170, 170))
        self.pushButton_38.setStyleSheet(u"")
        icon34 = QIcon()
        icon34.addFile(u":/images/probe_x_ridge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_38.setIcon(icon34)
        self.pushButton_38.setIconSize(QSize(150, 150))

        self.gridLayout_5.addWidget(self.pushButton_38, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_19)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(3, 393, 400, 70))
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setMinimumSize(QSize(400, 70))
        self.frame_5.setMaximumSize(QSize(400, 70))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: black;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.horizontalLayout_71 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.step_increment_label_5 = QLabel(self.frame_5)
        self.step_increment_label_5.setObjectName(u"step_increment_label_5")
        self.step_increment_label_5.setMinimumSize(QSize(115, 40))
        self.step_increment_label_5.setMaximumSize(QSize(115, 40))
        self.step_increment_label_5.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(191, 191, 191);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.step_increment_label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.step_increment_label_5)

        self.label_39 = QLabel(self.frame_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(50, 0))
        self.label_39.setMaximumSize(QSize(50, 16777215))
        self.label_39.setStyleSheet(u"QLabel{\n"
"font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"border: transparent;\n"
"Background:transparent;\n"
"}")
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_39.setIndent(0)

        self.horizontalLayout_4.addWidget(self.label_39)

        self.x_hint_3 = QLineEdit(self.frame_5)
        self.x_hint_3.setObjectName(u"x_hint_3")
        self.x_hint_3.setMinimumSize(QSize(80, 40))
        self.x_hint_3.setMaximumSize(QSize(80, 40))
        self.x_hint_3.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.x_hint_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.x_hint_3)

        self.label_40 = QLabel(self.frame_5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(50, 0))
        self.label_40.setMaximumSize(QSize(50, 16777215))
        self.label_40.setStyleSheet(u"QLabel{\n"
"font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"border: transparent;\n"
"Background:transparent;\n"
"}")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_40.setIndent(0)

        self.horizontalLayout_4.addWidget(self.label_40)

        self.y_hint_3 = QLineEdit(self.frame_5)
        self.y_hint_3.setObjectName(u"y_hint_3")
        self.y_hint_3.setMinimumSize(QSize(80, 40))
        self.y_hint_3.setMaximumSize(QSize(80, 40))
        self.y_hint_3.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.y_hint_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.y_hint_3)


        self.horizontalLayout_71.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_72.addWidget(self.frame_19)


        self.horizontalLayout_74.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, -1, -1, 170)
        self.label_37 = QLabel(self.valley_and_ridge_tab)
        self.label_37.setObjectName(u"label_37")
        sizePolicy4.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy4)
        self.label_37.setMinimumSize(QSize(411, 271))
        self.label_37.setMaximumSize(QSize(411, 271))
        self.label_37.setStyleSheet(u"image: url(:/images/ridge_and_valley_group.png);")
        self.label_37.setScaledContents(True)
        self.label_37.setIndent(0)

        self.horizontalLayout_73.addWidget(self.label_37)


        self.horizontalLayout_74.addLayout(self.horizontalLayout_73)

        self.probe_tab_widget.addTab(self.valley_and_ridge_tab, "")
        self.rotary_axis_tab = QWidget()
        self.rotary_axis_tab.setObjectName(u"rotary_axis_tab")
        self.probe_tab_widget.addTab(self.rotary_axis_tab, "")
        self.multi_axis_tab = QWidget()
        self.multi_axis_tab.setObjectName(u"multi_axis_tab")
        self.probe_tab_widget.addTab(self.multi_axis_tab, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.probe_tab_widget.addTab(self.tab_7, "")
        self.probe_help_tab = QWidget()
        self.probe_help_tab.setObjectName(u"probe_help_tab")
        self.horizontalLayout_52 = QHBoxLayout(self.probe_help_tab)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 15)
        self.tabWidget_2 = QTabWidget(self.probe_help_tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy15)
        self.tabWidget_2.setFont(font10)
        self.tabWidget_2.setTabPosition(QTabWidget.South)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_60 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label = QLabel(self.tab_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(541, 451))
        self.label.setMaximumSize(QSize(541, 451))
        self.label.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"	image: url(:/images/step_off_width.png);\n"
"}")
        self.label.setScaledContents(True)
        self.label.setIndent(0)

        self.horizontalLayout_59.addWidget(self.label)


        self.horizontalLayout_60.addLayout(self.horizontalLayout_59)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_58 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_2 = QLabel(self.tab_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(411, 331))
        self.label_2.setMaximumSize(QSize(411, 331))
        self.label_2.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"	image: url(:/images/extra_probe_depth.png);\n"
"}")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(0)

        self.horizontalLayout_57.addWidget(self.label_2)


        self.horizontalLayout_58.addLayout(self.horizontalLayout_57)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.horizontalLayout_56 = QHBoxLayout(self.tab_8)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_3 = QLabel(self.tab_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(785, 407))
        self.label_3.setMaximumSize(QSize(785, 407))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"	image: url(:/images/max_distance.png);\n"
"}")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setLineWidth(0)
        self.label_3.setMidLineWidth(0)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setIndent(0)

        self.horizontalLayout_55.addWidget(self.label_3)


        self.horizontalLayout_56.addLayout(self.horizontalLayout_55)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayout_54 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_4 = QLabel(self.tab_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(791, 391))
        self.label_4.setMaximumSize(QSize(791, 391))
        self.label_4.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"	image: url(:/images/clearance.png);\n"
"}")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setIndent(0)

        self.horizontalLayout_53.addWidget(self.label_4)


        self.horizontalLayout_54.addLayout(self.horizontalLayout_53)

        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.tabWidget_2.addTab(self.tab_12, "")

        self.verticalLayout_3.addWidget(self.tabWidget_2)


        self.horizontalLayout_52.addLayout(self.verticalLayout_3)

        self.probe_tab_widget.addTab(self.probe_help_tab, "")

        self.horizontalLayout_70.addWidget(self.probe_tab_widget)

        self.tabWidget.addTab(self.probing_tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.frame = QFrame(self.tab_4)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 250, 1061, 285))
        self.frame.setStyleSheet(u"QFrame{ \n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(136, 138, 133);\n"
"    border-radius: 4px;\n"
"    background: rgb(46, 52, 54);    \n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_40 = QPushButton(self.frame)
        self.pushButton_40.setObjectName(u"pushButton_40")
        sizePolicy4.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy4)
        self.pushButton_40.setMinimumSize(QSize(45, 45))
        self.pushButton_40.setMaximumSize(QSize(45, 45))
        self.pushButton_40.setFont(font9)
        self.pushButton_40.setFocusPolicy(Qt.NoFocus)
        self.pushButton_40.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_40)

        self.pushButton_16 = QPushButton(self.frame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy4.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy4)
        self.pushButton_16.setMinimumSize(QSize(45, 45))
        self.pushButton_16.setMaximumSize(QSize(45, 45))
        self.pushButton_16.setFont(font9)
        self.pushButton_16.setFocusPolicy(Qt.NoFocus)
        self.pushButton_16.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_16)

        self.pushButton_28 = QPushButton(self.frame)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy4.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy4)
        self.pushButton_28.setMinimumSize(QSize(45, 45))
        self.pushButton_28.setMaximumSize(QSize(45, 45))
        self.pushButton_28.setFont(font9)
        self.pushButton_28.setFocusPolicy(Qt.NoFocus)
        self.pushButton_28.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_28)

        self.pushButton_29 = QPushButton(self.frame)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy4.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy4)
        self.pushButton_29.setMinimumSize(QSize(45, 45))
        self.pushButton_29.setMaximumSize(QSize(45, 45))
        self.pushButton_29.setFont(font9)
        self.pushButton_29.setFocusPolicy(Qt.NoFocus)
        self.pushButton_29.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_29)

        self.pushButton_30 = QPushButton(self.frame)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy4.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy4)
        self.pushButton_30.setMinimumSize(QSize(45, 45))
        self.pushButton_30.setMaximumSize(QSize(45, 45))
        self.pushButton_30.setFont(font9)
        self.pushButton_30.setFocusPolicy(Qt.NoFocus)
        self.pushButton_30.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_30)

        self.pushButton_31 = QPushButton(self.frame)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy4.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy4)
        self.pushButton_31.setMinimumSize(QSize(45, 45))
        self.pushButton_31.setMaximumSize(QSize(45, 45))
        self.pushButton_31.setFont(font9)
        self.pushButton_31.setFocusPolicy(Qt.NoFocus)
        self.pushButton_31.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_31)

        self.pushButton_41 = QPushButton(self.frame)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy4.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy4)
        self.pushButton_41.setMinimumSize(QSize(45, 45))
        self.pushButton_41.setMaximumSize(QSize(45, 45))
        self.pushButton_41.setFont(font9)
        self.pushButton_41.setFocusPolicy(Qt.NoFocus)
        self.pushButton_41.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_41)

        self.pushButton_42 = QPushButton(self.frame)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy4.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy4)
        self.pushButton_42.setMinimumSize(QSize(45, 45))
        self.pushButton_42.setMaximumSize(QSize(45, 45))
        self.pushButton_42.setFont(font9)
        self.pushButton_42.setFocusPolicy(Qt.NoFocus)
        self.pushButton_42.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_42)

        self.pushButton_43 = QPushButton(self.frame)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy4.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy4)
        self.pushButton_43.setMinimumSize(QSize(45, 45))
        self.pushButton_43.setMaximumSize(QSize(45, 45))
        self.pushButton_43.setFont(font9)
        self.pushButton_43.setFocusPolicy(Qt.NoFocus)
        self.pushButton_43.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_43)

        self.pushButton_44 = QPushButton(self.frame)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy4.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy4)
        self.pushButton_44.setMinimumSize(QSize(45, 45))
        self.pushButton_44.setMaximumSize(QSize(45, 45))
        self.pushButton_44.setFont(font9)
        self.pushButton_44.setFocusPolicy(Qt.NoFocus)
        self.pushButton_44.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_44)

        self.pushButton_45 = QPushButton(self.frame)
        self.pushButton_45.setObjectName(u"pushButton_45")
        sizePolicy4.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy4)
        self.pushButton_45.setMinimumSize(QSize(45, 45))
        self.pushButton_45.setMaximumSize(QSize(45, 45))
        self.pushButton_45.setFont(font9)
        self.pushButton_45.setFocusPolicy(Qt.NoFocus)
        self.pushButton_45.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_45)

        self.pushButton_46 = QPushButton(self.frame)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy4.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy4)
        self.pushButton_46.setMinimumSize(QSize(45, 45))
        self.pushButton_46.setMaximumSize(QSize(45, 45))
        self.pushButton_46.setFont(font9)
        self.pushButton_46.setFocusPolicy(Qt.NoFocus)
        self.pushButton_46.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_46)

        self.pushButton_47 = QPushButton(self.frame)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy4.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy4)
        self.pushButton_47.setMinimumSize(QSize(45, 45))
        self.pushButton_47.setMaximumSize(QSize(45, 45))
        self.pushButton_47.setFont(font9)
        self.pushButton_47.setFocusPolicy(Qt.NoFocus)
        self.pushButton_47.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_47)

        self.pushButton_48 = QPushButton(self.frame)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy4.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy4)
        self.pushButton_48.setMinimumSize(QSize(101, 45))
        self.pushButton_48.setMaximumSize(QSize(101, 45))
        self.pushButton_48.setFont(font9)
        self.pushButton_48.setFocusPolicy(Qt.NoFocus)
        self.pushButton_48.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_48)

        self.pushButton_85 = QPushButton(self.frame)
        self.pushButton_85.setObjectName(u"pushButton_85")
        sizePolicy4.setHeightForWidth(self.pushButton_85.sizePolicy().hasHeightForWidth())
        self.pushButton_85.setSizePolicy(sizePolicy4)
        self.pushButton_85.setMinimumSize(QSize(45, 45))
        self.pushButton_85.setMaximumSize(QSize(45, 45))
        self.pushButton_85.setFont(font3)
        self.pushButton_85.setFocusPolicy(Qt.NoFocus)
        self.pushButton_85.setStyleSheet(u"QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 12pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_85)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)
        self.pushButton.setMinimumSize(QSize(45, 45))
        self.pushButton.setMaximumSize(QSize(45, 45))
        font11 = QFont()
        font11.setFamilies([u"Probe Basic Bebas Mono"])
        font11.setPointSize(18)
        font11.setBold(False)
        font11.setItalic(False)
        self.pushButton.setFont(font11)
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy4)
        self.pushButton_2.setMinimumSize(QSize(45, 45))
        self.pushButton_2.setMaximumSize(QSize(45, 45))
        self.pushButton_2.setFont(font11)
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_2.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        self.pushButton_3.setMinimumSize(QSize(45, 45))
        self.pushButton_3.setMaximumSize(QSize(45, 45))
        self.pushButton_3.setFont(font11)
        self.pushButton_3.setFocusPolicy(Qt.NoFocus)
        self.pushButton_3.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_49 = QPushButton(self.frame)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy4.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy4)
        self.pushButton_49.setMinimumSize(QSize(45, 45))
        self.pushButton_49.setMaximumSize(QSize(45, 45))
        font12 = QFont()
        font12.setFamilies([u"Probe Basic Bebas Mono"])
        font12.setPointSize(20)
        font12.setBold(False)
        font12.setItalic(False)
        self.pushButton_49.setFont(font12)
        self.pushButton_49.setFocusPolicy(Qt.NoFocus)
        self.pushButton_49.setStyleSheet(u"QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 20pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_49)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_50 = QPushButton(self.frame)
        self.pushButton_50.setObjectName(u"pushButton_50")
        sizePolicy4.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy4)
        self.pushButton_50.setMinimumSize(QSize(71, 45))
        self.pushButton_50.setMaximumSize(QSize(71, 45))
        self.pushButton_50.setFont(font9)
        self.pushButton_50.setFocusPolicy(Qt.NoFocus)
        self.pushButton_50.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_50)

        self.pushButton_51 = QPushButton(self.frame)
        self.pushButton_51.setObjectName(u"pushButton_51")
        sizePolicy4.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy4)
        self.pushButton_51.setMinimumSize(QSize(45, 45))
        self.pushButton_51.setMaximumSize(QSize(45, 45))
        self.pushButton_51.setFont(font11)
        self.pushButton_51.setFocusPolicy(Qt.NoFocus)
        self.pushButton_51.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_51)

        self.pushButton_52 = QPushButton(self.frame)
        self.pushButton_52.setObjectName(u"pushButton_52")
        sizePolicy4.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy4)
        self.pushButton_52.setMinimumSize(QSize(45, 45))
        self.pushButton_52.setMaximumSize(QSize(45, 45))
        self.pushButton_52.setFont(font11)
        self.pushButton_52.setFocusPolicy(Qt.NoFocus)
        self.pushButton_52.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_52)

        self.pushButton_53 = QPushButton(self.frame)
        self.pushButton_53.setObjectName(u"pushButton_53")
        sizePolicy4.setHeightForWidth(self.pushButton_53.sizePolicy().hasHeightForWidth())
        self.pushButton_53.setSizePolicy(sizePolicy4)
        self.pushButton_53.setMinimumSize(QSize(45, 45))
        self.pushButton_53.setMaximumSize(QSize(45, 45))
        self.pushButton_53.setFont(font11)
        self.pushButton_53.setFocusPolicy(Qt.NoFocus)
        self.pushButton_53.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_53)

        self.pushButton_54 = QPushButton(self.frame)
        self.pushButton_54.setObjectName(u"pushButton_54")
        sizePolicy4.setHeightForWidth(self.pushButton_54.sizePolicy().hasHeightForWidth())
        self.pushButton_54.setSizePolicy(sizePolicy4)
        self.pushButton_54.setMinimumSize(QSize(45, 45))
        self.pushButton_54.setMaximumSize(QSize(45, 45))
        self.pushButton_54.setFont(font11)
        self.pushButton_54.setFocusPolicy(Qt.NoFocus)
        self.pushButton_54.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_54)

        self.pushButton_55 = QPushButton(self.frame)
        self.pushButton_55.setObjectName(u"pushButton_55")
        sizePolicy4.setHeightForWidth(self.pushButton_55.sizePolicy().hasHeightForWidth())
        self.pushButton_55.setSizePolicy(sizePolicy4)
        self.pushButton_55.setMinimumSize(QSize(45, 45))
        self.pushButton_55.setMaximumSize(QSize(45, 45))
        self.pushButton_55.setFont(font11)
        self.pushButton_55.setFocusPolicy(Qt.NoFocus)
        self.pushButton_55.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_55)

        self.pushButton_56 = QPushButton(self.frame)
        self.pushButton_56.setObjectName(u"pushButton_56")
        sizePolicy4.setHeightForWidth(self.pushButton_56.sizePolicy().hasHeightForWidth())
        self.pushButton_56.setSizePolicy(sizePolicy4)
        self.pushButton_56.setMinimumSize(QSize(45, 45))
        self.pushButton_56.setMaximumSize(QSize(45, 45))
        self.pushButton_56.setFont(font11)
        self.pushButton_56.setFocusPolicy(Qt.NoFocus)
        self.pushButton_56.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_56)

        self.pushButton_57 = QPushButton(self.frame)
        self.pushButton_57.setObjectName(u"pushButton_57")
        sizePolicy4.setHeightForWidth(self.pushButton_57.sizePolicy().hasHeightForWidth())
        self.pushButton_57.setSizePolicy(sizePolicy4)
        self.pushButton_57.setMinimumSize(QSize(45, 45))
        self.pushButton_57.setMaximumSize(QSize(45, 45))
        self.pushButton_57.setFont(font11)
        self.pushButton_57.setFocusPolicy(Qt.NoFocus)
        self.pushButton_57.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_57)

        self.pushButton_58 = QPushButton(self.frame)
        self.pushButton_58.setObjectName(u"pushButton_58")
        sizePolicy4.setHeightForWidth(self.pushButton_58.sizePolicy().hasHeightForWidth())
        self.pushButton_58.setSizePolicy(sizePolicy4)
        self.pushButton_58.setMinimumSize(QSize(45, 45))
        self.pushButton_58.setMaximumSize(QSize(45, 45))
        self.pushButton_58.setFont(font11)
        self.pushButton_58.setFocusPolicy(Qt.NoFocus)
        self.pushButton_58.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_58)

        self.pushButton_59 = QPushButton(self.frame)
        self.pushButton_59.setObjectName(u"pushButton_59")
        sizePolicy4.setHeightForWidth(self.pushButton_59.sizePolicy().hasHeightForWidth())
        self.pushButton_59.setSizePolicy(sizePolicy4)
        self.pushButton_59.setMinimumSize(QSize(45, 45))
        self.pushButton_59.setMaximumSize(QSize(45, 45))
        self.pushButton_59.setFont(font11)
        self.pushButton_59.setFocusPolicy(Qt.NoFocus)
        self.pushButton_59.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_59)

        self.pushButton_60 = QPushButton(self.frame)
        self.pushButton_60.setObjectName(u"pushButton_60")
        sizePolicy4.setHeightForWidth(self.pushButton_60.sizePolicy().hasHeightForWidth())
        self.pushButton_60.setSizePolicy(sizePolicy4)
        self.pushButton_60.setMinimumSize(QSize(45, 45))
        self.pushButton_60.setMaximumSize(QSize(45, 45))
        self.pushButton_60.setFont(font11)
        self.pushButton_60.setFocusPolicy(Qt.NoFocus)
        self.pushButton_60.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_60)

        self.pushButton_61 = QPushButton(self.frame)
        self.pushButton_61.setObjectName(u"pushButton_61")
        sizePolicy4.setHeightForWidth(self.pushButton_61.sizePolicy().hasHeightForWidth())
        self.pushButton_61.setSizePolicy(sizePolicy4)
        self.pushButton_61.setMinimumSize(QSize(45, 45))
        self.pushButton_61.setMaximumSize(QSize(45, 45))
        self.pushButton_61.setFont(font9)
        self.pushButton_61.setFocusPolicy(Qt.NoFocus)
        self.pushButton_61.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_61)

        self.pushButton_62 = QPushButton(self.frame)
        self.pushButton_62.setObjectName(u"pushButton_62")
        sizePolicy4.setHeightForWidth(self.pushButton_62.sizePolicy().hasHeightForWidth())
        self.pushButton_62.setSizePolicy(sizePolicy4)
        self.pushButton_62.setMinimumSize(QSize(45, 45))
        self.pushButton_62.setMaximumSize(QSize(45, 45))
        self.pushButton_62.setFont(font9)
        self.pushButton_62.setFocusPolicy(Qt.NoFocus)
        self.pushButton_62.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_62)

        self.pushButton_63 = QPushButton(self.frame)
        self.pushButton_63.setObjectName(u"pushButton_63")
        sizePolicy4.setHeightForWidth(self.pushButton_63.sizePolicy().hasHeightForWidth())
        self.pushButton_63.setSizePolicy(sizePolicy4)
        self.pushButton_63.setMinimumSize(QSize(75, 45))
        self.pushButton_63.setMaximumSize(QSize(70, 45))
        self.pushButton_63.setFont(font9)
        self.pushButton_63.setFocusPolicy(Qt.NoFocus)
        self.pushButton_63.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_63)

        self.pushButton_79 = QPushButton(self.frame)
        self.pushButton_79.setObjectName(u"pushButton_79")
        sizePolicy4.setHeightForWidth(self.pushButton_79.sizePolicy().hasHeightForWidth())
        self.pushButton_79.setSizePolicy(sizePolicy4)
        self.pushButton_79.setMinimumSize(QSize(45, 45))
        self.pushButton_79.setMaximumSize(QSize(45, 45))
        self.pushButton_79.setFont(font3)
        self.pushButton_79.setFocusPolicy(Qt.NoFocus)
        self.pushButton_79.setStyleSheet(u"QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 12pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_79)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy4.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy4)
        self.pushButton_4.setMinimumSize(QSize(45, 45))
        self.pushButton_4.setMaximumSize(QSize(45, 45))
        self.pushButton_4.setFont(font11)
        self.pushButton_4.setFocusPolicy(Qt.NoFocus)
        self.pushButton_4.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy4.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy4)
        self.pushButton_5.setMinimumSize(QSize(45, 45))
        self.pushButton_5.setMaximumSize(QSize(45, 45))
        self.pushButton_5.setFont(font11)
        self.pushButton_5.setFocusPolicy(Qt.NoFocus)
        self.pushButton_5.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)
        self.pushButton_6.setMinimumSize(QSize(45, 45))
        self.pushButton_6.setMaximumSize(QSize(45, 45))
        self.pushButton_6.setFont(font11)
        self.pushButton_6.setFocusPolicy(Qt.NoFocus)
        self.pushButton_6.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_6)

        self.pushButton_64 = QPushButton(self.frame)
        self.pushButton_64.setObjectName(u"pushButton_64")
        sizePolicy4.setHeightForWidth(self.pushButton_64.sizePolicy().hasHeightForWidth())
        self.pushButton_64.setSizePolicy(sizePolicy4)
        self.pushButton_64.setMinimumSize(QSize(45, 45))
        self.pushButton_64.setMaximumSize(QSize(45, 45))
        self.pushButton_64.setFont(font12)
        self.pushButton_64.setFocusPolicy(Qt.NoFocus)
        self.pushButton_64.setStyleSheet(u"QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 20pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_64)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_65 = QPushButton(self.frame)
        self.pushButton_65.setObjectName(u"pushButton_65")
        sizePolicy4.setHeightForWidth(self.pushButton_65.sizePolicy().hasHeightForWidth())
        self.pushButton_65.setSizePolicy(sizePolicy4)
        self.pushButton_65.setMinimumSize(QSize(87, 45))
        self.pushButton_65.setMaximumSize(QSize(87, 45))
        self.pushButton_65.setFont(font9)
        self.pushButton_65.setFocusPolicy(Qt.NoFocus)
        self.pushButton_65.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_65)

        self.pushButton_66 = QPushButton(self.frame)
        self.pushButton_66.setObjectName(u"pushButton_66")
        sizePolicy4.setHeightForWidth(self.pushButton_66.sizePolicy().hasHeightForWidth())
        self.pushButton_66.setSizePolicy(sizePolicy4)
        self.pushButton_66.setMinimumSize(QSize(45, 45))
        self.pushButton_66.setMaximumSize(QSize(45, 45))
        self.pushButton_66.setFont(font11)
        self.pushButton_66.setFocusPolicy(Qt.NoFocus)
        self.pushButton_66.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_66)

        self.pushButton_67 = QPushButton(self.frame)
        self.pushButton_67.setObjectName(u"pushButton_67")
        sizePolicy4.setHeightForWidth(self.pushButton_67.sizePolicy().hasHeightForWidth())
        self.pushButton_67.setSizePolicy(sizePolicy4)
        self.pushButton_67.setMinimumSize(QSize(45, 45))
        self.pushButton_67.setMaximumSize(QSize(45, 45))
        self.pushButton_67.setFont(font11)
        self.pushButton_67.setFocusPolicy(Qt.NoFocus)
        self.pushButton_67.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_67)

        self.pushButton_68 = QPushButton(self.frame)
        self.pushButton_68.setObjectName(u"pushButton_68")
        sizePolicy4.setHeightForWidth(self.pushButton_68.sizePolicy().hasHeightForWidth())
        self.pushButton_68.setSizePolicy(sizePolicy4)
        self.pushButton_68.setMinimumSize(QSize(45, 45))
        self.pushButton_68.setMaximumSize(QSize(45, 45))
        self.pushButton_68.setFont(font11)
        self.pushButton_68.setFocusPolicy(Qt.NoFocus)
        self.pushButton_68.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_68)

        self.pushButton_69 = QPushButton(self.frame)
        self.pushButton_69.setObjectName(u"pushButton_69")
        sizePolicy4.setHeightForWidth(self.pushButton_69.sizePolicy().hasHeightForWidth())
        self.pushButton_69.setSizePolicy(sizePolicy4)
        self.pushButton_69.setMinimumSize(QSize(45, 45))
        self.pushButton_69.setMaximumSize(QSize(45, 45))
        self.pushButton_69.setFont(font11)
        self.pushButton_69.setFocusPolicy(Qt.NoFocus)
        self.pushButton_69.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_69)

        self.pushButton_70 = QPushButton(self.frame)
        self.pushButton_70.setObjectName(u"pushButton_70")
        sizePolicy4.setHeightForWidth(self.pushButton_70.sizePolicy().hasHeightForWidth())
        self.pushButton_70.setSizePolicy(sizePolicy4)
        self.pushButton_70.setMinimumSize(QSize(45, 45))
        self.pushButton_70.setMaximumSize(QSize(45, 45))
        self.pushButton_70.setFont(font11)
        self.pushButton_70.setFocusPolicy(Qt.NoFocus)
        self.pushButton_70.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_70)

        self.pushButton_71 = QPushButton(self.frame)
        self.pushButton_71.setObjectName(u"pushButton_71")
        sizePolicy4.setHeightForWidth(self.pushButton_71.sizePolicy().hasHeightForWidth())
        self.pushButton_71.setSizePolicy(sizePolicy4)
        self.pushButton_71.setMinimumSize(QSize(45, 45))
        self.pushButton_71.setMaximumSize(QSize(45, 45))
        self.pushButton_71.setFont(font11)
        self.pushButton_71.setFocusPolicy(Qt.NoFocus)
        self.pushButton_71.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_71)

        self.pushButton_72 = QPushButton(self.frame)
        self.pushButton_72.setObjectName(u"pushButton_72")
        sizePolicy4.setHeightForWidth(self.pushButton_72.sizePolicy().hasHeightForWidth())
        self.pushButton_72.setSizePolicy(sizePolicy4)
        self.pushButton_72.setMinimumSize(QSize(45, 45))
        self.pushButton_72.setMaximumSize(QSize(45, 45))
        self.pushButton_72.setFont(font11)
        self.pushButton_72.setFocusPolicy(Qt.NoFocus)
        self.pushButton_72.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_72)

        self.pushButton_73 = QPushButton(self.frame)
        self.pushButton_73.setObjectName(u"pushButton_73")
        sizePolicy4.setHeightForWidth(self.pushButton_73.sizePolicy().hasHeightForWidth())
        self.pushButton_73.setSizePolicy(sizePolicy4)
        self.pushButton_73.setMinimumSize(QSize(45, 45))
        self.pushButton_73.setMaximumSize(QSize(45, 45))
        self.pushButton_73.setFont(font11)
        self.pushButton_73.setFocusPolicy(Qt.NoFocus)
        self.pushButton_73.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_73)

        self.pushButton_74 = QPushButton(self.frame)
        self.pushButton_74.setObjectName(u"pushButton_74")
        sizePolicy4.setHeightForWidth(self.pushButton_74.sizePolicy().hasHeightForWidth())
        self.pushButton_74.setSizePolicy(sizePolicy4)
        self.pushButton_74.setMinimumSize(QSize(45, 45))
        self.pushButton_74.setMaximumSize(QSize(45, 45))
        self.pushButton_74.setFont(font11)
        self.pushButton_74.setFocusPolicy(Qt.NoFocus)
        self.pushButton_74.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_74)

        self.pushButton_75 = QPushButton(self.frame)
        self.pushButton_75.setObjectName(u"pushButton_75")
        sizePolicy4.setHeightForWidth(self.pushButton_75.sizePolicy().hasHeightForWidth())
        self.pushButton_75.setSizePolicy(sizePolicy4)
        self.pushButton_75.setMinimumSize(QSize(45, 45))
        self.pushButton_75.setMaximumSize(QSize(45, 45))
        self.pushButton_75.setFont(font9)
        self.pushButton_75.setFocusPolicy(Qt.NoFocus)
        self.pushButton_75.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_75)

        self.pushButton_76 = QPushButton(self.frame)
        self.pushButton_76.setObjectName(u"pushButton_76")
        sizePolicy4.setHeightForWidth(self.pushButton_76.sizePolicy().hasHeightForWidth())
        self.pushButton_76.setSizePolicy(sizePolicy4)
        self.pushButton_76.setMinimumSize(QSize(45, 45))
        self.pushButton_76.setMaximumSize(QSize(45, 45))
        self.pushButton_76.setFont(font9)
        self.pushButton_76.setFocusPolicy(Qt.NoFocus)
        self.pushButton_76.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_76)

        self.pushButton_77 = QPushButton(self.frame)
        self.pushButton_77.setObjectName(u"pushButton_77")
        sizePolicy4.setHeightForWidth(self.pushButton_77.sizePolicy().hasHeightForWidth())
        self.pushButton_77.setSizePolicy(sizePolicy4)
        self.pushButton_77.setMinimumSize(QSize(110, 45))
        self.pushButton_77.setMaximumSize(QSize(110, 45))
        self.pushButton_77.setFont(font9)
        self.pushButton_77.setFocusPolicy(Qt.NoFocus)
        self.pushButton_77.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_77)

        self.pushButton_83 = QPushButton(self.frame)
        self.pushButton_83.setObjectName(u"pushButton_83")
        sizePolicy4.setHeightForWidth(self.pushButton_83.sizePolicy().hasHeightForWidth())
        self.pushButton_83.setSizePolicy(sizePolicy4)
        self.pushButton_83.setMinimumSize(QSize(45, 45))
        self.pushButton_83.setMaximumSize(QSize(45, 45))
        self.pushButton_83.setFont(font3)
        self.pushButton_83.setFocusPolicy(Qt.NoFocus)
        self.pushButton_83.setStyleSheet(u"QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 12pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_83)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy4.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy4)
        self.pushButton_7.setMinimumSize(QSize(45, 45))
        self.pushButton_7.setMaximumSize(QSize(45, 45))
        self.pushButton_7.setFont(font11)
        self.pushButton_7.setFocusPolicy(Qt.NoFocus)
        self.pushButton_7.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy4.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy4)
        self.pushButton_8.setMinimumSize(QSize(45, 45))
        self.pushButton_8.setMaximumSize(QSize(45, 45))
        self.pushButton_8.setFont(font11)
        self.pushButton_8.setFocusPolicy(Qt.NoFocus)
        self.pushButton_8.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy4.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy4)
        self.pushButton_9.setMinimumSize(QSize(45, 45))
        self.pushButton_9.setMaximumSize(QSize(45, 45))
        self.pushButton_9.setFont(font11)
        self.pushButton_9.setFocusPolicy(Qt.NoFocus)
        self.pushButton_9.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_9)

        self.pushButton_78 = QPushButton(self.frame)
        self.pushButton_78.setObjectName(u"pushButton_78")
        sizePolicy4.setHeightForWidth(self.pushButton_78.sizePolicy().hasHeightForWidth())
        self.pushButton_78.setSizePolicy(sizePolicy4)
        self.pushButton_78.setMinimumSize(QSize(45, 45))
        self.pushButton_78.setMaximumSize(QSize(45, 45))
        self.pushButton_78.setFont(font12)
        self.pushButton_78.setFocusPolicy(Qt.NoFocus)
        self.pushButton_78.setStyleSheet(u"QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 20pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_78)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_80 = QPushButton(self.frame)
        self.pushButton_80.setObjectName(u"pushButton_80")
        sizePolicy4.setHeightForWidth(self.pushButton_80.sizePolicy().hasHeightForWidth())
        self.pushButton_80.setSizePolicy(sizePolicy4)
        self.pushButton_80.setMinimumSize(QSize(115, 45))
        self.pushButton_80.setMaximumSize(QSize(115, 45))
        self.pushButton_80.setFont(font9)
        self.pushButton_80.setFocusPolicy(Qt.NoFocus)
        self.pushButton_80.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_80)

        self.pushButton_81 = QPushButton(self.frame)
        self.pushButton_81.setObjectName(u"pushButton_81")
        sizePolicy4.setHeightForWidth(self.pushButton_81.sizePolicy().hasHeightForWidth())
        self.pushButton_81.setSizePolicy(sizePolicy4)
        self.pushButton_81.setMinimumSize(QSize(45, 45))
        self.pushButton_81.setMaximumSize(QSize(45, 45))
        self.pushButton_81.setFont(font11)
        self.pushButton_81.setFocusPolicy(Qt.NoFocus)
        self.pushButton_81.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_81)

        self.pushButton_82 = QPushButton(self.frame)
        self.pushButton_82.setObjectName(u"pushButton_82")
        sizePolicy4.setHeightForWidth(self.pushButton_82.sizePolicy().hasHeightForWidth())
        self.pushButton_82.setSizePolicy(sizePolicy4)
        self.pushButton_82.setMinimumSize(QSize(45, 45))
        self.pushButton_82.setMaximumSize(QSize(45, 45))
        self.pushButton_82.setFont(font11)
        self.pushButton_82.setFocusPolicy(Qt.NoFocus)
        self.pushButton_82.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_82)

        self.pushButton_84 = QPushButton(self.frame)
        self.pushButton_84.setObjectName(u"pushButton_84")
        sizePolicy4.setHeightForWidth(self.pushButton_84.sizePolicy().hasHeightForWidth())
        self.pushButton_84.setSizePolicy(sizePolicy4)
        self.pushButton_84.setMinimumSize(QSize(45, 45))
        self.pushButton_84.setMaximumSize(QSize(45, 45))
        self.pushButton_84.setFont(font11)
        self.pushButton_84.setFocusPolicy(Qt.NoFocus)
        self.pushButton_84.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_84)

        self.pushButton_86 = QPushButton(self.frame)
        self.pushButton_86.setObjectName(u"pushButton_86")
        sizePolicy4.setHeightForWidth(self.pushButton_86.sizePolicy().hasHeightForWidth())
        self.pushButton_86.setSizePolicy(sizePolicy4)
        self.pushButton_86.setMinimumSize(QSize(45, 45))
        self.pushButton_86.setMaximumSize(QSize(45, 45))
        self.pushButton_86.setFont(font11)
        self.pushButton_86.setFocusPolicy(Qt.NoFocus)
        self.pushButton_86.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_86)

        self.pushButton_87 = QPushButton(self.frame)
        self.pushButton_87.setObjectName(u"pushButton_87")
        sizePolicy4.setHeightForWidth(self.pushButton_87.sizePolicy().hasHeightForWidth())
        self.pushButton_87.setSizePolicy(sizePolicy4)
        self.pushButton_87.setMinimumSize(QSize(45, 45))
        self.pushButton_87.setMaximumSize(QSize(45, 45))
        self.pushButton_87.setFont(font11)
        self.pushButton_87.setFocusPolicy(Qt.NoFocus)
        self.pushButton_87.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_87)

        self.pushButton_88 = QPushButton(self.frame)
        self.pushButton_88.setObjectName(u"pushButton_88")
        sizePolicy4.setHeightForWidth(self.pushButton_88.sizePolicy().hasHeightForWidth())
        self.pushButton_88.setSizePolicy(sizePolicy4)
        self.pushButton_88.setMinimumSize(QSize(45, 45))
        self.pushButton_88.setMaximumSize(QSize(45, 45))
        self.pushButton_88.setFont(font11)
        self.pushButton_88.setFocusPolicy(Qt.NoFocus)
        self.pushButton_88.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_88)

        self.pushButton_89 = QPushButton(self.frame)
        self.pushButton_89.setObjectName(u"pushButton_89")
        sizePolicy4.setHeightForWidth(self.pushButton_89.sizePolicy().hasHeightForWidth())
        self.pushButton_89.setSizePolicy(sizePolicy4)
        self.pushButton_89.setMinimumSize(QSize(45, 45))
        self.pushButton_89.setMaximumSize(QSize(45, 45))
        self.pushButton_89.setFont(font11)
        self.pushButton_89.setFocusPolicy(Qt.NoFocus)
        self.pushButton_89.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_89)

        self.pushButton_90 = QPushButton(self.frame)
        self.pushButton_90.setObjectName(u"pushButton_90")
        sizePolicy4.setHeightForWidth(self.pushButton_90.sizePolicy().hasHeightForWidth())
        self.pushButton_90.setSizePolicy(sizePolicy4)
        self.pushButton_90.setMinimumSize(QSize(45, 45))
        self.pushButton_90.setMaximumSize(QSize(45, 45))
        self.pushButton_90.setFont(font9)
        self.pushButton_90.setFocusPolicy(Qt.NoFocus)
        self.pushButton_90.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_90)

        self.pushButton_91 = QPushButton(self.frame)
        self.pushButton_91.setObjectName(u"pushButton_91")
        sizePolicy4.setHeightForWidth(self.pushButton_91.sizePolicy().hasHeightForWidth())
        self.pushButton_91.setSizePolicy(sizePolicy4)
        self.pushButton_91.setMinimumSize(QSize(45, 45))
        self.pushButton_91.setMaximumSize(QSize(45, 45))
        self.pushButton_91.setFont(font9)
        self.pushButton_91.setFocusPolicy(Qt.NoFocus)
        self.pushButton_91.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_91)

        self.pushButton_92 = QPushButton(self.frame)
        self.pushButton_92.setObjectName(u"pushButton_92")
        sizePolicy4.setHeightForWidth(self.pushButton_92.sizePolicy().hasHeightForWidth())
        self.pushButton_92.setSizePolicy(sizePolicy4)
        self.pushButton_92.setMinimumSize(QSize(45, 45))
        self.pushButton_92.setMaximumSize(QSize(45, 45))
        self.pushButton_92.setFont(font9)
        self.pushButton_92.setFocusPolicy(Qt.NoFocus)
        self.pushButton_92.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_92)

        self.pushButton_93 = QPushButton(self.frame)
        self.pushButton_93.setObjectName(u"pushButton_93")
        sizePolicy12.setHeightForWidth(self.pushButton_93.sizePolicy().hasHeightForWidth())
        self.pushButton_93.setSizePolicy(sizePolicy12)
        self.pushButton_93.setMinimumSize(QSize(78, 45))
        self.pushButton_93.setMaximumSize(QSize(82, 45))
        self.pushButton_93.setFont(font9)
        self.pushButton_93.setFocusPolicy(Qt.NoFocus)
        self.pushButton_93.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_93)

        self.pushButton_94 = QPushButton(self.frame)
        self.pushButton_94.setObjectName(u"pushButton_94")
        sizePolicy4.setHeightForWidth(self.pushButton_94.sizePolicy().hasHeightForWidth())
        self.pushButton_94.setSizePolicy(sizePolicy4)
        self.pushButton_94.setMinimumSize(QSize(45, 45))
        self.pushButton_94.setMaximumSize(QSize(45, 45))
        self.pushButton_94.setFont(font11)
        self.pushButton_94.setFocusPolicy(Qt.NoFocus)
        self.pushButton_94.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon35 = QIcon()
        icon35.addFile(u":/images/up_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_94.setIcon(icon35)
        self.pushButton_94.setIconSize(QSize(21, 21))

        self.horizontalLayout_12.addWidget(self.pushButton_94)

        self.pushButton_95 = QPushButton(self.frame)
        self.pushButton_95.setObjectName(u"pushButton_95")
        sizePolicy4.setHeightForWidth(self.pushButton_95.sizePolicy().hasHeightForWidth())
        self.pushButton_95.setSizePolicy(sizePolicy4)
        self.pushButton_95.setMinimumSize(QSize(45, 45))
        self.pushButton_95.setMaximumSize(QSize(45, 45))
        self.pushButton_95.setFont(font3)
        self.pushButton_95.setFocusPolicy(Qt.NoFocus)
        self.pushButton_95.setStyleSheet(u"QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 12pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_95)

        self.pushButton_96 = QPushButton(self.frame)
        self.pushButton_96.setObjectName(u"pushButton_96")
        sizePolicy4.setHeightForWidth(self.pushButton_96.sizePolicy().hasHeightForWidth())
        self.pushButton_96.setSizePolicy(sizePolicy4)
        self.pushButton_96.setMinimumSize(QSize(45, 45))
        self.pushButton_96.setMaximumSize(QSize(45, 45))
        self.pushButton_96.setFont(font11)
        self.pushButton_96.setFocusPolicy(Qt.NoFocus)
        self.pushButton_96.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_96)

        self.pushButton_97 = QPushButton(self.frame)
        self.pushButton_97.setObjectName(u"pushButton_97")
        sizePolicy4.setHeightForWidth(self.pushButton_97.sizePolicy().hasHeightForWidth())
        self.pushButton_97.setSizePolicy(sizePolicy4)
        self.pushButton_97.setMinimumSize(QSize(45, 45))
        self.pushButton_97.setMaximumSize(QSize(45, 45))
        self.pushButton_97.setFont(font9)
        self.pushButton_97.setFocusPolicy(Qt.NoFocus)
        self.pushButton_97.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_97)

        self.pushButton_98 = QPushButton(self.frame)
        self.pushButton_98.setObjectName(u"pushButton_98")
        sizePolicy4.setHeightForWidth(self.pushButton_98.sizePolicy().hasHeightForWidth())
        self.pushButton_98.setSizePolicy(sizePolicy4)
        self.pushButton_98.setMinimumSize(QSize(45, 45))
        self.pushButton_98.setMaximumSize(QSize(45, 45))
        self.pushButton_98.setFont(font9)
        self.pushButton_98.setFocusPolicy(Qt.NoFocus)
        self.pushButton_98.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon36 = QIcon()
        icon36.addFile(u":/images/backspace.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_98.setIcon(icon36)
        self.pushButton_98.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.pushButton_98)

        self.pushButton_99 = QPushButton(self.frame)
        self.pushButton_99.setObjectName(u"pushButton_99")
        sizePolicy4.setHeightForWidth(self.pushButton_99.sizePolicy().hasHeightForWidth())
        self.pushButton_99.setSizePolicy(sizePolicy4)
        self.pushButton_99.setMinimumSize(QSize(45, 45))
        self.pushButton_99.setMaximumSize(QSize(45, 45))
        self.pushButton_99.setFont(font12)
        self.pushButton_99.setFocusPolicy(Qt.NoFocus)
        self.pushButton_99.setStyleSheet(u"QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 20pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_99)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_100 = QPushButton(self.frame)
        self.pushButton_100.setObjectName(u"pushButton_100")
        sizePolicy4.setHeightForWidth(self.pushButton_100.sizePolicy().hasHeightForWidth())
        self.pushButton_100.setSizePolicy(sizePolicy4)
        self.pushButton_100.setMinimumSize(QSize(55, 45))
        self.pushButton_100.setMaximumSize(QSize(55, 45))
        self.pushButton_100.setFont(font9)
        self.pushButton_100.setFocusPolicy(Qt.NoFocus)
        self.pushButton_100.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton_100)

        self.pushButton_101 = QPushButton(self.frame)
        self.pushButton_101.setObjectName(u"pushButton_101")
        sizePolicy4.setHeightForWidth(self.pushButton_101.sizePolicy().hasHeightForWidth())
        self.pushButton_101.setSizePolicy(sizePolicy4)
        self.pushButton_101.setMinimumSize(QSize(55, 45))
        self.pushButton_101.setMaximumSize(QSize(55, 45))
        self.pushButton_101.setFont(font9)
        self.pushButton_101.setFocusPolicy(Qt.NoFocus)
        self.pushButton_101.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton_101)

        self.pushButton_102 = QPushButton(self.frame)
        self.pushButton_102.setObjectName(u"pushButton_102")
        sizePolicy14.setHeightForWidth(self.pushButton_102.sizePolicy().hasHeightForWidth())
        self.pushButton_102.setSizePolicy(sizePolicy14)
        self.pushButton_102.setMinimumSize(QSize(423, 45))
        self.pushButton_102.setMaximumSize(QSize(423, 16777215))
        self.pushButton_102.setFont(font11)
        self.pushButton_102.setFocusPolicy(Qt.NoFocus)
        self.pushButton_102.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(117, 118, 119);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton_102)

        self.pushButton_103 = QPushButton(self.frame)
        self.pushButton_103.setObjectName(u"pushButton_103")
        sizePolicy4.setHeightForWidth(self.pushButton_103.sizePolicy().hasHeightForWidth())
        self.pushButton_103.setSizePolicy(sizePolicy4)
        self.pushButton_103.setMinimumSize(QSize(55, 45))
        self.pushButton_103.setMaximumSize(QSize(55, 45))
        self.pushButton_103.setFont(font9)
        self.pushButton_103.setFocusPolicy(Qt.NoFocus)
        self.pushButton_103.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton_103)

        self.pushButton_104 = QPushButton(self.frame)
        self.pushButton_104.setObjectName(u"pushButton_104")
        sizePolicy4.setHeightForWidth(self.pushButton_104.sizePolicy().hasHeightForWidth())
        self.pushButton_104.setSizePolicy(sizePolicy4)
        self.pushButton_104.setMinimumSize(QSize(55, 45))
        self.pushButton_104.setMaximumSize(QSize(55, 45))
        self.pushButton_104.setFont(font9)
        self.pushButton_104.setFocusPolicy(Qt.NoFocus)
        self.pushButton_104.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton_104)

        self.pushButton_105 = QPushButton(self.frame)
        self.pushButton_105.setObjectName(u"pushButton_105")
        sizePolicy4.setHeightForWidth(self.pushButton_105.sizePolicy().hasHeightForWidth())
        self.pushButton_105.setSizePolicy(sizePolicy4)
        self.pushButton_105.setMinimumSize(QSize(45, 45))
        self.pushButton_105.setMaximumSize(QSize(45, 45))
        self.pushButton_105.setFont(font11)
        self.pushButton_105.setFocusPolicy(Qt.NoFocus)
        self.pushButton_105.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.pushButton_105.setIcon(icon8)
        self.pushButton_105.setIconSize(QSize(21, 21))

        self.horizontalLayout_13.addWidget(self.pushButton_105)

        self.pushButton_106 = QPushButton(self.frame)
        self.pushButton_106.setObjectName(u"pushButton_106")
        sizePolicy4.setHeightForWidth(self.pushButton_106.sizePolicy().hasHeightForWidth())
        self.pushButton_106.setSizePolicy(sizePolicy4)
        self.pushButton_106.setMinimumSize(QSize(45, 45))
        self.pushButton_106.setMaximumSize(QSize(45, 45))
        self.pushButton_106.setFont(font11)
        self.pushButton_106.setFocusPolicy(Qt.NoFocus)
        self.pushButton_106.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon37 = QIcon()
        icon37.addFile(u":/images/down_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_106.setIcon(icon37)
        self.pushButton_106.setIconSize(QSize(21, 21))

        self.horizontalLayout_13.addWidget(self.pushButton_106)

        self.pushButton_107 = QPushButton(self.frame)
        self.pushButton_107.setObjectName(u"pushButton_107")
        sizePolicy4.setHeightForWidth(self.pushButton_107.sizePolicy().hasHeightForWidth())
        self.pushButton_107.setSizePolicy(sizePolicy4)
        self.pushButton_107.setMinimumSize(QSize(45, 45))
        self.pushButton_107.setMaximumSize(QSize(45, 45))
        self.pushButton_107.setFont(font11)
        self.pushButton_107.setFocusPolicy(Qt.NoFocus)
        self.pushButton_107.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.pushButton_107.setIcon(icon9)
        self.pushButton_107.setIconSize(QSize(21, 21))

        self.horizontalLayout_13.addWidget(self.pushButton_107)

        self.pushButton_108 = QPushButton(self.frame)
        self.pushButton_108.setObjectName(u"pushButton_108")
        sizePolicy12.setHeightForWidth(self.pushButton_108.sizePolicy().hasHeightForWidth())
        self.pushButton_108.setSizePolicy(sizePolicy12)
        self.pushButton_108.setMinimumSize(QSize(50, 45))
        self.pushButton_108.setSizeIncrement(QSize(0, 0))
        self.pushButton_108.setBaseSize(QSize(0, 0))
        self.pushButton_108.setFont(font9)
        self.pushButton_108.setFocusPolicy(Qt.NoFocus)
        self.pushButton_108.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton_108)

        self.pushButton_109 = QPushButton(self.frame)
        self.pushButton_109.setObjectName(u"pushButton_109")
        sizePolicy12.setHeightForWidth(self.pushButton_109.sizePolicy().hasHeightForWidth())
        self.pushButton_109.setSizePolicy(sizePolicy12)
        self.pushButton_109.setMinimumSize(QSize(50, 45))
        self.pushButton_109.setMaximumSize(QSize(16777215, 45))
        self.pushButton_109.setFont(font9)
        self.pushButton_109.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.pushButton_109)

        self.pushButton_110 = QPushButton(self.frame)
        self.pushButton_110.setObjectName(u"pushButton_110")
        sizePolicy12.setHeightForWidth(self.pushButton_110.sizePolicy().hasHeightForWidth())
        self.pushButton_110.setSizePolicy(sizePolicy12)
        self.pushButton_110.setMinimumSize(QSize(50, 45))
        self.pushButton_110.setMaximumSize(QSize(16777215, 45))
        self.pushButton_110.setFont(font9)
        self.pushButton_110.setFocusPolicy(Qt.NoFocus)
        self.pushButton_110.setStyleSheet(u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton_110)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tabWidget.addTab(self.tab_10, "")

        self.verticalLayout_30.addWidget(self.tabWidget)


        self.horizontalLayout_101.addLayout(self.verticalLayout_30)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.tabWidget_24 = QTabWidget(self.centralwidget)
        self.tabWidget_24.setObjectName(u"tabWidget_24")
        sizePolicy2.setHeightForWidth(self.tabWidget_24.sizePolicy().hasHeightForWidth())
        self.tabWidget_24.setSizePolicy(sizePolicy2)
        self.tabWidget_24.setMinimumSize(QSize(251, 0))
        self.tabWidget_24.setMaximumSize(QSize(251, 16777215))
        self.tabWidget_24.setFont(font1)
        self.tabWidget_24.setTabPosition(QTabWidget.South)
        self.tabWidget_24Page1 = QWidget()
        self.tabWidget_24Page1.setObjectName(u"tabWidget_24Page1")
        self.frame_26 = QFrame(self.tabWidget_24Page1)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(7, 31, 201, 600))
        sizePolicy4.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy4)
        self.frame_26.setStyleSheet(u"QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_26)
        self.verticalLayout_32.setSpacing(12)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.z_plus_jogbutton = ActionButton(self.frame_26)
        self.z_plus_jogbutton.setObjectName(u"z_plus_jogbutton")
        self.z_plus_jogbutton.setMinimumSize(QSize(56, 56))
        self.z_plus_jogbutton.setMaximumSize(QSize(56, 56))
        icon38 = QIcon()
        icon38.addFile(u":/images/z_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.z_plus_jogbutton.setIcon(icon38)
        self.z_plus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_106.addWidget(self.z_plus_jogbutton)


        self.verticalLayout_32.addLayout(self.horizontalLayout_106)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.z_minus_jogbutton = ActionButton(self.frame_26)
        self.z_minus_jogbutton.setObjectName(u"z_minus_jogbutton")
        self.z_minus_jogbutton.setMinimumSize(QSize(56, 56))
        self.z_minus_jogbutton.setMaximumSize(QSize(56, 56))
        icon39 = QIcon()
        icon39.addFile(u":/images/z_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.z_minus_jogbutton.setIcon(icon39)
        self.z_minus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_107.addWidget(self.z_minus_jogbutton)


        self.verticalLayout_32.addLayout(self.horizontalLayout_107)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(15)
        self.x_plus_jogbutton = ActionButton(self.frame_26)
        self.x_plus_jogbutton.setObjectName(u"x_plus_jogbutton")
        sizePolicy4.setHeightForWidth(self.x_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.x_plus_jogbutton.setSizePolicy(sizePolicy4)
        self.x_plus_jogbutton.setMinimumSize(QSize(56, 56))
        self.x_plus_jogbutton.setMaximumSize(QSize(56, 56))
        icon40 = QIcon()
        icon40.addFile(u":/images/x_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.x_plus_jogbutton.setIcon(icon40)
        self.x_plus_jogbutton.setIconSize(QSize(48, 48))

        self.gridLayout_6.addWidget(self.x_plus_jogbutton, 1, 2, 1, 1)

        self.x_minus_jogbutton = ActionButton(self.frame_26)
        self.x_minus_jogbutton.setObjectName(u"x_minus_jogbutton")
        sizePolicy4.setHeightForWidth(self.x_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.x_minus_jogbutton.setSizePolicy(sizePolicy4)
        self.x_minus_jogbutton.setMinimumSize(QSize(56, 56))
        self.x_minus_jogbutton.setMaximumSize(QSize(56, 56))
        icon41 = QIcon()
        icon41.addFile(u":/images/x_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.x_minus_jogbutton.setIcon(icon41)
        self.x_minus_jogbutton.setIconSize(QSize(48, 48))

        self.gridLayout_6.addWidget(self.x_minus_jogbutton, 1, 0, 1, 1)

        self.y_minus_jogbutton = ActionButton(self.frame_26)
        self.y_minus_jogbutton.setObjectName(u"y_minus_jogbutton")
        sizePolicy4.setHeightForWidth(self.y_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.y_minus_jogbutton.setSizePolicy(sizePolicy4)
        self.y_minus_jogbutton.setMinimumSize(QSize(56, 56))
        self.y_minus_jogbutton.setMaximumSize(QSize(56, 56))
        icon42 = QIcon()
        icon42.addFile(u":/images/y_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.y_minus_jogbutton.setIcon(icon42)
        self.y_minus_jogbutton.setIconSize(QSize(48, 48))

        self.gridLayout_6.addWidget(self.y_minus_jogbutton, 2, 1, 1, 1)

        self.y_plus_jogbutton = ActionButton(self.frame_26)
        self.y_plus_jogbutton.setObjectName(u"y_plus_jogbutton")
        self.y_plus_jogbutton.setMinimumSize(QSize(56, 56))
        self.y_plus_jogbutton.setMaximumSize(QSize(56, 56))
        icon43 = QIcon()
        icon43.addFile(u":/images/y_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.y_plus_jogbutton.setIcon(icon43)
        self.y_plus_jogbutton.setIconSize(QSize(48, 48))

        self.gridLayout_6.addWidget(self.y_plus_jogbutton, 0, 1, 1, 1)


        self.verticalLayout_32.addLayout(self.gridLayout_6)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.a_minus_jogbutton = ActionButton(self.frame_26)
        self.a_minus_jogbutton.setObjectName(u"a_minus_jogbutton")
        sizePolicy4.setHeightForWidth(self.a_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.a_minus_jogbutton.setSizePolicy(sizePolicy4)
        self.a_minus_jogbutton.setMinimumSize(QSize(56, 56))
        self.a_minus_jogbutton.setMaximumSize(QSize(56, 56))
        icon44 = QIcon()
        icon44.addFile(u":/images/a_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.a_minus_jogbutton.setIcon(icon44)
        self.a_minus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_112.addWidget(self.a_minus_jogbutton)

        self.a_plus_jogbutton = ActionButton(self.frame_26)
        self.a_plus_jogbutton.setObjectName(u"a_plus_jogbutton")
        sizePolicy4.setHeightForWidth(self.a_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.a_plus_jogbutton.setSizePolicy(sizePolicy4)
        self.a_plus_jogbutton.setMinimumSize(QSize(56, 56))
        self.a_plus_jogbutton.setMaximumSize(QSize(56, 56))
        icon45 = QIcon()
        icon45.addFile(u":/images/a_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.a_plus_jogbutton.setIcon(icon45)
        self.a_plus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_112.addWidget(self.a_plus_jogbutton)


        self.verticalLayout_32.addLayout(self.horizontalLayout_112)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.b_minus_jogbutton = ActionButton(self.frame_26)
        self.b_minus_jogbutton.setObjectName(u"b_minus_jogbutton")
        sizePolicy4.setHeightForWidth(self.b_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.b_minus_jogbutton.setSizePolicy(sizePolicy4)
        self.b_minus_jogbutton.setMinimumSize(QSize(56, 56))
        self.b_minus_jogbutton.setMaximumSize(QSize(56, 56))
        icon46 = QIcon()
        icon46.addFile(u":/images/b_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_minus_jogbutton.setIcon(icon46)
        self.b_minus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_111.addWidget(self.b_minus_jogbutton)

        self.b_plus_jogbutton = ActionButton(self.frame_26)
        self.b_plus_jogbutton.setObjectName(u"b_plus_jogbutton")
        sizePolicy4.setHeightForWidth(self.b_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.b_plus_jogbutton.setSizePolicy(sizePolicy4)
        self.b_plus_jogbutton.setMinimumSize(QSize(56, 56))
        self.b_plus_jogbutton.setMaximumSize(QSize(56, 56))
        icon47 = QIcon()
        icon47.addFile(u":/images/b_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_plus_jogbutton.setIcon(icon47)
        self.b_plus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_111.addWidget(self.b_plus_jogbutton)


        self.verticalLayout_32.addLayout(self.horizontalLayout_111)

        self.label_20 = QLabel(self.tabWidget_24Page1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(55, 3, 150, 20))
        sizePolicy4.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy4)
        self.label_20.setMinimumSize(QSize(150, 20))
        self.label_20.setMaximumSize(QSize(150, 20))
        self.label_20.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.layoutWidget_2 = QWidget(self.tabWidget_24Page1)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(214, 0, 32, 621))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.statuslabel_15 = StatusLabel(self.layoutWidget_2)
        self.statuslabel_15.setObjectName(u"statuslabel_15")
        self.statuslabel_15.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.statuslabel_15.sizePolicy().hasHeightForWidth())
        self.statuslabel_15.setSizePolicy(sizePolicy1)
        self.statuslabel_15.setMinimumSize(QSize(30, 0))
        self.statuslabel_15.setMaximumSize(QSize(30, 16777215))
        self.statuslabel_15.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.statuslabel_15.setWordWrap(True)
        self.statuslabel_15.setIndent(0)

        self.verticalLayout_12.addWidget(self.statuslabel_15)

        self.statuslabel_16 = StatusLabel(self.layoutWidget_2)
        self.statuslabel_16.setObjectName(u"statuslabel_16")
        self.statuslabel_16.setMinimumSize(QSize(30, 0))
        self.statuslabel_16.setMaximumSize(QSize(30, 16777215))
        self.statuslabel_16.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_16.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.statuslabel_16.setWordWrap(True)
        self.statuslabel_16.setIndent(0)

        self.verticalLayout_12.addWidget(self.statuslabel_16)

        self.tabWidget_24.addTab(self.tabWidget_24Page1, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.layoutWidget = QWidget(self.tab_17)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(214, 0, 32, 621))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.statuslabel_13 = StatusLabel(self.layoutWidget)
        self.statuslabel_13.setObjectName(u"statuslabel_13")
        self.statuslabel_13.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.statuslabel_13.sizePolicy().hasHeightForWidth())
        self.statuslabel_13.setSizePolicy(sizePolicy1)
        self.statuslabel_13.setMinimumSize(QSize(30, 0))
        self.statuslabel_13.setMaximumSize(QSize(30, 16777215))
        self.statuslabel_13.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.statuslabel_13.setWordWrap(True)
        self.statuslabel_13.setIndent(0)

        self.verticalLayout_9.addWidget(self.statuslabel_13)

        self.statuslabel_14 = StatusLabel(self.layoutWidget)
        self.statuslabel_14.setObjectName(u"statuslabel_14")
        self.statuslabel_14.setMinimumSize(QSize(30, 0))
        self.statuslabel_14.setMaximumSize(QSize(30, 16777215))
        self.statuslabel_14.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_14.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.statuslabel_14.setWordWrap(True)
        self.statuslabel_14.setIndent(0)

        self.verticalLayout_9.addWidget(self.statuslabel_14)

        self.label_19 = QLabel(self.tab_17)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setEnabled(True)
        self.label_19.setGeometry(QRect(-3, 1, 208, 24))
        self.label_19.setMaximumSize(QSize(16777215, 30))
        self.label_19.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tabWidget_24.addTab(self.tab_17, "")

        self.verticalLayout.addWidget(self.tabWidget_24)


        self.horizontalLayout_101.addLayout(self.verticalLayout)


        self.verticalLayout_31.addLayout(self.horizontalLayout_101)

        self.main_control_screen_layout_panel = QHBoxLayout()
        self.main_control_screen_layout_panel.setSpacing(9)
        self.main_control_screen_layout_panel.setObjectName(u"main_control_screen_layout_panel")
        self.main_control_screen_layout_panel.setSizeConstraint(QLayout.SetFixedSize)
        self.main_control_screen_layout_panel.setContentsMargins(12, 0, 12, -1)
        self.main_control_qframe = QFrame(self.centralwidget)
        self.main_control_qframe.setObjectName(u"main_control_qframe")
        sizePolicy4.setHeightForWidth(self.main_control_qframe.sizePolicy().hasHeightForWidth())
        self.main_control_qframe.setSizePolicy(sizePolicy4)
        self.main_control_qframe.setMinimumSize(QSize(350, 340))
        self.main_control_qframe.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.main_control_qframe)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(18, 9, 18, 4)
        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(-1, -1, -1, 4)
        self.actionbutton_3 = ActionButton(self.main_control_qframe)
        self.actionbutton_3.setObjectName(u"actionbutton_3")
        sizePolicy12.setHeightForWidth(self.actionbutton_3.sizePolicy().hasHeightForWidth())
        self.actionbutton_3.setSizePolicy(sizePolicy12)
        self.actionbutton_3.setMinimumSize(QSize(0, 52))
        self.actionbutton_3.setMaximumSize(QSize(16777215, 52))
        self.actionbutton_3.setStyleSheet(u"QPushButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_92.addWidget(self.actionbutton_3)


        self.verticalLayout_28.addLayout(self.horizontalLayout_92)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.actionbutton_7 = ActionButton(self.main_control_qframe)
        self.actionbutton_7.setObjectName(u"actionbutton_7")
        sizePolicy4.setHeightForWidth(self.actionbutton_7.sizePolicy().hasHeightForWidth())
        self.actionbutton_7.setSizePolicy(sizePolicy4)
        self.actionbutton_7.setMinimumSize(QSize(130, 42))
        self.actionbutton_7.setMaximumSize(QSize(130, 42))
        self.actionbutton_7.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_91.addWidget(self.actionbutton_7)

        self.ref_coilumn_header_13 = QLabel(self.main_control_qframe)
        self.ref_coilumn_header_13.setObjectName(u"ref_coilumn_header_13")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_13.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_13.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_13.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_91.addWidget(self.ref_coilumn_header_13)

        self.actionbutton_10 = ActionButton(self.main_control_qframe)
        self.actionbutton_10.setObjectName(u"actionbutton_10")
        sizePolicy4.setHeightForWidth(self.actionbutton_10.sizePolicy().hasHeightForWidth())
        self.actionbutton_10.setSizePolicy(sizePolicy4)
        self.actionbutton_10.setMinimumSize(QSize(130, 42))
        self.actionbutton_10.setMaximumSize(QSize(130, 42))
        self.actionbutton_10.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_10.setCheckable(True)

        self.horizontalLayout_91.addWidget(self.actionbutton_10)


        self.verticalLayout_28.addLayout(self.horizontalLayout_91)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.actionbutton = ActionButton(self.main_control_qframe)
        self.actionbutton.setObjectName(u"actionbutton")
        sizePolicy4.setHeightForWidth(self.actionbutton.sizePolicy().hasHeightForWidth())
        self.actionbutton.setSizePolicy(sizePolicy4)
        self.actionbutton.setMinimumSize(QSize(130, 42))
        self.actionbutton.setMaximumSize(QSize(130, 42))
        self.actionbutton.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_90.addWidget(self.actionbutton)

        self.ref_coilumn_header_14 = QLabel(self.main_control_qframe)
        self.ref_coilumn_header_14.setObjectName(u"ref_coilumn_header_14")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_14.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_14.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_14.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_90.addWidget(self.ref_coilumn_header_14)

        self.actionbutton_5 = ActionButton(self.main_control_qframe)
        self.actionbutton_5.setObjectName(u"actionbutton_5")
        sizePolicy4.setHeightForWidth(self.actionbutton_5.sizePolicy().hasHeightForWidth())
        self.actionbutton_5.setSizePolicy(sizePolicy4)
        self.actionbutton_5.setMinimumSize(QSize(130, 42))
        self.actionbutton_5.setMaximumSize(QSize(130, 42))
        self.actionbutton_5.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_90.addWidget(self.actionbutton_5)


        self.verticalLayout_28.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.actionbutton_9 = ActionButton(self.main_control_qframe)
        self.actionbutton_9.setObjectName(u"actionbutton_9")
        sizePolicy4.setHeightForWidth(self.actionbutton_9.sizePolicy().hasHeightForWidth())
        self.actionbutton_9.setSizePolicy(sizePolicy4)
        self.actionbutton_9.setMinimumSize(QSize(130, 42))
        self.actionbutton_9.setMaximumSize(QSize(130, 42))
        self.actionbutton_9.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_9.setCheckable(True)

        self.horizontalLayout_75.addWidget(self.actionbutton_9)

        self.ref_coilumn_header_15 = QLabel(self.main_control_qframe)
        self.ref_coilumn_header_15.setObjectName(u"ref_coilumn_header_15")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_15.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_15.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_15.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.ref_coilumn_header_15)

        self.actionbutton_6 = ActionButton(self.main_control_qframe)
        self.actionbutton_6.setObjectName(u"actionbutton_6")
        sizePolicy4.setHeightForWidth(self.actionbutton_6.sizePolicy().hasHeightForWidth())
        self.actionbutton_6.setSizePolicy(sizePolicy4)
        self.actionbutton_6.setMinimumSize(QSize(130, 42))
        self.actionbutton_6.setMaximumSize(QSize(130, 42))
        self.actionbutton_6.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_6.setCheckable(True)

        self.horizontalLayout_75.addWidget(self.actionbutton_6)


        self.verticalLayout_28.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(-1, -1, -1, 0)
        self.actionbutton_8 = ActionButton(self.main_control_qframe)
        self.actionbutton_8.setObjectName(u"actionbutton_8")
        sizePolicy4.setHeightForWidth(self.actionbutton_8.sizePolicy().hasHeightForWidth())
        self.actionbutton_8.setSizePolicy(sizePolicy4)
        self.actionbutton_8.setMinimumSize(QSize(130, 42))
        self.actionbutton_8.setMaximumSize(QSize(130, 42))
        self.actionbutton_8.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_8.setCheckable(True)

        self.horizontalLayout_88.addWidget(self.actionbutton_8)

        self.ref_coilumn_header_17 = QLabel(self.main_control_qframe)
        self.ref_coilumn_header_17.setObjectName(u"ref_coilumn_header_17")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_17.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_17.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_17.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_88.addWidget(self.ref_coilumn_header_17)

        self.actionbutton_2 = ActionButton(self.main_control_qframe)
        self.actionbutton_2.setObjectName(u"actionbutton_2")
        sizePolicy4.setHeightForWidth(self.actionbutton_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_2.setSizePolicy(sizePolicy4)
        self.actionbutton_2.setMinimumSize(QSize(130, 42))
        self.actionbutton_2.setMaximumSize(QSize(130, 42))
        self.actionbutton_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.actionbutton_2.setCheckable(True)

        self.horizontalLayout_88.addWidget(self.actionbutton_2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_88)

        self.line = QFrame(self.main_control_qframe)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 2))
        self.line.setMaximumSize(QSize(16777215, 2))
        self.line.setStyleSheet(u"Line{\n"
"color:rgb(186, 189, 182);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(186, 189, 182);\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"}")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_28.addWidget(self.line)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.power_button = ActionButton(self.main_control_qframe)
        self.power_button.setObjectName(u"power_button")
        sizePolicy4.setHeightForWidth(self.power_button.sizePolicy().hasHeightForWidth())
        self.power_button.setSizePolicy(sizePolicy4)
        self.power_button.setMinimumSize(QSize(65, 35))
        self.power_button.setMaximumSize(QSize(65, 35))
        self.power_button.setFocusPolicy(Qt.NoFocus)
        self.power_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.power_button.setCheckable(True)

        self.horizontalLayout_89.addWidget(self.power_button)

        self.ref_coilumn_header_16 = QLabel(self.main_control_qframe)
        self.ref_coilumn_header_16.setObjectName(u"ref_coilumn_header_16")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_16.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_16.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_16.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.ref_coilumn_header_16)

        self.feedrate_2 = QLabel(self.main_control_qframe)
        self.feedrate_2.setObjectName(u"feedrate_2")
        sizePolicy4.setHeightForWidth(self.feedrate_2.sizePolicy().hasHeightForWidth())
        self.feedrate_2.setSizePolicy(sizePolicy4)
        self.feedrate_2.setMinimumSize(QSize(18, 25))
        self.feedrate_2.setMaximumSize(QSize(18, 25))
        self.feedrate_2.setStyleSheet(u"QLabel{\n"
"    border-style: none;\n"
"    border-color: rgb(46, 52, 54);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(46, 52, 54);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_89.addWidget(self.feedrate_2)

        self.label_26 = QLabel(self.main_control_qframe)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(80, 33))
        self.label_26.setMaximumSize(QSize(80, 33))
        self.label_26.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_89.addWidget(self.label_26)

        self.ref_coilumn_header_18 = QLabel(self.main_control_qframe)
        self.ref_coilumn_header_18.setObjectName(u"ref_coilumn_header_18")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_18.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_18.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_18.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.ref_coilumn_header_18)

        self.exit_button = ActionButton(self.main_control_qframe)
        self.exit_button.setObjectName(u"exit_button")
        sizePolicy4.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy4)
        self.exit_button.setMinimumSize(QSize(65, 35))
        self.exit_button.setMaximumSize(QSize(65, 35))
        self.exit_button.setFocusPolicy(Qt.NoFocus)
        self.exit_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.exit_button.setCheckable(True)

        self.horizontalLayout_89.addWidget(self.exit_button)


        self.verticalLayout_28.addLayout(self.horizontalLayout_89)


        self.main_control_screen_layout_panel.addWidget(self.main_control_qframe)

        self.tool_info_qframe = QFrame(self.centralwidget)
        self.tool_info_qframe.setObjectName(u"tool_info_qframe")
        sizePolicy4.setHeightForWidth(self.tool_info_qframe.sizePolicy().hasHeightForWidth())
        self.tool_info_qframe.setSizePolicy(sizePolicy4)
        self.tool_info_qframe.setMinimumSize(QSize(210, 340))
        self.tool_info_qframe.setMaximumSize(QSize(210, 340))
        self.tool_info_qframe.setFocusPolicy(Qt.NoFocus)
        self.tool_info_qframe.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.tool_info_qframe)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(12, 9, 12, 3)
        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.frame_27 = QFrame(self.tool_info_qframe)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy12.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy12)
        self.frame_27.setMinimumSize(QSize(0, 38))
        self.frame_27.setMaximumSize(QSize(16777215, 38))
        self.frame_27.setStyleSheet(u"QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(176, 179,172);\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(90, 90, 90);\n"
"padding: -5px;\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 1, 0)
        self.ref_coilumn_header_3 = QLabel(self.frame_27)
        self.ref_coilumn_header_3.setObjectName(u"ref_coilumn_header_3")
        sizePolicy4.setHeightForWidth(self.ref_coilumn_header_3.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_3.setSizePolicy(sizePolicy4)
        self.ref_coilumn_header_3.setMinimumSize(QSize(15, 36))
        self.ref_coilumn_header_3.setMaximumSize(QSize(15, 36))
        self.ref_coilumn_header_3.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.ref_coilumn_header_3.setAlignment(Qt.AlignCenter)
        self.ref_coilumn_header_3.setIndent(0)

        self.horizontalLayout_105.addWidget(self.ref_coilumn_header_3)

        self.tool_number_entry_box = QLineEdit(self.frame_27)
        self.tool_number_entry_box.setObjectName(u"tool_number_entry_box")
        sizePolicy4.setHeightForWidth(self.tool_number_entry_box.sizePolicy().hasHeightForWidth())
        self.tool_number_entry_box.setSizePolicy(sizePolicy4)
        self.tool_number_entry_box.setMinimumSize(QSize(55, 0))
        self.tool_number_entry_box.setMaximumSize(QSize(55, 16777215))
        palette3 = QPalette()
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        brush8 = QBrush(QColor(235, 235, 235, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.tool_number_entry_box.setPalette(palette3)
        font13 = QFont()
        font13.setFamilies([u"Probe Basic Bebas Mono"])
        font13.setPointSize(17)
        font13.setBold(False)
        font13.setItalic(False)
        self.tool_number_entry_box.setFont(font13)
        self.tool_number_entry_box.setFocusPolicy(Qt.ClickFocus)
        self.tool_number_entry_box.setContextMenuPolicy(Qt.NoContextMenu)
        self.tool_number_entry_box.setStyleSheet(u"QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_number_entry_box.setFrame(True)
        self.tool_number_entry_box.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_105.addWidget(self.tool_number_entry_box)


        self.horizontalLayout_96.addWidget(self.frame_27)

        self.m6_button = MDIButton(self.tool_info_qframe)
        self.m6_button.setObjectName(u"m6_button")
        self.m6_button.setMinimumSize(QSize(70, 40))
        self.m6_button.setMaximumSize(QSize(16777215, 40))
        self.m6_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_96.addWidget(self.m6_button)


        self.verticalLayout_29.addLayout(self.horizontalLayout_96)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.G43 = MDIButton(self.tool_info_qframe)
        self.G43.setObjectName(u"G43")
        self.G43.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.G43.sizePolicy().hasHeightForWidth())
        self.G43.setSizePolicy(sizePolicy5)
        self.G43.setMinimumSize(QSize(0, 40))
        self.G43.setMaximumSize(QSize(16777215, 40))
        self.G43.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.G43.setCheckable(True)
        self.G43.setAutoExclusive(True)

        self.horizontalLayout_104.addWidget(self.G43)

        self.G49 = MDIButton(self.tool_info_qframe)
        self.G49.setObjectName(u"G49")
        self.G49.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.G49.sizePolicy().hasHeightForWidth())
        self.G49.setSizePolicy(sizePolicy5)
        self.G49.setMinimumSize(QSize(0, 40))
        self.G49.setMaximumSize(QSize(16777215, 40))
        self.G49.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.G49.setCheckable(True)
        self.G49.setAutoExclusive(True)

        self.horizontalLayout_104.addWidget(self.G49)


        self.verticalLayout_29.addLayout(self.horizontalLayout_104)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.go_to_g30_button_2 = ActionButton(self.tool_info_qframe)
        self.go_to_g30_button_2.setObjectName(u"go_to_g30_button_2")
        sizePolicy5.setHeightForWidth(self.go_to_g30_button_2.sizePolicy().hasHeightForWidth())
        self.go_to_g30_button_2.setSizePolicy(sizePolicy5)
        self.go_to_g30_button_2.setMinimumSize(QSize(0, 40))
        self.go_to_g30_button_2.setMaximumSize(QSize(16777215, 40))
        self.go_to_g30_button_2.setFocusPolicy(Qt.NoFocus)
        self.go_to_g30_button_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_95.addWidget(self.go_to_g30_button_2)

        self.go_to_g30 = MDIButton(self.tool_info_qframe)
        self.go_to_g30.setObjectName(u"go_to_g30")
        self.go_to_g30.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.go_to_g30.sizePolicy().hasHeightForWidth())
        self.go_to_g30.setSizePolicy(sizePolicy5)
        self.go_to_g30.setMinimumSize(QSize(0, 40))
        self.go_to_g30.setMaximumSize(QSize(16777215, 40))
        self.go_to_g30.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_95.addWidget(self.go_to_g30)


        self.verticalLayout_29.addLayout(self.horizontalLayout_95)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setSpacing(5)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(-1, -1, 0, -1)
        self.work_column_header_4 = QLabel(self.tool_info_qframe)
        self.work_column_header_4.setObjectName(u"work_column_header_4")
        self.work_column_header_4.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.work_column_header_4.sizePolicy().hasHeightForWidth())
        self.work_column_header_4.setSizePolicy(sizePolicy4)
        self.work_column_header_4.setMinimumSize(QSize(60, 33))
        self.work_column_header_4.setMaximumSize(QSize(60, 33))
        self.work_column_header_4.setStyleSheet(u"QLabel{\n"
"    border-style: none;\n"
"    border-color: rgb(46, 52, 54);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(46, 52, 54);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.work_column_header_4.setAlignment(Qt.AlignCenter)
        self.work_column_header_4.setWordWrap(True)
        self.work_column_header_4.setIndent(0)

        self.horizontalLayout_94.addWidget(self.work_column_header_4)

        self.tool_length = StatusLabel(self.tool_info_qframe)
        self.tool_length.setObjectName(u"tool_length")
        sizePolicy7.setHeightForWidth(self.tool_length.sizePolicy().hasHeightForWidth())
        self.tool_length.setSizePolicy(sizePolicy7)
        self.tool_length.setMinimumSize(QSize(0, 33))
        self.tool_length.setMaximumSize(QSize(16777215, 33))
        self.tool_length.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_length.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_94.addWidget(self.tool_length)

        self.statuslabel_8 = StatusLabel(self.tool_info_qframe)
        self.statuslabel_8.setObjectName(u"statuslabel_8")
        sizePolicy12.setHeightForWidth(self.statuslabel_8.sizePolicy().hasHeightForWidth())
        self.statuslabel_8.setSizePolicy(sizePolicy12)
        self.statuslabel_8.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_94.addWidget(self.statuslabel_8)


        self.verticalLayout_29.addLayout(self.horizontalLayout_94)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setSpacing(5)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.work_column_header_5 = QLabel(self.tool_info_qframe)
        self.work_column_header_5.setObjectName(u"work_column_header_5")
        self.work_column_header_5.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.work_column_header_5.sizePolicy().hasHeightForWidth())
        self.work_column_header_5.setSizePolicy(sizePolicy4)
        self.work_column_header_5.setMinimumSize(QSize(60, 33))
        self.work_column_header_5.setMaximumSize(QSize(60, 33))
        self.work_column_header_5.setStyleSheet(u"QLabel{\n"
"    border-style: none;\n"
"    border-color: rgb(46, 52, 54);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(46, 52, 54);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"")
        self.work_column_header_5.setAlignment(Qt.AlignCenter)
        self.work_column_header_5.setWordWrap(True)
        self.work_column_header_5.setIndent(0)

        self.horizontalLayout_93.addWidget(self.work_column_header_5)

        self.tool_diameter = StatusLabel(self.tool_info_qframe)
        self.tool_diameter.setObjectName(u"tool_diameter")
        sizePolicy7.setHeightForWidth(self.tool_diameter.sizePolicy().hasHeightForWidth())
        self.tool_diameter.setSizePolicy(sizePolicy7)
        self.tool_diameter.setMinimumSize(QSize(0, 33))
        self.tool_diameter.setMaximumSize(QSize(16777215, 33))
        self.tool_diameter.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.tool_diameter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_93.addWidget(self.tool_diameter)

        self.statuslabel_11 = StatusLabel(self.tool_info_qframe)
        self.statuslabel_11.setObjectName(u"statuslabel_11")
        sizePolicy12.setHeightForWidth(self.statuslabel_11.sizePolicy().hasHeightForWidth())
        self.statuslabel_11.setSizePolicy(sizePolicy12)
        self.statuslabel_11.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_93.addWidget(self.statuslabel_11)


        self.verticalLayout_29.addLayout(self.horizontalLayout_93)

        self.line_7 = QFrame(self.tool_info_qframe)
        self.line_7.setObjectName(u"line_7")
        sizePolicy12.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy12)
        self.line_7.setMinimumSize(QSize(0, 2))
        self.line_7.setMaximumSize(QSize(16777215, 2))
        self.line_7.setStyleSheet(u"Line{\n"
"color:rgb(186, 189, 182);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(186, 189, 182);\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"}")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_29.addWidget(self.line_7)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(-1, -1, -1, 0)
        self.axisactionbutton_5 = ActionButton(self.tool_info_qframe)
        self.axisactionbutton_5.setObjectName(u"axisactionbutton_5")
        sizePolicy12.setHeightForWidth(self.axisactionbutton_5.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_5.setSizePolicy(sizePolicy12)
        self.axisactionbutton_5.setMinimumSize(QSize(60, 40))
        self.axisactionbutton_5.setMaximumSize(QSize(16777215, 40))
        self.axisactionbutton_5.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_97.addWidget(self.axisactionbutton_5)


        self.verticalLayout_29.addLayout(self.horizontalLayout_97)


        self.main_control_screen_layout_panel.addWidget(self.tool_info_qframe)

        self.main_dro_qframe = QFrame(self.centralwidget)
        self.main_dro_qframe.setObjectName(u"main_dro_qframe")
        sizePolicy4.setHeightForWidth(self.main_dro_qframe.sizePolicy().hasHeightForWidth())
        self.main_dro_qframe.setSizePolicy(sizePolicy4)
        self.main_dro_qframe.setMinimumSize(QSize(482, 340))
        self.main_dro_qframe.setMaximumSize(QSize(482, 340))
        self.main_dro_qframe.setFocusPolicy(Qt.NoFocus)
        self.main_dro_qframe.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"padding-left: 7px;\n"
"padding-right: 7px;\n"
"padding-top: -1px;\n"
"padding-bottom:-1px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.main_dro_qframe)
        self.verticalLayout_4.setSpacing(13)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 15, -1, 11)
        self.frame_25 = QFrame(self.main_dro_qframe)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy12.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy12)
        self.frame_25.setMinimumSize(QSize(0, 40))
        self.frame_25.setMaximumSize(QSize(16777215, 40))
        self.frame_25.setStyleSheet(u"QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(176, 179,172);\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(90, 90, 90);\n"
"padding: -5px;\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_103.setSpacing(8)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(5, -1, 7, -1)
        self.axis_column_header = QLabel(self.frame_25)
        self.axis_column_header.setObjectName(u"axis_column_header")
        sizePolicy4.setHeightForWidth(self.axis_column_header.sizePolicy().hasHeightForWidth())
        self.axis_column_header.setSizePolicy(sizePolicy4)
        self.axis_column_header.setMinimumSize(QSize(55, 17))
        self.axis_column_header.setMaximumSize(QSize(65, 17))
        self.axis_column_header.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_column_header.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_103.addWidget(self.axis_column_header)

        self.statuslabel_12 = StatusLabel(self.frame_25)
        self.statuslabel_12.setObjectName(u"statuslabel_12")
        sizePolicy4.setHeightForWidth(self.statuslabel_12.sizePolicy().hasHeightForWidth())
        self.statuslabel_12.setSizePolicy(sizePolicy4)
        self.statuslabel_12.setMinimumSize(QSize(100, 17))
        self.statuslabel_12.setMaximumSize(QSize(100, 17))
        self.statuslabel_12.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_103.addWidget(self.statuslabel_12)

        self.work_column_header_2 = QLabel(self.frame_25)
        self.work_column_header_2.setObjectName(u"work_column_header_2")
        self.work_column_header_2.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.work_column_header_2.sizePolicy().hasHeightForWidth())
        self.work_column_header_2.setSizePolicy(sizePolicy4)
        self.work_column_header_2.setMinimumSize(QSize(100, 17))
        self.work_column_header_2.setMaximumSize(QSize(100, 17))
        self.work_column_header_2.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.work_column_header_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_103.addWidget(self.work_column_header_2)

        self.dtg_column_header = QLabel(self.frame_25)
        self.dtg_column_header.setObjectName(u"dtg_column_header")
        sizePolicy4.setHeightForWidth(self.dtg_column_header.sizePolicy().hasHeightForWidth())
        self.dtg_column_header.setSizePolicy(sizePolicy4)
        self.dtg_column_header.setMinimumSize(QSize(100, 17))
        self.dtg_column_header.setMaximumSize(QSize(100, 17))
        self.dtg_column_header.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.dtg_column_header.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_103.addWidget(self.dtg_column_header)

        self.dtg_column_header_3 = QLabel(self.frame_25)
        self.dtg_column_header_3.setObjectName(u"dtg_column_header_3")
        sizePolicy4.setHeightForWidth(self.dtg_column_header_3.sizePolicy().hasHeightForWidth())
        self.dtg_column_header_3.setSizePolicy(sizePolicy4)
        self.dtg_column_header_3.setMinimumSize(QSize(60, 17))
        self.dtg_column_header_3.setMaximumSize(QSize(60, 17))
        self.dtg_column_header_3.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.dtg_column_header_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_103.addWidget(self.dtg_column_header_3)


        self.verticalLayout_4.addWidget(self.frame_25)

        self.x_axis_dro_layout = QHBoxLayout()
        self.x_axis_dro_layout.setSpacing(8)
        self.x_axis_dro_layout.setObjectName(u"x_axis_dro_layout")
        self.zero_x_button_3 = MDIButton(self.main_dro_qframe)
        self.zero_x_button_3.setObjectName(u"zero_x_button_3")
        self.zero_x_button_3.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zero_x_button_3.sizePolicy().hasHeightForWidth())
        self.zero_x_button_3.setSizePolicy(sizePolicy1)
        self.zero_x_button_3.setMinimumSize(QSize(50, 40))
        self.zero_x_button_3.setMaximumSize(QSize(58, 40))
        self.zero_x_button_3.setLayoutDirection(Qt.LeftToRight)
        self.zero_x_button_3.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon48 = QIcon()
        icon48.addFile(u":/images/zero.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zero_x_button_3.setIcon(icon48)
        self.zero_x_button_3.setIconSize(QSize(20, 20))

        self.x_axis_dro_layout.addWidget(self.zero_x_button_3)

        self.statuslabel_40 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_40.setObjectName(u"statuslabel_40")
        sizePolicy4.setHeightForWidth(self.statuslabel_40.sizePolicy().hasHeightForWidth())
        self.statuslabel_40.setSizePolicy(sizePolicy4)
        self.statuslabel_40.setMinimumSize(QSize(100, 35))
        self.statuslabel_40.setMaximumSize(QSize(100, 35))
        self.statuslabel_40.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.x_axis_dro_layout.addWidget(self.statuslabel_40)

        self.statuslabel_45 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_45.setObjectName(u"statuslabel_45")
        sizePolicy4.setHeightForWidth(self.statuslabel_45.sizePolicy().hasHeightForWidth())
        self.statuslabel_45.setSizePolicy(sizePolicy4)
        self.statuslabel_45.setMinimumSize(QSize(100, 35))
        self.statuslabel_45.setMaximumSize(QSize(100, 35))
        self.statuslabel_45.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"StatusLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"StatusLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.statuslabel_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.x_axis_dro_layout.addWidget(self.statuslabel_45)

        self.statuslabel_75 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_75.setObjectName(u"statuslabel_75")
        sizePolicy4.setHeightForWidth(self.statuslabel_75.sizePolicy().hasHeightForWidth())
        self.statuslabel_75.setSizePolicy(sizePolicy4)
        self.statuslabel_75.setMinimumSize(QSize(100, 35))
        self.statuslabel_75.setMaximumSize(QSize(100, 35))
        self.statuslabel_75.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_75.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.x_axis_dro_layout.addWidget(self.statuslabel_75)

        self.axisactionbutton_6 = ActionButton(self.main_dro_qframe)
        self.axisactionbutton_6.setObjectName(u"axisactionbutton_6")
        sizePolicy4.setHeightForWidth(self.axisactionbutton_6.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_6.setSizePolicy(sizePolicy4)
        self.axisactionbutton_6.setMinimumSize(QSize(60, 40))
        self.axisactionbutton_6.setMaximumSize(QSize(60, 40))
        self.axisactionbutton_6.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.x_axis_dro_layout.addWidget(self.axisactionbutton_6)


        self.verticalLayout_4.addLayout(self.x_axis_dro_layout)

        self.y_axis_dro_layout = QHBoxLayout()
        self.y_axis_dro_layout.setSpacing(8)
        self.y_axis_dro_layout.setObjectName(u"y_axis_dro_layout")
        self.zero_y_button_3 = MDIButton(self.main_dro_qframe)
        self.zero_y_button_3.setObjectName(u"zero_y_button_3")
        self.zero_y_button_3.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zero_y_button_3.sizePolicy().hasHeightForWidth())
        self.zero_y_button_3.setSizePolicy(sizePolicy1)
        self.zero_y_button_3.setMinimumSize(QSize(50, 40))
        self.zero_y_button_3.setMaximumSize(QSize(55, 40))
        self.zero_y_button_3.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_y_button_3.setIcon(icon48)
        self.zero_y_button_3.setIconSize(QSize(20, 20))

        self.y_axis_dro_layout.addWidget(self.zero_y_button_3)

        self.statuslabel_41 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_41.setObjectName(u"statuslabel_41")
        sizePolicy4.setHeightForWidth(self.statuslabel_41.sizePolicy().hasHeightForWidth())
        self.statuslabel_41.setSizePolicy(sizePolicy4)
        self.statuslabel_41.setMinimumSize(QSize(100, 35))
        self.statuslabel_41.setMaximumSize(QSize(100, 35))
        self.statuslabel_41.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.y_axis_dro_layout.addWidget(self.statuslabel_41)

        self.statuslabel_46 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_46.setObjectName(u"statuslabel_46")
        sizePolicy4.setHeightForWidth(self.statuslabel_46.sizePolicy().hasHeightForWidth())
        self.statuslabel_46.setSizePolicy(sizePolicy4)
        self.statuslabel_46.setMinimumSize(QSize(100, 35))
        self.statuslabel_46.setMaximumSize(QSize(100, 35))
        self.statuslabel_46.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"StatusLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"StatusLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.statuslabel_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.y_axis_dro_layout.addWidget(self.statuslabel_46)

        self.statuslabel_76 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_76.setObjectName(u"statuslabel_76")
        sizePolicy4.setHeightForWidth(self.statuslabel_76.sizePolicy().hasHeightForWidth())
        self.statuslabel_76.setSizePolicy(sizePolicy4)
        self.statuslabel_76.setMinimumSize(QSize(100, 35))
        self.statuslabel_76.setMaximumSize(QSize(100, 35))
        self.statuslabel_76.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_76.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.y_axis_dro_layout.addWidget(self.statuslabel_76)

        self.axisactionbutton_3 = ActionButton(self.main_dro_qframe)
        self.axisactionbutton_3.setObjectName(u"axisactionbutton_3")
        sizePolicy4.setHeightForWidth(self.axisactionbutton_3.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_3.setSizePolicy(sizePolicy4)
        self.axisactionbutton_3.setMinimumSize(QSize(60, 40))
        self.axisactionbutton_3.setMaximumSize(QSize(60, 40))
        self.axisactionbutton_3.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.y_axis_dro_layout.addWidget(self.axisactionbutton_3)


        self.verticalLayout_4.addLayout(self.y_axis_dro_layout)

        self.z_axis_dro_layout = QHBoxLayout()
        self.z_axis_dro_layout.setSpacing(8)
        self.z_axis_dro_layout.setObjectName(u"z_axis_dro_layout")
        self.zero_z_button_3 = MDIButton(self.main_dro_qframe)
        self.zero_z_button_3.setObjectName(u"zero_z_button_3")
        self.zero_z_button_3.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zero_z_button_3.sizePolicy().hasHeightForWidth())
        self.zero_z_button_3.setSizePolicy(sizePolicy1)
        self.zero_z_button_3.setMinimumSize(QSize(50, 40))
        self.zero_z_button_3.setMaximumSize(QSize(55, 40))
        self.zero_z_button_3.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_z_button_3.setIcon(icon48)
        self.zero_z_button_3.setIconSize(QSize(20, 20))

        self.z_axis_dro_layout.addWidget(self.zero_z_button_3)

        self.statuslabel_42 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_42.setObjectName(u"statuslabel_42")
        sizePolicy4.setHeightForWidth(self.statuslabel_42.sizePolicy().hasHeightForWidth())
        self.statuslabel_42.setSizePolicy(sizePolicy4)
        self.statuslabel_42.setMinimumSize(QSize(100, 35))
        self.statuslabel_42.setMaximumSize(QSize(100, 35))
        self.statuslabel_42.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.z_axis_dro_layout.addWidget(self.statuslabel_42)

        self.statuslabel_47 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_47.setObjectName(u"statuslabel_47")
        sizePolicy4.setHeightForWidth(self.statuslabel_47.sizePolicy().hasHeightForWidth())
        self.statuslabel_47.setSizePolicy(sizePolicy4)
        self.statuslabel_47.setMinimumSize(QSize(100, 35))
        self.statuslabel_47.setMaximumSize(QSize(100, 35))
        self.statuslabel_47.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"StatusLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"StatusLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.statuslabel_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.z_axis_dro_layout.addWidget(self.statuslabel_47)

        self.statuslabel_77 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_77.setObjectName(u"statuslabel_77")
        sizePolicy4.setHeightForWidth(self.statuslabel_77.sizePolicy().hasHeightForWidth())
        self.statuslabel_77.setSizePolicy(sizePolicy4)
        self.statuslabel_77.setMinimumSize(QSize(100, 35))
        self.statuslabel_77.setMaximumSize(QSize(100, 35))
        self.statuslabel_77.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_77.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.z_axis_dro_layout.addWidget(self.statuslabel_77)

        self.axisactionbutton = ActionButton(self.main_dro_qframe)
        self.axisactionbutton.setObjectName(u"axisactionbutton")
        sizePolicy4.setHeightForWidth(self.axisactionbutton.sizePolicy().hasHeightForWidth())
        self.axisactionbutton.setSizePolicy(sizePolicy4)
        self.axisactionbutton.setMinimumSize(QSize(60, 40))
        self.axisactionbutton.setMaximumSize(QSize(60, 40))
        self.axisactionbutton.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.z_axis_dro_layout.addWidget(self.axisactionbutton)


        self.verticalLayout_4.addLayout(self.z_axis_dro_layout)

        self.a_axis_dro_layout = QHBoxLayout()
        self.a_axis_dro_layout.setSpacing(8)
        self.a_axis_dro_layout.setObjectName(u"a_axis_dro_layout")
        self.zero_a_button_3 = MDIButton(self.main_dro_qframe)
        self.zero_a_button_3.setObjectName(u"zero_a_button_3")
        self.zero_a_button_3.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zero_a_button_3.sizePolicy().hasHeightForWidth())
        self.zero_a_button_3.setSizePolicy(sizePolicy1)
        self.zero_a_button_3.setMinimumSize(QSize(50, 40))
        self.zero_a_button_3.setMaximumSize(QSize(55, 40))
        self.zero_a_button_3.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_a_button_3.setIcon(icon48)
        self.zero_a_button_3.setIconSize(QSize(20, 20))

        self.a_axis_dro_layout.addWidget(self.zero_a_button_3)

        self.statuslabel_43 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_43.setObjectName(u"statuslabel_43")
        sizePolicy4.setHeightForWidth(self.statuslabel_43.sizePolicy().hasHeightForWidth())
        self.statuslabel_43.setSizePolicy(sizePolicy4)
        self.statuslabel_43.setMinimumSize(QSize(100, 35))
        self.statuslabel_43.setMaximumSize(QSize(100, 35))
        self.statuslabel_43.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.a_axis_dro_layout.addWidget(self.statuslabel_43)

        self.statuslabel_48 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_48.setObjectName(u"statuslabel_48")
        sizePolicy4.setHeightForWidth(self.statuslabel_48.sizePolicy().hasHeightForWidth())
        self.statuslabel_48.setSizePolicy(sizePolicy4)
        self.statuslabel_48.setMinimumSize(QSize(100, 35))
        self.statuslabel_48.setMaximumSize(QSize(100, 35))
        self.statuslabel_48.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"StatusLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"StatusLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.statuslabel_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.a_axis_dro_layout.addWidget(self.statuslabel_48)

        self.statuslabel_78 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_78.setObjectName(u"statuslabel_78")
        sizePolicy4.setHeightForWidth(self.statuslabel_78.sizePolicy().hasHeightForWidth())
        self.statuslabel_78.setSizePolicy(sizePolicy4)
        self.statuslabel_78.setMinimumSize(QSize(100, 35))
        self.statuslabel_78.setMaximumSize(QSize(100, 35))
        self.statuslabel_78.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_78.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.a_axis_dro_layout.addWidget(self.statuslabel_78)

        self.axisactionbutton_2 = ActionButton(self.main_dro_qframe)
        self.axisactionbutton_2.setObjectName(u"axisactionbutton_2")
        sizePolicy4.setHeightForWidth(self.axisactionbutton_2.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_2.setSizePolicy(sizePolicy4)
        self.axisactionbutton_2.setMinimumSize(QSize(60, 40))
        self.axisactionbutton_2.setMaximumSize(QSize(60, 40))
        self.axisactionbutton_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.a_axis_dro_layout.addWidget(self.axisactionbutton_2)


        self.verticalLayout_4.addLayout(self.a_axis_dro_layout)

        self.b_axis_dro_layout = QHBoxLayout()
        self.b_axis_dro_layout.setSpacing(8)
        self.b_axis_dro_layout.setObjectName(u"b_axis_dro_layout")
        self.zero_b_button_3 = MDIButton(self.main_dro_qframe)
        self.zero_b_button_3.setObjectName(u"zero_b_button_3")
        self.zero_b_button_3.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zero_b_button_3.sizePolicy().hasHeightForWidth())
        self.zero_b_button_3.setSizePolicy(sizePolicy1)
        self.zero_b_button_3.setMinimumSize(QSize(50, 40))
        self.zero_b_button_3.setMaximumSize(QSize(55, 40))
        self.zero_b_button_3.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_b_button_3.setIcon(icon48)
        self.zero_b_button_3.setIconSize(QSize(20, 20))

        self.b_axis_dro_layout.addWidget(self.zero_b_button_3)

        self.statuslabel_44 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_44.setObjectName(u"statuslabel_44")
        sizePolicy4.setHeightForWidth(self.statuslabel_44.sizePolicy().hasHeightForWidth())
        self.statuslabel_44.setSizePolicy(sizePolicy4)
        self.statuslabel_44.setMinimumSize(QSize(100, 35))
        self.statuslabel_44.setMaximumSize(QSize(100, 35))
        self.statuslabel_44.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.b_axis_dro_layout.addWidget(self.statuslabel_44)

        self.statuslabel_49 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_49.setObjectName(u"statuslabel_49")
        sizePolicy4.setHeightForWidth(self.statuslabel_49.sizePolicy().hasHeightForWidth())
        self.statuslabel_49.setSizePolicy(sizePolicy4)
        self.statuslabel_49.setMinimumSize(QSize(100, 35))
        self.statuslabel_49.setMaximumSize(QSize(100, 35))
        self.statuslabel_49.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"StatusLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"StatusLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.statuslabel_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.b_axis_dro_layout.addWidget(self.statuslabel_49)

        self.statuslabel_79 = StatusLabel(self.main_dro_qframe)
        self.statuslabel_79.setObjectName(u"statuslabel_79")
        sizePolicy4.setHeightForWidth(self.statuslabel_79.sizePolicy().hasHeightForWidth())
        self.statuslabel_79.setSizePolicy(sizePolicy4)
        self.statuslabel_79.setMinimumSize(QSize(100, 35))
        self.statuslabel_79.setMaximumSize(QSize(100, 35))
        self.statuslabel_79.setStyleSheet(u"StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_79.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.b_axis_dro_layout.addWidget(self.statuslabel_79)

        self.axisactionbutton_4 = ActionButton(self.main_dro_qframe)
        self.axisactionbutton_4.setObjectName(u"axisactionbutton_4")
        sizePolicy4.setHeightForWidth(self.axisactionbutton_4.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_4.setSizePolicy(sizePolicy4)
        self.axisactionbutton_4.setMinimumSize(QSize(60, 40))
        self.axisactionbutton_4.setMaximumSize(QSize(60, 40))
        self.axisactionbutton_4.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.b_axis_dro_layout.addWidget(self.axisactionbutton_4)


        self.verticalLayout_4.addLayout(self.b_axis_dro_layout)


        self.main_control_screen_layout_panel.addWidget(self.main_dro_qframe)

        self.main_override_tool_qframe = QFrame(self.centralwidget)
        self.main_override_tool_qframe.setObjectName(u"main_override_tool_qframe")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.main_override_tool_qframe.sizePolicy().hasHeightForWidth())
        self.main_override_tool_qframe.setSizePolicy(sizePolicy16)
        self.main_override_tool_qframe.setMinimumSize(QSize(370, 340))
        self.main_override_tool_qframe.setFocusPolicy(Qt.NoFocus)
        self.main_override_tool_qframe.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"padding-left: 7px;\n"
"padding-right: 7px;\n"
"}")
        self.gridLayout = QGridLayout(self.main_override_tool_qframe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(13)
        self.gridLayout.setContentsMargins(-1, 11, -1, 2)
        self.statuslabel = StatusLabel(self.main_override_tool_qframe)
        self.statuslabel.setObjectName(u"statuslabel")
        sizePolicy4.setHeightForWidth(self.statuslabel.sizePolicy().hasHeightForWidth())
        self.statuslabel.setSizePolicy(sizePolicy4)
        self.statuslabel.setMinimumSize(QSize(50, 36))
        self.statuslabel.setMaximumSize(QSize(50, 36))
        self.statuslabel.setToolTipDuration(-3)
        self.statuslabel.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel.setLineWidth(0)
        self.statuslabel.setAlignment(Qt.AlignCenter)
        self.statuslabel.setMargin(-6)
        self.statuslabel.setIndent(0)

        self.gridLayout.addWidget(self.statuslabel, 2, 1, 1, 1)

        self.actionslider_4 = ActionSlider(self.main_override_tool_qframe)
        self.actionslider_4.setObjectName(u"actionslider_4")
        self.actionslider_4.setMinimumSize(QSize(0, 50))
        self.actionslider_4.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.actionslider_4.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.actionslider_4, 5, 0, 1, 1)

        self.statuslabel_2 = StatusLabel(self.main_override_tool_qframe)
        self.statuslabel_2.setObjectName(u"statuslabel_2")
        sizePolicy4.setHeightForWidth(self.statuslabel_2.sizePolicy().hasHeightForWidth())
        self.statuslabel_2.setSizePolicy(sizePolicy4)
        self.statuslabel_2.setMinimumSize(QSize(50, 36))
        self.statuslabel_2.setMaximumSize(QSize(50, 36))
        self.statuslabel_2.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_2.setLineWidth(0)
        self.statuslabel_2.setAlignment(Qt.AlignCenter)
        self.statuslabel_2.setMargin(-6)
        self.statuslabel_2.setIndent(0)

        self.gridLayout.addWidget(self.statuslabel_2, 4, 1, 1, 1)

        self.statuslabel_3 = StatusLabel(self.main_override_tool_qframe)
        self.statuslabel_3.setObjectName(u"statuslabel_3")
        sizePolicy4.setHeightForWidth(self.statuslabel_3.sizePolicy().hasHeightForWidth())
        self.statuslabel_3.setSizePolicy(sizePolicy4)
        self.statuslabel_3.setMinimumSize(QSize(50, 36))
        self.statuslabel_3.setMaximumSize(QSize(50, 36))
        self.statuslabel_3.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_3.setLineWidth(0)
        self.statuslabel_3.setAlignment(Qt.AlignCenter)
        self.statuslabel_3.setMargin(-6)
        self.statuslabel_3.setIndent(0)

        self.gridLayout.addWidget(self.statuslabel_3, 5, 1, 1, 1)

        self.work_column_header_3 = QLabel(self.main_override_tool_qframe)
        self.work_column_header_3.setObjectName(u"work_column_header_3")
        self.work_column_header_3.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.work_column_header_3.sizePolicy().hasHeightForWidth())
        self.work_column_header_3.setSizePolicy(sizePolicy4)
        self.work_column_header_3.setMinimumSize(QSize(65, 40))
        self.work_column_header_3.setMaximumSize(QSize(65, 40))
        self.work_column_header_3.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"border-style: solid;\n"
"border-color: rgb(176, 179,172);\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(90, 90, 90);\n"
"font: 13pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.work_column_header_3.setLineWidth(0)
        self.work_column_header_3.setAlignment(Qt.AlignCenter)
        self.work_column_header_3.setWordWrap(False)
        self.work_column_header_3.setMargin(-6)
        self.work_column_header_3.setIndent(0)

        self.gridLayout.addWidget(self.work_column_header_3, 0, 2, 1, 1)

        self.loadmeter = LoadMeter(self.main_override_tool_qframe)
        self.loadmeter.setObjectName(u"loadmeter")
        self.loadmeter.setMinimumSize(QSize(0, 25))
        self.loadmeter.setMaximumSize(QSize(16777215, 25))
        self.loadmeter.setFont(font2)
        self.loadmeter.setStyleSheet(u"")
        self.loadmeter.setMaximum(150)
        self.loadmeter.setValue(150)

        self.gridLayout.addWidget(self.loadmeter, 0, 0, 1, 2)

        self.statuslabel_4 = StatusLabel(self.main_override_tool_qframe)
        self.statuslabel_4.setObjectName(u"statuslabel_4")
        sizePolicy4.setHeightForWidth(self.statuslabel_4.sizePolicy().hasHeightForWidth())
        self.statuslabel_4.setSizePolicy(sizePolicy4)
        self.statuslabel_4.setMinimumSize(QSize(50, 36))
        self.statuslabel_4.setMaximumSize(QSize(50, 36))
        self.statuslabel_4.setToolTipDuration(-1)
        self.statuslabel_4.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_4.setLineWidth(0)
        self.statuslabel_4.setAlignment(Qt.AlignCenter)
        self.statuslabel_4.setMargin(-6)
        self.statuslabel_4.setProperty(u"conv_factor", 60.000000000000000)

        self.gridLayout.addWidget(self.statuslabel_4, 1, 1, 1, 1)

        self.actionslider = ActionSlider(self.main_override_tool_qframe)
        self.actionslider.setObjectName(u"actionslider")
        self.actionslider.setMinimumSize(QSize(0, 50))
        self.actionslider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.actionslider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.actionslider, 4, 0, 1, 1)

        self.actionbutton_28 = ActionButton(self.main_override_tool_qframe)
        self.actionbutton_28.setObjectName(u"actionbutton_28")
        self.actionbutton_28.setMinimumSize(QSize(65, 40))
        self.actionbutton_28.setMaximumSize(QSize(65, 40))
        self.actionbutton_28.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.gridLayout.addWidget(self.actionbutton_28, 4, 2, 1, 1)

        self.actionslider_2 = ActionSlider(self.main_override_tool_qframe)
        self.actionslider_2.setObjectName(u"actionslider_2")
        self.actionslider_2.setMinimumSize(QSize(0, 50))
        self.actionslider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.actionslider_2.setMaximum(100)
        self.actionslider_2.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.actionslider_2, 2, 0, 1, 1)

        self.actionslider_3 = ActionSlider(self.main_override_tool_qframe)
        self.actionslider_3.setObjectName(u"actionslider_3")
        self.actionslider_3.setMinimumSize(QSize(0, 50))
        self.actionslider_3.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.actionslider_3.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.actionslider_3, 1, 0, 1, 1)

        self.actionbutton_29 = ActionButton(self.main_override_tool_qframe)
        self.actionbutton_29.setObjectName(u"actionbutton_29")
        self.actionbutton_29.setMinimumSize(QSize(65, 40))
        self.actionbutton_29.setMaximumSize(QSize(65, 40))
        self.actionbutton_29.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.gridLayout.addWidget(self.actionbutton_29, 2, 2, 1, 1)

        self.actionbutton_30 = ActionButton(self.main_override_tool_qframe)
        self.actionbutton_30.setObjectName(u"actionbutton_30")
        self.actionbutton_30.setMinimumSize(QSize(65, 40))
        self.actionbutton_30.setMaximumSize(QSize(65, 40))
        self.actionbutton_30.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.gridLayout.addWidget(self.actionbutton_30, 1, 2, 1, 1)

        self.actionbutton_31 = ActionButton(self.main_override_tool_qframe)
        self.actionbutton_31.setObjectName(u"actionbutton_31")
        self.actionbutton_31.setMinimumSize(QSize(65, 40))
        self.actionbutton_31.setMaximumSize(QSize(65, 40))
        self.actionbutton_31.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.gridLayout.addWidget(self.actionbutton_31, 5, 2, 1, 1)


        self.main_control_screen_layout_panel.addWidget(self.main_override_tool_qframe)

        self.jog_and_spindle_qframe = QFrame(self.centralwidget)
        self.jog_and_spindle_qframe.setObjectName(u"jog_and_spindle_qframe")
        sizePolicy4.setHeightForWidth(self.jog_and_spindle_qframe.sizePolicy().hasHeightForWidth())
        self.jog_and_spindle_qframe.setSizePolicy(sizePolicy4)
        self.jog_and_spindle_qframe.setMinimumSize(QSize(380, 340))
        self.jog_and_spindle_qframe.setMaximumSize(QSize(380, 16777215))
        self.jog_and_spindle_qframe.setFocusPolicy(Qt.NoFocus)
        self.jog_and_spindle_qframe.setStyleSheet(u"QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.jog_and_spindle_qframe)
        self.verticalLayout_27.setSpacing(12)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(15, 10, 15, 3)
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setSpacing(16)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.jogincrement = JogIncrementWidget(self.jog_and_spindle_qframe)
        self.jogincrement.setObjectName(u"jogincrement")
        sizePolicy12.setHeightForWidth(self.jogincrement.sizePolicy().hasHeightForWidth())
        self.jogincrement.setSizePolicy(sizePolicy12)
        self.jogincrement.setMinimumSize(QSize(0, 42))
        self.jogincrement.setMaximumSize(QSize(16777215, 42))
        self.jogincrement.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"\n"
"}\n"
"\n"
"")
        self.jogincrement.setProperty(u"diameter", 0)

        self.horizontalLayout_83.addWidget(self.jogincrement)


        self.verticalLayout_27.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setSpacing(15)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, -1, 0, -1)
        self.actionslider_5 = ActionSlider(self.jog_and_spindle_qframe)
        self.actionslider_5.setObjectName(u"actionslider_5")
        self.actionslider_5.setMinimumSize(QSize(0, 50))
        self.actionslider_5.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.actionslider_5.setMaximum(100)
        self.actionslider_5.setValue(30)
        self.actionslider_5.setOrientation(Qt.Horizontal)

        self.horizontalLayout_84.addWidget(self.actionslider_5)

        self.fr_override_dro_2 = QSpinBox(self.jog_and_spindle_qframe)
        self.fr_override_dro_2.setObjectName(u"fr_override_dro_2")
        sizePolicy4.setHeightForWidth(self.fr_override_dro_2.sizePolicy().hasHeightForWidth())
        self.fr_override_dro_2.setSizePolicy(sizePolicy4)
        self.fr_override_dro_2.setMinimumSize(QSize(48, 38))
        self.fr_override_dro_2.setMaximumSize(QSize(42, 38))
        self.fr_override_dro_2.setStyleSheet(u"QSpinBox {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.fr_override_dro_2.setAlignment(Qt.AlignCenter)
        self.fr_override_dro_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.fr_override_dro_2.setMaximum(100)
        self.fr_override_dro_2.setValue(100)

        self.horizontalLayout_84.addWidget(self.fr_override_dro_2)


        self.verticalLayout_27.addLayout(self.horizontalLayout_84)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.statuslabel_6 = StatusLabel(self.jog_and_spindle_qframe)
        self.statuslabel_6.setObjectName(u"statuslabel_6")
        sizePolicy4.setHeightForWidth(self.statuslabel_6.sizePolicy().hasHeightForWidth())
        self.statuslabel_6.setSizePolicy(sizePolicy4)
        self.statuslabel_6.setMinimumSize(QSize(105, 38))
        self.statuslabel_6.setMaximumSize(QSize(105, 38))
        self.statuslabel_6.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"	font: 50 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_85.addWidget(self.statuslabel_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_3)

        self.frame_30 = QFrame(self.jog_and_spindle_qframe)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy1.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy1)
        self.frame_30.setMaximumSize(QSize(16777215, 38))
        self.frame_30.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Plain)
        self.frame_30.setLineWidth(0)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.rpm_label_3 = QLabel(self.frame_30)
        self.rpm_label_3.setObjectName(u"rpm_label_3")
        sizePolicy17 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.rpm_label_3.sizePolicy().hasHeightForWidth())
        self.rpm_label_3.setSizePolicy(sizePolicy17)
        self.rpm_label_3.setMaximumSize(QSize(16777215, 30))
        self.rpm_label_3.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.rpm_label_3.setAlignment(Qt.AlignCenter)
        self.rpm_label_3.setWordWrap(False)
        self.rpm_label_3.setIndent(0)

        self.horizontalLayout_110.addWidget(self.rpm_label_3)

        self.rpm_label_4 = QLabel(self.frame_30)
        self.rpm_label_4.setObjectName(u"rpm_label_4")
        sizePolicy4.setHeightForWidth(self.rpm_label_4.sizePolicy().hasHeightForWidth())
        self.rpm_label_4.setSizePolicy(sizePolicy4)
        self.rpm_label_4.setMinimumSize(QSize(5, 30))
        self.rpm_label_4.setMaximumSize(QSize(5, 16777215))
        self.rpm_label_4.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.rpm_label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.rpm_label_4.setWordWrap(True)
        self.rpm_label_4.setIndent(0)

        self.horizontalLayout_110.addWidget(self.rpm_label_4)

        self.statuslabel_10 = StatusLabel(self.frame_30)
        self.statuslabel_10.setObjectName(u"statuslabel_10")
        sizePolicy17.setHeightForWidth(self.statuslabel_10.sizePolicy().hasHeightForWidth())
        self.statuslabel_10.setSizePolicy(sizePolicy17)
        self.statuslabel_10.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_10.setAlignment(Qt.AlignCenter)
        self.statuslabel_10.setIndent(0)

        self.horizontalLayout_110.addWidget(self.statuslabel_10)

        self.work_column_header_7 = QLabel(self.frame_30)
        self.work_column_header_7.setObjectName(u"work_column_header_7")
        self.work_column_header_7.setEnabled(True)
        sizePolicy17.setHeightForWidth(self.work_column_header_7.sizePolicy().hasHeightForWidth())
        self.work_column_header_7.setSizePolicy(sizePolicy17)
        self.work_column_header_7.setMaximumSize(QSize(16777215, 30))
        self.work_column_header_7.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.work_column_header_7.setAlignment(Qt.AlignCenter)
        self.work_column_header_7.setWordWrap(False)
        self.work_column_header_7.setIndent(0)

        self.horizontalLayout_110.addWidget(self.work_column_header_7)


        self.horizontalLayout_85.addWidget(self.frame_30)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_4)

        self.statuslabel_7 = StatusLabel(self.jog_and_spindle_qframe)
        self.statuslabel_7.setObjectName(u"statuslabel_7")
        sizePolicy12.setHeightForWidth(self.statuslabel_7.sizePolicy().hasHeightForWidth())
        self.statuslabel_7.setSizePolicy(sizePolicy12)
        self.statuslabel_7.setMinimumSize(QSize(105, 38))
        self.statuslabel_7.setMaximumSize(QSize(105, 38))
        self.statuslabel_7.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_85.addWidget(self.statuslabel_7)


        self.verticalLayout_27.addLayout(self.horizontalLayout_85)

        self.line_2 = QFrame(self.jog_and_spindle_qframe)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 2))
        self.line_2.setMaximumSize(QSize(16777215, 2))
        self.line_2.setStyleSheet(u"Line{\n"
"color:rgb(186, 189, 182);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(186, 189, 182);\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"}")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_27.addWidget(self.line_2)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.statuslabel_5 = StatusLabel(self.jog_and_spindle_qframe)
        self.statuslabel_5.setObjectName(u"statuslabel_5")
        sizePolicy4.setHeightForWidth(self.statuslabel_5.sizePolicy().hasHeightForWidth())
        self.statuslabel_5.setSizePolicy(sizePolicy4)
        self.statuslabel_5.setMinimumSize(QSize(105, 38))
        self.statuslabel_5.setMaximumSize(QSize(105, 38))
        self.statuslabel_5.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"	font: 50 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_87.addWidget(self.statuslabel_5)

        self.rpm_label = QLabel(self.jog_and_spindle_qframe)
        self.rpm_label.setObjectName(u"rpm_label")
        sizePolicy1.setHeightForWidth(self.rpm_label.sizePolicy().hasHeightForWidth())
        self.rpm_label.setSizePolicy(sizePolicy1)
        self.rpm_label.setMaximumSize(QSize(16777215, 38))
        self.rpm_label.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.rpm_label.setAlignment(Qt.AlignCenter)
        self.rpm_label.setWordWrap(False)
        self.rpm_label.setIndent(0)

        self.horizontalLayout_87.addWidget(self.rpm_label)

        self.statuslabel_9 = StatusLabel(self.jog_and_spindle_qframe)
        self.statuslabel_9.setObjectName(u"statuslabel_9")
        sizePolicy4.setHeightForWidth(self.statuslabel_9.sizePolicy().hasHeightForWidth())
        self.statuslabel_9.setSizePolicy(sizePolicy4)
        self.statuslabel_9.setMinimumSize(QSize(105, 38))
        self.statuslabel_9.setMaximumSize(QSize(105, 38))
        self.statuslabel_9.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.statuslabel_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_87.addWidget(self.statuslabel_9)


        self.verticalLayout_27.addLayout(self.horizontalLayout_87)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(-1, 5, -1, -1)
        self.spindle_rev_button = ActionButton(self.jog_and_spindle_qframe)
        self.spindle_rev_button.setObjectName(u"spindle_rev_button")
        sizePolicy4.setHeightForWidth(self.spindle_rev_button.sizePolicy().hasHeightForWidth())
        self.spindle_rev_button.setSizePolicy(sizePolicy4)
        self.spindle_rev_button.setMinimumSize(QSize(100, 42))
        self.spindle_rev_button.setMaximumSize(QSize(100, 42))
        self.spindle_rev_button.setFocusPolicy(Qt.NoFocus)
        self.spindle_rev_button.setStyleSheet(u"QPushButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.spindle_rev_button.setIcon(icon6)
        self.spindle_rev_button.setIconSize(QSize(18, 18))
        self.spindle_rev_button.setProperty(u"option", True)

        self.horizontalLayout_86.addWidget(self.spindle_rev_button)

        self.spindle_stop_button = ActionButton(self.jog_and_spindle_qframe)
        self.spindle_stop_button.setObjectName(u"spindle_stop_button")
        sizePolicy4.setHeightForWidth(self.spindle_stop_button.sizePolicy().hasHeightForWidth())
        self.spindle_stop_button.setSizePolicy(sizePolicy4)
        self.spindle_stop_button.setMinimumSize(QSize(90, 42))
        self.spindle_stop_button.setMaximumSize(QSize(90, 42))
        self.spindle_stop_button.setFocusPolicy(Qt.NoFocus)
        self.spindle_stop_button.setStyleSheet(u"QPushButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.spindle_stop_button.setProperty(u"option", True)

        self.horizontalLayout_86.addWidget(self.spindle_stop_button)

        self.spindle_fwd_button = ActionButton(self.jog_and_spindle_qframe)
        self.spindle_fwd_button.setObjectName(u"spindle_fwd_button")
        sizePolicy4.setHeightForWidth(self.spindle_fwd_button.sizePolicy().hasHeightForWidth())
        self.spindle_fwd_button.setSizePolicy(sizePolicy4)
        self.spindle_fwd_button.setMinimumSize(QSize(100, 42))
        self.spindle_fwd_button.setMaximumSize(QSize(100, 42))
        self.spindle_fwd_button.setFocusPolicy(Qt.NoFocus)
        self.spindle_fwd_button.setLayoutDirection(Qt.RightToLeft)
        self.spindle_fwd_button.setStyleSheet(u"QPushButton {\n"
"    text-align: right;\n"
"    padding-right: 22px;\n"
"    font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.spindle_fwd_button.setIcon(icon7)
        self.spindle_fwd_button.setIconSize(QSize(18, 18))
        self.spindle_fwd_button.setProperty(u"option", True)

        self.horizontalLayout_86.addWidget(self.spindle_fwd_button)


        self.verticalLayout_27.addLayout(self.horizontalLayout_86)


        self.main_control_screen_layout_panel.addWidget(self.jog_and_spindle_qframe)


        self.verticalLayout_31.addLayout(self.main_control_screen_layout_panel)

        Form.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(Form)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1924, 27))
        self.menuBar.setMinimumSize(QSize(0, 25))
        self.menuBar.setStyleSheet(u"QMenuBar {\n"
"color: white;\n"
"background: rgb(118, 122, 124);\n"
"font: 11pt Probe Basic Bebas Mono;\n"
"}")
        self.menuExit = QMenu(self.menuBar)
        self.menuExit.setObjectName(u"menuExit")
        self.menuRecentFiles = QMenu(self.menuExit)
        self.menuRecentFiles.setObjectName(u"menuRecentFiles")
        self.menuMachine = QMenu(self.menuBar)
        self.menuMachine.setObjectName(u"menuMachine")
        self.menuHoming = QMenu(self.menuMachine)
        self.menuHoming.setObjectName(u"menuHoming")
        self.menuCooling = QMenu(self.menuMachine)
        self.menuCooling.setObjectName(u"menuCooling")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        Form.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(Form)
        self.statusBar.setObjectName(u"statusBar")
        Form.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuExit.menuAction())
        self.menuBar.addAction(self.menuMachine.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuExit.addAction(self.actionOpen)
        self.menuExit.addAction(self.menuRecentFiles.menuAction())
        self.menuExit.addAction(self.actionReload)
        self.menuExit.addAction(self.actionClose)
        self.menuExit.addAction(self.actionSave_As)
        self.menuExit.addSeparator()
        self.menuExit.addAction(self.actionExit)
        self.menuRecentFiles.addAction(self.actionFile1)
        self.menuMachine.addAction(self.action_EmergencyStop_toggle)
        self.menuMachine.addAction(self.action_MachinePower_toggle)
        self.menuMachine.addSeparator()
        self.menuMachine.addAction(self.actionRun_Program)
        self.menuMachine.addAction(self.menuHoming.menuAction())
        self.menuMachine.addAction(self.menuCooling.menuAction())
        self.menuHoming.addAction(self.actionHome_All)
        self.menuHoming.addAction(self.actionHome_X)
        self.menuHoming.addAction(self.actionHome_Y)
        self.menuHoming.addAction(self.actionHome_Z)
        self.menuCooling.addAction(self.action_Mist_toggle)
        self.menuCooling.addAction(self.action_Flood_toggle)
        self.menuView.addAction(self.actionReport_Actual_Position)
        self.menuView.addAction(self.actionTest)

        self.retranslateUi(Form)
        self.tool_table_delete_button.clicked.connect(self.tableWidget_2.deleteSelectedTool)
        self.tool_table_reread_button.clicked.connect(self.tableWidget_2.loadToolTable)
        self.tool_table_reload_button.clicked.connect(self.tableWidget_2.loadToolTable)
        self.tool_table_add_tool_button.clicked.connect(self.tableWidget_2.insertToolBelow)
        self.x_axis_button_27.clicked.connect(self.filesystemtable.deleteFile)
        self.x_axis_button_23.clicked.connect(self.filesystemtable.goUP)
        self.x_axis_button_29.clicked.connect(self.filesystemtable.createDirectory)
        self.tool_table_save_button.clicked.connect(self.tableWidget_2.saveToolTable)
        self.x_axis_button_35.clicked.connect(self.filesystemtable_2.createDirectory)
        self.x_axis_button_33.clicked.connect(self.filesystemtable_2.deleteFile)
        self.copy_to_usb_2.clicked.connect(self.filesystemtable.doFileTransfer)
        self.copy_from_usb_2.clicked.connect(self.filesystemtable_2.doFileTransfer)
        self.x_axis_button_30.clicked.connect(self.filesystemtable_2.goUP)
        self.filesystemtable.transferFileRequest.connect(self.filesystemtable_2.transferFile)
        self.filesystemtable_2.transferFileRequest.connect(self.filesystemtable.transferFile)
        self.x_axis_button_31.clicked.connect(self.filesystemtable.newFile)
        self.x_axis_button_37.clicked.connect(self.filesystemtable_2.newFile)
        self.actionslider_5.sliderMoved.connect(self.fr_override_dro_2.setValue)
        self.x_axis_button_26.clicked.connect(self.filesystemtable.loadSelectedFile)
        self.filesystemtable.gcodeFileSelected.connect(self.x_axis_button_26.setEnabled)
        self.filesystemtable.filePreviewText.connect(self.plainTextEdit.setPlainText)
        self.filesystemtable_2.filePreviewText.connect(self.plainTextEdit.setPlainText)

        self.tabWidget.setCurrentIndex(6)
        self.tabWidget_24.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Probe Basic", None))
        self.actionExit.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.actionOpen.setText(QCoreApplication.translate("Form", u"&Open ...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("Form", u"O", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("Form", u"Close", None))
        self.actionReload.setText(QCoreApplication.translate("Form", u"&Reload", None))
#if QT_CONFIG(shortcut)
        self.actionReload.setShortcut(QCoreApplication.translate("Form", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("Form", u"Save As ...", None))
        self.actionHome_X.setText(QCoreApplication.translate("Form", u"Home &X", None))
        self.actionHome_Y.setText(QCoreApplication.translate("Form", u"Home &Y", None))
        self.actionHome_Z.setText(QCoreApplication.translate("Form", u"Home &Z", None))
        self.action_EmergencyStop_toggle.setText(QCoreApplication.translate("Form", u"Toggle E-stop", None))
#if QT_CONFIG(shortcut)
        self.action_EmergencyStop_toggle.setShortcut(QCoreApplication.translate("Form", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.action_MachinePower_toggle.setText(QCoreApplication.translate("Form", u"Machine Power", None))
#if QT_CONFIG(shortcut)
        self.action_MachinePower_toggle.setShortcut(QCoreApplication.translate("Form", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.actionHome_All.setText(QCoreApplication.translate("Form", u"Home All", None))
        self.actionRun_Program.setText(QCoreApplication.translate("Form", u"Run Program", None))
#if QT_CONFIG(shortcut)
        self.actionRun_Program.setShortcut(QCoreApplication.translate("Form", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.actionFile1.setText(QCoreApplication.translate("Form", u"File1", None))
        self.actionReport_Actual_Position.setText(QCoreApplication.translate("Form", u"Report Actual Position", None))
        self.actionTest.setText(QCoreApplication.translate("Form", u"Test", None))
        self.action_Mist_toggle.setText(QCoreApplication.translate("Form", u"Mist On", None))
#if QT_CONFIG(shortcut)
        self.action_Mist_toggle.setShortcut(QCoreApplication.translate("Form", u"F7", None))
#endif // QT_CONFIG(shortcut)
        self.action_Flood_toggle.setText(QCoreApplication.translate("Form", u"Flood On", None))
#if QT_CONFIG(shortcut)
        self.action_Flood_toggle.setShortcut(QCoreApplication.translate("Form", u"F8", None))
#endif // QT_CONFIG(shortcut)
        self.recentfilecombobox.setProperty(u"resource", "")
        self.mdi_entry_box.setPlaceholderText(QCoreApplication.translate("Form", u"MDI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"          MAIN          ", None))
        self.x_axis_button_30.setText(QCoreApplication.translate("Form", u"  FOLDER UP", None))
        self.x_axis_button_32.setText(QCoreApplication.translate("Form", u"EJECT USB", None))
        self.x_axis_button_33.setText(QCoreApplication.translate("Form", u" DELETE", None))
        self.x_axis_button_37.setText(QCoreApplication.translate("Form", u" NEW FILE", None))
        self.x_axis_button_35.setText(QCoreApplication.translate("Form", u" NEW FOLDER", None))
        self.x_axis_button_34.setText(QCoreApplication.translate("Form", u"RENAME", None))
        self.copy_from_usb_2.setText(QCoreApplication.translate("Form", u"COPY\n"
"FROM\n"
"  USB", None))
        self.copy_to_usb_2.setText(QCoreApplication.translate("Form", u"COPY\n"
"TO\n"
"USB", None))
        self.x_axis_button_23.setText(QCoreApplication.translate("Form", u"  FOLDER UP", None))
        self.x_axis_button_26.setText(QCoreApplication.translate("Form", u"LOAD G-CODE", None))
        self.x_axis_button_27.setText(QCoreApplication.translate("Form", u" DELETE", None))
        self.x_axis_button_31.setText(QCoreApplication.translate("Form", u" NEW FILE", None))
        self.x_axis_button_29.setText(QCoreApplication.translate("Form", u" NEW FOLDER", None))
        self.x_axis_button_28.setText(QCoreApplication.translate("Form", u"RENAME", None))
        self.work_column_header_8.setText(QCoreApplication.translate("Form", u"G-CODE FILE PREVIEW", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Select a text file to preview", None))
        self.x_axis_button_36.setText(QCoreApplication.translate("Form", u"EDIT G-CODE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), QCoreApplication.translate("Form", u"          FILE          ", None))
        self.machine_column_header_9.setText(QCoreApplication.translate("Form", u"ATC MANUAL CONTROL PANEL", None))
        self.m01_break_button_4.setText(QCoreApplication.translate("Form", u"INSERT", None))
        self.m01_break_button_8.setText(QCoreApplication.translate("Form", u"DELETE ALL", None))
        self.m01_break_button_9.setText(QCoreApplication.translate("Form", u"DELETE", None))
        self.subcallbutton_9.setText(QCoreApplication.translate("Form", u" ATC REV", None))
        self.subcallbutton_9.setProperty(u"sub_name", QCoreApplication.translate("Form", u"m11.ngc", None))
        self.subcallbutton_3.setText(QCoreApplication.translate("Form", u" ATC FWD ", None))
        self.subcallbutton_3.setProperty(u"sub_name", QCoreApplication.translate("Form", u"m12.ngc", None))
        self.subcallbutton_10.setText(QCoreApplication.translate("Form", u" ATC RETRACT", None))
        self.subcallbutton_10.setProperty(u"sub_name", QCoreApplication.translate("Form", u"retractatc.ngc", None))
        self.subcallbutton_11.setText(QCoreApplication.translate("Form", u" ATC EXTEND ", None))
        self.subcallbutton_11.setProperty(u"sub_name", QCoreApplication.translate("Form", u"extendatc.ngc", None))
        self.subcallbutton_12.setText(QCoreApplication.translate("Form", u"DRAWBAR LOOSE", None))
        self.subcallbutton_12.setProperty(u"sub_name", QCoreApplication.translate("Form", u"unclamptool.ngc", None))
        self.subcallbutton_13.setText(QCoreApplication.translate("Form", u"DRAWBAR TIGHT", None))
        self.subcallbutton_13.setProperty(u"sub_name", QCoreApplication.translate("Form", u"clamptool.ngc", None))
        self.m01_break_button_10.setText(QCoreApplication.translate("Form", u"SET TC POSITION", None))
        self.m01_break_button_27.setText(QCoreApplication.translate("Form", u"AIR BLAST", None))
        self.subcallbutton_14.setText(QCoreApplication.translate("Form", u"REF CAROUSEL", None))
        self.subcallbutton_14.setProperty(u"sub_name", QCoreApplication.translate("Form", u"m13.ngc", None))
        self.m01_break_button_14.setText(QCoreApplication.translate("Form", u"+ +", None))
        self.m01_break_button_15.setText(QCoreApplication.translate("Form", u"- -", None))
        self.mdi_entry_box_3.setPlaceholderText(QCoreApplication.translate("Form", u"MDI", None))
        self.label_53.setText("")
        self.label_60.setText(QCoreApplication.translate("Form", u"P9", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"T5", None))
        self.label_67.setText(QCoreApplication.translate("Form", u"T2", None))
        self.label_68.setText(QCoreApplication.translate("Form", u"T8", None))
        self.label_69.setText(QCoreApplication.translate("Form", u"P2", None))
        self.label_70.setText(QCoreApplication.translate("Form", u"P3", None))
        self.label_71.setText(QCoreApplication.translate("Form", u"T10", None))
        self.label_72.setText(QCoreApplication.translate("Form", u"P11", None))
        self.label_73.setText(QCoreApplication.translate("Form", u"T4", None))
        self.label_74.setText(QCoreApplication.translate("Form", u"P5", None))
        self.label_75.setText(QCoreApplication.translate("Form", u"P1", None))
        self.label_76.setText(QCoreApplication.translate("Form", u"P6", None))
        self.label_77.setText(QCoreApplication.translate("Form", u"T3", None))
        self.label_78.setText(QCoreApplication.translate("Form", u"T1", None))
        self.label_79.setText(QCoreApplication.translate("Form", u"T6", None))
        self.label_80.setText(QCoreApplication.translate("Form", u"P4", None))
        self.label_81.setText(QCoreApplication.translate("Form", u"T9", None))
        self.label_82.setText(QCoreApplication.translate("Form", u"P8", None))
        self.label_83.setText(QCoreApplication.translate("Form", u"T11", None))
        self.label_84.setText(QCoreApplication.translate("Form", u"P7", None))
        self.label_85.setText(QCoreApplication.translate("Form", u"T12", None))
        self.label_86.setText(QCoreApplication.translate("Form", u"P10", None))
        self.label_87.setText(QCoreApplication.translate("Form", u"P12", None))
        self.label_88.setText(QCoreApplication.translate("Form", u"T7", None))
        self.label_89.setText("")
        self.tool_length_8.setText(QCoreApplication.translate("Form", u"T0", None))
        self.tool_length_8.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:tool_in_spindle?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"'T' + ch[0]\", \"name\": \"current tool\"}]", None))
        self.tool_length_8.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_length_8.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.label_38.setText("")
        self.machine_column_header_3.setText(QCoreApplication.translate("Form", u"ATC AUTOMATIC CONTROL PANEL", None))
        self.load_spindle_tool_number.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.load_current_tool.setText(QCoreApplication.translate("Form", u"LOAD SPINDLE", None))
        self.load_current_tool.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.load_current_tool.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"M61 Q#<load_spindle_tool_number>", None))
        self.remove_current_tool.setText(QCoreApplication.translate("Form", u"UNLOAD SPINDLE", None))
        self.remove_current_tool.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.remove_current_tool.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"M61 Q0 G49", None))
        self.subcallbutton_15.setText(QCoreApplication.translate("Form", u" ATC REV", None))
        self.subcallbutton_15.setProperty(u"sub_name", QCoreApplication.translate("Form", u"m11.ngc", None))
        self.subcallbutton_4.setText(QCoreApplication.translate("Form", u" ATC FWD ", None))
        self.subcallbutton_4.setProperty(u"sub_name", QCoreApplication.translate("Form", u"m12.ngc", None))
        self.store_current_tool.setText(QCoreApplication.translate("Form", u"STORE CURRENT TOOL", None))
        self.store_current_tool.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.store_current_tool.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"M6 T0", None))
        self.machine_column_header_2.setText(QCoreApplication.translate("Form", u"ELECTRONIC TOOL SETTER", None))
        self.m01_break_button_24.setText(QCoreApplication.translate("Form", u"TOUCH OFF ENTIRE CAROUSEL", None))
        self.m01_break_button_25.setText(QCoreApplication.translate("Form", u"TOUCH OFF CURRENT TOOL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.status_tab), QCoreApplication.translate("Form", u"          ATC          ", None))
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"OFFSET", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"X", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Y", None));
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Z", None));
        ___qtablewidgetitem4 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"A", None));
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"B", None));
        ___qtablewidgetitem6 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem7 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem8 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem9 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem10 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"5", None));
        ___qtablewidgetitem11 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"6", None));
        ___qtablewidgetitem12 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"7", None));
        ___qtablewidgetitem13 = self.tableWidget_3.verticalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"8", None));
        ___qtablewidgetitem14 = self.tableWidget_3.verticalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"9", None));

        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem15 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"G54", None));
        ___qtablewidgetitem16 = self.tableWidget_3.item(0, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem17 = self.tableWidget_3.item(0, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem18 = self.tableWidget_3.item(0, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem19 = self.tableWidget_3.item(0, 4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem20 = self.tableWidget_3.item(0, 5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem21 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"G55", None));
        ___qtablewidgetitem22 = self.tableWidget_3.item(1, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem23 = self.tableWidget_3.item(1, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem24 = self.tableWidget_3.item(1, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem25 = self.tableWidget_3.item(1, 4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem26 = self.tableWidget_3.item(1, 5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem27 = self.tableWidget_3.item(2, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form", u"G56", None));
        ___qtablewidgetitem28 = self.tableWidget_3.item(2, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem29 = self.tableWidget_3.item(2, 2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem30 = self.tableWidget_3.item(2, 3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem31 = self.tableWidget_3.item(2, 4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem32 = self.tableWidget_3.item(2, 5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem33 = self.tableWidget_3.item(3, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Form", u"G57", None));
        ___qtablewidgetitem34 = self.tableWidget_3.item(3, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem35 = self.tableWidget_3.item(3, 2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem36 = self.tableWidget_3.item(3, 3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem37 = self.tableWidget_3.item(3, 4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem38 = self.tableWidget_3.item(3, 5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem39 = self.tableWidget_3.item(4, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Form", u"G58", None));
        ___qtablewidgetitem40 = self.tableWidget_3.item(4, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem41 = self.tableWidget_3.item(4, 2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem42 = self.tableWidget_3.item(4, 3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem43 = self.tableWidget_3.item(4, 4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem44 = self.tableWidget_3.item(4, 5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem45 = self.tableWidget_3.item(5, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Form", u"G59", None));
        ___qtablewidgetitem46 = self.tableWidget_3.item(5, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem47 = self.tableWidget_3.item(5, 2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem48 = self.tableWidget_3.item(5, 3)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem49 = self.tableWidget_3.item(5, 4)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem50 = self.tableWidget_3.item(5, 5)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem51 = self.tableWidget_3.item(6, 0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Form", u"G59.1", None));
        ___qtablewidgetitem52 = self.tableWidget_3.item(6, 1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem53 = self.tableWidget_3.item(6, 2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem54 = self.tableWidget_3.item(6, 3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem55 = self.tableWidget_3.item(6, 4)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem56 = self.tableWidget_3.item(6, 5)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem57 = self.tableWidget_3.item(7, 0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("Form", u"G59.2", None));
        ___qtablewidgetitem58 = self.tableWidget_3.item(7, 1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem59 = self.tableWidget_3.item(7, 2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem60 = self.tableWidget_3.item(7, 3)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem61 = self.tableWidget_3.item(7, 4)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem62 = self.tableWidget_3.item(7, 5)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem63 = self.tableWidget_3.item(8, 0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("Form", u"G59.3", None));
        ___qtablewidgetitem64 = self.tableWidget_3.item(8, 1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem65 = self.tableWidget_3.item(8, 2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem66 = self.tableWidget_3.item(8, 3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem67 = self.tableWidget_3.item(8, 4)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("Form", u"0.0000", None));
        ___qtablewidgetitem68 = self.tableWidget_3.item(8, 5)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("Form", u"0.0000", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)

        self.x_axis_button_10.setText(QCoreApplication.translate("Form", u"CLEAR", None))
        self.x_axis_button_12.setText(QCoreApplication.translate("Form", u"RE-READ", None))
        self.x_axis_button_13.setText(QCoreApplication.translate("Form", u"SAVE TABLE", None))
        self.x_axis_button_14.setText(QCoreApplication.translate("Form", u"RELOAD TABLE", None))
        self.mdi_entry_box_6.setPlaceholderText(QCoreApplication.translate("Form", u"MDI", None))
        self.machine_column_header_4.setText(QCoreApplication.translate("Form", u"WORK COORDINATE OFFSETS", None))
        self.actionbutton_g54_2.setText(QCoreApplication.translate("Form", u"G54", None))
        self.actionbutton_g54_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G54", None))
        self.actionbutton_g55_2.setText(QCoreApplication.translate("Form", u"G55", None))
        self.actionbutton_g55_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G55", None))
        self.actionbutton_g56_2.setText(QCoreApplication.translate("Form", u"G56", None))
        self.actionbutton_g56_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G56", None))
        self.actionbutton_g57_2.setText(QCoreApplication.translate("Form", u"G57", None))
        self.actionbutton_g57_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G57", None))
        self.actionbutton_g58_2.setText(QCoreApplication.translate("Form", u"G58", None))
        self.actionbutton_g58_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G58", None))
        self.actionbutton_g59_4.setText(QCoreApplication.translate("Form", u"G59", None))
        self.actionbutton_g59_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59", None))
        self.actionbutton_g59_5.setText(QCoreApplication.translate("Form", u"G59.1", None))
        self.actionbutton_g59_5.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.1", None))
        self.actionbutton_g59_6.setText(QCoreApplication.translate("Form", u"G59.2", None))
        self.actionbutton_g59_6.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.2", None))
        self.actionbutton_g59_7.setText(QCoreApplication.translate("Form", u"G59.3", None))
        self.actionbutton_g59_7.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.3", None))
        self.axis_column_header_9.setText(QCoreApplication.translate("Form", u"SET TO ZERO", None))
        self.axis_column_header_10.setText(QCoreApplication.translate("Form", u"AXIS", None))
        self.machine_column_header_10.setText(QCoreApplication.translate("Form", u"WC CURRENT POSITION", None))
        self.machine_column_header_11.setText(QCoreApplication.translate("Form", u"MACHINE\n"
"COORDS", None))
        self.machine_column_header_12.setText(QCoreApplication.translate("Form", u"WC\n"
"OFFSET", None))
        self.ref_coilumn_header_4.setText(QCoreApplication.translate("Form", u"G52/G92\n"
"OFFSET", None))
        self.machine_column_header_13.setText(QCoreApplication.translate("Form", u"TOOL\n"
"OFFSET", None))
        self.zero_x_button_2.setText(QCoreApplication.translate("Form", u"ZERO", None))
        self.zero_x_button_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_x_button_2.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G10 L20 P{ch[0]} X0.0", None))
        self.axis_column_header_11.setText(QCoreApplication.translate("Form", u"X", None))
        self.statuslabel_50.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_51.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:position\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_52.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_53.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_54.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]", None))
        self.zero_y_button_2.setText(QCoreApplication.translate("Form", u"ZERO", None))
        self.zero_y_button_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_y_button_2.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G10 L20 P{ch[0]} Y0.0", None))
        self.axis_column_header_12.setText(QCoreApplication.translate("Form", u"Y", None))
        self.statuslabel_55.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_56.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:position\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_57.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_58.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_59.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]", None))
        self.zero_z_button_2.setText(QCoreApplication.translate("Form", u"ZERO", None))
        self.zero_z_button_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_z_button_2.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G10 L20 P{ch[0]} Z0.0", None))
        self.axis_column_header_13.setText(QCoreApplication.translate("Form", u"Z", None))
        self.statuslabel_60.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_61.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:position\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_62.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_63.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_64.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:tool_offset\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"tool offset\"}]", None))
        self.zero_a_button_2.setText(QCoreApplication.translate("Form", u"ZERO", None))
        self.zero_a_button_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_a_button_2.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G10 L2 P{ch[0]} A0.0", None))
        self.axis_column_header_14.setText(QCoreApplication.translate("Form", u"A", None))
        self.statuslabel_65.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_66.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:position\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_67.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_68.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_69.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]", None))
        self.zero_b_button_2.setText(QCoreApplication.translate("Form", u"ZERO", None))
        self.zero_b_button_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_b_button_2.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G10 L2 P{ch[0]} B0.0", None))
        self.axis_column_header_15.setText(QCoreApplication.translate("Form", u"B", None))
        self.statuslabel_70.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_71.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:position\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_72.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_73.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4])\", \"name\": \"New Rule\"}]", None))
        self.statuslabel_74.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4])\", \"name\": \"New Rule\"}]", None))
        self.label_47.setText("")
        self.label_51.setText("")
        self.set_tool_touch_off_position_button_2.setText(QCoreApplication.translate("Form", u"SET TOOL TOUCH OFF POSITION", None))
        self.set_tool_touch_off_position_button_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:gcodes\", \"trigger\": true}], \"property\": \"None\", \"expression\": \"\", \"name\": \"set tool touch off position\"}]", None))
        self.set_tool_touch_off_position_button_2.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G30.1", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"X :", None))
        self.tool_length_2.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_length_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.3f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]", None))
        self.tool_length_2.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_length_2.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"Y :", None))
        self.tool_length_4.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_length_4.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.3f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]", None))
        self.tool_length_4.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_length_4.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"Z :", None))
        self.tool_length_3.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_length_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.3f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]", None))
        self.tool_length_3.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_length_3.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_16), QCoreApplication.translate("Form", u"        OFFSETS        ", None))
        self.tool_table_delete_button.setText(QCoreApplication.translate("Form", u"DELETE", None))
        self.tool_table_add_tool_button.setText(QCoreApplication.translate("Form", u"ADD TOOL", None))
        self.tool_table_reread_button.setText(QCoreApplication.translate("Form", u"RE-READ", None))
        self.tool_table_save_button.setText(QCoreApplication.translate("Form", u"SAVE TABLE", None))
        self.tool_table_reload_button.setText(QCoreApplication.translate("Form", u"RELOAD TABLE", None))
        self.label_43.setText("")
        self.label_48.setText(QCoreApplication.translate("Form", u"TOOL LENGTH", None))
        self.tool_length_5.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_length_5.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]", None))
        self.tool_length_5.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_length_5.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"DIAM", None))
        self.tool_diameter_2.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_diameter_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?diameter\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Diameter\"}]", None))
        self.tool_diameter_2.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_diameter_2.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"COMMENT", None))
        self.tool_length_7.setText(QCoreApplication.translate("Form", u"No Tool Loaded", None))
        self.tool_length_7.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?comment\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Tool Comment\"}]", None))
        self.tool_length_7.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_length_7.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.mdi_entry_box_4.setPlaceholderText(QCoreApplication.translate("Form", u"MDI", None))
        self.tool_length_6.setText(QCoreApplication.translate("Form", u"T0", None))
        self.tool_length_6.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:tool_in_spindle?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"'T' + ch[0]\", \"name\": \"current tool\"}]", None))
        self.tool_length_6.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_length_6.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tooling_tab), QCoreApplication.translate("Form", u"          TOOL          ", None))
        self.label_24.setText(QCoreApplication.translate("Form", u" WORK OFFSETS", None))
        self.actionbutton_11.setText(QCoreApplication.translate("Form", u"G54", None))
        self.actionbutton_11.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G54", None))
        self.actionbutton_14.setText(QCoreApplication.translate("Form", u"G55", None))
        self.actionbutton_14.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G55", None))
        self.actionbutton_15.setText(QCoreApplication.translate("Form", u"G56", None))
        self.actionbutton_15.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G56", None))
        self.actionbutton_17.setText(QCoreApplication.translate("Form", u"G59", None))
        self.actionbutton_17.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59", None))
        self.actionbutton_16.setText(QCoreApplication.translate("Form", u"G59.3", None))
        self.actionbutton_16.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.3", None))
        self.actionbutton_12.setText(QCoreApplication.translate("Form", u"G58", None))
        self.actionbutton_12.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G58", None))
        self.actionbutton_13.setText(QCoreApplication.translate("Form", u"G59.2", None))
        self.actionbutton_13.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.2", None))
        self.actionbutton_4.setText(QCoreApplication.translate("Form", u"G57", None))
        self.actionbutton_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G57", None))
        self.actionbutton_18.setText(QCoreApplication.translate("Form", u"G59.1", None))
        self.actionbutton_18.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.1", None))
        self.label_23.setText(QCoreApplication.translate("Form", u" Probing Parameters", None))
        self.ref_coilumn_header_12.setText("")
        self.label_22.setText(QCoreApplication.translate("Form", u"Probe Tool #:", None))
        self.probe_tool_number.setText(QCoreApplication.translate("Form", u"99", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Step Off Width:", None))
        self.step_off_width.setText(QCoreApplication.translate("Form", u"0.5000", None))
        self.ref_coilumn_header_11.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Probe Fast FR:", None))
        self.probe_fast_fr.setInputMask("")
        self.probe_fast_fr.setText(QCoreApplication.translate("Form", u"30.0", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Probe Slow FR:", None))
        self.probe_slow_fr.setText(QCoreApplication.translate("Form", u"5.0", None))
        self.ref_coilumn_header_10.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Max X/Y Distance:", None))
        self.max_xy_distance.setText(QCoreApplication.translate("Form", u"1.0000", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"X/Y Clearance:", None))
        self.xy_clearance.setText(QCoreApplication.translate("Form", u"0.1000", None))
        self.ref_coilumn_header_9.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"Max Z Distance:", None))
        self.max_z_distance.setText(QCoreApplication.translate("Form", u"1.0000", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Z Clearance:", None))
        self.z_clearance.setText(QCoreApplication.translate("Form", u"0.1000", None))
        self.ref_coilumn_header_8.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"Extra Probe Depth:", None))
        self.extra_probe_depth.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Calibration Dia:", None))
        self.calibration_dia.setText(QCoreApplication.translate("Form", u"0.1500", None))
        self.ref_coilumn_header_7.setText("")
        self.label_54.setText(QCoreApplication.translate("Form", u"EDGE WIDTH:", None))
        self.step_off_width_2.setText(QCoreApplication.translate("Form", u"0.5000", None))
        self.label_25.setText(QCoreApplication.translate("Form", u" Probe Results", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"EDGE ANGLE:", None))
        self.probed_diameter_2.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"X Width:", None))
        self.x_probed_width.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"X Probed Pos:", None))
        self.x_probed_pos.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"EDGE DELTA:", None))
        self.x_probed_width_2.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Y Width:", None))
        self.probed_diameter.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Y Probed Pos:", None))
        self.z_probed_pos.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.ref_coilumn_header.setText("")
        self.label_50.setText(QCoreApplication.translate("Form", u"DIAM:", None))
        self.y_probed_width.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Z Probed Pos:", None))
        self.y_probed_pos.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.mdi_entry_box_2.setPlaceholderText(QCoreApplication.translate("Form", u"MDI", None))
        self.pushButton_10.setText("")
        self.pushButton_10.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_14.setText("")
        self.pushButton_14.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_12.setText("")
        self.pushButton_12.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_13.setText("")
        self.pushButton_13.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_11.setText("")
        self.pushButton_11.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_15.setText("")
        self.pushButton_15.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_17.setText("")
        self.pushButton_17.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_18.setText("")
        self.pushButton_18.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.probe_front_left_top_corner.setProperty(u"sub_name", QCoreApplication.translate("Form", u"probe_front_left_top_corner", None))
        self.probe_front_left_top_corner.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.label_36.setText("")
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.outside_corners_tab), QCoreApplication.translate("Form", u"        OUTSIDE CORNERS        ", None))
        self.pushButton_19.setText("")
        self.pushButton_19.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_25.setText("")
        self.pushButton_25.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_22.setText("")
        self.pushButton_22.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_21.setText("")
        self.pushButton_21.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_20.setText("")
        self.pushButton_20.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_24.setText("")
        self.pushButton_24.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_23.setText("")
        self.pushButton_23.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_26.setText("")
        self.pushButton_26.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_27.setText("")
        self.pushButton_27.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.label_35.setText("")
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.inside_corners_tab), QCoreApplication.translate("Form", u"       INSIDE CORNERS       ", None))
        self.pushButton_35.setText("")
        self.pushButton_35.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_33.setText("")
        self.pushButton_33.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_34.setText("")
        self.pushButton_34.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_32.setText("")
        self.pushButton_32.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.step_increment_label_4.setText(QCoreApplication.translate("Form", u"HINT", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"dIAMETER:", None))
        self.diameter_hint_2.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"X :", None))
        self.x_hint_2.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Y :", None))
        self.y_hint_2.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_31.setText("")
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.boss_and_pocket_tab), QCoreApplication.translate("Form", u"       BOSS AND POCKETS       ", None))
        self.pushButton_36.setText("")
        self.pushButton_36.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_39.setText("")
        self.pushButton_39.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_37.setText("")
        self.pushButton_37.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.pushButton_38.setText("")
        self.pushButton_38.setProperty(u"styleClass", QCoreApplication.translate("Form", u"probeButton", None))
        self.step_increment_label_5.setText(QCoreApplication.translate("Form", u"HINT", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"X :", None))
        self.x_hint_3.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"Y :", None))
        self.y_hint_3.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_37.setText("")
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.valley_and_ridge_tab), QCoreApplication.translate("Form", u"       VALLEYS AND RIDGES       ", None))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.rotary_axis_tab), QCoreApplication.translate("Form", u"       ROTARY AXIS         ", None))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.multi_axis_tab), QCoreApplication.translate("Form", u"        MULTI-AXIS         ", None))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.tab_7), QCoreApplication.translate("Form", u"         CALIBRATE         ", None))
        self.label.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("Form", u"     STEP OFF WIDTH     ", None))
        self.label_2.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("Form", u"     EXTRA PROBE DEPTH     ", None))
        self.label_3.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("Form", u"     MAX DISTANCE     ", None))
        self.label_4.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("Form", u"     CLEARANCE     ", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), QCoreApplication.translate("Form", u"     PROBE FAST FR     ", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("Form", u"     PROBE SLOW FR     ", None))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.probe_help_tab), QCoreApplication.translate("Form", u"        PROBE HELP        ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.probing_tab), QCoreApplication.translate("Form", u"          PROBING          ", None))
        self.pushButton_40.setText(QCoreApplication.translate("Form", u"`", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_28.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_29.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_30.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_31.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_41.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_42.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_43.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_44.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_45.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_46.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_47.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_48.setText(QCoreApplication.translate("Form", u"BACK", None))
        self.pushButton_85.setText(QCoreApplication.translate("Form", u"INSERT", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_49.setText(QCoreApplication.translate("Form", u"\u00f7", None))
        self.pushButton_50.setText(QCoreApplication.translate("Form", u"TAB", None))
        self.pushButton_51.setText(QCoreApplication.translate("Form", u"Q", None))
        self.pushButton_52.setText(QCoreApplication.translate("Form", u"W", None))
        self.pushButton_53.setText(QCoreApplication.translate("Form", u"E", None))
        self.pushButton_54.setText(QCoreApplication.translate("Form", u"R", None))
        self.pushButton_55.setText(QCoreApplication.translate("Form", u"T", None))
        self.pushButton_56.setText(QCoreApplication.translate("Form", u"Y", None))
        self.pushButton_57.setText(QCoreApplication.translate("Form", u"U", None))
        self.pushButton_58.setText(QCoreApplication.translate("Form", u"I", None))
        self.pushButton_59.setText(QCoreApplication.translate("Form", u"O", None))
        self.pushButton_60.setText(QCoreApplication.translate("Form", u"P", None))
        self.pushButton_61.setText(QCoreApplication.translate("Form", u"[", None))
        self.pushButton_62.setText(QCoreApplication.translate("Form", u"]", None))
        self.pushButton_63.setText(QCoreApplication.translate("Form", u"\\", None))
        self.pushButton_79.setText(QCoreApplication.translate("Form", u"DEL", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_64.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.pushButton_65.setText(QCoreApplication.translate("Form", u"CAPS", None))
        self.pushButton_66.setText(QCoreApplication.translate("Form", u"A", None))
        self.pushButton_67.setText(QCoreApplication.translate("Form", u"S", None))
        self.pushButton_68.setText(QCoreApplication.translate("Form", u"D", None))
        self.pushButton_69.setText(QCoreApplication.translate("Form", u"F", None))
        self.pushButton_70.setText(QCoreApplication.translate("Form", u"G", None))
        self.pushButton_71.setText(QCoreApplication.translate("Form", u"H", None))
        self.pushButton_72.setText(QCoreApplication.translate("Form", u"J", None))
        self.pushButton_73.setText(QCoreApplication.translate("Form", u"K", None))
        self.pushButton_74.setText(QCoreApplication.translate("Form", u"L", None))
        self.pushButton_75.setText(QCoreApplication.translate("Form", u";", None))
        self.pushButton_76.setText(QCoreApplication.translate("Form", u"'", None))
        self.pushButton_77.setText(QCoreApplication.translate("Form", u"ENTER", None))
        self.pushButton_83.setText(QCoreApplication.translate("Form", u"HOME", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_78.setText(QCoreApplication.translate("Form", u"\u2212", None))
        self.pushButton_80.setText(QCoreApplication.translate("Form", u"SHIFT", None))
        self.pushButton_81.setText(QCoreApplication.translate("Form", u"Z", None))
        self.pushButton_82.setText(QCoreApplication.translate("Form", u"X", None))
        self.pushButton_84.setText(QCoreApplication.translate("Form", u"C", None))
        self.pushButton_86.setText(QCoreApplication.translate("Form", u"V", None))
        self.pushButton_87.setText(QCoreApplication.translate("Form", u"B", None))
        self.pushButton_88.setText(QCoreApplication.translate("Form", u"N", None))
        self.pushButton_89.setText(QCoreApplication.translate("Form", u"M", None))
        self.pushButton_90.setText(QCoreApplication.translate("Form", u",", None))
        self.pushButton_91.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_92.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_93.setText(QCoreApplication.translate("Form", u"shift", None))
        self.pushButton_94.setText("")
        self.pushButton_95.setText(QCoreApplication.translate("Form", u"END", None))
        self.pushButton_96.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_97.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_98.setText("")
        self.pushButton_99.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_100.setText(QCoreApplication.translate("Form", u"CTRL", None))
        self.pushButton_101.setText(QCoreApplication.translate("Form", u"ALT", None))
        self.pushButton_102.setText("")
        self.pushButton_103.setText(QCoreApplication.translate("Form", u"FN", None))
        self.pushButton_104.setText(QCoreApplication.translate("Form", u"CTRL", None))
        self.pushButton_105.setText("")
        self.pushButton_106.setText("")
        self.pushButton_107.setText("")
        self.pushButton_108.setText(QCoreApplication.translate("Form", u"CANCEL", None))
        self.pushButton_109.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Probe Basic Bebas Mono\";\n"
"}", None))
        self.pushButton_109.setText(QCoreApplication.translate("Form", u"in/mm", None))
        self.pushButton_110.setText(QCoreApplication.translate("Form", u"ENTER", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"          CONVERSATIONAL          ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"          SETTINGS           ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("Form", u"          STATUS           ", None))
        self.z_plus_jogbutton.setText("")
        self.z_plus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,pos", None))
        self.z_minus_jogbutton.setText("")
        self.z_minus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,neg", None))
        self.x_plus_jogbutton.setText("")
        self.x_plus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,pos", None))
        self.x_minus_jogbutton.setText("")
        self.x_minus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,neg", None))
        self.y_minus_jogbutton.setText("")
        self.y_minus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,neg", None))
        self.y_plus_jogbutton.setText("")
        self.y_plus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,pos", None))
        self.a_minus_jogbutton.setText("")
        self.a_minus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:a,neg", None))
        self.a_plus_jogbutton.setText("")
        self.a_plus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:a,pos", None))
        self.b_minus_jogbutton.setText("")
        self.b_minus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:b,neg", None))
        self.b_plus_jogbutton.setText("")
        self.b_plus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:b,pos", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"MACHINE STATUS:", None))
        self.statuslabel_15.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"str\", \"url\": \"status:gcodes?text\"}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Active Codes\"}]", None))
        self.statuslabel_15.setProperty(u"statusItem", "")
        self.statuslabel_16.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"str\", \"url\": \"status:mcodes?text\"}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Active Mcodes\"}]", None))
        self.statuslabel_16.setProperty(u"statusItem", "")
        self.tabWidget_24.setTabText(self.tabWidget_24.indexOf(self.tabWidget_24Page1), QCoreApplication.translate("Form", u"     JOG CONTROL     ", None))
        self.statuslabel_13.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"str\", \"url\": \"status:gcodes?text\"}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Active Codes\"}]", None))
        self.statuslabel_13.setProperty(u"statusItem", "")
        self.statuslabel_14.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"str\", \"url\": \"status:mcodes?text\"}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Active Mcodes\"}]", None))
        self.statuslabel_14.setProperty(u"statusItem", "")
        self.label_19.setText(QCoreApplication.translate("Form", u"MACHINE STATUS:", None))
        self.tabWidget_24.setTabText(self.tabWidget_24.indexOf(self.tab_17), QCoreApplication.translate("Form", u"       CUSTOM       ", None))
        self.actionbutton_3.setText(QCoreApplication.translate("Form", u"CYCLE START", None))
        self.actionbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"program.run", None))
        self.actionbutton_7.setText(QCoreApplication.translate("Form", u"RUN FM HERE", None))
        self.actionbutton_7.setProperty(u"actionName", QCoreApplication.translate("Form", u"program.run-from-line", None))
        self.ref_coilumn_header_13.setText("")
        self.actionbutton_10.setText(QCoreApplication.translate("Form", u"FEED HOLD", None))
        self.actionbutton_10.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 'Paused'\", \"name\": \"check when paused\"}]", None))
        self.actionbutton_10.setProperty(u"actionName", QCoreApplication.translate("Form", u"program.pause", None))
        self.actionbutton.setText(QCoreApplication.translate("Form", u"SINGLE BLOCK", None))
        self.actionbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"program.step", None))
        self.ref_coilumn_header_14.setText("")
        self.actionbutton_5.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.actionbutton_5.setProperty(u"actionName", QCoreApplication.translate("Form", u"program.abort", None))
        self.actionbutton_9.setText(QCoreApplication.translate("Form", u"Flood", None))
        self.actionbutton_9.setProperty(u"actionName", QCoreApplication.translate("Form", u"coolant.flood.toggle", None))
        self.ref_coilumn_header_15.setText("")
        self.actionbutton_6.setText(QCoreApplication.translate("Form", u"BLOCK DELETE", None))
        self.actionbutton_6.setProperty(u"actionName", QCoreApplication.translate("Form", u"program.block-delete.toggle", None))
        self.actionbutton_8.setText(QCoreApplication.translate("Form", u"Mist", None))
        self.actionbutton_8.setProperty(u"actionName", QCoreApplication.translate("Form", u"coolant.mist.toggle", None))
        self.ref_coilumn_header_17.setText("")
        self.actionbutton_2.setText(QCoreApplication.translate("Form", u"M01 BREAK", None))
        self.actionbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"program.optional-stop.toggle", None))
        self.power_button.setText(QCoreApplication.translate("Form", u"POWER", None))
        self.power_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.power.toggle", None))
        self.ref_coilumn_header_16.setText("")
        self.feedrate_2.setText(QCoreApplication.translate("Form", u"ET", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"0:00:00", None))
        self.ref_coilumn_header_18.setText("")
        self.exit_button.setText(QCoreApplication.translate("Form", u"E-STOP", None))
        self.exit_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.estop.toggle", None))
        self.ref_coilumn_header_3.setText(QCoreApplication.translate("Form", u"  T", None))
        self.tool_number_entry_box.setText(QCoreApplication.translate("Form", u"0", None))
        self.m6_button.setText(QCoreApplication.translate("Form", u"M6", None))
        self.m6_button.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"T#<tool_number_entry_box> M6", None))
        self.G43.setText(QCoreApplication.translate("Form", u"G43", None))
        self.G43.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:gcodes?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"'G43' in ch[0]\", \"name\": \"G43\"}, {\"channels\": [{\"url\": \"status:tool_in_spindle\", \"trigger\": false}, {\"url\": \"status:interp_state\", \"trigger\": true}, {\"url\": \"status:homed\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] != 0\", \"name\": \"disable if no tool loaded\"}]", None))
        self.G43.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G43", None))
        self.G49.setText(QCoreApplication.translate("Form", u"G49", None))
        self.G49.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:gcodes?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"'G49' in ch[0]\", \"name\": \"G49\"}]", None))
        self.G49.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G49", None))
        self.go_to_g30_button_2.setText(QCoreApplication.translate("Form", u"GO TO ZERO", None))
        self.go_to_g30_button_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.issue-mdi:G0 X0 Y0 Z0", None))
        self.go_to_g30.setText(QCoreApplication.translate("Form", u"GO TO G30", None))
        self.go_to_g30.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:gcodes\", \"trigger\": true}], \"property\": \"None\", \"expression\": \"\", \"name\": \"go to g30\"}]", None))
        self.go_to_g30.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G30", None))
        self.work_column_header_4.setText(QCoreApplication.translate("Form", u"LENGTH", None))
        self.tool_length.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_length.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]", None))
        self.tool_length.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_length.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.statuslabel_8.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:linear_units?text\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"str\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"ch[0]\",\n"
"        \"name\": \"Units\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]", None))
        self.statuslabel_8.setProperty(u"statusItem", QCoreApplication.translate("Form", u"program_units", None))
        self.work_column_header_5.setText(QCoreApplication.translate("Form", u"DIAM", None))
        self.tool_diameter.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_diameter.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?diameter\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Diameter\"}]", None))
        self.tool_diameter.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_diameter.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.statuslabel_11.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:linear_units?text\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"str\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"ch[0]\",\n"
"        \"name\": \"Units\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]", None))
        self.statuslabel_11.setProperty(u"statusItem", QCoreApplication.translate("Form", u"program_units", None))
        self.axisactionbutton_5.setText(QCoreApplication.translate("Form", u"REFERENCE ALL", None))
        self.axisactionbutton_5.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.home.all", None))
        self.axis_column_header.setText(QCoreApplication.translate("Form", u"AXIS", None))
        self.statuslabel_12.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:g5x_index?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0] + ' WORK'\\n\", \"name\": \"WCS Header\"}]", None))
        self.work_column_header_2.setText(QCoreApplication.translate("Form", u"MACHINE", None))
        self.dtg_column_header.setText(QCoreApplication.translate("Form", u"DTG", None))
        self.dtg_column_header_3.setText(QCoreApplication.translate("Form", u"REF", None))
        self.zero_x_button_3.setText(QCoreApplication.translate("Form", u"X", None))
        self.zero_x_button_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_x_button_3.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G10 L20 P{ch[0]} X0.0", None))
        self.statuslabel_40.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"('%.4f' if ch[1] == 'in' else '%.3f') % ch[0][0]\", \"name\": \"REL axis position\"}]", None))
        self.statuslabel_45.setProperty(u"style", QCoreApplication.translate("Form", u"unhomed", None))
        self.statuslabel_45.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?abs\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][0])\", \"name\": \"axis position\"}, {\"channels\": [{\"url\": \"status:joint[0].homed\", \"trigger\": true}, {\"url\": \"status:joint[0].homing\", \"trigger\": true}], \"property\": \"Style Class\", \"expression\": \"\\\"homed\\\" if ch[0] else \\\"homing\\\" if ch[1] else \\\"unhomed\\\"\", \"name\": \"homing indicator\"}]", None))
        self.statuslabel_75.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?dtg\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"('%.4f' if ch[1] == 'in' else '%.3f') % ch[0][0]\", \"name\": \"REL axis position\"}]", None))
        self.axisactionbutton_6.setText(QCoreApplication.translate("Form", u"REF X", None))
        self.axisactionbutton_6.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.home.axis:x", None))
        self.zero_y_button_3.setText(QCoreApplication.translate("Form", u"Y", None))
        self.zero_y_button_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_y_button_3.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G10 L20 P{ch[0]} Y0.0", None))
        self.statuslabel_41.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][1])\", \"name\": \"REL axis position\"}]", None))
        self.statuslabel_46.setProperty(u"style", QCoreApplication.translate("Form", u"unhomed", None))
        self.statuslabel_46.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?abs\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][1])\", \"name\": \"axis position\"}, {\"channels\": [{\"url\": \"status:joint[1].homed\", \"trigger\": true}, {\"url\": \"status:joint[1].homing\", \"trigger\": true}], \"property\": \"Style Class\", \"expression\": \"\\\"homed\\\" if ch[0] else \\\"homing\\\" if ch[1] else \\\"unhomed\\\"\", \"name\": \"homing indicator\"}]", None))
        self.statuslabel_76.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?dtg\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][1])\", \"name\": \"REL axis position\"}]", None))
        self.axisactionbutton_3.setText(QCoreApplication.translate("Form", u"REF Y", None))
        self.axisactionbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.home.axis:y", None))
        self.zero_z_button_3.setText(QCoreApplication.translate("Form", u"Z", None))
        self.zero_z_button_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_z_button_3.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G10 L20 P{ch[0]} Z0.0", None))
        self.statuslabel_42.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][2])\", \"name\": \"REL axis position\"}]", None))
        self.statuslabel_47.setProperty(u"style", QCoreApplication.translate("Form", u"unhomed", None))
        self.statuslabel_47.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?abs\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][2])\", \"name\": \"axis position\"}, {\"channels\": [{\"url\": \"status:joint[2].homed\", \"trigger\": true}, {\"url\": \"status:joint[2].homing\", \"trigger\": true}], \"property\": \"Style Class\", \"expression\": \"\\\"homed\\\" if ch[0] else \\\"homing\\\" if ch[1] else \\\"unhomed\\\"\", \"name\": \"homing indicator\"}]", None))
        self.statuslabel_77.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?dtg\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][2])\", \"name\": \"REL axis position\"}]", None))
        self.axisactionbutton.setText(QCoreApplication.translate("Form", u"REF Z", None))
        self.axisactionbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.home.axis:z", None))
        self.zero_a_button_3.setText(QCoreApplication.translate("Form", u"A", None))
        self.zero_a_button_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_a_button_3.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G10 L2 P{ch[0]} A0.0", None))
        self.statuslabel_43.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][3])\", \"name\": \"REL axis position\"}]", None))
        self.statuslabel_48.setProperty(u"style", QCoreApplication.translate("Form", u"unhomed", None))
        self.statuslabel_48.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?abs\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][3])\", \"name\": \"axis position\"}, {\"channels\": [{\"url\": \"status:joint[3].homed\", \"trigger\": true}, {\"url\": \"status:joint[3].homing\", \"trigger\": true}], \"property\": \"Style Class\", \"expression\": \"\\\"homed\\\" if ch[0] else \\\"homing\\\" if ch[1] else \\\"unhomed\\\"\", \"name\": \"homing indicator\"}]", None))
        self.statuslabel_78.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?dtg\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][3])\", \"name\": \"REL axis position\"}]", None))
        self.axisactionbutton_2.setText(QCoreApplication.translate("Form", u"REF A", None))
        self.axisactionbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.home.axis:a", None))
        self.zero_b_button_3.setText(QCoreApplication.translate("Form", u"B", None))
        self.zero_b_button_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_b_button_3.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G10 L2 P{ch[0]} B0.0", None))
        self.statuslabel_44.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][4])\", \"name\": \"REL axis position\"}]", None))
        self.statuslabel_49.setProperty(u"style", QCoreApplication.translate("Form", u"unhomed", None))
        self.statuslabel_49.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?abs\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][4])\", \"name\": \"axis position\"}, {\"channels\": [{\"url\": \"status:joint[4].homed\", \"trigger\": true}, {\"url\": \"status:joint[4].homing\", \"trigger\": true}], \"property\": \"Style Class\", \"expression\": \"\\\"homed\\\" if ch[0] else \\\"homing\\\" if ch[1] else \\\"unhomed\\\"\", \"name\": \"homing indicator\"}]", None))
        self.statuslabel_79.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"position:axis?dtg\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4]) if ch[1] == 'in' else \\\"{:.3f}\\\".format(ch[0][4])\", \"name\": \"REL axis position\"}]", None))
        self.axisactionbutton_4.setText(QCoreApplication.translate("Form", u"REF B", None))
        self.axisactionbutton_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.home.axis:b", None))
        self.statuslabel.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:feedrate\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"float\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"'{:.0%}'.format(ch[0])\",\n"
"        \"name\": \"New Rule\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]", None))
        self.statuslabel.setProperty(u"statusItem", QCoreApplication.translate("Form", u"feedrate", None))
        self.actionslider_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.rapid-override.set", None))
        self.statuslabel_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:spindle[0].override\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"float\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"'{:.0%}'.format(ch[0])\",\n"
"        \"name\": \"New Rule\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]", None))
        self.statuslabel_2.setProperty(u"statusItem", QCoreApplication.translate("Form", u"spindle.0.override", None))
        self.statuslabel_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:rapidrate\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"float\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"'{:.0%}'.format(ch[0])\",\n"
"        \"name\": \"New Rule\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]", None))
        self.statuslabel_3.setProperty(u"statusItem", QCoreApplication.translate("Form", u"rapidrate", None))
        self.work_column_header_3.setText(QCoreApplication.translate("Form", u"SPINDLE\n"
"LOAD", None))
        self.loadmeter.setProperty(u"barGradient", [
            QCoreApplication.translate("Form", u"0.0, 170, 170, 236", None),
            QCoreApplication.translate("Form", u"0.63, 85, 85, 238", None),
            QCoreApplication.translate("Form", u"0.65, 171, 171, 158", None),
            QCoreApplication.translate("Form", u"0.79, 227, 237, 106", None),
            QCoreApplication.translate("Form", u"0.84, 219, 124, 55", None),
            QCoreApplication.translate("Form", u"1.0, 209, 0, 0", None)])
        self.statuslabel_4.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:max_velocity\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"float\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"'{:.0f}'.format(ch[0] * 60)\",\n"
"        \"name\": \"New Rule\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]", None))
        self.statuslabel_4.setProperty(u"statusItem", QCoreApplication.translate("Form", u"max_velocity", None))
        self.statuslabel_4.setProperty(u"fromat", QCoreApplication.translate("Form", u"{:.0f}", None))
        self.actionslider.setProperty(u"actionName", QCoreApplication.translate("Form", u"spindle.override", None))
        self.actionbutton_28.setText(QCoreApplication.translate("Form", u"S 100%", None))
        self.actionbutton_28.setProperty(u"actionName", QCoreApplication.translate("Form", u"spindle.override.reset", None))
        self.actionslider_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.feed-override.set", None))
        self.actionslider_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.max-velocity.set", None))
        self.actionbutton_29.setText(QCoreApplication.translate("Form", u"F 100%", None))
        self.actionbutton_29.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.feed-override.reset", None))
        self.actionbutton_30.setText(QCoreApplication.translate("Form", u"MV 100%", None))
        self.actionbutton_30.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.max-velocity.reset", None))
        self.actionbutton_31.setText(QCoreApplication.translate("Form", u"R 100%", None))
        self.actionbutton_31.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.rapid-override.reset", None))
        self.actionslider_5.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.set-linear-speed-percentage", None))
        self.statuslabel_6.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:current_vel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"'%.1f' % (ch[0] * 60)\", \"name\": \"cur vel\"}]", None))
        self.statuslabel_6.setProperty(u"format", QCoreApplication.translate("Form", u"{:.1f}", None))
        self.statuslabel_6.setProperty(u"statusItem", "")
        self.rpm_label_3.setText(QCoreApplication.translate("Form", u"FEEDRATE", None))
        self.rpm_label_4.setText("")
        self.statuslabel_10.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:program_units?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Linear Units\"}]", None))
        self.statuslabel_10.setProperty(u"statusItem", QCoreApplication.translate("Form", u"linear_units", None))
        self.statuslabel_10.setProperty(u"fromat", "")
        self.work_column_header_7.setText(QCoreApplication.translate("Form", u"/M", None))
        self.statuslabel_7.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:settings\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"'%.1f' % ch[0][1]\", \"name\": \"F Word\"}]", None))
        self.statuslabel_7.setProperty(u"format", QCoreApplication.translate("Form", u"{:.1f}", None))
        self.statuslabel_7.setProperty(u"statusItem", "")
        self.statuslabel_5.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"trigger\": true, \"type\": \"float\", \"url\": \"status:spindle[0].speed\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.2f}\\\".format(ch[0])\", \"name\": \"Speed\"}]", None))
        self.statuslabel_5.setProperty(u"format", QCoreApplication.translate("Form", u"{:.2f}", None))
        self.statuslabel_5.setProperty(u"statusItem", "")
        self.rpm_label.setText(QCoreApplication.translate("Form", u"SPINDLE RPM", None))
        self.statuslabel_9.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:settings\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str( ch[0][2] )\", \"name\": \"S Word\"}]", None))
        self.statuslabel_9.setProperty(u"format", QCoreApplication.translate("Form", u"{:.2f}", None))
        self.statuslabel_9.setProperty(u"statusItem", "")
        self.spindle_rev_button.setText(QCoreApplication.translate("Form", u"REV", None))
        self.spindle_rev_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"spindle.reverse", None))
        self.spindle_stop_button.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.spindle_stop_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"spindle.off", None))
        self.spindle_fwd_button.setText(QCoreApplication.translate("Form", u"FWD", None))
        self.spindle_fwd_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"spindle.forward", None))
        self.menuExit.setTitle(QCoreApplication.translate("Form", u"File", None))
        self.menuRecentFiles.setTitle(QCoreApplication.translate("Form", u"Recent &Files", None))
        self.menuMachine.setTitle(QCoreApplication.translate("Form", u"Machine", None))
        self.menuHoming.setTitle(QCoreApplication.translate("Form", u"Homing", None))
        self.menuCooling.setTitle(QCoreApplication.translate("Form", u"Cooling", None))
        self.menuView.setTitle(QCoreApplication.translate("Form", u"View", None))
    # retranslateUi

