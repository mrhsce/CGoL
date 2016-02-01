###########################################################################
# MM          MM            HH      HH                  CCCCCCC  EEEEEEEE #
# MMMMM     MMMM  rr  rr    HH      HH     ssss        C         E        #
# MM  MM  MM  MM  rrrr  rr  HHHHHHHHHH  ss            C          EEEEEEEE #
# MM    MM    MM  rrr       HHHHHHHHHH    s           C          EEEEEEEE #
# MM          MM  rr        HH      HH     s  ss       C         E        #
# MM          MM  rr        HH      HH  sssss           CCCCCCC  EEEEEEEE #
###########################################################################
##                        Written in python 2.7
'''Program number: 61 Date: 31/1/2016 DtD: 9 Copyright:(c)MrHs 2016'''

#Comment :


import turtle
import time

scrn = turtle.Screen()


mainTurtle=turtle.Turtle()


def createCell(x,y,type):
    if(type):
           mainTurtle.shape("pics/alive.gif")
    else:
           mainTurtle.shape("pics/dead.gif")
    mainTurtle.goto(x,y)
    mainTurtle.stamp()

class tableCell:
    number=0
    def __init__(self,x,y,type):
        ######turle####
        #self.name=(li[0],li[1])
        self.turtle=turtle.Turtle()
        self.turtle.up()
        self.turtle.ht()
        self.turtle.speed(0)
        self.turtle.resizemode("user")
        if(type):
            self.turtle.shape("pics/alive.gif")
        else:
            self.turtle.shape("pics/dead.gif")
        self.turtle.shapesize(1,1)
        self.turtle.goto(x,y)
        self.turtle.stamp()

def initalizeScreen():
    #Turtle initializing
    scrn.delay(0)
    scrn.tracer(0,0)
    scrn.register_shape("pics/alive.gif")
    scrn.register_shape("pics/dead.gif")
    scrn.title("Conwoy Game of Life")

    mainTurtle.up()
    mainTurtle.ht()
    mainTurtle.speed(0)

def dimensionQuery():
    inputDim = input("Insert board dimension: width,height separated by comma: ")
    if(inputDim == "\n"):
        return (10,10)
    else:
        return (int(inputDim[0]),int(inputDim[1]))


def turtleInput(dimension):

    return """"""

def turtleOutput(board,x_dim,y_dim):
    scrn.clear()
    x_origin = -150
    y_origin = -150 + y_dim*30
    for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if board[y][x]:
                    createCell(x_origin + x*30,y_origin - y*30,True)
                else:
                    createCell(x_origin + x*30,y_origin - y*30,False)
    mainTurtle.goto(0,0)
    #scrn.update()
    time.sleep(1)




class Game(object):

    def __init__(self, state, infinite_board = True):

        self.state = state
        self.width = state.width
        self.height = state.height
        self.infinite_board = infinite_board

    def step(self, count = 1):

        for generation in range(count):

            new_board = [[False] * self.width for row in range(self.height)]

            for y, row in enumerate(self.state.board):
                for x, cell in enumerate(row):
                    neighbours = self.neighbours(x, y)
                    previous_state = self.state.board[y][x]
                    should_live = neighbours == 3 or (neighbours == 2 and previous_state == True)
                    new_board[y][x] = should_live

            self.state.board = new_board

    def neighbours(self, x, y):

        count = 0

        for hor in [-1, 0, 1]:
            for ver in [-1, 0, 1]:
                if not hor == ver == 0 and (self.infinite_board == True or (0 <= x + hor < self.width and 0 <= y + ver < self.height)):
                    count += self.state.board[(y + ver) % self.height][(x + hor) % self.width]

        return count

    def display(self):
        return self.state.display()
    def isFinished(self):
        return self.state.isFinalStep()

class State(object):

    def __init__(self, positions, x, y, width, height):

        active_cells = []

        for y, row in enumerate(positions.splitlines()):
            for x, cell in enumerate(row.strip()):
                if cell == 'o':
                    active_cells.append((x,y))

        board = [[False] * width for row in range(height)]

        for cell in active_cells:
            board[cell[1] + y][cell[0] + x] = True

        self.board = board
        self.width = width
        self.height = height

    def display(self):

        output = ''

        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if self.board[y][x]:
                    output += ' o'
                else:
                    output += ' .'
            output += '\n'

        return output

    def isFinalStep(self):

        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if self.board[y][x]:
                    return False

        return True


dims = dimensionQuery()
initalizeScreen()
glider = """ oo.
             o.o
             o.. """

my_game = Game(State(glider, x = 2, y = 3, width = dims[0], height = dims[1]))


while not my_game.isFinished():
    my_game.step(1)
    print my_game.isFinished()
    print my_game.display()
    turtleOutput(my_game.state.board,dims[0],dims[1])


