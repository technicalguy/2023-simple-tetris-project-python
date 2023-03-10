import copy
import itertools
import random


class Tetris:
    _ = False
    Z = True
    _PIECES = (
        (
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, Z, Z, Z),
                (_, _, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, Z, _),
                (_, Z, Z, _),
                (_, _, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, Z, _),
                (_, Z, Z, Z),
                (_, _, _, _),
            ),
            (
                (_, _, _, _),
                (_, _, Z, _),
                (_, _, Z, Z),
                (_, _, Z, _),
            ),
        ),
        (
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, Z, Z, Z),
                (_, _, _, Z),
            ),
            (
                (_, _, _, _),
                (_, _, Z, _),
                (_, _, Z, _),
                (_, Z, Z, _),
            ),
            (
                (_, _, _, _),
                (_, Z, _, _),
                (_, Z, Z, Z),
                (_, _, _, _),
            ),
            (
                (_, _, _, _),
                (_, _, Z, Z),
                (_, _, Z, _),
                (_, _, Z, _),
            ),
        ),
        (
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, Z, Z, _),
                (_, _, Z, Z),
            ),
            (
                (_, _, _, _),
                (_, _, _, Z),
                (_, _, Z, Z),
                (_, _, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, Z, Z, _),
                (_, _, Z, Z),
            ),
            (
                (_, _, _, _),
                (_, _, _, Z),
                (_, _, Z, Z),
                (_, _, Z, _),
            ),
        ),
        (
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, Z, Z, _),
                (_, Z, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, Z, Z, _),
                (_, Z, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, Z, Z, _),
                (_, Z, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, Z, Z, _),
                (_, Z, Z, _),
            ),
        ),
        (
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, _, Z, Z),
                (_, Z, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, Z, _),
                (_, _, Z, Z),
                (_, _, _, Z),
            ),
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, _, Z, Z),
                (_, Z, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, Z, _),
                (_, _, Z, Z),
                (_, _, _, Z),
            ),
        ),
        (
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, _, Z, Z),
                (_, Z, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, Z, _),
                (_, _, Z, Z),
                (_, _, _, Z),
            ),
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, _, Z, Z),
                (_, Z, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, Z, _),
                (_, _, Z, Z),
                (_, _, _, Z),
            ),
        ),
        (
            (
                (_, _, _, _),
                (_, _, _, _),
                (_, Z, Z, Z),
                (_, Z, _, _),
            ),
            (
                (_, _, _, _),
                (_, Z, Z, _),
                (_, _, Z, _),
                (_, _, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, _, Z),
                (_, Z, Z, Z),
                (_, _, _, _),
            ),
            (
                (_, _, _, _),
                (_, _, Z, _),
                (_, _, Z, _),
                (_, _, Z, Z),
            ),
        ),
        (
            (
                (_, _, _, _),
                (_, _, _, _),
                (Z, Z, Z, Z),
                (_, _, _, _),
            ),
            (
                (_, _, Z, _),
                (_, _, Z, _),
                (_, _, Z, _),
                (_, _, Z, _),
            ),
            (
                (_, _, _, _),
                (_, _, _, _),
                (Z, Z, Z, Z),
                (_, _, _, _),
            ),
            (
                (_, _, Z, _),
                (_, _, Z, _),
                (_, _, Z, _),
                (_, _, Z, _),
            ),
        ),
    )

    _WIDTH = 10
    _HEIGHT = 20

    def __init__(self):
        self.board = [[False] * Tetris._WIDTH] * Tetris._HEIGHT
        self.shuffle()
        self.next = self.upcoming.pop()
        self.new_piece()

    def new_piece(self):
        self.piece = Tetris._PIECES[self.next]
        if not self.upcoming:
            self.shuffle()
        self.next = self.upcoming.pop()
        self.px = (Tetris._WIDTH - len(self.piece[0])) // 2
        self.py = -2

    def shuffle(self):
        pieces=list(range(len(Tetris._PIECES))) * 2
        random.shuffle(pieces)
        self.upcoming=pieces

    def __str__(self):
        fbuffer = copy.deepcopy(self.board)
        for i,j in range(len(self.piece)):
        out=[]
        out.append("Next: {}\n".format(self.next))
        header="+—" + "—".join(["—"] * Tetris._WIDTH) + "—+"
        out.append(header)
        out.append("\n")
        for row in fbuffer:
            out.append("| ")
            out.append(" ".join(("#" if x else " ") for x in row))
            out.append(" |\n")
        out.append(header)
        return "".join(out)


def main():
    actions={
        'a': 'left',
        # 'w': 'up',
        'd': 'right',
        's': 'down',
        'e': 'clockwise',
        'q': 'counterclockwise',
    }
    t=Tetris()
    while True:
        command=input()
        if command in actions:
            print(actions[command])
            print(t)
        else:
            print("Unrecognised command")


if __name__ == "__main__":
    main()
