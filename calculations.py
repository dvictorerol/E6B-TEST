from math import sin, cos, asin, sqrt, pow, pi

def wind_correction_angle(v_w : float, w : float, d : float, v_a : float, angle_unit : str):

    """

    Returns the wind correction angle in degrees or radians

    v_w : wind speed

    w : wind direction

    d : desired course

    v_a : true airspeed

    angle_unit : degrees or radians

    """

    if angle_unit == "degrees":
        return asin(v_w * sin((w  - d) * pi / 180) / v_a) * 180 / pi
    
    elif angle_unit == "radians":
        return asin(v_w * sin(w  - d) / v_a) 
    

def true_ground_speed(v_w : float, w : float, d : float, v_a : float, angle_unit : str):

    """

    returns the true ground speed

    v_w : wind speed

    w : wind direction

    d : desired course

    v_a : true airspeed

    angle_unit : degrees or radians

    """

    delta_a = wind_correction_angle(v_w, w, d, v_a, angle_unit)

    if angle_unit == "degrees":
        return sqrt(pow(v_a, 2) + pow(v_w, 2) - 2 * v_a * v_w * cos((d - w + delta_a) * pi / 180))
    
    elif angle_unit == "radians":
        return sqrt(pow(v_a, 2) + pow(v_w, 2) - 2 * v_a * v_w * cos(d - w + delta_a))
    


