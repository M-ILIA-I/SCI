import random

import requests

url_joke = "https://official-joke-api.appspot.com/random_joke"
res_joke = requests.get(url_joke).json()
joke = res_joke["setup"] + " " + res_joke["punchline"]
print(joke)
