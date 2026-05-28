import chess

class Game: 

    def __init__(self, board_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.board = chess.Board(board_fen)
        self.move_count = 0
       
    def move(self, san)->None:
        """
        param san: standard algebraic notation of the move to be executed
        post: board is updated to reflect the move that was made, and ascii 
              representation of the board is printed to command line
        """
        move = self.board.parse_san(san)
        if move in self.board.legal_moves:
            self.board.push(move)
        else:
            raise chess.IllegalMoveError(san)

    def undo_move(self)->None:
        """
        post: board is updated to reflect the move that was taken back, ascii 
              representation of board is printed to command line
        """
        pass

    def legal_moves(self)->str: 
        """
        returns a string that lists the algebraic notation of the legal moves
                 the player can make
        """
        pass

    def mate_in_one(self)->bool:
        """
        return: boolean, true if the current player has opportunity for mate-
                in-one, false otherwise
        """
        pass

    def check_castle(self)->str:
        """
        return: string 'short allowed', 'long allowed', 'yes', 'no', telling the player if they
                have castling rights
        """
        pass

    def get_total_moves(self)->int:
        """
        return: int, move count (a single move is when both white and black have moved)
        """
        pass




