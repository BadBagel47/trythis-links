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

## Dokumentkarta
- `AGENTS.md`: hänvisning till agentreglerna + projektregler
- `CLAUDE.md`: bara en pekare till `AGENTS.md`
- `docs/BACKLOG.md`: buggar, funktioner och planering (B-/F-/D-) samt föreslagna körningar

## Beslut
_Inga ännu._

## Engångsåtgärder
- **Kommer att föreslås (F-002):** koppla repot till en Worker hos Cloudflare och lägg till underdomänen som egen domän, så att varje push till `main` publiceras automatiskt.
- **Kan föreslås:** tillåt `trythis.one` (och underdomänen) i molnmiljöns nätverk, så att agenten kan kontrollera den publicerade sidan.

## Väntande anpassning
_Inget._

## Läget nu
- Repot har bara dokumentation. Ingen sida är byggd än.
- Första körningen (F-001) väntar på ägarens svar om vad sidan ska innehålla.

## Nästa steg
1. Ägaren svarar på frågorna under F-001 och F-002 i `docs/BACKLOG.md`.
2. Bygg första versionen (F-001), sedan publicering (F-002).

## Senaste ändringar
| Datum | Agent | Vad |
|---|---|---|
| 2026-11-26 | Claude | Repot uppsatt enligt agentreglerna v1.14: AGENTS.md, handoff och backlog. F-001 och F-002 inlagda. |
