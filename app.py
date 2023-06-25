import random
from colorama import Fore, Style
from time import sleep

class WordList:
    def get_word(self):
        words = ["marsala", "ciano", "amarelo", "violeta", "bordô", "coral", "fúcsia", "magenta", "marrom", "turquesa"]
        return random.choice(words)

class HangmanGame:
    def __init__(self):
        self.word_provider = WordList()
        self.max_attempts = 12
        self.current_word = ""
        self.guessed_letters = []
        self.attempts_left = 0

    def setup(self):
        self.current_word = self.word_provider.get_word()
        self.guessed_letters = []
        self.attempts_left = self.max_attempts

    def display_word(self):
        masked_word = "".join(
            [letter if letter in self.guessed_letters else "_" for letter in self.current_word]
        )
        print(Fore.MAGENTA + f"\nPalavra: {masked_word}")

    def display_attempts_left(self):
        print(f"Tentativas restantes: {self.attempts_left}")

    def display_guessed_letters(self):
        print(f"Chutes: {', '.join(self.guessed_letters)}")

    def evaluating_guess(self, guess):
        if guess in self.guessed_letters:
            sleep(1)
            print(Fore.YELLOW + "\nVocê já tentou essa letra!" + Style.RESET_ALL)
            return  

        if guess.isalpha():
          self.guessed_letters.append(guess)
          self.attempts_left -= 1
          
        else:
          sleep(1)
          print(Fore.YELLOW + "\nDigite apenas letras!" + Style.RESET_ALL)

    def restart_game(self):
        self.setup()
        self.play()

    def play(self):
        self.setup()
        print(Fore.CYAN + "Bem-vindo ao jogo da forca das cores!\n" + Style.RESET_ALL)
        sleep(1)

        while self.attempts_left > 0:
            self.display_word()
            self.display_attempts_left()
            self.display_guessed_letters()

            guess = input("Faça um chute: " + Style.RESET_ALL).lower()
            self.evaluating_guess(guess)

            if all(letter in self.guessed_letters for letter in self.current_word):
                sleep(1)
                print(Fore.GREEN + "\nParabéns! Você venceu!\n" + Style.RESET_ALL)
                return 


        sleep(1)  
        print(Fore.RED + f"FIM DE JOGO! A palavra era: {self.current_word}")
        play_again = input(Fore.BLUE + "\nVocê deseja jogar novamente? (s/n): " + Style.RESET_ALL).lower()
        if play_again == "s":
            self.restart_game()
        else:
            print(Fore.BLUE + "Obrigado por jogar!" + Style.RESET_ALL)
            return

if __name__ == "__main__":
    game = HangmanGame()
    game.play()