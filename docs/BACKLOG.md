# Backlog

ID: `B-###` buggar · `F-###` funktioner · `D-###` planering/design. En gemensam nummerserie. Prioritet: Hög, Medel, Låg.

## Föreslagna körningar
Ögonblicksbild, ersätts vid varje nytt förslag.

Prioriterat för: en första fungerande sida så snabbt som möjligt
- **A** – stark modell, medelnivå – Första versionen av länksidan – väntar på svar
  - F-001 – Bygg sidan med länkar i kategorier, fungerande på mobil och dator
- **B** – standardmodell, medelnivå – Publicering på underdomänen – bygger på A
  - F-002 – Förbered publicering via Cloudflare Workers och ge ägaren stegen för engångsåtgärden

## Öppet

### F-001 Länksida: första versionen
- **Prioritet:** Hög
- **Status:** Väntar på svar
- **Vad:** En strukturerad länksida (länkar grupperade i kategorier) på en underdomän till trythis.one. Allt i en `index.html` utan byggsteg, som trythis.one. Webbgrunderna i agentreglernas `WEB.md` ingår från start.
- **Frågor (2026-11-26):**
  - Vad ska sidan vara: en "länk i bio"-sida om ägaren (profil + knappar), eller en länksamling/katalog med kategorier? Ingen rekommendation.
  - Vilka länkar och kategorier? Rekommendation: ägaren skickar en lista i valfri form; annars byggs sidan med några exempellänkar som byts ut.
  - Utseende och språk? Rekommendation: samma mörka rymdtema och typsnitt (Inter) som trythis.one men lugnare, med sökruta; sidans text på engelska.

### F-002 Publicering på underdomänen
- **Prioritet:** Hög
- **Status:** Bygger på F-001
- **Vad:** Publicera sidan på Cloudflare Workers (static assets) som trythis.one, med `.assetsignore` så att dokumentation och verktyg inte publiceras. Ägaren gör en engångsåtgärd hos Cloudflare: koppla repot och lägga till underdomänen.
- **Frågor (2026-11-26):**
  - Vilken underdomän? Rekommendation: `links.trythis.one` (kort, tydligt, matchar repots namn).

## Klart
_Inget ännu._
