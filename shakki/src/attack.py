class Attack:
    
    """
    This class makes and updates a 2D matrix of squares that are being threatened for both colors
    """

    def __init__(self, GS, Result):
        self.whiteAttacks = [[0]*8 for _ in range(8)]
        self.blackAttacks = [[0]*8 for _ in range(8)]
        self.GS = GS
        self.Result = Result

    def whiteThreatens(self, state):
        self.whiteAttacks = [[0]*8 for _ in range(8)]
        for row in range(8):
            for colum in range(8):
                piece = state[row][colum]
                if piece != "" and piece[0] == "w":
                    if piece[1] == "P":
                        if 0 <= row-1 <= 7:
                            if 0 <= colum-1 <= 7:
                                self.whiteAttacks[row-1][colum-1] = 1
                            if 0 <= colum+1 <= 7:
                                self.whiteAttacks[row-1][colum+1] = 1
                    if piece[1] == "R":
                        attacks = self.rookAttacks(row, colum, state)
                        for attack in attacks:
                            self.whiteAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "B":
                        attacks = self.bishopAttacks(row, colum, state)
                        for attack in attacks:
                            self.whiteAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "N":
                        attacks = self.knightAttacks(row, colum)
                        for attack in attacks:
                            self.whiteAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "Q":
                        attacks = self.queenAttacks(row, colum, state)
                        for attack in attacks:
                            self.whiteAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "K":
                        attacks = self.kingAttacks(row, colum)
                        for attack in attacks:
                            self.whiteAttacks[attack[0]][attack[1]] = 1

    def blackThreatens(self, state):
        self.blackAttacks = [[0]*8 for _ in range(8)]
        for row in range(8):
            for colum in range(8):
                piece = state[row][colum]
                if piece != "" and piece[0] == "b":
                    if piece[1] == "P":
                        if 0 <= row+1 <= 7:
                            if 0 <= colum-1 <= 7:
                                self.blackAttacks[row+1][colum-1] = 1
                            if 0 <= colum+1 <= 7:
                                self.blackAttacks[row+1][colum+1] = 1
                    if piece[1] == "R":
                        attacks = self.rookAttacks(row, colum, state)
                        for attack in attacks:
                            self.blackAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "B":
                        attacks = self.bishopAttacks(row, colum, state)
                        for attack in attacks:
                            self.blackAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "N":
                        attacks = self.knightAttacks(row, colum)
                        for attack in attacks:
                            self.blackAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "Q":
                        attacks = self.queenAttacks(row, colum, state)
                        for attack in attacks:
                            self.blackAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "K":
                        attacks = self.kingAttacks(row, colum)
                        for attack in attacks:
                            self.blackAttacks[attack[0]][attack[1]] = 1

    def rookAttacks(self, row, colum, state):
        attacks = []
        for y in range(row+1, 8):
            attacks.append((y, colum))
            if state[y][colum] != "":
                break
        for y in range(row-1, -1, -1):
            attacks.append((y, colum))
            if state[y][colum] != "":
                break
        for x in range(colum+1, 8):
            attacks.append((row, x))
            if state[row][x] != "":
                break
        for x in range(colum-1, -1, -1):
            attacks.append((row, x))
            if state[row][x] != "":
                break
        return attacks

    def bishopAttacks(self, row, colum, state):
        attacks = []
        i = 1
        for y in range(row+1, 8):
            if colum+i >= 8:
                break
            attacks.append((y, colum+i))
            if state[y][colum+i] != "":
                break
            i += 1
        i = -1
        for y in range(row+1, 8):
            if colum+i <= -1:
                break
            attacks.append((y, colum+i))
            if state[y][colum+i] != "":
                break
            i -= 1
        i = 1
        for y in range(row-1, -1, -1):
            if colum+i >= 8:
                break
            attacks.append((y, colum+i))
            if state[y][colum+i] != "":
                break
            i += 1
        i = -1
        for y in range(row-1, -1, -1):
            if colum+i <= -1:
                break
            attacks.append((y, colum+i))
            if state[y][colum+i] != "":
                break
            i -= 1
        return attacks

    def knightAttacks(self, row, colum):
        attacks = []
        if 0 <= row + 2 <= 7:
            if 0 <= colum + 1 <= 7:
                attacks.append((row+2, colum+1))
            if 0 <= colum - 1 <= 7:
                attacks.append((row+2, colum-1))
        if 0 <= row - 2 <= 7:
            if 0 <= colum + 1 <= 7:
                attacks.append((row-2, colum+1))
            if 0 <= colum - 1 <= 7:
                attacks.append((row-2, colum-1))
        if 0 <= row + 1 <= 7:
            if 0 <= colum + 2 <= 7:
                attacks.append((row+1, colum+2))
            if 0 <= colum - 2 <= 7:
                attacks.append((row+1, colum-2))
        if 0 <= row - 1 <= 7:
            if 0 <= colum + 2 <= 7:
                attacks.append((row-1, colum+2))
            if 0 <= colum - 2 <= 7:
                attacks.append((row-1, colum-2))
        return attacks

    def queenAttacks(self, row, colum, state):
        attacks = self.rookAttacks(row, colum, state)
        diag = self.bishopAttacks(row, colum, state)
        for i in diag:
            attacks.append(i)
        return attacks

    def kingAttacks(self, row, colum):
        attacks = []
        if 0 <= row+1 <= 7:
            attacks.append((row+1, colum))
            if 0 <= colum + 1 <= 7:
                attacks.append((row+1, colum+1))
            if 0 <= colum - 1 <= 7:
                attacks.append((row+1, colum-1))
        if 0 <= row-1 <= 7:
            attacks.append((row-1, colum))
            if 0 <= colum + 1 <= 7:
                attacks.append((row-1, colum+1))
            if 0 <= colum - 1 <= 7:
                attacks.append((row-1, colum-1))
        if 0 <= colum + 1 <= 7:
            attacks.append((row, colum+1))
        if 0 <= colum - 1 <= 7:
            attacks.append((row, colum-1))
        return attacks

    def check(self):
        self.GS.white_in_check = False
        self.GS.black_in_check = False
        kings = self.GS.find_kings()
        wk = kings[0]
        bk = kings[1]
        if self.blackAttacks[wk[1]][wk[0]] == 1:
            self.GS.white_in_check = True
            if self.Result.check_checkmate():
                self.GS.Game_Result = 3
        if self.whiteAttacks[bk[1]][bk[0]] == 1:
            self.GS.black_in_check = True
            if self.Result.check_checkmate():
                self.GS.Game_Result = 1

    def check_after(self, piece, s_pos, d_pos, copy):
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
        if self.GS.moveWhite:
            copy[s_pos[1]][s_pos[0]] = ""
            copy[d_pos[1]][d_pos[0]] = piece
            previous = [i[:] for i in self.blackAttacks]
            self.blackThreatens(copy)
            if self.blackAttacks[wk[1]][wk[0]] == 1:
                self.blackAttacks = previous
                return True
            self.blackAttacks = previous
        else:
            copy[s_pos[1]][s_pos[0]] = ""
            copy[d_pos[1]][d_pos[0]] = piece
            previous = [i[:] for i in self.whiteAttacks]
            self.whiteThreatens(copy)
            if self.whiteAttacks[bk[1]][bk[0]] == 1:
                self.whiteAttacks = previous
                return True
            self.whiteAttacks = previous
        return False
