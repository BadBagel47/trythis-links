# Backlog

ID: `B-###` buggar · `F-###` funktioner · `D-###` planering/design. En gemensam nummerserie. Prioritet: Hög, Medel, Låg.

## Föreslagna körningar
Ögonblicksbild, ersätts vid varje nytt förslag.

Prioriterat för: nytt innehåll först, sedan lättare påfyllning och levande innehåll
- **A** – standardmodell, låg nivå – Ny kanal
  - F-007 – Lägg till That Good News Girl i en ny grupp "Feel-good", med bild
- **B** – standardmodell, medelnivå – Snabbspara-knapp
  - F-003 – Bokmärkesknapp som lägger till sidan du står på i listan
- **C** – standardmodell, medelnivå – Senaste videon per kanal
  - F-005 – Visa senaste videons bild och titel på kanalkorten, uppdateras automatiskt

Parkerat: F-002 (publicering på links.trythis.one)

## Öppet

### F-002 Publicering på underdomänen
- **Prioritet:** Låg
- **Status:** Parkerad 2026-11-26 – ägaren vill låta sidan ligga på GitHub Pages under arbetet (F-006).
- **Vad:** Publicera sidan på Cloudflare Workers (static assets) som trythis.one, med `.assetsignore` så att dokumentation och verktyg inte publiceras. Ägaren gör en engångsåtgärd hos Cloudflare: koppla repot och lägga till underdomänen.
- **Frågor (2026-11-26):**
  - Vilken underdomän? Rekommendation: `links.trythis.one`.

### F-003 Snabbspara-knapp (bokmärke)
- **Prioritet:** Medel
- **Vad:** Ett bokmärke i ägarens webbläsare som, när man står på t.ex. en YouTube-kanal, öppnar ett förifyllt formulär på GitHub (länk, namn, välj grupp). En GitHub Action lägger in länken i listfilen och sidan publiceras. Kräver troligen en engångsåtgärd om agenten inte får skapa workflow-filer.

### F-005 Senaste videon per kanal
- **Prioritet:** Låg
- **Vad:** YouTubes öppna flöde per kanal (ingen API-nyckel) läses av en schemalagd GitHub Action som uppdaterar senaste videons bild och titel. Ingen inbäddad spelare, så inga kakor från YouTube.
- **Utredning (2026-11-26):**
  - Flödet `https://www.youtube.com/feeds/videos.xml?channel_id=UC…` är öppet och tillhandahålls av YouTube för flödesläsare. Det behöver kanalens ID (UC…), inte @namnet. ID:t slås upp en gång och sparas i `links.json`.
  - Flödet kan inte läsas direkt från besökarens webbläsare (YouTube tillåter inte det, CORS), så hämtningen måste ske på serversidan: schemalagd GitHub Action (rekommenderas) eller en Cloudflare Worker.
  - Flödet tar med Shorts. Ett inofficiellt flöde för bara vanliga videor finns (`playlist_id=UULF…`), men det kan sluta fungera utan förvarning.
  - Flödet svarar ibland med fel; behåll då senast kända video.
  - Miniatyrbilden laddas ner och sparas på sidan, så att besökarna inte kontaktar Google.
  - Rättat 2026-11-26: Tom Scott är tillbaka sedan mars 2026 med en veckoserie ("Tom Scott: England", först på Nebula, en vecka senare på YouTube), så flödet ger färska videor.

### F-007 Ny kanal: That Good News Girl
- **Prioritet:** Medel
- **Vad:** Lägg till https://www.youtube.com/@thatgoodnewsgirl/videos (Jenn Crumm, "A cozy corner of the internet for animal stories and good news", cirka 10 000 prenumeranter 2026-11-27). Passar inte befintliga grupper.
- **Förslag:** ny grupp "Feel-good" (id `feelgood`, "Kind stories, animals and good news for a better mood.") och korttexten "Cozy animal stories and good news from around the world, a calm break from the headlines." Bild hämtas med `tools/fetch-images.py`.

## Klart

### F-006 Publicering på GitHub Pages under arbetet
- **Prioritet:** Hög
- **Vad:** En GitHub Action publicerar bara sidans filer (`index.html`, `links.json`, `assets/`) till GitHub Pages vid varje push till `main`, så att dokumentationen inte blir en del av sajten. Adress: https://badbagel47.github.io/trythis-links/
- **Engångsåtgärd för ägaren:** Settings → Pages → Source: "GitHub Actions". Behövs också om agenten inte får skapa workflow-filer: lägg in filen via github.com.
- **Klar:** 2026-11-26. Publicerad och kontrollerad: sidan svarar, dokumentation och verktyg publiceras inte.

### F-001 Länksida: första versionen
- **Prioritet:** Hög
- **Vad:** En länksamling med grupper av länkar, först YouTube-kanaler, senare andra platser. Snygg, inte bara rena länkar: varje länk visas som ett kort (bild, namn, ägarens egen kommentar), grupperat i sektioner, med sökruta och filtrering på grupp. Alla länkar ligger i en enda lättläst listfil som sidan byggs från. Allt utan ramverk, som trythis.one. Webbgrunderna i agentreglernas `WEB.md` ingår från start.
- **Nya länkar från ägaren (2026-11-26)**, föreslagen ny grupp "Design & web" (id `design`) med korttexter:
  - https://material.io/ – Material Design: "Google's open design system: guidelines, components, colour and type tools, and icons."
  - https://developer.chrome.com/docs/modern-web-guidance – Modern Web Guidance: "Chrome's vetted guides that teach AI coding agents modern web patterns, with browser support data."
  - https://styles.refero.design/ – Refero Styles: "Over 2,000 design systems pulled from real product sites, ready to copy as tokens or DESIGN.md."
  - https://21st.dev/ – 21st.dev: "Over 12,000 hand-made React components, templates and themes, ready to drop into your project."
  - Beskrivningarna kontrollerade mot sajternas egna beskrivningar 2026-11-26. Alla fyra har en delningsbild (og:image) som kan användas som kortbild (F-004).
- **Förslag på ny korttext för Tom Scott** (införd 2026-11-26): "Short videos about amazing places and odd facts, now back with a weekly road trip through England."
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
- **Klar:** 2026-11-26

### F-004 Hämta kanalbild och namn automatiskt
- **Prioritet:** Hög
- **Vad:** Bild, namn och beskrivning hämtas från länkens förhandsinformation och sparas på sidan, så att besökarnas webbläsare inte kontaktar YouTube (inga kakor från tredje part). Sedan ägaren ändrade nätverket 2026-11-26 når molnmiljön YouTube och de övriga länkarnas sajter, så agenten kan hämta och prova själv.
- **Lag och regler:** kanalbilder och namn används som förhandsvisning med länk till källan, vilket är vanligt, men bilderna tillhör kanalerna. Ingen juridisk bedömning; ägaren kan välja att ta bort en bild på begäran.
- **Klar:** 2026-11-26

