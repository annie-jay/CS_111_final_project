# Intro CS Final Project

from graphics import *
import random


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
        input: none
        output: none
        side effect: draws shape based on user clicks and inputs
    """
    numPoints = int(input("How many points will your polygon be? "))
    color = input("What color do you want your polygon to be? (red, orange, yellow, green, blue, or purple) ")
    pointList = []
    for i in range(numPoints):
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

def drawCircle(win):
    """
        input: none
        output: none
        side effect: draws circle based on user clicks and inputs
    """
    print("Click where you want the center of your circle to be")
    center = win.getMouse()

    print("Click where you want the radius to extend out to.")

def drawRect():
    pass

def drawLine():
    pass
def drawOval():
    pass


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
    drawPolygon(win)

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


