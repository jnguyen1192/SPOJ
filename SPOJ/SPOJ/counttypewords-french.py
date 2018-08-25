def counttypewordsfrench(file):
    arr = ['ABR',
           'ADJ',
           'ADV',
           'DET:ART',
           'DET:POS',
           'INT',
           'KON',
           'NAM',
           'NUM',
           'PRO',
           'PRO:DEM',
           'PRO:IND',
           'PRO:PER',
           'PRO:POS',
           'PRO:REL',
           'PRP',
           'PRP:det',
           'PUN',
           'PUN:cit',
           'SENT',
           'SYM',
           'VER:cond',
           'VER:futu',
           'VER:impe',
           'VER:impf',
           'VER:infi',
           'VER:pper',
           'VER:ppre',
           'VER:pres',
           'VER:simp',
           'VER:subi',
           'VER:subp',
           ]
    fichier = open(file, "r")
    # lis le fichier et le stocke dans un tableau en fonction des espaces
    text = fichier.read().split()
    # initialise le compteur
    c = 0
    for i in xrange(1, len(text), 3):
        # test si i existe dans arr
        if text[i] in arr:
        # supprimer i dans arr
            arr.remove(text[i])
            c = c + 1
        # incremente le compteur
    print(c)

counttypewordsfrench('OUTPUT.txt')
