print("Welcome to Chase bank.")
print("Have a nice day!")

class BankAccount():
  def __init__(self):
    self.balance = 0

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

def bank():
    account = BankAccount()
    print('Your current balance is '+ str(account.balance))
    while True:
        kind = input("What would you like to do? (deposit, withdraw, check_balance)\n")
        if kind == 'deposit':
            wages = int(input('How much would you like to deposit?\n'))
            account.deposit(wages)
            print('Your current balance is '+ str(account.balance))
        elif kind == 'withdraw':
            wages = int(input('How much would you like to withdraw?\n'))
            account.withdraw(wages)
            print('Your current balance is '+ str(account.balance))
        elif kind == 'check_balance':
            print('Your current balance is '+ str(account.balance))

        done = input("Are you done?\n")
        if done == 'yes':
            print('Thank you!')
            break

bank()
