class Attack:

    """
    This class makes and updates a 2D matrix of squares that are being threatened for both colors
    """

    def __init__(self, GS):
        self.whiteAttacks = [[0]*8 for _ in range(8)]
        self.blackAttacks = [[0]*8 for _ in range(8)]
        self.GS = GS

    
    def whiteThreatens(self):
        self.whiteAttacks = [[0]*8 for _ in range(8)]
        for row in range(8):
            for colum in range(8):
                piece = self.GS.boardstate[row][colum]
                if piece != "" and piece[0] == "w":
                    if piece[1] == "P":
                        if 0 <= row-1 <= 7:
                            if 0 <= colum-1 <= 7:
                                self.whiteAttacks[row-1][colum-1] = 1
                            if 0 <= colum+1 <= 7:
                                self.whiteAttacks[row-1][colum+1] = 1
                    if piece[1] == "R":
                        attacks = self.rookAttacks(row, colum)
                        for attack in attacks:
                            self.whiteAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "B":
                        attacks = self.bishopAttacks(row, colum)
                        for attack in attacks:
                            self.whiteAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "N":
                        attacks = self.knightAttacks(row, colum)
                        for attack in attacks:
                            self.whiteAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "Q":
                        attacks = self.queenAttacks(row, colum)
                        for attack in attacks:
                            self.whiteAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "K":
                        attacks = self.kingAttacks(row, colum)
                        for attack in attacks:
                            self.whiteAttacks[attack[0]][attack[1]] = 1
    

    def blackThreatens(self):
        self.blackAttacks = [[0]*8 for _ in range(8)]
        for row in range(8):
            for colum in range(8):
                piece = self.GS.boardstate[row][colum]
                if piece != "" and piece[0] == "b":
                    if piece[1] == "P":
                        if 0 <= row+1 <= 7:
                            if 0 <= colum-1 <= 7:
                                self.blackAttacks[row+1][colum-1] = 1
                            if 0 <= colum+1 <= 7:
                                self.blackAttacks[row+1][colum+1] = 1
                    if piece[1] == "R":
                        attacks = self.rookAttacks(row, colum)
                        for attack in attacks:
                            self.blackAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "B":
                        attacks = self.bishopAttacks(row, colum)
                        for attack in attacks:
                            self.blackAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "N":
                        attacks = self.knightAttacks(row, colum)
                        for attack in attacks:
                            self.blackAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "Q":
                        attacks = self.queenAttacks(row, colum)
                        for attack in attacks:
                            self.blackAttacks[attack[0]][attack[1]] = 1
                    if piece[1] == "K":
                        attacks = self.kingAttacks(row, colum)
                        for attack in attacks:
                            self.blackAttacks[attack[0]][attack[1]] = 1


    def rookAttacks(self, row, colum):
        attacks = []
        for y in range(row+1, 8):
            attacks.append((y, colum))
            if self.GS.boardstate[y][colum] != "":
                break
        for y in range(row-1, -1, -1):
            attacks.append((y, colum))
            if self.GS.boardstate[y][colum] != "":
                break
        for x in range(colum+1, 8):
            attacks.append((row, x))
            if self.GS.boardstate[row][x] != "":
                break
        for x in range (colum-1, -1, -1):
            attacks.append((row, x))
            if self.GS.boardstate[row][x] != "":
                break
        return attacks

    
    def bishopAttacks(self, row, colum):
        attacks = []
        i = 1
        for y in range(row+1, 8):
            if colum+i >= 8:
                break
            attacks.append((y, colum+i))
            if self.GS.boardstate[y][colum+i] != "":
                break
            i += 1
        i = -1
        for y in range(row+1, 8):
            if colum+i <= -1:
                break
            attacks.append((y, colum+i))
            if self.GS.boardstate[y][colum+i] != "":
                break
            i -= 1
        i = 1
        for y in range(row-1, -1, -1):
            if colum+i >= 8:
                break
            attacks.append((y, colum+i))
            if self.GS.boardstate[y][colum+i] != "":
                break
            i += 1
        i = -1 
        for y in range(row-1, -1, -1):
            if colum+i <= -1:
                break
            attacks.append((y, colum+i))
            if self.GS.boardstate[y][colum+i] != "":
                break
            i -= 1
        return attacks


    def knightAttacks(self, row, colum):
        attacks = []
        if 0 <= row + 2 <= 7:
            if 0 <= colum +1 <= 7:
                attacks.append((row+2, colum+1))
            if 0 <= colum -1 <= 7:
                attacks.append((row+2, colum-1))
        if 0 <= row - 2 <= 7:
            if 0 <= colum +1 <= 7:
                attacks.append((row-2, colum+1))
            if 0 <= colum -1 <= 7:
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

    
    def queenAttacks(self, row, colum):
        attacks = self.rookAttacks(row, colum)
        diag = self.bishopAttacks(row, colum)
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

            