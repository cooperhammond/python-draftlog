# -*- coding: UTF-8 -*-
from draftlog.draft import Draft
from random import randrange

def progress_bar(progress):
    units = progress / 2
    return "[{0}{1}] {2}%".format("=" * units, " " * (50 - units), progress)

class Download:
    def __init__(self):
        self.progress = 0
    def interval(self):
        self.progress += randrange(1, 5)
        if self.progress >= 100:
            return progress_bar(100), False
        return progress_bar(self.progress), True

d = Draft()
d.add_text("Starting Downloads...")
d.add_text(" ")
for n in range(1, 10):
    d.add_interval(Download(), 0.1)
d.start()