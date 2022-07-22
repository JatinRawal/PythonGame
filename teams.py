# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teams.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3,math

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        db = sqlite3.connect("project.db")
        Dialog.setObjectName("Dialog")
        Dialog.resize(581, 437)
        Dialog.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 541, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.team_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.team_lbl.setFont(font)
        self.team_lbl.setAutoFillBackground(False)
        self.team_lbl.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.team_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.team_lbl.setObjectName("team_lbl")
        self.horizontalLayout.addWidget(self.team_lbl)
        self.teamcbox = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.teamcbox.setFont(font)
        self.teamcbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.teamcbox.setObjectName("teamcbox")
        self.horizontalLayout.addWidget(self.teamcbox)
        self.match_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.match_lbl.setFont(font)
        self.match_lbl.setAutoFillBackground(False)
        self.match_lbl.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.match_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.match_lbl.setObjectName("match_lbl")
        self.horizontalLayout.addWidget(self.match_lbl)
        sql = "SELECT name from teams"
        record = db.execute(sql)
        teams = []
        for row in record:
            teams.append(row[0])
            self.teamcbox.addItem(row[0])
        self.matchcbox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.matchcbox.setFont(font)
        self.matchcbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.matchcbox.setObjectName("matchcbox")
        self.matchcbox.addItem("")
        self.matchcbox.addItem("")
        self.horizontalLayout.addWidget(self.matchcbox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(19, 159, 541, 211))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout3.setSpacing(50)
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.player_list = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.player_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.player_list.setObjectName("player_list")
        self.horizontalLayout3.addWidget(self.player_list)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout3.addWidget(self.listWidget)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(19, 380, 541, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout4.setSpacing(30)
        self.horizontalLayout4.setObjectName("horizontalLayout4")
        self.click_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.click_btn.setFont(font)
        self.click_btn.setAutoFillBackground(False)
        self.click_btn.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.click_btn.setObjectName("click_btn")
        self.horizontalLayout4.addWidget(self.click_btn)
        self.click_btn.clicked.connect(self.evaluatePoints)
        self.result_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.result_lbl.setFont(font)
        self.result_lbl.setAutoFillBackground(False)
        self.result_lbl.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.result_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.result_lbl.setObjectName("result_lbl")
        self.horizontalLayout4.addWidget(self.result_lbl)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 90, 521, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2.setSpacing(15)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.player_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.player_lbl.setFont(font)
        self.player_lbl.setAutoFillBackground(False)
        self.player_lbl.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.player_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.player_lbl.setObjectName("player_lbl")
        self.horizontalLayout2.addWidget(self.player_lbl)
        self.score_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.score_lbl.setFont(font)
        self.score_lbl.setAutoFillBackground(False)
        self.score_lbl.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.score_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.score_lbl.setObjectName("score_lbl")
        self.horizontalLayout2.addWidget(self.score_lbl)
        self.totalPoints = 0
        self.line1 = QtWidgets.QFrame(Dialog)
        self.line1.setGeometry(QtCore.QRect(20, 70, 541, 20))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QFrame(Dialog)
        self.line2.setGeometry(QtCore.QRect(20, 140, 541, 20))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.team_lbl.setText(_translate("Dialog", "Select Team"))
        self.match_lbl.setText(_translate("Dialog", "Select Match"))
        self.matchcbox.setItemText(0, _translate("Dialog", "match1"))
        self.matchcbox.setItemText(1, _translate("Dialog", "match2"))
        self.click_btn.setText(_translate("Dialog", "Click to calculate Score"))
        self.result_lbl.setText(_translate("Dialog", "00"))
        self.player_lbl.setText(_translate("Dialog", "PLAYERS"))
        self.score_lbl.setText(_translate("Dialog", "SCORES"))
    
    def evaluatePoints(self):
        db = sqlite3.connect("project.db")
        cursordb = db.cursor()
        self.totalPoints=0
        team = self.teamcbox.currentText()
        self.player_list.clear()
        sql = "SELECT players,value FROM teams WHERE name='"+team+"';"
        cursordb.execute(sql)
        record = cursordb.fetchone()
        players = record[0].split(',')
        self.player_list.addItems(players)
        self.listWidget.clear()
        match = self.matchcbox.currentText()
        for i in range(self.player_list.count()):
                        nm = self.player_list.item(i).text()
                        cursordb.execute("SELECT * from "+match+" where player='"+nm+"';")
                        record = cursordb.fetchone()
                        pointsCalc = bat(record)
                        pointsCalc +=bowl(record)
                        self.listWidget.addItem(str(pointsCalc))
                        self.totalPoints += pointsCalc
        self.result_lbl.setText(str(self.totalPoints))

def bat(val):
        batscore = 0
        strike_rate = 0
        if val[2] > 0:
            strike_rate = int(val[1]/val[2] * 100)
            batscore += math.floor(val[1]/2)
        if val[1] > 50:
            batscore += 5
            if val[1] > 100:
                batscore += 10
        if (strike_rate > 100) :
            batscore += 4
        elif (strike_rate > 80) and (strike_rate < 100):
            batscore += 2
        if val[3] > 0:
            batscore  += 1 * val[3]
        if val[4] > 0:
            batscore  += 2 * val[4]
        if val[9] > 0 :
            batscore += 10 * val[9]
        if val[10] > 0:
            batscore += 10 * val[10]
        if val[11] > 0:
            batscore += 10 * val[11]
        return batscore

def bowl(val):
        bowlscore = 0
        bowlscore += val[8] * 10
        if val[8] >= 3 :
            bowlscore += 5
        if val[8] >= 5:
            bowlscore += 10
        if val[5] > 0:
            overs = val[5] / 6
            economy_rate = (val[7] / overs)
            if economy_rate >= 3.5 and economy_rate <=4.5:
                bowlscore +=4
            elif economy_rate > 2  and economy_rate <=3.5:
                bowlscore += 7
            elif economy_rate <=2:
              bowlscore += 10
        return bowlscore    

if __name__ == "__main__":
    import sys,sqlite3,math
    db = sqlite3.connect("project.db")
    cursordb = db.cursor()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    db.close()