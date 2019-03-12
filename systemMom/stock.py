import getch as g

word = ''
while True:
    ch = g.getch()
    print ord(ch)
    if ch == '\r':
        break
