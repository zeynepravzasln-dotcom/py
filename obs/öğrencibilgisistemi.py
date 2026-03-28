'''
    yazar: ravza
    email: zeynepravzasln@gmail.com

    açıklama: python programlama dilini bir öğrenci bilgi sistemi senaryosu ile öğreten bir repo  (anaprogram dosyası)

'''

if __name__ == 'main':
    print('''
----------------------------------
Öğrenci Bilgi Sistemi v.1
----------------------------------         
| Komut Listesi                  |    
----------------------------------
|kapat  | Uygulamayı Sonlandır   |
|ekle   | Öğrenci Ekle           |
|sil    | öğrenci siler          |
|listele| öğrenci listelendir    |      
----------------------------------          
      ''')
    #"kapat".strip()="kapat"   "kapat".strip()="kapat")
    #"kapat".lower()="kapat"   "kaPat".lower()="kapat")
    #"kapat".upper()="KAPAT"   "kapat".strip()="KAPAT")
    komut = input('komut giriniz:').strip().lower()
    while komut != 'kapat':
        if komut == 'ekle':
            print('----------------------------------')
            print('öğrenci ekleme kodları!!!!')
        elif komut == 'sil':
            print('----------------------------------')
            print('öğrenci silme kodları!!!!')
        elif komut == 'listele':
            print('----------------------------------')
            print('öğrenci listeleme kodları!!!!')
        else:
            print('----------------------------------')
            print(f'"{komut}" şeklinde tanımlı bir komut bulunamadı!')
            print('----------------------------------')
        komut = input('komut giriniz:').strip().lower()
    print('----------------------------------')
    print('program sonlandırıldı')
    print('----------------------------------')

    başlık = 'Öğrenci Bilgi Sistemi (v1)'

    print('-' * 100)
    print(f'| {başlık:<94} |x|')
    print('-' * 100)
    öğrenci_adları = []
    öğrenci_soyadları = []
    öğrenci_numaraları = []

    öğrenci_sayısı = int(input('Öğrenci Sayısını Giriniz:'))

    for sıra in range(öğrenci_sayısı):
        öğrenci_adları.append(input(f'{sıra+1}. Öğrenci adını giriniz:')) 
        öğrenci_soyadları.append(input(f'{sıra+1}. Öğrenci soyadını giriniz:')) 
        öğrenci_numaraları.append(input(f'{sıra+1}. Öğrenci numarasını giriniz:'))
    

    print('-' * 100)
    print(f'|{" "*9} | {"İsim":<35} | {"Soyisim":<25} | {"Numara":<20} |')
    print('-' * 100)
    for sıra in range(öğrenci_sayısı):
        print(f'| {(sıra+1):>7} | {öğrenci_adları[sıra]:<35} | {öğrenci_soyadları[sıra]:<25} | {öğrenci_numaraları[sıra]:<20} |')



    #print('|',' ' *96, '|')
    #print('|',' ' *96, '|')
    #print('|',' ' *96, '|')
    #print('-' * 100)
    
