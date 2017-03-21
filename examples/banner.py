import draftlog

draft = draftlog.inject()

class Banner:
    def __init__(self, string, update):
        self.string = string
        self.update = update
        self.counter = 0
    def scroll(self):
        if self.counter >= 50:
            raise draftlog.IntervalQuit
        self.counter += 1
        self.string = self.string[1:] + self.string[0]
        self.update(self.string)

string = "  Wow! Banners!     This is so cool!     All with draftlog!   "

print ("*" * len(string))
banner = draft.log()
print ("*" * len(string))

draftlog.set_interval(Banner(string, banner).scroll, 0.1)