import random
number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('Okay! ' + player_name + ' I am Guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is little bit low')
    if guess > number:
        print('Your guess is little bit high')
    if guess == number:
        break
if guess == number:
    print('You "Won",WELL DONE!,' + player_name)
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')

else:
    print('You lose! ,You did not guess the number, The number was ' + str(number))
if guess != number:
    print("New Game Starts!,"
          "PRESS RUN BUTTON ON THE TOP")
