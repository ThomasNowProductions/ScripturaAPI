// Zoek een specifiek vers
const verseForm = document.getElementById('verseForm');
const verseResult = document.getElementById('verseResult');
verseForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    verseResult.textContent = 'Bezig met zoeken...';
    const book = document.getElementById('book').value;
    const chapter = document.getElementById('chapter').value;
    const verse = document.getElementById('verse').value;
    try {
        const res = await fetch(`/verse?book=${encodeURIComponent(book)}&chapter=${chapter}&verse=${verse}`);
        if (!res.ok) throw new Error('Niet gevonden of fout in API');
        const data = await res.json();
        verseResult.innerHTML = `<b>${data.book} ${data.chapter}:${data.verse}</b><br>${data.text}`;
    } catch (err) {
        verseResult.textContent = 'Kon vers niet ophalen. Controleer je invoer.';
    }
});

// Dagtekst ophalen
const daytextBtn = document.getElementById('getDaytext');
const daytextResult = document.getElementById('daytextResult');
daytextBtn.addEventListener('click', async () => {
    daytextResult.textContent = 'Bezig met ophalen...';
    try {
        const res = await fetch('/daytext');
        if (!res.ok) throw new Error('Fout in API');
        const data = await res.json();
        daytextResult.innerHTML = `<b>${data.book} ${data.chapter}:${data.verse}</b><br>${data.text}`;
    } catch (err) {
        daytextResult.textContent = 'Kon dagtekst niet ophalen.';
    }
});

// Laad boekenlijst in dropdown voor hoofdstuk zoeken
async function loadBooksDropdown() {
    const select = document.getElementById('bookChapterSelect');
    select.innerHTML = '<option value="">Laden...</option>';
    try {
        const res = await fetch('/books');
        const books = await res.json();
        select.innerHTML = books.map(book => `<option value="${book}">${book}</option>`).join('');
    } catch {
        select.innerHTML = '<option>Fout bij laden</option>';
    }
}
if (document.getElementById('bookChapterSelect')) loadBooksDropdown();

// Hoofdstuk zoeken
const chapterForm = document.getElementById('chapterForm');
const chapterResult = document.getElementById('chapterResult');
if (chapterForm) {
    chapterForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        chapterResult.textContent = 'Bezig met laden...';
        const book = document.getElementById('bookChapterSelect').value;
        const chapter = document.getElementById('chapterNum').value;
        try {
            const res = await fetch(`/chapter?book=${encodeURIComponent(book)}&chapter=${chapter}`);
            if (!res.ok) throw new Error('Niet gevonden of fout in API');
            const data = await res.json();
            let html = `<b>${data.book} ${data.chapter}</b><br>`;
            html += '<div class="card">';
            for (const [vers, tekst] of Object.entries(data.verses)) {
                html += `<b>${vers}</b> ${tekst}<br>`;
            }
            html += '</div>';
            chapterResult.innerHTML = html;
        } catch (err) {
            chapterResult.textContent = 'Kon hoofdstuk niet ophalen. Controleer je invoer.';
        }
    });
}

// Kopieerknoppen voor API endpoints
function setupCopyButtons() {
    const btns = document.querySelectorAll('.copy-btn');
    btns.forEach(btn => {
        btn.addEventListener('click', () => {
            const url = btn.getAttribute('data-url');
            navigator.clipboard.writeText(url);
            btn.textContent = 'Gekopieerd!';
            btn.classList.add('copied');
            setTimeout(() => {
                btn.textContent = 'Kopieer';
                btn.classList.remove('copied');
            }, 1200);
        });
    });
}
setupCopyButtons();
// Herhaal na dynamische updates indien nodig 