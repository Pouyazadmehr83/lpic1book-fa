// Theme Toggle & Persistence
function initTheme() {
    const savedTheme = localStorage.getItem('lpic_theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
}

function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || 'light';
    const next = current === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('lpic_theme', next);
}

// Mobile Sidebar Toggle
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar) {
        sidebar.classList.toggle('open');
    }
}

// Copy Code Button
function copyCode(btn) {
    const pre = btn.closest('.code-wrapper').querySelector('pre');
    if (!pre) return;
    const text = pre.innerText;
    
    navigator.clipboard.writeText(text).then(() => {
        const orig = btn.innerText;
        btn.innerText = 'کپی شد! ✓';
        btn.style.background = '#10b981';
        btn.style.color = '#fff';
        setTimeout(() => {
            btn.innerText = orig;
            btn.style.background = '';
            btn.style.color = '';
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}

// Search Functionality
let searchData = [];

async function loadSearchData() {
    if (searchData.length === 0) {
        try {
            const res = await fetch('./search_index.json');
            searchData = await res.json();
        } catch (e) {
            console.error('Could not load search index', e);
        }
    }
}

function openSearchModal() {
    loadSearchData();
    const modal = document.getElementById('searchModal');
    if (modal) {
        modal.classList.add('open');
        const input = document.getElementById('searchInput');
        if (input) {
            input.value = '';
            input.focus();
            handleSearch('');
        }
    }
}

function closeSearchModal(event, force) {
    const modal = document.getElementById('searchModal');
    if (!modal) return;
    if (force || (event && event.target === modal)) {
        modal.classList.remove('open');
    }
}

function handleSearch(query) {
    const resultsContainer = document.getElementById('searchResults');
    if (!resultsContainer) return;
    
    const q = query.trim().toLowerCase();
    if (!q) {
        resultsContainer.innerHTML = '<div style="padding: 1rem; color: var(--text-muted); text-align: center;">عنوان درس یا اصطلاح مورد نظر خود را تایپ کنید...</div>';
        return;
    }

    const matches = searchData.filter(item => {
        return item.title.toLowerCase().includes(q) || 
               item.group.toLowerCase().includes(q) ||
               item.exam.toLowerCase().includes(q);
    });

    if (matches.length === 0) {
        resultsContainer.innerHTML = '<div style="padding: 1rem; color: var(--text-muted); text-align: center;">هیچ درسی پیدا نشد.</div>';
        return;
    }

    resultsContainer.innerHTML = matches.map(item => `
        <a href="${item.url}" class="search-result-item">
            <div class="search-result-title">${item.title}</div>
            <div class="search-result-group">${item.exam} • ${item.group}</div>
        </a>
    `).join('');
}

// Keyboard shortcuts: '/' to search, 'Esc' to close
document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        openSearchModal();
    }
    if (e.key === 'Escape') {
        closeSearchModal(null, true);
    }
});

// Run theme init on load
initTheme();
