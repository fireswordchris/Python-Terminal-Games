import numbergame
import tictactoe
import rockpaperscissors

def main():
    game = input("What game do you want to play? (number, tictactoe, rps, or quit) ").lower()
    
    if (game == "number"):
        numbergame.main()
        
    elif (game == "tictactoe"):
        tictactoe.main()
        
    elif (game == "rps"):
        rockpaperscissors.main()
        
    elif (game == "quit"):
        quit()
        
    else:
        print("Not a valid choice please try again")
        main()
        
if __name__ == "__main__":
    main()