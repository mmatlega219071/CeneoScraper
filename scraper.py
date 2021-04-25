import requests

response = requests.get('https://www.ceneo.pl/7199209#tab=reviews')

print(response.text)