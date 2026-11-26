# Handoff

Läs den här först i varje ny session, oavsett agent. Skriv så att någon utan tillgång till chatten kan fortsätta.

## Agentregler och inventering
- **Agentregler:** v1.14 (2026-11-18), inlästa 2026-11-26. Repot följde inte agentreglerna tidigare (det var tomt).
- **Inventory: 2026-11-26**
  - Repot var helt tomt: inga commits, inga grenar, inga PR och inga Issues. Ingen befintlig dokumentation, inget att anpassa.
  - Lagar och regler: inget ännu. Se över när innehållet är bestämt (t.ex. om sidan visar personuppgifter, bilder eller tredjepartstjänster).
- **Projektspråk:** inte bestämt. Standard enligt agentreglerna är engelska för nya projekt (samma som trythis.one). Arbetsdokumenten skrivs på svenska.
- **Publicering:** inte uppsatt. Förslag: Cloudflare Workers (static assets) kopplad till repot, som trythis.one och dess underdomäner (F-002).
- **Miljöns begränsningar (2026-11-26, molnsession):**
  - `trythis.one` nås inte från miljön (proxy 403), så agenten kan inte kontrollera den publicerade sidan.
  - Repot `BadBagel47/trythis.one` gick att läsa (för design och publiceringssätt). Läsåtkomst till `BadBagel47/trythis-infra` nekades.
  - Agenten har ingen åtkomst till Cloudflare (DNS, Workers).
  - 2026-11-26 (senare): ägaren ändrade nätverket. YouTube, material.io, developer.chrome.com, styles.refero.design och 21st.dev nås nu. `trythis.one` svarar fortfarande 403, nu från Cloudflare själv (zonens skydd stoppar troligen molnagenter, samma som noterat i trythis.one-repot).

## Dokumentkarta
- `AGENTS.md`: hänvisning till agentreglerna + projektregler
- `CLAUDE.md`: bara en pekare till `AGENTS.md`
- `docs/BACKLOG.md`: buggar, funktioner och planering (B-/F-/D-) samt föreslagna körningar
- `index.html`: hela sidan (HTML, CSS och JS i en fil, inget byggsteg)
- `links.json`: alla grupper och länkar. Sidan byggs från den här filen; nya länkar läggs till här.
- `assets/fonts/`: Inter (lokalt, OFL-licens bredvid), samma fil som trythis.one
- `.assetsignore`: det Cloudflare inte ska publicera (dokumentation m.m.)

## Beslut
- **2026-11-26:** Sidan är en länksamling med grupper av länkar, inte en "länk i bio"-sida. Först YouTube-kanaler, senare andra platser. Det är tips på saker ägaren gillar som kan intressera alla, utan profil eller annat som knyter sidan till ägaren personligen. Den ska vara snygg och strukturerad, inte bara rena länkar (ägarens besked).

## Engångsåtgärder
- **Kommer att föreslås (F-002):** koppla repot till en Worker hos Cloudflare och lägg till underdomänen som egen domän, så att varje push till `main` publiceras automatiskt.
- **Kan föreslås:** tillåt `trythis.one` (och underdomänen) i molnmiljöns nätverk, så att agenten kan kontrollera den publicerade sidan.

## Väntande anpassning
_Inget._

## Läget nu
- Demodesign klar (F-001): mörkt tema som trythis.one, fem YouTube-kanaler i två grupper, kort med färgad cirkel, sökruta och gruppfilter (gruppen kan länkas med t.ex. `#space`). Provad i Chromium i dator- och mobilbredd utan konsolfel. Inte publicerad på någon adress än (F-002).
- En förhandsvisning finns som privat Claude-artefakt för ägaren.

## Nästa steg
1. Ägaren tittar på demodesignen och ger synpunkter.
2. Justera (F-001), hämta kanalbilder (F-004), sedan publicering (F-002).

## Senaste ändringar
| Datum | Agent | Vad |
|---|---|---|
| 2026-11-26 | Claude | F-001: demodesign med fem kanaler i två grupper, ej publicerad. |
| 2026-11-26 | Claude | Beslut: länksamling, först YouTube-kanaler. F-003–F-005 inlagda. |
| 2026-11-26 | Claude | Repot uppsatt enligt agentreglerna v1.14: AGENTS.md, handoff och backlog. F-001 och F-002 inlagda. |
