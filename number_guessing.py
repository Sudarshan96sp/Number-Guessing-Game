import random

def num_guessing():
    num_guess = 0
    computer_num = random.randint(1,5)

    while True:
        num_guess+=1
        player_guess = int(input("Guess Right Number : "))
    
        if (computer_num==player_guess):
            print(f"Matched!\nYou are Winner!\nYou have taken {num_guess} guesses.")
            break
        elif (player_guess>computer_num):
            print("Lower Number Please")
        elif (player_guess<computer_num):
            print("Higher Number Please")
        else:
            print("Something went wrong!")
        
while True:
    num_guessing()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break