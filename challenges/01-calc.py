# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calc():
    method = input("What calculation would you like to do? (add, sub, mult, div)")
    num1 = int(input("What is number 1? "))
    num2 = int(input("What is number 2? "))

    if method == 'add':
        print(f'Your result is {num1 + num2}')
    elif method == 'sub':
        print(f'Your result is {num1 - num2}')
    elif method == 'mult':
        print(f'Your result is {num1 * num2}')
    elif method == 'div':
        print(f'Your result is {num1 / num2}')
    else:
        print('Your result is None')

calc()
