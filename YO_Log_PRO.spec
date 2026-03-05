# -*- mode: python ; coding: utf-8 -*-
# PyInstaller SPEC file pentru YO Log PRO v16.5
# Compatibil cu Windows 7 SP1+
# Foloseste Python 3.8 (ultima versiune cu suport Win7)

block_cipher = None

a = Analysis(
    ['yo_log_pro.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Adauga fisiere JSON daca exista
        # ('contests.json', '.'),
        # ('config.json', '.'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'tkinter.scrolledtext',
        'winsound',
        'json',
        'csv',
        'math',
        'hashlib',
        'pathlib',
        'collections',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude biblioteci inutile pentru a reduce dimensiunea
        'numpy',
        'pandas',
        'matplotlib',
        'scipy',
        'PIL',
        'PyQt5',
        'wx',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='YO_Log_PRO_v16.5',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,           # Comprima executabilul (optional, necesita UPX instalat)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,      # False = fara fereastra CMD (aplicatie GUI)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='icon.ico',  # Decomentati daca aveti un fisier icon.ico
)
