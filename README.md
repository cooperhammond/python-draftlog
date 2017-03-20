# Draftlog
> :scroll: Fancy logs with expandable tools. Bring life to your terminal!

[![demo](http://i.imgur.com/nMqj7Rr.gif)](http://i.imgur.com/nMqj7Rr.gif)

A module that is useful for CLI's, logs and pretty much any cool multi-line python tool.

All inspiration goes to [Ivan Seidel](https://github.com/ivanseidel) with [`node-draftlog`](https://github.com/ivanseidel/node-draftlog).

Works with Python 2 and 3.

## Install
```
$ pip install draftlog
```

## Examples
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

For a more in-depth view of the module, look to the [wiki](https://github.com/kepoorhampond/python-draftlog/wiki). If you still have questions, email me at `kepoorh@gmail.com`, all questions are appreciated!
## Support on Beerpay
Hey dude! Help me out for a couple of :beers:!

[![Beerpay](https://beerpay.io/kepoorhampond/python-draftlog/badge.svg?style=beer-square)](https://beerpay.io/kepoorhampond/python-draftlog)  [![Beerpay](https://beerpay.io/kepoorhampond/python-draftlog/make-wish.svg?style=flat-square)](https://beerpay.io/kepoorhampond/python-draftlog?focus=wish)