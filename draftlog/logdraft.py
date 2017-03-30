import ansi
import sys

"""
A single line object that saves its relative position
in the terminal. It's responsible for updating itself.
"""
class LogDraft:
    def __init__(self, drafter):
        self.stream = sys.stdout
        self.drafter = drafter
        self.valid = True
        self.save_line()

    # For if someone wants to call "LogDraft()('update text')"
    def __call__(self, text):
        self.update(text)

    # Updates the line that "LogDraft" was created on
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

        # Move cursor to the beginning of the line
        self.stream.write("\r")

        # Save the current text
        self.text = text


    # What the user gets when they call "draft.log().set_interval(**args**)"
    def set_interval(self, func, sec, **args):
        self.drafter.add_interval(self, func, sec, **args)

    # Writes to the LCS
    def write(self, text):
        if self.valid:
            self.stream.write(text)

    # Checks if the line being monitored is off screen.
    def off_screen(self):
        return self.lines_up() >= self.stream.rows

    # Counts how many lines up until the correct line.
    def lines_up(self):
        return self.stream.lines - self.line

    # Sets the line to be monitored.
    def save_line(self, relative=0):
        self.line = self.stream.lines + relative