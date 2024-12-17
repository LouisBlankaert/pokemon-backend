from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Permet les requêtes cross-origin (nécessaire pour la communication avec un frontend)

# URL de l'API Pokémon
POKEMON_API = "https://pokeapi.co/api/v2/pokemon"

# Route pour récupérer une liste de Pokémon avec pagination
@app.route('/', methods=['GET'])
def get_pokemons():
    offset = int(request.args.get('offset', 0))  # Récupérer l'offset, par défaut 0
    limit = int(request.args.get('limit', 12))   # Limite par défaut 12

    response = requests.get(f"{POKEMON_API}?offset={offset}&limit={limit}")

    if response.status_code == 200:
        pokemons = response.json()
        return jsonify(pokemons)
    else:
        return jsonify({"error": "Impossible de charger les Pokémon"}), 500

# Point d'entrée principal
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Récupère le port défini par l'environnement (pour Render)
    app.run(host='0.0.0.0', port=port, debug=False)  # Écoute sur toutes les interfaces
