# main.py

from src.definir_besoin import definir_besoin
from src.creer_profil import creer_profil
from src.rediger_annonce import rediger_annonce
from src.selectionner_candidats import selectionner_candidats
from src.entretien_candidats import entretien_candidats

def main():
    # Spécifiez les chemins des fichiers
    chemin_besoin_recrutement = "data/besoin_recrutement.json"  # Par exemple, un fichier JSON pour stocker les besoins de recrutement
    chemin_fichier_candidatures = "data/base_candidatures.csv"
    chemin_fichier_annonce = "data/annonce_recrutement.txt"

    # Étape 1: Définir les besoins
    besoin_recrutement = definir_besoin(chemin_besoin_recrutement)

    # Étape 2: Créer le profil du candidat
    creer_profil(besoin_recrutement)

    # Étape 3: Rédiger l'annonce
    rediger_annonce(besoin_recrutement, chemin_fichier_annonce)

    # Étape 4: Sélectionner les candidats
    candidats_selectionnes = selectionner_candidats(besoin_recrutement, chemin_fichier_candidatures)

    # Étape 5: Entretiens avec les candidats
    entretien_candidats(candidats_selectionnes, besoin_recrutement)

if __name__ == "__main__":
    main()
