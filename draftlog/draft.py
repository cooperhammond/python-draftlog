# -*- coding: UTF-8 -*-
import time, sys
from ansi import *

if sys.version_info[0] >= 3:
    import io
elif sys.version_info[0] == 2:
    import StringIO as io

class Loader:
    def __init__(self, text, status=True):
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
        self.counter = -1
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
        self.intervals.append({
            "class": class_,
            "time": n,
            "status": True
        })

    def add_loader(self, class_, n):
        """
        Pretty much the same as `add_interval`, but finishes when the rest do
        rather than on its own time.
        """
        self.intervals.append({
            "class": class_,
            "time": n,
            "status": None
        })

    def sort_intervals(self):
        """
        Note that this doesn't actually sort anything, it just adds a 4 element
        so that there is an average for how much something is called so that
        times aren't useless.
        """
        smallest = lambda x: x["time"]
        sort = sorted(self.intervals, key=smallest)
        smallest_interval = min(sort, key=smallest)
        self.time_interval = smallest_interval["time"]
        for interval in self.intervals:
            interval["increment_counter"] = round(interval["time"] / self.time_interval)
            interval["backup"] = ""

    def parse_interval(self, interval):
        if interval["status"] == False:
            return interval["backup"], False
        elif interval["status"] == None:
            return interval["class"].interval()
        elif self.counter % interval["increment_counter"] == 0:
            return interval["class"].interval()
        else:
            return interval["backup"], True

    def generate_frame(self):
        """ Generates a single frame of the log. """
        self.capture() # Begin capturing each interval.
        for interval in self.intervals:
            t, check = self.parse_interval(interval)
            if check == False and interval["status"] != False:
                interval["status"] = False

            if t:
                self.counter += 1
                interval["backup"] = t
                sys.stdout.write(clearline)
                print (t)

        return self.get_capture() # Return the captured intervals.

    def check_done(self):
        """ Checks if all of `self.intervals[x]["status"]` is a `bad bool`"""
        return all(x["status"] in (False, None) for x in self.intervals)

    def start(self):
        """ Runs the program until `check_done()` returns `True`"""
        self.sort_intervals()
        lines = 0
        while self.check_done() == False:
            frame = self.generate_frame()
            lines = len(frame.split("\n"))
            print (frame)
            up(lines)
            time.sleep(self.time_interval)
        down(lines - 1)