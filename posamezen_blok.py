import re

posamezen_blok = re.compile(
    r'<td class=.collection_thumbnail.>'
    r'.*?'
    r'<td class=.collection_shop.>',
    flags=re.DOTALL
)

with open('podatki-o-igrah.html', 'r', encoding='utf-8') as f:
    stran = f.read()

bloki = posamezen_blok.findall(stran)

print(f"Število najdenih blokov: {len(bloki)}")