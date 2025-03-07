#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from contents/ui/configIcon.ui on Mon Jul  6 18:07:36 2009
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_configIcon(object):
    def setupUi(self, configIcon):
        configIcon.setObjectName("configIcon")
        configIcon.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(configIcon)
        self.gridLayout.setObjectName("gridLayout")
        self.checkStatus = QtGui.QCheckBox(configIcon)
        self.checkStatus.setObjectName("checkStatus")
        self.gridLayout.addWidget(self.checkStatus, 0, 0, 1, 1)
        self.checkTraffic = QtGui.QCheckBox(configIcon)
        self.checkTraffic.setObjectName("checkTraffic")
        self.gridLayout.addWidget(self.checkTraffic, 1, 0, 1, 1)
        self.checkWifi = QtGui.QCheckBox(configIcon)
        self.checkWifi.setObjectName("checkWifi")
        self.gridLayout.addWidget(self.checkWifi, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(configIcon)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinInterval = QtGui.QSpinBox(configIcon)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinInterval.sizePolicy().hasHeightForWidth())
        self.spinInterval.setSizePolicy(sizePolicy)
        self.spinInterval.setMinimum(2)
        self.spinInterval.setObjectName("spinInterval")
        self.horizontalLayout.addWidget(self.spinInterval)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 162, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.checkBattery = QtGui.QCheckBox(configIcon)
        self.checkBattery.setObjectName("checkBattery")
        self.gridLayout.addWidget(self.checkBattery, 4, 0, 1, 1)

        self.retranslateUi(configIcon)
        QtCore.QMetaObject.connectSlotsByName(configIcon)

    def retranslateUi(self, configIcon):
        configIcon.setWindowTitle(kdecore.i18n("Form"))
        self.checkStatus.setText(kdecore.i18n("Show connection status"))
        self.checkTraffic.setText(kdecore.i18n("Show traffic lights"))
        self.checkWifi.setText(kdecore.i18n("Update wifi signal quality"))
        self.label.setText(kdecore.i18n("Update Interval :"))
        self.spinInterval.setSuffix(kdecore.i18n(" sec."))
        self.checkBattery.setText(kdecore.i18n("Dont poll anything while battery is discharging"))

