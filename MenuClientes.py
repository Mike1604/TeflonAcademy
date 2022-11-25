from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_83 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_83.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_83.setSpacing(0)
        self.gridLayout_83.setObjectName("gridLayout_83")
        self.Frame_Inferior = QtWidgets.QFrame(self.centralwidget)
        self.Frame_Inferior.setStyleSheet("background-color: #231f20;")
        self.Frame_Inferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_Inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Inferior.setObjectName("Frame_Inferior")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Frame_Inferior)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Frame_Inferior)
        self.stackedWidget.setMinimumSize(QtCore.QSize(300, 70))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Catalogo = QtWidgets.QWidget()
        self.Catalogo.setObjectName("Catalogo")
        self.stackedWidget.addWidget(self.Catalogo)
        self.InfoPersona = QtWidgets.QWidget()
        self.InfoPersona.setObjectName("InfoPersona")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.InfoPersona)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(150, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        self.label_119 = QtWidgets.QLabel(self.InfoPersona)
        self.label_119.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_119.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_119.setObjectName("label_119")
        self.gridLayout_2.addWidget(self.label_119, 0, 1, 1, 1)
        self.label_121 = QtWidgets.QLabel(self.InfoPersona)
        self.label_121.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_121.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_121.setObjectName("label_121")
        self.gridLayout_2.addWidget(self.label_121, 2, 1, 1, 1)
        self.label_123 = QtWidgets.QLabel(self.InfoPersona)
        self.label_123.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_123.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_123.setObjectName("label_123")
        self.gridLayout_2.addWidget(self.label_123, 4, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.InfoPersona)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_5.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 3, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.InfoPersona)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_3.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.InfoPersona)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_2.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.InfoPersona)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_4.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 2, 2, 1, 1)
        self.label_122 = QtWidgets.QLabel(self.InfoPersona)
        self.label_122.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_122.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_122.setObjectName("label_122")
        self.gridLayout_2.addWidget(self.label_122, 3, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.InfoPersona)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_6.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 4, 2, 1, 1)
        self.label_124 = QtWidgets.QLabel(self.InfoPersona)
        self.label_124.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_124.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_124.setObjectName("label_124")
        self.gridLayout_2.addWidget(self.label_124, 5, 1, 1, 1)
        self.label_120 = QtWidgets.QLabel(self.InfoPersona)
        self.label_120.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_120.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_120.setObjectName("label_120")
        self.gridLayout_2.addWidget(self.label_120, 1, 1, 1, 1)
        self.label_125 = QtWidgets.QLabel(self.InfoPersona)
        self.label_125.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_125.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_125.setObjectName("label_125")
        self.gridLayout_2.addWidget(self.label_125, 6, 1, 1, 1)
        self.label_126 = QtWidgets.QLabel(self.InfoPersona)
        self.label_126.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_126.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_126.setObjectName("label_126")
        self.gridLayout_2.addWidget(self.label_126, 7, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.InfoPersona)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_7.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 5, 2, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.InfoPersona)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_8.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 6, 2, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.InfoPersona)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_9.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 7, 2, 1, 1)
        self.stackedWidget.addWidget(self.InfoPersona)
        self.Membresia = QtWidgets.QWidget()
        self.Membresia.setObjectName("Membresia")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Membresia)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.Membresia)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem2, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem3, 3, 4, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_28.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_28.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_28.setReadOnly(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_10.addWidget(self.lineEdit_28, 0, 2, 1, 2)
        self.label_146 = QtWidgets.QLabel(self.frame)
        self.label_146.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_146.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_146.setObjectName("label_146")
        self.gridLayout_10.addWidget(self.label_146, 1, 0, 1, 3)
        self.label_147 = QtWidgets.QLabel(self.frame)
        self.label_147.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_147.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_147.setObjectName("label_147")
        self.gridLayout_10.addWidget(self.label_147, 2, 0, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_30.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_30.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_30.setText("")
        self.lineEdit_30.setReadOnly(True)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_10.addWidget(self.lineEdit_30, 2, 1, 1, 3)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_29.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_29.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_29.setText("")
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_10.addWidget(self.lineEdit_29, 1, 3, 1, 1)
        self.label_145 = QtWidgets.QLabel(self.frame)
        self.label_145.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_145.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_145.setObjectName("label_145")
        self.gridLayout_10.addWidget(self.label_145, 0, 0, 1, 2)
        self.label_159 = QtWidgets.QLabel(self.frame)
        self.label_159.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_159.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_159.setObjectName("label_159")
        self.gridLayout_10.addWidget(self.label_159, 4, 0, 1, 1)
        self.label_148 = QtWidgets.QLabel(self.frame)
        self.label_148.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_148.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_148.setObjectName("label_148")
        self.gridLayout_10.addWidget(self.label_148, 3, 0, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_31.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_31.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_31.setText("")
        self.lineEdit_31.setReadOnly(True)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_10.addWidget(self.lineEdit_31, 3, 1, 1, 3)
        self.lineEdit_42 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_42.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_42.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_42.setText("")
        self.lineEdit_42.setReadOnly(True)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.gridLayout_10.addWidget(self.lineEdit_42, 4, 1, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 4, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem5, 0, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem6, 1, 4, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.Membresia)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_160 = QtWidgets.QLabel(self.frame_2)
        self.label_160.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_160.setAlignment(QtCore.Qt.AlignCenter)
        self.label_160.setObjectName("label_160")
        self.gridLayout_11.addWidget(self.label_160, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem7, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 3)
        self.stackedWidget.addWidget(self.Membresia)
        self.Reusmen = QtWidgets.QWidget()
        self.Reusmen.setObjectName("Reusmen")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Reusmen)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.Reusmen)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem8 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem9, 0, 0, 1, 1)
        self.label_162 = QtWidgets.QLabel(self.frame_5)
        self.label_162.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_162.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_162.setObjectName("label_162")
        self.gridLayout_12.addWidget(self.label_162, 1, 1, 1, 1)
        self.lineEdit_44 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_44.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_44.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_44.setReadOnly(True)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.gridLayout_12.addWidget(self.lineEdit_44, 1, 2, 1, 1)
        self.lineEdit_43 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_43.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_43.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_43.setReadOnly(True)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.gridLayout_12.addWidget(self.lineEdit_43, 0, 2, 1, 1)
        self.label_161 = QtWidgets.QLabel(self.frame_5)
        self.label_161.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_161.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_161.setObjectName("label_161")
        self.gridLayout_12.addWidget(self.label_161, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem10, 0, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem11, 1, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.Reusmen)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.TablaEmpleados_4 = QtWidgets.QTableWidget(self.frame_6)
        self.TablaEmpleados_4.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #77838d;\n"
