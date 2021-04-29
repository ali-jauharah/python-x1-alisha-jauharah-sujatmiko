def ceknilai(nilai):
    if nilai%2==0:
        nilai+=2
    else:
        nilai*=2
    return nilai
angka=input('masukkan nilai = ')
hasil = ceknilai(int(angka))
print('hasilnya adalah {}'.format(hasil))

def segitiga(a, t):
    luas = (a*t)/2
    return luas
print('mencari luas segitiga')
a = int(input('alas = '))
t = int(input('alas = '))
print('luas : ', segitiga(a,t))

def hitung_FPB(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1, smaller+1):
        if((x%i==0)and(y%i==0)):
            fpb=i
    return fpb
num1=106
num2=24
print('FPB dari', num1, 'dan', num2, '=', hitung_FPB(num1, num2))

def print_faktor(x):
    """Fungsi menerima input bilangan dan mencetak faktornya"""
    print('faktor dari', x, 'adalah : ')
    for i in range(1, x+1):
        if x%i==0:
            print(i)
num=int(input('Masukkan bilangan : '))
print_faktor(num)

def penjumlahan(*vartuple):
    print('rata-ratanya adalah : ')
    rerata=0
    tot=0
    for var in vartuple:
        tot = tot + var
    rerata=tot/len(vartuple)
    print(rerata)
penjumlahan(10, 30, 50, 70)
rata(10,30,50,70)