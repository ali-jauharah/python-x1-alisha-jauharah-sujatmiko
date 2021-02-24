num=int(input('input number: '))
if num>1:
    for i in range(2,num):
            if (num%i)==0:
                print(num, 'bukan bilangan prima')
                print(i, 'kali', num//i, 'adalah', num)
                break
    else:
        print(num,'adalah bilangan prima')
else:
    print(num,'bukan bilangan prima')

lower=int(input('lower: '))
upper=int(input('upper: '))
print('bilangan ganjil antara', lower, 'dan', upper, 'adalah')
for num in range(lower,upper+1):
    if num>1:
        for i in range (2,num):
            if (num%2)==0:
                break
        else:
            print(num)

x=[[12,7],
    [4,5],
    [3,8]]
hasil=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        hasil[j][i]=x[i][j]
for h in hasil:
    print(h)

lower=100
upper=2000
for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print(num)

num=int(input('num: '))
for i in range(1,11):
    print(num,'x',i,'=',num*i)

kata='drtd blm makan e laper'
jum=0
for letter in kata:
    if letter=='a':
        jum+=1
        #continue
    #print('huruf sekarang: ', letter)
print('jumlah:', jum)