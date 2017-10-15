#! usr/bin/python3

from Account import Account	

class Customer(object):

	def __init__(self, firstName, lastName, account):
			self.firstName = firstName
			self.lastName = lastName
			self.Account = account
			
	def getFirstName(self):
			return self.firstName
			
	def getLastName(self):
			return self.lastName
			
	def getAccount(self):
			return self.Account
			
	def setAccount(self, account):
			self.Account = account
			
	def printData(self):
			print("Firstname ", self.firstName)
			print("Balance : ", self.Account.getBalance())
