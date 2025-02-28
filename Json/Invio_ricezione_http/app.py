import flask

import json

from flask import (render_template,request)

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/invio_ricezione_http', methods=['POST'])
def invio_ricezione_http():
    titolo = request.form['titolo']
    anno = request.form['anno']
    scrittore = request.form['scrittore']
    with open('Invio_ricezione_http/data.json', 'w') as file:
        data = {
                "title": titolo,
                "year": anno,
                "author": scrittore
            }
        json.dump(data, file)
    return data

if __name__ == "__main__":
    app.run(debug=True, port=5678)