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
Here's a simple banner made with `draftlog`. If you want to see some more examples, check out the  [`examples`](https://github.com/kepoorhampond/python-draftlog/tree/master/examples) folder!
```python
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
```
Please note that you can specify the arguments `loader` and `update`. If `loader` is set to `True`, then when the interval ends depends on the other intervals. If `update` is set to `False`, then rather than updating the `draft.log()` line, it will append on the new lines after it with each update.

## How does it do like it does?
It generates timings based off of the `intervals` you add and overwrites the `draft.log()` lines with ANSI escape codes! Since it's very open-ended, you can make practically anything with it! In the [`examples`](https://github.com/kepoorhampond/python-draftlog/tree/master/examples) folder I've already made a sample install, a multi-line progress bar, and more!

## Have questions?
If you still have questions or need some help, email me at `kepoorh@gmail.com`, all feedback is appreciated!