"    border: .5px solid #034aa6;\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"\n"
"}")
        self.TablaEmpleados_4.setDragEnabled(False)
        self.TablaEmpleados_4.setObjectName("TablaEmpleados_4")
        self.TablaEmpleados_4.setColumnCount(4)
        self.TablaEmpleados_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(3, item)
        self.TablaEmpleados_4.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaEmpleados_4.horizontalHeader().setHighlightSections(False)
        self.TablaEmpleados_4.horizontalHeader().setSortIndicatorShown(False)
        self.TablaEmpleados_4.horizontalHeader().setStretchLastSection(True)
        self.TablaEmpleados_4.verticalHeader().setVisible(False)
        self.TablaEmpleados_4.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_13.addWidget(self.TablaEmpleados_4, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)
        self.stackedWidget.addWidget(self.Reusmen)
        self.Menu = QtWidgets.QWidget()
        self.Menu.setObjectName("Menu")
        self.gridLayout = QtWidgets.QGridLayout(self.Menu)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.Menu)
        self.pushButton_5.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 8, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.Menu)
        self.pushButton_12.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 8, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 11, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 11, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.Menu)
        self.pushButton_11.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 11, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 12, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.Menu)
        self.pushButton_10.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 5, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 8, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.Menu)
        self.pushButton_8.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.Menu)
        self.pushButton_4.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 11, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 5, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.Menu)
        self.pushButton_3.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.Menu)
        self.pushButton_2.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 5, 3, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 8, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 2, 3, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(149, 117, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.Menu)
        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout_83.addWidget(self.Frame_Inferior, 1, 0, 1, 1)
        self.Navbar_Frame = QtWidgets.QFrame(self.centralwidget)
        self.Navbar_Frame.setMinimumSize(QtCore.QSize(0, 0))
        self.Navbar_Frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.Navbar_Frame.setStyleSheet("background-color: #F4F4F4;")
        self.Navbar_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Navbar_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Navbar_Frame.setObjectName("Navbar_Frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Navbar_Frame)
        self.horizontalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_Info_actual = QtWidgets.QLabel(self.Navbar_Frame)
        self.label_Info_actual.setMinimumSize(QtCore.QSize(0, 0))
        self.label_Info_actual.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_Info_actual.setText("")
        self.label_Info_actual.setWordWrap(True)
        self.label_Info_actual.setObjectName("label_Info_actual")
        self.horizontalLayout_2.addWidget(self.label_Info_actual)
        self.label_3 = QtWidgets.QLabel(self.Navbar_Frame)
        self.label_3.setMinimumSize(QtCore.QSize(70, 70))
        self.label_3.setStyleSheet("image: url(:/menu/logonegro.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.Navbar_Frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 87 18pt;\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem22 = QtWidgets.QSpacerItem(386, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem22)
        self.pushButton = QtWidgets.QPushButton(self.Navbar_Frame)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/menuiconBLACK.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    \n"
"    image: url(:/menu/menuIcon.png);\n"
"}\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem23)
        self.gridLayout_83.addWidget(self.Navbar_Frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_119.setText(_translate("MainWindow", "ID de cliente:"))
        self.label_121.setText(_translate("MainWindow", "Teléfono"))
        self.label_123.setText(_translate("MainWindow", "Edad:"))
        self.label_122.setText(_translate("MainWindow", "Correo electronico:"))
        self.label_124.setText(_translate("MainWindow", "Peso actual:"))
        self.label_120.setText(_translate("MainWindow", "Nombre:"))
        self.label_125.setText(_translate("MainWindow", "Altura:"))
        self.label_126.setText(_translate("MainWindow", "IMC:"))
        self.label_146.setText(_translate("MainWindow", "Nombre:"))
        self.label_147.setText(_translate("MainWindow", "Fecha de ingreso:"))
        self.label_145.setText(_translate("MainWindow", "ID de cliente:"))
        self.label_159.setText(_translate("MainWindow", "Fecha de vencimiento:"))
        self.label_148.setText(_translate("MainWindow", "Membresia actual:"))
        self.label_160.setText(_translate("MainWindow", "Tu membresía vence en: "))
        self.label_162.setText(_translate("MainWindow", "Nombre:"))
        self.label_161.setText(_translate("MainWindow", "ID de cliente:"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Peso"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IMC"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dias asistidos"))
        self.pushButton_12.setText(_translate("MainWindow", "Ver catálogo de productos"))
        self.pushButton_11.setText(_translate("MainWindow", "Ver resumen personal"))
        self.pushButton_10.setText(_translate("MainWindow", "Ver plan de membresía"))
        self.pushButton_8.setText(_translate("MainWindow", "Ver información personal"))
        self.label_4.setText(_translate("MainWindow", "  Bienvenido "))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

