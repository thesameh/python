import math 
from decimal import Decimal
def angle(x1 ,y1,x2,y2):
        
        x1 = Decimal(x1)
        x2 = Decimal(x2)
        y1 = Decimal(y1)
        y2 = Decimal(y2)
        if y1 == y2 :
            if x1 >= 0 and x2 <= 0 or x1 <= 0 and x2 >= 0:
                if x1==0 and x2 == 0:
                    return 0 
                        
                else:
                
                    return 180
            else:

                return 0
        else:

            t1 = (x2 - x1)
            t2 = (y2 - y1)
            tanAngle = t1 / t2
            tanAngle = math.degrees(math.atan(tanAngle))
            tanAngle =  90 - tanAngle


            return tanAngle
