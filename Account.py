#! usr/bin/python3

class Account:
			
	def __init__(self, balance):
			self.balance = balance
			
	def getBalance(self):
			return self.balance
			
	def deposit(self, amt):
			if	amt>0:
					self.balance += amt
					return 1
			else:
					return 0
	
	def withdraw(self, amt):
			if	amt>0 and amt<=self.balance:
					self.balance -= amt
					return 1
			else:
					return 0
					
	def transfer(self, amt, Account, recipient):
			if	self.withdraw(amt) == 1:
					Account.deposit(amt)
					print(amt, " Transfered to 	" , recipient.getFirstName())
					return Account
			else: 
					return null
					
