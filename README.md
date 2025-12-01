# Lab8 – Modules et Imports en Python

Projet Python illustrant la création et l'utilisation de modules personnalisés avec imports, constantes globales et fonctions réutilisables. Ce lab démontre les bonnes pratiques de structuration de code en plusieurs fichiers.

Le programme met en œuvre la séparation entre utilitaires (module `utils.py`) et application principale (`app.py`), avec documentation complète et tests intégrés.

---

## Fonctionnalités

### Module `utils.py`
- **Constantes globales** : `TAUX_TVA` (20%), `SEUIL_ADMISSION` (10)
- **Fonctions statistiques** : calcul de moyenne avec gestion des listes vides
- **Fonction d'admission** : test selon un seuil paramétrable
- **Calcul financier** : prix TTC avec taux de TVA personnalisable
- **Génération de rapport** : formatage des statistiques de notes
- **Tests intégrés** : bloc `if __name__ == "__main__"` pour validation

### Application `app.ipynb`
- **Deux styles d'import** : démonstration de `import utils` et `from utils import`
- **Utilisation des fonctions** : appel des utilitaires du module
- **Accès aux constantes** : utilisation de `utils.TAUX_TVA`
- **Tests d'admission** : vérification du statut des étudiants
- **Fonction main()** : point d'entrée principal structuré

### Documentation
- **Docstrings de module** : description complète en haut de `utils.py`
- **Docstrings de fonctions** : documentation de chaque fonction
- **Commentaires explicatifs** : sections clairement délimitées

---

## Architecture
```
Lab8/ → Dossier du projet contenant :

1. Fichier utils.py (module utilitaire)
   - TAUX_TVA : constante globale (0.2)
   - SEUIL_ADMISSION : constante globale (10)
   - moyenne(notes) : calcul de moyenne
   - est_admis(note, seuil) : test d'admission
   - prix_ttc(prix_ht, taux) : calcul TTC
   - formater_rapport(notes) : génération de rapport
   - Bloc de tests rapides

2. Fichier app.ipynb (application principale)
   - Import du module utils (deux méthodes)
   - Données de test (notes et prix)
   - Fonction main() : orchestration
   - Appels de fonctions du module
   - Affichage des résultats

3. Structure des fichiers
   Lab8/
   ├── utils.py
   └── app.ipynb
```

---

## Installation

Cloner le projet :
```bash
git clone https://github.com/benhirtfatimaezzahra/Lab8.git
```

Naviguer dans le dossier :
```bash
cd Lab8
```

Exécuter l'application :
```bash
python app.ipynb
```

---



## Notes Techniques

### Concepts Python utilisés
- **Modules personnalisés** : création de `utils.py` réutilisable
- **Imports multiples** : `import utils` vs `from utils import`
- **Constantes globales** : `TAUX_TVA`, `SEUIL_ADMISSION` en majuscules
- **Docstrings de module** : documentation au début du fichier
- **Docstrings de fonctions** : description de chaque fonction
- **Paramètres par défaut** : `seuil=SEUIL_ADMISSION`, `taux=TAUX_TVA`
- **`if __name__ == "__main__"`** : tests conditionnels
- **Fonction main()** : point d'entrée structuré
- **List comprehensions** : `[note for note in notes if est_admis(note)]`

## Démonstration



https://github.com/user-attachments/assets/6f4788c9-1748-44d3-8c2f-d5cdefc1de8b


---

## Auteur

**Nom :** Benhirt Fatima Ezzahra  
**Cours :** Introduction à Python  
**Date :** Decembre 2025  
**Encadré par :** Pr. Mohamed LACHGAR
