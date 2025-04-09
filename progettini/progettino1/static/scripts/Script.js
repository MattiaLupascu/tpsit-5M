document.getElementById('filter-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const marca = document.getElementById('marca').value;
    const alimentazione = document.getElementById('alimentazione').value;
    const colore = document.getElementById('colore').value;

    fetch('/filter', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ marca, alimentazione, colore }),
    })
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('car-table-body');
            tableBody.innerHTML = '';

            if (data.length > 0) {
                data.forEach(macchina => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${macchina.marca}</td>
                        <td>${macchina.modello}</td>
                        <td>${macchina.alimentazione}</td>
                        <td>${macchina.colore}</td>
                    `;
                    tableBody.appendChild(row);
                });
            } else {
                const row = document.createElement('tr');
                row.innerHTML = `<td colspan="4" class="text-center">Nessuna macchina disponibile</td>`;
                tableBody.appendChild(row);
            }
        })
        .catch(error => console.error('Errore:', error));
});