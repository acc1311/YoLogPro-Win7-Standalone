# 📋 Ghid: Creare Repository GitHub pentru YO Log PRO

## Pasul 1 — Creează repository nou pe GitHub

1. Mergi pe https://github.com
2. Click **"New repository"** (butonul verde sau +)
3. Completează:
   - **Repository name:** `yo-log-pro` (sau ce nume dorești)
   - **Description:** `YO Log PRO - Amateur Radio Logger (Windows 7 Compatible)`
   - Bifează **"Public"** (pentru Releases gratuite)
   - Bifează **"Add a README file"**
4. Click **"Create repository"**

---

## Pasul 2 — Încarcă fișierele

### Metoda A — Direct pe site (fără Git instalat)

1. Intră în repository-ul nou creat
2. Click **"Add file"** → **"Upload files"**
3. Încarcă:
   - `yo_log_pro.py`
   - `README.md` (înlocuiește-l pe cel generat automat)
   - `YO_Log_PRO.spec`
4. Click **"Commit changes"**

### Metoda B — Creează fișierele direct pe GitHub

Pentru `.github/workflows/build.yml`:
1. Click **"Add file"** → **"Create new file"**
2. În câmpul de nume scrie: `.github/workflows/build.yml`
   - GitHub va crea automat folderele
3. Copiază conținutul din `build.yml` furnizat
4. Click **"Commit new file"**

---

## Pasul 3 — Verifică că Actions funcționează

1. Mergi la tab-ul **"Actions"** din repository
2. Ar trebui să vezi workflow-ul rulând automat
3. Dacă nu rulează, click pe workflow → **"Run workflow"**

---

## Pasul 4 — Descarcă executabilul

### Din Artifacts (temporar, 30 zile):
1. Actions → click pe build reușit (verde ✅)
2. Scroll jos la **"Artifacts"**
3. Descarcă `YO_Log_PRO_Windows7_Compatible`

### Din Releases (permanent):
- Mergi la **Releases** în repository
- Descarcă `YO_Log_PRO_v16.5.exe`

---

## ⚠️ IMPORTANT — Setare permisiuni pentru Release

Dacă primești eroarea **"Resource not accessible by integration"**:

1. Mergi la **Settings** → **Actions** → **General**
2. La **"Workflow permissions"** selectează:
   - ✅ **"Read and write permissions"**
3. Bifează **"Allow GitHub Actions to create and approve pull requests"**
4. Click **Save**

---

## 🔧 Structura finală a repository-ului

```
yo-log-pro/
├── .github/
│   └── workflows/
│       └── build.yml       ← COPIAZĂ CONȚINUTUL DIN build.yml
├── yo_log_pro.py           ← ÎNCARCĂ FIȘIERUL TĂU
├── YO_Log_PRO.spec         ← COPIAZĂ CONȚINUTUL DIN spec
└── README.md               ← ÎNLOCUIEȘTE CU README-ul FURNIZAT
```

---

## ❓ Probleme frecvente

**Build eșuează cu "icon.ico not found"**
→ Normal, workflow-ul are fallback automat fără icon

**EXE-ul nu pornește pe Windows 7**
→ Verifică că Python 3.8 este selectat în `build.yml` (nu 3.9+)

**"This app can't run on your PC" pe Windows 7**
→ Executabilul a fost construit cu Python 3.9+. Asigură-te că workflow-ul folosește `python-version: '3.8.10'`

---

73 de YO8ACR!
