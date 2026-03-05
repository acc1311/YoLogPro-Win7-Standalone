# YO Log PRO v16.5
**Professional Multi-Contest Amateur Radio Logger**

Dezvoltat de: **Ardei Constantin-Cătălin (YO8ACR)**  
Email: yo8acr@gmail.com

---

## 📥 Descărcare

Mergi la [**Releases**](../../releases) și descarcă `YO_Log_PRO_v16.5.exe`

> ✅ **Compatibil cu Windows 7 SP1, Windows 8, Windows 10, Windows 11**  
> ✅ **Nu necesită instalare Python** — executabil standalone

---

## 🖥️ Cerințe sistem

| Sistem | Status |
|--------|--------|
| Windows 7 SP1 (32/64 bit) | ✅ Compatibil |
| Windows 8 / 8.1 | ✅ Compatibil |
| Windows 10 | ✅ Compatibil |
| Windows 11 | ✅ Compatibil |

> **Notă:** Executabilul este construit cu **Python 3.8**, ultima versiune care suportă Windows 7.

---

## ✨ Funcționalități principale

- Logger multi-contest pentru radioamatori
- Export **Cabrillo 2.0** cu dialog configurabil (County/Grid/Serial/None)
- Export **ADIF 3.1**, **CSV**, **EDI (REG1TEST)**
- Import Cabrillo 2.0 și 3.0
- Calcul distanță prin locator Maidenhead
- Baza de date DXCC (lookup țară după indicativ)
- Backup automat înainte de export
- Interfață în română și engleză
- Sunet la QSO nou (Windows beep)

---

## 🔨 Build din sursa (pentru dezvoltatori)

### Cerințe
- **Python 3.8.x** (obligatoriu pentru compatibilitate Windows 7)
- PyInstaller 5.13.2

### Instalare
```bash
pip install pyinstaller==5.13.2
```

### Build manual
```bash
# Simplu (recomandat)
pyinstaller --onefile --windowed --name "YO_Log_PRO_v16.5" yo_log_pro.py

# Cu fisier SPEC (avansat)
pyinstaller YO_Log_PRO.spec
```

### Build automat (GitHub Actions)
La fiecare push pe `main`, Actions construiește automat executabilul.  
Vezi `.github/workflows/build.yml`

---

## 📁 Structura repository

```
├── yo_log_pro.py              # Codul sursa principal
├── YO_Log_PRO.spec            # Configuratie PyInstaller
├── .github/
│   └── workflows/
│       └── build.yml          # GitHub Actions - build automat
└── README.md
```

---

## ⚠️ De ce Python 3.8?

Python **3.9 și versiunile mai noi** nu mai suportă Windows 7.  
Python **3.8** este ultima versiune oficială compatibilă cu Windows 7 SP1.

Dacă folosești Python 3.9+ pentru build, executabilul va afișa eroarea:  
`This app can't run on your PC` pe Windows 7.

---

## 📜 Changelog

### v16.5 (FINAL)
- FIX: Frecvența, banda, modul și RST persistă între QSO-uri

### v16.4
- ADĂUGAT: Export Cabrillo 2.0 cu dialog configurabil
- ADĂUGAT: Import Cabrillo 2.0 și 3.0
- ADĂUGAT: Câmpuri Email și Soapbox în setări
- ADĂUGAT: Preview înainte de export

---

**73 de YO8ACR!**
