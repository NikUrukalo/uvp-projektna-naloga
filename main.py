import csv
import json
import os
import requests
import sys
import json


def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)


def shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False):
    '''Vsebino strani na danem naslovu shrani v datoteko z danim imenom.'''
    try:
        print(f'Shranjujem {url} ...', end='')
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke) and not vsili_prenos:
            print('shranjeno že od prej')
            return
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja')
    else:
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')


if not os.path.exists('igre'):
    print("Imenik 'igre' ne obstaja.")
else:
    print("Imenik obstaja in vsebuje:", os.listdir('igre'))

for i in range(1, 11):
    if i == 1:
        url = 'https://boardgamegeek.com/browse/boardgame/page/1'
    else:
        url = f'https://boardgamegeek.com/browse/boardgame/page/{i}'
    
    ime_datoteke = os.path.join('igre', f'igre{i}.html')

    shrani_spletno_stran(url, ime_datoteke)

                

from izlusci_igro import izloci_podatke_igre, posamezni_blok

igre = []
count = 0
for i in range (1, 11):
    ime_datoteke = os.path.join('igre', f'igre{i}.html')
    with open(ime_datoteke, encoding='utf-8') as f:
        vsebina = f.read()
    for blok in posamezni_blok.finditer(vsebina):
        igra = izloci_podatke_igre(blok.group(0))
        count += 1
        igre.append(igra)
print(count)



def zapisi_json(objekt, ime_datoteke):
    '''Iz danega objekta ustvari JSON datoteko.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as json_datoteka:
        json.dump(objekt, json_datoteka, indent=4, ensure_ascii=False)

zapisi_json(igre, "igre.json")

def zapisi_csv(slovarji, imena_polj, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        writer.writerows(slovarji)

imena_polj = ['rang', 'ime', 'leto', 'opis', 'ocena_strani', 'povprecna_ocena', 'stevilo_glasov']

zapisi_csv(igre, imena_polj, 'igre.csv')