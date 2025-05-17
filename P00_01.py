# chaines de caracteres
print(" ---- chaines de caracteres")
#
nom = "Hugo"
prenom = "Victor"
livre = "Les misérables"
est_ecrivain = True
print (f"{prenom} {nom} est {est_ecrivain} et a écrit {livre}")

# listes
print("--- listes")
#
plateformes_sociales = ["Facebook","Instagram","Snapchat","X"]
print (plateformes_sociales[0])
print (plateformes_sociales[1])
print (plateformes_sociales[2])
print (plateformes_sociales[3])

language = "Python"
print (language[0])
print (language[1])
print (language[2])
print (language[3])
print (language[4])
print (language[5])

# ajouter et enlevers des éléments d'une liste
print(plateformes_sociales)
print(len(plateformes_sociales))

plateformes_sociales.append("TikTok")
print(plateformes_sociales)
print(len(plateformes_sociales))

plateformes_sociales.remove("Snapchat")
print(plateformes_sociales)
print(len(plateformes_sociales))

# trier les éléments d'une liste
plateformes_sociales.sort()
print(plateformes_sociales)

# recchercher un élément dans la liste
print ("Hugo" in plateformes_sociales)
print ("Facebook" in plateformes_sociales)

# dictionnaires
print("--- Dictionnaires")
#
ecrivain = {
    "nom": "Hugo",
    "prenom": "Victor" 
}

print("nom" in ecrivain)

# conditions
print("--- Conditions")
#

ensoleille = False
neige = True
if ensoleille:
    print("on va à la plage !")
elif neige:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")


avec_soleil = True
en_semaine = False
if avec_soleil and not en_semaine:
    print("on va à la plage !")
elif avec_soleil and en_semaine:
    print("on va au travail !")
else:
    print("on reste à la maison !")


# operateurs comparatifs 
#  a == b
#  a != b
#  a <  b
#  a <=  b
#  a >  b
#  a >=  b 

# Match/Case
print("--- listes")
#

fruit = "pomme"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")

# Boucles: for
print("--- Boucles for")
#

races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

for x in range(5,10):
    print(x)
    print ("dans la boucle")
print ("après la boucle")

# Boucles: while
print("--- Boucles while")
#
capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1
    print (capacite_actuelle)


liste = [1, 2, 3, 4, 5]
# Boucle for sur la liste
for element in liste:
    if element == 3:
        # Si l'élément vaut 3, on passe à l'itération suivante sans exécuter le reste du code
        continue
    # Dans tous les autres cas, on exécute le reste du code
    print(element)

# Fonctions
print("--- Fonctions")
#
def afficher_message():
    print("Bonjour, comment ça va ?")

afficher_message()

def afficher_nom_prenom(nom, prenom):
    print("Nom :", nom)
    print("Prénom :", prenom)

afficher_nom_prenom("Dupont", "Jean")

def addition(a,b):
    resultat = a + b
    print (resultat)

addition(10,20) 

param1 = 20
param2 = 50

def multi(a,b):
    resultat = a * b
    return resultat, a, b

retour = multi(param1,param2) 
print(retour)

# Exercice
salaire_annuel = 50000
heures_hebdomadaires = 70

def salaire_mensuel(salaire_annuel):
    """
    calcul du salaire mensuel à partir du salaire annuel
    """
    salaire_mensuel = salaire_annuel / 12
    return salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel / 4
    return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_hebdomadaires):
    salaire_horaire = salaire_hebdomadaire / heures_hebdomadaires
    return salaire_horaire

salaire_mensuel = salaire_mensuel(salaire_annuel)
salaire_hebdomadaire = salaire_hebdomadaire(salaire_mensuel)
salaire_horaire = salaire_horaire(salaire_hebdomadaire,heures_hebdomadaires)
print ("votre salaire horaire est de: ",salaire_horaire)

# xxx
print("--- try / except")
#
"""
try/except
while True:
    try:
        x = int(input("Entrez un nombre entier : "))
        break
    except ValueError:
        print("Oops ! Ce n'est pas un nombre entier. Essayez encore...")


numerateur = input("Numerateur: ")
denominateur = input("denominateur: ")
try:
    resultat = int(numerateur)/int(denominateur)
    print("Le resultat est:",resultat)
except ZeroDivisionError:
    print("Erreur: Division par zero !")
except ValueError:
    print("Erreur: Il faut donner 2 nombres")
"""

# xxx
print("--- packages")
#

import calculator.fonction 
resultat = calculator.fonction.somme(10,15)
print(resultat)

import requests
resultat = requests.get("https://google.fr")
print(resultat.content)


# xxx
print("--- request")
#

# URL de l'API
url = "https://api.open-meteo.com/v1/forecast"

# Paramètres de la requête
params = {
    "latitude": 48.8566,     # Paris
    "longitude": 2.3522,
    "hourly": "temperature_2m",
}

# Requête GET
response = requests.get(url, params=params)

# Vérification du code retour
if response.status_code == 200:
    data = response.json()  # Convertit la réponse JSON en dict Python
    print("Température horaire :", data["hourly"]["temperature_2m"][:5])  # exemple d'affichage
else:
    print("Erreur :", response.status_code)

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

# Voir le code html source
print(page.content)

# xxx
print("--- beautifulsoup")
#

from bs4 import BeautifulSoup
with open("index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')

# Extraction du titre de la page
title = soup.title.string
print("Titre de la page:", title)

# Extraction du texte de la balise h1
h1_text = soup.find("h1").string
print("Texte de la balise h1:", h1_text)

# Dictionnaire pour stocker les produits
all_products = dict()

# Extraction des noms et des prix des produits dans la liste
products = soup.find_all("li")
for product in products:
    name = product.find("h2").string
    price_str = product.find("p", class_="price").string
    # On sépare la chaine avec " " en liste de mots
    price_list = price_str.split(" ")
    # On récupère le prix (= deuxième mot)
    all_products[name] = {"prix": price_list[1]}

# Extraction des descriptions des produits dans la liste
descriptions_list = []
for product in products:
    # La description eest le dernier élément de la liste des paragraphes
    description = product.find_all("p")[-1].string
    all_products[name]["description"] = description

# Affichage des informations extraites
print("Produits:", all_products)

# Transformation des prix en dollars
for name in all_products.keys():
    price_str = all_products[name]["prix"]
    # Supprimer le symbole €
    price = price_list[1].strip("€")
    # Convertir en float
    price = float(price)
    dollar_price = price * 1.2
    all_products[name]["prix_dollar"] = f"{dollar_price}$"

# Affichage avec les prix en dollars
print("Tous les produits:", all_products)


# xxx
print("--- manipulation de fichiers")

# ouvrir un fichier en ecriture
fichier = open("hello.txt", "w")
fichier.write("Hello, world!")
fichier.close()

# ouvrir un fichier en lecture (par defaut) et fermeture automatique avec with
with open("hello.txt") as fichier:
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)

import csv
with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne['nom'] + " travaille en tant que " 
              + ligne['metier'] + " et sa couleur préférée est " 
              + ligne['couleur_preferee'])



# xxx
print("--- ecriture dans un fichier")

url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")

print(soup.prettify()[:2000])

titres = soup.find_all("a", class_="gem-c-document-list__item-title")
print("titres: ",titres)
titre_textes = []
for titre in titres:
    titre_textes.append(titre.string)

print("titre_texte: ",titre_textes)

descriptions = soup.find_all("a", class_="gem-c-document-list__item-description")
description_textes = []
for description in descriptions:
    description_textes.append(description.string)

print("description_textes: ",description_textes)


