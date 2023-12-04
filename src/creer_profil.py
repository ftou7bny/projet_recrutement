# creer_profil.py

import os
from pdfminer.high_level import extract_text

def extraire_infos_de_cv(chemin_du_cv):
    # Fonction pour extraire des informations à partir d'un CV au format PDF
    infos = {}
    
    # Extraire le texte du CV
    texte_cv = extract_text(chemin_du_cv)

    # Analyser le texte du CV pour extraire les informations nécessaires
    infos["nom"] = extraire_info(texte_cv, "Nom:")
    infos["experience"] = extraire_info(texte_cv, "Expérience:")
    infos["education"] = extraire_info(texte_cv, "Éducation:")

    return infos

def extraire_info(texte, balise):
    # Fonction pour extraire une information spécifique du CV
    debut_info = texte.find(balise) + len(balise)
    fin_info = texte.find("\n", debut_info)
    return texte[debut_info:fin_info].strip()

def creer_profil(chemin_du_cv):
    """
    Cette fonction crée le profil du candidat en se basant sur les informations extraites du CV.
    """
    print("\nCréation du profil du candidat en fonction des informations extraites du CV.")

    # Chemin complet vers le fichier PDF du CV
    chemin_complet_cv = os.path.join("cv", chemin_du_cv)

    # Extraire les informations du CV
    infos_cv = extraire_infos_de_cv(chemin_complet_cv)

    # Créer le profil du candidat
    profil_candidat = {
        "nom": infos_cv.get("nom", ""),
        "experience": infos_cv.get("experience", ""),
        "education": infos_cv.get("education", ""),
        # Ajoutez d'autres informations pertinentes extraites du CV
    }

    # Afficher le profil du candidat
    print("\nProfil du candidat basé sur les informations extraites du CV :")
    for cle, valeur in profil_candidat.items():
        print(f"{cle.capitalize()}: {valeur}")

    # Enregistrer le profil dans un fichier texte
    enregistrer_profil_dans_fichier(profil_candidat)

    return profil_candidat

def enregistrer_profil_dans_fichier(profil_candidat):
    # Fonction pour enregistrer le profil dans un fichier texte
    chemin_fichier = os.path.join("data", "profil_candidat.txt")
    with open(chemin_fichier, "a") as fichier:
        fichier.write("\nProfil du candidat :\n")
        for cle, valeur in profil_candidat.items():
            fichier.write(f"{cle.capitalize()}: {valeur}\n")
# ...

if __name__ == "__main__":
    # Exemple d'utilisation avec le fichier PDF du CV nommé "cv.pdf" dans le dossier "cv/"
    chemin_du_cv_pdf = "cv.pdf"
    creer_profil(chemin_du_cv_pdf)
