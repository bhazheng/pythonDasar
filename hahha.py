# compile python3 -m py_compile nama.py
from ctypes import c_double

x = "aku" #str
y = 5 #int
z = 1.9 #float
a = True #bool
c = complex(5,9) #data complex
c_xdouble = c_double(10.8) #data ctypes

print(x)
print("mamakmu",x) #kalo pake + ga langsung spasi
print(y)

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(c))
print(type(c_xdouble))

if y > 2:
    print("besar")
if y < 2:
    print("lebih kecil")
elif x == "aku":
    print("kamu bau")
else :
    print("tidak valid")

