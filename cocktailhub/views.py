import urllib.request
import json
from django.shortcuts import render

def index(request):
    query = request.GET.get('query', '').strip()
    results = []

    if query:
        api_url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}"
        try:
            with urllib.request.urlopen(api_url) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    results = data.get('drinks', [])
        except:
            results = []

    return render(request, 'index.html', {
        'results': results,
        'query': query,
    })


def detail(request, detail):  # detail is the drink ID from the URL
    api_url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={detail}"
    drink = None
    ingredients = []

    try:
        with urllib.request.urlopen(api_url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                drinks = data.get('drinks')
                if drinks:
                    drink = drinks[0]
                    for i in range(1, 4):
                        ing = drink.get(f'strIngredient{i}')
                        measure = drink.get(f'strMeasure{i}')
                        if ing:
                            ingredients.append(f"{ing} — {measure or ''}")
    except:
        pass

    return render(request, 'detail.html', {
        'drink': drink,
        'ingredients': ingredients,
    })
