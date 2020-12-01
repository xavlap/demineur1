# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.


#tableau des cartes 
tabCartes = ['<img src = "cards/AC.sgv">', '<img src = "cards/AD.sgv">',
                    '<img src = "cards/AH.sgv">', '<img src = "cards/AS.sgv">',
                    
                    '<img src = "cards/2C.sgv">', '<img src = "cards/2D.sgv">',
                    '<img src = "cards/2H.sgv">', '<img src = "cards/2S.sgv">',
                    
                    '<img src = "cards/3C.sgv">', '<img src = "cards/3D.sgv">',
                    '<img src = "cards/3H.sgv">', '<img src = "cards/3S.sgv">',
                    
                    '<img src = "cards/4C.sgv">', '<img src = "cards/4D.sgv">',
                    '<img src = "cards/4H.sgv">', '<img src = "cards/4S.sgv">',
                    
                    '<img src = "cards/5C.sgv">', '<img src = "cards/5D.sgv">',
                    '<img src = "cards/5H.sgv">', '<img src = "cards/5S.sgv">',
                    
                    '<img src = "cards/6C.sgv">', '<img src = "cards/6D.sgv">',
                    '<img src = "cards/6H.sgv">', '<img src = "cards/6S.sgv">',
                    
                    '<img src = "cards/7C.sgv">', '<img src = "cards/7D.sgv">',
                    '<img src = "cards/7H.sgv">', '<img src = "cards/7S.sgv">',
                    
                    '<img src = "cards/8C.sgv">', '<img src = "cards/8D.sgv">',
                    '<img src = "cards/8H.sgv">', '<img src = "cards/8S.sgv">',
                    
                    '<img src = "cards/9C.sgv">', '<img src = "cards/9D.sgv">',
                    '<img src = "cards/9H.sgv">', '<img src = "cards/9S.sgv">',
                    
                    '<img src = "cards/10C.sgv">','<img src = "cards/10D.sgv">',
                    '<img src = "cards/10H.sgv">','<img src = "cards/10S.sgv">',
                    
                    '<img src = "cards/JC.sgv">', '<img src = "cards/JD.sgv">',
                    '<img src = "cards/JH.sgv">', '<img src = "cards/JS.sgv">',
                    
                    '<img src = "cards/QC.sgv">', '<img src = "cards/QD.sgv">',
                    '<img src = "cards/QH.sgv">', '<img src = "cards/QS.sgv">',
                    
                    '<img src = "cards/KC.sgv">', '<img src = "cards/KD.sgv">',
                    '<img src = "cards/KH.sgv">', '<img src = "cards/KS.sgv">']
                    
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
    main.innerHTML+='<div id="jeu">'+afficherCartes(cartesMelanger())+'</div>'
    

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
def td(contenu): return '<td>' + contenu + '</td>'


def afficherCartes(cartes):
    return table(tr(td('<img src="cards/2S.svg">')))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    