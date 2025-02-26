import json

# Open and read the JSON file
with open('Json/data.json', 'r') as file:
    data = json.load(file)

# Print the data
print(data)

with open('Json/data.json', 'w') as file:
    data = {
    "books": [
        {
            "title": "Il nome della rosa",
            "author": "Umberto Eco",
            "year": 1980
        },
        {
            "title": "Il signore degli anelli",
            "author": "J.R.R. Tolkien",
            "year": 1954
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "year": 1949
        }
    ]
}
    json.dump(data, file)