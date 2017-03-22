import ansi
import sys

class LogDraft:
    def __init__(self, drafter):
        self.stream = sys.stdout
        self.drafter = drafter
        self.valid = True
        self.save_line()

    def __call__(self, text):
        self.update(text)

    def update(self, text):
        lines_up = self.lines_up()

        if self.off_screen(): # Check if offscreen, if so, don't update the line.
            self.valid = False
            return

        # Move cursor up
        self.stream.write(ansi.up(lines_up))

        # Clear the line
        self.stream.write(ansi.clearline)

        # Write the line
        self.write(text)

        # Flush the data
        self.stream.flush()

        # Restore cursor position
        self.stream.write(ansi.down(lines_up))


    def set_interval(self, func, sec, **args):
        self.drafter.add_interval(self, func, sec, **args)

    def write(self, text):
        if self.valid:
            self.stream.write(text)

    def off_screen(self):
        return self.stream.rows <= self.lines_up()

    def lines_up(self):
        return self.stream.lines - self.line

    def save_line(self, relative=0):
        self.line = self.stream.lines + relative