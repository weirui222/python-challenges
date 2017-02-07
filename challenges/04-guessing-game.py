from random import randint

MIN = 1
MAX = 100

print("Guess a number between %d and %d" % (MIN, MAX))
#print("Delete me. Here's a random number:", randint(MIN, MAX))

def guess():
    number = randint(MIN, MAX)
    count = 0
    while True:
        guenum = int(input())
        count += 1
        if guenum > number:
            print(f'The number is lower than {guenum}.  Guess again')
        elif guenum < number:
            print(f'The number is higher than {guenum}.  Guess again')
        else:
            break
    print(f'You got it in {count} tries')

guess()
