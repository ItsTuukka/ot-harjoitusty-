import unittest
from gamelogic.gamestate import GameState


class TestGameState(unittest.TestCase):
    def setUp(self):
        self.startingBoard = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                              ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                              ["", "", "", "", "", "", "", ""],
                              ["", "", "", "", "", "", "", ""],
                              ["", "", "", "", "", "", "", ""],
                              ["", "", "", "", "", "", "", ""],
                              ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                              ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.GS = GameState()

    def test_startingTurn(self):
        self.assertEqual(self.GS.moveWhite, True)

    def test_changeturn(self):
        self.GS.changeBoardState("wP", (6, 6), (6, 5), False, False)
        self.assertEqual(self.GS.moveWhite, False)

    def test_startBoard(self):
        self.assertEqual(self.GS.boardstate, self.startingBoard)

    def test_betweenHorizontally(self):
        self.assertEqual(self.GS.betweenHorizontally((0, 7), (2, 7)), True)
        self.assertEqual(self.GS.betweenHorizontally((0, 5), (2, 5)), False)

    def test_betweenVertically(self):
        self.assertEqual(self.GS.betweenVertically((0, 7), (0, 5)), True)
        self.assertEqual(self.GS.betweenVertically((0, 5), (0, 3)), False)

    def test_betweenDiagonally(self):
        self.assertEqual(self.GS.betweenDiagonally((0, 7), (2, 5)), True)
        self.assertEqual(self.GS.betweenDiagonally((0, 5), (2, 3)), False)

    def test_kingMovement(self):
        self.assertEqual(self.GS.wKmove, False)
        self.assertEqual(self.GS.bKmove, False)
        self.GS.changeBoardState("wP", (4, 6), (4, 4), False, False)
        self.GS.changeBoardState("bP", (4, 1), (4, 3), False, False)
        self.GS.changeBoardState("wK", (4, 7), (4, 6), False, False)
        self.GS.changeBoardState("bK", (4, 0), (4, 1), False, False)
        self.assertEqual(self.GS.wKmove, True)
        self.assertEqual(self.GS.bKmove, True)
