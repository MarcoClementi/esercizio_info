import requests
from bs4 import BeautifulSoup
import webbrowser

link = "https://www.subito.it/annunci-emilia-romagna/vendita/sport/?q=wing%20foil"
pre_link_annuncio = "https://www.subito.it/sport/"

response = requests.get(link)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
div_annunci = soup.find('div', class_='ListingContainer_col__1TZpb ListingContainer_items__3lMdo col items')
trova_annunci = div_annunci.find_all('a')
link_annunci = []
for trova_annunci in trova_annunci:
    link_annuncio = str(trova_annunci.get('href'))
    if pre_link_annuncio in link_annuncio:
        link_annunci.append(link_annuncio)

#from pprint import pprint
#pprint(link_annunci)

f = open('risultati_salvati.txt','a')
vecchio_link_annunci = [riga.rstrip('/n') for riga in open('risultati_salvati.txt') ]
nuovi_link_annunci = []
for link_annuncio in link_annunci:
    if link_annuncio not in vecchio_link_annunci:
        nuovi_link_annunci.append(link_annuncio)
        f.write('%s/n' % link_annuncio)
f.close()
if nuovi_link_annunci:
    print("Ci sono nuovi risultati apertura in corso ...")
    for nuovi_link_annunci in link_annunci:
        webbrowser.open(nuovi_link_annunci)
else:
    print('nessun nuovo annuncio')
input('/n tutto bene')
