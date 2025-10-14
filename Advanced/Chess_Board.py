
# This Python mini-project uses the `turtle` graphics library to draw an 8x8 chess board.

import turtle

screen = turtle.Screen()
pencil = turtle.Turtle()

def draw_square():
    for i in range(4):
        pencil.forward(30)
        pencil.left(90)
    pencil.forward(30)

if __name__ == "__main__":
    screen.setup(600, 600)
    pencil.speed(0)
    
    for index in range(8):
        for second_index in range(8):
            
            if (index + second_index) % 2 == 0:
                colour = 'black'
            else:
                colour = 'white'

            pencil.up()
            pencil.setpos(30 * second_index, 30 * index)
            pencil.down()

            pencil.fillcolor(colour)
            pencil.begin_fill()
            draw_square()
            pencil.end_fill()

    pencil.hideturtle()
    screen.mainloop()
