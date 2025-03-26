from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista di esempio di nomi
nomi = ["Alice", "Bob", "Carlo", "Davide", "Eva", "Francesco", "Giulia", "Hannah"]

@app.route('/')
def indice():
    return render_template('index.html')

@app.route('/ottieni_nomi', methods=['GET'])
def ottieni_nomi():
    ricerca = request.args.get('query', '').lower()
    nomi_filtrati = [nome for nome in nomi if nome.lower().startswith(ricerca)]
    return jsonify(nomi_filtrati)

if __name__ == '__main__':
    app.run(debug=True, port=60000)