import random
def main():
    print("Welcome to the Number Guessing Game!")
    print("I`m thinking of a number between 1 and 100")

    while True:
        try:
            choice = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
            if choice == 'easy':
                easy_mode()
                break
            elif choice == 'hard':
                hard_mode()
                break
        except ValueError:
            pass


#hard 5 attempts
#easy 10 attepmpts

def easy_mode():
    random_number = random.randint(0,100)
    attempts = 9
    while True:
        try:
            guess_number = int(input("Make a guess: "))
            if guess_number == random_number:
                print("You won, the number was: ",random_number)
                break
            elif guess_number < random_number and attempts !=0:
                print("Too low")
                print("You have ", attempts, "remaining to guess a number")
                attempts = attempts - 1
                continue
            elif guess_number > random_number and attempts !=0:
                print("Too high")
                print("You have ", attempts, "remaining to guess a number")
                attempts = attempts - 1
                continue
            elif attempts == 0:
                print("You have lost")
                break
            else:
                print("You have ",attempts, "remaining to guess a number")
                attempts = attempts-1
                continue
        except ValueError:
            print("Please enter only integer numbers in range 0-100")
            pass


def hard_mode():
    random_number = random.randint(0,100)
    attempts = 4
    while True:
        try:
            guess_number = int(input("Make a guess: "))
            if guess_number == random_number:
                print("You won, the number was: ",random_number)
                break
            elif guess_number < random_number and attempts !=0:
                print("Too low")
                print("You have ", attempts, "remaining to guess a number")
                attempts = attempts - 1
                continue
            elif guess_number > random_number and attempts !=0:
                print("Too high")
                print("You have ", attempts, "remaining to guess a number")
                attempts = attempts - 1
                continue
            elif attempts == 0:
                print("You have lost")
                break
        except ValueError:
            print("Please enter only integer numbers in range 0-100")
            pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

