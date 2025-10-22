# Intro CS Final Project

from graphics import *
import random
import math


def getRandomWord():
    """
        input: word list
        output: correctWord
        side effect: graphs window with word message
    """
    wordlist = ["dog", "house", "sun", "cat", "boat"]
    return random.choice(wordlist)


def drawMainBoard(win):
    """
        Generate user interface
    """
    win.setCoords(-0.25, -0.25, 10.25, 7.25) # give a little buffer, w/o buffer, board is 10x7
    win.setBackground("white")

    # making space for drawing
    drawingSpace = Rectangle(Point(10,7), Point(3,2))
    drawingSpace.setOutline("black")
    drawingSpace.draw(win)

    # making bar with shape options (legend)
    legendOutline = Rectangle(Point(10,1.75), Point(3,0))
    legendOutline.setOutline("black")
    legendOutline.draw(win)


def drawPolygon(win):
    """
        input: window
        output: none
        side effect: draws shape based on user clicks and inputs
    """
    numPoints = int(input("How many points will your polygon be? "))
    color = input("What color do you want your polygon to be? (red, orange, yellow, green, blue, or purple) ")
    
    pointList = []
    for i in range(numPoints): # collecting points for polgon, drawing them as they are clicked
        point = win.getMouse()
        pointList.append(point)
        xVal = point.getX()
        yVal = point.getY()
        pointDraw = Point(xVal, yVal)
        pointDraw.draw(win)

    poly = Polygon(pointList)
    poly.setWidth(3)
    poly.setFill(color)
    poly.draw(win)

def lineFromTwoPoints (point1, point2):
    x1 = point1.getX()
    y1 = point1.getY()
    x2 = point2.getX()
    y2 = point2.getY()

    p1 = math.pow((x2-x1), 2)
    p2 = math.pow((y2-y1), 2)
    
    line = math.sqrt(p1+p2)
    return line

def drawCircle(win):
    """
        input: window
        output: none
        side effect: draws circle based on user clicks and inputs
    """

    color = input("What color do you want your circle to be? (red, orange, yellow, green, blue, or purple) ")
    
    print("Click where you want the center of your circle to be")
    center = win.getMouse()
    centerDraw = Point(center.getX(), center.getY())
    centerDraw.draw(win)

    print("Click where you want the radius to extend out to.")
    point2 = win.getMouse()
    radius = lineFromTwoPoints(center, point2)

    circ = Circle(center, radius)
    circ.setFill(color)
    circ.draw(win)


def drawRectangle(win):
    """
        input: window
        output: none
        side effect: draws circle based on user clicks and inputs
    """
    color = input("What color do you want your rectangle to be? (red, orange, yellow, green, blue, or purple) ")

    print("click on the top right point of your rectangle ")
    point1 = win.getMouse()
    point1Draw = Point(point1.getX(), point1.getY())
    point1Draw.draw(win)

    print("click on the bottom left point of your rectangle ")
    point2 = win.getMouse()
    point2Draw = Point(point2.getX(), point2.getY())
    point2Draw.draw(win)

    rect = Rectangle(point1, point2)
    rect.setFill(color)
    rect.draw(win)


def drawLine(win):
    """
        input: window
        output: none
        side effect: draws line based on user clicks and inputs
    """
    color = input("What color do you want your line to be? (red, orange, yellow, green, blue, or purple) ")

    print("Click the beginning of the line")
    point1 = win.getMouse()
    point1Draw = Point(point1.getX(), point1.getY())
    point1Draw.draw(win)

    print("Click the end of the line")
    point2 = win.getMouse()
    point2.draw(win)
    point2Draw = Point(point2.getX(), point2.getY())
    point2Draw.draw(win)

    line = Line(point1, point2)
    line.setFill(color)
    line.setWidth(3)
    line.draw(win)

def drawPoint(win):
    """
        input: window
        output: none
        side effect: draws point based on user clicks and inputs
    """
    color = input("What color do you want your point to be? (red, orange, yellow, green, blue, or purple) ")

    size = input("What size do you want your point to be? (1-5) ")

    print("Click where you want your point")
    pt = win.getMouse()
    pt = Point(pt.getX(), pt.getY())

    mainPt = Circle(pt, size)
    mainPt.setFill(color)
    mainPt.draw(win)
    







# #def colorWheel():
#     color_image = Image(Point(0, 0), "colorwheel.gif")

#     color_image.draw(win)
#     return color_image


def getAndCheckGuess(correct_word):
    """
        input: guess
        output: none
        side effect: updates guessVaule: ends game if guessValue == true,
            takes away life if guessValue == false
    """

    guess = input("Enter your guess. Please type in lowercase: ")

    if guess == correct_word:
        return True
    else:
        return False


def takeTurn(Player1, Player2, win):
    """
   Manages a single turn for a player, either player 1 or player 2
    """
    # adding this just while making the board
    win.getMouse()
    win.close()

    # Start Round 1
    print("--------------------------------")
    print("It is", Player1, "'s turn to draw!")
    input("Guesser, please look away. Drawer, press Enter when you are ready.")

    correct_word = getRandomWord()
    print("The word to draw is:", correct_word)
    print("The guesser will have 3 lives.")
    print("--------------------------------")


    # Draw and guess loop

    correct_guess_made = False

    for i in range(3):
        guesses_left = 3 - i
        print("\nGuesser has", guesses_left, "guesses left")


        input("Drawer, you have 30 seconds to draw. Press Enter when time is up.")


        input("Okay, time to guess! Guesser, press Enter when you are ready.")

        if getAndCheckGuess(correct_word):
            print("That's correct! Great work!")
            correct_guess_made = True
            break
        else:
            print("Not quite! Let's give the drawer more time.")


    if correct_guess_made != True:
        print("\nYou're out of guesses! The word was:", correct_word)

    print("Round Over.")
    
    



def gameOver():
    """
        input: none
        output: none
        side effect: if lives == 0, or guessValue == true, ends game
    """
    pass



def main():
    # Set up the board
    win = GraphWin("Pictionary", 1000, 700)
    drawMainBoard(win)

    # testing code
    drawLine(win)
    drawPoint(win)
    drawPolygon(win)
    drawRectangle(win)
    drawCircle(win)
    drawLine(win)
    # drawPoint(win)

    #print("the random word is:", currentword) ### TEST###

    # players take turns

    # Player 1's Turn
    takeTurn("Player 1", "Player 2", win)

    # Player 2's Turn
    takeTurn("Player 2", "Player 1", win)


    # Game end
    print("\nGame Over! Thanks for playing.")
    print("Click on the window to close.")
    win.getMouse()
    win.close()



if __name__ == "__main__":
    main()


