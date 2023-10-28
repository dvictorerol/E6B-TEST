from PyQt5.QtCore import pyqtSignal, QObject
from calculations import wind_correction_angle, true_ground_speed


class Backend(QObject):

    return_values = pyqtSignal(float, float)
    def __init__(self):
        super().__init__()


    def calculate(self, v_w : float, w : float, d : float, v_a : float, angle_unit : str):

        if v_a == 0:
             self.return_values.emit(0, 0)

        elif v_a > 0:
            delta_a = wind_correction_angle(v_w, w, d, v_a, angle_unit)
            v_g = true_ground_speed(v_w, w, d, v_a, angle_unit)
            self.return_values.emit(round(delta_a, 2), round(v_g, 2))

