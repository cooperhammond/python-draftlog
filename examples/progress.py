import draftlog
from random import randrange

draft = draftlog.inject()

def progress_bar(progress):
    if progress >= 100:
        progress = 100
    units = progress / 2
    return "[{0}{1}] {2}%".format("#" * units, "-" * (50 - units), progress)

class Download:
    def __init__(self):
        self.progress = 0
        self.status = True
    def interval(self):
        if self.progress >= 102:
            raise draftlog.Exception
        self.progress += randrange(1, 5)
        if self.progress > 102: self.progress = 100
        return progress_bar(self.progress)


for n in range(1, 10):
    log = draft.log()
    log.set_interval(Download().interval, 0.1)

draft.start()
