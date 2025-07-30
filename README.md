# 📖 Scriptura API

<p>
  <img src="https://img.shields.io/badge/Version-v1.0-blue?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/github/license/AlexLamper/bijbel-api?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/github/issues/AlexLamper/bijbel-api?style=for-the-badge" alt="Issues" />
</p>

**A REST API for retrieving Bible texts from multiple Bible translations.**  
Supports various languages including Dutch, English, Afrikaans, and more. Developed for developers, theologians, students, and hobby projects who want to use Biblical texts digitally.

---

## ✨ Features

- 🔀 **Random verses** retrieval  
- 🔍 **Text search** across the entire Bible  
- 📚 **Structure overview** of books, chapters, and verses  
- 📖 **Specific verses or passages** retrieval  
- 📅 **Daily texts** generation (optional with seed)  

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Homepage with API information + link to docs |
| GET | `/random` | Random verse |
| GET | `/verse?book=...&chapter=...&verse=...` | Specific verse |
| GET | `/passage?book=...&chapter=...&start=...&end=...` | Multiple verses |
| GET | `/books` | All books |
| GET | `/chapters?book=...` | Chapters in book |
| GET | `/verses?book=...&chapter=...` | Verse numbers in chapter |
| GET | `/search?query=...` | Search in Bible text |
| GET | `/daytext?seed=...` | Daily text, optional seed |
| GET | `/versions` | Available translations |

👉 All routes are documented via:
- `/docs` – Swagger UI
- `/redoc` – ReDoc UI

---

## 🧩 Expansion

I plan to expand this API further, for example by:
- Adding more Bible translations in various languages.
- Adding additional API endpoints that can be useful.
- Writing better documentation.

---

## 📜 License

This API is licensed under the [MIT License](LICENSE).

---

## 📎 Contact

- GitHub: [@AlexLamper](https://github.com/AlexLamper)
- Mail: `devlamper06@gmail.com`
- Website: [https://www.scriptura-edu.com](https://www.scriptura-edu.com)

---

## 📌 Version

**Current Version**: `v1.0`
