from turtle import*
speed("fast")
for i in range(6):
 fd(100)
 circle(50)
 lt(360/6)
 for i in range(6):
    fd(50)
    lt(360/6)
    dot(10)

mainloop()


