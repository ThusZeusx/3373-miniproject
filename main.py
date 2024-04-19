
#Bank clss
class Bank:
    def __init__(self):
        self.account = {}

#account create function
    def Create_account(self,account_number,initial_deposit):
        if len(account_number) != 10:
            print("Account number must have 10 digits!!!")
            return
        if account_number  in self.account:
            print("This account number already have!!!")
            return
        elif initial_deposit < 0:
            print("Insuffint deposit balance!!")
            return
        else:
            self.account[account_number] = initial_deposit
            print(f"Account number {account_number} Created successfull!! and deposited {initial_deposit}")

#deposit function
    def Deposit(self,account_number,deposit_value):
        if account_number not in self.account:
            print("This account dosen't exists!!!")
        elif deposit_value < 0:
            print("Deposit amount can't be negative!!")
        else:
            self.account[account_number] += deposit_value
            print(f"Account number {account_number} credited in {deposit_value}. new balance is {self.account[account_number]}")

#withdraw funtion
    def Withdraw(self,account_number,withdraw_amount):
        if account_number not in self.account:
            print("This account dosen't exists!!!")
            return
        elif withdraw_amount > self.account[account_number]:
            print("Your requested withdraw amount is higher than your account balance!!")
            return
        elif withdraw_amount==0 or withdraw_amount<0:
            print("Withdraw amount cannot be zero or negative: ")
            return
        else:
            self.account[account_number] -= withdraw_amount
            print(f"Withdraw success from account number : {account_number}, New balance : {self.account[account_number]}")

#balance check function
    def Balance_check(self,account_number):
        if account_number not in self.account:
            print(f"Account number {account_number} not in database!!, check Again ")
            return
        else:
            print(f"Your account {account_number} balance is : {self.account[account_number]}")
            return

#money transfer function
    def Money_transfer(self,from_account,to_account,amount):
        if from_account not in self.account or to_account not in self.account:
            print(f"Account number  didn't exists!!!")
            return
        elif amount > self.account[from_account]:
            print(f"Amount is grater than account number : {from_account}")
        else:
            self.account[from_account] -= amount
            self.account[to_account] += amount
            print(f"Transfer Success!! Credited RS{amount} from account number {from_account} to account number {to_account}\n"
                  f"Account number {from_account} new balance = {self.account[from_account]}\n"
                  f"Account number {to_account} new balance = {self.account[to_account]}")


bank = Bank() #Bank object

#User interface/user input
while True:
    print("-------BANK CENTRAL-------")
    print("[1] - Create Accout")
    print("[2] - Deposit")
    print("[3] - Withdrawal")
    print("[4] - Balance Check")
    print("[5] - Transfer Money")
    choice = None
    try:
        choice = int(input("Enter your choice - \n"))
    except ValueError:
        print("You must enter integer values!!!")
    except KeyboardInterrupt:
        print("Programme terminated!!!")


    if choice == 1:
        try:
            account_number = input("Enter Account Number (account number must have 10 digits) : ")
            initial_deposit = float(input("Enter initial deposit value : "))
            bank.Create_account(account_number, initial_deposit)
        except:
            print("You must enter integer values!! not string values")

    elif choice == 2:
        try:
            account_number = input("Enter account number : ")
            deposit_amount = float(input("Enter deposit amount : "))
            bank.Deposit(account_number, deposit_amount)
        except:
            print("You must enter integer values!! not string values")

    elif choice == 3:
        try:
            account_number = input("Enter account number : ")
            withdraw_amount = float(input("Enter withdraw amount : "))
            bank.Withdraw(account_number, withdraw_amount)
        except:
            print("You must enter integer values!! not string values")

    elif choice==4:
        try:
            account_number = input("Enter account number : ")
            bank.Balance_check(account_number)
        except:
            print("You must enter integer values!! not string values")
    elif choice==5:
        try:
            from_account = input("Enter account number : ")
            to_account = input("To witch account :  ")
            amount = float(input("Enter amount you wish to transfer : "))
            bank.Money_transfer(from_account, to_account, amount)
        except:
            print("You must enter integer values!! not string values")
    else:
        print("Exiting!! Programme Exiting!!")
        break
