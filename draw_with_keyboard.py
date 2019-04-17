import turtle
i = 32
print('w: forward 10 /nl: forward 100\nd:right 10deg \na: left10 deg\nu: turn 180 deg')
while i :
    d = input('go: ')
    if d == 'w':
        turtle.forward(10)
    if d == 'd':
        turtle.right(10)
        
    if d == 'a':
        turtle.left(10)
        
    if d == 'u':
        turtle.left(180)
    if d == 'l':
        turtle.forward(100)