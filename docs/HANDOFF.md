# Handoff

Läs den här först i varje ny session, oavsett agent. Skriv så att någon utan tillgång till chatten kan fortsätta.

## Agentregler och inventering
- **Agentregler:** v1.14 (2026-11-18), inlästa 2026-11-26. Repot följde inte agentreglerna tidigare (det var tomt).
- **Inventory: 2026-11-26**
  - Repot var helt tomt: inga commits, inga grenar, inga PR och inga Issues. Ingen befintlig dokumentation, inget att anpassa.
  - Lagar och regler: inget ännu. Se över när innehållet är bestämt (t.ex. om sidan visar personuppgifter, bilder eller tredjepartstjänster).
- **Projektspråk:** inte bestämt. Standard enligt agentreglerna är engelska för nya projekt (samma som trythis.one). Arbetsdokumenten skrivs på svenska.
- **Publicering:** GitHub Pages via `.github/workflows/pages.yml`, automatiskt vid push till `main` (F-006, beslut 2026-11-26). Cloudflare och underdomänen är parkerade (F-002).
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
- `assets/images/`: kortbilder, hämtade med `tools/fetch-images.py` (kräver Pillow)
- `.github/workflows/pages.yml`: publicerar bara sidans filer till GitHub Pages vid push till `main`
- `.assetsignore`: det Cloudflare inte ska publicera (används först när F-002 tas upp igen)

## Beslut
- **2026-11-27:** Projektregel godkänd: länkar som ägaren skickar i chatten läggs in och publiceras direkt när de passar en befintlig grupp. Nya grupper och större ändringar går via körförslag. Står i `AGENTS.md`.
- **2026-11-26:** Sidan ligger på GitHub Pages medan den utvecklas. trythis.one och underdomänen ignoreras tills vidare (F-002 parkerad). Ägarens besked.
- **2026-11-26:** Sidan är en länksamling med grupper av länkar, inte en "länk i bio"-sida. Först YouTube-kanaler, senare andra platser. Det är tips på saker ägaren gillar som kan intressera alla, utan profil eller annat som knyter sidan till ägaren personligen. Den ska vara snygg och strukturerad, inte bara rena länkar (ägarens besked).

## Engångsåtgärder
- **Klar 2026-11-26:** GitHub Pages med källa "GitHub Actions".
- **Klar 2026-11-26:** ägaren öppnade molnmiljöns nätverk för YouTube och länkarnas sajter.
- **Kommer att föreslås (F-002):** koppla repot till en Worker hos Cloudflare och lägg till underdomänen som egen domän, så att varje push till `main` publiceras automatiskt.
- **Kan föreslås:** tillåt `trythis.one` (och underdomänen) i molnmiljöns nätverk, så att agenten kan kontrollera den publicerade sidan.

## Väntande anpassning
_Inget._

## Läget nu
- Sidan har 19 länkar i fem grupper: Space, Science & curiosities, Animals & good news, Tools & design, Game making. Kort med riktiga bilder (utom Poly Pizza, som blockerar hämtning), sökruta och gruppfilter.
- Bilderna hämtas med `tools/fetch-images.py` (kör den när nya länkar läggs till) och sparas i `assets/images/`.
- Publicerad på GitHub Pages (F-006): https://badbagel47.github.io/trythis-links/ – varje push till `main` publiceras automatiskt.

## Nästa steg
1. Ägaren tittar på sidan och ger synpunkter.
2. Nästa körningar: F-003 (snabbspara-knapp) och F-005 (senaste videon).

## Senaste ändringar
| Datum | Agent | Vad |
|---|---|---|
| 2026-11-27 | Claude | F-007–F-009: tio nya länkar, grupperna Animals & good news och Game making, Design & web heter nu Tools & design. Projektregel om direkt tillägg godkänd. |
| 2026-11-26 | Claude | F-001, F-004: nio länkar i tre grupper med riktiga bilder. F-006: GitHub Pages-workflow. |
| 2026-11-26 | Claude | F-001: demodesign med fem kanaler i två grupper, ej publicerad. |
| 2026-11-26 | Claude | Beslut: länksamling, först YouTube-kanaler. F-003–F-005 inlagda. |
| 2026-11-26 | Claude | Repot uppsatt enligt agentreglerna v1.14: AGENTS.md, handoff och backlog. F-001 och F-002 inlagda. |
