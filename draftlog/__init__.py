from .lcs import LineCountStream
import sys

def inject():
    print ("")
    sys.stdout = LineCountStream()
    return sys.stdout

class IntervalQuit(Exception):
    pass