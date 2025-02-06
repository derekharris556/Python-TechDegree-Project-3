# Create your Phrase class logic here.
class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def check_letter(self, guess):
        # check if letter is in phrase
        return guess in self.phrase

    def check_complete(self, guesses):
        # check if phrase has been completed
        for letter in self.phrase:
            if letter != ' ' and letter not in guesses:
                return False
        return True

    def display_phrase(self, guesses):
        displayed_phrase = ''
        for letter in self.phrase:
            if letter in guesses or letter == " ":
                displayed_phrase += letter
            else:
                displayed_phrase += "_ "
        return displayed_phrase