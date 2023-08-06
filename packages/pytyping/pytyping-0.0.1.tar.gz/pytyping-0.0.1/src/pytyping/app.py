import curses
import time
import requests
from random import randint


QUOTES = requests.get('https://type.fit/api/quotes').json()
VALIDS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

minutes = None
wpm = None
accuracy = None


def menu(stdsrc):
    '''
    Main menu
    '''

    options = ['Start Typing', 'Exit']
    selected = 0

    while True:
        # Clear the screen
        stdsrc.clear()

        # Get width and height of the screen
        (height, width) = stdsrc.getmaxyx()

        # Center the options
        for (i, option) in enumerate(options):
            x = width // 2 - len(option) // 2
            y = height // 2 - len(options) // 2 + i

            # Highlight the selected option
            if i == selected:
                stdsrc.addstr(y, x, option, curses.color_pair(3))
            else:
                stdsrc.addstr(y, x, option)

        # Get input
        key = stdsrc.getch()

        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(options) - 1:
            selected += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # Exit the loop
            if options[selected] == 'Start Typing':
                break
            elif options[selected] == 'Exit':
                # Quit the program
                quit()


def game(stdsrc):
    '''
    Let's you play the game
    '''

    global minutes, wpm, accuracy

    sentence = get_quote()
    user_input = ''

    # Variables to calculate the accuracy
    corrects = 0
    total = 0

    # Get the time when the game starts
    start = time.time()

    while True:

        # Clear screen
        stdsrc.clear()

        if len(user_input) == len(sentence):
            break

        # Get the width and height of the screen
        (height, width) = stdsrc.getmaxyx()

        # Center the text
        x = width // 2 - len(sentence) // 2
        y = height // 2

        # Check every letter of the sentence and of the user input
        for i in range(len(sentence)):

            # Check if the current character is a `\n` and ignores it
            if sentence[i] == '\n':
                y += 1
                continue

            # While the user has written something
            if i < len(user_input):
                current = user_input[i]

                # If it's correct then print it as green
                if current == sentence[i]:
                    stdsrc.addstr(y, x + i, current,
                                  curses.color_pair(1))
                else:
                    # If it's wrong then print it as red
                    stdsrc.addstr(y, x + i, current,
                                  curses.color_pair(2))
            else:
                # Else if the user didn't typed until now
                # If it's the letter the user is about to type then highlight it
                if i == len(user_input):
                    stdsrc.addstr(y, x + i, sentence[i],
                                  curses.color_pair(3))
                else:
                    # Else print it normally
                    stdsrc.addstr(y, x + i, sentence[i])

        # Get input as string
        key = stdsrc.getkey()

        # If the user pressed the backspace then delete the last letter
        if key == 'KEY_BACKSPACE':
            user_input = user_input[:-1]
        elif key in VALIDS and len(user_input) < len(sentence):
            # Else if it's a valid key, add it to the user input
            user_input += key

            # Increase the number of correct entries if the character is correct
            if user_input[-1] == sentence[len(user_input) - 1]:
                corrects += 1

            # Increase the number of total entries
            total += 1

        # Refresh the screen to see the changes
        stdsrc.refresh()

    # Get the time when the game ends
    stop = time.time()

    # Calculate the minutes by subtracting the final and the initial time, dividing by 60 and rounding to the seconds
    minutes = round((stop - start) / 60, 2)

    # Calculate the WPM, see: https://www.speedtypingonline.com/typing-equations
    wpm = round(len(sentence) / 5 / minutes)

    # Calculate the accuracy
    accuracy = round(corrects / total * 100)


def score(stdsrc):
    '''
    Display the score
    '''

    global minutes, wpm

    # Clear the screen
    stdsrc.clear()

    # Get width and height
    (height, width) = stdsrc.getmaxyx()

    # Calculate the y (should be the center of the screen)
    y = height // 2

    # Center all the elements
    minutes_string = 'Time (minutes): ' + str(minutes)
    x = width // 2 - len(minutes_string) // 2
    stdsrc.addstr(y - 4, x, minutes_string)

    wpm_string = 'WPM: ' + str(wpm)
    x = width // 2 - len(wpm_string) // 2
    stdsrc.addstr(y - 3, x, wpm_string)

    accuracy_string = 'Accuracy: ' + str(accuracy) + '%'
    x = width // 2 - len(accuracy_string) // 2
    stdsrc.addstr(y - 2, x, accuracy_string)

    message = 'Press any key to continue'

    x = width // 2 - len(message) // 2
    stdsrc.addstr(y + 1, x, message)

    # Wait for a key
    stdsrc.getch()


def main_loop(stdsrc):
    '''
    Define the main loop for the application
    '''

    # Set cursor as invisible
    curses.curs_set(0)

    # Initialize color schemes
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Main loop
    while True:
        menu(stdsrc)
        game(stdsrc)
        score(stdsrc)


def get_quote():
    '''
    Get a random quote
    '''
    return QUOTES[randint(0, 1643)]['text']


def run():
    '''
    Entry point for the application
    '''
    curses.wrapper(main_loop)
