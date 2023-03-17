import matplotlib.pyplot as plt
import numpy as np

def rentabilite200():
    r = 0
    i = 0
    while i < 368950:
        r = r + np.sqrt(200)*np.pi
        i = i + 1000
    return i

# Attractivité du marché (axe y)
x = [2, 4, 6]
y = [6, 4, 2]

# Force concurrentielle (axe x)
x2 = [6, 4, 2]
y2 = [2, 4, 6]

# Divisions de SFR (Domaines d'activité stratégique - DAS)
segments = ['Téléphonie mobile', 'Télévision', 'Fibre optique/Cloud']

# Rentabilité et attractivité des DAS de SFR
rentabilite = [2, 3, 1]
attractivite = [3, 2, 1]

# Création du graphique
fig, ax = plt.subplots()
ax.scatter(x, y, s= rentabilite200, c=attractivite, cmap='cool')
ax.scatter(x2, y2, s=rentabilite200, c=attractivite, cmap='cool')

# Ajout des labels et des annotations
plt.xlabel('Force concurrentielle')
plt.ylabel('Attractivité du marché')
plt.title('Matrice de McKinsey pour SFR')
for i, txt in enumerate(segments):
    ax.annotate(txt, (x[i]-0.3, y[i]+0.3))
    ax.annotate(txt, (x2[i]+0.2, y2[i]-0.3))

# Affichage du graphique
plt.show()