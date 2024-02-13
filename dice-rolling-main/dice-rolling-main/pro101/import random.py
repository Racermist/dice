import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        print("Rolling the dice:", roll_dice())
        choice = input("Do you want to roll again? (y/n): ").lower()
        
        if choice == 'n':
            print("Thanks for rolling!")
            break
        elif choice != 'y':
            print("Invalid input. Please enter 'y' to continue or 'n' to end.")

if __name__ == "__main__":
    main()

