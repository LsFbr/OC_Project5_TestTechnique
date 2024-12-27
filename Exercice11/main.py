# Écrivez votre code ici !
class BankAccount:
    # Initialisation des attributs
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    # Méthode pour déposer de l'argent sur le compte
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            print("Le montant du dépôt doit être supérieur à 0 !")

    # Méthode pour retirer de l'argent du compte
    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Solde insuffisant !")

    # Méthode pour afficher le solde et le nom du propriétaire du compte
    def display_balance(self):
        print(f"Compte de {self.account_holder}\nSolde: {self.balance}")


# Test
account = BankAccount("David Douillet", 1000)
account.display_balance()
account.deposit(500)
account.display_balance()
account.withdraw(200)
account.display_balance()

