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

posamezna_igra = re.compile(
    r'<a name=.(?P<rang>\d+.)></a>'
    r'alt=.Board Game: (?P<ime>.*?)"'
    r'<span class='smallerfont dull'>.(?P<leto>\d+).</span>'
    r'<a\s+href="/boardgame/(?P<id>\d+)/'
    r'<p class="smallefont dull" style="margin: 2px 0 0 0;">\n(?P<opis>*.*\n.*?)\n.*?</p>'
    r'<td class='collection_bggrating' align='center'>\n(?P<ocena_strani>.*)\n\n.*?<td class='collection_bggrating' align='center'>\n.*\n\n.*?<td class='collection_bggrating' align='center'>\n.*\n\n.*?'
    r'<td class='collection_bggrating' align='center'>\n.*\n\n.*?<td class='collection_bggrating' align='center'>\n(?P<povprecna_ocena>.*)\n\n.*?<td class='collection_bggrating' align='center'>\n.*\n\n.*?'
    r'<td class='collection_bggrating' align='center'>\n.*\n\n.*?<td class='collection_bggrating' align='center'>\n.*\n\n.*?<td class='collection_bggrating' align='center'>\n(?P<st_glasov>.*)\n\n.*?',
    flags=re.DOTALL
)



