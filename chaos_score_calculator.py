import os

def var_olan_ilk(yollar):
    for p in yollar:
        if p and os.path.isdir(p):
            return p
    return None

def dosya_say(klasor):
    if not klasor or not os.path.isdir(klasor):
        return 0
    sayi = 0
    for ad in os.listdir(klasor):
        tam = os.path.join(klasor, ad)
        if os.path.isfile(tam):
            sayi += 1
    return sayi

def puan_hesapla(sayi, limit):
    if sayi <= limit:
        return int(sayi * 30 / limit)
    elif sayi <= 2 * limit:
        ekstra = sayi - limit
        return 30 + int(ekstra * 50 / limit)
    elif sayi <= 3 * limit:
        ekstra = sayi - 2 * limit
        return 80 + int(ekstra * 20 / limit)
    else:
        return 100

def mesaj4(toplam):
    if toplam < 25:
        return "Harika, neredeyse hiç kaos yok!"
    elif toplam < 50:
        return "Fena değil, biraz düzen iyi olabilir."
    elif toplam < 70:
        return "Kaos seviyesi biraz yüksek, düzen iyi olur."
    else:
        return "Kaos seviyesi yüksek, temizlik zamanı!"

def main():
    home = os.path.expanduser("~")

    masaustu = var_olan_ilk([os.path.join(home, "Desktop"),
                             os.path.join(home, "Masaüstü")])
    indirilenler = var_olan_ilk([os.path.join(home, "Downloads"),
                                 os.path.join(home, "İndirilenler")])
    belgeler = var_olan_ilk([os.path.join(home, "Documents"),
                             os.path.join(home, "Belgeler")])

    # limitleri sabit değişkenler olarak tutmak okunurluğu artırır
    M_LIMIT = 20
    D_LIMIT = 50
    B_LIMIT = 30

    m_sayi = dosya_say(masaustu)
    d_sayi = dosya_say(indirilenler)
    b_sayi = dosya_say(belgeler)

    m_puan = puan_hesapla(m_sayi, M_LIMIT)
    d_puan = puan_hesapla(d_sayi, D_LIMIT)
    b_puan = puan_hesapla(b_sayi, B_LIMIT)

    toplam = int((m_puan + d_puan + b_puan) / 3)
    on_uzerinden = int(toplam / 10)
    yorum = mesaj4(toplam)

    print("=== Chaos Score Calculator ===\n")
    print("Masaüstü  :", m_sayi, "dosya ->", m_puan, "/100")
    print("Downloads :", d_sayi, "dosya ->", d_puan, "/100")
    print("Belgeler  :", b_sayi, "dosya ->", b_puan, "/100")
    print("--------------------------------")
    print("Toplam Chaos Puanı:", toplam, "/100  |  10 üzerinden:", on_uzerinden, "/10")
    print(yorum)

    f = open("chaos_rapor.txt", "w", encoding="utf-8")
    f.write("Chaos Score Raporu\n")
    f.write("-------------------\n")
    f.write("Masaüstü  : " + str(m_sayi) + " dosya -> " + str(m_puan) + "/100\n")
    f.write("Downloads : " + str(d_sayi) + " dosya -> " + str(d_puan) + "/100\n")
    f.write("Belgeler  : " + str(b_sayi) + " dosya -> " + str(b_puan) + "/100\n")
    f.write("Toplam Chaos Puanı: " + str(toplam) + "/100  |  10 üzerinden: " + str(on_uzerinden) + "/10\n")
    f.write(yorum + "\n")
    f.close()

if __name__ == "__main__":
    main()
