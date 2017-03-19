# -*- coding: UTF-8 -*-

from colorconsole.terminal import get_terminal
import time
import sys
import threading
if sys.version_info[0] <= 2:
    import Queue as queue
else:
    import queue

class Loading(threading.Thread):
    def __init__(self, frames=None):
        # Frames takes each frame seperated by a space with the very last frame
        # being the "done" frame.

        # Initialize self into a threading object and start running it.
        super(Loading, self).__init__()
        self.text_queue = queue.Queue()
        self.setDaemon(True)

        # Internal variables
        if frames == None:
            self.change_frames("snake")
        else:
            self.frames = frames.split(" ")
            self.time = 0.03
        self.t = get_terminal()
        self.text = ""
        self.frame = 0
        sys.stdout.write("\x1b[7")

    def change_frames(self, key):
        # Valid types: dots, circles
        frames = {
            "snake":    ("⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏ ⠿", 0.03),
            "fatsnake": ("⣾ ⣽ ⣻ ⢿ ⡿ ⣟ ⣯ ⣷ ⣿", 0.1),
            "drumming": ("⠋ ⠙ ⠚ ⠞ ⠖ ⠦ ⠴ ⠲ ⠳ ⠓ ⠿", 0.03),
            "pouring":  ("⠄ ⠆ ⠇ ⠋ ⠙ ⠸ ⠰ ⠠ ⠰ ⠸ ⠙ ⠋ ⠇ ⠆ ⠿", 0.05),
            "curls":    ("⠋ ⠙ ⠚ ⠒ ⠂ ⠂ ⠒ ⠲ ⠴ ⠦ ⠖ ⠒ ⠐ ⠐ ⠒ ⠓ ⠋ ⠿", 0.05),
            "jumping":  ("⢄ ⢂ ⢁ ⡁ ⡈ ⡐ ⡠ ⠿", 0.05),
            "flash":     ("◯ ◉ ● ◉ ●", 0.2),
            "circles":  ("◜ ◠ ◝ ◞ ◡ ◟ ◯", 0.1),
            "bars":     ("▁ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ █", 0.1),
            "wheel":    ("| / - \\ |", 0.3),
            "pulse":    ("▉ ▊ ▋ ▌ ▍ ▎ ▏ ▎ ▍ ▌ ▋ ▊ ▉", 0.03),
            "arrows":   ("← ↖ ↑ ↗ → ↘ ↓ ↙ ↑", 0.1),
            "pipes":    ("┤ ┘ ┴ └ ├ ┌ ┬ ┐ ─", 0.1),
            "grow":     (". o O ° O o O", 0.1),
            "evolve":   (". o O @ * @ O o *", 0.1),
            "eyes":     ("◡◡ ⊙⊙ ◠◠ ⊙⊙ ⊙⊙", 0.3),
            "trigram":  ("☰ ☱ ☳ ☷ ☶ ☴ ☰ ☰ ☰", 0.1),
            "sphere":   ("🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘 🌑", 0.1),
            "dot":      ("⠁ ⠂ ⠄ ⡀ ⢀ ⠠ ⠐ ⠈ .", 0.05)
        }

        if frames.get(key) == None:
            raise KeyError("Not a valid type. Must be of type: %s" % switch.keys())
        else:
            self.frames, self.time = frames.get(key)
            self.frames = self.frames.split(" ")

    def write_text(self, frame=None, text=None):
        if not frame: frame = self.frame
        if not text:  text  = self.text
        sys.stdout.write("\x1b[8")
        print (text.replace("%s", "{0}").format(self.frames[frame]))

    def color_frames(self, n):
        # cyan = 36; purple = 35; blue = 34; green = 32; yellow = 33; red = 31
        self.frames = ["\x1b[" + str(n) + "m\x1b[1m" + s + "\x1b[0m" for s in self.frames]

    def log(self, text):
        self.text_queue.put(text)

    def end(self, text=None):
        if text == None: text = self.text
        self.text_queue.put("quit")
        self.write_text(frame=-1, text=text)
        self.join()

    def run(self):
        while True:
            if not self.text_queue.empty():
                self.text = self.text_queue.get()
            if self.text == "quit":
                break

            if self.text:
                if self.frame > len(self.frames) - 2:
                    self.frame = 0
                self.write_text()
                self.t.move_up()
                time.sleep(self.time)
                self.frame += 1

l = Loading()
l.start()
l.color_frames(36)
l.log("%s" + "Loading THE THING".center(20) + "%s")
time.sleep(3)
l.change_frames("pouring")
l.color_frames(36)
l.log("%s" + "Still loading".center(20) + "%s")
time.sleep(3)
l.end("%s" + "Done Loading".center(20) + "%s")