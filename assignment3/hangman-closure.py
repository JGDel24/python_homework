def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        display = ''
        for char in secret_word:
            if char in guesses:
                display += char
            else: display += '_'

        print(display)

        return all(char in guesses for char in secret_word)
    return hangman_closure

if __name__ == '_main_':
    secret = input("Enter the secret word: ")
    guess_letter = make_hangman(secret)

    print("\nLet's play Hangman!")
    
    while True:
        guess = input("Guess a letter: ")
        if not guess:
            print("Please enter a letter.")
            continue
        if guess_letter(guess): 
            print(f"\nYou guessed the word: {secret}!")
            break
