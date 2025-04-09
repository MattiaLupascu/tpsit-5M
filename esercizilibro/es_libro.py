import json

# Lista da codificare
lista = [1, 2, 3, 'a', 'b', 'c']

# Codifica la lista in formato JSON
json_data = json.dumps(lista)

# Scrittura del JSON in un file
nome_file = 'output.json'
with open(nome_file, 'w') as file_json:
    file_json.write(json_data)

# Lettura del file JSON e decodifica in lista
with open(nome_file, 'r') as file_json:
    lista_decodificata = json.load(file_json)

print("Lista originale:", lista)
print("Lista decodificata:", lista_decodificata)