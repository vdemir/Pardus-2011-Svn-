#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from contents/ui/configPopup.ui on Thu Jul  2 13:02:26 2009
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_configPopup(object):
    def setupUi(self, configPopup):
        configPopup.setObjectName("configPopup")
        configPopup.resize(317, 363)
        self.gridLayout = QtGui.QGridLayout(configPopup)
        self.gridLayout.setObjectName("gridLayout")
        self.radioAll = QtGui.QRadioButton(configPopup)
        self.radioAll.setChecked(True)
        self.radioAll.setObjectName("radioAll")
        self.gridLayout.addWidget(self.radioAll, 0, 0, 1, 1)
        self.radioSelected = QtGui.QRadioButton(configPopup)
        self.radioSelected.setObjectName("radioSelected")
        self.gridLayout.addWidget(self.radioSelected, 1, 0, 1, 1)
        self.listProfiles = QtGui.QListWidget(configPopup)
        self.listProfiles.setEnabled(False)
        self.listProfiles.setObjectName("listProfiles")
        self.gridLayout.addWidget(self.listProfiles, 2, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 92, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 2)

        self.retranslateUi(configPopup)
        QtCore.QObject.connect(self.radioSelected, QtCore.SIGNAL("clicked(bool)"), self.listProfiles.setEnabled)
        QtCore.QObject.connect(self.radioAll, QtCore.SIGNAL("clicked(bool)"), self.listProfiles.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(configPopup)

    def retranslateUi(self, configPopup):
        configPopup.setWindowTitle(kdecore.i18n("Form"))
        self.radioAll.setText(kdecore.i18n("Show all profiles"))
        self.radioSelected.setText(kdecore.i18n("Show selected profiles from list"))

