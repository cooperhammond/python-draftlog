from draftlog.draft import *
from random import randrange

draft, exit = inject_draftlog()


def progress_bar(progress):
    units = progress / 2
    return "[{0}{1}] {2}%".format("#" * units, "-" * (50 - units), progress)

class Download:
    def __init__(self):
        self.progress = 0
        self.status = True
    def interval(self):
        if self.progress >= 100:
            exit()
        self.progress += randrange(1, 5)
        if self.progress >= 100: self.progress = 100
        return progress_bar(self.progress)

for i, n in enumerate(range(1, 5)):
    log = draft.log()
    log.set_update(Download().interval, float(i + 1) / 10.0)
