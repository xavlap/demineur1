# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

#Xavier Lapalme et Abderrezak Agsous
#date : 20 decembre 2020

#ce programme est un jeu de carte solitaire sur le web 
#il n'est cepandant pas complet desole pour l'inconvenient.

#tableau des cartes 
tabCartes = [' ', '  ',             #les as vide pour pas les affichers
                    '    ', '     ',
                    
                    '<img src="cards/2C.svg">', '<img src="cards/2D.svg">',
                    '<img src="cards/2H.svg">', '<img src="cards/2S.svg">',
                    
                    '<img src="cards/3C.svg">', '<img src="cards/3D.svg">',
                    '<img src="cards/3H.svg">', '<img src="cards/3S.svg">',
                    
                    '<img src="cards/4C.svg">', '<img src="cards/4D.svg">',
                    '<img src="cards/4H.svg">', '<img src="cards/4S.svg">',
                    
                    '<img src="cards/5C.svg">', '<img src="cards/5D.svg">',
                    '<img src="cards/5H.svg">', '<img src="cards/5S.svg">',
                    
                    '<img src="cards/6C.svg">', '<img src="cards/6D.svg">',
                    '<img src="cards/6H.svg">', '<img src="cards/6S.svg">',
                    
                    '<img src="cards/7C.svg">', '<img src="cards/7D.svg">',
                    '<img src="cards/7H.svg">', '<img src="cards/7S.svg">',
                   
                    '<img src="cards/8C.svg">', '<img src="cards/8D.svg">',
                    '<img src="cards/8H.svg">', '<img src="cards/8S.svg">',
                    
                    '<img src="cards/9C.svg">', '<img src="cards/9D.svg">',
                    '<img src="cards/9H.svg">', '<img src="cards/9S.svg">',
                    
                    '<img src="cards/10C.svg">','<img src="cards/10D.svg">',
                    '<img src="cards/10H.svg">','<img src="cards/10S.svg">',
                    
                    '<img src="cards/JC.svg">', '<img src="cards/JD.svg">',
                    '<img src="cards/JH.svg">', '<img src="cards/JS.svg">',
                    
                    '<img src="cards/QC.svg">', '<img src="cards/QD.svg">',
                    '<img src="cards/QH.svg">', '<img src="cards/QS.svg">',
                    
                    '<img src="cards/KC.svg">', '<img src="cards/KD.svg">',
                    '<img src="cards/KH.svg">', '<img src="cards/KS.svg">']
                    
#melange un tableau
def melangerTab(tab):
    for i in range(len(tab)-1,0,-1):
        rand = math.floor(random()*i)
        temp = tab[i]
        tab[i] = tab[rand]
        tab[rand] = temp
    return tab
    
#tableau qui represente l'ordre des cartes tout au long du programme
ordreDesCartes = 0
 
def init():
    main = document.querySelector("#main")
    
    main.innerHTML = '''
    <style>
       #jeu table { float: none; }
       #jeu table td { border: 0; padding: 1px 2px; height: auto; }
       #jeu table td img { height: auto; }
    ''' 
    global ordreDesCartes
    
    ordreDesCartes = melangerTab(list(range(52)))
    print(ordreDesCartes)
    main.innerHTML+= '<div id="jeu">'+afficherCartes()+ '<button' \
    ' onclick="init();">Nouvelle Partie</button>'\
    '<br>Vous pouvez encore <button onclick="brasser();">Brasser les cartes'\
    '</button> 3 fois</div>' 
    mettreEnVert()

#trouve les position juste avant les troues
def trouverCartesAvantTrou():
    return [ordreDesCartes.index(0)-1,ordreDesCartes.index(1)-1,
    ordreDesCartes.index(2)-1,ordreDesCartes.index(3)-1]
     
#cette fonction n'est pas terminer il faudrais mettre la carte qu'on clic
#dans le bon espace vide et refaire mettreEnVert.
#il y aussi plusieurs erreur dans le code qui est deja la...
def clic(pos):
    global ordreDesCartes
    carteClic = pos
    
    cartesAvantTrou = trouverCartesAvantTrou()
    
    #si on clic sur une carte qui verte on la change de position avec le trou
    if carteClic%4 == cartesAvantTrou[0]%4 and\
    carteClic//4 == cartesAvantTrou[0]//4:
    
        document.querySelector("#carte"\
        +str(ordreDesCartes[cartesAvantTrou[0]+1])).innerHTML = \
        tdIdClicPourCartes(tabCartes[ordreDesCartes.index(carteClic)],carteClic)
        
        document.querySelector("#carte"+str(carteClic)).innerHTML = \
        tdIdClicPourCartes(tabCartes[cartesAvantTrou[0]+1],cartesAvantTrou[0]+1)
        
    elif carteClic%4 == cartesAvantTrou[1]%4 and\
    carteClic//4 == cartesAvantTrou[1]//4:
    
        document.querySelector("#carte"\
        +str(ordreDesCartes[cartesAvantTrou[1]+1])).innerHTML = \
        tdIdClicPourCartes(tabCartes[ordreDesCartes.index(carteClic)],carteClic)
        
        document.querySelector("#carte"+str(carteClic)).innerHTML = \
        tdIdClicPourCartes(tabCartes[cartesAvantTrou[1]+1],cartesAvantTrou[1]+1)
        
    elif carteClic%4 == cartesAvantTrou[2]%4 and\
    carteClic//4 == cartesAvantTrou[2]//4:
    
        document.querySelector("#carte"\
        +str(ordreDesCartes[cartesAvantTrou[2]+1])).innerHTML = \
        tdIdClicPourCartes(tabCartes[ordreDesCartes.index(carteClic)],carteClic)
        
        document.querySelector("#carte"+str(carteClic)).innerHTML = \
        tdIdClicPourCartes(tabCartes[cartesAvantTrou[2]+1],cartesAvantTrou[2]+1)
        
    elif carteClic%4 == cartesAvantTrou[3]%4 and\
    carteClic//4 == cartesAvantTrou[3]//4:
    
        document.querySelector("#carte"\
        +str(ordreDesCartes[cartesAvantTrou[3]+1])).innerHTML =\
        tdIdClicPourCartes(tabCartes[ordreDesCartes.index(carteClic)],carteClic)
        
        document.querySelector("#carte"+str(carteClic)).innerHTML = \
        tdIdClicPourCartes(tabCartes[cartesAvantTrou[3]+1],cartesAvantTrou[3]+1)
   
