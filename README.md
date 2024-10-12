# Analiza družabnih iger

_Avtor: Nik Urukalo_

Pri predmetu __Uvod v programiranje__ sem pripravil projektno nalogo analize družabnih iger s spletne strani [BoardGameGeek](https://boardgamegeek.com/browse/boardgame). Zajel sem tisoč družabnih iger, ki so imele na spletni strani najvišjo oceno strani. Pri tem sem uporabil programski jezik Python. Za vsako igro sem zajel:
- rang (mesto na seznamu, glede na oceno strani), 
- naslov,
- opis,
- leto nastanka,
- ocena strani,
- povprečna ocena in
- število glasov.
Projektna naloga je sestavljena iz treh delov. V prvem delu sem sestavil lestvice najboljših 10 iz vsake kategorije(ocena strani, povprečna ocena ter število glasov). V drugem delu sem analiziral 3 desetletja na različne načine. V zadnjem pa sem postavil pet hipotez, katerih resničnost sem preverjal.

## Navodila za uporabo
Uporabnik lahko samo odpre datoteko analiza.ipynb, kjer si lahko ogleda analizo družabnih iger.

Glavna datoteka je main.py. Program najprej shrani vseh 10 spletnih strani, nato iz njih s pomožnim programom izlusci_igro.py zbere vse podatke ter jih shrani v csv datoteko.

Uporabil sem knjižnice pandas, numpy, matplotlib, csv, json, os, requests, sys ter json.