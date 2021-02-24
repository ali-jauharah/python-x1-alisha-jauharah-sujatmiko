print('hi :)')
print('ini aku lg ngomong sm siapa?')
name=input('nama: ')
print('hi', name,'! :)')
print('apa kabar? jawab BAIK atau GA BAIK')
kabar=input('jawab: ')
if kabar=='BAIK':
    print('gud :)')
    print('lg ngapain?')
    print('jawab NGGABUT atau NUGAS atau GTW JG')
    ngapa=input('jawab: ')
    if ngapa=='NGGABUT':
        print('ih emg susah bgt nyari kerjaan. apa ga mbaca lah kek, drakoran kek :v')
    elif ngapa=='NUGAS':
        print('lah trs ngapain yu di sini?? nugas lah sana hush')
    else:
        print('lah gmn si wkwk')
else:
    print('loh :( knp?')
    print('jawab LIFE IS SUSAH atau CM BAD MOOD')
    knp=(input('jawab: '))
    if knp=='LIFE IS SUSAH':
        print(':( mau curhat g? langsung wa aja')
        print('jawab MAU atau GA USAH')
        curhat=input('jawab: ')
        if curhat=='MAU':
            print('ok :) wa aja, ayuk')
        else:
            print('alright... moga2 bakal oke :) ganbatte', name, ':)')
    else:
        print('oo oke. moga2 bakal oke', name, ', ganbatte!!')
