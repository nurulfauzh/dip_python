from bank import Bank

class KartuDebit(Bank):
    
    def do_transaction(self,total :int):
        print(f"Transaksi Sejumlah {total} Mengunakan Debit")