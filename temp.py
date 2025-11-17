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
    wordlist = ["dog", "house", "sun", "cat", "boat"]
    return random.choice(wordlist)

def isEnterClicked(pointClicked): 
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

        self.current_color = "black"
    

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


    def drawPolygon(self, color):
        """
            input: window, color
            output: none
            side effect: draws shape based on user clicks and inputs
        """
        self.instructions.setText("How many points \n will your polygon be? \n Press enter to confirm")
        
        pointClicked = self.win.getMouse()
        while isEnterClicked(pointClicked) == False: 
            self.instructions.setText("You didn't click \n enter. Please input \nnumber of points \n and click enter.")
            pointClicked = self.win.getMouse() 
            
        try: 
            numPoints = int(self.inputBox.getText())
            if numPoints < 3:
                self.instructions.setText("Please enter an \n integer greater than 3. \n Then click enter.")
                self.inputBox.setText("")

                pointClicked = self.win.getMouse()
                while isEnterClicked(pointClicked) == False:
                    self.instructions.setText("Click Enter to confirm.")
                    pointClicked = self.win.getMouse()
                numPoints = int(self.inputBox.getText())
        except:
            self.instructions.setText("Please enter an \n integer greater than 3.")
            self.inputBox.setText("")
            numPoints = 3 # default is simplest polygon
        self.inputBox.setText("")

        self.instructions.setText(f"Color is {color}. \n Click {numPoints} times.")

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

    def drawCircle(self, color):
        """
            input: window, color
            output: none
            side effect: draws circle based on user clicks and inputs
        """
        
        self.instructions.setText("Click where you want \n the center of your \n circle to be")
        center = self.win.getMouse()
        centerDraw = Point(center.getX(), center.getY())
        centerDraw.draw(self.win)

        self.instructions.setText("Click where you want \n the radius to \n extend out to.")
        point2 = self.win.getMouse()
        radius = self.distanceBetweenTwoPoints(center, point2)

        circ = Circle(center, radius)
        circ.setFill(color)
        circ.draw(self.win)

    def drawRectangle(self, color):
        """
            input: window, color
            output: none
            side effect: draws circle based on user clicks and inputs
        """
        self.instructions.setText("Click on the top \n right point of \n your rectangle ")
        point1 = self.win.getMouse()
        point1Draw = Point(point1.getX(), point1.getY())
        point1Draw.draw(self.win)

        self.instructions.setText("Click on the bottom \n left point of \n your rectangle ")
        point2 = self.win.getMouse()
        point2Draw = Point(point2.getX(), point2.getY())
        point2Draw.draw(self.win)

        rect = Rectangle(point1, point2)
        rect.setFill(color)
        rect.draw(self.win)


    def drawLine(self, color):
        """
            input: window, color
            output: none
            side effect: draws line based on user clicks and inputs
        """
        self.instructions.setText("Click the beginning \n of the line")
        point1 = self.win.getMouse()
        point1Draw = Point(point1.getX(), point1.getY())
        point1Draw.draw(self.win)

        self.instructions.setText("Click the end \n of the line")
        point2 = self.win.getMouse()
        point2Draw = Point(point2.getX(), point2.getY())
        point2Draw.draw(self.win)

        line = Line(point1, point2)
        line.setOutline(color)
        line.setWidth(3)
        line.draw(self.win)

    def drawPoint(self, color):
        """
            input: window, color
            output: none
            side effect: draws point based on user clicks and inputs
        """
        size = 0.1

        self.instructions.setText("Click where you \n want your point")
        pt = self.win.getMouse()
        pt = Point(pt.getX(), pt.getY())

        mainPt = Circle(pt, size)
        mainPt.setFill(color)
        mainPt.setOutline(color)
        mainPt.draw(self.win)
        

    def drawShapes(self):
        """ 
        input: window
        output: none
        side effect: Calls different draw shape functions based on where user clicks on the board
        """

        
        shapes_drawn = 0
        while shapes_drawn < 3:
            self.instructions.setText(f"Drawer: Click a color \n or a shape. \n Shapes drawn: {shapes_drawn}/3")
            
            pointClicked = self.win.getMouse()
            x = pointClicked.getX()
            y = pointClicked.getY()

            # if 
            #     r, g, b = self.colorWheel.getPixel(int(x), int(y))
            #     self.current_color = color_rgb(r, g, b)
            #     self.instructions.setText(f"Color set to \n {self.current_color}!")
            #     continue

            if (x > 3) and (x < 4.4) and (y > 0) and (y < 1.75):
                self.drawPoint(self.current_color)
                shapes_drawn = shapes_drawn + 1
            elif (x > 4.4) and (x < 5.8) and (y > 0) and (y < 1.75):
                self.drawLine(self.current_color)
                shapes_drawn = shapes_drawn + 1
            elif (x > 5.8) and (x < 7.2) and (y > 0) and (y < 1.75):
                self.drawCircle(self.current_color)
                shapes_drawn = shapes_drawn + 1
            elif (x > 7.2) and (x < 8.6) and (y > 0) and (y < 1.75):
                self.drawRectangle(self.current_color)
                shapes_drawn = shapes_drawn + 1
            elif (x > 8.6) and (x < 10) and (y > 0) and (y < 1.75):
                self.drawPolygon(self.current_color)
                shapes_drawn = shapes_drawn + 1
            else:
                if not (x > 3 and x < 10 and y > 2 and y < 7):
                    self.instructions.setText("That wasn't a button! \n Click a color or shape.")

        self.instructions.setText("You have drawn 3 shapes! \n Time for the guesser.")


