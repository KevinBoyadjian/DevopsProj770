#Importe les modules nécessaires
import json
import random
from flask import Flask, render_template, request

#Crée l'application Flask (c'est l'objet principal)
app = Flask(__name__)

# Chemin vers le fichier JSON (ajuste si tu as mis data/ ou pas)
QUOTES_FILE = 'data/Rabbiquotes.json'

# Fonction pour charger toutes les citations depuis le JSON
def load_quotes():
    try:
        with open (QUOTES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Route principale : page d'accueil    
@app.route('/', methods=['GET'])
def index():
    quotes = load_quotes()
    print("Nombre de citations chargées :", len(quotes))  # ← ajoute ça
    if quotes:
        print("Exemple de première citation :", quotes[0])  # ← ajoute ça
    if not quotes:
        quote = None
    else:
        # Choisit une citation au hasard
        quote = random.choice(quotes)
    
    # On envoie la variable 'quote' au template HTML
    return render_template('index.html', quote=quote)

# Lancement de l'application (seulement si on lance directement ce fichier)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)