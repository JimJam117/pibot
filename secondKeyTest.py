import curses
import os

from basic import *

def main(win):
    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("JimjamBot Control - w,s,a,d (q,e for pivot) - return to exit - ")
    win.addstr("Detected Key:")
    while 1:
        try:
            key = win.getkey()
            win.clear()
            win.addstr("JimjamBot Control - w,s,a,d (q,e for pivot) - return to exit - ")
            win.addstr("Detected Key:")
            win.addstr(str(key))
            if key == os.linesep:
                break

            elif str(key) == 'w':
                #print(str(key))
                win.addstr('[FWD]')
                forwardPwm(1, 100, 95)

            elif str(key) == 's':
                #print(str(key))
                win.addstr('[BWD]')
                backwardPwm(1, 95, 100)

            elif str(key) == 'a':
                #print(str(key))
                win.addstr('[TLE]')
                turn_left(1)

            elif str(key) == 'd':
                #print(str(key))
                win.addstr('[TRI]')
                turn_right(1)

            elif str(key) == 'q':
                #print(str(key))
                win.addstr('[PLE]')
                pivot_left(0.2)

            elif str(key) == 'e':
                #print(str(key))
                win.addstr('[PRI]')
                pivot_right(0.2)


            else:
                win.addstr('[UKN CMD]')
                pass
        except Exception as e:
            # No Input
            pass

curses.wrapper(main)