def getAndCheckGuess(correctWord, interface):
    """
        input: guess
        output: ture or false
        side effect: updates guessVaule: ends game if guessValue == true,
            takes away life if guessValue == false
    """

    guess = interface.inputBox.getText()

    if guess.lower() == correctWord.lower():
        return True
    else:
        return False

class Player: 
    def __init__ (self, name, role):
        self.name = name
        self.role = role 
        self.guesses = 3
        self.correct_guess_made = False

    def draw (self, interface):
        interface.instructions.setText(f"{self.name}, draw 3 shapes!\n Click on a shape \n in the menu and \n follow the instructions.")
        interface.drawShapes()


    def guess(self, interface, correctWord):
        interface.instructions.setText(f"{self.name} ({self.guesses} left): \n type your guess and \n click the enter button")
        
        pointClicked = interface.win.getMouse() 
        while isEnterClicked(pointClicked) == False:
            interface.instructions.setText(f"Please click enter \n {self.name}. \n Guesses left: {self.guesses}")
            pointClicked = interface.win.getMouse() 
            
        interface.inputBox.setText("")
        if getAndCheckGuess(correctWord, interface):
            interface.instructions.setText("That is correct! \n Great work.")
            self.correct_guess_made = True
        else:
            self.guesses = self.guesses - 1 
            interface.instructions.setText(f"Not quite. \n {self.guesses} guesses left. \n Click Enter to continue")
            
            pointClicked = interface.win.getMouse()
            while isEnterClicked(pointClicked) == False:
                interface.instructions.setText("Click Enter to \n let the drawer \n continue.")
                pointClicked = interface.win.getMouse()

            interface.instructions.setText("")


    def returnGuesses(self):
        return self.guesses
    
    def returnGuessState(self):
        return self.correct_guess_made 



def takeTurn(Player1, Player2, interface):
    """
   Manages a single turn for a player, either player 1 or player 2
    """
    
    # Start Round 1
    print("--------------------------------")
    print("It is", Player1, "'s turn to draw!")
    input("Guesser, please look away. Drawer, press Enter when you are ready.")

    correctWord = getRandomWord()
    print("The word to draw is:", correctWord)
    print("The guesser will have 3 lives.")
    print("--------------------------------")

    
    

