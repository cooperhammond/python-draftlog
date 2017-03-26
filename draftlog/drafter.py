from .logdraft import LogDraft
import draftlog
import time
import sys
import ansi
import threading

# Imports the correct module according to
# Python version.
if sys.version_info[0] <= 2:
    import Queue as queue
else:
    import queue

"""
A background process to coordinate all the intervals
with their correct times rather than having clashing
multiple threads.
"""
class DaemonDrafter(threading.Thread):
    def __init__(self):
        super(DaemonDrafter, self).__init__()

        self.lcs = sys.stdout
        self.intervals = []
        self.counter = -1
        self.time_interval = 0
        self.end = False

    """
    What actually adds the interval.
    "Loader" specifies if the interval should
    affect when the draft actually exits.
    line, or to add a new line afterwards.
    """
    def add_interval(self, logdraft, func, seconds, loader=False):
        if loader != None:
            loader = not loader

        self.intervals.append({
            "function":  func,
            "logdraft":  logdraft,
            "time"    :  seconds,
            "backup"  :  "",
            "status"  :  loader,
        })
        self.sort_intervals()

    # Generates correct timing for intervals
    def sort_intervals(self):
        smallest = lambda x: x["time"]
        sort = sorted(self.intervals, key=smallest)
        self.smallest_interval = min(sort, key=smallest)
        self.time_interval = self.smallest_interval["time"]
        for interval in self.intervals:
            interval["increment_on"] = int(round(interval["time"] / self.time_interval))
            interval["backup"] = "" # This is an important thing to change/remember

    # Parses interval output according to its statuses
    def parse_interval_output(self, interval):
        try:
            if self.counter % interval["increment_on"] == 0:
                output = interval["function"]()
                interval["backup"] = output
            else:
                output = interval["backup"]
        except draftlog.Exception:
            output = interval["backup"]
            interval["status"] = False

        return str(output)

    # What actually updates the LogDraft lines.
    def run_intervals(self):
        for interval in self.intervals:
            text = self.parse_interval_output(interval)
            interval["logdraft"].update(text)

    # Checks if all intervals are done.
    def check_done(self):
        return all(x["status"] in (False, None) for x in self.intervals)

    # The actual running loop for updating intervals.
    def run(self):
        lines = 0
        while self.check_done() == False and self.end == False:
            self.counter += 1
            self.run_intervals()
            time.sleep(self.time_interval)
        self.lcs.write(ansi.clearline)
        sys.exit()

    def stop(self):
        self.end = True

"""
Pretty much just a wrapper for "DaemonDrafter".
It's what the user actually interacts with and what
"draftlog.inject()" returns.
"""
class Drafter:
    def __init__(self):
        self.daemon_drafter = DaemonDrafter()
        self.lcs = self.daemon_drafter.lcs

    # Returns a "LogDraft" object on the correct line
    def log(self, text="\n"):
        if text != "\n": text = text + "\n"
        logdraft = LogDraft(self.daemon_drafter)
        self.lcs.write(text)
        return logdraft

    def start(self):
        self.daemon_drafter.start()

    def stop(self):
        self.daemon_drafter.stop()