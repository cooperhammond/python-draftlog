import draftlog

draft = draftlog.inject()

class Banner:
    def __init__(self, string):
        self.string = string
        self.counter = 0
    def scroll(self):
        if self.counter >= 60:
            raise draftlog.Exception
        self.counter += 1
        self.string = self.string[1:] + self.string[0]
        return draftlog.ansi.YELLOW + self.string + draftlog.ansi.END

string = "  Wow! Banners!     This is so cool!     All with draftlog!   "

print ("\n")
print ("*" * len(string))
banner = draft.log()
print ("*" * len(string))
print ("\n")

banner.set_interval(Banner(string).scroll, 0.1)

draft.start()