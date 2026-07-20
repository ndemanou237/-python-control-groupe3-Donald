class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Dépôt de {amount} effectué pour {self.owner}. Nouveau solde : {self._balance}")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Retrait de {amount} effectué pour {self.owner}. Nouveau solde : {self._balance}")
            else:
                print(f"Échec du retrait pour {self.owner} : Solde insuffisant ({self._balance}).")
        else:
            print("Le montant du retrait doit être positif.")

    def get_balance(self):
        return self._balance


class SavingsAccount(Account):
    def __init__(self, owner, balance=0.0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Intérêts de {interest} appliqués pour {self.owner}. Nouveau solde : {self._balance}")


if __name__ == "__main__":
    print("Test du compte bancaire classique")
    compte_courant = Account("Alice", 500.0)
    compte_courant.deposit(200.0)
    compte_courant.withdraw(100.0)
    compte_courant.withdraw(800.0)  
    print(f"Solde final de Alice : {compte_courant.get_balance()}\n")

    print("Test du compte épargne")
    compte_epargne = SavingsAccount("Bob", 1000.0, 0.03)
    compte_epargne.deposit(500.0)
    compte_epargne.apply_interest()
    compte_epargne.withdraw(200.0)
    print(f"Solde final de Bob : {compte_epargne.get_balance()}")