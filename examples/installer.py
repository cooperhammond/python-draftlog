# -*- coding: UTF-8 -*-
import draftlog
from random import randrange

draft = draftlog.inject()

def install_progress(package, step, finished=False):
    spaces = " " * (15 - len(package))
    if finished:
        return " > " + package + spaces + "Installed"
    else:
        return " > " + package + spaces + step

class Loader:
    def __init__(self, text, status=True):
        self.frames = "⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏".split(" ")
        self.frame = -1
        self.status = status
        self.text = text
    def interval(self):
        if self.frame > len(self.frames) - 2:
            self.frame = -1
        self.frame += 1
        return ("{0} " + self.text + " {0}").format(self.frames[self.frame])

class MockInstall:
    def __init__(self, package, wait=0):
        self.package = package
        self.steps = "gathering dependencies  downloading dependencies  compiling code  cleaning up".split("  ")
        self.step = 0
        self.count = 0
        self.wait = wait
        self.status = True
    def interval(self):
        self.count += 1
        if self.status == False:
            raise draftlog.IntervalQuit
        if self.count >= self.wait:
            if self.step > len(self.steps) - 2:
                self.status = False
                return install_progress(self.package, self.steps[self.step], finished=True)
            self.step += 1
            return install_progress(self.package, self.steps[self.step])
        else:
            return ""


packages = ["irs", "bobloblaw", "youtube-dl", "truffleHog", "numpy", "scipy"]
load = Loader("Installing Packages")

load_draft = draft.log()

load_draft.set_interval(load.interval, 0.03, daemon=True)

for i, package in enumerate(packages):
    draft.log().set_interval(
        MockInstall(package, wait=i).interval,
        round(float(randrange(25, 150) / 100.0), 1)
    )