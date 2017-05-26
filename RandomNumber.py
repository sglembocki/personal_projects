import random

secret_number = random.randint(0, 100)
guess = -1
count = 0

while secret_number != guess:
    guess = input('enter a number from 0 - 100: ')
    if guess > 100 or guess < 0:
        print 'error: number is out of range'
    elif guess < secret_number:
        print 'your guess is low'
        count += 1
    elif guess > secret_number:
        print 'your guess is high'
        count += 1
    if count == 10:
        print 'you ran out of tries'
        break
else:
    print 'your guess is correct!'