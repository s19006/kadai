x = 12
y = "気温"
z = 22.4

def template(x, y, z):
    return '{}時の{}は{}'.format(x,y,z)


print(template(x, y, z))
