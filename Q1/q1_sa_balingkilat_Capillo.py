class Account:
    def __init__(self, balance, accName, accNumber, accType):
        self.accName = accName
        self.accNumber = accNumber
        self.balance = balance
        self.accType = accType
        
    def deposit(self, deposit):
        self.balance += deposit
        deposit = input("Enter amount to deposit: ")
        print("You are about to deposit an amount of" ,deposit,)
        
    def withdraw(self, withdraw):
        self.balance -= withdraw
        withdraw = input("Enter amount to withdraw: ")
        print("You are about to deposit an amount of" ,withdraw,)
        
    def __str__(self):
        return f"{accName} [{accNumber}] P {balance}"
    
    
class SavingsAccount(Account):
    def __init__(self, addInterest, interestrate):
        self.addInterest = addInterest
        self.interestrate = interestrate
    
    def interest(self, interest, interestrate):
        self.interestrate = balance*0.02
        self.interest = balance += interestrate
        print("Adding interest to all accounts")
        
        
class Bank:
    def __init__(mbtc, openAccount, showAccounts, deposit, addInterest, closeAccount)
        mbtc = Bank("Metrobank")
        mbtc.openAccount()
        mbtc.openAccount()
        mbtc.showAccounts()
        mbtc.deposit()
        mbtc.deposit()
        mbtc.addInterest()
        mbtc.closeAccount()
        
print("Welcome to MetroBank")
print("Ready to open an account")
accName = input("Account name: ")
accNumber = input("Account number: ")
accType = input("Account type: ")
