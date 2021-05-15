class Attack:
    
    """
    This class makes and updates a 2D matrix of squares that are being threatened for both colors.
    Also checks for checks.

    Attributes:
        white_attacks = 2D matrix of squares that are being attacked by white.
        black_attacks = 2D matrix of squares that are being attacked by black.
        GS: Gamestate class.
        Result: Result class.
    """

    def __init__(self, GS, Result):
        """Constructor for the class.

        Args:
            GS: GameState class.
            Result: Result class.
        """

        self.white_attacks = [[0]*8 for _ in range(8)]
        self.black_attacks = [[0]*8 for _ in range(8)]
        self.GS = GS
        self.Result = Result

    def whiteThreatens(self, state):
        """Makes and updates the 2D matrix for white.
        Different functions for every rank of pieces except pawns.

        Args:
            state: State of the board.
        """

        self.white_attacks = [[0]*8 for _ in range(8)]
        for row in range(8):
            for column in range(8):
                piece = state[row][column]
                if piece != "" and piece[0] == "w":
                    if piece[1] == "P":
                        if 0 <= row-1 <= 7:
                            if 0 <= column-1 <= 7:
                                self.white_attacks[row-1][column-1] = 1
                            if 0 <= column+1 <= 7:
                                self.white_attacks[row-1][column+1] = 1
                    if piece[1] == "R":
                        attacks = self.rookAttacks(row, column, state)
                        for attack in attacks:
                            self.white_attacks[attack[0]][attack[1]] = 1
                    if piece[1] == "B":
                        attacks = self.bishopAttacks(row, column, state)
                        for attack in attacks:
                            self.white_attacks[attack[0]][attack[1]] = 1
                    if piece[1] == "N":
                        attacks = self.knightAttacks(row, column)
                        for attack in attacks:
                            self.white_attacks[attack[0]][attack[1]] = 1
                    if piece[1] == "Q":
                        attacks = self.queenAttacks(row, column, state)
                        for attack in attacks:
                            self.white_attacks[attack[0]][attack[1]] = 1
                    if piece[1] == "K":
                        attacks = self.kingAttacks(row, column)
                        for attack in attacks:
                            self.white_attacks[attack[0]][attack[1]] = 1

    def blackThreatens(self, state):
        """Makes and updates the 2D matrix for black.
        Different functions for every rank of pieces except pawns.

        Args:
            state: State of the board.
        """

        self.black_attacks = [[0]*8 for _ in range(8)]
        for row in range(8):
            for column in range(8):
                piece = state[row][column]
                if piece != "" and piece[0] == "b":
                    if piece[1] == "P":
                        if 0 <= row+1 <= 7:
                            if 0 <= column-1 <= 7:
                                self.black_attacks[row+1][column-1] = 1
                            if 0 <= column+1 <= 7:
                                self.black_attacks[row+1][column+1] = 1
                    if piece[1] == "R":
                        attacks = self.rookAttacks(row, column, state)
                        for attack in attacks:
                            self.black_attacks[attack[0]][attack[1]] = 1
                    if piece[1] == "B":
                        attacks = self.bishopAttacks(row, column, state)
                        for attack in attacks:
                            self.black_attacks[attack[0]][attack[1]] = 1
                    if piece[1] == "N":
                        attacks = self.knightAttacks(row, column)
                        for attack in attacks:
                            self.black_attacks[attack[0]][attack[1]] = 1
                    if piece[1] == "Q":
                        attacks = self.queenAttacks(row, column, state)
                        for attack in attacks:
                            self.black_attacks[attack[0]][attack[1]] = 1
                    if piece[1] == "K":
                        attacks = self.kingAttacks(row, column)
                        for attack in attacks:
                            self.black_attacks[attack[0]][attack[1]] = 1

    def rookAttacks(self, row, column, state):
        """Checks all the squares that rooks attack.

        Args:
            row: The row where the piece is.
            column: The columnn where the piece is.
            state: The state of the board.

        Returns:
            All the squares that the piece attacks.
        """

        attacks = []
        for y in range(row+1, 8):
            attacks.append((y, column))
            if state[y][column] != "":
                break
        for y in range(row-1, -1, -1):
            attacks.append((y, column))
            if state[y][column] != "":
                break
        for x in range(column+1, 8):
            attacks.append((row, x))
            if state[row][x] != "":
                break
        for x in range(column-1, -1, -1):
            attacks.append((row, x))
            if state[row][x] != "":
                break
        return attacks

    def bishopAttacks(self, row, column, state):
        """Checks all the squares that bishops attack.

        Args:
            row: The row where the piece is.
            colum: The column where the piece is.
            state: The state of the board.

        Returns:
            All the squares that the piece attacks.
        """

        attacks = []
        i = 1
        for y in range(row+1, 8):
            if column+i >= 8:
                break
            attacks.append((y, column+i))
            if state[y][column+i] != "":
                break
            i += 1
        i = -1
        for y in range(row+1, 8):
            if column+i <= -1:
                break
            attacks.append((y, column+i))
            if state[y][column+i] != "":
                break
            i -= 1
        i = 1
        for y in range(row-1, -1, -1):
            if column+i >= 8:
                break
            attacks.append((y, column+i))
            if state[y][column+i] != "":
                break
            i += 1
        i = -1
        for y in range(row-1, -1, -1):
            if column+i <= -1:
                break
            attacks.append((y, column+i))
            if state[y][column+i] != "":
                break
            i -= 1
        return attacks

    def knightAttacks(self, row, column):
        """Checks all the squares that knights attack.

        Args:
            row: The row where the piece is.
            colum: The column where the piece is.

        Returns:
            All the squares that the piece attacks.
        """

        attacks = []
        if 0 <= row + 2 <= 7:
            if 0 <= column + 1 <= 7:
                attacks.append((row+2, column+1))
            if 0 <= column - 1 <= 7:
                attacks.append((row+2, column-1))
        if 0 <= row - 2 <= 7:
            if 0 <= column + 1 <= 7:
                attacks.append((row-2, column+1))
            if 0 <= column - 1 <= 7:
                attacks.append((row-2, column-1))
        if 0 <= row + 1 <= 7:
            if 0 <= column + 2 <= 7:
                attacks.append((row+1, column+2))
            if 0 <= column - 2 <= 7:
                attacks.append((row+1, column-2))
        if 0 <= row - 1 <= 7:
            if 0 <= column + 2 <= 7:
                attacks.append((row-1, column+2))
            if 0 <= column - 2 <= 7:
                attacks.append((row-1, column-2))
        return attacks

    def queenAttacks(self, row, column, state):
        """Checks all the squares that queens attack.
        Uses the functions for rooks and bishops.

        Args:
            row: The row where the piece is.
            colum: The column where the piece is.
            state: The state of the board.

        Returns:
            All the squares that the piece attacks.
        """

        attacks = self.rookAttacks(row, column, state)
        diag = self.bishopAttacks(row, column, state)
        for i in diag:
            attacks.append(i)
        return attacks

    def kingAttacks(self, row, column):
        """Checks all the squares that kings attack.

        Args:
            row: The row where the piece is.
            colum: The column where the piece is.

        Returns:
            All the squares that the piece attacks.
        """

        attacks = []
        if 0 <= row+1 <= 7:
            attacks.append((row+1, column))
            if 0 <= column + 1 <= 7:
                attacks.append((row+1, column+1))
            if 0 <= column - 1 <= 7:
                attacks.append((row+1, column-1))
        if 0 <= row-1 <= 7:
            attacks.append((row-1, column))
            if 0 <= column + 1 <= 7:
                attacks.append((row-1, column+1))
            if 0 <= column - 1 <= 7:
                attacks.append((row-1, column-1))
        if 0 <= column + 1 <= 7:
            attacks.append((row, column+1))
        if 0 <= column - 1 <= 7:
            attacks.append((row, column-1))
        return attacks

    def check(self):
        """Checks for check for both colors.
        If there is a check, then asks if checkmate.
        If checkmate, adjusts the game result accordingly.
        """

        self.GS.white_in_check = False
        self.GS.black_in_check = False
        kings = self.GS.find_kings()
        wk = kings[0]
        bk = kings[1]
        if self.black_attacks[wk[1]][wk[0]] == 1:
            self.GS.white_in_check = True
            if self.Result.check_checkmate():
                self.game_result = 3
        if self.white_attacks[bk[1]][bk[0]] == 1:
            self.GS.black_in_check = True
            if self.Result.check_checkmate():
                self.game_result = 1

    def check_after(self, piece, s_pos, d_pos, copy):
        """If a move is valid otherwise, this function checks
        that the move does not bring your own king into a check.
        Uses a copy of the boardstate, makes the move on the copy and makes a new 2D attack matrix from that.
        So if the move would bring your own king into a check it does not affect the real boardstate or 2D attack matrix.

        Args:
            piece: Piece that is trying to move.
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.
            copy: Copy of the real boardsate.

        Returns:
            True if the move brings your own king into a check, otherwise False.
        """

        kings = self.GS.find_kings()
        if piece[1] == "K" and piece[0] == "w":
            wk = d_pos
            bk = kings[1]
        elif piece[1] == "K" and piece[0] == "b":
            wk = kings[0]
            bk = d_pos
        else:
            wk = kings[0]
            bk = kings[1]
        if self.GS.move_white:
            copy[s_pos[1]][s_pos[0]] = ""
            copy[d_pos[1]][d_pos[0]] = piece
            previous = [i[:] for i in self.black_attacks]
            self.blackThreatens(copy)
            if self.black_attacks[wk[1]][wk[0]] == 1:
                self.black_attacks = previous
                return True
            self.black_attacks = previous
        else:
            copy[s_pos[1]][s_pos[0]] = ""
            copy[d_pos[1]][d_pos[0]] = piece
            previous = [i[:] for i in self.white_attacks]
            self.whiteThreatens(copy)
            if self.white_attacks[bk[1]][bk[0]] == 1:
                self.white_attacks = previous
                return True
            self.white_attacks = previous
        return False
