"""
ANSI, as in the escape characters that trigger actions in the terminal.

Info:
 - https://en.wikipedia.org/wiki/ANSI_escape_code
 - http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html
 - http://ascii-table.com/ansi-escape-sequences-vt-100.php
"""

# The escape character in Python
esc = '\x1b['

# The escape characters to clear a line
clearline =  esc + '2K' + esc + '1G'

# To save the cursor state
save = esc + "7"

# To restore the cursor state
restore = esc + "8"

# Move up "n" spaces
def up(n=1):
    return esc + str(n) + 'A'

# Move down "n" spaces
def down(n=1):
    return esc + str(n) + 'B'

def code(code1):
    return "\x1b[%sm" % str(code1)

END = code(0)
BOLD = code(1)
DIM = code(2)
RED = code(31)
GREEN = code(32)
YELLOW = code(33)
BLUE = code(34)
PURPLE = code(35)
CYAN = code(36)
GRAY = code(37)
BRED = RED + BOLD
BGREEN = GREEN + BOLD
BYELLOW = YELLOW + BOLD
BBLUE = BLUE + BOLD
BPURPLE = PURPLE + BOLD
BCYAN = CYAN + BOLD
BGRAY = GRAY + BOLD