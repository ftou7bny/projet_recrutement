# cv_processor.py
import re
import pandas as pd
import numpy as np
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from src.file_manager import read_annonce_keywords
import fitz  # PyMuPDF
from .file_manager import read_annonce_keywords


nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    if isinstance(text, list):
        words = [word.lower() for sublist in text for word in sublist if word.isalnum()]
    else:
        words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def calculate_similarity(annonce_keywords, cv_text):
    try:
        # Convertir la liste de mots-clés en une chaîne de caractères
        annonce_keywords_str = " ".join(annonce_keywords)

        # Utiliser TfidfVectorizer pour représenter les documents en vecteurs TF-IDF
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([annonce_keywords_str, cv_text])

        # Calculer la similarité du cosinus entre les deux vecteurs
        cosine_sim = linear_kernel(tfidf_matrix[0], tfidf_matrix[1])

        return cosine_sim[0][0]
    except Exception as e:
        print(f"Une erreur s'est produite lors du calcul de la similarité : {str(e)}")
        return 0.0

def extract_keywords_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        keywords = set()

        for page_num in range(doc.page_count):
            page = doc[page_num]
            page_text = page.get_text("text")
            
            # Ajoutez votre logique pour extraire des mots-clés spécifiques à partir du texte de la page.
            # Par exemple, utilisez des expressions régulières ou une autre logique de traitement.
            # Ajoutez ces mots-clés à l'ensemble keywords.

        return keywords
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'extraction des mots-clés du CV {pdf_path}: {str(e)}")
        return set()


def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'extraction du texte du CV {pdf_path}: {str(e)}")
        return ""
    

# ...
def filter_cvs(annonce_keywords, cv_directory):
    try:
        filtered_cvs = []

        df = pd.DataFrame()

        for cv_file in os.listdir(cv_directory):
            df_per_cv = pd.DataFrame()
            cv_path = os.path.join(cv_directory, cv_file)
            cv_text = extract_text_from_pdf(cv_path)
            similarity = calculate_similarity(annonce_keywords, cv_text)
            print(f"Similarité pour {cv_path} : {similarity}")
            df_per_cv["keyword"] = annonce_keywords
            df_per_cv["main_cv"] = re.sub(r'^.+[\\\/]|\.pdf$', '', os.path.basename(cv_path))

            df_per_cv["similarity"] = np.NaN
            if similarity > 0.01:
                filtered_cvs.append((cv_text, similarity, cv_path))
                df_per_cv["similarity"] = similarity
            df=pd.concat([df,df_per_cv])
        filtered_cvs.sort(key=lambda x: x[1], reverse=True)
        print(df)
        df.to_csv("simularity_file.csv",index=False)
        return filtered_cvs
    
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

#keyword main_cv Similarity

