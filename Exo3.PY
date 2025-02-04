from dataclasses import dataclass, replace
from typing import List

# Structure pour les articles
@dataclass(frozen=True)
class Article:
    nom: str
    prix: float
    quantite: int

    def __repr__(self):
        return f"Article ='{self.nom}', prix={self.prix}, quantite={self.quantite})"

# Gestion de l'inventaire 
def ajouter_article(inventaire, article):
    # Ajoute un nouvel article à l'inventaire
    return inventaire + [article]

def mettre_a_jour_quantite(inventaire, nom, nouvelle_quantite):
    # Met à jour la quantité d'un article sans modifier l'inventaire d'origine
    return [replace(article, quantite=nouvelle_quantite) if article.nom == nom else article for article in inventaire]

def supprimer_article(inventaire, nom):
    # Supprime un article de l'inventaire
    return [article for article in inventaire if article.nom != nom]

# Calcul du montant total d'une commande
@dataclass(frozen=True)
class Commande:
    articles: List[Article]

def calculer_total_commande(commande):
    # Retourne le montant total de la commande
    return sum(article.prix * article.quantite for article in commande.articles)

# Gestion des promotions
@dataclass(frozen=True)
class Promotion:
    nom: str
    condition: float  # Montant minimum requis
    reduction: float  # Réduction en %

def appliquer_promotions(commande, promotions):
    # Applique les promotions si la condition est remplie
    total = calculer_total_commande(commande)
    for promo in promotions:
        if total >= promo.condition:
            total *= (1 - promo.reduction / 100)
    return total

# Mise à jour de l'inventaire après une commande
def mettre_a_jour_stock(inventaire, commande):
    # Met à jour l'inventaire après une commande sans modifier l'original
    new_inventaire = []
    for article in inventaire:
        for cmd in commande.articles:
            if article.nom == cmd.nom:
                new_inventaire.append(replace(article, quantite=article.quantite - cmd.quantite))
                break
        else:
            new_inventaire.append(article)
    return new_inventaire

# Test
# Création d'un inventaire initial
inventaire = []
inventaire = ajouter_article(inventaire, Article("Chaise", 50, 10))
inventaire = ajouter_article(inventaire, Article("Table", 150, 5))
print("Inventaire initial :", inventaire)

# Mise à jour de la quantité
inventaire = mettre_a_jour_quantite(inventaire, "Chaise", 8)
print("Inventaire après mise à jour :", inventaire)

# Suppression d'un article
inventaire = supprimer_article(inventaire, "Table")
print("Inventaire après suppression :", inventaire)

# Création d'une commande
commande = Commande([Article("Chaise", 50, 2)])
print("Total de la commande :", calculer_total_commande(commande))

# Application d'une promotion
promotions = [Promotion("Promo10%", 100, 10)]
print("Total avec promotions :", appliquer_promotions(commande, promotions))

# Mise à jour de l'inventaire après la commande
inventaire = mettre_a_jour_stock(inventaire, commande)
print("Inventaire après commande :", inventaire)
