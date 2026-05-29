import chess
from game import Game

def main():
    print("Chess CLI\n\n")

    # Initial setup
    setup = input("Press Enter to start a new game, or enter a FEN string start in the middle of a game: ")

    done = False
    while not done:
        try:
            if setup=="":
                game = Game()
            else:
                game = Game(setup)
            print(game.board)
            print()
            done = True
        except Exception:
            print("Invalid FEN string") 
            setup = input("Press Enter to start a new game, or enter a FEN string start in the middle of a game: ")
            
    # Menu of options: Make a move, undo a move, see legal moves, check for 
    # mate-in-one, check castling rights, quit game, print board
    choice = input("m: Make a move\tu: Undo a move\tl: Legal moves\t1: Turn color\tq: Quit game\n1: Check for mate-in-one\tc: Check castling rights\n")
    
    game_over = False
    while not game_over:
        if choice == "m":
            game_over = make_move(game)
        elif choice == "q":
            game_over = True
        choice = input("m: Make a move\tu: Undo a move\tl: Legal moves\t1: Turn color\tq: Quit game\n1: Check for mate-in-one\tc: Check castling rights\n")



    # Make a move - display move count, call move(), and print ASCII board
def make_move(game)->bool:
    san = input("Enter Algebraic Notation of move to make, or b to go back")
    if san == "b":
        return False
    else:
        done = False
        while not done:
            try:
                game.move(san)
                done = True
            except chess.InvalidMoveError:
                print("Invalid move")
                san = input("Enter Algebraic Notation of move to make, or b to go back")
            except ValueError:
                print("Invalid SAN")
                san = input("Enter Algebraic Notation of move to make, or b to go back")

    if game.board.is_checkmate():
        print("Checkmate!")
        return True
    elif game.board.is_stalemate():
        print("Stalemate")
        return True
    else: 
        return False


    # Undo a move - display a move count, call undo_move(), print board


    # See legal moves - call get_legal_moves(), print the list


    # Check for mate-in-one - call mate_in_one(), print true or false and board


    # Check castling - print where the rights remain





main()

