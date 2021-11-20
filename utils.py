import requests

def get_google_suggestions(kw):
    url = f'https://www.google.com/complete/search?client=firefox&q={kw}'
    response = requests.get(url)
    data = response.json()
    suggestions = data[1]
    return suggestions

def get_amazon_suggestions(kw):
    url = f'https://completion.amazon.com/api/2017/suggestions?session-id=132-9553966-7632905&customer-id=A3V141IASC13KS&request-id=0FR95W9VHVCJWA8EJPER&page-type=Gateway&lop=es_US&site-variant=desktop&client-info=amazon-search-ui&mid=ATVPDKIKX0DER&alias=aps&ks=undefined&prefix={kw}&event=onFocusWithSearchTerm&limit=11&b2b=0&fresh=0&fb=1&suggestion-type=KEYWORD&suggestion-type=WIDGET&_=1637420187493'
    response = requests.get(url)
    data = response.json()
    suggestions = [x['value'] for x in data['suggestions']]
    return suggestions
