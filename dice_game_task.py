import random
import time

class Player:

    def __init__(self, name: str):
        self.name = name

    def rolls_dice(self, counter=0):
        roll_again = "Yes"
        while roll_again == "Yes":
            counter += 1
            dice_one = random.randint(1, 6)
            dice_two = random.randint(1, 6)
            if dice_one == 6 and dice_two == 6:
                roll_again = "No"
            else:
                roll_again = "Yes"
        print(str(self.name) + " rolled double sixes in " + str(counter) + " rolls.")

class Game:

    def __init__(self, player_count: int):
        self.player_count = player_count

    def main_game(self):
        for i in range(0, self.player_count):
            self.new_player()

    def new_player(self):
        name = input("What is your name? ")
        new_player = Player(name)
        time.sleep(1)
        print("Welcome " + str(name) + ", please roll the dice.")
        time.sleep(1)
        new_player.rolls_dice()

if __name__ == "__main__":
    print("|Double Dice Game|")
    no_of_players = int(input("How many players? "))
    my_game = Game(no_of_players)
    my_game.main_game()
