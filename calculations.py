from math import sin, cos, asin, sqrt, pow, pi

def wind_correction_angle(v_w, w, d, v_a, angle_unit):

    """
    Comment
    """

    if angle_unit == "degrees":
        return asin(v_w * sin((w  - d) * pi / 180) / v_a) * 180 / pi
    
    elif angle_unit == "radians":
        return asin(v_w * sin(w  - d) / v_a) 
    

def true_ground_speed(v_w, w, d, v_a, angle_unit):

    """
    Comment
    """

    delta_a = wind_correction_angle(v_w, w, d, v_a, angle_unit)

    if angle_unit == "degrees":
        return sqrt(pow(v_a, 2) + pow(v_w, 2) - 2 * v_a * v_w * cos((d - w + delta_a) * pi / 180))
    
    elif angle_unit == "radians":
        return sqrt(pow(v_a, 2) + pow(v_w, 2) - 2 * v_a * v_w * cos(d - w + delta_a))
    



print(wind_correction_angle(23, 90, 320, 100, "degrees"))

print(true_ground_speed(23, 90, 320, 100, "degrees"))