def isRoundOver(guesser):
    """
        input: none
        output: none
        side effect: if guesses == 0, or guessValue == true, ends game
    """
    if guesser.returnGuesses() == 0:
        return True 
    elif guesser.returnGuessState():
        return True 
    else:
        return False
    

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
        pass 
    

def main():

    # unit test

    # Set up the board for round 1
    interface = PictionaryBoard(1000, 700, "Pictionary")
    interface.drawBoard()

    interface.instructions.setText("Player 1, you are \n the guesser. Please \n enter your name.\n Then click enter button.")
    
    pointClicked = interface.win.getMouse()
    while isEnterClicked(pointClicked) == False:
        interface.instructions.setText("Please click enter.")
        pointClicked = interface.win.getMouse()

    name1 = interface.inputBox.getText()
    interface.inputBox.setText("")

    interface.instructions.setText("Player 2, you are \n the drawer. Please \n enter your name. \n Then click enter button.")
    
    pointClicked = interface.win.getMouse()
    while isEnterClicked(pointClicked) == False:
        interface.instructions.setText("Please click enter.")
        pointClicked = interface.win.getMouse()
        
    name2 = interface.inputBox.getText()
    interface.inputBox.setText("")


    player1 = Player(name1, "guesser")
    
    player2 = Player(name2, "drawer")

    correctWord = getRandomWord()
    
    interface.instructions.setText(f"{player2.name}, look at the \n terminal for your word! \n {player1.name}, look away!")

    print(f"{player2.name}, your word is: {correctWord}")

    input("Drawer, press Enter in the TERMINAL when you are ready to start...")


    while isRoundOver(player1) == False: 
        player2.draw(interface)
        player1.guess(interface, correctWord)


    if player1.returnGuessState():
        interface.instructions.setText(f"You win round 1! \n You will now switch roles.\n It is {name1}'s turn to draw. \n Click anywhere to start the next round")
    else: 
        interface.instructions.setText(f"You lose round 1! \n The word was {correctWord}. \n You will now switch roles.\n It is {name1}'s turn to draw.\n Click anywhere to start the next round")

    interface.win.getMouse()
    interface.win.close()
    
    # this is round 2
    interface = PictionaryBoard(1000, 700, "Pictionary")
    interface.drawBoard()

    interface.instructions.setText(f"{name2}, you are \n the guesser. {name1}, you are \n the drawer.")

    correctWord = getRandomWord()
    
    player1 = Player(name1, "drawer")
    player2 = Player(name2, "guesser")
 
    
    interface.instructions.setText(f"{player1.name}, look at the \n terminal for your word! \n {player2.name}, look away!")

    print(f"Drawer ({player1.name}), your word is: {correctWord}")
    input("Drawer, press Enter in the TERMINAL when you are ready to start...")


    while isRoundOver(player2) == False: 
        player1.draw(interface)
        player2.guess(interface, correctWord)

    if player2.returnGuessState():
        interface.instructions.setText(f"You win round 2! \n Thanks for playing.\n Click anywhere to exit")
    else: 
        interface.instructions.setText(f"You lose round 2! \n The word was {correctWord}. \n Thanks for playing.\n Click anywhere to exit")

    interface.win.getMouse()
    interface.win.close()


    #print("the random word is:", currentword) ### TEST###

    # --- EDIT: ---
    # The 'takeTurn' function is not used by this main()
    # so I'm commenting out the calls.
    # players take turns 
    # Player 1's Turn
    # takeTurn("Player 1", "Player 2", interface)
    # # Player 2's Turn
    # takeTurn("Player 2", "Player 1", interface)


    # # Game end ( this is place holder, function not coded yet)
    # print("\nGame Over! Thanks for playing.")
    # print("Click on the window to close.")





if __name__ == "__main__":
    main()