from Account import Account

class Purchase:
    def __init__(self, coffee, cnt):
        self.__coffee = coffee
        self.__cnt = cnt

    def execute(self):
        account = Account.get_instance()
        if(account.regist_expenses(self.coffee.cost * self.cnt)):
            self.coffee.add_stock(self.cnt)
            return True
        
        return False

    @property
    def coffee(self):
        return self.__coffee

    @property
    def cnt(self):
        return self.__cnt


