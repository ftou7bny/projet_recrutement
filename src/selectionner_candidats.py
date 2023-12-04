# src/selectionner_candidats.py

import csv

def lire_candidatures_depuis_csv(chemin_fichier):
    candidatures = []

    try:
        with open(chemin_fichier, mode='r', newline='') as fichier_csv:
            lecteur_csv = csv.DictReader(fichier_csv)
            for ligne in lecteur_csv:
                candidatures.append(ligne)
    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier} n'existe pas. Aucune candidature n'a été lue.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")

    return candidatures

def ecrire_candidatures_dans_csv(chemin_fichier, candidatures):
    try:
        with open(chemin_fichier, mode='w', newline='') as fichier_csv:
            champs = ["nom", "experience", "diplome"]
            ecrivain_csv = csv.DictWriter(fichier_csv, fieldnames=champs)
            ecrivain_csv.writeheader()
            ecrivain_csv.writerows(candidatures)
        print(f"Les candidatures ont été enregistrées dans {chemin_fichier}.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'écriture du fichier : {e}")

# src/selectionner_candidats.py

def selectionner_candidats(besoin_recrutement, chemin_fichier_candidatures):
    # Logique de sélection des candidats...
    candidats_selectionnes = [...]  # Mettez ici votre logique de sélection

    # Appel à la fonction pour écrire les candidatures dans le fichier CSV
    ecrire_candidatures_dans_csv(chemin_fichier_candidatures, candidats_selectionnes)

    return candidats_selectionnes  # Assurez-vous de retourner la liste des candidats sélectionnés
