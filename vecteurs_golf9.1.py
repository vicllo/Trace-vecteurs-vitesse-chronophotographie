"""
--------------------------------------------------------------------------------------------------------------------
Victor LL - Novembre 2019 - Lycée LdB, MlR
Présente la trajectoire d'un objet, sa vitesse et sa variation de vitesse

Fichier à importer sous le format TXT depuis Avimeca

Rentrer le chemin du fichier dans la variable "fichier"
Cliquer sur un point pour voir ses coordonnées,
cliquer de nouveau sur ce point pour observer la translation réalisée par les différents vecteurs

Si vous souhaitez cacher les vecteurs vitesse, il suffit de changer opacitéVecteurVitesse (0 = invisible / 1 = visible)
Si vous souhaitez cacher les vecteurs variation de vitesse, il suffit de changer oppacitéVecteurVarVitesse

Il y a donc possibilité de projeter, tracer les vecteurs au tableau et vérifier le tracé plus tard

Présence d'outils en bas de graphique pour zoomer, bouger etc...

--------------------------------------------------------------------------------------------------------------------
"""

# On importe les librairies
import matplotlib.pyplot as plt  # pour les graphiques
import mplcursors  # pour l'interraction avec la souris
import csv  # pour l'interpretation des résultats depuis le logiciel de pointage

fichier = 'C:\\Users\\victo\\Desktop\\tennis.txt'  # rentrer ici le chemin du fichier. Attention "/" -> "//" !
opaciteVecteurVitesse = 1
opaciteVecteurVarVitesse = 1
cs = 3  # permet de régler le nombre de chiffres après la virgule (une prochaine version pourrait intégrer les CS)
scale = 10
scale = 100/scale

entree = csv.reader(open(fichier, newline=''), delimiter='\t')  # ouverture du fichier
liste = []  # creation de la liste de lecture

# Création des différentes listes, vides pour le moment
t = []
x = []
y = []

numero_ligne = 0

for ligne in entree:  # tant qu'il y a des lignes à lire
    if ligne[0][0] != "#":  # si la ligne n'est pas un commentaire (commençant par le caractère #)
        # del ligne[3]  on supprime la 4ème colonne de ligne qui est une erreur de lecture (à activer si besoin)
        liste.append(ligne)  # on ajoute la lecture à la liste de lecture

        if numero_ligne < 3:  # On supprime les 3 premières lignes, inutiles sur Avimeca
            liste.remove(ligne)
        numero_ligne = numero_ligne + 1


for i in range(len(liste)):  # pour chaque point mesuré
    for j in range(3):
        liste[i][j] = liste[i][j].replace(",", ".")  # on remplace  , par  . (ex : 9,24 -> 9.24) pour l'exploitation
    t.append(liste[i][0])  # on donne le temps de la mesure
    x.append(liste[i][1])  # on donne l'abscisse mesurée
    y.append(liste[i][2])  # on donne l'ordonée mesurée
    # on convertit les chaines de caractère en nombres pour effectuer des opérations dessus
    x[i] = float(x[i])
    y[i] = float(y[i])
    t[i] = float(t[i])


# On définit le calcul et le tracé des vecteurs vitesse.
def vecteurvitesse():
    for n in range(len(x) - 1):
        v_x.append(round((x[n + 1] - x[n-1]) / (t[n + 1] - t[n]), cs))  # On calcule l'abscisse du vecteur vitesse
        v_y.append(round((y[n + 1] - y[n-1]) / (t[n + 1] - t[n]), cs))  # On calcule l'ordonnée du vecteur vitesse
        if n > 1:
            plt.quiver(x[n], y[n], v_x[n], v_y[n], scale_units='xy', angles='xy', scale=scale, width=0.003,
                       color='green', alpha=opaciteVecteurVitesse)
            # On trace le vecteur d'origine x,y et de fin v_x,v_y sans lui attribuer de légende
        elif n == 1:
            plt.quiver(x[n], y[n], v_x[n], v_y[n], scale_units='xy', angles='xy', scale=scale, width=0.003,
                       color='green', label='vecteur vitesse', alpha=opaciteVecteurVitesse)
            # On trace le vecteur d'origine x,y et de fin v_x,v_y en lui attribuant une légende


# On définit le calcul et le tracé des vecteurs variation de vitesse.
def vecteurvariationvitesse():
    for o in range(len(v_y) - 1):
        dv_x.append(round((v_x[o + 1] - v_x[o - 1]), cs))  # On calcule l'abscisse de Vn+1-Vn-1
        dv_y.append(round((v_y[o + 1] - v_y[o - 1]), cs))  # On calcule l'ordonnée de Vn+1-Vn-1
        if o > 2:
            plt.quiver(x[o], y[o], dv_x[o], dv_y[o], scale_units='xy', angles='xy', scale=scale, width=0.003,
                       color='red', alpha=opaciteVecteurVarVitesse)
            # On trace le vecteur d'origine x,y et de fin dv_x,dv_y sans lui attribuer de légende
        elif o == 2:
            plt.quiver(x[o], y[o], dv_x[o], dv_y[o], scale_units='xy', angles='xy', scale=scale, width=0.003,
                       color='red', label='vecteurs variation de vitesse', alpha=opaciteVecteurVarVitesse)
            # On trace le vecteur d'origine x,y et de fin dv_x,dv_y en lui attribuant une légende


# On introduit les différentes suites nécéssaires
v_x = []  # Vitesse en x
v_y = []  # Vitesse en y
dv_y = []  # Variation de vitesse en x
dv_x = []  # Variation de vitesse en y

# appel aux fonctions
vecteurvitesse()
vecteurvariationvitesse()

"""
définition de la fenêtre et de la légende
Si la légende gène, possiblité de changer entre 'upper left' et 'lower left'
"""

plt.scatter(x, y, marker='+', s=100)
plt.title('Positions successives occupées par la balle de golf')
plt.xlabel('x en (m)')
plt.ylabel('y en (m)')
plt.xlim(min(x) - abs((max(x)-min(x))/10), max(x) + abs((max(x)-min(x))/5))
plt.ylim(min(y) - abs((max(y)-min(y))/2), max(y) + abs((max(y)-min(y))/7))
leg = plt.legend(loc='lower left', fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.4)
mplcursors.cursor()  # fonction pour l'interractivité souris
plt.get_current_fig_manager().window.state('zoomed')
plt.show()
