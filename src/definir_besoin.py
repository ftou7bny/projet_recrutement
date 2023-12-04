# src/definir_besoin.py

def definir_besoin(chemin_besoin_recrutement=None):
    """
    Cette fonction permet de définir les besoins de recrutement en demandant à l'utilisateur
    de fournir les informations nécessaires.
    """
    besoin_recrutement = {}

    print("Bienvenue dans le processus de définition des besoins de recrutement.")

    # Demander à l'utilisateur de fournir les informations nécessaires
    besoin_recrutement["missions"] = input("Quelles seront les missions du salarié ? ")
    besoin_recrutement["conditions_travail"] = input("Quelles seront les conditions de travail ? ")
    besoin_recrutement["competences_recherchees"] = input("Quelles sont les compétences que vous recherchez ? ")
    besoin_recrutement["diplome_requis"] = input("Le salarié devra-t-il être diplômé ? (oui/non) ").lower() == "oui"
    
    if besoin_recrutement["diplome_requis"]:
        besoin_recrutement["diplomes_acceptables"] = input("Quels diplômes pourraient convenir ? ")
    else:
        besoin_recrutement["experience_min"] = input("Quelle expérience minimale dans le même poste estimez-vous suffisante ? ")

    besoin_recrutement["delai_prise_fonction"] = input("Quel est le délai de prise de fonction ? ")
    besoin_recrutement["salaire_estime"] = float(input("Quel est le salaire moyen que vous estimez pouvoir offrir ? "))
    besoin_recrutement["avantages_entreprise"] = input("Quels sont les autres avantages offerts par votre entreprise ? ")
    besoin_recrutement["avantages_poste"] = input("Quels sont les autres avantages spécifiques au poste ? ")

    # Afficher les informations saisies par l'utilisateur
    print("\nRécapitulatif des besoins de recrutement :")
    for cle, valeur in besoin_recrutement.items():
        print(f"{cle.capitalize()}: {valeur}")

    # Enregistrer les besoins dans un fichier ou une base de données si nécessaire

    return besoin_recrutement
