# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.


#tableau des cartes 
tabCartes = [' ', ' ',             #les as vide pour pas les affichers
                    ' ', ' ',
                    
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
ordreDesCartes=melangerTab(list(range(52)))
 
def init():
    main = document.querySelector("#main")
    
    main.innerHTML = '''
    <style>
       #jeu table { float: none; }
       #jeu table td { border: 0; padding: 1px 2px; height: auto; }
       #jeu table td img { height: auto; }
    ''' 
    
    main.innerHTML+= '<div id="jeu">'+afficherCartes()+'</div>'
    mettreEnVert()
    

def clic(pos):
    global ordreDesCartes
    print(ordreDesCartes[0])
    ordreDesCartes[0] = ordreDesCartes[9]
    print(ordreDesCartes[0])
    pass
    
#ajoute le td l'id et la fonction clic pour chaque cartes 
def tdIdClicPourCartes(tabCartes):
    for i in range(len(tabCartes)):
        tabCartes[i] = '<td id="case'+str(i)+'" onclick="clic('\
        + str(ordreDesCartes.index(i)) + ')">' + tabCartes[i] + '</td>'
    return tabCartes

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'

#retourne se qu'il faut ecrire dans le html pour afficher les cartes
#selon l'ordre quelle ont dans le tableau cartes
def afficherCartes():

    #on fait cette fonction ici car la fonction clic depend de la position
    #elle doit donc etre changer a chauqe fois qu'on afficher les cartes
    cartesPasMelange = tdIdClicPourCartes(tabCartes.copy())
    
    tabCartesMelange =['']*52
    
    for i in range(52):
        tabCartesMelange[i] = cartesPasMelange[ordreDesCartes[i]]
    
    string = (tr(''.join(tabCartesMelange[0:13])))
    string += (tr(''.join(tabCartesMelange[13:26])))
    string += (tr(''.join(tabCartesMelange[26:39])))
    string += (tr(''.join(tabCartesMelange[39:52])))
    
    return table(string)
    
#met les cartes qui doivent etre mise en vert en vert selon l'odre des cartes
def mettreEnVert():  
   
    #on commence par enlever le vert de toutes les cartes
    for i in range(52):
        document.querySelector("#case" + str(i)).setAttribute("style",
        "background-color: none")
    
    #les position juste avant les troues
    positionVide0 = ordreDesCartes.index(0)-1
    positionVide1 = ordreDesCartes.index(1)-1
    positionVide2 = ordreDesCartes.index(2)-1
    positionVide3 = ordreDesCartes.index(3)-1
    
    #on assigne les test ainsi pour ne pas les evaluer a chaque
    #iteration de la boucle
    testRoi0 = ordreDesCartes[positionVide0]%52 < 48
    testRoi1 = ordreDesCartes[positionVide1]%52 < 48
    testRoi2 = ordreDesCartes[positionVide2]%52 < 48
    testRoi3 = ordreDesCartes[positionVide3]%52 < 48
    
    #si un trou est au debut d'une des ligne on met tous les deux en vert
    if positionVide0+1%13 == 0:
        for i in range(4,8):
            document.querySelector("#case" + str(i)).setAttribute("style",
            "background-color: lime")
                
    if positionVide1+1%13 == 0:
        for i in range(4,8):
            document.querySelector("#case" + str(i)).setAttribute("style",
            "background-color: lime") 
                
    if positionVide2+1%13 == 0:
        for i in range(4,8):
            document.querySelector("#case" + str(i)).setAttribute("style",
            "background-color: lime")
                
    if positionVide3+1%13 == 0:
        for i in range(4,8):
            document.querySelector("#case" + str(i)).setAttribute("style",
            "background-color: lime")                
    
    #on trouve quelles sont les cartes qui doivent etre mise en vert
    for i in range(52):
        if testRoi0:
            if i%4 == ordreDesCartes[positionVide0]%4 and\
            i//4 == ordreDesCartes[positionVide0]//4:
                document.querySelector("#case" + str(i+4)).setAttribute("style",
                "background-color: lime")
          
        if testRoi1:
            if i%4 == ordreDesCartes[positionVide1]%4 and\
            i//4 == ordreDesCartes[positionVide1]//4:
                document.querySelector("#case" + str(i+4)).setAttribute("style",
                "background-color: lime")     
       
        if testRoi2:
            if i%4 == ordreDesCartes[positionVide2]%4 and\
            i//4 == ordreDesCartes[positionVide2]//4:
                document.querySelector("#case" + str(i+4)).setAttribute("style",
                "background-color: lime")
  
        if testRoi3:
            if i%4 == ordreDesCartes[positionVide3]%4 and\
            i//4 == ordreDesCartes[positionVide3]//4:
                document.querySelector("#case" + str(i+4)).setAttribute("style",
                "background-color: lime")
    
    

  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    