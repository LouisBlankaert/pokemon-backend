from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

pokemon_api = "https://pokeapi.co/api/v2/pokemon"

# Route pour récupérer une liste de Pokémon avec pagination
@app.route('/api/pokemon', methods=['GET'])
def get_pokemons():
    offset = int(request.args.get('offset', 0))  # Récupérer l'offset, par défaut 0
    limit = int(request.args.get('limit', 12))   # Limite par défaut 12
    response = requests.get(f"{pokemon_api}?offset={offset}&limit={limit}")

    if response.status_code == 200:
        pokemons = response.json()
        return jsonify(pokemons)
    else:
        return jsonify({"error": "Impossible de charger les Pokémon"}), 500

if __name__ == '__main__':
    app.run(debug=True)
