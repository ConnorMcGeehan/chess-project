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
        self.board.pop()

    def get_legal_moves(self)->str: 
        """
        return: string that lists the algebraic notation of the legal moves
                 the player can make
        """
        legal = self.board.legal_moves
        possible_moves = ""

        for move in legal:
            san = self.board.san(move)
            possible_moves += san + " "

        return possible_moves[0:-1]

    def mate_in_one(self)->bool:
        """
        return: boolean, true if the current player has opportunity for mate-
                in-one, false otherwise
        """
        moves = self.get_legal_moves()
        if "#" in moves:
            return True
        else:
            return False

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




