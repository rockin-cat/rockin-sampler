# Rockin Sampler

Sampler de pads per fer servir el **Novation Launchkey 25** com un instrument més de la banda. Inspirat en Koala Sampler, pensat per a l'aula i el directe.

**Obre'l al navegador (Chrome o Edge):** https://rockin-cat.github.io/rockin-sampler/

**App per a Mac (funciona sense internet):** a [Releases](https://github.com/rockin-cat/rockin-sampler/releases/latest) hi ha `Rockin-Sampler-Mac-Apple.zip` (Mac amb xip M1–M4) i `Rockin-Sampler-Mac-Intel.zip`. Descomprimeix-lo i fes clic dret → Obre a «Instal·la Rockin Sampler.command».

Rockin.cat SCCL · llicència [CC BY-NC-SA 4.0](LICENSE.md)

## Novetats de la 0.6

- **Cada pista amb la seva llargada**: si apuges la «Llargada del bucle», les pistes ja gravades es repeteixen soles (p. ex. bateria d'1 compàs sota un teclat de 4). «Es repeteix cada» canvia la llargada d'una pista; si l'allargues, el contingut es duplica.
- **Bucles de teclat**: amb ● gravant, les notes de les tecles també es graven en bucle amb el so triat (durada i força incloses). Cada so fa la seva pista a dalt del seqüenciador; es pot esborrar amb × o desfer.
- Pantalla completa amb barra de navegació (Pads, Seqüenciador, Sons del teclat, Kits i connexió), transport fix i tema fosc.
- El seqüenciador comença buit; «Esborra-ho tot» i avís quan sonen ritmes d'altres bancs.

## Novetats de la 0.4

- **Seqüenciador en bucle tipus Koala**: prem ● (pantalla o Launchkey), compte enrere d'un compàs i tot el que toques als pads es grava en bucle; cada volta s'hi afegeix el que toques. Bucle d'1, 2, 4 o 8 compassos, quantització (sense, 1/8, 1/16, 1/32), compte enrere, metrònom, swing i botó de desfer. La graella permet editar-ho a mà, compàs a compàs.
- **Capa d'efectes (FX)**: el botó FX del costat dels pads (el botó «Stop/Solo/Mute» del Launchkey) converteix els 16 pads en efectes en directe sobre tot el que sona. Es mantenen premuts; Shift + pad els deixa fixos. Fila de dalt: Repeat 1/4, 1/8, 1/16, 1/32, Gate, Al revés, Tape stop, Lent. Fila de baix: Filtre greu, Filtre agut, Telèfon, Distorsió, Bitcrush, Pitch avall, Pitch amunt, Espai.
- **Gravar un so des del Launchkey**: mantén ● i toca un pad; per parar, torna a tocar el pad o prem ●. ● sol (prémer i deixar anar) grava el ritme. Shift + ● també grava al pad triat.

## Novetats de la 0.3

- La pantalla segueix la disposició del Launchkey 25 MK3: pantalla, knobs, ▶ i ●, Shift, fletxes, pads, botons de l'escena, rodes i tecles. Els botons físics fan el mateix que els de la pantalla.
- **80 pads en 5 bancs** (▲ ▼): A Bateria, B Electrònica (808/909), C Percussió, D Efectes i acords, E Gravacions (buit, per als sons propis). Tots els sons es generen dins l'app, sense fitxers.
- **17 sons de teclat** (◄ ►): piano elèctric, piano de joguina, orgue, marimba, campanes, baix, sub, baix àcid, sintetitzador, lead, pad, cordes, metalls, cor, xip 8-bit, guitarra, arpa, flauta, i «El meu so».
- **Seqüenciador de 16 passos**: ▶ l'engega; ● mentre sona grava el que toques als pads (quantitzat). Tempo, swing i metrònom. Es desa amb el kit.
- **Shift + pad** tria un pad sense fer-lo sonar (per gravar-hi des del Launchkey).
- Rodes de pitch i modulació, i botons d'octava per al teclat en pantalla.

## Què fa

- **Ja configurat per al Launchkey 25**: els 16 pads (mode Drum o Session), els 8 knobs i les 25 tecles funcionen en connectar-lo.
- **Llums dels pads**: cada pad del Launchkey s'il·lumina amb el mateix color que a la pantalla. El pad seleccionat fa pampallugues suaus, el que està gravant es posa vermell i en tocar-los fan un flaix blanc. Es pot desactivar amb el botó «Llums dels pads».
- **Sons del teclat**: piano elèctric, baix, sintetitzador, pad, orgue, campanes, o qualsevol so gravat («Toca'l amb el teclat»; el Do3 és el to original). Roda de modulació = vibrato, pitch bend = ±2 semitons, pedal = sustain.
- **Gravació**: tria un pad buit i prem el botó vermell (o la barra espaiadora). Es veu el nivell mentre grava i retalla els silencis sol.
- **Knobs**: 1 Filtre · 2 Reverb · 3 Eco · 4 Volum màster · 5 To · 6 Volum · 7 Inici · 8 Final (els quatre últims, del pad seleccionat). També es poden girar amb el ratolí.
- **Configura els pads**: si un model envia notes diferents, l'assistent demana prémer els 16 pads en ordre i ho recorda.
- Teclat de l'ordinador: Q–I i A–K per als pads, ← → per canviar el so del teclat.
- Kits desats a l'ordinador i exportables com a `.rockinkit`.

## Com funcionen les llums

L'app posa el Launchkey en **mode DAW** (el mateix que fa servir Ableton) a través del seu segon port MIDI, i li diu de quin color ha d'encendre cada pad. Quan tanques l'app, el torna al mode normal. Si les llums no s'encenen, l'app continua funcionant igual; només cal que els pads estiguin en mode Drum.

## Com provar-lo

**Web (GitHub Pages):** puja la carpeta a un repo de `rockin-cat` i activa Pages. Obre-ho amb **Chrome o Edge** (Safari no té MIDI). El micròfon necessita `https://` o `localhost`.

**En local:** obre `index.html` amb Chrome. Si el micròfon no respon, serveix la carpeta amb `npx serve`.

## Fer el .exe (Windows)

Cal [Node.js](https://nodejs.org).

```
npm install
npm start        # prova l'app d'escriptori
npm run exe      # genera dist/Rockin Sampler 0.2.0.exe (portable)
```

A l'app d'escriptori el micròfon i el MIDI funcionen sense demanar permís.
