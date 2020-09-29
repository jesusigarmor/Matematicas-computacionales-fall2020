
def esfericas(r,o,p):
    pi = math.pi
    theta = o*pi
    phi = p*pi

    x = r*cos(theta)*sin(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(phi)
    
    return (x,y,z)
