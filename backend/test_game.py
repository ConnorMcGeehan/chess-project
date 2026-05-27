import chess
import pytest
from game import Game


class TestGame:

    def test_move(self):
        game = Game()

        # Test initial state
        assert game.board.board_fen() == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

        # Test FEN initialization
        fen = "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"
        game6 = Game(fen)
        assert game6.board.fen() == fen

        # Test basic moves for each piece 
        # Pawns
        game.move("E4")
        game.move("e5")
        assert game.board.board_fen() == "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR"
        
        # Knights
        game.move("Nf3")
        game.move("nf6")
        assert game.board.board_fen() == "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R"

        # Bishops
        game.move("bb5")
        game.move("BB4")
        assert game.board.board_fen() == "rnbqk2r/pppp1ppp/5n2/1B2p3/1b2P3/5N2/PPPP1PPP/RNBQK2R"

        # Rooks
        game.move("rg1")
        game.move("RG8")
        assert game.board.board_fen() == "rnbqk1r1/pppp1ppp/5n2/1B2p3/1b2P3/5N2/PPPP1PPP/RNBQK1R1"

        # Queens
        game.move("QE2")
        game.move("qe7")
        assert game.board.board_fen() == "rnb1k1r1/ppppqppp/5n2/1B2p3/1b2P3/5N2/PPPPQPPP/RNB1K1R1"

        # Kings
        game.move("KD1")
        game.move("kd8")
        assert game.board.board_fen() == "rnbk2r1/ppppqppp/5n2/1B2p3/1b2P3/5N2/PPPPQPPP/RNBK2R1"

        # Test captures
        game.move("Bxd7")
        game.move("Qxb7")
        assert game.board.board_fen() == "rnbk2r1/pppq1ppp/5n2/4p3/1b2P3/5N2/PPPPQPPP/RNBK2R1"

        # Test castling
        # Kingside castling (white), queenside castling (black)
        game2 = Game("r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1")
        game2.move("O-O")
        assert game2.board.board_fen() == "r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R4RK1"
        game2.move("O-O-O")
        assert game2.board.board_fen() == "2kr3r/pppppppp/8/8/8/8/PPPPPPPP/R4RK1"

        # Test LAN (Long Algebraic Notation) 
        # Both white rooks can reach e1; specify which file the rook comes from
        game3 = Game("4k3/8/8/8/8/8/8/R3K2R w KQ - 0 1")
        game3.move("Ra1e1")
        assert game3.board.board_fen() == "4k3/8/8/8/8/8/8/4KR1R"
        game3.move("ke8d8")  
        assert game3.board.board_fen() == "3k4/8/8/8/8/8/8/4KR1R"

        # Test check
        game4 = Game("4k3/8/8/8/8/8/8/4K2R w K - 0 1")
        game4.move("Rh8+")
        assert game4.board.board_fen() == "4k2R/8/8/8/8/8/8/4K3"

        # Test checkmate
        game5 = Game("4k3/R7/8/8/8/8/8/R3K3 w Q - 0 1")
        game5.move("Ra8#")
        assert game5.board.board_fen() == "R3k3/R7/8/8/8/8/8/4K3"

        game = Game()
        with pytest.raises(chess.InvalidMoveError):
            game.move("Ke9")       # square doesn't exist
        with pytest.raises(chess.InvalidMoveError):
            game.move("Zf3")       # 'Z' is not a piece
        with pytest.raises(chess.InvalidMoveError):
            game.move("")          # empty string

        # Well-formed but illegal in the current position
        with pytest.raises(chess.IllegalMoveError):
            game.move("e5")        # pawn can't jump to e5 on the first move
        with pytest.raises(chess.IllegalMoveError):
            game.move("Nf6")       # it's white's turn, not black's

        # Moving into / through check
        game2 = Game("4k3/8/8/8/8/8/8/R3K2b w Q - 0 1")
        with pytest.raises(chess.IllegalMoveError):
            game2.move("O-O-O")    # can't castle through check (bishop covers d1)

        # Ambiguous move — two knights can both reach f3
        game3 = Game("4k3/8/8/8/8/8/8/1N1NK3 w - - 0 1")
        with pytest.raises(chess.AmbiguousMoveError):
            game3.move("Nd2")      # both knights can reach d2 

        # TODO: Add test only allowing the proper color to move (include 
        # illegal attempts in previous section)



    def test_undo_move(self):
        #TODO
        pytest.fail()

    def test_legal_moves(self):
        #TODO
        pytest.fail()

    def test_turn(self):
        #TODO
        pytest.fail()

    def test_mate_in_one(self):
        #TODO
        pytest.fail()

    def test_check_castle(self):
        #TODO
        pytest.fail()

    def test_get_total_moves(self):
        #TODO
        pytest.fail()

