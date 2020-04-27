from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re


def parse_price(sku=None):
    sku = input('Entrez l\'id du produit : ')
    path = 'https://www.cdiscount.com/f-0-' + sku + '.html'
    with urllib.request.urlopen(path) as resp:
        data = resp.read()
        lien = r'<link rel="canonical" href="https://www.cdiscount.com/" />'
        if re.findall(lien, str(data)):
            print('Cet id n\'est pas référencé')
            return parse_price()
        else:
            soup = BeautifulSoup(data, 'html.parser')
            prixClasse = 'fpPrice price jsMainPrice jsProductPrice hideFromPro'
            prix = soup.find_all('span', {'class': prixClasse})
            prixData = float(re.findall(r'content="(.*?)"', str(prix))[0])
            return f"{prixData}"
