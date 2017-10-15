#! usr/bin/python3
from Bank import Bank

def main():
    StartMenu()

def StartMenu():
    print("1) Input Bank Name ")
    print("2) Exit")
    option = int(input("Enter choice 1/2 : "))
    if  option==1:
        InitBank()
    else:
        exit()

def InitBank():
    bankname = input("Enter BANK NAME: ")
    theBank = Bank(bankname)
    MainMenu(theBank)

def MainMenu(bank):
            print("1) Add Customer")
            print("2) View Customer")
            print("3)Manage Customer")
            options = int(input("Enter choice 1/2/3 : "))
            if options == 1:
                addCustomer(bank)
            elif options == 2:
                viewCustomer(bank)
            elif options == 3:
                ManageCustomer(bank)
            else:
                print("error ")
                MainMenu(bank)
def ManageCustomer(bank):
    index = int(input("Enter which customer index "))
    ManageCustomerMenu(bank, index)

def ManageCustomerMenu(bank, index):
    print("1) See Balance")
    print("2) Withdraw")
    print("3) Deposit")
    print("4)Log Out")
    print("5)Exit")
    optionss = int(input("Enter Choice 1/2/3"))
    if optionss == 1:
        print(bank.getCustomer(index).getAccount().getBalance())
        ManageCustomerMenu(bank, index)
    elif optionss == 2:
        withdrawMenu(bank,index)
    elif optionss == 3:
        depositMenu(bank,index)
    elif optionss == "4":
        ManageCustomer(bank)
    else:
        exit()
def withdrawMenu(bank, index):
    amt = float(input("How much would you  like to withdraw? \n"))
    if (bank.getCustomer(index).getAccount().withdraw(amt)==1):
        print("Withdraw Success")
    else :
        print("Withdraw FAILED, Balance not enough")
    MainMenu(bank)

def depositMenu(bank, index):
    amt = float(input("How much would you like to deposit? \n"))
    if  (bank.getCustomer(index).getAccount().deposit(amt)==1):
        print("Deposit Success")
    else:
        print("Deposit FAILED, ERROR CODE: NEGATIVE INPUT")
    MainMenu(bank)

def addCustomer(bank):
    firstNamer = input("Please enter your first name:")
    lastNamer = input("Please enter your last name:")
    bank.addCustomer(firstNamer,lastNamer)
    MainMenu(bank)

def viewCustomer(bank):
    if bank.getNumberOfCustomer() >= 1:
        index = 0
        while   (index<bank.getNumberOfCustomer()):
            print(index, ' ', bank.getCustomer(index).getFirstName(),' ', bank.getCustomer(index).getLastName()), ' ', bank.getCustomer(index).getAccount().getBalance()
            index+=1
    else:
            print("No customer")
    MainMenu(bank)






main()
