class GameState:

    """
    This class is responsible for keeping track of the game/boardstate and making changes to it.
    """

    def __init__(self):
        self.boardstate = [["bR", "bN", "bB","bQ","bK","bB","bN","bR"],
        ["bP","bP","bP","bP","bP","bP","bP","bP"],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["wP","wP","wP","wP","wP","wP","wP","wP"],
        ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.moveWhite = True


    def changeBoardState(self, piece, s_pos, d_pos):
        if self.moveWhite:
            if piece[0] == "b":
                return
            self.boardstate[s_pos[1]][s_pos[0]] = ""
            self.boardstate[d_pos[1]][d_pos[0]] = piece
            self.moveWhite = False
        else:
            if piece[0] == "w":
                return
            self.boardstate[s_pos[1]][s_pos[0]] = ""
            self.boardstate[d_pos[1]][d_pos[0]] = piece
            self.moveWhite = True


    def betweenDiagonally(self, s_pos, d_pos):
        dif = abs(s_pos[0]-s_pos[1])
        if d_pos[0] > s_pos[0]:
            step = -1
            if d_pos[1] > s_pos[1]:
                for i in range(s_pos[0]+1, d_pos[0]):
                    if self.boardstate[i-dif][i] != "":
                        return True
            else:
                for i in range(s_pos[0]+1, d_pos[0]):
                    if self.boardstate[s_pos[1]+step][i] != "":
                        return True
                    step -= 1
        else:
            step = -1
            if d_pos[1] > s_pos[1]:
                for i in range(d_pos[0]+1, s_pos[0]):
                    if self.boardstate[d_pos[1]+step][i] != "":
                        return True
                    step -= 1
            else:
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






