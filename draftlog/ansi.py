esc =        '\x1b['
clearline =  esc + '2K' + esc + '1G'
save = esc + "7"
restore = esc + "8"

def up(n=1):
    return esc + str(n) + 'A'

def down(n=1):
    return esc + str(n) + 'B'

