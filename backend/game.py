import chess

class Game: 

    def __init__(self):
        self.board = chess.Board()
        self.move_count = 0
       
    def move(self, code):
        """
        param code: algebraic notation of the move to be executed
        post: board is updated to reflect the move that was made, and ascii 
              representation of the board is printed to command line
        """
        pass

    def undo_move(self):
        """
        post: board is updated to reflect the move that was taken back, ascii 
              representation of board is printed to command line
        """
        pass

    def legal_moves(self):
        """
        returns a string that lists the algebraic notation of the legal moves
                 the player can make
        """
        pass

    def turn(self):
        """
        return: returns either the string 'black' or 'white', dictating which
                players turn it is
        """
        pass

    def mate_in_one(self):
        """
        return: boolean, true if the current player has opportunity for mate-
                in-one, false otherwise
        """
        pass

    def check_castle(self):
        """
        return: string 'short allowed', 'long allowed', 'yes', 'no', telling the player if they
                have castling rights
        """
        pass

    def get_total_moves(self):
        """
        return: int, move count (a single move is when both white and black have moved)
        """
        pass




