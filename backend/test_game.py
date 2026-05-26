from game import Game

class TestGame:

    def test_legal_moves(self):
        self.x = Game()
        assert self.x.legal_moves() == ""

