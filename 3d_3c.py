import turtle
import datetime

##################################################################
def printTimeStamp(name):                                       ##
 print('Автор програми: ' + name)                               ##
 print('Час компіляції: ' + str(datetime.datetime.now()) +"\n") ##
printTimeStamp('Beliaev and Pereviznyk')                        ##
##################################################################

def draw_triangle(vertices,color,iturtle): ### Малює трикутник 
    iturtle.speed(10)
    iturtle.fillcolor(color)
    iturtle.up()
    iturtle.goto(vertices[0][0],vertices[0][1])
    iturtle.down()
    iturtle.begin_fill()
    iturtle.goto(vertices[1][0],vertices[1][1])
    iturtle.goto(vertices[2][0],vertices[2][1])
    iturtle.goto(vertices[0][0],vertices[0][1])
    iturtle.end_fill()
    
def midpoint(point1, point2): 
    return [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]
    
def draw_fractal(vertices,level,iturtle): ###Малює фрактал

    colors = [(210,122,160),(251,231,166),(255,250,246),(49, 167, 83),(185, 8, 64),
                (23,31,101),(51,187,204)]
    draw_triangle(vertices,colors[level],iturtle)

    if level > 0:

        draw_fractal([vertices[0],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                      level - 1, iturtle)
        draw_fractal([vertices[1],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[1], vertices[2])],
                      level - 1, iturtle)
        draw_fractal([vertices[2],
                      midpoint(vertices[2], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                      level - 1, iturtle)

iturtle = turtle.Turtle()
iturtle.shape('turtle')
screen = turtle.Screen()
screen.colormode(255)
vertices = [[-200, -100], [0, 200], [200, -100]]
level = 5
draw_fractal(vertices, level, iturtle)
screen.exitonclick()

