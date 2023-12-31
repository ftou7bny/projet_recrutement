# matching_processor.py

from src.cv_processor import calculate_similarity, filter_cvs
from src.file_manager import read_annonce
from src.data import annonces  # Ajoutez l'importation de la variable annonces
from os.path import isfile  # Importez la fonction isfile depuis le module os
import csv


def find_best_matching_cv(poste, cvs_data):
    annonce_file_name = f"{poste}_annonce.txt"

    # Ajoutez cette vérification pour s'assurer que le fichier d'annonce existe
    if not isfile(annonce_file_name):
        print(f"Le fichier d'annonce '{annonce_file_name}' n'existe pas.")
        return None, None

    # Lire le fichier annonce pour obtenir les mots clés
    annonce_keywords, _, _ = read_annonce(annonce_file_name)

    best_match = None
    best_similarity = 0

    for cv_filename, cv_content in cvs_data.items():
        similarity = calculate_similarity(annonce_keywords, cv_content)
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = cv_filename

    return best_match, best_similarity

import csv
from src.file_manager import load_existing_data

def save_matching_results(matches, csv_file_path):
    try:
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Poste", "CV Correspondant", "Similarité"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Écrivez l'en-tête du fichier CSV
            writer.writeheader()

            # Écrivez chaque ligne de données
            for match in matches:
                writer.writerow({"Poste": match[0], "CV Correspondant": match[1], "Similarité": match[2]})

            print(f"Les résultats du matching ont été enregistrés dans {csv_file_path}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'enregistrement des résultats : {str(e)}")



def find_best_matching_cv_and_save(poste, cv_directory, output_csv):
    annonce_keywords, _, _ = use_existing_annonce()

    if annonce_keywords is not None:
        filtered_cvs = filter_cvs(annonce_keywords, cv_directory)

        if filtered_cvs:
            # Créer un tableau pour stocker les résultats
            results = [("CV Path", "Similarity")]

            for cv_text, similarity, cv_path in filtered_cvs:
                print(f"CV trouvé : {cv_path} avec une similarité de {similarity}")
                
                # Ajouter le résultat au tableau
                results.append((cv_path, similarity))

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

            # Enregistrer les résultats dans un fichier CSV
            with open(output_csv, "w", newline="", encoding="utf-8") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(results)
            print(f"Résultats enregistrés dans le fichier CSV : {output_csv}")
        else:
            print("Aucun CV correspondant trouvé.")
    else:
        print("Aucune annonce existante.")
