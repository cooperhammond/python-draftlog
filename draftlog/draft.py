import sys, time
import threading

esc =        '\x1b['
clearline =  esc + '2K' + esc + '1G'

def up(n=1):
    sys.stdout.write(esc + str(n) + 'A')

def down(n=1):
    sys.stdout.write(esc + str(n) + 'B')

class Interval(threading.Thread):
    def __init__(self, line_marker, function, time, daemon, suffix=""):
        super(Interval, self).__init__()
        self.setDaemon(daemon)

        self.line_marker = line_marker
        self.function = function
        self.time = time
        self.suffix = suffix
    def run(self):
        while True:
            self.line_marker.update(self.function())
            time.sleep(self.time)

class Looper(threading.Thread):
    def __init__(self, function, time, daemon):
        super(Looper, self).__init__()
        self.setDaemon(daemon)

        self.function = function
        self.time = time
    def run(self):
        while True:
            sys.stdout.write(self.function())
            sys.stdout.flush()
            time.sleep(self.time)

class LineMarker:
    def __init__(self, lines):
        self._lines = lines - 1
    def lines(self):
        return sys.stdout.lines - self._lines
    def update(self, text):
        up(self.lines())
        sys.stdout.write(clearline + text)
        down(self.lines())
        sys.stdout.write(clearline)
        sys.stdout.flush()
    def set_update(self, function, time, daemon=False):
        # Note that if daemon is set to True, the program will end when the
        # mainloop ends, and will not otherwise until sys.exit is called
        sys.stdout.threads += 1
        Interval(self, function, time, daemon=daemon).start()
    def loop(self, function, time, daemon=False):
        sys.stdout.threads += 1
        Looper(function, time, daemon=daemon).start()


class LineCountStream(object):
    def __init__(self, lines=0):
        self.stdout = sys.stdout
        self.lines  = lines
        self.logs   = 1
        self.threads = 0
        print ("")

    def write(self, s):
        self.lines += s.count("\n")
        self.stdout.write("%s" % s)
    def flush(self):
        self.stdout.flush()

    def log(self):
        self.logs += 1
        print ("")
        return LineMarker(self.lines)

def inject_draftlog():
    sys.stdout = LineCountStream()
    return sys.stdout, sys.exit