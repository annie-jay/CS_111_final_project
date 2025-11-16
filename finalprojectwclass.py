# Intro CS Final Project
# authors: Jasper and Annie
# Part 1

from graphics import *
import random
import math
import unittest
import time 

def getRandomWord():
    """
        input: word list
        output: correctWord
        side effect: graphs window with word message
    """
    #wordlist = ["dog", "house", "sun", "cat", "boat"]
    #return random.choice(wordlist)

    # hardcodeing one work for testing purposes
    return "dog"

def isEnterClicked(win): 
        pointClicked = win.getMouse() 
        x = pointClicked.getX()
        y = pointClicked.getY()
        if (x > 1.9) and (x < 2.75) and (y > 0) and (y < .25):
            return True
        return False

class PictionaryBoard:
    def __init__(self, width, height, name):
        self.win = GraphWin(name, width, height)
        self.instructions = Text(Point(1.375, 1.75), "Welcome!")
        self.inputBox = Entry(Point(.92,0.14), 18)
        self.colorWheel = Image(Point(1.375, 5.3), "colorwheel.gif")
        self.enterButton = Rectangle(Point(1.9, 0), Point(2.75, .25))
    

    def drawBoard(self):
        """
            Generate user interface
        """
        self.win.setCoords(-0.25, -0.25, 10.25, 7.25) # give a little buffer, w/o buffer, board is 10x7
        self.win.setBackground("thistle")

        # making space for drawing
        drawingSpace = Rectangle(Point(10,7), Point(3,2))
        drawingSpace.setOutline("black")
        drawingSpace.setFill("seashell")
        drawingSpace.draw(self.win)

        # making bar with shape options (legend)
        legendOutline = Rectangle(Point(10,1.75), Point(3,0))
        legendOutline.setOutline("black")
        legendOutline.draw(self.win)

        line1 = Line(Point(4.4, 0), Point(4.4, 1.75))
        line1.draw(self.win)
        line2 = Line(Point(5.8, 0), Point(5.8, 1.75))
        line2.draw(self.win)
        line3 = Line(Point(7.2, 0), Point(7.2, 1.75))
        line3.draw(self.win)
        line4 = Line(Point(8.6, 0), Point(8.6, 1.75))
        line4.draw(self.win)

        pt = Circle(Point(3.7,0.875), 0.06)
        pt.setFill("black")
        pt.draw(self.win)
        line = Line(Point(4.6, 0.2), Point(5.6, 1.55))
        line.setWidth(2)
        line.draw(self.win)
        circ = Circle(Point(6.5, 0.875), 0.5)
        circ.setWidth(2)
        circ.draw(self.win)
        rect = Rectangle(Point(7.4, 0.2), Point(8.4, 1.55))
        rect.setWidth(2)
        rect.draw(self.win)
        poly = Polygon(Point(9, 0.2), Point(9.6, 0.2), Point(9.8, 0.875), Point(9.6, 1.55), Point(9, 1.55), Point(8.8, 0.875))
        poly.setWidth(2)
        poly.draw(self.win)

        # making text entry box
        self.inputBox.draw(self.win)
        self.enterButton.setFill("seashell")
        self.enterButton.draw(self.win)
        enterButtonText = Text(Point(2.15, 0.125), "Enter")
        enterButtonText.draw(self.win)
        
        # making instruction box
        intructionsOutline = Rectangle(Point(2.75, 0.5), Point(0,3))
        intructionsOutline.setOutline("black")
        intructionsOutline.draw(self.win)
        self.instructions.setSize(18)
        self.instructions.draw(self.win)

        # drawing color wheel 
        self.colorWheel.draw(self.win)


    def drawPolygon(self):
        """
            input: window
            output: none
            side effect: draws shape based on user clicks and inputs
        """
        self.instructions.setText("How many points \n will your polygon be? \n Press enter to confirm")
        while isEnterClicked(self.win) == False: 
            self.instructions.setText("You didn't click enter")
        numPoints = int(self.inputBox.getText())
        self.instructions.setText("Click on the color wheel to select your color!")
        pointClicked = self.win.getMouse() 
        x = pointClicked.getX()
        y = pointClicked.getY()
        r, g, b = self.colorWheel.getPixel(x, y)
        color = color_rgb(r, g, b)
            
        pointList = []
        for i in range(numPoints): # collecting points for polgon, drawing them as they are clicked
            point = self.win.getMouse()
            pointList.append(point)
            xVal = point.getX()
            yVal = point.getY()
            pointDraw = Point(xVal, yVal)
            pointDraw.draw(self.win)

        poly = Polygon(pointList)
        poly.setWidth(3)
        poly.setFill(color)
        poly.draw(self.win)

    def distanceBetweenTwoPoints (self, point1, point2):
        """
            input: two points 
            output: distance 
            side effect: calculates the distance between two points 
            This will give us the radius of the circle!
        """
        x1 = point1.getX()
        y1 = point1.getY()
        x2 = point2.getX()
        y2 = point2.getY()

        p1 = math.pow((x2-x1), 2)
        p2 = math.pow((y2-y1), 2)
        
        line = math.sqrt(p1+p2)
        return line

    def drawCircle(self):
        """
            input: window
            output: none
            side effect: draws circle based on user clicks and inputs
        """

        color = input("What color do you want your circle to be? (red, orange, yellow, green, blue, or purple) ")
        
        print("Click where you want the center of your circle to be")
        center = self.win.getMouse()
        centerDraw = Point(center.getX(), center.getY())
        centerDraw.draw(self.win)

        print("Click where you want the radius to extend out to.")
        point2 = self.win.getMouse()
        radius = self.distanceBetweenTwoPoints(center, point2)

        circ = Circle(center, radius)
        circ.setFill(color)
        circ.draw(self.win)


    def drawRectangle(self):
        """
            input: window
            output: none
            side effect: draws circle based on user clicks and inputs
        """
        color = input("What color do you want your rectangle to be? (red, orange, yellow, green, blue, or purple) ")

        print("click on the top right point of your rectangle ")
        point1 = self.win.getMouse()
        point1Draw = Point(point1.getX(), point1.getY())
        point1Draw.draw(self.win)

        print("click on the bottom left point of your rectangle ")
        point2 = self.win.getMouse()
        point2Draw = Point(point2.getX(), point2.getY())
        point2Draw.draw(self.win)

        rect = Rectangle(point1, point2)
        rect.setFill(color)
        rect.draw(self.win)


    def drawLine(self):
        """
            input: window
            output: none
            side effect: draws line based on user clicks and inputs
        """
        color = input("What color do you want your line to be? (red, orange, yellow, green, blue, or purple) ")

        print("Click the beginning of the line")
        point1 = self.win.getMouse()
        point1Draw = Point(point1.getX(), point1.getY())
        point1Draw.draw(self.win)

        print("Click the end of the line")
        point2 = self.win.getMouse()
        point2.draw(self.win)
        point2Draw = Point(point2.getX(), point2.getY())
        point2Draw.draw(self.win)

        line = Line(point1, point2)
        line.setFill(color)
        line.setWidth(3)
        line.draw(self.win)

    def drawPoint(self):
        """
            input: window
            output: none
            side effect: draws point based on user clicks and inputs
        """
        color = input("What color do you want your point to be? (red, orange, yellow, green, blue, or purple) ")

        size = 0.1*(int(input("What size do you want your point to be? (1-5) ")))

        print("Click where you want your point")
        pt = self.win.getMouse()
        pt = Point(pt.getX(), pt.getY())

        mainPt = Circle(pt, size)
        mainPt.setFill(color)
        mainPt.draw(self.win)
        

    def drawShapes(self):
        """ 
        input: window
        output: none
        side effect: Calls different draw shape functions based on where user clicks on the board
        """
        # message that says click on shape to draw it!
        for i in range(1): 
            pointClicked = self.win.getMouse()
            x = pointClicked.getX()
            y = pointClicked.getY()
            print(f"your point is {x},{y} !")

            if (x > 3) and (x < 4.4) and (y > 0) and (y < 1.75):
                self.drawPoint()
            elif (x > 4.4) and (x < 5.8) and (y > 0) and (y < 1.75):
                self.drawLine()
            elif (x > 5.8) and (x < 7.2) and (y > 0) and (y < 1.75):
                self.drawCircle()
            elif (x > 7.2) and (x < 8.6) and (y > 0) and (y < 1.75):
                self.drawRectangle()
            elif (x > 8.6) and (x < 10) and (y > 0) and (y < 1.75):
                self.drawPolygon()
            continue
            #else:
                #message says click on shape to draw

