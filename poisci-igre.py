import re

with open("podatki-o-igrah.html") as dat:
    besedilo = dat.read() 
    niz = r'<a\s+href="/boardgame/(?P<id>\d+)/[^"]*"><img\s+alt="Board Game: (?P<naslov>[^"]*)"'
    igre = []
    for najdba in re.finditer(niz, besedilo):
        
        igre.append((najdba.group("naslov"), int(najdba.group("id")))) 
print(igre, len(igre))


