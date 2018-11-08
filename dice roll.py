


import random

def dice_roll():
    while True:
        print("Your number is: " + str(random.randint(1,6)))
        play_again = input("Would you like to play again? ")
        while play_again != 'yes':
            if play_again == 'no':
                return print("Game Over")
            else:
                print("Input not recognized")
                play_again = input("Would you like to play again? ")

def main():
    game_start = input("Would you like to roll the dice?")
    if game_start == 'yes':
        dice_roll()
    else:
        print('too bad')

if __name__ == '__main__':
    main()
    
    
    
    