# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/bbaukema/Documents/python/pyqt5/src/main/python/main.py'],
             pathex=['/Users/bbaukema/Documents/python/pyqt5/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/bbaukema/.pyenv/versions/3.6.5/envs/venv/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/bbaukema/Documents/python/pyqt5/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='MyApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/bbaukema/Documents/python/pyqt5/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='MyApp')
app = BUNDLE(coll,
             name='MyApp.app',
             icon='/Users/bbaukema/Documents/python/pyqt5/target/Icon.icns',
             bundle_identifier=None)
