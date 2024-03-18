from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal
import sys
from backend import Backend

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        self.backend = Backend()
        self.backend.return_values.connect(self.modify_text_boxes)
        self.connect_spinbox_signals()
        self.show()

    def connect_spinbox_signals(self):

        self.wind_speed.valueChanged.connect(self.spinbox_value_change)
        self.wind_direction.valueChanged.connect(self.spinbox_value_change)
        self.desired_course.valueChanged.connect(self.spinbox_value_change)
        self.true_airspeed.valueChanged.connect(self.spinbox_value_change)

    def spinbox_value_change(self):
        
        self.backend.calculate(self.wind_speed.value(), self.wind_direction.value(),
                               self.desired_course.value(), self.true_airspeed.value())
        self.arrow.resize(21, int(self.wind_speed.value() // 3))
    
    def modify_text_boxes(self, delta_a, v_g):

        self.wind_correction_angle.setPlainText(str(delta_a).replace('.', ','))
        self.true_ground_speed.setPlainText(str(v_g).replace('.', ','))
        
