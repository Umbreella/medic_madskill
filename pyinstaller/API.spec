# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

datas = []
datas += collect_data_files('coreschema')
datas += [
    (r'./venv/Lib/site-packages/coreschema/', './coreschema'),
    (r'./venv/Lib/site-packages/django_filters/', './django_filters'),
    (r'./venv/Lib/site-packages/rest_framework/', './rest_framework'),
    (r'./venv/Lib/site-packages/drf_yasg/', './drf_yasg'),
    (r'./venv/Lib/site-packages/whitenoise/', './whitenoise'),
]

block_cipher = None


a = Analysis(
    ['medic_madskill\\manage.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='API',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='API',
)
