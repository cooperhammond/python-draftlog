# Draftlog
> :scroll: Fancy logs with expandable tools. Bring life to your terminal!

[![demo](http://i.imgur.com/rWE21Ts.gif)](http://i.imgur.com/rWE21Ts.gif)

[![License: MIT](https://img.shields.io/badge/license-mit-blue.svg?style=flat-square)](https://mit-license.org/)
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
Here's about the simplest program with `draftlog` that actually does something:
```python
import draftlog
import time

draft = draftlog.inject()

print ("The line below me will be updated!")
update_me = draft.log("I will be updated!")
print ("The line above me will be updated!")

time.sleep(3)

update_me.update("I've been updated!")
```

Here's a more complicated program: a scrolling banner . If you want to see some more examples in this thread, check out the  [`examples`](https://github.com/kepoorhampond/python-draftlog/tree/master/examples) folder!
```python
import draftlog

draft = draftlog.inject()

class Banner:
    def __init__(self, string):
        self.string = string
        self.counter = 0
    def scroll(self):
        if self.counter >= 50:
            # This is what exits out of the loop in:
            # "draft.log().set_interval"
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

# You can still print stuff after starting the draft as well:
import time
time.sleep(2)
print ("Wow, some more text!")
```

`set_interval` is a function that takes another function and the time to wait. It overwrites the `draft.log()` line with whatever the function returns. The function will stop being called once it `raises draftlog.Exception`. `draft.start()` will actually start all intervals that have been set.

### How
`draft.log()` creates a `DraftLog` object that keeps track of what line it was created on. You can call `update(text)` on it to update the line that it's set on.

`draft.log().set_interval(function, time)` primes an interval in a background threading process called `DaemonDrafter`. When `draft.start()` is called, it generates interval timing based off of the time specified and then runs it in "frames."

Since I've made the program open-ended, you can create a lot (see the [`examples`](https://github.com/kepoorhampond/python-draftlog/tree/master/examples) folder) of stuff.

## Questions
If you still have questions or need some help, check out the [wiki](https://github.com/kepoorhampond/python-draftlog/wiki/) or email me at `kepoorh@gmail.com`, all feedback is appreciated!