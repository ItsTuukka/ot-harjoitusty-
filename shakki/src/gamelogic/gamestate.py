class GameState:

    """This class is responsible for keeping track of the game/boardstate and making changes to it

    Attributes:
        boardstate: Current boardstate of the game.
        move_log: Move log for moves.
        move_white: Boolean for white to move.
        white_in_check: Boolean for white in check.
        black_in_check. Boolean for black in check.
        white_king_moved: Boolean for has the white king moved.
        black_king_moved: Boolean for has the black king moved.
        lw_rook_moved: Boolean for has the left white rook moved.
        rw_rook_moved: Boolean for has the right white rook moved.
        lb_rook_moved: Boolean for has the left black rook moved.
        rb_rook_moved: Boolean for has the right black rook moved.

    """

    def __init__(self):
        """Constructor for the class.
        """

        self.boardstate = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                           ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                           ["", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", ""],
                           ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                           ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.move_log = []
        self.move_white = True
        self.white_in_check = False
        self.black_in_check = False
        self.game_result = None
        self.white_king_moved = False
        self.black_king_moved = False
        self.lw_rook_moved = False
        self.rw_rook_moved = False
        self.lb_rook_moved = False
        self.rb_rook_moved = False

    def changeBoardState(self, piece, s_pos, d_pos, castle, enpassant):
        """Gets information from the move piece function and makes changes
        to the boardstate accordingly. Also changes turns.

        Args:
            piece: Piece that is trying to move.
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.
            castle: True if player is trying to castle, otherwise False.
            enpassant: True if the player is trying to enpassant, otherwise False.
        """

        if self.move_white:
            if piece[0] == "b":
                return
            if piece[1] == "P" and d_pos[1] == 0:
                piece = "wQ"
            if piece[1] == "K":
                self.white_king_moved = True
            if piece[1] == "R":
                if s_pos == (0, 7):
                    self.lw_rook_moved = True
                if s_pos == (7, 7):
                    self.rw_rook_moved = True
            self.move_white = False
        else:
            if piece[0] == "w":
                return
            if piece[1] == "P" and d_pos[1] == 7:
                piece = "bQ"
            if piece[1] == "K":
                self.black_king_moved = True
            if piece[1] == "R":
                if s_pos == (0, 0):
                    self.lb_rook_moved = True
                if s_pos == (7, 0):
                    self.rb_rook_moved = True
            self.move_white = True
        if castle:
            if d_pos[0] > s_pos[0]:
                self.boardstate[s_pos[1]][s_pos[0]+1] = piece[0] + "R"
                self.boardstate[s_pos[1]][s_pos[0]+2] = piece
            else:
                self.boardstate[s_pos[1]][s_pos[0]-1] = piece[0] + "R"
                self.boardstate[s_pos[1]][s_pos[0]-2] = piece
            self.boardstate[s_pos[1]][s_pos[0]] = ""
            self.boardstate[d_pos[1]][d_pos[0]] = ""
            self.move_log.append((s_pos, d_pos, piece[0], "castle"))
        else:
            self.boardstate[s_pos[1]][s_pos[0]] = ""
            self.boardstate[d_pos[1]][d_pos[0]] = piece
            if enpassant:
                lastmove = self.move_log[-1]
                self.boardstate[lastmove[1][1]][lastmove[1][0]] = ""
            self.move_log.append((s_pos, d_pos, piece))

    def betweenDiagonally(self, s_pos, d_pos):
        """If a piece tries to move diagonally, this function checks
        is there anything between. Used to validate moves.

        Args:
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.

        Returns:
            True, if nothing between, otherwise False.
        """

        dif = abs(s_pos[0]-s_pos[1])
        step = -1
        if d_pos[0] > s_pos[0]:
            if d_pos[1] > s_pos[1]:
                if s_pos[0] > s_pos[1]:
                    dif = -dif
                for i in range(s_pos[0]+1, d_pos[0]):
                    if self.boardstate[i+dif][i] != "":
                        return True
            else:
                for i in range(s_pos[0]+1, d_pos[0]):
                    if self.boardstate[s_pos[1]+step][i] != "":
                        return True
                    step -= 1
        else:
            if d_pos[1] > s_pos[1]:
                for i in range(d_pos[0]+1, s_pos[0]):
                    if self.boardstate[d_pos[1]+step][i] != "":
                        return True
                    step -= 1
            else:
                if s_pos[0] > s_pos[1]:
                    dif = -dif
                for i in range(d_pos[0]+1, s_pos[0]):
                    if self.boardstate[i+dif][i] != "":
                        return True
        return False

    def betweenVertically(self, s_pos, d_pos):
        """If a piece tries to move vertically, this function checks
        is there anything between. Used to validate moves.

        Args:
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.

        Returns:
            True, if nothing between, otherwise False.
        """

        if d_pos[1] > s_pos[1]:
            step = 1
        else:
            step = -1
        for i in range(s_pos[1]+step, d_pos[1], step):
            if self.boardstate[i][s_pos[0]] != "":
                return True
        return False

    def betweenHorizontally(self, s_pos, d_pos):
        """If a piece tries to move horizontally, this function checks
        is there anything between. Used to validate moves.

        Args:
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.

        Returns:
            True, if nothing between, otherwise False.
        """

        if d_pos[0] > s_pos[0]:
            step = 1
        else:
            step = -1
        for i in range(s_pos[0]+step, d_pos[0], step):
            if self.boardstate[s_pos[1]][i] != "":
                return True
        return False

    def find_kings(self):
        """Finds both kings from the board.

        Returns:
            Tuple, containing coordinates for the kings.
        """

        wk = ""
        bk = ""
        for row in range(8):
            for column in range(8):
                piece = self.boardstate[row][column]
                if piece == "wK":
                    wk = (column, row)
                if piece == "bK":
                    bk = (column, row)
        return (wk, bk)
