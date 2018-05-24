"""
Final exam, problem 3.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Zikang Zhang.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the   problem3  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem3  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of problem3: '
    window = rg.RoseWindow(450, 300, title)

    point = rg.Point(200, 30)
    circle1 = rg.Circle(rg.Point(100, 50), 15)
    circle2 = rg.Circle(rg.Point(300, 100), 10)
    circle1.fill_color = 'red'
    circle2.fill_color = 'blue'
    problem3(point, circle1, circle2, window)
    window.continue_on_mouse_click()

    point = rg.Point(200, 250)
    circle1 = rg.Circle(rg.Point(150, 150), 20)
    circle2 = rg.Circle(rg.Point(100, 200), 5)
    circle1.fill_color = 'green'
    circle2.fill_color = 'pink'
    problem3(point, circle1, circle2, window)
    window.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of problem3: '
    window = rg.RoseWindow(180, 250, title)

    point = rg.Point(50, 150)
    circle1 = rg.Circle(rg.Point(50, 50), 15)
    circle2 = rg.Circle(rg.Point(150, 100), 20)
    circle1.fill_color = 'blue'
    circle2.fill_color = 'green'
    problem3(point, circle1, circle2, window)
    window.close_on_mouse_click()


def problem3(point, circle1, circle2, window):
    """
    See   problem3_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Point.
      -- Two rg.Circle objects (circle1 and circle2)
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:  Draws all the following on the given rg.RoseWindow:
      -- Draws the given rg.Point and rg.Circle objects.
      -- Then draws 3 rg.Lines:
            -- one from the given rg.Point to the center of circle1
            -- one from the center of circle1 to the center of circle2
            -- one from the center of circle2 to the given rg.Point
         where the color of each of those lines is the same color
         as the fill color of circle1.
      -- Then draws 3 more rg.Lines:
            -- one from the midpoint of the 1st line above
                 to the midpoint of the 2nd line above
            -- one from the midpoint of the 2nd line above
                 to the midpoint of the 3rd line above
            -- one from the midpoint of the 3rd line above
                 to the midpoint of the 1st line above
         where the color of each of those lines is the same color
         as the fill color of circle2.
      Must  render but  ** NOT close **   the window.

    Type hints:
       :type point:    rg.Point
       :type circle1:  rg.Circle
       :type circle2:  rg.Circle
      :type window:    rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------
    point.attach_to(window)
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    line1 = rg.Line(point, circle1.center)
    line2 = rg.Line(circle1.center, circle2.center)
    line3 = rg.Line(circle2.center, point)
    line1.color = circle1.fill_color
    line2.color = circle1.fill_color
    line3.color = circle1.fill_color
    line1.attach_to(window)
    line2.attach_to(window)
    line3.attach_to(window)
    window.render()
    line4 = rg.Line(line1.get_midpoint(), line2.get_midpoint())
    line5 = rg.Line(line2.get_midpoint(), line3.get_midpoint())
    line6 = rg.Line(line3.get_midpoint(), line1.get_midpoint())
    line4.color = circle2.fill_color
    line5.color = circle2.fill_color
    line6.color = circle2.fill_color
    line4.attach_to(window)
    line5.attach_to(window)
    line6.attach_to(window)
    window.render()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------

# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
