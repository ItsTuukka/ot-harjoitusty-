import unittest
from initialize_db import initialize
from repositories.match_history_repository import MatchHistoryRepository

class TestDatabase(unittest.TestCase):
    def setUp(self):
        initialize()
        self.match_history = MatchHistoryRepository()
    
    def add_scores(self):
        self.match_history.add_score('test1', 'test2', 1)
        self.match_history.add_score('test3', 'test4', 2)
        self.match_history.add_score('test5', 'test6', 3)
        self.match_history.add_score('test7', 'test8', 2)
    
    def test_add_score(self):
        self.add_scores()
        matches = self.match_history.find_all()
        self.assertEqual(len(matches), 4)

    def test_find_all(self):
        self.add_scores()
        matches = self.match_history.find_all()
        self.assertEqual(matches[0][1], 'test2')
        self.assertEqual(matches[2][2], 3)
        self.assertEqual(matches[1][0], 'test3')
        self.assertEqual(matches[3][2], 2)


