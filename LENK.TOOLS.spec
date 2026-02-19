# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('mods.json', '.'),
        ('assets', 'assets'),
    ],
    hiddenimports=[
        'mods.forge.mod',
        'mods.forge.circle_detect',
        'mods.forge.cursor_jiggle',
        'mods.forge.bar_game',
        'mods.forge.go_detector',
        'components.autoclicker',
        'components.sprint',
        'components.hold_key',
        'components.periodic_attack',
        'components.auto_sell',
        'components.macro_editor',
        'wiki.data',
        'wiki.parser',
        'wiki.search',
        'wiki.window',
        'wiki.search_overlay',
    ],
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
    a.binaries,
    a.datas,
    [],
    name='LENK.TOOLS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=False,
)
