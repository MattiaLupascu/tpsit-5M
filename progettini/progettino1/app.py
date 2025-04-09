from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista di auto usate (simulazione di un database)
macchine_usate = [
    {"marca": "Toyota", "modello": "Corolla", "alimentazione": "Benzina", "colore": "Blu"},
    {"marca": "Ford", "modello": "Focus", "alimentazione": "Diesel", "colore": "Grigio"},
    {"marca": "Volkswagen", "modello": "Golf", "alimentazione": "Elettrica", "colore": "Bianco"},
    {"marca": "Fiat", "modello": "500", "alimentazione": "Benzina", "colore": "Rosso"},
    {"marca": "Tesla", "modello": "Model 3", "alimentazione": "Elettrica", "colore": "Nero"},
    {"marca": "Audi", "modello": "A4", "alimentazione": "Diesel", "colore": "Argento"},
    {"marca": "BMW", "modello": "Serie 3", "alimentazione": "Diesel", "colore": "Blu"},
    {"marca": "Mercedes", "modello": "Classe C", "alimentazione": "Benzina", "colore": "Nero"},
    {"marca": "Peugeot", "modello": "308", "alimentazione": "Diesel", "colore": "Bianco"},
    {"marca": "Renault", "modello": "Clio", "alimentazione": "Benzina", "colore": "Giallo"},
    {"marca": "Opel", "modello": "Corsa", "alimentazione": "GPL", "colore": "Verde"},
    {"marca": "Hyundai", "modello": "i30", "alimentazione": "Ibrida", "colore": "Argento"},
    {"marca": "Kia", "modello": "Sportage", "alimentazione": "Diesel", "colore": "Rosso"},
    {"marca": "Seat", "modello": "Leon", "alimentazione": "Metano", "colore": "Arancione"},
    {"marca": "Mazda", "modello": "CX-5", "alimentazione": "Benzina", "colore": "Marrone"},
    {"marca": "Nissan", "modello": "Qashqai", "alimentazione": "Diesel", "colore": "Grigio"},
    {"marca": "Honda", "modello": "Civic", "alimentazione": "Ibrida", "colore": "Azzurro"}
]

@app.route('/')
def index():
    return render_template('index.html', macchine_usate=macchine_usate)

@app.route('/filter', methods=['POST'])
def filter_cars():
    filtro = request.json
    macchine_filtrate = [
        macchina for macchina in macchine_usate
        if (filtro.get('marca', '').lower() in macchina['marca'].lower()) and
           (filtro.get('alimentazione', '').lower() in macchina['alimentazione'].lower()) and
           (filtro.get('colore', '').lower() in macchina['colore'].lower())
    ]
    return jsonify(macchine_filtrate)

if __name__ == '__main__':
    app.run(debug=True,port=64001)