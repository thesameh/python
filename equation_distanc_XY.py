import math 
from decimal import Decimal
def dist(x1 ,y1,x2,y2):
    
    if x1 == x2 and y1 == y2:

        return 0 
    else:
        x1 = Decimal(x1)
        x2 = Decimal(x2)
        y1 = Decimal(y1)
        y2 = Decimal(y2)
        t1 = (x2 - x1)
        t1 = t1 * t1
        t2 = (y2 - y1)
        t2 = t2 * t2
        l = math.sqrt(t1 + t2)

        return l



    