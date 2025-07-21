from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import json
import os
import random
import hashlib
from datetime import date

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from /site
app.mount("/site", StaticFiles(directory="site"), name="site")

# Load and structure the data
def load_data():
    path = os.path.join("data", "statenvertaling.json")
    with open(path, encoding="utf-8") as f:
        raw_data = json.load(f)

    structured_data = {}
    for verse in raw_data["verses"]:
        book = verse["book_name"]
        chapter = str(verse["chapter"])
        verse_number = str(verse["verse"])
        text = verse["text"]

        if book not in structured_data:
            structured_data[book] = {}
        if chapter not in structured_data[book]:
            structured_data[book][chapter] = {}
        structured_data[book][chapter][verse_number] = text

    return structured_data

data = load_data()

# Dummy versions list (extend as needed)
available_versions = ["Statenvertaling"]

# Normalize book names for consistent lookup
def normalize_book_name(book_name):
    for name in data:
        if name.lower().replace("ë", "e") == book_name.lower().replace("ë", "e"):
            return name
    return None

# Serve index.html on /
@app.get("/", response_class=FileResponse)
def serve_index():
    index_path = os.path.join("site", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path, media_type="text/html")
    raise HTTPException(status_code=404, detail="index.html niet gevonden")

@app.get("/api/random")
def get_random_verse():
    book = random.choice(list(data.keys()))
    chapter = random.choice(list(data[book].keys()))
    verse = random.choice(list(data[book][chapter].keys()))
    return {
        "book": book,
        "chapter": chapter,
        "verse": verse,
        "text": data[book][chapter][verse],
    }

@app.get("/api/verse")
def get_verse(book: str, chapter: str, verse: str):
    book_key = normalize_book_name(book)
    if not book_key:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    try:
        text = data[book_key][chapter][verse]
        return {
            "book": book_key,
            "chapter": chapter,
            "verse": verse,
            "text": text,
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Vers niet gevonden")

@app.get("/api/passage")
def get_passage(book: str, chapter: str, start: int, end: int):
    book_key = normalize_book_name(book)
    if not book_key:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    try:
        verses = []
        for i in range(start, end + 1):
            verses.append({"verse": str(i), "text": data[book_key][str(chapter)][str(i)]})
        return {
            "book": book_key,
            "chapter": chapter,
            "verses": verses,
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Passage niet gevonden")

@app.get("/api/books")
def get_books():
    return list(data.keys())

@app.get("/api/chapters")
def get_chapters(book: str):
    book_key = normalize_book_name(book)
    if not book_key:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    return list(data[book_key].keys())

@app.get("/api/verses")
def get_verses(book: str, chapter: str):
    book_key = normalize_book_name(book)
    if not book_key:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    try:
        return list(data[book_key][chapter].keys())
    except KeyError:
        raise HTTPException(status_code=404, detail="Hoofdstuk niet gevonden")

@app.get("/api/search")
def search_verses(query: str = Query(..., min_length=1)):
    results = []
    for book, chapters in data.items():
        for chapter, verses in chapters.items():
            for verse_number, text in verses.items():
                if query.lower() in text.lower():
                    results.append({
                        "book": book,
                        "chapter": chapter,
                        "verse": verse_number,
                        "text": text,
                    })
    return results

@app.get("/api/daytext")
def get_daytext(seed: str = None):
    books = list(data.keys())
    # Use today's date or a seed to get a reproducible random
    base = seed if seed else date.today().isoformat()
    hash_val = int(hashlib.sha256(base.encode()).hexdigest(), 16)
    random.seed(hash_val)
    book = random.choice(books)
    chapter = random.choice(list(data[book].keys()))
    verse = random.choice(list(data[book][chapter].keys()))
    return {
        "book": book,
        "chapter": chapter,
        "verse": verse,
        "text": data[book][chapter][verse],
    }

@app.get("/api/versions")
def get_versions():
    return available_versions

@app.get("/api/chapter")
def get_chapter(book: str, chapter: str):
    book_key = normalize_book_name(book)
    if not book_key:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    try:
        return {
            "book": book_key,
            "chapter": chapter,
            "verses": data[book_key][chapter],
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Hoofdstuk niet gevonden")
