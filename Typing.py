import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
     stdscr.clear()

     text = "---- WELCOME TO SEBIVALLO TYPING SPEED GAME ----"
     height, width = stdscr.getmaxyx()
     x = (width - len(text))//2
     y = height//2
     color = curses.color_pair(1)

     stdscr.addstr(y,x,text, color )
     stdscr.addstr("\n\n\n Press any key to begin!", color)
     stdscr.refresh()
     stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    height, width = stdscr.getmaxyx()
    text = f"WPM: {wpm}"
    x = (width - len(text))//2
    y = height//2

    height, width = stdscr.getmaxyx()
    x = (width - len(target))//2
    y = height//2

    stdscr.addstr(y-1,x-1,target)
    stdscr.addstr(y+2, 1, text)

    for i, char in enumerate(current):

        height, width = stdscr.getmaxyx()
        x = (width - len(target))//2
        y = height//2

        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(y-1, i+x-1, char, color)


def load_text():
    with open("text.txt", "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
     target_text = load_text()
     current_text = []
     wpm = 0
     start_time = time.time()
     stdscr.nodelay(True)

     while True:
        time_elapsed = max (time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed/60)) / 5)
        
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)  
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        try:   
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key) 

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        height, width = stdscr.getmaxyx()
        text = "would you like to continue..."
        x = (width - len(text))//2
        y = height//2
    
        wpm_test(stdscr)

        stdscr.addstr(y+4, 1,"🎈🎈🎈 CONGRATULATIONS! 🎈🎈🎈" )
        stdscr.addstr(y+5, 1,"You completed the test" )
        stdscr.addstr(y+7, 1,text )
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)