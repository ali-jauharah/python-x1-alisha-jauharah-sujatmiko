#konversi bilangan desimal ke biner
def konversi(desimal):
    if desimal>1:
        konversi (desimal//2)
    print(desimal%2, end=' ')
desimal=int(input('input nilai desimal: '))
konversi(desimal)
print()

#mencari nilai faktorial dari suatu bilangan
def faktor(n):
    if n==1:
        return n
    else:
        return n*faktor(n-1)
bil=int(input('input bilangan: '))
if bil<0:
    print('faktorial hanya untuk bilangan positif')
elif bil==0:
    print('faktorial bilangan 0 adalah 1')
else:
    print('faktorial dari', bil, 'adalah', faktor(bil))

#mencari nilai penjumlahan dari nilai asli suatu bilangan
def penjumlah(n):
    if n<=1:
        return n
    else:
        return n+penjumlah(n-1)
bil=int(input('input bilangan:'))
if bil<0:
    print('masukkan bilangan positif')
else:
    print('penjumlahan dari nilai asli', bil, 'adalah', penjumlah(bil))

#menampilkan deret fibonacci
def deret_fibo(n):
    if n<=1:
        return n
    else:
        return (deret_fibo(n-1)+deret_fibo(n-2))
jumlah_deret=int(input('jumlah deret: '))
if jumlah_deret<=0:
    print('masukkan bilangan bulat positif')
else:
    print('deret fibonacci: ')
    for i in range(jumlah_deret):
        print(deret_fibo(i))

 #konversi biner ke desimal   
def konversi(n): 
    if n == 1 or n == 0:
        return n
    l = len(str(n))
    bin1 = n//pow(10,l-1)
    
    return (pow(2,l-1) * bin1)+ konversi(n%pow(10,l-1))

biner = int(input('input biner: '))
desimal = konversi(biner)

print('Desimal dari', biner, 'adalah', desimal)
