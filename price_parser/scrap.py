from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re


def user_input():
    sku = input('Entrez l\'id du produit : ')
    product_scanner(sku)


def product_scanner(sku):
    path = 'https://www.cdiscount.com/f-0-' + sku + '.html'
    with urllib.request.urlopen(path) as resp:
        data = resp.read()
        lien = r'<link rel="canonical" href="https://www.cdiscount.com/" />'
        if re.findall(lien, str(data)):
            print('Cet id n\'est pas référencé')
            user_input()
        else:
            parse_price(data)


def parse_price(data):
    soup = BeautifulSoup(data, 'html.parser')
    prixClasse = 'fpPrice price jsMainPrice jsProductPrice hideFromPro'
    prix = soup.find_all('span', {'class': prixClasse})
    prixData = float(re.findall(r'content="(.*?)"', str(prix))[0])
    print(prixData)


user_input()
