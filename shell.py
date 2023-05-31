from turtle import*
pencolor('blue')
pensize(3)
fillcolor('red')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)                     #creates circle of the radius entered in the brackets
    lt(25)                           #shifts circle center by 25 degrees
    end_fill()
mainloop()