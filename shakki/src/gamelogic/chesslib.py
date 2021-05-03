import chess


class Result:

    """
    This class uses the chess library for python and is only used to check for the result of the game.
    These results include: checkmate, stalemate, draw by insufficient material 
    and draw by fivefold repetition of moves.
    """

    def __init__(self, GS):
        self.GS = GS
        self.board = chess.Board()
        notations = self.notation_maker()
        self.rows = notations[0]
        self.colums = notations[1]

    def notation_maker(self):
        """Makes notation dictionaries for rows and colums.
        """
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
        """Moves pieces on the chess library board.
        Needed for keeping it updated, so it can detect the result of the game.
        """
        sx = s_pos[0]
        sy = s_pos[1]
        dx = d_pos[0]
        dy = d_pos[1]
        sq = self.colums[sx] + str(self.rows[sy])
        dq = self.colums[dx] + str(self.rows[dy])
        move = sq + dq
        Move = chess.Move.from_uci(move)
        self.board.push(Move)

    def check_checkmate(self):
        """Checks for checkmate, funtion by chess library.
        """
        return self.board.is_checkmate()

    def check_stalemate(self):
        """Checks for checmate, function by chess library.
        If True, game result is draw.
        """
        if self.board.is_stalemate():
            self.GS.Game_Result = 2

    def insufficient_material(self):
        """Checks for insufficient material, function by chess library.
        If True, game result is draw.
        """
        if self.board.is_insufficient_material():
            self.GS.Game_Result = 2

    def fivefold_repetition(self):
        """Checks for fivefold repetition, function by chess library.
        If True, game result is draw.
        """
        if self.board.is_fivefold_repetition():
            self.GS.Game_Result = 2
