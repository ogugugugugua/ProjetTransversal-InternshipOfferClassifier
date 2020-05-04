const darkButton = document.getElementById('dark');
const lightButton = document.getElementById('light');
const select = document.getElementById('category-select');
const offerTable = document.querySelectorAll('.crud-table tbody tr');
const body = document.body;
const theme = localStorage.getItem('theme');

if (theme) {
    body.classList.add(theme);

    if (theme === 'dark') {
        body.classList.replace('light', 'dark');
    } else if (theme === 'light') {
        body.classList.replace('dark', 'light');
    }
}

darkButton.onclick = () => {
    body.classList.replace('light', 'dark');
    localStorage.setItem('theme', 'dark');
}

lightButton.onclick = () => {
    body.classList.replace('dark', 'light');
    localStorage.setItem('theme', 'light');
}

const tableChange = () => {
    offerTable.forEach(e => {
        if (select.options[select.selectedIndex].value === 'all') {
            e.style.display = 'table-row';
        } else if (e.children[0].textContent !== select.options[select.selectedIndex].value) {
            e.style.display = 'none';
        } else {
            e.style.display = 'table-row';
        }
    });
}

select.addEventListener('change', tableChange);

tableChange();