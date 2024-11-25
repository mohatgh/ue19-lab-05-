import requests

def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data.get("type") == "single":
            return joke_data.get("joke")
        else:
            return f"{joke_data.get('setup')} - {joke_data.get('delivery')}"
    else:
        return "Failed to retrieve a joke"

if __name__ == "__main__":
    print("Fetching a random joke from JokeAPI...\n")
    print(fetch_joke())

