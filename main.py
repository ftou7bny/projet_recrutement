from src.matching_processor import find_best_matching_cv_and_save
from src.file_manager import (
    list_existing_annonces,
    read_annonce,
    save_annonce_to_file,
    generate_job_description_paragraph,
    save_annonce_to_data_file,
    save_to_csv,  # Ajoutez cette ligne pour importer la fonction save_to_csv
)
from src.data import annonces  # Assurez-vous d'avoir la variable annonces ici
from src.cv_processor import filter_cvs
import os

# ...

def create_annonce_keywords():
    return input("Entrez les mots clés de l'annonce (séparés par des espaces) : ")


def create_annonce_details():
    missions = input("Entrez les missions du poste : ")
    conditions_travail = input("Entrez les conditions de travail : ")
    competences_recherchees = input("Entrez les compétences recherchées : ")
    diplome_requis = input("Entrez le diplôme requis : ")
    diplomes_acceptables = input("Entrez les diplômes acceptables : ")
    experience_min = input("Entrez l'expérience minimale requise : ")
    delai_prise_fonction = input("Entrez le délai de prise de fonction : ")
    salaire_estime = input("Entrez le salaire estimé : ")
    avantages_entreprise = input("Entrez les avantages de l'entreprise : ")
    avantages_poste = input("Entrez les avantages du poste : ")

    annonce_details = f"\nMissions : {missions}\nConditions de travail : {conditions_travail}\n" \
                      f"Compétences recherchées : {competences_recherchees}\nDiplôme requis : {diplome_requis}\n" \
                      f"Diplômes acceptables : {diplomes_acceptables}\nExpérience minimale requise : {experience_min}\n" \
                      f"Délai de prise de fonction : {delai_prise_fonction}\nSalaire estimé : {salaire_estime}\n" \
                      f"Avantages de l'entreprise : {avantages_entreprise}\nAvantages du poste : {avantages_poste}\n"

    return annonce_details


def save_annonce_to_data(poste, annonce_keywords, annonce_details):
    annonces[poste] = {
        "keywords": annonce_keywords,
        "details": annonce_details,
    }

def save_annonce_to_file(poste, annonce_keywords, annonce_details, filename):
    directory = os.path.join("data", "annonces")
    filepath = os.path.join(directory, filename)

    # Créer le répertoire s'il n'existe pas
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"Mots clés de l'annonce : {annonce_keywords}")
            file.write(annonce_details)
            file.write(generate_job_description_paragraph(poste, annonce_details))

        save_annonce_to_data(poste, annonce_keywords, annonce_details)

        print(f"L'annonce a été enregistrée dans le fichier {filepath}")
    except FileNotFoundError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")



def write_annonces_to_data_file(filename):
    with open("data.py", "w", encoding="utf-8") as file:
        file.write("annonces = {\n")
        for poste, details in annonces.items():
            keywords = details["keywords"]
            file.write(f'    "{poste}": {{"keywords": "{keywords}", "details": """{details["details"]}"""}},\n')
        file.write("}\n")

    print(f"Données d'annonces mises à jour dans le fichier data.py")
    print(f"Le fichier d'annonce a été enregistré ici : {filename}")

def use_existing_annonce():
    annonce_files = list_existing_annonces()

    if not annonce_files:
        print("Aucun fichier d'annonce existant.")
        return None, None

    print("Annonces existantes :")
    for i, annonce_file in enumerate(annonce_files, start=1):
        print(f"{i}. {annonce_file}")

    choice = int(input("Choisissez le numéro du fichier d'annonce que vous souhaitez utiliser : "))

    if 1 <= choice <= len(annonce_files):
        selected_annonce_file = annonce_files[choice - 1]
        annonce_keywords, poste, annonce_details = read_annonce(selected_annonce_file)
        print(f"Les mots clés de l'annonce '{selected_annonce_file}' ont été chargés.")
        print(f"Details de la poste :\n{annonce_details}")
        return annonce_keywords, poste, annonce_details
    else:
        print("Choix invalide.")
        return None, None, None
