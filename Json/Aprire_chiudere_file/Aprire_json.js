const fs = require('fs');

// Leggi e mostra i dati esistenti
fs.readFile("data.json", (error, data) => {
  if (error) {
    console.error(error);
    throw error;
  }
  console.log(JSON.parse(data));
});

// Nuovi dati da aggiungere
const newBook = {
  "title": "Il piccolo principe",
  "author": "Antoine de Saint-Exupéry",
  "year": 1943
};

// Sovrascrivi il file con i nuovi dati
fs.writeFile("data.json", JSON.stringify(newBook), (error) => {
  if (error) {
    console.error('Errore durante la scrittura del file JSON:', error);
  } else {
    console.log('Dati aggiornati con successo:', newBook);
  }
});