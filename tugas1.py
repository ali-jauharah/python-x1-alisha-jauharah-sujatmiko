kilometers=float(input('input kilometers:'))
conv_fac=0.621317
miles=kilometers*conv_fac
print('%02f kilometers is equal to %02f'.format(kilometers, miles))

num1=float(input('num1:'))
num2=float(input('num2:'))
sum=num1+num2
print('penjumlahan {0} dan {1} adalah {2}'.format(num1,num2,sum))

x=int(input('x:'))
y=int(input('y:'))
temp=x
x=y
y=temp
print('nilai x sekarang : {}'.format(x))
print('nilai y sekarang : {}'.format(y))

import math
angka=int(input('input angka:'))
akar_angka=math.sqrt(angka)
print('akar dari',angka,'adalah',akar_angka)

tahun=int(input('masukkan tahun:'))
if (tahun%4) == 0:
    if (tahun%100)==0:
        if (tahun%400)==0:
            print('{0} adalah tahun kabisat'.format(tahun))
        else:
            print('{0} bukan tahun kabisat'.format(tahun))
    else:
        print('{0} adalah tahun kabisat'.format(tahun))
else:
    print('{0} bukan tahun kabisat'.format(tahun))

num1=int(input('num1:'))
num2=int(input('num2:'))
num3=int(input('num3:'))

if (num1>=num2) and (num1>=num3):
    terbesar=num1
elif (num2>=num1) and (num2>=num3):
    terbesar=num2
else:
    terbesar=num3
print('bilangan terbesar:',terbesar)

num=int(input('input nilai:'))
if (num%2)==0:
    print('{0} adalah genap'.format(num))
else:
    print('{0} adalah ganjil'.format(num))

def hitung_FPB(x, y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1, smaller+1):
        if ((x%i==0)and(y%i==0)):
            fpb=i
    return fpb
num1=int(input('num1:'))
num2=int(input('num2:'))
print('FPB dari',num1,'dan',num2,'=',hitung_FPB(num1, num2))

num=int(input('bilangan:'))
faktorial=1
if num<0:
    print('maaf, faktorial idak bisa untuk bilangan negatif')
elif num==0:
    print('faktorial dari 0 adalah 1')
else:
    for i in range(1, num+1):
        faktorial=faktorial*i
    print('faktorial dari',num,'adalah',faktorial)

c=int(input('suhu celsius: '))
r=c*0.8
f=(c*1.8)+32
print(c,'celsius sama dengan',f,'fahrenheit dan',r,'reamur')
