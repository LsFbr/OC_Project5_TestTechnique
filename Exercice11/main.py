# Écrivez votre code ici !
class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Solde insuffisant !")

    def display_balance(self):
        print(f"Compte de {self.account_holder}\nSolde: {self.balance}")


# test
account = BankAccount("David Douillet", 1000)
account.display_balance()
account.deposit(500)
account.display_balance()
account.withdraw(200)
account.display_balance()
