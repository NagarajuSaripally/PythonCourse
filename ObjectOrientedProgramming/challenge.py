"""
For this challenge, create a bank account class that has two attributes:

owner
balance

and two methods:

deposit
withdraw

As an added requirement, withdrawals may not exceed the available balance.
"""


class Account():
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

	def deposit(self, amount):
		self.balance += amount
		print(f'Hello Mr/Mrs {self.owner}, your Deposit Accepted')

	def withdraw(self, amount):
		if (self.balance > amount):
			self.balance -= amount
			print(f'Hello Mr/Mrs {self.owner}, your Withdrawal Accepted')
		else:
			print('Funds Unavailable!')

acct1 = Account('Jose',100)

print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)

acct1.withdraw(75)

acct1.withdraw(500)