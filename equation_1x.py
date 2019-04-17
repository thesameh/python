import math 
from decimal import Decimal
def x1(a,b,c):
    if a and b and c :
        a = Decimal(a)
        b = Decimal(b)
        c = Decimal(c)
        t = Decimal(c - b)
        sum = t / a
        print( a , 'X + ',b,'=',c, '\n',
                a , 'X = ' , c ,' - ', b , '\n',
                a , 'X = ' ,t , '\n' ,
                'X = ' ,t ,' / ' ,a,'\n' ,
                'X =',sum)
    else:
        print('sorry .. too few arguments given')









