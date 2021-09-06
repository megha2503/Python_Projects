class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath,"r") as file:
            self.balance=int(file.read())
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# account = Account("balance.txt")
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.commit()
class Checking(Account):
    """This class should generate checking account objects"""
    #class variable: is declared outside the methods

    type="checking"

    def __init__(self, filepath,fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance- amount - self.fee

checking =Checking("balance.txt",1)
checking.transfer(100)
print(checking.balance)
checking.commit()


megha_checking =Checking("megha.txt",1)
megha_checking.transfer(100)
print(megha_checking.balance)
megha_checking.commit()

varsha_checking =Checking("varsha.txt",1)
varsha_checking.transfer(100)
print(varsha_checking.balance)
varsha_checking.commit()
print(varsha_checking.type)
