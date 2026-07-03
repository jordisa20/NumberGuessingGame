# Number Guessing Game
import random   

def random_guess(max_guesses):
    random_number = random.randint(1,100) # returns a random number between 1 and 100
    guesses_left = max_guesses # determines which difficulty is chosen
    
    while guesses_left > 0:  # loop runs as long as the user has guesses left
        guess = int(input("Enter your guess: "))  

        attempts = (max_guesses - guesses_left) + 1 # the amount of attempts made
        
        if guess == random_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts")
            return

        elif guess > random_number:
            print(f"Incorrect! The number is less than {guess}")

        else:
            print(f"Incorrect! The number is greater than {guess}")
    
        guesses_left -= 1   # removes 1 guess
        print(f"You have {guesses_left} guesses left.")

    print(f"You lost! The correct number was {random_number}.")

def choose_difficulty(): # choose difficulty

    
    while True:
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Great! You have selected the Easy difficulty level.")
            print("Let's start the game!")
            print("I'm thinking of a number between 1 and 100.")
            print("You have 10 chances to guess the correct number.")

            random_guess(10)

        elif choice == "2":
            print("Great! You have selected the Medium difficulty level.")
            print("Let's start the game!")
            print("I'm thinking of a number between 1 and 100.")
            print("You have 5 chances to guess the correct number.")

            random_guess(5)

        elif choice == "3":
            print("Great! You have selected the Hard difficulty level.")
            print("Let's start the game!")
            print("I'm thinking of a number between 1 and 100.")
            print("You have 3 chances to guess the correct number.")


            random_guess(3)

        elif choice == "4":
            print("Exiting Game...")
            break

        else:
            print("Invalid choice. Try again.")

def main(): # main game loop
    while True: # while loop for game menu
        print("\n=== Menu ===")
        print("1. Play")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Welcome to the Number Guessing Game!")
            choose_difficulty()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

main()