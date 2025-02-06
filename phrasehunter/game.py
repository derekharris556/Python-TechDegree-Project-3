from phrasehunter.phrase import Phrase
import random
import sys

# Create your Game class logic in here.
class Game:
    # initialize game attributes
    def __init__(self):
        self.missed = 0
        self.phrases = self.phrases_list()
        self.active_phrase = None
        self.guesses = []

    # create welcome header
    def welcome(self):
        print(
            '|' + ('-*-*' * 8)
            + 'GUESS THE PHRASE'
            + ('*-*-' * 8) + '|'
        )

    # create a list of instances of phrases
    def phrases_list(self):
        phrases = [
            Phrase('Life is like a box of chocolates'),
            Phrase('May the force be with you'),
            Phrase('Talk to me Goose'),
            Phrase('Make my day punk'),
            Phrase('Say hello to my little friend')
        ]
        return phrases

    # select a random phrase from the phrases_list for game's active_phrase
    def get_random_phrase(self):
        return random.choice(self.phrases)

    def get_guess(self):
        # method will loop until users guess is 1 letter,
        # Checks is 1 letter, and is an alphabetic character
        while True:
            guess = input("Guess a letter: ").lower().strip()
            if guess == 'solve':
                return self.solve_puzzle()
            elif len(guess) == 1 and guess.isalpha():
                return guess
            print('Please enter a single letter.')

    # create method to check guess, if false count miss
    def check_guess(self, guess):
        if guess in self.active_phrase.phrase:
            print(f'"{guess}" is in the phrase.')
        else:
            self.missed += 1
            print(
                f'"{guess}" is not in the phrase.'
            )

    # create method for user to solve puzzle if they know the answer
    def solve_puzzle(self):
        print(
            '''If your guess is wrong, it's GAME OVER!'''
        )
        while True:
            solve_puzzle = input('What is your guess?: ')
            # remove spaces to verify
            if solve_puzzle.replace(' ', '').isalpha():
                if solve_puzzle.lower() == self.active_phrase.phrase:
                    print('YOU SOLVED THE PUZZLE!')
                    self.play_again()
                    return True
                elif solve_puzzle.lower() != self.active_phrase.phrase:
                    self.missed = 5
                    self.game_over()
                    return False
            else:
                print(
                    'Enter only letters and spaces.'
                    'MUST BE AN EXACT MATCH.'
                )
                return self.get_guess()

    # handles conditions that end game
    # returns False until 1 of 2 conditions = True
    def game_over(self):
        # if guesses reach 5, end game, display phrase
        if self.missed == 5:
            print('\nGAME OVER! YOU"RE OUT OF GUESSES!')
            print(f'The phrase was: "{self.active_phrase.phrase}"')
            self.play_again()
            return True
        elif self.active_phrase.check_complete(self.guesses):
            print('\nYOU GOT IT!!!')
            print(f'The phrase was: "{self.active_phrase.phrase}"')
            self.play_again()
            return True

        return False

    # handles logic
    def play_again(self):
        while True:
                play_again = input(
                    'Would you like to play again? y/n: '
                ).lower().strip()
                # if user wishes to play again, new instance of Game is created
                # new instance resets all attributes (guesses, misses and phrase)
                if play_again == 'y':
                    new_game = Game()
                    new_game.start()
                elif play_again == 'n':
                    sys.exit('Thanks For Playing!')
                else:
                    print('Invalid input.')

    def start(self):
        self.welcome()
        # set the phrase the player will guess
        self.active_phrase = self.get_random_phrase()
        # begin the actual game loop
        while True:
            print(f"\n# of Misses: {self.missed}")
            print("Guess this famous movie quote:")
            print(self.active_phrase.display_phrase(self.guesses))
            print()

            guess = self.get_guess()

            # Prevent duplicate guesses
            if guess in self.guesses:
                print("\nYou've already guessed that letter!")
                continue

            # Store the players guess
            self.guesses.append(guess)
            # Check if it's in the phrase
            self.check_guess(guess)

            # Check if the game has ended
            if self.game_over():
                return

