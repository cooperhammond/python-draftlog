from draftlog.lcs import LineCountStream
from draftlog.drafter import Drafter
import sys

import colorama

"""
To inject the Drafter into sys.stdout which is
routed through with "print". It returns the Drafter
object.
"""
def inject(): # TODO: Make a thread version and a frame version.
    colorama.init()
    sys.stdout = LineCountStream()
    return Drafter()

# The exception to raise to exit your objects loop.
class Exception(Exception):
    pass
