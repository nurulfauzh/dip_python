from bank import Bank

class Transaksi:
    def __init__(self, transaksi : Bank):
        self.__transaksi = transaksi
        
    def do_payment(self,total: int):
        self.__transaksi.do_transaction(total)