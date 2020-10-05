import random
import curses

#using the curses for the screen.
srn = curses.initscr()

#making the curses now show on the screen.
curses.curs_set(0)

#set up for the width and hieght.
h, w = srn.getmaxyx()

sw = curses.newwin(h, w, 0, 0)
#set up keypad
sw.keypad(1)
sw.timeout(100)

#snake positions.
sn_x = w/4
sn_y = h/2

#the body of the snake.
snake = [
    [sn_y, sn_x],
    [sn_y, sn_x - 1],
    [sn_y, sn_x - 2]
]

#the food for the snake
fd = [h/2, w/2]
sw.addch(int(fd[0]), int(fd[1]), curses.ACS_PI)

#default key.
key = curses.KEY_RIGHT

while True:
    nxt_key = sw.getch()
    key = key if nxt_key == -1 else nxt_key

    if snake[0][0] in [0, h] or snake[0][1] in [0, w] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    nw_h = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        nw_h[0] += 1
    if key == curses.KEY_UP:
        nw_h[0] -= 1
    if key == curses.KEY_LEFT:
        nw_h[1] -= 1
    if key == curses.KEY_RIGHT:
        nw_h[1] += 1

    snake.insert(0, nw_h)

    #checking for the food for the snake
    if snake[0] == fd:
        fd = None
        while sfd is None:
            nt = [
                random.randint(1, h - 1),
                random.randint(1, w - 1)
            ]
            fd = nt if nt not in snake else None
        sw.addch(int(fd[0]), int(fd[1]), curses.ACS_PI)
    else:
        tl = snake.pop()
        sw.addch(int(tl[0]), int(tl[1]), ' ')
    #this generates the board.
    sw.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

















