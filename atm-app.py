#ATM UYGULAMASI

hesapElbistan = {
    'isim': 'yunus karaca',
    'hesap_no': '82004623',
    'bakiye': 6000,
    'avans': 3000
}

hesapMalatya = {
    'isim': 'emre karaca',
    'hesap_no': '82004425',
    'bakiye': 10000,
    'avans': 8000
}

def paraYatir(hesap, miktar):
    hesap['bakiye'] += miktar;
    print(f"{hesap['hesap_no']} nolu hesabınıza {miktar} TL para yatırıldı. Yeni bakiyeniz {hesap['bakiye']} oldu")


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['isim']}")
    
    if(hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar;
        print("paranızı alabilirsiniz")
        
    else:
        toplam = hesap['bakiye'] + hesap['avans'];
        
        if(toplam >= miktar):
            avans_kullanimi = input('avans kullanmak istiyormusunuz (e / h)')
            
            if(avans_kullanimi == 'e'):
                avans_kullanilacak_miktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['avans'] -= avans_kullanilacak_miktar
                print("paranızı alabilirsiniz")
                
            else:
                print(f"{hesap['hesap_no']} nolu hesabınızda {hesap['bakiye']} TL para mevcuttur")
            
        else:
            print("hesabınızda yeterli para mevcut değil")
        
def bakiyeSorgula(hesap):
    print(f"{hesap['hesap_no']} nolu hesabınızda { hesap['bakiye']} TL para mevcuttur. Avans hesabınızda {hesap['avans']} TL para mevcuttur")


paraCek(hesapElbistan, 1000)
paraYatir(hesapElbistan, 20000)
bakiyeSorgula(hesapElbistan)