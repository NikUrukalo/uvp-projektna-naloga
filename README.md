# Analiza družabnih iger

_Avtor: Nik Urukalo_

Pri predmetu __Uvod v programiranje__ sem pripravil projektno nalogo analize družabnih iger s spletne strani [BoardGameGeek](https://boardgamegeek.com/browse/boardgame). Zajel sem tisoč družabnih iger, ki so imele na spletni strani najvišjo oceno strani. Pri tem sem uporabil programski jezik _Python_. Za vsako igro sem zajel:
- rang (mesto na seznamu, glede na oceno strani), 
- naslov,
- opis,
- leto nastanka,
- ocena strani,
- povprečna ocena in
- število glasov.

Projektna naloga je sestavljena iz treh delov. V prvem delu sem sestavil lestvice najboljših 10 iz vsake kategorije(ocena strani, povprečna ocena ter število glasov). V drugem delu sem analiziral 3 desetletja na različne načine. V zadnjem pa sem postavil pet hipotez, katerih resničnost sem preverjal.

## Navodila za uporabo
Glavna datoteka je main.py. Program najprej shrani vseh 10 spletnih strani. Pomožni program izlusci_igro.py s pomočjo regularnih izrazov zbere vse podatke o igrah. Nato jih program main.py shrani v csv in json datoteko. Podatki, ki so shranjeni v igre.csv datoteki uvozimo v analiza.ipynb s knjižnico _Pandas_. V tej datoteki pa sledi analiza družabnih iger.

Uporabil sem knjižnice pandas, numpy, matplotlib, csv, json, os, requests, sys ter json.