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
            game.move("Ke9")       
        with pytest.raises(chess.InvalidMoveError):
            game.move("Zf3")       
        with pytest.raises(chess.InvalidMoveError):
            game.move("")         

        # Well-formed but illegal in the current position
        with pytest.raises(chess.IllegalMoveError):
            game.move("e5")      
        with pytest.raises(chess.IllegalMoveError):
            game.move("Nf6")    

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
        # Undo a single move restores the board
        game = Game()
        game.move("e4")
        game.undo_move()
        assert game.board.board_fen() == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

        # Undo restores turn to white
        game.move("e4")
        game.undo_move()
        assert game.board.turn == chess.WHITE

        # Undo multiple moves one at a time
        game.move("e4")
        game.move("e5")
        game.undo_move()
        assert game.board.board_fen() == "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"
        assert game.board.turn == chess.BLACK
        game.undo_move()
        assert game.board.board_fen() == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        assert game.board.turn == chess.WHITE

        # Undo a capture restores the captured piece
        game2 = Game("rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
        game2.move("Nf3")
        game2.move("Nc6")
        game2.move("Bb5")
        game2.move("a6")
        game2.move("Bxc6")   # bishop captures knight
        game2.undo_move()
        assert game2.board.board_fen() == "r1bqkbnr/1ppppppp/p1n5/1B6/4P3/5N2/PPPP1PPP/RNBQK2R"

        # Undo castling restores king and rook
        game3 = Game("r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1")
        game3.move("O-O")
        game3.undo_move()
        assert game3.board.board_fen() == "r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R"

        # Undo on an empty move stack raises an error
        game4 = Game()
        with pytest.raises(Exception):
            game4.undo_move()


    def test_legal_moves(self):
        # Returns a string
        game = Game()
        result = game.legal_moves()
        assert isinstance(result, str)

        # Starting position has exactly 20 legal moves
        moves = result.split()
        assert len(moves) == 20

        # Known opening moves are present
        assert "e4" in moves
        assert "d4" in moves
        assert "Nf3" in moves

        # Black moves are not listed on white's turn
        assert "e5" not in moves

        # Legal moves update after a move is made
        game.move("e4")
        moves_after = game.legal_moves().split()
        assert len(moves_after) == 20   # black also has 20 replies
        assert "e5" in moves_after
        assert "e4" not in moves_after  # white's move no longer listed

        # Checkmate position has no legal moves
        game2 = Game("rnb1kbnr/pppp1ppp/4p3/8/6Pq/5P2/PPPPP2P/RNBQKBNR w KQkq - 1 3")
        assert game2.legal_moves().split() == []

        # Only legal moves escape check
        game3 = Game("4k3/8/8/8/8/8/8/R3K2R b KQ - 0 1")
        game3.move("ke8d8") if "ke8d8" in game3.legal_moves() else None
        game4 = Game("3k4/R7/1R6/8/8/8/8/4K3 b - - 0 1")  # black king has 1 legal move
        legal = game4.legal_moves().split()
        assert len(legal) == 1

    
    def test_mate_in_one(self):
        # Returns a bool
        game = Game()
        assert isinstance(game.mate_in_one(), bool)
    
        # No mate-in-one from the starting position
        assert game.mate_in_one() is False
    
        # No mate-in-one after e4 (black's turn, no forced mate)
        game.move("e4")
        assert game.mate_in_one() is False
    
        # White has mate in one: Qh5# (Fool's mate setup, but white delivers it)
        game2 = Game("rnbqkbnr/ppppp2p/5p2/6pQ/4P3/8/PPPP1PPP/RNB1KBNR w KQkq - 0 3")
        assert game2.mate_in_one() is True
    
        # Black has mate in one: Qxg2# (Scholar's mate reverse)
        game3 = Game("rnb1kbnr/pppp1ppp/4p3/8/6Pq/5P2/PPPPP2P/RNBQKBNR b KQkq - 0 3")
        assert game3.mate_in_one() is True
    
        # One move away but no mate — just a check
        game4 = Game("4k3/8/8/8/8/8/8/4K2R w K - 0 1")
        assert game4.mate_in_one() is False   # Rh8+ is check, not mate
    
        # Actual back-rank mate in one
        game5 = Game("4k3/R7/8/8/8/8/8/R3K3 w Q - 0 1")
        assert game5.mate_in_one() is True    # Ra8#
    
    
    def test_check_castle(self):
        # Both rights available at the start
        game = Game()
        assert game.check_castle() == "yes"
    
        # Kingside only
        game2 = Game("r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w Kkq - 0 1")
        assert game2.check_castle() == "short allowed"
    
        # Queenside only
        game3 = Game("r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w Qkq - 0 1")
        assert game3.check_castle() == "long allowed"
    
        # No castling rights
        game4 = Game("r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w kq - 0 1")
        assert game4.check_castle() == "no"
    
        # Rights lost after king moves
        game5 = Game("r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1")
        game5.move("Ke2")
        game5.move("e5")
        assert game5.check_castle() == "no"
    
        # Kingside right lost after kingside rook moves
        game6 = Game("r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1")
        game6.move("Rh2")
        game6.move("e5")
        assert game6.check_castle() == "long allowed"
    
        # Queenside right lost after queenside rook moves
        game7 = Game("r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1")
        game7.move("Ra2")
        game7.move("e5")
        assert game7.check_castle() == "short allowed"
    
        # Reflects black's rights when it's black's turn
        game8 = Game("r3k2r/pppppppp/8/8/4P3/8/PPPP1PPP/R3K2R b KQkq - 0 1")
        assert game8.check_castle() == "yes"
        game8.move("O-O")
        game8.move("e5")  # white filler
        assert game8.check_castle() == "no"  # black already castled
    
    
    def test_get_total_moves(self):
        # Zero before any moves
        game = Game()
        assert game.get_total_moves() == 0
    
        # Still zero after only white moves
        game.move("e4")
        assert game.get_total_moves() == 0
    
        # One after both white and black have moved
        game.move("e5")
        assert game.get_total_moves() == 1
    
        # Increments once per full round
        game.move("Nf3")
        assert game.get_total_moves() == 1
        game.move("Nf6")
        assert game.get_total_moves() == 2
    
        game.move("Bb5")
        game.move("a6")
        assert game.get_total_moves() == 3
    
        # Undo one half-move (black's) drops count back
        game.undo_move()
        assert game.get_total_moves() == 2
    
        # Undo white's half-move — still 2 (white hasn't completed the round)
        game.undo_move()
        assert game.get_total_moves() == 2
    
        # Undo black's previous move — back to 1
        game.undo_move()
        assert game.get_total_moves() == 1
    
        # FEN with fullmove_number > 1 doesn't affect move_count tracking
        # (move_count tracks moves made *in this game instance*, not the FEN clock)
        game2 = Game("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2")
        assert game2.get_total_moves() == 0
        game2.move("d5")
        assert game2.get_total_moves() == 0
        game2.move("d4")
        assert game2.get_total_moves() == 1 
