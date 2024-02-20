import streamlit as st
import time
import pandas as pd
import os

# login.user_info()

def spacer(n, line=True) :
  for i in range(n+1):
    st.write("")
  if line :
    "---"

"# Bienvenue sur les fiches amas de Marion🎈"

st.sidebar.write("Choix de l'année de la fiche :")
selected_date  = st.sidebar.selectbox("Date de MAJ de la fiche :", ["2023", "2024"], index=1)
st.sidebar.write("Choix du site :")
selected_site  = st.sidebar.selectbox("selection du site :", ["Thio Plateau","Thio Camps des sapins", "Népoui", "Kouaoua"], index=1)
if selected_site == "Thio Plateau":
  selected_amas  = st.sidebar.selectbox("selection de l'amas :", ["belvedere", "clemence", "gsp", "santamaria"], index=1)
elif selected_site == "Thio Camps des sapins":
  selected_amas  = st.sidebar.selectbox("selection de l'amas :", ["3piments", "pt171"], index=1)
elif selected_site == "Népoui":
  selected_amas  = st.sidebar.selectbox("selection de l'amas :", ["ballantine", "bernablanche", "krans", "montvert", "paidi", "surprise4"], index=1)
elif selected_site == "Kouaoua":
  selected_amas  = st.sidebar.selectbox("selection de l'amas :", ["ednkarembe", "extpentecost", "marmelade", "nordmea", "sousbureaux", "stamboul"], index=1)
elif selected_site == "Poro":
  selected_amas  = st.sidebar.selectbox("selection de l'amas :", ["bonini", "francaise", "mecoyamatos"], index=1)
elif selected_site == "Thiebagui":
  selected_amas  = st.sidebar.selectbox("selection de l'amas :", ["alpha", "dome"], index=1)
elif selected_site == "Tontouta":
  selected_amas  = st.sidebar.selectbox("selection de l'amas :", ["colthomp", "fernandepaul"], index=1)
elif selected_site == "Dothio":
  selected_amas  = st.sidebar.selectbox("selection de l'amas :", ["pauline", "revanche"], index=1)

# file_path_text_generalite = os.path.join("Fiches Amas", selected_site, selected_amas, "generalite.txt")

# # Vérifier si le fichier existe
# if os.path.exists(file_path):
#     # Lire le contenu du fichier texte
#     with open(file_path, 'r') as file:
#         text_content = file.read()

#     # Afficher le contenu du fichier texte
#     st.text("Contenu du fichier texte :")
#     st.text(text_content)
# else:
#     st.error("Le fichier 'tata.txt' n'a pas été trouvé dans le dossier 'toto'.")

if st.sidebar.button("voir la fiche"):
  st.write("Vous consultez le site de",selected_site,"et l'amas",selected_amas, "sur l'année",selected_date)  
  tabs = st.tabs(["Généralités", "Environnement", "Acquisition des données", "Modèle d'estimation", "Projet Opti", "Reserves", "Reconciliation", "Validation"])
  
  with tabs[0]:
    st.write(f"Contenu de l'onglet 'toto' pour la date {selected_date}")
    
    container=st.container()
    container.write("aaa")
  with tabs[1]:
      st.write(f"Contenu de l'onglet 'tata' pour la date {selected_date}")

