import copy
import itertools
import random
import readchar
import sys


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
        self.score = 0
        self.board = []
        for _ in range(Tetris._HEIGHT):
            self.board.append([False] * Tetris._WIDTH)
        self.shuffle()
        self.next = self.upcoming.pop()
        self.new_piece()

    def get_piece(self):
        return Tetris._PIECES[self.pid][self.prot]

    def new_piece(self):
        self.pid = self.next
        if not self.upcoming:
            self.shuffle()
        self.next = self.upcoming.pop()
        self.prot = 0
        self.px = (Tetris._WIDTH - len(self.get_piece()[0])) // 2
        self.py = -2
        if self.piece_intersect():
            print("G A M E   O V E R")
            print("S C O R E :   {}".format(" ".join(str(self.score))))
            sys.exit(0)

    def shuffle(self):
        pieces = list(range(len(Tetris._PIECES))) * 2
        random.shuffle(pieces)
        self.upcoming = pieces

    def piece_positions(self):
        for i, j in itertools.product(
                range(len(self.get_piece())), range(len(self.get_piece()[0]))):
            if self.get_piece()[i][j]:
                yield (self.py + i, self.px + j)
        return

    def piece_board_positions(self):
        for gy, gx in self.piece_positions():
            if ((0 <= gy < Tetris._HEIGHT) and (0 <= gx < Tetris._WIDTH)):
                yield (gy, gx)
        return

    def set_piece(self):
        for i, j in self.piece_board_positions():
            self.board[i][j] = True
        i = 0
        while i < len(self.board):
            if all(self.board[i]):
                del self.board[i]
                self.score += 1
            else:
                i += 1
        while len(self.board) < Tetris._HEIGHT:
            self.board.insert(0, [False] * Tetris._WIDTH)

    def piece_out_of_bounds(self):
        """Above the top of the board is fine."""
        return not all(i < Tetris._HEIGHT and 0 <= j < Tetris._WIDTH
                       for i, j in self.piece_positions())

    def piece_intersect(self):
        return any(self.board[i][j]
                   for i, j in self.piece_board_positions())

    def move(self, dy, dx, rot=0, settle=False):
        prevrot = self.prot
        # try
        self.prot = (self.prot + rot) % 4
        self.py += dy
        self.px += dx
        if self.piece_out_of_bounds() or self.piece_intersect():
            # reset
            self.prot = prevrot
            self.py -= dy
            self.px -= dx
            if settle:
                self.set_piece()
                self.new_piece()

    def down(self):
        self.move(1, 0, 0, True)

    def right(self):
        self.move(0, 1)

    def left(self):
        self.move(0, -1)

    def cw(self):
        self.move(0, 0, 1)

    def ccw(self):
        self.move(0, 0, -1)

    def __str__(self):
        # fbuffer = [[False] * Tetris._WIDTH] * Tetris._HEIGHT
        # for i, j in itertools.product(range(Tetris._HEIGHT), range(Tetris._WIDTH)):
        #    fbuffer[i][j] = self.board[i][j]
        fbuffer = []
        for row in self.board:
            fbuffer.append([("#" if x else " ") for x in row])
        out = []
        out.append("S C O R E :   {}\n".format(" ".join(str(self.score))))
        out.append("+—N E X T—+\n")
        for i in range(len(self.get_piece())):
            out.append("| ")
            out.append(" ".join(
                ("#" if Tetris._PIECES[self.next][0][i][j] else " ")
                for j in range(len(self.get_piece()[i]))
            ))
            out.append(" |\n")
        # out.append("+—————————+\n")
        for gy, gx in self.piece_board_positions():
            fbuffer[gy][gx] = "Z"
        # out.append("Next: {}\n".format(self.next))
        header = "+—" + "—".join(["—"] * Tetris._WIDTH) + "—+"
        out.append(header)
        out.append("\n")
        for row in fbuffer:
            out.append("| ")
            out.append(" ".join(row))
            out.append(" |\n")
        out.append(header)
        return "".join(out)


def main():
    t = Tetris()
    actions = {
        'a': t.left,
        # 'w': 'up',
        'd': t.right,
        's': t.down,
        'e': t.cw,
        'q': t.ccw,
        'z': lambda: sys.exit(0),
    }
    print(t)
    while True:
        command = readchar.readchar()
        if command in actions:
            actions[command]()
            print(t)
        else:
            print("Unrecognised command")


if __name__ == "__main__":
    main()
