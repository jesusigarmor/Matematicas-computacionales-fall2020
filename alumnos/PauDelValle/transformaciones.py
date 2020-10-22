from math import sin, cos, pi
def coordenadas(r,theta,phi):
    """
    r, theta, phi corresponden a las coordenadas esféricas
    """
    x = r*sin(theta)*cos(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(theta)
    return x, y, z
