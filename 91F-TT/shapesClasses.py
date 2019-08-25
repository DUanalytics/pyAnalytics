#Topic:
#-----------------------------
#http://www.greenteapress.com/thinkpython/html/book016.html

class Rectangle(object):
    """represent a rectangle. 
       attributes: width, height, corner
    """
box = Rectangle()
box.width = 100.0
box.height = 200.0

class Point(object):
    """represents a point in 2-D space"""
print(Point)  

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
