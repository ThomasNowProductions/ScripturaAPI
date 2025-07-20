from fastapi import FastAPI, Query, HTTPException
import json, random
import os
from typing import List
from fastapi.staticfiles import StaticFiles

app = FastAPI()

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "statenvertaling.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)["Statenvertaling"]

app.mount("/site", StaticFiles(directory="site", html=True), name="site")

@app.get("/")
def root():
    return {"message": "Welkom bij de Bijbel-API! Zie /docs voor documentatie."}

@app.get("/random")
def get_random_verse():
    boek = random.choice(list(data.keys()))
    hoofdstuk = random.choice(list(data[boek].keys()))
    vers = random.choice(list(data[boek][hoofdstuk].keys()))
    tekst = data[boek][hoofdstuk][vers]
    return {"book": boek, "chapter": hoofdstuk, "verse": vers, "text": tekst}

@app.get("/verse", summary="Haal een specifiek vers op", description="Geef boek, hoofdstuk en versnummer op.")
def get_verse(book: str = Query(..., description="Naam van het bijbelboek"),
              chapter: int = Query(..., description="Hoofdstuknummer"),
              verse: int = Query(..., description="Versnummer")):
    try:
        tekst = data[book][str(chapter)][str(verse)]
    except KeyError:
        raise HTTPException(status_code=404, detail="Vers niet gevonden")
    return {"book": book, "chapter": chapter, "verse": verse, "text": tekst}

@app.get("/passage")
def get_passage(book: str, chapter: int, start: int, end: int):
    try:
        verzen = {
            str(v): data[book][str(chapter)][str(v)]
            for v in range(start, end + 1)
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Passage niet gevonden")
    return {"book": book, "chapter": chapter, "verses": verzen}

@app.get("/books")
def get_books():
    return list(data.keys())

@app.get("/chapters")
def get_chapters(book: str):
    try:
        hoofdstukken = list(data[book].keys())
    except KeyError:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    return {"book": book, "chapters": hoofdstukken}

@app.get("/verses")
def get_verses(book: str, chapter: int):
    try:
        verzen = list(data[book][str(chapter)].keys())
    except KeyError:
        raise HTTPException(status_code=404, detail="Hoofdstuk niet gevonden")
    return {"book": book, "chapter": chapter, "verses": verzen}

@app.get("/search", summary="Zoek in de bijbeltekst", description="Zoek naar verzen die een bepaalde tekst bevatten.")
def search_verses(query: str) -> dict:
    results: List[dict] = []
    for boek, hoofdstukken in data.items():
        for hoofdstuk, verzen in hoofdstukken.items():
            for vers, tekst in verzen.items():
                if query.lower() in tekst.lower():
                    results.append({
                        "book": boek,
                        "chapter": hoofdstuk,
                        "verse": vers,
                        "text": tekst
                    })
    return {"results": results}

@app.get("/daytext", summary="Genereer een vaste dagtekst", description="Genereert een dagtekst op basis van de dag of een optionele seed.")
def daytext(seed: int = None):
    import datetime
    import hashlib
    if seed is None:
        # Gebruik de huidige datum als seed (YYYYMMDD)
        today = datetime.date.today().strftime("%Y%m%d")
        seed = int(hashlib.sha256(today.encode()).hexdigest(), 16) % (10 ** 8)
    rng = random.Random(seed)
    boek = rng.choice(list(data.keys()))
    hoofdstuk = rng.choice(list(data[boek].keys()))
    vers = rng.choice(list(data[boek][hoofdstuk].keys()))
    tekst = data[boek][hoofdstuk][vers]
    return {"book": boek, "chapter": hoofdstuk, "verse": vers, "text": tekst, "seed": seed}

@app.get("/versions", summary="Beschikbare vertalingen", description="Geeft een lijst van beschikbare bijbelvertalingen.")
def get_versions():
    # In de toekomst uitbreidbaar, nu alleen Statenvertaling
    return {"versions": ["Statenvertaling"]}

@app.get("/chapter", summary="Geef alle verzen van een hoofdstuk", description="Geeft alle verzen van een opgegeven boek en hoofdstuk.")
def get_chapter(book: str, chapter: int):
    try:
        verzen = data[book][str(chapter)]
    except KeyError:
        raise HTTPException(status_code=404, detail="Hoofdstuk niet gevonden")
    return {"book": book, "chapter": chapter, "verses": verzen}