import turtle

def initialize_plotter(width, height, min_x, max_x, min_y, max_y):
    global x_begin, x_end, x_increment

    turtle.delay(0)

    x_begin, x_end = min_x, max_x

    turtle.setup(width=width, height=height)

    turtle.screensize(width, height)

    turtle.setworldcoordinates(min_x, min_y, max_x, max_y)

    x_increment = (max_x - min_x)/width

    turtle.hideturtle()

    # draw x axis
    turtle.pencolor('black')
    
    turtle.penup()

    turtle.setposition(min_x, 0) # move the pen to the left center

    turtle.setheading(0) #aim the pen to the right

    turtle.pendown()

    turtle.forward(max_x - min_x) # draw a line left to right

    #draw y axis
    turtle.penup()

    turtle.setposition(0, min_y) # move the pen to the center bottom

    turtle.setheading(90) # aim up

    turtle.pendown() # draw line bottom to top

    turtle.forward(max_y - min_y)


def plot(f, color):
    """ Plots function F on the cartesian coordinate plane established by 
        initialize_plotter. Plots (x, f(x)),
        for all x in the range x_begin <= x x_end.
        The color parameter dictates the curve's color. """

    # move the pen to the starting position
    turtle.penup()
    turtle.setposition(x_begin, f(x_begin))

    turtle.pencolor(color)
    turtle.pendown()

    x = x_begin
    while x < x_end:
        turtle.setposition(x, f(x))
        x += x_increment # next x 

def finish_plotting():
    turtle.exitonclick()

def quad(x): # Quadratic function (parabola)
    return 1/2 * x**2 + 3

def main():
    """ Provides a simple test of plot function . """
    from  math import sin
    initialize_plotter(600, 600, -10, 10, -10, 10)

    # Plot f(x) = 1/2*x + 3, for -10 <= x < 100

    plot(quad, 'red')

    # Plot f(x) = x, for -10 <= x < 100
    plot(lambda x:x, 'blue')

    plot(lambda x: 3*sin(x), 'green')
    finish_plotting()

if __name__ == '__main__':
    main()