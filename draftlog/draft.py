# -*- coding: UTF-8 -*-
import time, sys
from ansi import *

if sys.version_info[0] >= 3:
    import io
elif sys.version_info[0] == 2:
    import StringIO as io

class Loader:
    def __init__(self, text):
        self.frames = "⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏ ⠿".split(" ")
        self.frame = -1
        self.text = text
    def interval(self):
        if self.frame > len(self.frames) - 3:
            self.frame = -2
            check = False
        else:
            check = True
        self.frame += 1
        return ("{0} " + self.text + " {0}").format(self.frames[self.frame]), check


class TmpInterval:
    def __init__(self, text):
        self.text = text
    def interval(self):
        return self.text, True

class Draft:
    def __init__(self):
        self.intervals = []
        self.time_interval = 0

    def capture(self):
        """
        Once run all print statements will be captured until `get_capture` is
        run.
        """
        self.tmp = sys.stdout
        sys.stdout = self.buffer = io.StringIO()

    def get_capture(self):
        """
        Resets all effects of `capture`, and return everything captured by it.
        """
        sys.stdout = self.tmp
        return self.buffer.getvalue()

    def add_interval(self, class_, n):
        """
        `class_`: a class with an `interval` function that returns a tuple with
        the format `(string, bool)`. If bool is `False`, then it will stop
        calling it, and use string everytime. `class_` Must be already
        initialized.
        `n`     : how often it should be updated.
        """
        self.intervals.append([class_, n]) # TODO: Implement the time to do something.

    def generate_frame(self):
        """ Generates a single frame of the log. """
        self.capture() # Begin capturing each interval.
        for index, interval_ in enumerate(self.intervals):
            t, check = interval_[0].interval()
            if check == False:
                self.intervals[index] = [TmpInterval(t), interval_[1]]

            # To check that it isn't `None or False`, because it would still print it
            if t:
                sys.stdout.write(clearline)
                print (t)

        return self.get_capture() # Return the captured intervals.

    def check_done(self):
        """ Checks if all of `self.intervals[x][0]` is a `TmpInterval`"""
        return all(isinstance(x[0], TmpInterval) for x in self.intervals)

    def start(self):
        """ Runs the program until `check_done()` returns `True`"""
        while self.check_done() == False:
            frame = self.generate_frame()
            lines = len(frame.split("\n"))
            print (frame)
            up(lines)
            time.sleep(0.03)
        down(lines - 1)

class Load:
    def __init__(self, text):
        self.text = text
        self.num = 0
    def interval(self):
        check = True
        if self.num >= 12:
            check = False
        self.num += 1

        return self.text, check

d = Draft()

d.add_interval(Loader("Loading"), 0.05)
d.add_interval(Load("Wow another!"), 0.5)


d.start()