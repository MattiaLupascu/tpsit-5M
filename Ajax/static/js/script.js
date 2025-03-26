function filtraNomi() {
    const ricerca = document.getElementById('inputNome').value.trim();
    const listaNomi = document.getElementById('listaNomi');
    
    if (ricerca.length === 0) {
        listaNomi.innerHTML = '<p>Scrivi una lettera</p>';
        return;
    }
    
    fetch(`/ottieni_nomi?query=${ricerca}`)
        .then(risposta => risposta.json())
        .then(dati => {
            listaNomi.innerHTML = '';
            
            if (dati.length === 0) {
                listaNomi.innerHTML = '<p>Nessun risultato trovato</p>';
                return;
            }
            
            dati.forEach(nome => {
                listaNomi.innerHTML += `<div>${nome}</div>`;
            });
        })
        .catch(errore => {
            console.error('Errore:', errore);
            listaNomi.innerHTML = '<p>Errore nel recuperare i dati</p>';
        });
}

// Permette di premere Invio per cercare
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('inputNome').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') filtraNomi();
    });
});