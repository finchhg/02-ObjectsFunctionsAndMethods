"""
Practice DEFINING and CALLING
     FUNCTIONS

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Harrison Finch.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# done: 2.
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#
#     In the Project window (to the left), right click on the src  folder,
#     then select  Mark Directory As  ~  Sources Root.
#
###############################################################################

import rosegraphics as rg


def main():
    i=hypotenuse(3,4)
    print(i)
    """
    TESTS the functions that you will write below.
    You write the tests per the _TODO_s below.
    """


###############################################################################
# done: 3a.  Define a function immediately below this _TODO_.
#   It takes two arguments that denote, for a right triangle,
#   the lengths of the two sides adjacent to its right angle,
#   and it returns the length of the hypotenuse of that triangle.
#     HINT: Apply the Pythagorean theorem.
#
#   You may name the function and its parameters whatever you wish.
#
# TODO: 3b.  In main, CALL your function and print the returned value,
#   to test whether you defined the function correctly.
#
###############################################################################

import math as m

def hypotenuse(a,b):
    hypotenuse = m.sqrt(a ** 2 + b ** 2)
    return hypotenuse


###############################################################################
# TODO: 4a.  Define a function immediately below this _TODO_.
#   It takes two arguments:
#     -- a string that represents a color (e.g. 'red')
#     -- a positive integer that represents the thickness of a Pen.
#
#   The function should do the following (in the order listed):
#     a. Constructs a TurtleWindow.
#     b. Constructs two SimpleTurtles, where:
#          - one has a Pen whose color is "green" and has the GIVEN thickness
#        - - the other has a Pen whose color is the GIVEN color
#              and whose thickness is 5
#
#        Note: the "GIVEN" color means the PARAMETER that represents a color.
#        Likewise, the "GIVEN" thickness means the PARAMETER for thickness.
#
#     c. Makes the first (green) SimpleTurtle move FORWARD 100 pixels, and
#        makes the other (thickness 5) SimpleTurtle move BACKWARD 100 pixels.
#
#     d. Tells the TurtleWindow to wait until the mouse is clicked.
#
#   You may name the function and its parameters whatever you wish.
#
# TODO: 4b.  In main, CALL your function at least TWICE (with different values
#   for the arguments) to test whether you defined the function correctly.
#
###############################################################################


###############################################################################
# TODO: 5.
#   COMMIT-and-PUSH your work (after changing this TO-DO to DONE).
#
#   As a reminder, here is how you should do so:
#     1. Select   VCS   from the menu bar (above).
#     2. Choose  Commit  from the pull-down menu that appears.
#     3. In the  Commit Changes  window that pops up,
#        press the   Commit and Push   button.
#           Note: If you see only a Commit button:
#              - HOVER over the  Commit  button
#                  (in the lower-right corner of the window)
#              - CLICK on  Commit and Push.
#
#   COMMIT adds the changed work to the version control on your computer.
#   PUSH adds the changed work into your Github repository in the "cloud".
#
#   COMMIT-and-PUSH your work as often as you want, but at the least, commit
#   and push after you have tested a module and believe that it is correct.
#
###############################################################################

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
