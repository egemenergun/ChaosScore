# Chaos Score Calculator

A simple Python script for **COE203 – Advanced Programming with Python**.

It counts files in **Desktop**, **Downloads**, and **Documents** and gives a **Chaos Score (0–100)** and an **out-of-10 score**.  
It also saves a short report to `chaos_report.txt`.

## How to Run (Quick)
1. Make sure Python 3 is installed (`python --version`, macOS/Linux: `python3 --version`).
2. Open a terminal in this project folder.
3. Run:
   - **Windows:** `python chaos_score_calculator.py`
   - **macOS/Linux:** `python3 chaos_score_calculator.py`

## What it uses (Course Topics)
- Variables, conditions (`if / elif / else`)
- Loops (`for`)
- Functions (`def`)
- Listing folder contents with `os.listdir`
- Simple file writing (`open(..., "w")`)

## How it finds folders
The script tries common names from your home directory and picks the first that exists:  
`Desktop / Masaüstü`, `Downloads / İndirilenler`, `Documents / Belgeler`.  
If a folder does not exist, it is counted as **0** and the program continues.

## Scoring (simple)
- File counts are converted to a smooth score with basic piece-wise math (not only 0/100).  
- Final score = average of the three folder scores.  
- Message levels (4):
  1) **Great, almost no chaos!**
  2) **Not bad, a bit of tidying could help.**
  3) **Chaos level is a bit high, tidying would help.**
  4) **Chaos level is high, time to clean!**

---

## Türkçe Özet

**Chaos Score Calculator**, **Masaüstü / İndirilenler / Belgeler** klasörlerindeki **dosya** sayısını sayar.  
**Kaos Puanı (0–100)** ve **10 üzerinden puan** üretir.  
Sonuçları `chaos_report.txt` dosyasına da yazar.

### Çalıştırma (Kısaca)
1. Python 3 kurulu olsun (`python --version` / macOS-Linux: `python3 --version`).
2. Bu proje klasöründe terminal aç.
3. Çalıştır:
   - **Windows:** `python chaos_score_calculator.py`
   - **macOS/Linux:** `python3 chaos_score_calculator.py`

### Kullandığı Konular
- Değişkenler, koşullar (`if / elif / else`)
- Döngüler (`for`)
- Fonksiyonlar (`def`)
- `os.listdir` ile klasör içeriği listeleme
- `open(..., "w")` ile basit dosya yazma

### Klasör Bulma
Ev dizininden şu yaygın adları dener ve bulunan ilkini kullanır:  
`Desktop / Masaüstü`, `Downloads / İndirilenler`, `Documents / Belgeler`.  
Bulunmayan klasör **0** kabul edilir, program devam eder.

### Puanlama (basit)
- Dosya sayısı, basit parça-parça hesapla 0–100 aralığına çevrilir.  
- Final puanı üç klasör puanının ortalamasıdır.  
- Mesaj seviyeleri (4):
  1) **Harika, neredeyse hiç kaos yok!**
  2) **Fena değil, biraz düzen iyi olabilir.**
  3) **Kaos seviyesi biraz yüksek, düzen iyi olur.**
  4) **Kaos seviyesi yüksek, temizlik zamanı!**
