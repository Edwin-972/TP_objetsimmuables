import asyncio
import random

#Les articles (produits) dans le stock
class Article:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return f"Article: {self.nom}, Prix: {self.prix}€, Quantité: {self.quantite}"


#Détecter les articles en rupture de stock
def detecter_stock_faible(inventaire, seuil=3):
    articles_a_reappro = []
    for article in inventaire:
        if article.quantite < seuil:
            articles_a_reappro.append(article)
    return articles_a_reappro


#Réapprovisionner les articles faibles
def reapprovisionner_stock(inventaire, articles_a_reappro, quantite_reappro=10):
    for article in inventaire:
        if article in articles_a_reappro:
            article.quantite += quantite_reappro  # On ajoute 10 à la quantité
    return inventaire


#Commander des articles chez un fournisseur
class Fournisseur:
    def __init__(self, nom, url_api):
        self.nom = nom
        self.url_api = url_api

    def commander(self, article, quantite):
        print(f"Commande passée à {self.nom} : {quantite}x {article.nom}")
        article.quantite += quantite  # On ajoute les quantités commandées
        return article


#Traitement des commandes clients (en parallèle)
class Commande:
    def __init__(self, articles):
        self.articles = articles

    def __repr__(self):
        return f"Commande: {', '.join([article.nom for article in self.articles])}"


#Fonction asynchrone pour traiter une commande
async def traiter_commande(commande):
    print(f"Traitement de la commande: {commande}")
    await asyncio.sleep(random.uniform(1, 3))  # Simule un délai
    print(f"Commande traitée: {commande}")


#Fonction pour traiter plusieurs commandes en même temps
async def traiter_plusieurs_commandes(commandes):
    await asyncio.gather(*(traiter_commande(cmd) for cmd in commandes))


#Sécuriser les données
def mesures_de_securite():
    print("\n🔒 Sécurité des Données :")
    print("- Utilisation de bases de données sécurisées.")
    print("- Transactions sécurisées pour éviter les erreurs.")
    print("- Authentification forte (par exemple JWT ou OAuth).")
    print("- Protection contre les attaques (par exemple SQL Injection).")


#TESTS

#Initialisation du stock
inventaire = [
    Article("Chaise", 50, 2),  # Stock critique
    Article("Table", 150, 5),  # Stock suffisant
    Article("Lampe", 30, 1)    # Stock critique
]

# Détecter les articles avec un stock faible
articles_faibles = detecter_stock_faible(inventaire)
print("Articles faibles (en rupture de stock) : ", articles_faibles)

#Réapprovisionner les articles faibles
inventaire = reapprovisionner_stock(inventaire, articles_faibles)
print("Inventaire après réapprovisionnement : ", inventaire)

#Commander des articles chez un fournisseur
fournisseur = Fournisseur("FournisseurA", "https://LeBonCoin.com")
article_manquant = Article("Bureau", 200, 0)  # Le Bureau est en rupture de stock
article_reapprovisionne = fournisseur.commander(article_manquant, 5)  # On commande 5 bureaux
print("Article réapprovisionné : ", article_reapprovisionne)

#Traiter les commandes en parallèle
commandes = [
    Commande([Article("Chaise", 50, 1)]),
    Commande([Article("Table", 150, 1)]),
    Commande([Article("Lampe", 30, 2)])
]

#Lancer le traitement des commandes
print("\n⏳ Lancement du traitement des commandes...")
asyncio.run(traiter_plusieurs_commandes(commandes))

#Afficher les bonnes pratiques de sécurité
mesures_de_securite()
