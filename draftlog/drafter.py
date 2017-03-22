from .logdraft import LogDraft
import draftlog
import time
import sys
import ansi

class Drafter:
    def __init__(self):
        self.lcs = sys.stdout
        self.intervals = []
        self.counter = -1
        self.time_interval = 0

    def log(self):
        logdraft = LogDraft(self)
        self.lcs.write(ansi.save)
        print ("")
        return logdraft

    def add_interval(self, logdraft, func, seconds, loader=False, update=True):
        if loader != None:
            loader = not loader

        self.intervals.append({
            "function":  func,
            "logdraft":  logdraft,
            "time"    :  seconds,
            "backup"  :  "",
            "backup1" :  "",
            "update"  :  update,
            "status"  :  loader,
        })

    def sort_intervals(self):
        smallest = lambda x: x["time"]
        sort = sorted(self.intervals, key=smallest)
        self.smallest_interval = min(sort, key=smallest)
        self.time_interval = self.smallest_interval["time"]
        for interval in self.intervals:
            interval["increment_on"] = int(round(interval["time"] / self.time_interval))
            interval["backup"] = "" # This is an important thing to change/remember

    def parse_interval_output(self, interval):
        try:
            if self.counter % interval["increment_on"] == 0:
                output = interval["function"]()
                interval["backup"] = interval["backup1"]
                interval["backup1"] = output
            else:
                output = interval["backup"]
        except draftlog.Exception:
            output = interval["backup"]
            interval["status"] = False

        return str(output)

    def run_intervals(self):
        #frame = []
        for interval in self.intervals:
            text = self.parse_interval_output(interval)
            if interval["update"] == True:
                interval["logdraft"].update(text)
            else:
                if text != interval["backup"] and text != "":
                    if interval.get("overwritten_init_line") != True:
                        interval["logdraft"].update(text)
                        interval["overwritten_init_line"] = True
                    else:
                        self.lcs.write(ansi.clearline)
                        print (text)
        #return "\n".join(frame)

    def check_done(self):
        return all(x["status"] in (False, None) for x in self.intervals)

    def start(self):
        self.sort_intervals()
        lines = 0
        while self.check_done() == False:
            self.counter += 1
            self.run_intervals()
            time.sleep(self.time_interval)
        self.lcs.write(ansi.clearline)