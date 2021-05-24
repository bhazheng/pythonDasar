#operator methobro = 
bro = "bro!"
print(bro.upper())
#check apakah lower
c = bro.islower()
print(c)
#isalpha() apakah semua huruf
print(bro.isalpha())
#isalnum() ada huruf dan angka
#isdecimal ada angka saja
#isspace() isinya ada spasi,tab,newline \n
#istitle() dimulai dengan huruf besar

#startswich / endswitch case sensitive
asu = "bapako tolol".startswith("bapako")
print(asu)

#join() split()
bb = ['kamu','kita','dia']
gabung = ','.join(bb)
print(gabung)

aa = "asucokkamucokanjing"
print(aa.split('cok'))

#left right center justify
aa = "asucokkamucokanjing".ljust(50)
print("'"+aa+"'")
aa = "asucokkamucokanjing".center(25,"=")
print("'"+aa+"'")
#menghilangkan
aa = "asucokkamucokanjing".strip("=")
print("'"+aa+"'")