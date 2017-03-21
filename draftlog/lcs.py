from .draft import LogDraft
import os
import sys

class LineCountStream(object):
    def __init__(self):
        self.stdout = sys.stdout
        self.line = 1
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

    def log(self):
        r = LogDraft()
        print ("")
        return r

    def flush(self):
        self.stdout.flush()

    def count_lines(self, data):
        datalines = len(str(data).split("\n")) - 1
        self.line += datalines