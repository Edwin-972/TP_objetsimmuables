from typing import List

def addToEach(n: int, lst: List[int]) -> List[int]:

#Ajoute n à chaque élément de la liste sans modifier la liste originale.

    return [x + n for x in lst]

#Retourne une nouvelle liste sans doublons, en conservant l'ordre d'apparition.
def removeDuplicates(lst: List[int]) -> List[int]: 
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Exemples d'utilisation
test_list = [1, 2, 3, 2, 4, 1, 5]
print(addToEach(2, test_list)) 
print(removeDuplicates(test_list)) 
