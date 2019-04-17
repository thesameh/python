import math 
from decimal import Decimal
# aX + bY = c
# dX + eY = f

# a = 2
# b = -3
# c = 1
# d = 5
# e = 2
# f = 31

def douple_XY(a,b,c,d,e,f,):

    if a and b and c and d and e and f :
        a=float(a)
        b=float (b)
        c=float (c)
        d=float (d)
        e=float (e)
        f=float (f)
        # print equation with given nr
        print('Equation: \n' , a,'X + ',b,'j = ',c,' \n',d,'X + ',e,'j = ',f,'\n')
        # do the magic 
        x = (c - (b * 1j) )/a
        # print X 
        print('X = (',c,'-',b,'j)/',a ,'\nX = ', x ,'\n')

        # put x in the second equation 
        t = (d * x ) + (e * 1j)
        print(d,x,' + ',e,'j = ',f,'\n')
        # print the new form of the equation 
        rel = t.real
        img = t.imag    
        print('j = (',f ,' - ',rel,')/',img,'\n')
        # do the magic
        t = (f - rel )/img
        # print everything 
        print('j = ' ,t,'\n')
        # now get x again 
        print('X = (' ,c,' - (',b,'*',t,'))/',a,'\n')
        # do the magic 
        x = (c - (b * t) )/a
        # print it  
        print('X = ', x)

