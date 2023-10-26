import random
import main as m

def main():
    num = random.randint(1,10)
    i = 0

    while i < 3:
        guess = input("Guess a number: ").lower()

        if (guess.isdigit()):
            if (int(guess) > num):
                print("Too high")

            elif (int(guess) < num):
                print("Too low")

            else:
                print("You won!")
                break

            i += 1
        
        else:
            print("Not a valid number")

    print("The number was " + str(num) + "!")
    
    again = input("Play again? ").lower()

    if (again == "yes" or again == "y" or again == "ye" or again == "yeah"):
        main()

    else:
        m.main()


if __name__ == "__main__":
    main()