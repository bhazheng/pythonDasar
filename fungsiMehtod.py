def cetak( param1 ):
   print(param1)
   return
cetak(2)
cetak("bapako burik")


def kali(angka1, angka2):
   # Kalikan kedua parameter
   hasil = angka1 * angka2
   print('Dicetak dari dalam fungsi: {}'.format(hasil))
   return hasil


# Panggil fungsi kali
keluaran = kali(10, 20);
print('Dicetak sebagai kembalian: {}'.format(keluaran))


def kuadrat(x):
   return x * x


a = 10
k = kuadrat(a)
print('nilai kuadrat dari {} adalah {}'.format(a, k))


def ubah(list_saya):
   list_saya.append([1, 2, 3, 4])
   print('Nilai di dalam fungsi: {}'.format(list_saya))


# Panggil fungsi ubah
list_saya = [10, 20, 30]
ubah(list_saya)
print('Nilai di luar fungsi: {}'.format(list_saya))