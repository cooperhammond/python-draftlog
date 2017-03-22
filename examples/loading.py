# -*- coding: UTF-8 -*-
import draftlog

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
        return ("{0} " + self.text + " {0}").format(self.frames[self.frame])

class Stepper:
    def __init__(self, steps):
        self.steps = steps
        self.step = -1
        self.status = True
    def interval(self):
        self.step += 1
        if self.step >= len(self.steps) - 1:
            raise draftlog.Exception
        return (" > " + self.steps[self.step])


steps = ['Doing that', 'Then that', 'And after that', 'We will finish', 'In', '3', '2', '1', '0']
stepper = Stepper(steps)
loader = Loader("Generic Loading")

draft.log().set_interval(loader.interval, 0.03, loader=True)
step = draft.log().set_interval(stepper.interval, 1, update=False)

draft.start()