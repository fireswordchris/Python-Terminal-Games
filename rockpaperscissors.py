import main as m
import random

def main():
    choices = ["rock", "paper", "scissors"]
    choice = random.choice(choices)
    
    player = input("Rock, paper, or scissors? (or quit) ").lower()
    
    
    
    if (choice == "rock" and player == "rock" or choice == "paper" and player == "paper" or choice == "scissors" and player == "scissors"):
        print("Computer chose " + choice)
        print("It's a tie!")
    elif (choice == "rock" and player == "scissors" or choice == "paper" and player == "rock" or choice == "scissors" and player == "paper"):
        print("Computer chose " + choice)
        print("Computer wins!")
    elif (choice == "rock" and player == "paper" or choice == "paper" and player == "scissors" or choice == "scissors" and player == "rock"):
        print("Computer chose " + choice)
        print("You win!")
    else:
        print("Not a valid choice please try again")
        main()
        
    again = input("Play again? ").lower()
    
    if (again == "yes" or again == "ye" or again == "y" or again == "yeah"):
        main()
    
    else:
        m.main()
    
if __name__ == "__main__":
    main()