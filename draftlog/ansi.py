import sys

esc =        '\x1b['
save =       esc + '7'
restore =    esc + '8'
reset =      esc + "0m"
clearline =  esc + '2K' + esc + '1G'
bold =       esc + "01m"
clear =      esc + "2J"
save =       esc + "s"
restore =    esc + "u"
dim =        esc + "2m"
underline =  esc + "4m"
reverse =    esc + "7m"
blink =      esc + "5m"
invisible =  esc + "8m"

def gotoxy(x, y):
    sys.stdout.write(esc + "%d;%dH" % (x, y))

def up(n=1):
    sys.stdout.write(esc + str(n) + 'A')

def down(n=1):
    sys.stdout.write(esc + str(n) + 'B')

def right(n=1):
    sys.stdout.write(esc + str(n) + 'C')

def left(n=1):
    sys.stdout.write(esc + str(n) + 'D')