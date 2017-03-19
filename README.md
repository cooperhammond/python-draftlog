# Draftlog
> :scroll: Fancy logs and CLI tools. Bring life to your terminal!

Inspired by [`node-draftlog`](https://github.com/ivanseidel/node-draftlog).

Works with Python 2 and 3.

## Install
```
$ pip install draftlog
```

## Examples
[![demo](http://i.imgur.com/nMqj7Rr.gif)](http://i.imgur.com/nMqj7Rr.gif)
A pointless, but explanatory example:
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
# Update the fancy text after 2 seconds
d.id_interval(t).update_after("*more jeopardy music*", 0.75)
# And start it!
d.start()
```