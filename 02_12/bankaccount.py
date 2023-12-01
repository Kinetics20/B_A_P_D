class BankAccount:
    def __init__(self, number, cash=0.0):
        self.number = number
        self.cash = cash

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount
            print(f'deposit on account {amount} zl . Actual balance of account : {self.cash} zl')

        else:
            print('Entered amount should be higher than 0')

    def withdraw_cash(self, amount):
        if amount > 0:
            if amount <= self.cash:
                self.cash -= amount
                print(f'withdraw from account : {amount} zl , actual balance of account {self.cash} zl')
                return amount
            else:
                withdrawn_amount = self.cash
                self.cash = 0
                print(f'There are insufficient funds in your account , Withdrawn only {withdrawn_amount} zl')
                return withdrawn_amount
        else:
            print('value of amount should be higher that 0')
            return 0

    def print_info(self):
        print(f'info about the account account of number {self.number} : ')
        print(f'balance of account : {self.cash} zl')


account = BankAccount(112345)
account.print_info()

account.deposit_cash(10000)
account.deposit_cash(500)
account.deposit_cash(80)

account.print_info()
