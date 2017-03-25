from .lcs import LineCountStream
from .drafter import Drafter
import sys

"""
To inject the Drafter into sys.stdout which is
routed through with "print". It returns the Drafter
object.
"""
def inject(): # TODO: Make a thread version and a frame version.
    sys.stdout = LineCountStream()
    return Drafter()

# The exception to raise to exit your objects loop.
class Exception(Exception):
    pass