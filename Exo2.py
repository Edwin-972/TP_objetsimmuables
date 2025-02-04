from dataclasses import dataclass, replace
import asyncio
import random


@dataclass(frozen=True)
class Personne:
    nom: str
    age: int


def anniversaire(personnes):
    #Retourne une nouvelle liste avec l'âge de chaque personne augmenté de 1 
    return [replace(p, age=p.age + 1) for p in personnes]


async def getRandomNumber():
    # retournant un nombre aléatoire après 1 seconde
    await asyncio.sleep(1)
    return random.randint(1, 100)


async def test_multiple():
    numbers = await asyncio.gather(getRandomNumber(), getRandomNumber())
    print("Deux nombres générés :", numbers)


#Création d'une liste de personnes
personnes = [Personne("Alice", 35), Personne("Bob", 45)]
print("Liste avant anniversaire :", personnes)
print("Liste après anniversaire :", anniversaire(personnes))

#Exécution de la génération asynchrone
asyncio.run(test_multiple())
