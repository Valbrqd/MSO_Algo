class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def josephus(n, k):
    # Créer une liste chaînée circulaire avec n noeuds
    head = Node(1)
    curr = head
    for i in range(2, n+1):
        curr.next = Node(i)
        curr = curr.next
    curr.next = head

    # Éliminer les personnes jusqu'à ce qu'il ne reste qu'une personne
    curr = head
    while curr.next != curr:
        # Sauter k-1 personnes
        for i in range(k-1):
            curr = curr.next
        # Éliminer la k-ème personne
        curr.next = curr.next.next
    return curr.data

# Exemple d'utilisation :
n = 41
k = 3
survivor = josephus(n, k)
print("Le survivant est la personne numéro :", survivor)
