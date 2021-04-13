import unittest
from gamestate import GameState

class TestGameState(unittest.TestCase):
    def setUp(self):
        self.startingBoard = [["bR", "bN", "bB","bQ","bK","bB","bN","bR"],
        ["bP","bP","bP","bP","bP","bP","bP","bP"],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["wP","wP","wP","wP","wP","wP","wP","wP"],
        ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.GS = GameState()
    
    def test_startingTurn(self):
        self.assertEqual(self.GS.moveWhite, True)

    def test_changeturn(self):
        self.GS.changeBoardState("wP", (6,6), (6,5))
        self.assertEqual(self.GS.moveWhite, False)
    
    def test_startBoard(self):
        self.assertEqual(self.GS.boardstate, self.startingBoard)