while True:
    import random
    print("""              *****************
              SAYI TAHMIN OYUNU
              ***************** """)
    puan=100
    ts=1
    sayi=random.randint(0,100)
    tahmin=-1
    isim=input("adinizi giriniz ")
    while tahmin!=sayi:
        tahmin=int(input(f"hadi {isim}, tahmin et "))
        if tahmin<sayi:
            print(f"daha buyuk tahmin et {isim}")
            ts=ts+1
            puan=puan-10
            if ts==10:
                print(f"bilemedin {isim}, cevap {sayi}, puanin {puan}")
                break
           
        
        elif tahmin>sayi:
            print(f"daha kucuk tahmin et {isim}")
            ts=ts+1
            puan=puan-10
            if ts==10:
                print(f"bilemedin {isim}, cevap {sayi}, puanin {puan}")
                break
            

        else:
            print(f"tebrikler {isim} dogru cevap {ts}. tahmininde buldun, puanin {puan}")
        

           
            
                
                

           

