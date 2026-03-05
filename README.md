# 📻 YO Log PRO v16.5 FINAL — Professional Multi-Contest Amateur Radio Logger

## ✅ Windows 7 / 8 / 10 / 11 Compatible

---

### 🇷🇴 DESPRE ACEASTĂ VERSIUNE

Această versiune este **identică** cu versiunea Windows 10/11, dar construită cu **Python 3.8** pentru compatibilitate maximă cu sistemele mai vechi.

> ✅ **Dacă e eroare DLL: instalați [vcredist\_x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe)**

---

### 🇬🇧 ABOUT THIS VERSION

This version is **identical** to the Windows 10/11 version, but built with **Python 3.8** for maximum compatibility with older systems.

> ✅ **If DLL error: install [vcredist\_x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe)**

---

## 🖥️ COMPATIBILITATE / COMPATIBILITY

| Sistem / System | Status |
|----------------|--------|
| Windows 7 SP1 (32/64 bit) | ✅ |
| Windows 8 / 8.1 | ✅ |
| Windows 10 | ✅ |
| Windows 11 | ✅ |

> **🇷🇴** Construit cu Python 3.8.10 — ultima versiune compatibilă cu Windows 7
>
> **🇬🇧** Built with Python 3.8.10 — the last version compatible with Windows 7

---

## 🆕 ACTUALIZĂRI v16.5 / UPDATES v16.5

### 🇷🇴 REZOLVĂRI MAJORE:

* ✅ **REZOLVAT:** Frecvența, banda, modul și RST **persistă între QSO-uri**
* ✅ **REZOLVAT:** Doar indicativul și nota se șterg după logare
* ✅ **ÎMBUNĂTĂȚIT:** Fluxul de operare este acum **mult mai rapid** — nu mai trebuie să setați banda/modul/RST la fiecare QSO
* ✅ **NOU:** Buton **Reset** complet separat pentru ștergere totală câmpuri

**ÎMBUNĂTĂȚIRI CABRILLO 2.0 (v16.4 → v16.5):**

* ✅ **ADĂUGAT:** Export Cabrillo 2.0 cu dialog configurare exchange
* ✅ **ADĂUGAT:** Opțiuni exchange TRIMIS: Județ/Locator/Serial/Nimic
* ✅ **ADĂUGAT:** Opțiuni exchange PRIMIT: Din log (notă/serial)/Nimic
* ✅ **ADĂUGAT:** Dialog previzualizare înainte de export
* ✅ **ADĂUGAT:** Import Cabrillo 2.0 și 3.0
* ✅ **ADĂUGAT:** Câmp `cabrillo_name` în editor concurs
* ✅ **ADĂUGAT:** Câmp `exchange_format` per concurs
* ✅ **ADĂUGAT:** Câmpuri Email și Soapbox în setări
* ✅ **ADĂUGAT:** Validare + backup automat înainte de export
* ✅ **ADĂUGAT:** Dialog salvare fișier pentru toate exporturile

---

### 🇬🇧 MAJOR FIXES:

* ✅ **FIXED:** Frequency, band, mode and RST **persist between QSOs**
* ✅ **FIXED:** Only callsign and note clear after logging
* ✅ **IMPROVED:** Operating flow is now **much faster** — no need to set band/mode/RST for every QSO
* ✅ **NEW:** Separate **Reset** button for full field clearing

**CABRILLO 2.0 IMPROVEMENTS (v16.4 → v16.5):**

* ✅ **ADDED:** Cabrillo 2.0 export with exchange configuration dialog
* ✅ **ADDED:** Exchange SENT options: County/Locator/Serial/None
* ✅ **ADDED:** Exchange RECEIVED options: From log (note/serial)/None
* ✅ **ADDED:** Preview dialog before export
* ✅ **ADDED:** Import Cabrillo 2.0 and 3.0
* ✅ **ADDED:** `cabrillo_name` field in contest editor
* ✅ **ADDED:** `exchange_format` field per contest
* ✅ **ADDED:** Email and Soapbox fields in settings
* ✅ **ADDED:** Validation + auto-backup before export
* ✅ **ADDED:** Save file dialog for all exports

---

## 📋 FLUX DE OPERARE / OPERATING FLOW

### 🇷🇴 Flux Rapid v16.5

```
PRIMUL QSO:
1. Setați banda → 40m
2. Setați modul → SSB (RST auto: 59)
3. Tastați indicativul → YO3ABC
4. ENTER → QSO logat!

URMĂTOARELE QSO-URI:
1. Tastați indicativul → YO4XYZ
2. ENTER → QSO logat!
   (banda, modul, RST — RĂMÂN!)

SCHIMBAȚI BANDA/MODUL:
- F2 = bandă următoare
- F3 = mod următor (RST se ajustează automat)

RESETARE COMPLETĂ:
- [Reset] → șterge TOATE câmpurile (freq, bandă, mod, RST)
```

### 🇬🇧 Quick Flow v16.5

```
FIRST QSO:
1. Set band → 40m
2. Set mode → SSB (auto RST: 59)
3. Type callsign → YO3ABC
4. ENTER → QSO logged!

NEXT QSOs:
1. Type callsign → YO4XYZ
2. ENTER → QSO logged!
   (band, mode, RST — PERSIST!)

CHANGE BAND/MODE:
- F2 = next band
- F3 = next mode (RST auto-adjusts)

FULL RESET:
- [Reset] → clears ALL fields (freq, band, mode, RST)
```

