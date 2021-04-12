class BoardState:

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
        




