# Draftlog
> :scroll: Fancy logs with expandable tools. Bring life to your terminal!

[![demo](http://i.imgur.com/nMqj7Rr.gif)](http://i.imgur.com/nMqj7Rr.gif)

[![License: GNU](https://img.shields.io/badge/license-gnu-yellow.svg?style=flat-square)](http://www.gnu.org/licenses/gpl.html)
[![Build Status](https://img.shields.io/travis/kepoorhampond/python-draftlog/master.svg?style=flat-square)](https://travis-ci.org/kepoorhampond/python-draftlog)
[![PyPI](https://img.shields.io/badge/pypi-draftlog-blue.svg?style=flat-square)](https://pypi.python.org/pypi/draftlog)
[![Say Thanks](https://img.shields.io/badge/say-thanks-ff69b4.svg?style=flat-square)](https://saythanks.io/to/kepoorhampond)

A module useful for CLI's, logs and pretty much any cool multi-line python tool.

All inspiration goes to [Ivan Seidel](https://github.com/ivanseidel) with [`node-draftlog`](https://github.com/ivanseidel/node-draftlog).

Works with Python 2 and 3.

## Install
```
$ pip install draftlog
```

## Intro Example
Here's an average unexciting example of `draftlog`, if you want some more exciting ones, check out the [`examples`](https://github.com/kepoorhampond/python-draftlog/tree/master/examples) folder!
```python
# Import the module
from draftlog.draft import Draft

# Make your "interval" object.
class UpdatableText:
    def __init__(self, texts):
        self.counter = -1
        self.texts = texts
        self.status = True
    def interval(self):
        self.counter += 1
        if self.counter > len(self.texts) - 1:
            self.status = False
            self.counter = -1

        return self.texts[self.counter]
texts = ["Loading ...", "Still Loading ...", "Even more loading!", "GAH! When will it end?!"]

# Initialize a `Draft` object...
d = Draft()
# Add your interval object...
d.add_interval(UpdatableText(texts), 1)
# Add some fancy text
t = d.add_text("*jeopardy music*")
# Update the fancy text after 3/4 of a second
t.update("text", "*more jeopardy music*").after(0.75)
# And start it!
d.start()
```

## How does it do like it does?
It generates frames based off of the `intervals` you add and overwrites them on a generated time basis with ANSI escape codes! Since it's very open, you can make practically anything with it! In the [`examples`](https://github.com/kepoorhampond/python-draftlog/tree/master/examples) folder I've already made a banner, a multi-line progress bar, and more! 

For a more in-depth view of the module, look to the [wiki](https://github.com/kepoorhampond/python-draftlog/wiki).

## Have questions?
If you still have questions or need some help, email me at `kepoorh@gmail.com`, all feedback is appreciated!