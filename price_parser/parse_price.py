from bs4 import BeautifulSoup
import urllib.request
import re


def sku_to_price():
    name = input("Entrez l'id du produit : ")
    sku(name)
    

def sku(name):
    path = 'https://www.cdiscount.com/f-0-' + name + '.html'
    with urllib.request.urlopen(path) as resp:
        data = resp.read()
        lien = r'<link rel="canonical" href="https://www.cdiscount.com/" />'
        if re.findall(lien, str(data)):
            print("Cet id n'est pas référencé.")
        else:
            price(data)


def price(data):
    soup = BeautifulSoup(data, 'html.parser')
    prixClasse = 'fpPrice price jsMainPrice jsProductPrice hideFromPro'
    prix = soup.find_all('span', {'class': prixClasse})
    prixData = float(re.findall(r'content="(.*?)"', str(prix))[0])
    return print(prixData)
