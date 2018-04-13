from mamom.models.Transation import Transation

class Expense(Transation):
    def __init__(self, id, name, createdAt, category, account, value):
        super(Expense, id, name, createdAt, category, account, value)
