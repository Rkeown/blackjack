import random

def dice_roll():
    roll = random.randrange(1,7,1)
    return roll



def game_master():
    player_score = 0
    dealer_score = 0
    num_of_rolls = 0
    roll = 0
    keep_playing = True
    player_input = "N"
    roll_dice = ""

    print("\nWelcome to Blackjack\n")
    for i in range(3):
        roll_dice = input("press any key to roll: ")
        roll = dice_roll()
        print("you rolled a ",roll)
        player_score += roll
        print("player's score: ",player_score,"\n")
        num_of_rolls += 1
        print("number of rolls: ", num_of_rolls)

    if num_of_rolls == 3:
        while player_score < 21:

            print("your score is ", player_score, "roll again y/N ")
            player_input = input()
            if player_input.upper() == 'Y':
                roll = dice_roll()
                player_score += roll
                num_of_rolls += 1
                if player_score > 21:
                    print("you lose")
                    break

                elif player_score == 21:
                    print("you win")
                    break

            elif player_input.upper() == 'N':
                for i in range(num_of_rolls):
                    roll = dice_roll()
                    dealer_score += roll
                    print("dealer rolled", roll, "\n")
                    print("dealer's score ", dealer_score)
                    print("\n")


                if dealer_score > 21:
                    print("player wins with a score of ", player_score, "because dealer broke\n dealer had a score of ", dealer_score)
                elif player_score > dealer_score:
                    print("player wins with a score of", player_score, "dealer had a score of", dealer_score)
                elif player_score < dealer_score:
                    print("dealer wins with a score of", dealer_score, "player had a score of" ,player_score)
                else:
                    print("dealer wins with a score of", dealer_score)
                break

game_master()

def play_again_handler():
    play_again = input("play again y/N? ")
    if play_again.upper() == 'Y':
        game_master()
    else:
        print("thanks for playing")
play_again_handler()


