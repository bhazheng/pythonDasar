for huruf in 'Dicoding':  # Contoh pertama
    print('Huruf: {}'.format(huruf))

flowers = ['mawar', 'melati', 'anggrek']
for flower in flowers:  # Contoh kedua
    print('Flower: {}'.format(flower))

flowers = ['mawar', 'melati', 'anggrek']
for index in range(len(flowers)):
    print('Flowers: {}'.format(flowers[index]))

count = 0
while (count < 7):
    print('Hitungannya adalah: {}'.format(count))
    count = count + 1

#infinite loop
#var = 1
#while var == 1:  # This constructs an infinite loop
#    num = input('Masukkan angka: ')
#    print('Anda memasukkan angka: {}'.format(num))

#while True:  # This constructs an infinite loop
#    num = input('Masukkan angka: ')
#    print('Anda memasukkan angka: {}'.format(num))

#while (var1): do_something()

for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()

#break
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            print()
            break
        else:
            print("*", end="")

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

for i in range (0,10):
    for j in range (0,10):
        if j>i:
            print()
            break
        else:
            print("*",end="")

#continue
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

jumlahbaris = 10
baris = 0
bintang = 0
while baris < jumlahbaris:
    if (bintang) >= (baris+1):
        print()
        baris = baris+1
        bintang=0
        continue      ##saat masuk ke if, maka bagian print * diluar if tidak akan dijalankan, langsung ulang ke while
    print("*",end="")
    bintang= bintang+1

#else setelah for
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, ' adalah bilangan prima')

#else setelah while
n = 10
while n > 0:
    n = n - 1
    print(n)
else:
    print("Loop selesai")

#pass
def sebuahfungsi(): #output bakal kosong
    pass
#def sebuahfungsi(): #outpu bakal error

import sys
data=''
while(data!='exit'):
    try:
        data=input('Please enter an integer (type exit to exit): ')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass  # exit gracefully without prompt any error
        else:
            print('error: {}'.format(sys.exc_info()[0]))

# Contoh3 menemukan item yang ada di kedua list
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = []
for a in list1:
    for b in list2:
        if a == b:
            duplikat.append(a)

print(duplikat)  # Output ['d','i']
#new_list = [expression for_loop_one_or_more conditions]
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = [a for a in list1 for b in list2 if a == b]
print(duplikat) # Output: ['d','i']

list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)