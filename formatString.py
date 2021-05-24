# dijava sama denagan printf
nama = "babi"
n = 207.6
m = 5000
b = 5000000000
format_str = f"kamu {nama}"
print(format_str)
print(f"hehe = {n}")
#bilangkan bulat
print(f"hehe = {int(n):d}")
#ribuan
print(f"hehe = {m:,}")
print(f"hehe = {b:,}")
#desimal
print(f"hehe = {n:.2f}")
#minus
kamu = +20
print(f"safsf = {kamu:+d}")
#persen
coba2 = 0.04545
print(f"persen = {coba2:.2%}")
print(f"persen = {coba2:%}")
#aritmatika
print(f"hasil = {coba2*m}")

#binary octal hexadecimal
print(f"binari = {bin(m)}")
print(f"binari = {hex(m)}")
print(f"binari = {oct(m)}")