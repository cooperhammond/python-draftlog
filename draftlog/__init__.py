from .lcs import LineCountStream
from .drafter import Drafter
import sys

def inject():
    print ("")
    sys.stdout = LineCountStream()
    return Drafter()

class Exception(Exception):
    pass