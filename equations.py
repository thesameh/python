
choice = input('PLease choose the equation Bou want to perform: \n' +
                '(1) C = A + B \n'+
                '(2) A% of B = C \n'+
                '(3) B^C = A \n'+
                '(4) aX + b = c\n'+
                '(5) aX + bj = c \n   '+
                    ' dX + ej = f\n' +
                'equation nr ? : ')


# simple addition 
if choice == '1':
    from equations_plus import plus
    print('equation forms: \nC = A + B \n'+
          'A = C - B \n'+
          'B = C - A \n')
    #inputs 
    var = input("inputs: \nA= ") or None
    var2 = input("\nB = ") or None
    var3 = input("\nC= ") or None
    # calculate 
    plus(var,var2 , var3)

# percentage 
if choice == '2':
    from equation_percentage import percentage
    print('equation forms : \nA% of B = C \n equation A = (C A 100): B ')
    # inputs 
    per = input("inputs: \nA = ") or None
    full = input("\nB : ") or None
    part = input("\nC= ") or None
    # calculate
    percentage(per,part , full)

# power and sqr root 
if choice == '3':
    from equation_squar_root import squar
    # \n\n\nequations: \n \n->  ->  \nB= 
    print('equation forms : \n'+
          'B^C = A \n'+
          'C√A = B \n'+
          'Log B (A) = C\n')
    # inputs 
    B= input("inputs: \nB= ") or None
    C = input("\nC= ") or None
    A = input("\nA= ") or None
    #calculate  
    squar(A,B ,C)



if choice == '4':
    from equation_1x import x1 
    a= input('equation forms : \naX + b = c \n'+
             'c - aX = b \n'+
             'aX = c - b \n'+
             'inputs: \na= ') or None
    b = input("\nb= ") or None
    c = input("\nc= ") or None

    x1(a,b,c,)

if choice == '5':
    from equation_douple_XY import douple_XY 
    print('Equation: /n ' +
      'aX + bj = c \n'+
      'dX + ej = f\n' +
      'inputs: \n')  

    a = input('a = ')
    b = input('b = ')
    c = input('c = ')
    d = input('d = ')
    e = input('e = ')
    f = input('f = ')

    douple_XY(a,b,c,d,e,f)