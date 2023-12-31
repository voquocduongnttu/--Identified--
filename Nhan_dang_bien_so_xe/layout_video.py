# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_video.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1538, 859)
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1521, 841))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setMouseTracking(False)
        self.frame.setTabletTracking(False)
        self.frame.setAcceptDrops(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.636826, y1:1, x2:0.627025, y2:0.102, stop:0 rgba(0, 200, 237, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 1491, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 90, 1481, 741))
        self.frame_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.636826, y1:1, x2:0.627025, y2:0.102, stop:0 rgba(0, 200, 237, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.original_video = QtWidgets.QLabel(self.frame_2)
        self.original_video.setGeometry(QtCore.QRect(10, 10, 1051, 511))
        self.original_video.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.original_video.setFrameShape(QtWidgets.QFrame.Box)
        self.original_video.setObjectName("original_video")
        self.lbl_contour = QtWidgets.QLabel(self.frame_2)
        self.lbl_contour.setGeometry(QtCore.QRect(10, 540, 1051, 191))
        self.lbl_contour.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_contour.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_contour.setObjectName("lbl_contour")
        self.btn_chonVideo = QtWidgets.QPushButton(self.frame_2)
        self.btn_chonVideo.setGeometry(QtCore.QRect(1090, 20, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_chonVideo.setFont(font)
        self.btn_chonVideo.setObjectName("btn_chonVideo")
        self.btn_nhandang = QtWidgets.QPushButton(self.frame_2)
        self.btn_nhandang.setGeometry(QtCore.QRect(1300, 20, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_nhandang.setFont(font)
        self.btn_nhandang.setObjectName("btn_nhandang")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(1080, 160, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.let_bienso = QtWidgets.QLineEdit(self.frame_2)
        self.let_bienso.setGeometry(QtCore.QRect(1220, 140, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.let_bienso.setFont(font)
        self.let_bienso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.let_bienso.setText("")
        self.let_bienso.setAlignment(QtCore.Qt.AlignCenter)
        self.let_bienso.setObjectName("let_bienso")
        self.let_ngay = QtWidgets.QLineEdit(self.frame_2)
        self.let_ngay.setGeometry(QtCore.QRect(1240, 590, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.let_ngay.setFont(font)
        self.let_ngay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.let_ngay.setAlignment(QtCore.Qt.AlignCenter)
        self.let_ngay.setObjectName("let_ngay")
        self.let_gio = QtWidgets.QLineEdit(self.frame_2)
        self.let_gio.setGeometry(QtCore.QRect(1240, 670, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.let_gio.setFont(font)
        self.let_gio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.let_gio.setAlignment(QtCore.Qt.AlignCenter)
        self.let_gio.setObjectName("let_gio")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(1080, 300, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(1090, 430, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(1090, 590, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(1090, 670, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(1090, 510, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.let_lop = QtWidgets.QLineEdit(self.frame_2)
        self.let_lop.setGeometry(QtCore.QRect(1240, 510, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.let_lop.setFont(font)
        self.let_lop.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.let_lop.setAlignment(QtCore.Qt.AlignCenter)
        self.let_lop.setObjectName("let_lop")
        self.let_ten = QtWidgets.QLineEdit(self.frame_2)
        self.let_ten.setGeometry(QtCore.QRect(1240, 430, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.let_ten.setFont(font)
        self.let_ten.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.let_ten.setText("")
        self.let_ten.setAlignment(QtCore.Qt.AlignCenter)
        self.let_ten.setObjectName("let_ten")
        self.let_tinh = QtWidgets.QLineEdit(self.frame_2)
        self.let_tinh.setGeometry(QtCore.QRect(1220, 290, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.let_tinh.setFont(font)
        self.let_tinh.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.let_tinh.setText("")
        self.let_tinh.setAlignment(QtCore.Qt.AlignCenter)
        self.let_tinh.setObjectName("let_tinh")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "QUẢN LÝ BIỂN SỐ XE VIỆT NAM"))
        self.original_video.setText(_translate("Frame", "TextLabel"))
        self.lbl_contour.setText(_translate("Frame", "TextLabelllll"))
        self.btn_chonVideo.setText(_translate("Frame", "Bắt Đầu"))
        self.btn_nhandang.setText(_translate("Frame", "Dừng"))
        self.label_4.setText(_translate("Frame", "Biển số"))
        self.label_9.setText(_translate("Frame", "Tỉnh"))
        self.label_5.setText(_translate("Frame", "Họ & Tên"))
        self.label_6.setText(_translate("Frame", "Ngày"))
        self.label_7.setText(_translate("Frame", "Giờ"))
        self.label_8.setText(_translate("Frame", "Lớp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
