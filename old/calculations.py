from math import sin, cos, asin, sqrt, pow, pi

def wind_correction_angle(v_w : float, w : float, d : float, v_a : float) -> float:

    """

    Returns the wind correction angle in degrees

    v_w : wind speed

    w : wind direction

    d : desired course

    v_a : true airspeed

    angle_unit : in degrees

    """

   

    asin_param = v_w * sin((w  - d) * pi / 180) / v_a

    if asin_param >= 0:
        asin_param = min(asin_param, 1)
    
    else:

        asin_param = max(asin_param, -1)
        
    return asin(asin_param) * 180 / pi

    


def true_ground_speed(v_w : float, w : float, d : float, v_a : float) -> float:

    """

    Returns the true ground speed

    v_w : wind speed

    w : wind direction

    d : desired course

    v_a : true airspeed

    angle_unit : in degrees

    """

    delta_a = wind_correction_angle(v_w, w, d, v_a)

    return sqrt(pow(v_a, 2) + pow(v_w, 2) - 2 * v_a * v_w * cos((d - w + delta_a) * pi / 180))
    
    