devojka_iz_petnice = "Da je ljubav nauka\ndobio bih Nobela\nA da je ljubav knjiga\nuzeo bih NIN-a\n\nDevojke iz Petnice\nredom su pametnice\nA jedna među njima\nsad moje srce ima\n\nŽelim da sam projekat\ni da sam joj u mislima\nmrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima\n\nDevojka iz Petnice\nona meni znači sve\ni kada me se seti\nja hoću da poletim\n\nDevojka iz Petnice\nu koju sam zaljubljen\nsad uči tamo negde\nDa li pamti mene?\n\nHoću da sam tema\nU nečemu što sprema\nMrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima"
c=devojka_iz_petnice.lower()
red=c.split("\n")
print(red)

lista_reci=[]
for x in red:
    stih=x.split(" ")
    for y in stih:
        lista_reci.append(y)
        
   
print (lista_reci)


print (len(lista_reci))

blank=[]
for rec in lista_reci:
    if rec not in blank:
        blank.append(rec)
print(len(blank))

lista_reci.sort()
recnik={rec:lista_reci.count(rec) for rec in lista_reci}
for k,v in recnik.items():
    print(k,v)



