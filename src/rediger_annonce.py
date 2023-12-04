# src/rediger_annonce.py

def rediger_annonce(besoin_recrutement, chemin_fichier_annonce):
    """
    Cette fonction rédige une annonce de recrutement en se basant sur les besoins définis.
    """
    print("\nRédaction de l'annonce de recrutement.")

    # Extraire les informations du besoin de recrutement
    missions = besoin_recrutement["missions"]
    conditions_travail = besoin_recrutement["conditions_travail"]
    competences_recherchees = besoin_recrutement["competences_recherchees"]
    diplome_requis = besoin_recrutement["diplome_requis"]
    delai_prise_fonction = besoin_recrutement["delai_prise_fonction"]
    salaire_estime = besoin_recrutement["salaire_estime"]
    avantages_entreprise = besoin_recrutement["avantages_entreprise"]
    avantages_poste = besoin_recrutement["avantages_poste"]

    # Rédaction de l'annonce
    annonce = f"""L'entreprise XYZ recherche un nouveau membre pour rejoindre notre équipe !

... (Reste du contenu de la fonction rediger_annonce)

Pour postuler, envoyez votre CV et votre lettre de motivation à [adresse_email@example.com].
"""

    # Afficher l'annonce
    print(annonce)

    # Enregistrer l'annonce dans un fichier
    with open(chemin_fichier_annonce, 'w') as fichier_annonce:
        fichier_annonce.write(annonce)

    print(f"L'annonce a été enregistrée dans {chemin_fichier_annonce}.")
