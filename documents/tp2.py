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
                    
def init():
    main = document.querySelector("#main")
    #main.innerHTML = """
    #  <style>
    #   #jeu table { float: none; }
    #    #jeu table td { border: 0; padding: 1px 2px; height: auto; }
    #    #jeu table td img { height: auto; }
    # </style>
    # <div id="jeu">
    #   <table>
    #     <tr>
    #         <td id="case0"><img src="cards/2S.svg"></td>
    #         <td id="case1"><img src="cards/QH.svg"></td>
    #      </tr>
    #      <tr>
    #          <td id="case2"><img src="cards/JC.svg"></td>
    #          <td id="case3"><img src="cards/10D.svg"></td>
    #      </tr>
    #    </table>
    # </div>"""

    #case0 = document.querySelector("#case0")
    #case0.setAttribute("style", "background-color: lime")
    main.innerHTML = '''
    <style>
       #jeu table { float: none; }
       #jeu table td { border: 0; padding: 1px 2px; height: auto; }
       #jeu table td img { height: auto; }
    ''' 
    ordreDesCartes=melangerTab(list(range(52)))
    
    main.innerHTML+= '<div id="jeu">'+afficherCartes(ordreDesCartes)+'</div>'
    
    mettreEnVert(ordreDesCartes)
    

def onClic(pos):
    pass

#melange un tableau 
def melangerTab(tab):
    for i in range(len(tab)-1,0,-1):
        rand = math.floor(random()*i)
        temp = tab[i]
        tab[i] = tab[rand]
        tab[rand] = temp
    return tab
    
    
def tdEtIdPourCarte(tabCartes):
    for i in range(len(tabCartes)):
        tabCartes[i] = '<td id="case'+str(i)+'">' + tabCartes[i] + '</td>'
    return tabCartes

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'

def afficherCartes(cartes):
    global tabCartes
    cartesPasMelange = tdEtIdPourCarte(tabCartes.copy())
    tabCartesMelange =['']*52
    
    for i in range(52):
        tabCartesMelange[i] = cartesPasMelange[cartes[i]]
    
    string = (tr(''.join(tabCartesMelange[0:13])))
    string += (tr(''.join(tabCartesMelange[13:26])))
    string += (tr(''.join(tabCartesMelange[26:39])))
    string += (tr(''.join(tabCartesMelange[39:52])))
    
    return table(string)
    

def mettreEnVert(cartes):
    global tabCartes
    
    positionVide0 = cartes.index(0)-1
    positionVide1 = cartes.index(1)-1
    positionVide2 = cartes.index(2)-1
    positionVide3 = cartes.index(3)-1
    print(tabCartes[cartes[positionVide0]])
    print(tabCartes[cartes[positionVide1]])
    print(tabCartes[cartes[positionVide2]])
    print(tabCartes[cartes[positionVide3]])
    
    for i in range(52):
        if i%4 == cartes[positionVide0]%4 and i//4 == cartes[positionVide0]//4:
            document.querySelector("#case" + str(i+4)).setAttribute("style", "background-color: lime")
        if i%4 == cartes[positionVide1]%4 and i//4 == cartes[positionVide1]//4:
            document.querySelector("#case" + str(i+4)).setAttribute("style", "background-color: lime")
        if i%4 == cartes[positionVide2]%4 and i//4 == cartes[positionVide2]//4:
            document.querySelector("#case" + str(i+4)).setAttribute("style", "background-color: lime")
        if i%4 == cartes[positionVide3]%4 and i//4 == cartes[positionVide3]//4:
            document.querySelector("#case" + str(i+4)).setAttribute("style", "background-color: lime")
    print(positionVide0)
    print(positionVide1)
    print(positionVide2)
    print(positionVide3)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    