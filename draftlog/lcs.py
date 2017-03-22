from .logdraft import LogDraft
from .drafter import Drafter
import os
import sys

class LineCountStream(object):
    def __init__(self):
        self.data = ""
        self.stdout = sys.stdout
        self.lines = 1
        self.logs = 0
        self.editing = False
        try:
            self.rows = os.popen("tput lines").read()
        except ValueError:
            self.rows = 20

    def write(self, data):
        if not self.editing:
            self.count_lines(data)
        self.stdout.write(data)

    def flush(self):
        self.stdout.flush()

    def count_lines(self, data):
        datalines = len(str(data).split("\n")) - 1
        self.lines += datalines
        self.data += data