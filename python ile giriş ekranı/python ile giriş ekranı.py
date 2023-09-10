import time

db_ka = "esra"
db_pw = 1234
şifre_hak = 0

while True:
    kullanıcı_adı = input("Lütfen kullanıcı adınızı girin: ")
    şifre = int(input("Lütfen şifrenizi girin: "))

    if(db_ka == kullanıcı_adı) and (db_pw == şifre):
        print("Hoşgeldin : {}".format(kullanıcı_adı))
        break
    elif(db_ka != kullanıcı_adı) and (db_pw == şifre):
        print("Kullanıcı adı hatalı.. Lütfen yeniden deneyiniz..")
    elif(db_ka == kullanıcı_adı) and (db_pw != şifre):
        print("Şifre hatalı..Lütfen yeniden deneyiniz.")
        şifre_hak += 1
        if(şifre_hak == 3):
            print("3 kere hatalı şifre girdiniz.Lütfen 10 saniye bekleyiniz.")
            time.sleep(10)
            print("Şifrenizi değiştirmek ister misiniz? E/H")
            cevap = input().lower()
            if(cevap == 'e'):
                yeni_şifre = int(input("Yeni şifrenizi girin: "))
                db_pw = yeni_şifre
                print("Şifreniz başarılı şekilde güncellenmiştir.")
            else:
                continue




