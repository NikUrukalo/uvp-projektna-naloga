import re

posamezen_blok = re.compile(
    r"<tr id='row_'>.*?<td class='collection_shop'>",
    flags=re.DOTALL
)

with open('podatki-o-igrah.html', 'r', encoding='utf-8') as f:
    stran = f.read()

bloki = posamezen_blok.findall(stran)

print(f"Število najdenih blokov: {len(bloki)}")

posamezna_igra = re.compile(
    r'<a name="(?P<rang>\d+)"></a>.*?'
    r'alt="Board Game: (?P<ime>.*?)".*?'
    r'<span class=\'smallerfont dull\'>\((?P<leto>\d{4})\)</span>.*?'
    r'<p class="smallefont dull".*?>(?P<opis>.*?)</p>.*?'
    r'<td class=\'collection_bggrating\' align=\'center\'>\s*(?P<ocena_strani>\d+\.\d+)\s*</td>.*?'
    r'<td class=\'collection_bggrating\' align=\'center\'>\s*(?P<povprecna_ocena>\d+\.\d+)\s*</td>.*?'
    r'<td class=\'collection_bggrating\' align=\'center\'>\s*(?P<stevilo_glasov>\d+)\s*</td>',
    flags=re.DOTALL
)

def izloci_podatke_igre(blok):
    igra = posamezna_igra.search(blok).groupdict()
    igra['rang'] = int(igra['rang'])
    igra['ime'] = igra['ime'].strip()
    igra['leto'] = int(igra['leto'])
    igra['opis'] = re.sub(r'\s+', ' ', igra['opis']).strip()
    igra['ocena_strani'] = float(igra['ocena_strani'])
    igra['povprecna_ocena'] = float(igra['povprecna_ocena'])
    igra['stevilo_glasov'] = int(igra['stevilo_glasov'])
    return igra

for blok in bloki:
    podatki_igre = izloci_podatke_igre(blok)
    print(podatki_igre)