#! usr/bin/python3

from Customer import Customer
from Account import Account

class Bank:
			customer = []
			numberOfCustomer = 0
			bankName = ""
			
			def __init__(self, bankName):
					self.bankName = bankName
					
			def addCustomer(self, firstname, lastname):
					self.customer.append(Customer(firstname, lastname, Account(0)))
					self.numberOfCustomer+=1;
					
			def getNumberOfCustomer(self):
					return self.numberOfCustomer
					
			def getCustomer(self, index):
					return self.customer[index]