if __name__ == "__main__":
    while True:
        cv_directory = os.path.join("data", "cv")
        print("  Annonces  (1) ")
        print("  CV        (2) ")

        option = input("Choisissez une option (1 ou 2) : ")

        if option == "1":
            print(" Créer une nouvelle annonce                  (1)")
            print(" Utiliser/Modifier une annonce existante     (2)")
           
            sub_option = input("Choisissez une option (1 ou 2) : ")
           
            if sub_option == "1":
                annonce_keywords = create_annonce_keywords()
                poste = input("Entrez le nom du poste : ")
                annonce_details = create_annonce_details()
                filename = f"{poste}_annonce.txt"
                save_annonce_to_file(poste, annonce_keywords, annonce_details, filename)
                save_annonce_to_data(poste, annonce_keywords, annonce_details)
                write_annonces_to_data_file(filename)

                find_best_matching_cv_and_save(poste, cv_directory, "matching_results.csv")

            elif sub_option == "2":
                annonce_keywords, poste, annonce_details = use_existing_annonce()

                if annonce_keywords is not None:
                    print(f"CV Directory: {cv_directory}")
                    filtered_cvs = filter_cvs(annonce_keywords, cv_directory)
        
                    modify_option = input("Voulez-vous modifier cette annonce ? (Oui/Non) : ").lower()

                    if modify_option == "oui":
                        annonce_keywords = create_annonce_keywords()
                        annonce_details = create_annonce_details()
                        save_annonce_to_file(poste, annonce_keywords, annonce_details, f"{poste}_annonce.txt")
                        save_annonce_to_data(poste, annonce_keywords, annonce_details)
                        print(f"L'annonce '{poste}' a été modifiée avec succès.")
                        
                        find_best_matching_cv_and_save(poste, cv_directory, "matching_results.csv")

                    else:
                        print("Aucune modification apportée.")

        elif option == "2":
            while True:
                print("1. Créer/Modifier une annonce")
                print("2. Rechercher un CV")

                sub_option = input("Choisissez une option (1 ou 2) : ")

                if sub_option == "1":
                    print("option 1 : 1 ")
                elif sub_option == "2":
                    search_option = input(
                        "Utiliser des mots-clés existants dans une annonce (1) ou entrer des mots-clés manuellement (2) ? ")

                    if search_option == "1":
                        annonce_keywords, _, _ = use_existing_annonce()
                        if annonce_keywords is not None:
                            print(f"CV Directory: {cv_directory}")
                            filtered_cvs = filter_cvs(annonce_keywords, cv_directory)
                            if filtered_cvs:
                                for cv_text, similarity, cv_path in filtered_cvs:
                                    print(f"CV trouvé : {cv_path} avec une similarité de {similarity}")

                                output_csv = "matching_results.csv"
                                find_best_matching_cv_and_save(poste, cv_directory, output_csv)
                            
                                cv_choice = input("Voulez-vous voir le détail d'un CV filtré ? (Oui/Non) : ").lower()
                                if cv_choice == "oui":
                                    cv_index = int(input("Entrez le numéro du CV que vous souhaitez voir : "))
                                    if 1 <= cv_index <= len(filtered_cvs):
                                        selected_cv = filtered_cvs[cv_index - 1]
                                        print(f"Détail du CV sélectionné :\n{selected_cv[0]}")
                                    else:
                                        print("Numéro de CV invalide.")
                                else:
                                    print("Aucune action supplémentaire effectuée.")

                            else:
                                print("Aucun CV correspondant trouvé.")

                        else:
                            print("Aucune annonce existante.")

                    elif search_option == "2":
                        custom_keywords = input("Entrez les mots-clés de recherche (séparés par des espaces) : ")
                        
                        # Modification ici pour traiter les mots-clés même s'ils contiennent des espaces
                        annonce_keywords = custom_keywords.split()

                        filtered_cvs = filter_cvs(annonce_keywords, cv_directory)

                        if filtered_cvs:
                            # Omet l'affichage des CVs filtrés
                            # for cv_text, similarity, cv_path in filtered_cvs:
                            #     print(f"CV trouvé : {cv_path} avec une similarité de {similarity}")

                            cv_choice = input("Voulez-vous voir le détail d'un CV filtré ? (Oui/Non) : ").lower()
                            if cv_choice == "oui":
                                cv_index = int(input("Entrez le numéro du CV que vous souhaitez voir : "))
                                if 1 <= cv_index <= len(filtered_cvs):
                                    selected_cv = filtered_cvs[cv_index - 1]
                                    print(f"Détail du CV sélectionné :\n{selected_cv[0]}")
                                else:
                                    print("Numéro de CV invalide.")
                            else:
                                print("Aucune action supplémentaire effectuée.")

                        else:
                            print("Aucun CV correspondant trouvé.")

                    else:
                        print("Option invalide. Veuillez choisir 1 ou 2.")
                else:
                    print("Option invalide. Veuillez choisir 1 ou 2.")
