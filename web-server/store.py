import requests

api_url_categories = "https://api.escuelajs.co/api/v1/categories"

def get_categories():
    r = requests.get(api_url_categories)
    print(r.status_code) # respuesta del servidor
    print(r.text) # muestra el contenido de la respuesta del server
    print(type(r.text)) # la respuesta viene como un str
    categories = r.json() # con el metodo .json lo convertimos a un dict

    for categori in categories:
        print(categori["name"])