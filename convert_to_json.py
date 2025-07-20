import json
from collections import defaultdict
import re
import os

# Vul deze lijst aan met alle bijbelboeken uit jouw tekst, exact dezelfde spelling
bijbel_boeken = [
    "Genesis", "Éxodus", "Leviticus", "Numeri", "Deuteronomium",
    "Jozua", "Richteren", "1 Samuël", "2 Samuël", "1 Koningen", "2 Koningen",
    "Jesaja", "Jeremia", "Ezechiël", "Hoséa", "Joël", "Amos", "Obadja", "Jona",
    "Micha", "Nahum", "Habakuk", "Zefanja", "Haggaï", "Zacharia", "Maleachi",
    "Psalmen", "Spreuken", "Job", "Hooglied", "Ruth", "Klaagliederen", "Prediker",
    "Esther", "Daniël", "Ezra", "Nehemia", "1 Kronieken", "2 Kronieken",
    "Matthéüs", "Markus", "Lukas", "Johannes", "Handelinge", "Romeinen",
    "1 Korinthe", "2 Korinthe", "Galaten", "Éfeze", "Filippenzen", "Kolossenzen",
    "1 Thessalonicenzen", "2 Thessalonicenzen", "1 Timótheüs", "2 Timótheüs",
    "Titus", "Filémon", "Hebreën", "Jakobus", "1 Petrus", "2 Petrus",
    "1 Johannes", "2 Johannes", "3 Johannes", "Judas", "Openbaring"
]

bijbel = defaultdict(lambda: defaultdict(dict))

current_book = None
current_chapter = None
current_verse = None
buffer_tekst = []

def save_verse():
    global current_book, current_chapter, current_verse, buffer_tekst
    if current_book and current_chapter and current_verse and buffer_tekst:
        tekst = " ".join(buffer_tekst).strip()
        bijbel[current_book][str(current_chapter)][str(current_verse)] = tekst
        buffer_tekst = []

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
TXT_PATH = os.path.join(DATA_DIR, "statenvertaling.txt")
JSON_PATH = os.path.join(DATA_DIR, "statenvertaling.json")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    for raw_line in f:
        line = raw_line.strip()
        if not line:
            continue

        # Detecteer boek
        if line in bijbel_boeken:
            save_verse()
            current_book = line
            current_chapter = None
            current_verse = None
            buffer_tekst = []
            continue

        # Detecteer hoofdstuk: regel met alleen een getal
        if re.fullmatch(r"\d+", line):
            save_verse()
            current_chapter = int(line)
            current_verse = None
            buffer_tekst = []
            continue

        # Detecteer versregel: begint met nummer + spatie + tekst
        match = re.match(r"^(\d+)\s+(.*)", line)
        if match:
            save_verse()
            current_verse = int(match.group(1))
            buffer_tekst = [match.group(2)]
            continue

        # Regels die bij het huidige vers horen (multiline vers)
        if current_verse is not None:
            buffer_tekst.append(line)

save_verse()

with open(JSON_PATH, "w", encoding="utf-8") as out:
    json.dump({"Statenvertaling": bijbel}, out, indent=2, ensure_ascii=False)

print("✅ statenvertaling.json is klaar.") 