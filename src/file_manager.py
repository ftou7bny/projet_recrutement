# src/file_manager.py

import csv
import os
from src.data import annonces
import pickle
from unidecode import unidecode



def load_existing_data():
    annonces_file = "data.py"
    cvs_file = "cvs.pkl"

    if os.path.exists(annonces_file) and os.path.exists(cvs_file):
        # Charger les annonces à partir du fichier data.py
        with open(annonces_file, "r", encoding="utf-8") as file:
            content = file.read()
            annonces = eval(content) if content else {}

        # Charger les CVs à partir du fichier cvs.pkl
        with open(cvs_file, "rb") as file:
            cvs = pickle.load(file)

        return annonces, cvs
    else:
        # Retournez des valeurs par défaut si les fichiers n'existent pas
        return {}, {}


def list_existing_annonces():
    annonces_directory = os.path.join("data", "annonces")
    
    # Liste des fichiers dans le répertoire racine
    annonce_files_root = [file.strip() for file in os.listdir() if file.endswith("_annonce.txt")]
    
    # Liste des fichiers dans le répertoire data/annonces
    annonce_files_data = [os.path.join("data", "annonces", file.strip()) for file in os.listdir(annonces_directory) if file.endswith("_annonce.txt")]

    return annonce_files_root + annonce_files_data


def read_annonce(file_name):
    with open(file_name, "r", encoding="latin-1") as file:
        lines = file.readlines()
        annonce_keywords = lines[0].replace("Mots clés de l'annonce : ", '').strip()
        poste = file_name.replace('_annonce.txt', '')
        annonce_details = "\n".join(lines[1:]).strip()
        return annonce_keywords, poste, annonce_details


def read_annonce_keywords(file_name):
    with open(file_name, "r", encoding="latin-1") as file:
        # Les mots clés de l'annonce sont la première ligne du fichier
        keywords_line = file.readline().replace("Mots clés de l'annonce : ", '').strip()
        # Utilisez unidecode pour normaliser les caractères accentués
    return keywords_line.split()

def save_annonce_to_data_file(poste, annonce_keywords, annonce_details):
    # Code pour sauvegarder l'annonce dans la structure de données
    annonces[poste] = {
        "keywords": annonce_keywords,
        "details": annonce_details,
    }

    # ...


def save_to_csv(filtered_cvs, csv_filename):
    try:
        with open(csv_filename, mode='w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['CV Path', 'Similarity'])

            for cv_text, similarity, cv_path in filtered_cvs:
                csv_writer.writerow([cv_path, similarity])

        print(f"Données enregistrées dans le fichier CSV : {csv_filename}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'enregistrement dans le fichier CSV : {str(e)}")


# Supprimez la première occurrence de os.path.join
    
def save_annonce_to_file(poste, annonce_keywords, annonce_details, filename):
    filepath = os.path.join("data", "annonces", filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(f"Mots clés de l'annonce : {annonce_keywords}")
        file.write(annonce_details)
        file.write(generate_job_description_paragraph(poste, annonce_details))

    save_annonce_to_data_file(poste, annonce_keywords, annonce_details)

    print(f"L'annonce a été enregistrée dans le fichier {filepath}")


# Ajout de la fonction generate_job_description_paragraph
def generate_job_description_paragraph(poste, annonce_details):
    # Utilisez les informations fournies pour générer la description du poste
    missions, conditions_travail, competences_recherchees, diplome_requis, diplomes_acceptables, \
        experience_min, delai_prise_fonction, salaire_estime, avantages_entreprise, avantages_poste = annonce_details.split("\n")[1:-1]

    # Générez le paragraphe de la description du poste
    job_description_paragraph = f"\n\n🚀 **Opportunité Passionnante en {poste.capitalize()} chez DRF**\n\n" \
                                f"Nous sommes à la recherche d'un talentueux {poste} pour rejoindre notre équipe dynamique chez [Nom de l'Entreprise]. " \
                                f"Si vous êtes passionné par la technologie et souhaitez contribuer au succès de projets informatiques stimulants, alors cette opportunité est faite pour vous !\n\n" \
                                f"**Missions :**\n{missions}\n\n" \
                                f"**Conditions de travail :**\n{conditions_travail}\n\n" \
                                f"**Compétences Recherchées :**\n{competences_recherchees}\n\n" \
                                f"**Diplôme Requis :**\n{diplome_requis}\n\n" \
                                f"**Diplômes Acceptables :**\n{diplomes_acceptables}\n\n" \
                                f"**Expérience Minimale Requise :**\n{experience_min}\n\n" \
                                f"**Délai de Prise de Fonction :**\n{delai_prise_fonction}\n\n" \
                                f"**Salaire Estimé :**\n{salaire_estime}\n\n" \
                                f"**Avantages de l'Entreprise :**\n{avantages_entreprise}\n\n" \
                                f"**Avantages du Poste :**\n{avantages_poste}\n\n" \
                                f"Si vous êtes passionné par le {poste}, que vous avez les compétences requises et que vous recherchez une opportunité stimulante, postulez dès aujourd'hui ! " \
                                f"Nous avons hâte de découvrir votre talent et de vous accueillir dans notre équipe.\n\n" \
                                f"#OpportunitéEmploi #{poste.capitalize()} #{poste.capitalize()}Opportunity #{poste.capitalize()}Jobs\n"

    return job_description_paragraph