---

## 📤 EXPORT CABRILLO 2.0 — GHID COMPLET

### 🇷🇴 Configurare Exchange

**PASUL 1:** Click `[📤 Export]` → `Cabrillo 2.0 (.log)`

**PASUL 2:** Dialog configurare exchange:

| Exchange TRIMIS | Ce trimiteți | Exemplu |
|----------------|--------------|---------|
| **Județ** | Județ din setări | `NT` |
| **Locator** | Locator din setări | `KN37` |
| **Nr. Serial** | Din coloana Nr S | `001` |
| **Nimic** | `--` | `--` |

| Exchange PRIMIT | Ce primiți | Exemplu |
|----------------|------------|---------|
| **Din log** | Notă sau Nr R din log | `BV` sau `045` |
| **Nimic** | `--` | `--` |

**PASUL 3:** Click `[📤 Exportă]` → previzualizare

**PASUL 4:** Click `[Salvează]` → alegeți locația

---

### 🇬🇧 Cabrillo 2.0 Exchange Configuration

**STEP 1:** Click `[📤 Export]` → `Cabrillo 2.0 (.log)`

**STEP 2:** Exchange configuration dialog:

| Exchange SENT | What you send | Example |
|---------------|---------------|---------|
| **County** | County from settings | `NT` |
| **Locator** | Locator from settings | `KN37` |
| **Serial Nr.** | From Nr S column | `001` |
| **None** | `--` | `--` |

| Exchange RECEIVED | What you receive | Example |
|-------------------|-----------------|---------|
| **From log** | Note or Nr R from log | `BV` or `045` |
| **None** | `--` | `--` |

**STEP 3:** Click `[📤 Export]` → preview

**STEP 4:** Click `[Save]` → choose location

---

## 🆚 COMPARAȚIE VERSIUNI / VERSION COMPARISON

| Funcționalitate | v16.2 | v16.4 | **v16.5** |
|----------------|-------|-------|-----------|
| **Persistență câmpuri** | ❌ Tot se șterge | ❌ Tot se șterge | ✅ **Freq/Band/Mode/RST persistă** |
| **Export Cabrillo 2.0** | ❌ | ✅ | ✅ **+ Exchange configurabil** |
| **Import Cabrillo** | ❌ | ✅ 3.0 only | ✅ **2.0 + 3.0** |
| **Preview export** | ❌ | ❌ | ✅ **Toate exporturile** |
| **Validare pre-export** | ❌ | ❌ | ✅ **Automat + backup** |
| **Email/Soapbox** | ❌ | ❌ | ✅ **În setări** |
| **Compatibil Win7** | ❌ | ❌ | ✅ **DA!** |

---

## 🐛 DEPANARE / TROUBLESHOOTING

| Problemă | Cauză | Soluție |
|----------|-------|---------|
| Banda nu se schimbă cu F2 | Concursul are o singură bandă | Normal — verificați concursul |
| RST nu se schimbă cu F3 | RST manual setat | Apăsați F3 din nou pentru auto-RST |
| Exchange dialog gol | Județ/Locator nesetat | [⚙ Setări] → Completați |
| Preview nu apare | Pop-up blocat | Verificați taskbar |
| Import Cabrillo eșuat | Format invalid | Verificați că e Cabrillo 2.0 sau 3.0 |
| Eroare DLL pe Win7 | Visual C++ lipsă | Instalați vcredist_x64.exe |
| „This app can't run" | EXE construit cu Python 3.9+ | Folosiți această versiune ✅ |

---

## 📜 CHANGELOG COMPLET / COMPLETE CHANGELOG

### v16.5 FINAL
* ✅ Freq/Band/Mode/RST persist between QSOs (only call+note clear)
* ✅ Separate Reset button for full clearing
* ✅ **Construit cu Python 3.8 — compatibil Windows 7!**

### v16.4 FINAL
* ✅ Cabrillo 2.0 export with exchange dialog
* ✅ Import Cabrillo 2.0 and 3.0
* ✅ Preview dialog for all exports
* ✅ Email and Soapbox fields
* ✅ Validation + auto-backup before export

### v16.2 FINAL
* ✅ Contest manager improvements
* ✅ Statistics window
* ✅ ADIF/EDI export

---

## 📞 CONTACT ȘI SUPORT / CONTACT AND SUPPORT

| | |
|---|---|
| **Dezvoltator / Developer** | Ardei Constantin-Cătălin |
| **Indicativ / Callsign** | **YO8ACR** |
| **Email** | yo8acr@gmail.com |
| **Versiune / Version** | **16.5 FINAL** |
| **Python build** | **3.8.10 (Windows 7 compatible)** |

---

**🎯 REMEMBER:**
* **F2** = Bandă următoare / Next band
* **F3** = Mod următor / Next mode
* **Enter** = LOG QSO
* **[Reset]** = Ștergere completă / Full clear
* **Ctrl+S** = Salvare forțată / Force save

---

**73 de YO8ACR! 📻**

*🇷🇴 „v16.5 — Acum și pe Windows 7!"*  
*🇬🇧 "v16.5 — Now also on Windows 7!"*

**YO Log PRO v16.5 FINAL — Compatible with ALL Windows versions**
