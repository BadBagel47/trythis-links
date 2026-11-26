# Backlog

ID: `B-###` buggar · `F-###` funktioner · `D-###` planering/design. En gemensam nummerserie. Prioritet: Hög, Medel, Låg.

## Föreslagna körningar
Ögonblicksbild, ersätts vid varje nytt förslag.

Prioriterat för: en snygg första version så snabbt som möjligt, sedan enklare påfyllning
- **A** – stark modell, medelnivå – Justera demodesignen och hämta kanalbilder – väntar på ägarens synpunkter
  - F-001 – Ändringar efter ägarens synpunkter på demodesignen
  - F-004 – Kanalbild, namn och beskrivning hämtas automatiskt från länken och sparas på sidan
- **B** – standardmodell, medelnivå – Publicering på underdomänen – bygger på A
  - F-002 – Förbered publicering via Cloudflare Workers och ge ägaren stegen för engångsåtgärden
- **C** – standardmodell, medelnivå – Snabbspara-knapp i webbläsaren – bygger på A
  - F-003 – Bokmärkesknapp som skickar sidan du står på till länklistan
- **D** – standardmodell, medelnivå – Senaste videon per kanal – bygger på A
  - F-005 – Visa senaste videons bild och titel i kanalkortet, uppdateras automatiskt

## Öppet

### F-001 Länksida: första versionen
- **Prioritet:** Hög
- **Status:** Demodesign klar 2026-11-26, väntar på ägarens synpunkter. Inte publicerad (F-002). Kanalerna visas med initialer i färgade cirklar tills riktiga kanalbilder hämtas (F-004).
- **Vad:** En länksamling med grupper av länkar, först YouTube-kanaler, senare andra platser. Snygg, inte bara rena länkar: varje länk visas som ett kort (bild, namn, ägarens egen kommentar), grupperat i sektioner, med sökruta och filtrering på grupp. Alla länkar ligger i en enda lättläst listfil som sidan byggs från. Allt utan ramverk, som trythis.one. Webbgrunderna i agentreglernas `WEB.md` ingår från start.
- **Svar 2026-11-26:** länksamling, i första hand YouTube-kanaler (se Beslut i HANDOFF).
- **Ägarens första länkar (2026-11-26):**
  - https://www.youtube.com/@EverydayAstronaut/videos
  - https://www.youtube.com/@joescott/videos
  - https://www.youtube.com/@TomScottGo/videos
  - https://www.youtube.com/@astrumspace/videos
  - https://www.youtube.com/@AstrumEarth/videos
  - Förslag på grupper: "Space" (Everyday Astronaut, Astrum) och "Science & curiosities" (Joe Scott, Tom Scott, Astrum Earth). Agenten skriver en kort kommentar per kanal på engelska som ägaren kan ändra.
- **Frågor (2026-11-26):**
  - Grupper? Rekommendation: se förslaget ovan.
  - Utseende och språk? Rekommendation: mörkt rymdtema och typsnittet Inter som trythis.one men lugnare; kort med kanalbild; sidans text på engelska.
  - Hur läggs länkar till? Rekommendation: en listfil som agenten fyller på när ägaren skickar länkar i chatten (eller som ägaren redigerar på github.com); snabbspara-knapp senare (F-003).

### F-002 Publicering på underdomänen
- **Prioritet:** Hög
- **Vad:** Publicera sidan på Cloudflare Workers (static assets) som trythis.one, med `.assetsignore` så att dokumentation och verktyg inte publiceras. Ägaren gör en engångsåtgärd hos Cloudflare: koppla repot och lägga till underdomänen.
- **Frågor (2026-11-26):**
  - Vilken underdomän? Rekommendation: `links.trythis.one`.

### F-003 Snabbspara-knapp (bokmärke)
- **Prioritet:** Medel
- **Vad:** Ett bokmärke i ägarens webbläsare som, när man står på t.ex. en YouTube-kanal, öppnar ett förifyllt formulär på GitHub (länk, namn, välj grupp). En GitHub Action lägger in länken i listfilen och sidan publiceras. Kräver troligen en engångsåtgärd om agenten inte får skapa workflow-filer.

### F-004 Hämta kanalbild och namn automatiskt
- **Prioritet:** Hög
- **Vad:** Bild, namn och beskrivning hämtas från länkens förhandsinformation och sparas på sidan, så att besökarnas webbläsare inte kontaktar YouTube (inga kakor från tredje part). Molnmiljön når inte YouTube (proxy 403, 2026-11-26), så hämtningen görs av en GitHub Action eller efter en engångsåtgärd som tillåter YouTube i miljöns nätverk.
- **Lag och regler:** kanalbilder och namn används som förhandsvisning med länk till källan, vilket är vanligt, men bilderna tillhör kanalerna. Ingen juridisk bedömning; ägaren kan välja att ta bort en bild på begäran.

### F-005 Senaste videon per kanal
- **Prioritet:** Låg
- **Vad:** YouTubes öppna flöde per kanal (ingen API-nyckel) läses av en schemalagd GitHub Action som uppdaterar senaste videons bild och titel. Ingen inbäddad spelare, så inga kakor från YouTube.

## Klart
_Inget ännu._
