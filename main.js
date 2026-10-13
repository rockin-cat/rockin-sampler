// Rockin Sampler: app d'escriptori (Electron) per a Windows i Mac. Funciona sense internet.
const { app, BrowserWindow, session, systemPreferences } = require('electron');
const path = require('path');

const PERMESOS = ['media', 'midi', 'midiSysex', 'audioCapture'];

app.whenReady().then(async () => {
  // Micròfon i MIDI permesos sense preguntar dins l'app
  session.defaultSession.setPermissionRequestHandler((wc, perm, cb) => cb(PERMESOS.includes(perm)));
  session.defaultSession.setPermissionCheckHandler((wc, perm) => PERMESOS.includes(perm));
  // Al Mac, el sistema demana permís del micròfon una sola vegada (la primera que s'obre l'app)
  if (process.platform === 'darwin'){ try { await systemPreferences.askForMediaAccess('microphone'); } catch (e) {} }

  const win = new BrowserWindow({
    width: 1320, height: 900, minWidth: 760, minHeight: 560,
    backgroundColor: '#f4f4f1', title: 'Rockin Sampler', autoHideMenuBar: true,
    webPreferences: { backgroundThrottling: false },   // el seqüenciador no s'alenteix si la finestra queda darrere
  });
  win.loadFile(path.join(__dirname, 'index.html'));
});

app.on('window-all-closed', () => app.quit());
