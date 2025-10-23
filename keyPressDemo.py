from graphics import *

# Reference: https://mcsp.wartburg.edu/zelle/python/graphics/graphics/node3.html

###########################################################
## main                                                  ##
###########################################################

def main():
    # Make the window
    win = GraphWin()

    # Draw a circle for no particular reason
    circle = Circle(Point(100, 100), 20)
    circle.setFill("dark blue")
    circle.draw(win)

    # Have the user press 10 keys, and print out their strings
    # (arrow keys are "Left", "Right", "Down", etc.)
    for i in range(10):
        keyString = win.getKey()
        print(f"Key pressed: {keyString}")

    win.getMouse()

if __name__ == "__main__":
    main()