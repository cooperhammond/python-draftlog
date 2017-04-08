# -*- coding: UTF-8 -*-
import draftlog
import time
from draftlog.ansi import * # For colors

draft = draftlog.inject()

class Loader:
    def __init__(self, text):
        self.frames = "⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏".split(" ")
        self.frame = -1
        self.text = text
    def interval(self):
        self.frame += 1
        if self.frame > len(self.frames) - 2:
            self.frame = -1
        return (CYAN + "{0} " + BYELLOW + self.text + END + CYAN + " {0}" + END).format(self.frames[self.frame])

class Stepper:
    def __init__(self, steps):
        self.steps = steps
        self.step = -1
        self.status = True
    def interval(self):
        self.step += 1
        if self.step >= len(self.steps) - 1:
            raise draftlog.Exception
        return (" > " + CYAN + self.steps[self.step] + END)


steps = ['Doing that', 'Then that', 'And after that', 'We will finish', 'In', '3', '2', '1', '0']
stepper = Stepper(steps)
loader = Loader("Generic Loading")

draft.log().set_interval(loader.interval, 0.05)
draft.start()

while True:
    try:
        time.sleep(1)
        print (stepper.interval())
    except draftlog.Exception:
        break
    except KeyboardInterrupt:
        pass

draft.stop()