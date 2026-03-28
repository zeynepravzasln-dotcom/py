if __name__ == '__main__':
    ogrenciler = {'12345':{'isim':'Ramazan Ozgur','soyisim':'Dogan'},
                  '12346':{'isim':'Hulya','soyisim':'Yaldiz'},
                  '12347':{'isim':'Yigit Kagan','soyisim':'Caliskan'}}
    
    print('''
----------------------------------------
Ogrenci Bilgi Sistemi v.1
----------------------------------------
| Komut Listesi                        |
----------------------------------------
| kapat   | Uygulamayi sonlandir       |
| ekle    | Ogrenci ekle               |
| sil     | Ogrenci siler              |
| guncelle| Ogrenci gunceller          |
| listele | Ogrencileri listeler       |
----------------------------------------        
''')
 
    komut = input('Komut giriniz:').strip().lower()
    while komut != 'kapat':
        if komut == 'ekle':
            print('----------------------------------------')
            ogrenci_sayisi = int(input('Ogrenci sayisini giriniz:'))

            for sira in range(ogrenci_sayisi):
                key = input(f'{sira+1}. Ogrenci numarasini giriniz:')
                
                if key in ogrenciler: 
                    print(f'{ogrenci_numarasi} numarali ogrenci zaten mevcut!')
                else:
                    isim = input(f'{sira+1}. Ogrenci adini giriniz:')
                    soyisim = input(f'{sira+1}. Ogrenci soyadini giriniz:')
                    ogrenciler[key] = {'isim':isim,'soyisim':soyisim}      
            print('----------------------------------------')
        elif komut == 'sil':
            print('----------------------------------------')
            ogrenci_numarasi = input('Ogrenci numarasini giriniz:')

            try:
                del ogrenciler[ogrenci_numarasi]
                print(f'{ogrenci_numarasi} numarali ogrenci silindi!')
            except:
                print(f'{ogrenci_numarasi} numarali bir ogrenci yok!')
            
            print('----------------------------------------')
        elif komut == 'guncelle':
            print('----------------------------------------')
            key = input(f'Ogrenci numarasini giriniz:')

            if key in ogrenciler:
                isim = input(f'Ogrenci adini giriniz:')
                soyisim = input(f'Ogrenci soyadini giriniz:')
                
                ogrenciler[key] = {'isim':isim,'soyisim':soyisim}

                print(f'{key} numarali bir ogrenci guncellendi!')
            else:
                print(f'{key} numarali bir ogrenci yok!')
            print('----------------------------------------')
        elif komut == 'listele':
            print('----------------------------------------')
            print('-' * 40)
            print(f'|{" "*2}| {"Isim":<13} | {"Soyisim":<8} | {"Numara":<5} |')
            print('-' * 40)

            for sira, key in enumerate(ogrenciler):
                print(f'|{(sira+1):>2}| {ogrenciler[key]['isim']:<13} | {ogrenciler[key]['soyisim']:<8} | {key:<5} |')    
            print('----------------------------------------')
        else:
            print('----------------------------------------')
            print(f'"{komut}" seklinde tanimli bir komut bulanamadi!')
            print('----------------------------------------')
        
        komut = input('Komut giriniz:').strip().lower()

    print('------------------------------------')
    print('Program sonlandirildi!')
    print('------------------------------------')