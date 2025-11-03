# Chaos Score Calculator

A simple Python script for **COE203 – Advanced Programming with Python**.

It counts files in Desktop, Downloads, and Documents folders and gives a “chaos score” (0–100).  
It also saves a short report to `chaos_rapor.txt`.

## How to Run (Quick)
1. Make sure Python 3 is installed. Check: `python --version` (macOS/Linux: `python3 --version`)
2. Open a terminal in the project folder.
3. Run:
   - Windows: `python chaos_score.py`
   - macOS/Linux: `python3 chaos_score.py`

## What it uses (Course Topics)
- Variables, conditions (`if/elif/else`)
- Loops (`for`)
- Functions (`def`)
- Getting folder contents with `os.listdir`
- Simple file writing (`open(..., "w")`)

## How it finds folders
The script builds common paths from your home directory (Desktop/Masaüstü, Downloads/İndirilenler, Documents/Belgeler, OneDrive variants) and uses the first existing one.  
If a folder doesn’t exist, its score is counted as 0 and the program continues.

---

## Türkçe Özet

**Chaos Score Calculator**, Masaüstü / İndirilenler / Belgeler klasörlerindeki dosya sayısını sayar ve 0–100 arası “kaos puanı” üretir.  
Sonuçlar terminalde görünür ve `chaos_rapor.txt` dosyasına yazılır.

### Çalıştırma (Kısaca)
1. Python 3 kurulu olsun (`python --version` ile kontrol).
2. Proje klasöründe terminal aç.
3. Çalıştır:
   - Windows: `python chaos_score.py`
   - macOS/Linux: `python3 chaos_score.py`

### Kapsam (Dersle uyumlu)
- Değişkenler, koşullar, döngüler, fonksiyonlar
- `os.listdir` ile liste alma
- Basit dosya yazma (`open(..., "w")`)

**Not:** Klasör adları bilgisayardan bilgisayara değişebildiği için (Desktop/Masaüstü, OneDrive vb.), script evrensel yolları dener; olmayan klasörleri 0 sayar, çalışmaya devam eder.
