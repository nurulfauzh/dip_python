from bank import Bank

class KartuKredit(Bank):

    def do_transaction(self,total : int):
        print(F"Transaksi Sebesar {total} dengan mengunakan Kredit")