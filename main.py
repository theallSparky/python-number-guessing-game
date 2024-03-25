import random

upper_limit = input("What is the highest number you'd be willing to guess up to? Between 1 and what? ")

if upper_limit.isdigit():
    upper_limit=int(upper_limit)

    if upper_limit <= 0:
        print("Your number must be greater than 0!")
        quit()
else:
    print("Please type a valid number above 0 next time.")
    quit()

r = random.randint(1, upper_limit)

while True:
    user_guess = input("Guess the number!")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a valid number next time.")
        continue

    if user_guess == r:
        print("You are correct!")
        break
    else:
        print("Your guess is incorrect.")
    