import turtle
import math
from decimal import Decimal
from equation_distanc_XY import dist
from equation_angle_XY import angle
from equation_squar_root import squar
from draw_axis import draw_axis
draw_axis(300)
for i in range(0 , 100):
    x1 = i
    y1 = i*i
    print(x1 , y1)

    i = i+1
    x2 = i
    y2 = i*i
    print(x2 , y2)

    l = dist(x1,y1,x2,y2)

    a = angle(x1,y1,x2,y2)
    
    print('l=',l ,'a=', a)

    turtle.left(a)
    turtle.forward(l)
    turtle.right(a)
