import requests

# URL de l'API pour obtenir une blague
url = "https://v2.jokeapi.dev/joke/Any"

# Paramètres de la requête
params = {
    "type": "single"  # Type de blague (une seule ligne)
}

# Faire la requête GET
response = requests.get(url, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    joke_data = response.json()
    if 'joke' in joke_data:
        print("Blague:", joke_data['joke'])
    else:
        print("Erreur: Aucune blague trouvée.")
else:
    print(f"Erreur lors de la requête API : {response.status_code}")
