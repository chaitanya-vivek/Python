name = input("What is your name ? ")
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess the secret number: '))
    guess_count += 1
    if guess == secret_number:
        print("You win " + name + " !")
        break
else:
        print("Sorry, you failed " + name + " !")