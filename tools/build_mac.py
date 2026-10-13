import plistlib, shutil, subprocess, os, json, sys
B='/home/claude/build'; SRC='/home/claude/rockin-sampler'
VER=json.load(open(f'{SRC}/package.json'))['version']
INSTALL='''#!/bin/bash
# Instal·la el Rockin Sampler a Aplicacions i el prepara per obrir-se en aquest Mac
cd "$(dirname "$0")"
APP="Rockin Sampler.app"
echo ""
echo "  Instal·lant el Rockin Sampler..."
rm -rf "/Applications/$APP"
ditto "$APP" "/Applications/$APP" || { echo "  No s'ha pogut copiar a Aplicacions."; exit 1; }
xattr -cr "/Applications/$APP"
codesign --force --deep --sign - "/Applications/$APP" >/dev/null 2>&1
echo "  Fet! S'obrirà ara. Ja pots tancar aquesta finestra."
open "/Applications/$APP"
'''
README='''ROCKIN SAMPLER per a Mac (funciona sense internet)

INSTAL·LACIÓ (només el primer cop)
  1. Fes clic dret (o Ctrl + clic) a «Instal·la Rockin Sampler.command» > Obre > Obre.
     (El Mac avisa perquè no és de l'App Store; és normal.)
  2. S'obre una finestra del Terminal: copia l'app a Aplicacions, la prepara i l'obre.
  3. Accepta el permís del micròfon.
  A partir d'aquí obre «Rockin Sampler» des d'Aplicacions o el Launchpad.

Si el pas 1 no deixa obrir el fitxer: Configuració del Sistema > Privacitat i seguretat >
a baix de tot, «Obre igualment».

Quin zip va amb cada Mac?  Menú  > Quant a aquest Mac:
  «Xip Apple M…»  -> versió Apple      «Processador Intel» -> versió Intel

Rockin.cat SCCL · CC BY-SA 4.0
'''
out=f'{B}/out'; os.makedirs(out,exist_ok=True)
for arch, label in [('arm64','Apple'),('x64','Intel')]:
    d=f'{out}/{arch}'; shutil.rmtree(d,ignore_errors=True); os.makedirs(d)
    subprocess.run(['unzip','-q',f'{B}/electron-darwin-{arch}.zip','-d',d],check=True)
    app=f'{d}/Rockin Sampler.app'; os.rename(f'{d}/Electron.app',app)
    res=f'{app}/Contents/Resources'
    if os.path.exists(f'{res}/default_app.asar'): os.remove(f'{res}/default_app.asar')
    a=f'{res}/app'; os.makedirs(a)
    for f in ['index.html','main.js','README.md']: shutil.copy(f'{SRC}/{f}',a)
    shutil.copytree(f'{SRC}/fonts',f'{a}/fonts')
    json.dump({'name':'rockin-sampler','productName':'Rockin Sampler','version':VER,'main':'main.js'},open(f'{a}/package.json','w'))
    shutil.copy(f'{B}/icon.icns',f'{res}/electron.icns')
    p=f'{app}/Contents/Info.plist'; info=plistlib.load(open(p,'rb'))
    info.update({'CFBundleName':'Rockin Sampler','CFBundleDisplayName':'Rockin Sampler','CFBundleIdentifier':'cat.rockin.sampler',
      'CFBundleShortVersionString':VER,'CFBundleVersion':VER,'LSApplicationCategoryType':'public.app-category.music',
      'NSMicrophoneUsageDescription':'El Rockin Sampler fa servir el micròfon per gravar sons als pads.','NSHumanReadableCopyright':'Rockin.cat SCCL · CC BY-SA 4.0'})
    for k in ['NSCameraUsageDescription','NSBluetoothAlwaysUsageDescription','NSBluetoothPeripheralUsageDescription']: info.pop(k,None)
    plistlib.dump(info,open(p,'wb'))
    subprocess.run([f'{B}/rcodesign','sign',app],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    sc=f'{d}/Instal·la Rockin Sampler.command'; open(sc,'w').write(INSTALL); os.chmod(sc,0o755)
    open(f'{d}/LLEGEIX-ME.txt','w').write(README)
    z=f'{out}/Rockin-Sampler-Mac-{label}.zip'
    if os.path.exists(z): os.remove(z)
    subprocess.run(['zip','-qry',z,'Rockin Sampler.app','Instal·la Rockin Sampler.command','LLEGEIX-ME.txt'],cwd=d,check=True)
    print(label, VER, os.path.getsize(z)//(1<<20),'MB')
