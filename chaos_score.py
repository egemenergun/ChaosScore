import os

def first_existing(paths):
    for p in paths:
        if p and os.path.isdir(p):
            return p
    return None

home = os.path.expanduser("~")

desktop_candidates = [
    os.path.join(home, "Desktop"),
    os.path.join(home, "Masaüstü"),
    os.path.join(home, "OneDrive", "Desktop"),
    os.path.join(home, "OneDrive", "Masaüstü"),
]
downloads_candidates = [
    os.path.join(home, "Downloads"),
    os.path.join(home, "İndirilenler"),
    os.path.join(home, "OneDrive", "Downloads"),
    os.path.join(home, "OneDrive", "İndirilenler"),
]
documents_candidates = [
    os.path.join(home, "Documents"),
    os.path.join(home, "Belgeler"),
    os.path.join(home, "OneDrive", "Documents"),
    os.path.join(home, "OneDrive", "Belgeler"),
]

DESKTOP_PATH = first_existing(desktop_candidates)
DOWNLOADS_PATH = first_existing(downloads_candidates)
DOCUMENTS_PATH = first_existing(documents_candidates)

def scan_folder(path, limit):
    if not path or not os.path.isdir(path):
        return 0, 0
    names = os.listdir(path)
    count = 0
    for name in names:
        full_path = os.path.join(path, name)
        if os.path.isfile(full_path):
            count += 1
    if count <= limit:
        score = 0
    elif count <= 2 * limit:
        score = 50
    else:
        score = 100
    return count, score

def msg(total):
    if total < 30:
        return "Harika, neredeyse hiç kaos yok!"
    elif total < 70:
        return "Fena değil, biraz düzen iyi olabilir."
    else:
        return "Kaos seviyesi yüksek, temizlik zamanı!"

def main():
    print("=== Chaos Score Calculator ===\n")
    d_n, d_s = scan_folder(DESKTOP_PATH, 20)
    dl_n, dl_s = scan_folder(DOWNLOADS_PATH, 50)
    dc_n, dc_s = scan_folder(DOCUMENTS_PATH, 30)
    total = int((d_s + dl_s + dc_s) / 3)
    print("Masaüstü  :", d_n, "dosya ->", d_s, "/100")
    print("Downloads :", dl_n, "dosya ->", dl_s, "/100")
    print("Belgeler  :", dc_n, "dosya ->", dc_s, "/100")
    print("--------------------------------")
    print("Toplam Chaos Puanı:", total, "/100")
    print(msg(total))
    f = open("chaos_rapor.txt", "w", encoding="utf-8")
    f.write("Chaos Score Raporu\n")
    f.write("-------------------\n")
    f.write(f"Masaüstü  : {d_n} dosya -> {d_s}/100\n")
    f.write(f"Downloads : {dl_n} dosya -> {dl_s}/100\n")
    f.write(f"Belgeler  : {dc_n} dosya -> {dc_s}/100\n")
    f.write(f"Toplam Chaos Puanı: {total}/100\n")
    f.write(msg(total) + "\n")
    f.close()

if __name__ == "__main__":
    main()
