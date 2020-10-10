
def transformacion(r,theta,fi):
    from math import  sin, cos

    x=r*sin(theta)*cos(fi)
    y=r*sin(theta)*sin(fi)
    z=r*cos(theta)
    print(x,y,z)

