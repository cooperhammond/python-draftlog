from draftlog.draft import *
import time
draft, exit = inject_draftlog()

class Banner:
    def __init__(self, string):
        self.string = string
        self.counter = 0
    def interval(self):
        if self.counter >= 100:
            exit()
        self.counter += 1
        self.string = self.string[1:] + self.string[0]
        return self.string

string = "  Wow! Banners!     This is so cool!     All with draftlog!   "

print ("*" * len(string))
banner = draft.log()
print ("*" * len(string))

banner.set_update(Banner(string).interval, 0.1)