# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExceptionScriptSelector(object):
    def setupUi(self, ExceptionScriptSelector):
        ExceptionScriptSelector.setObjectName("ExceptionScriptSelector")
        ExceptionScriptSelector.setWindowModality(QtCore.Qt.WindowModal)
        ExceptionScriptSelector.resize(510, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(ExceptionScriptSelector.sizePolicy().hasHeightForWidth())
        ExceptionScriptSelector.setSizePolicy(sizePolicy)
        ExceptionScriptSelector.setMinimumSize(QtCore.QSize(510, 250))
        self.verticalLayout = QtWidgets.QVBoxLayout(ExceptionScriptSelector)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(ExceptionScriptSelector)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.selected_scripts = QtWidgets.QListWidget(ExceptionScriptSelector)
        self.selected_scripts.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selected_scripts.setObjectName("selected_scripts")
        self.verticalLayout_2.addWidget(self.selected_scripts)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.threshold_label = QtWidgets.QLabel(ExceptionScriptSelector)
        self.threshold_label.setObjectName("threshold_label")
        self.horizontalLayout_2.addWidget(self.threshold_label)
        self.weighting_selector = QtWidgets.QSpinBox(ExceptionScriptSelector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weighting_selector.sizePolicy().hasHeightForWidth())
        self.weighting_selector.setSizePolicy(sizePolicy)
        self.weighting_selector.setMaximumSize(QtCore.QSize(50, 16777215))
        self.weighting_selector.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weighting_selector.setMaximum(100)
        self.weighting_selector.setObjectName("weighting_selector")
        self.horizontalLayout_2.addWidget(self.weighting_selector)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.move_up = QtWidgets.QToolButton(ExceptionScriptSelector)
        self.move_up.setText("")
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-up.png")
        self.move_up.setIcon(icon)
        self.move_up.setObjectName("move_up")
        self.verticalLayout_3.addWidget(self.move_up)
        self.add_script = QtWidgets.QToolButton(ExceptionScriptSelector)
        self.add_script.setText("")
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-previous.png")
        self.add_script.setIcon(icon)
        self.add_script.setObjectName("add_script")
        self.verticalLayout_3.addWidget(self.add_script)
        self.remove_script = QtWidgets.QToolButton(ExceptionScriptSelector)
        self.remove_script.setText("")
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-next.png")
        self.remove_script.setIcon(icon)
        self.remove_script.setObjectName("remove_script")
        self.verticalLayout_3.addWidget(self.remove_script)
        self.move_down = QtWidgets.QToolButton(ExceptionScriptSelector)
        self.move_down.setText("")
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-down.png")
        self.move_down.setIcon(icon)
        self.move_down.setObjectName("move_down")
        self.verticalLayout_3.addWidget(self.move_down)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(ExceptionScriptSelector)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.available_scripts = QtWidgets.QListWidget(ExceptionScriptSelector)
        self.available_scripts.setObjectName("available_scripts")
        self.verticalLayout_4.addWidget(self.available_scripts)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.button_box = QtWidgets.QDialogButtonBox(ExceptionScriptSelector)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(ExceptionScriptSelector)
        QtCore.QMetaObject.connectSlotsByName(ExceptionScriptSelector)

    def retranslateUi(self, ExceptionScriptSelector):
        _translate = QtCore.QCoreApplication.translate
        ExceptionScriptSelector.setWindowTitle(_("Exception Script Selector"))
        self.label.setText(_("Selected Scripts"))
        self.threshold_label.setText(_("Selected script match threshold:"))
        self.move_up.setToolTip(_("Move selected script up"))
        self.add_script.setToolTip(_("Add to selected scripts"))
        self.remove_script.setToolTip(_("Remove selected script"))
        self.move_down.setToolTip(_("Move selected script down"))
        self.label_2.setText(_("Available Scripts"))
