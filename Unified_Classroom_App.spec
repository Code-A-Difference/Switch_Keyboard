# -*- mode: python ; coding: utf-8 -*-

import mediapipe
import os
mediapipe_path = os.path.dirname(mediapipe.__file__)

a = Analysis(
    ['Unified_Classroom_App.py'],
    pathex=[],
    binaries=[],
    datas=[(mediapipe_path, 'mediapipe')], 
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Unified_Classroom_App',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Unified_Classroom_App',
)

app = BUNDLE(
    coll,  # <--- FIXED: Changed from 'exe' to 'coll' so ALL dependencies are included!
    name='Unified_Classroom_App.app',
    icon=None,
    bundle_identifier='com.codeadifference.unifiedclassroom',
    info_plist={
        'NSCameraUsageDescription': 'This application requires webcam access to perform AI hand tracking.',
        'NSHighResolutionCapable': True,
    },
)