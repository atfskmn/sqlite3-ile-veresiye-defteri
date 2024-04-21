import sqlite3
import time

db = sqlite3.connect("veresiye.db")

yetki = db.cursor()

yetki.execute("CREATE TABLE IF NOT EXISTS kisiler(isim,borc)")


while True:
    
    print("***veresiye defterine hoş geldiniz***")
    
    sor = input("1-)borçlu ekle\n2-)borçluları gör\n")
    
    if sor =="1":
        borclu_isim = input("borçlu ismi giriniz:")
        borc_miktari = int(input ("borç miktarını giriniz:"))
        
        yetki.execute(f"INSERT INTO kisiler VALUES('{borclu_isim}','{borc_miktari}')")
        db.commit()
        
        print("işlem tamamlanıyor...")
        time.sleep(2)
        print(f" işlem tamamlandı borçlu kişinin ismi:{borclu_isim}")
        
    elif sor == "2":
        yetki.execute("SELECT *FROM kisiler")
        yazdır = yetki.fetchall()
        for i in yazdır:
          print(f"borçlu ismi:{i[0]}\nborç miktarı:{i[1]}\n")
           
db.commit()
db.close()

    
    
