"""
LCS: Line Count Stream
"""
from .logdraft import LogDraft
from .drafter import Drafter
import os
import sys

"""
An object inserted into "sys.stdout" in order to
keep track of how many lines have been logged.
"""
class LineCountStream(object):
    def __init__(self):
        self.data = ""
        self.stdout = sys.stdout
        self.lines = 1
        self.logs = 0
        self.editing = False

        # Reads the command "tput lines" if valid
        try:
            self.rows = os.popen("tput lines").read()
        except ValueError:
            self.rows = 20

    """
    The function that overwrites "sys.stdout.write", and
    counts the number of lines in what is being "printed".
    """
    def write(self, data):
        if not self.editing:
            self.count_lines(data)
        self.stdout.write(data)

    def flush(self):
        self.stdout.flush()

    # Counts lines
    def count_lines(self, data):
        datalines = len(str(data).split("\n")) - 1
        self.lines += datalines
        self.data += data