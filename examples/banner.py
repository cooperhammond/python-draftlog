from draftlog.draft import Draft

class Banner:
    def __init__(self, text):
        self.text = text
        self.shift = 0
    def interval(self):
        self.shift += 1
        if self.shift >= 50:
            return self.text, False
        self.text = self.text[1:] + self.text[0]
        return self.text, True

string = "  Wow! Banners!     This is so cool!     All in 15 lines with `draftlog`!   "

d = Draft()

d.add_text("*" * len(string))
d.add_interval(Banner(string), 0.2)
d.add_text("*" * len(string))

d.start()