#ajoute le td l'id et la fonction clic pour chaque cartes 
def tdIdClicPourCartes(carte,i):
    return'<td id="carte'+str(tabCartes.index(carte))+'" onclick="clic('\
    + str(tabCartes.index(carte)) + ')">' + carte + '</td>'

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'

#retourne se qu'il faut ecrire dans le html pour afficher les cartes
#selon l'ordre quelle ont dans le tableau cartes
def afficherCartes():
    
    tabCartesMelange =['']*52
    for i in range(52):
        tabCartesMelange[i] = tabCartes[ordreDesCartes[i]]
           
    string = (tr(''.join(map(tdIdClicPourCartes,tabCartesMelange[0:13],range(0,13)))))
    string += (tr(''.join(map(tdIdClicPourCartes,tabCartesMelange[13:26],range(13,26)))))
    string += (tr(''.join(map(tdIdClicPourCartes,tabCartesMelange[26:39],range(26,39)))))
    string += (tr(''.join(map(tdIdClicPourCartes,tabCartesMelange[39:52],range(39,52)))))
    
    return table(string)
    
#met les cartes qui doivent etre mise en vert en vert selon l'odre des cartes
def mettreEnVert():  
   
    #on commence par enlever le vert de toutes les cartes
    for i in range(52):
        document.querySelector("#carte" + str(i)).setAttribute("style",
        "background-color: none")
    
    #les position juste avant les troues
    cartesAvantTrou = trouverCartesAvantTrou()
    
    #on assigne les test ainsi pour ne pas les evaluer a chaque
    #iteration de la boucle
    testRoi0 = ordreDesCartes[cartesAvantTrou[0]]%52 < 48
    testRoi1 = ordreDesCartes[cartesAvantTrou[1]]%52 < 48
    testRoi2 = ordreDesCartes[cartesAvantTrou[2]]%52 < 48
    testRoi3 = ordreDesCartes[cartesAvantTrou[3]]%52 < 48
    
    #si un trou est au debut d'une des ligne on met tous les deux en vert
    if cartesAvantTrou[0]+1%13 == 0:
        for i in range(4,8):
            document.querySelector("#carte" + str(i)).setAttribute("style",
            "background-color: lime")
                
    if cartesAvantTrou[1]+1%13 == 0:
        for i in range(4,8):
            document.querySelector("#carte" + str(i)).setAttribute("style",
            "background-color: lime") 
                
    if cartesAvantTrou[2]+1%13 == 0:
        for i in range(4,8):
            document.querySelector("#carte" + str(i)).setAttribute("style",
            "background-color: lime")
                
    if cartesAvantTrou[3]+1%13 == 0:
        for i in range(4,8):
            document.querySelector("#carte" + str(i)).setAttribute("style",
            "background-color: lime")                
    
    #on trouve quelles sont les cartes qui doivent etre mise en vert
    for i in range(52):
        if testRoi0:
            if i%4 == ordreDesCartes[cartesAvantTrou[0]]%4 and\
            i//4 == ordreDesCartes[cartesAvantTrou[0]]//4:
                document.querySelector("#carte" + str(i+4)).setAttribute("style",
                "background-color: lime")
          
        if testRoi1:
            if i%4 == ordreDesCartes[cartesAvantTrou[1]]%4 and\
            i//4 == ordreDesCartes[cartesAvantTrou[1]]//4:
                document.querySelector("#carte" + str(i+4)).setAttribute("style",
                "background-color: lime")     
       
        if testRoi2:
            if i%4 == ordreDesCartes[cartesAvantTrou[2]]%4 and\
            i//4 == ordreDesCartes[cartesAvantTrou[2]]//4:
                document.querySelector("#carte" + str(i+4)).setAttribute("style",
                "background-color: lime")
  
        if testRoi3:
            if i%4 == ordreDesCartes[cartesAvantTrou[3]]%4 and\
            i//4 == ordreDesCartes[cartesAvantTrou[3]]//4:
                document.querySelector("#carte" + str(i+4)).setAttribute("style",
                "background-color: lime")
def brasser():
    pass    


  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    