# -*- coding: UTF-8 -*-
from draftlog.draft import Draft

class Loader:
    def __init__(self, text, status=True):
        self.frames = "⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏ ⠿".split(" ")
        self.frame = -1
        self.status = status
        self.text = text
    def interval(self):
        if self.frame > len(self.frames) - 2:
            self.frame = -1
        self.frame += 1
        return ("{0} " + self.text + " {0}").format(self.frames[self.frame]), self.status

class Stepper:
    def __init__(self, steps):
        self.steps = steps
        self.step = 0
        self.check = True
    def interval(self):
        self.step += 1
        if self.step >= len(self.steps) - 1:
            self.check = False
        string = ""
        for step in self.steps[:self.step]:
            string += " > " + step + "\n"
        return string, self.check

steps = ['Doing that', 'Then that', 'And after that', 'We will finish', 'In', '3', '2', '1']

d = Draft()
d.add_loader(Loader("Generic Stuff Loading"), 0.05)
d.add_interval(Stepper(steps), 1)
d.start()