from PyQt5.QtCore import pyqtSignal, QObject
from calculations import wind_correction_angle, true_ground_speed


class Backend(QObject):

    return_values = pyqtSignal(float, float)
    def __init__(self):
        super().__init__()


    def calculate(self, v_w : float, w : float, d : float, v_a : float):

        if v_a == 0:
             self.return_values.emit(0, 0)

        elif v_a > 0:
            delta_a = wind_correction_angle(v_w, w, d, v_a)
            v_g = true_ground_speed(v_w, w, d, v_a)
            self.return_values.emit(round(delta_a, 2), round(v_g, 2))

