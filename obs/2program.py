'''
yazar: zravza
email: zeynepravzasln@gmail.com

açıklama: python programlama dilini
bir öğrenci bilgi sistemi senaryosu ile 
öğreten repo (anaprogram dosyası)
'''
if __name__ == '__main__':

    başlık= 'Öğrenci bilgi sistemi (v1)'
    print(başlık)
    print(len(başlık))

    print('-'*100)
    print(f'| {başlık:<94} |x|')
    # print(başlık," "*(94-(len(başlık)+1)),"|x|")
    print('-'*100)
    
    öğrenci_adı = input("öğrenci adını giriniz:")
    öğrenci_soyadı = input("öğrenci soyadını giriniz: ")
    öğrenci_numarası = input("öğrenci numarasını giriniz: ")
    
    print('-'*100)
    print(f'|{"isim":<40} | {"soyisim":<30} | {"numara":<20} |')
    print('-'*100)
    print(f'|{öğrenci_adı:<40} | {öğrenci_soyadı:<30} | {öğrenci_numarası:<20} |')
    #print('|','isim'," "*(94-(len(başlık)+1)),"|x|")
    



    #print("|"," "*96,"|")
    #print("|"," "*96,"|")
    #print("|"," "*96,"|")
    #print("|"," "*96,"|")
    #print('-'*100)
