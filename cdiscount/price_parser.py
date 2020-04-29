from bs4 import BeautifulSoup
import urllib.request
import re


def parse_price(sku):

    with urllib.request.urlopen('https://www.cdiscount.com/f-0-' + sku + '.html') as resp:

        lien = r'<link rel="canonical" href="https://www.cdiscount.com/" />'
        data = resp.read()

        if re.findall(lien, str(data)):
            return False

        else:
            soup = BeautifulSoup(data, 'html.parser')
            classe = 'fpPrice price jsMainPrice jsProductPrice hideFromPro'
            prix = float(re.findall(
                r'content="(.*?)"', str(soup.find_all('span', {'class': classe})))[0])
            return prix
