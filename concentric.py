from turtle import*
s=Screen()
s.setup(1000,700)                                     # screen coordinates
colors=['purple','red']
pencolor('green')
pensize(5)
for i in range(6,0,-1):
    penup()                                           #move pen up from the screen
    setpos(0,-20*i)                                   #move to a position on y axis
    pendown()                                         #put pen down 
    fillcolor(colors[i%2])
    begin_fill()                                     #create circle with different radiusa s i changes with every loop itteration
    circle(20*i)                                            
    end_fill()
mainloop()