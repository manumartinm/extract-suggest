import requests

def get_google_suggestions(kw):
    url = f'https://www.google.com/complete/search?client=firefox&q={kw}'
    response = requests.get(url)
    data = response.json()
    suggestions = data[1]
    return suggestions

def get_amazon_suggestions(kw):
    url = f'https://completion.amazon.com/api/2017/suggestions?lop=es&mid=ATVPDKIKX0DER&alias=aps&prefix={kw}&suggestion-type=KEYWORD&suggestion-type=WIDGET'
    response = requests.get(url)
    data = response.json()
    suggestions = [x['value'] for x in data['suggestions']]
    return suggestions
