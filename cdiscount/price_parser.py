from bs4 import BeautifulSoup
import urllib.request
import re


def parse_price():
    name = input("Entrez l'id du produit : ")

    with urllib.request.urlopen('https://www.cdiscount.com/f-0-' + name + '.html') as resp:

        data = resp.read()
        lien = r'<link rel="canonical" href="https://www.cdiscount.com/" />'

        if re.findall(lien, str(data)):
            print("Cet id n'est pas référencé.")
            return parse_price()

        else:
            soup = BeautifulSoup(data, 'html.parser')
            prixClasse = 'fpPrice price jsMainPrice jsProductPrice hideFromPro'
            prixData = float(re.findall(
                r'content="(.*?)"', str(soup.find_all('span', {'class': prixClasse})))[0])
            print(prixData)
