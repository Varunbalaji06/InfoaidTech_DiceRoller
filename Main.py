# Dice-Rolling App using python
import random

def roll_dice(num):
    results = [random.randint(1, 6) for _ in range(num)]
    return results

def main():
    print("Welcome to Dice Rolling App!!")

    while True:
        try:
            num = int(input("Enter the number of dice you want to roll: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if num<0:
            print("Please enter a positive number greater than 0.")
            continue
        
        dice_result = roll_dice(num)

        print(f"Result of rolling {num} dice: {dice_result}")

        play_again = input("Do you want to roll again? (yes/no): ").lower()

        if play_again != 'yes':
            print("Thank you for using the dice rolling app. GoodBye! ")
            break

if __name__ == "__main__":
    main()

