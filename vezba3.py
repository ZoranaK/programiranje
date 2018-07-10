with open("xml.xml", "r", encoding="utf-8") as xml:
    recnik = dict()
    for red in xml:
        if not (red.startswith("<")):
            try:
                rec, mala_rec, lema, pos =red.split("\t")
                if pos.startswith("N"):
                    if lema in recnik.keys():
                        recnik[lema]=recnik[lema]+1
                    else:
                        recnik[lema]=1
            except:
                print(red)
    with open("recnik2.txt", "w", encoding="utf-8") as recnik2:
        for l, f in recnik.items():
            recnik2.write(l + "\t\t" + str(f) + "\n")

             
                    
                    
                
