class Category():


    def __init__(self, balance):
        self.ledger = []
        self.balance = balance

    def deposit(self, amount, description=""):
        self.balance += amount
        self.log_history(amount, description)


    def withdraw(self, amount, description=""):

        available_funds = self.check_funds(self, amount)

        if available_funds:
            self.balance -= amount
            amount = amount * -1
            self.log_history(amount, description)
            return True
        else:
            return False
        

    def get_balance(self):
        return self.balance
    

    def transfer(self, amount, budget):

        available_funds = self.check_funds(amount)
        if available_funds:
            self.withdraw(amount, f"Transfer to {budget}")
            budget.deposit(budget, amount, f"Transfer from {self}")##?
            
        else:
            pass

        pass


    def check_funds(self, amount):

        if self.balance < amount:
            return False
        return True
        

    def log_history(self, amount, description):
        ledger_entry = dict()
        ledger_entry["amount"] = amount
        ledger_entry["description"] = description
        self.ledger.append(ledger_entry)
        

def create_spend_chart(categories):

    pass