def getAndCheckGuess(correct_word, interface):
    """
        input: guess
        output: ture or false
        side effect: updates guessVaule: ends game if guessValue == true,
            takes away life if guessValue == false
    """

    guess = interface.inputBox.getText()

    if guess == correct_word:
        return True
    else:
        return False



def takeTurn(Player1, Player2, interface):
    """
   Manages a single turn for a player, either player 1 or player 2
    """

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

        input("Drawer, you have 30 seconds to draw. Press enter key to start drawing. Press enter button on interface when time is up.")
        interface.drawShapes()

        pointClicked = interface.win.getMouse() 
        x = pointClicked.getX()
        y = pointClicked.getY()
        if (x > 1.9) and (x < 2.75) and (y > 0) and (y < .25):
            if getAndCheckGuess(correct_word, interface):
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

# Unit test code!
class Test_Happy(unittest.TestCase):

    def test1(self):
        expected = "dog"
        actual = getRandomWord()
        self.assertEqual(expected, actual)

    def test2(self):
        expected = True
        actual = getAndCheckGuess("dog")
        self.assertEqual(expected, actual)

    

def main():

    # unit test
    # unittest.main(verbosity=2)

    # Set up the board
    interface = PictionaryBoard(1000, 700, "Pictionary")
    interface.drawBoard()


    #print("the random word is:", currentword) ### TEST###

    # players take turns

    # Player 1's Turn
    takeTurn("Player 1", "Player 2", interface)

    # # Player 2's Turn
    takeTurn("Player 2", "Player 1", interface)

    interface.win.getMouse()
    interface.win.close()
    # # Game end ( this is place holder, function not coded yet)
    # print("\nGame Over! Thanks for playing.")
    # print("Click on the window to close.")





if __name__ == "__main__":
    main()


