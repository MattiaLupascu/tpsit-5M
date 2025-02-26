const fs = require('fs');

// Leggi il file JSON
const data = require('./data.json');
console.log('Dati esistenti:', data);

// Nuovi dati da aggiungere
const newBook = {
    "title": "Il piccolo principe",
    "author": "Antoine de Saint-Exupéry",
    "year": 1943
};

// Aggiungi il nuovo libro ai dati esistenti
data.books.push(newBook);

// Scrivi i dati aggiornati nel file JSON
fs.writeFile('./data.json', JSON.stringify(data, null, 4), (err) => {
    if (err) {
        console.error('Errore durante la scrittura del file JSON:', err);
    } else {
        console.log('Dati aggiornati con successo:', data);
    }
});