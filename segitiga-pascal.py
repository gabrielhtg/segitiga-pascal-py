import os

os.system('clear||cls')

def faktorial(x) :
    hasil = 1
    for z in range(1, x + 1) :
        hasil = hasil * z
    return hasil
    
n = int(input("Masukkan banyak baris segitiga pascal : "))

for i in range(n) :
    for k in range(n-i-1) :
        print(" ", end="")
        
    for k in range(i + 1) :
        print(int(faktorial(i) / (faktorial(k) * faktorial(i - k))), end=" ")
    
    print()