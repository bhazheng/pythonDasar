x = 100
print('Nilai x adalah', x)

print('hai {}'.format('bro'))

nama = "Dicoding"
print("Halo, %s!" % nama)

nama = "Dicoding"
umur = 5
print("Umur %s adalah %d tahun." % (nama, umur))

angka = [7, 9, 11, 13]
print("Angka saya: %s" % angka)

a, b = 10, 11
a, b
print('a: %x and b: %X' % (a, b))

print(eval('90+10'))

import sys
print('Jumlah arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
print(sys.argv[1])

#menghapus ruang kosong pada kanan atau kiri kata
print('Dicoding    '.rstrip()) #kanan
print('    Dicoding'.lstrip()) #kiri
print('    Dicoding    '.strip()) #Metode strip() akan menghapus whitespace pada bagian awal atau akhir string
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip('Code')) #output Dicoding

print('Dicoding Indonesia'.startswith('Dicoding')) #awalan dicoding true
print('Dicoding Indonesia'.endswith('Indonesia')) #akhiran indonesia true

#menggabung string
print(' '.join(['Dicoding', 'Indonesia', '!']))
print('123'.join(['Dicoding', 'Indonesia', '!']))

#memisahkan string
print('Dicoding Indonesia !'.split())
print('Dicoding123Indonesia123!'.split('123')) #pisahkan dengan parameter 123
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n')) #memisahkan setiap baris

#replace
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(string.replace("Coding", "Pemrograman", 1)) #hanya coding diawal yang dirubah

#check string
katax = "DICODING"
katax.isupper()
katax.islower()
print('Dicoding'.upper().lower())
print('Dicoding'.lower().upper())
print('DICODING'.upper().lower().islower())
print('DICODING'.upper().lower().isupper())
'dicoding'.isalpha()
'dicoding123'.isnumeric() #angka huruf
'12345'.isdecimal() #hanya angka
'    '.isspace() #hanya whitespace (tab spasi)
'Dicoding Indonesia'.istitle() #jika awal setiap kata huruf besar

# Contoh 1: Penggunaan zfill 5 pada angka satuan
angka = 5
print (str(angka).zfill(5));
# Contoh 2: Penggunaan zfill 5 pada angka ratusan
angka = 300
print (str(angka).zfill(5));
# Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
angka = -0.45
print (str(angka).zfill(5));
# Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
angka = -0.45
print (str(angka).zfill(7));

# Contoh 1
kata = 'aku'
print (kata.zfill(5));
# Contoh 2
kata = 'kamu'
print (kata.zfill(5));
# Contoh 3
kata = 'dirinya'
print (kata.zfill(5));