import math 
from decimal import Decimal
from equation_self_multi  import self_mult
def squar(a,b ,c):
    # if the user inputs all vars 
    if a and b and c : 
        a = Decimal(a)
        b = Decimal(b)
        c = Decimal(c)
        # power b by c 
        sum = Decimal(self_mult(b , c))
        # check if the given value is right and if not output the right value 
        if a == sum :
            print('that\'s right' ,b ,"^", c ," = "  ,Decimal(self_mult(b , c))  )
        else:
            print("is realy ",b ,"^", c ," = "  ,a ," ? \nI think it's ", sum )
    
    else:
        if a and c :

            a= Decimal(a)
            c = Decimal(c)
            i = Decimal('0.000')
            sum = Decimal('0.000')

            while sum != a:

                sum = math.floor(Decimal(self_mult(i , c)))
                
                if sum == a:
                    print( c,"√",a," = ",i)

                else:
                    i+=Decimal('0.001')



            # print( "√",a," = ",math.sqrt(a))

        else:
            if b and c :
                b= Decimal(b)
                c = Decimal(c)
                sum = math.floor(Decimal(self_mult(b , c)))
                print(  b ,"^", c ," = "  , sum  )
            else:
                if b and a :
                    b= Decimal(b)
                    a = Decimal(a)
                    sum = math.log(a,b)
                    print('Log ',b,' (',a,') = ',sum)

                    
                else:
                    if a:
                        a= Decimal(a)
                        i = Decimal('0.000')
                        sum = Decimal('0.000')

                        while sum != a:
                            sum = math.floor(Decimal(i*i))
                            
                            if sum == a:
                                print("√",a," = ",i)

                            else:
                                i+=Decimal('0.001')
                    else:
                        print('sorry .. too few arguments given')