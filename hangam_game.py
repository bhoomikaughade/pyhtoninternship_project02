import random


words = ["python", "programming", "computer", "science", "algorithm", "database", "network", "software", "developer"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    guessed_letters = set()

    lives = 6

    
    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left.")
        print("Guessed letters:", ' '.join(guessed_letters))

        
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_list))

        guess = input("Guess a letter: ").lower()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives = lives - 1
                print("Letter is not in the word.")
        elif guess in guessed_letters:
            print("You have already guessed that letter. Try again!")
        else:
            print("Invalid character. Please try again.")

    
    if lives == 0:
        print("\nSorry, you died. The word was", word)
    else:
        print("\nCongratulations! You guessed the word", word, "!!")

if __name__ == "__main__":
    hangman()