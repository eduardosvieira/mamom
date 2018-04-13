from mamom.models.Transation import Transation

class Income(Transation):
    def __init__(self, id, name, createdAt, category, account, value):
        super(Income, id, name, createdAt, category, account, value)
