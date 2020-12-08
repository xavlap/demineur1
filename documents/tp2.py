# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.


#tableau des cartes 
tabCartes = ['<img src="cards/AC.svg">', '<img src="cards/AD.svg">',
                    '<img src="cards/AH.svg">', '<img src="cards/AS.svg">',
                    
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
    main.innerHTML+= '<div id="jeu">'+afficherCartes(cartesMelanger())+'</div>'
    
    #je sais pas pourquoi je peux pas faire ca come si case 1 existe pas mais 
    #j'écrit bien son id dans td()
    case1 = document.querySelector("case1").setAttribute("style","backgroud-color: lime")
    print(case1)
    #case1.setAttribute("style", "background-color: lime")
    
    

def onClic(pos):
    pass

#retourne un packet de 52 cartes melange
def cartesMelanger():
    cartes = list(range(52))
    for i in range(51,0,-1):
        rand = math.floor(random()*i)
        temp = cartes[i]
        cartes[i] = cartes[rand]
        cartes[rand] = temp
    return cartes
    
def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'

#mauvais nom de fonction
def td(contenu,case):
    print('<td id="case'+str(case)+'">' + contenu + '</td>')
    return '<td id="case1">' + contenu + '</td>' #test pour etre sur d'avoir id="case1"
    #return '<td id="case"'+str(case)+'">' + contenu + '</td>' #se qu'il faudra mettre


def afficherCartes(cartes):
    global tabCartes
    tabCartesMelange =['']*52
    
    for i in range(52):
        if cartes[i]==0 or cartes[i]==1 or cartes[i]==2 or cartes[i]==3:
            continue        
        tabCartesMelange[i] = tabCartes[cartes[i]]
    
        
    string = (tr(''.join(map(td,tabCartesMelange[0:13],list(range(13))))))
    string += (tr(''.join(map(td,tabCartesMelange[13:26],list(range(13,26))))))
    string += (tr(''.join(map(td,tabCartesMelange[26:39],list(range(26,39))))))
    string += (tr(''.join(map(td,tabCartesMelange[39:52],list(range(39,52))))))
    
    return table(string)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    