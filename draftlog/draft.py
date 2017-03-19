# -*- coding: UTF-8 -*-
import time, sys
from ansi import *
import random

if sys.version_info[0] >= 3:
    import io
elif sys.version_info[0] == 2:
    import StringIO as io

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


ids = []
def gen_id():
    global ids
    id = random.random()
    if id not in ids:
        ids.append(id)
        return id
    else:
        return gen_id()

class TmpInterval:
    def __init__(self, text, status=True):
        self.text = text
        self.tmp_text = text
        self.status = status
        self.init_time = time.time()
        self.time_reach = 0
    def interval(self):
        if time.time() > self.time_reach + (self.time_reach - self.init_time):
            self.text = self.tmp_text
        return self.text
    def update_after(self, text, time_):
        self.tmp_text = text
        self.time_reach = time.time() + time_

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
        id = gen_id()
        self.intervals.append({
            "class": class_,
            "time": n,
            "status": True,
            "id": id,
        })
        return

    def add_loader(self, class_, n):
        """
        Pretty much the same as `add_interval`, but finishes when the rest do
        rather than on its own time.
        """
        id = gen_id()
        self.intervals.append({
            "class": class_,
            "time": n,
            "status": None,
            "id": id
        })
        return id

    def add_text(self, text, n=0.01):
        """ A really hacky `loader` pretty much. (look up)"""
        id = gen_id()
        self.intervals.append({
            "class": TmpInterval(text, status=None),
            "time": n,
            "status": None,
            "id": id
        })
        return id

    def id_interval(self, id):
        for interval in self.intervals:
            if interval["id"] == id:
                return interval["class"]

    def sort_intervals(self):
        """
        Note that this doesn't actually sort anything, it just adds a 4 element
        so that there is an average for how much something is called so that
        times aren't useless.
        """
        smallest = lambda x: x["time"]
        sort = sorted(self.intervals, key=smallest)
        self.smallest_interval = min(sort, key=smallest)
        self.time_interval = self.smallest_interval["time"]
        for interval in self.intervals:
            interval["increment_counter"] = int(round(interval["time"] / self.time_interval))
            interval["backup"] = ""
            if "id" not in interval:
                interval["id"] = gen_id()

    def parse_interval(self, interval):
        if interval["status"] == False:
            return interval["backup"], False
        elif interval["status"] == None:
            return interval["class"].interval(), interval["class"].status
        elif self.counter % interval["increment_counter"] == 0:
            return interval["class"].interval(), interval["class"].status
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
            self.counter += 1
            frame = self.generate_frame()
            lines = len(frame.split("\n"))
            print (frame)
            up(lines)
            time.sleep(self.time_interval)
        down(lines - 1)