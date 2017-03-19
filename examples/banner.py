from draftlog.draft import Draft

class Banner:
    def __init__(self, text):
        self.text = text
        self.shift = 0
        self.status = True
    def interval(self):
        self.shift += 1
        if self.shift >= 25:
            self.status = False
        self.text = self.text[1:] + self.text[0]
        return self.text

string = "  Wow! Banners!     This is so cool!     All in 15 lines with `draftlog`!   "

d = Draft()

d.add_text("*" * len(string))
d.add_interval(Banner(string), 0.2)
d.add_text("*" * len(string))

d.start()