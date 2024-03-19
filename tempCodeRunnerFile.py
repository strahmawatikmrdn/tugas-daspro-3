a = int(input("masukkan angka:"))

x = bin(a)[2:].zfill(8)
y = oct(a)[2:].zfill(8)
z = hex(a)[2:].zfill(8)

print("bilangan desimal: ",a)
print("bilangan biner: ",x)
print("bilangan octal: ",y)
print("bilangan hexa desimal: ",z) 