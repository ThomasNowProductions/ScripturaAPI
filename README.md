# Bijbel-API (Statenvertaling)

Dit project biedt een eenvoudige, uitbreidbare API voor de Statenvertaling van de Bijbel, gebouwd met FastAPI.

## Functies
- Geef een willekeurig vers
- Haal specifieke verzen of passages op
- Zoek op tekst in de Bijbel
- Overzicht van boeken, hoofdstukken en verzen
- Genereer een vaste dagtekst
- Ondersteuning voor meerdere vertalingen (uitbreidbaar)

## Projectstructuur
```
.
├── main.py                       ← FastAPI app met API-endpoints
├── data/
│   ├── statenvertaling.txt       ← Ruwe originele tekstbestand (zelf toevoegen)
│   └── statenvertaling.json      ← Geparste JSON-versie van de bijbeltekst
├── utils/
│   └── bible_parser.py           ← (optioneel) parsing-helpers
├── convert_to_json.py            ← Script dat .txt omzet naar .json
├── requirements.txt              ← Python dependencies
└── README.md                     ← Documentatie en uitleg
```

## Installatie & Gebruik
1. **Plaats je `statenvertaling.txt` in de map `data/`.**
2. Installeer de vereisten:
   ```
   pip install -r requirements.txt
   ```
3. Genereer de JSON-database:
   ```
   python convert_to_json.py
   ```
4. Start de API:
   ```
   uvicorn main:app --reload
   ```

## Endpoints
| Endpoint | Beschrijving |
|----------|-------------|
| `/` | Welkomstbericht en verwijzing naar de documentatie |
| `/random` | Één willekeurig vers uit de hele Statenvertaling |
| `/verse?book=...&chapter=...&verse=...` | Haal een specifiek vers op |
| `/passage?book=...&chapter=...&start=...&end=...` | Meerdere verzen uit één hoofdstuk |
| `/books` | Lijst van alle boeken |
| `/chapters?book=...` | Lijst van hoofdstukken voor een boek |
| `/verses?book=...&chapter=...` | Lijst met versnummers in een hoofdstuk |
| `/search?query=...` | Zoek op een woord of zin in alle teksten |
| `/daytext` | Genereert een vaste dagtekst (optioneel: `?seed=...`) |
| `/versions` | Lijst met beschikbare vertalingen (nu: Statenvertaling) |

Alle endpoints zijn gedocumenteerd en direct te testen via `/docs` (Swagger UI) of `/redoc`.

## Uitbreiden
- Voeg extra vertalingen toe door nieuwe .txt/.json bestanden te maken en het datamodel uit te breiden
- Voeg parsing- of zoekhulpmethodes toe in `utils/bible_parser.py`
- Voeg extra endpoints of functionaliteit toe in `main.py`

## Licentie
MIT 