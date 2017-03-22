import draftlog

draft = draftlog.inject()

class Banner:
    def __init__(self, string):
        self.string = string
        self.counter = 0
    def scroll(self):
        if self.counter >= 50:
            raise draftlog.Exception
        self.counter += 1
        self.string = self.string[1:] + self.string[0]
        return self.string

string = "  Wow! Banners!     This is so cool!     All with draftlog!   "

print ("*" * len(string))
banner = draft.log()
print ("*" * len(string))

banner.set_interval(Banner(string).scroll, 0.1)

draft.start()