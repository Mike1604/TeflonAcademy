

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow , cursor, id, LogIn):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 718)
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
        self.gridLayout = QtWidgets.QGridLayout(self.Frame_Inferior)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.Frame_Inferior)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setMinimumSize(QtCore.QSize(300, 70))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Catalogo_2 = QtWidgets.QWidget()
        self.Catalogo_2.setObjectName("Catalogo_2")
        self.stackedWidget.addWidget(self.Catalogo_2)
        self.InfoPersona_2 = QtWidgets.QWidget()
        self.InfoPersona_2.setObjectName("InfoPersona_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.InfoPersona_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(150, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 3, 1, 1)
        self.label_127 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_127.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_127.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_127.setObjectName("label_127")
        self.gridLayout_4.addWidget(self.label_127, 0, 1, 1, 1)
        self.label_128 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_128.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_128.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_128.setObjectName("label_128")
        self.gridLayout_4.addWidget(self.label_128, 2, 1, 1, 1)
        self.label_129 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_129.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_129.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_129.setObjectName("label_129")
        self.gridLayout_4.addWidget(self.label_129, 4, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_10.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_4.addWidget(self.lineEdit_10, 3, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_11.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_4.addWidget(self.lineEdit_11, 1, 2, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_12.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_4.addWidget(self.lineEdit_12, 0, 2, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_13.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_4.addWidget(self.lineEdit_13, 2, 2, 1, 1)
        self.label_130 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_130.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_130.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_130.setObjectName("label_130")
        self.gridLayout_4.addWidget(self.label_130, 3, 1, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_14.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_4.addWidget(self.lineEdit_14, 4, 2, 1, 1)
        self.label_131 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_131.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_131.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_131.setObjectName("label_131")
        self.gridLayout_4.addWidget(self.label_131, 5, 1, 1, 1)
        self.label_132 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_132.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_132.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_132.setObjectName("label_132")
        self.gridLayout_4.addWidget(self.label_132, 1, 1, 1, 1)
        self.label_133 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_133.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_133.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_133.setObjectName("label_133")
        self.gridLayout_4.addWidget(self.label_133, 6, 1, 1, 1)
        self.label_134 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_134.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_134.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_134.setObjectName("label_134")
        self.gridLayout_4.addWidget(self.label_134, 7, 1, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_15.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_4.addWidget(self.lineEdit_15, 5, 2, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_16.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_4.addWidget(self.lineEdit_16, 6, 2, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_17.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_4.addWidget(self.lineEdit_17, 7, 2, 1, 1)
        self.stackedWidget.addWidget(self.InfoPersona_2)
        self.Membresia_2 = QtWidgets.QWidget()
        self.Membresia_2.setObjectName("Membresia_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Membresia_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.Membresia_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem2 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem2, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem3, 3, 4, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_32.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_32.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_32.setReadOnly(True)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_14.addWidget(self.lineEdit_32, 0, 2, 1, 2)
        self.label_149 = QtWidgets.QLabel(self.frame_7)
        self.label_149.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_149.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_149.setObjectName("label_149")
        self.gridLayout_14.addWidget(self.label_149, 1, 0, 1, 3)
        self.label_150 = QtWidgets.QLabel(self.frame_7)
        self.label_150.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_150.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_150.setObjectName("label_150")
        self.gridLayout_14.addWidget(self.label_150, 2, 0, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_33.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_33.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_33.setText("")
        self.lineEdit_33.setReadOnly(True)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_14.addWidget(self.lineEdit_33, 2, 1, 1, 3)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_34.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_34.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_34.setText("")
        self.lineEdit_34.setReadOnly(True)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_14.addWidget(self.lineEdit_34, 1, 3, 1, 1)
        self.label_151 = QtWidgets.QLabel(self.frame_7)
        self.label_151.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_151.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_151.setObjectName("label_151")
        self.gridLayout_14.addWidget(self.label_151, 0, 0, 1, 2)
        self.label_163 = QtWidgets.QLabel(self.frame_7)
        self.label_163.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_163.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_163.setObjectName("label_163")
        self.gridLayout_14.addWidget(self.label_163, 4, 0, 1, 1)
        self.label_152 = QtWidgets.QLabel(self.frame_7)
        self.label_152.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_152.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_152.setObjectName("label_152")
        self.gridLayout_14.addWidget(self.label_152, 3, 0, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_35.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_35.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_35.setText("")
        self.lineEdit_35.setReadOnly(True)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_14.addWidget(self.lineEdit_35, 3, 1, 1, 3)
        self.lineEdit_45 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_45.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_45.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_45.setText("")
        self.lineEdit_45.setReadOnly(True)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.gridLayout_14.addWidget(self.lineEdit_45, 4, 1, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem4, 4, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem5, 0, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem6, 1, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.Membresia_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_164 = QtWidgets.QLabel(self.frame_8)
        self.label_164.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_164.setAlignment(QtCore.Qt.AlignCenter)
        self.label_164.setObjectName("label_164")
        self.gridLayout_15.addWidget(self.label_164, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem7, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 3)
        self.stackedWidget.addWidget(self.Membresia_2)
        self.Reusmen_2 = QtWidgets.QWidget()
        self.Reusmen_2.setObjectName("Reusmen_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Reusmen_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.Reusmen_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem8 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem9, 0, 0, 1, 1)
        self.label_165 = QtWidgets.QLabel(self.frame_9)
        self.label_165.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_165.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_165.setObjectName("label_165")
        self.gridLayout_16.addWidget(self.label_165, 1, 1, 1, 1)
        self.lineEdit_46 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_46.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_46.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_46.setReadOnly(True)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.gridLayout_16.addWidget(self.lineEdit_46, 1, 2, 1, 1)
        self.lineEdit_47 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_47.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_47.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_47.setReadOnly(True)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.gridLayout_16.addWidget(self.lineEdit_47, 0, 2, 1, 1)
        self.label_166 = QtWidgets.QLabel(self.frame_9)
        self.label_166.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_166.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_166.setObjectName("label_166")
        self.gridLayout_16.addWidget(self.label_166, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem10, 0, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem11, 1, 3, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.Reusmen_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.TablaEmpleados_5 = QtWidgets.QTableWidget(self.frame_10)
        self.TablaEmpleados_5.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #77838d;\n"
"    border: .5px solid #034aa6;\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"\n"
"}")
        self.TablaEmpleados_5.setDragEnabled(False)
        self.TablaEmpleados_5.setObjectName("TablaEmpleados_5")
        self.TablaEmpleados_5.setColumnCount(4)
        self.TablaEmpleados_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_5.setHorizontalHeaderItem(3, item)
        self.TablaEmpleados_5.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaEmpleados_5.horizontalHeader().setHighlightSections(False)
        self.TablaEmpleados_5.horizontalHeader().setSortIndicatorShown(False)
        self.TablaEmpleados_5.horizontalHeader().setStretchLastSection(True)
        self.TablaEmpleados_5.verticalHeader().setVisible(False)
        self.TablaEmpleados_5.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_17.addWidget(self.TablaEmpleados_5, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 2)
        self.stackedWidget.addWidget(self.Reusmen_2)
        self.Menu_2 = QtWidgets.QWidget()
        self.Menu_2.setObjectName("Menu_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Menu_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
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
        self.pushButton_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_5.addWidget(self.pushButton_7, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem12, 7, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_13.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
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
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_5.addWidget(self.pushButton_13, 7, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem13, 10, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_15.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
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
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_5.addWidget(self.pushButton_15, 10, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem14, 4, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_16.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
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
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_5.addWidget(self.pushButton_16, 4, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem15, 10, 3, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(149, 117, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem16, 1, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem17, 4, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem18, 1, 3, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_14.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
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
        self.pushButton_14.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon1)
        self.pushButton_14.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_5.addWidget(self.pushButton_14, 7, 2, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem19, 7, 3, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_17.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
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
        self.pushButton_17.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon2)
        self.pushButton_17.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_5.addWidget(self.pushButton_17, 10, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_9.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
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
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_5.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
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
        self.pushButton_6.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_5.addWidget(self.pushButton_6, 4, 2, 1, 1)
        self.stackedWidget.addWidget(self.Menu_2)
        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.Frame_Inferior)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_22.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_22.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_22.setStyleSheet("QPushButton{\n"
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
        self.pushButton_22.setText("")
        self.pushButton_22.setIcon(icon)
        self.pushButton_22.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_7.addWidget(self.pushButton_22, 1, 1, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_19.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_19.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_19.setStyleSheet("QPushButton{\n"
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
        self.pushButton_19.setText("")
        self.pushButton_19.setIcon(icon3)
        self.pushButton_19.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_7.addWidget(self.pushButton_19, 2, 1, 1, 2)
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_21.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_21.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_21.setStyleSheet("QPushButton{\n"
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
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon2)
        self.pushButton_21.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_7.addWidget(self.pushButton_21, 4, 1, 1, 2)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_20.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_20.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_20.setStyleSheet("QPushButton{\n"
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
        self.pushButton_20.setText("")
        self.pushButton_20.setIcon(icon1)
        self.pushButton_20.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_7.addWidget(self.pushButton_20, 3, 1, 1, 2)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_18.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_18.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
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
        self.pushButton_18.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/menu/home2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon4)
        self.pushButton_18.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_7.addWidget(self.pushButton_18, 0, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem20, 1, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem21, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)
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
        
        # Botones del menu 
        self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.InfoPersona_2))
        self.pushButton_16.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Membresia_2))
        self.pushButton_13.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Catalogo_2))
        self.pushButton_15.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reusmen_2))
        
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.InfoPersona_2))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Membresia_2))
        self.pushButton_14.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Catalogo_2))
        self.pushButton_17.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reusmen_2))
        
        #menu de navegacion
        self.pushButton.clicked.connect(lambda: self.desplegarMenu())
        self.pushButton_18.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Menu_2))
        
        self.pushButton_22.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.InfoPersona_2))
        self.pushButton_19.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Membresia_2))
        self.pushButton_20.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Catalogo_2))
        self.pushButton_21.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reusmen_2))
        
        #informacion personal
        sql = "select * from cliente where cast(id_cliente as varchar)='{}' """.format(id)
        cursor.execute(sql)
        row=cursor.fetchall()
        for rows in row:
            self.lineEdit_12.setText(str(rows[0]))
            self.lineEdit_11.setText(str(rows[1]))
            self.lineEdit_13.setText(str(rows[2]))
            self.lineEdit_10.setText(str(rows[3]))
            self.lineEdit_14.setText(str(rows[4]))
            self.lineEdit_15.setText(str(rows[5]))
            self.lineEdit_16.setText(str(rows[6]))
            self.lineEdit_17.setText(str(rows[7]))
            
    #funcion para el menu de navegacion
    def desplegarMenu(self):
        
        if True:
            width = self.frame_2.width()
            normal = 0
            if width==0:
                extender = 150
            else:
                extender = normal
            
            self.animacion = QtCore.QPropertyAnimation(self.frame_2, b'minimumWidth') 
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width) 
            self.animacion.setEndValue(extender) 
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart) 
            self.animacion.start()
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_127.setText(_translate("MainWindow", "ID de cliente:"))
        self.label_128.setText(_translate("MainWindow", "Teléfono"))
        self.label_129.setText(_translate("MainWindow", "Edad:"))
        self.label_130.setText(_translate("MainWindow", "Correo electronico:"))
        self.label_131.setText(_translate("MainWindow", "Peso actual:"))
        self.label_132.setText(_translate("MainWindow", "Nombre:"))
        self.label_133.setText(_translate("MainWindow", "Altura:"))
        self.label_134.setText(_translate("MainWindow", "IMC:"))
        self.label_149.setText(_translate("MainWindow", "Nombre:"))
        self.label_150.setText(_translate("MainWindow", "Fecha de ingreso:"))
        self.label_151.setText(_translate("MainWindow", "ID de cliente:"))
        self.label_163.setText(_translate("MainWindow", "Fecha de vencimiento:"))
        self.label_152.setText(_translate("MainWindow", "Membresia actual:"))
        self.label_164.setText(_translate("MainWindow", "Tu membresía vence en: "))
        self.label_165.setText(_translate("MainWindow", "Nombre:"))
        self.label_166.setText(_translate("MainWindow", "ID de cliente:"))
        item = self.TablaEmpleados_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.TablaEmpleados_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Peso"))
        item = self.TablaEmpleados_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IMC"))
        item = self.TablaEmpleados_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dias asistidos"))
        self.pushButton_13.setText(_translate("MainWindow", "Ver catálogo de productos"))
        self.pushButton_15.setText(_translate("MainWindow", "Ver resumen personal"))
        self.pushButton_16.setText(_translate("MainWindow", "Ver plan de membresía"))
        self.pushButton_9.setText(_translate("MainWindow", "Ver información personal"))
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

