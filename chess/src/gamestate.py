class GameState:
    
    """
    This class is responsible for keeping track of the game/boardstate and making changes to it
    """

    def __init__(self):
        self.boardstate = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                           ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                           ["", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", ""],
                           ["", "", "", "", "", "", "", ""],
                           ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                           ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.move_log = []
        self.moveWhite = True
        self.wKmove = False
        self.bKmove = False
        self.LwRmove = False
        self.RwRmove = False
        self.LbRmove = False
        self.RbRmove = False

    def changeBoardState(self, piece, s_pos, d_pos, castle, enpassant):
        if self.moveWhite:
            if piece[0] == "b":
                return
            if piece[1] == "P" and d_pos[1] == 0:
                piece = "wQ"
            if piece[1] == "K":
                self.wKmove = True
            if piece[1] == "R":
                if s_pos == (0, 7):
                    self.LwRmove = True
                if s_pos == (7, 7):
                    self.RwRmove = True
            self.moveWhite = False
        else:
            if piece[0] == "w":
                return
            if piece[1] == "P" and d_pos[1] == 7:
                piece = "bQ"
            if piece[1] == "K":
                self.bKmove = True
            if piece[1] == "R":
                if s_pos == (0, 0):
                    self.LbRmove = True
                if s_pos == (7, 0):
                    self.RbRmove = True
            self.moveWhite = True
        if castle:
            if d_pos[0] > s_pos[0]:
                self.boardstate[s_pos[1]][s_pos[0]+1] = piece[0] + "R"
                self.boardstate[s_pos[1]][s_pos[0]+2] = piece
            else:
                self.boardstate[s_pos[1]][s_pos[0]-1] = piece[0] + "R"
                self.boardstate[s_pos[1]][s_pos[0]-2] = piece
            self.boardstate[s_pos[1]][s_pos[0]] = ""
            self.boardstate[d_pos[1]][d_pos[0]] = ""
            self.move_log.append((s_pos, d_pos, piece[0] + "castle"))
        else:
            self.boardstate[s_pos[1]][s_pos[0]] = ""
            self.boardstate[d_pos[1]][d_pos[0]] = piece
            if enpassant:
                lastmove = self.move_log[-1]
                self.boardstate[lastmove[1][1]][lastmove[1][0]] = ""
            self.move_log.append((s_pos, d_pos, piece))
        

    def betweenDiagonally(self, s_pos, d_pos):
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
        if d_pos[1] > s_pos[1]:
            step = 1
        else:
            step = -1
        for i in range(s_pos[1]+step, d_pos[1], step):
            if self.boardstate[i][s_pos[0]] != "":
                return True
        return False

    def betweenHorizontally(self, s_pos, d_pos):
        if d_pos[0] > s_pos[0]:
            step = 1
        else:
            step = -1
        for i in range(s_pos[0]+step, d_pos[0], step):
            if self.boardstate[s_pos[1]][i] != "":
                return True
        return False
