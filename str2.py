a1 = "bapako"
a2 = "D"
a3 = "Luffy"
aFinal = a1+' '+a2+"'"+a3
print(aFinal)
print(len(aFinal)) #panjang string
#check char di string sensitive terhadap huruf besar kecil
b = "b"
print(b in aFinal)# bisa pakai not in
#mengulang string
print(14*'haha')

#mengambil index huruf ke
print(aFinal[7])
print(aFinal[-1])#negatif mengammbil dari belakang
print(aFinal[7:15])
print(aFinal[0:15:2])#dari o - 14 kelipatan 2, 0,2,4

#index paling kecil
print(min(aFinal))
print(max(aFinal))

ascii_code = ord(" ") #orde ke dari suatu char
print(str(ascii_code))
print(chr(89))

bb = aFinal.capitalize()
print(bb)