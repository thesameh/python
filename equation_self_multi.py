from functools import reduce
def self_mult(x , t ):
   
    i = 1
    s = []
    while i <= t :
        s.append(x)

        if i == t:
            summ = reduce(lambda z, y: z*y, s) 
            return summ
        i+= 1
