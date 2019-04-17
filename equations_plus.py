import math 
from decimal import Decimal
def plus(var,var2,var3):
    if var and var2 and var3:
        print("now I have to correct you ")

        if Decimal(var3) == Decimal(var2) + Decimal(var):
            print(var ," + ", var2 ," = ", var3, " and that is correct")
        else:
           print("you think ",var ," + ", var2 ," = ", var3, "? HAHA you wish .. it's",Decimal(var2) + Decimal(var))

    else:
        if var and var2:
            print ("C = A + B\nC = " , Decimal(var) , "+",Decimal(var2),"\nC= ",Decimal(var)+Decimal(var2))
        else:
        
            if var2 and var3:
                print ("A = C - B\nA = " , Decimal(var3)," - ",Decimal(var2),"\nA= ",Decimal(var3)-Decimal(var2))
            else:
                if var and var3:
                    print ("B = C - A\nB =  " , Decimal(var3)," - ",Decimal(var),"\nB= ", Decimal(var3)-Decimal(var))
                else:
                    print("sorry too few arguments")
    
    

