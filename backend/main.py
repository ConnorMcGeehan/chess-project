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
    
    game_over = False
    while not game_over:
        choice = input("m: Make a move\tu: Undo a move\tl: Legal moves\tt: Turn color\tq: Quit game\n1: Check for mate-in-one\tc: Check castling rights\n")
        if choice == "m":
            game_over = make_move(game)
        elif choice == "u":
            undo_last_move(game)
        elif choice == "l":
            see_legal_moves(game)
        elif choice == "1":
            see_mi1(game)
        elif choice == "c":
            check_castle_rights(game)
        elif choice == "t":
            if game.board.turn:
                print("White")
            else:
                print("Black")
        elif choice == "q":
            game_over = True




    # Make a move - display move count, call move(), and print ASCII board
def make_move(game)->bool:
    san = input("Enter Algebraic Notation of move to make, or b to go back: ")
    if san == "b":
        return False
    else:
        done = False
        while not done:
            try:
                game.move(san)
                done = True
            except ValueError:
                print("Invalid move, please enter move using SAN.")
                san = input("Enter Algebraic Notation of move to make, or b to go back: ")
                if san == "b":
                    return False

    if game.board.is_checkmate():
        print("Checkmate!")
        return True
    elif game.board.is_stalemate():
        print("Stalemate")
        return True
    else: 
        return False


    # Undo a move - display a move count, call undo_move(), print board
def undo_last_move(game)->None:
    try:
        game.undo_move()
    except IndexError:
        print("There are no moves to undo.")


    # See legal moves - call get_legal_moves(), print the list
def see_legal_moves(game)->None:
    moves = game.get_legal_moves()
    print(moves)


    # Check for mate-in-one - call mate_in_one(), print true or false and board
def see_mi1(game)->None:
    possible = game.mate_in_one()
    if possible:
        print("There is mate-in-one.")
        print(game.board)
    else:
        print("There is not mate-in-one.")
        print(game.board)
        


    # Check castling - print where the rights remain
def check_castle_rights(game)->None:
    print(game.check_castle())





main()

