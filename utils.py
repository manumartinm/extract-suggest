import requests

def get_google_suggestions(kw):
    url = f'https://www.google.com/complete/search?client=firefox&q={kw}'
    response = requests.get(url)
    data = response.json()
    suggestions = data[1]
    return suggestions
