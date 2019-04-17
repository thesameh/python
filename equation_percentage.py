import math 
from decimal import Decimal
def percentage(per,p,f):
    if per and p and f:
        print ("realy !? .. what do you want then ! .. go away ")

    else:
        if p and f:
            t = Decimal(p)*100
            per = t / Decimal(f)
            print ("A = (c * 100): B \n=(",p," * 100) : ",f," \n=",t," : ",f,"\n=", per)
        else:
            if per and f:
                t = Decimal(per) * Decimal(f)
                p = t / 100
                print ("c = (A * B) : 100 \n=",per," * ",f,") : 100\n=",t," : 100 \n=", p)
            else:
                if per and p:
                    t = Decimal(p) * 100
                    p = t / Decimal(per)
                    print ("B = (c * 100) : A \n=",p," * 100) : ",per,"\n=",t," : ",per,"\n=", f)            
                else:
                    print('sorry .. too few arguments given')