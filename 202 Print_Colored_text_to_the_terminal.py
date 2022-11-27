#using ANSI escape sequence
# RGB=Red,Blue,Green
# SGR= Select Graphics Rendition
print('\x1b[38;2;6;96;243m'+ 'Today is the only day yesterday is gone.','\x1b[0m')

# termcolor
from termcolor import colored

print(colored('Whoever is happy make others happy.','red'))