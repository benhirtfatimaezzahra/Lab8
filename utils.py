"""utils.py Fonctions utilitaires pour la gestion des notes et du calcul de prix.

Ce module contient :
- une constante globale TAUX_TVA (taux de TVA par défaut),
- des fonctions génériques pour calculer une moyenne,
- tester une admission selon un seuil,
- calculer un prix TTC,
- et générer un rapport formaté sur une liste de notes.

Ce docstring apparaît dans help(utils) ou dans les infobulles d’un IDE.
"""

TAUX_TVA = 0.2  
SEUIL_ADMISSION = 10 

def moyenne(notes):
    """Renvoie la moyenne d'une liste de notes (0 si la liste est vide)."""
    if not notes:
        return 0
    return sum(notes) / len(notes)


def est_admis(note, seuil=SEUIL_ADMISSION):
    """Retourne True si la note est >= au seuil (10 par défaut)."""
    return note >= seuil


def prix_ttc(prix_ht, taux=TAUX_TVA):
    """Applique un taux de TVA (20 % par défaut) pour obtenir un prix TTC."""
    return prix_ht * (1 + taux)


def formater_rapport(notes):
    """Construit une petite chaîne de rapport à partir d'une liste de notes."""
    moyenne_classe = moyenne(notes)
    notes_valides = [note for note in notes if est_admis(note)]
    lignes = [
        "=== Rapport des notes ===",
        f"Notes : {notes}",
        f"Moyenne : {moyenne_classe:.2f}",
        f"Nombre d'étudiants admis : {len(notes_valides)}",
    ]
    return "\n".join(lignes)


if __name__ == "__main__":
    print("Tests rapides de utils.py")
    print("Moyenne de [10, 12, 14] =", moyenne([10, 12, 14]))
