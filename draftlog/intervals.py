import time
import sys
import threading
import draftlog

class Timer(threading.Thread):
    def __init__(self, line, func, sec, daemon=False):
        super(Timer, self).__init__()
        self.setDaemon(daemon)

        self.update = line
        self.func = func
        self.sec = sec
    def run(self):
        while True:
            try:
                self.update(self.func())
                time.sleep(self.sec)
            except draftlog.IntervalQuit:
                sys.exit()