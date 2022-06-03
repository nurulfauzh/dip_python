from transaksi import Transaksi
from kartudebit import KartuDebit
from kartukredit import KartuKredit


debit=KartuDebit()
kredit=KartuKredit()

trans1 = Transaksi(debit)
trans1.do_payment(3000000)

trans2 = Transaksi(kredit)
trans2.do_payment(2500000)