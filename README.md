# 📖 Bijbel API

<p>
  <img src="https://img.shields.io/badge/Version-v1.0-blue?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/github/license/AlexLamper/bijbel-api?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/github/issues/AlexLamper/bijbel-api?style=for-the-badge" alt="Issues" />
</p>

**Een REST API voor het opvragen van bijbelteksten uit Nederlandse bijbelvertalingen.**  
Ontwikkeld voor developers, theologen, studenten en hobbyprojecten die Bijbelse teksten digitaal willen gebruiken.

---

## ✨ Features

- 🔀 **Willekeurige verzen** opvragen  
- 🔍 **Zoeken op tekst** in de gehele Bijbel  
- 📚 **Structuur-overzicht** van boeken, hoofdstukken en verzen  
- 📖 **Specifieke verzen of passages** ophalen  
- 📅 **Dagteksten** genereren (optioneel met seed)  

---

## 🌐 API Endpoints

| Methode | Endpoint | Beschrijving |
|--------|----------|--------------|
| GET | `/` | Homepagina met informatie over de API + link naar docs |
| GET | `/random` | Willekeurig vers |
| GET | `/verse?book=...&chapter=...&verse=...` | Specifiek vers |
| GET | `/passage?book=...&chapter=...&start=...&end=...` | Meerdere verzen |
| GET | `/books` | Alle boeken |
| GET | `/chapters?book=...` | Hoofdstukken in boek |
| GET | `/verses?book=...&chapter=...` | Versnummers in hoofdstuk |
| GET | `/search?query=...` | Zoek in bijbeltekst |
| GET | `/daytext?seed=...` | Dagtekst, optioneel seed |
| GET | `/versions` | Beschikbare vertalingen |

👉 Alle routes zijn gedocumenteerd via:
- `/docs` – Swagger UI
- `/redoc` – ReDoc UI

---

## 🧩 Uitbreiden

Ik ben van plan deze API nog uit te breiden, bijvoorbeeld door:
- Meer Nederlandstalige bijbelvertalingen toe te voegen.
- Extra API endpoints toe te voegen die handig kunnen zijn.
- Betere documentatie schrijven.

---

## 📜 License

Deze API valt onder de [MIT License](LICENSE).

---

## 📎 Contact

- GitHub: [@AlexLamper](https://github.com/AlexLamper)
- Mail: `devlamper06@gmail.com`
- Website: [https://bijbel-api.nl](https://bijbel-api.nl)

---

## 📌 Versie

**Current Version**: `v1.0`
