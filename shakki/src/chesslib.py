import chess


class Result:

    """
    This class uses the chess library for python and is only used to check for checkmate or stalemate
    """

    def __init__(self, GS):
        self.GS = GS
        self.board = chess.Board()
        notations = self.notation_maker()
        self.rows = notations[0]
        self.colums = notations[1]

    def notation_maker(self):
        rows = {}
        colums = {}
        value = 8
        for i in range(8):
            rows[i] = value
            value -= 1
        atoh = "abcdefgh"
        index = 0
        for i in range(8):
            colums[i] = atoh[index]
            index += 1
        return [rows, colums]

    def move(self, s_pos, d_pos):
        sx = s_pos[0]
        sy = s_pos[1]
        dx = d_pos[0]
        dy = d_pos[1]
        sq = self.colums[sx] + str(self.rows[sy])
        dq = self.colums[dx] + str(self.rows[dy])
        move = sq + dq
        Move = chess.Move.from_uci(move)
        self.board.push(Move)
        print(self.board)

    def check_checkmate(self):
        return self.board.is_checkmate()

    def check_stalemate(self):
        if self.board.is_stalemate():
            self.GS.Game_Result = 2
