import streamlit as st
import time
import pandas as pd

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
  selected_amas  = st.sidebar.selectbox("selection du site :", ["belvedere", "clemence", "gsp", "santamaria"], index=1)
if selected_site == "Thio Camps des sapins":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["3piments", "pt171"], index=1)
if selected_site == "Népoui":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["ballantine", "bernablanche", "krans", "montvert", "paidi", "surprise4"], index=1)
if selected_site == "Kouaoua":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["ednkarembe", "extpentecost", "marmelade", "nordmea", "sousbureaux", "stamboul"], index=1)
if selected_site == "Poro":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["bonini", "francaise", "mecoyamatos"], index=1)
if selected_site == "Thiebagui":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["alpha", "dome"], index=1)
if selected_site == "Tontouta":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["colthomp", "fernandepaul"], index=1)
if selected_site == "Dothio":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["pauline", "revanche"], index=1)

if st.sidebar.button("voir la fiche"):
  st.write("Vous consultez le site de",selected_site,"et l'amas",selected_amas, "sur l'année",selected_date)  
  tabs = st.tabs(["Généralités", "Environnement", "Acquisition des données", "Modèle d'estimation", "Projet Opti", "Reserves", "Reconciliation", "Validation"])
  
  with tabs[0]:
    st.write(f"Contenu de l'onglet 'toto' pour la date {selected_date}")
    
    container=st.container()
    container.write("Le gisement est situé au cœur du Plateau de Thio sur la rive gauche de la rivière Thio. Il est cerné par les grandes structures traversant ce plateau : la N50 de Sans Culotte et la N140 de Clémence ainsi qu'une structure N140 au sud-ouest.  La topographie d'origine était celle d'une dépression de grande taille entouré par des mamelons de roches dures ou saines, sous les murs des failles majeures.  A l'ouest il y une zone bréchique siliceuse et la minéralisation y est erratique. L'altération est majoritairement de type altéré dur, issu des harzburgites de faciès normal 
(FICHE_RER _AMAS_2018_MT_PLT_GRAND_SAINT_PIERRE)


L’altitude moyenne du Plateau est comprise entre 500 et 550 m. Ce plateau comporte des petits dômes de péridotites, vestiges d’une surface plus élevée aujourd’hui démantelée. Les sommets de ces dômes peuvent atteindre 650 m.
- Le gisement de BELVEDERE OUEST se situe à la pointe Sud Est du plateau de Thio.
- L'amas de BELVEDERE EST se situe à la pointe Sud Est du plateau de Thio.
- Le gisement CLEMENCE est situé au Nord du Plateau de Thio.
- L'amas DUC DE WELLINGTON se situe à environ 600m à l'est de l'amas CLEMENCE.
- L’amas HAPPY GO LUCKY est situé dans le domaine de Thio Plateau, à environ 1.5 km à vol d’oiseau, au Nord-Ouest du « Tritout ». Cet amas marque l’extrémité Nord-Ouest du Plateau de Thio. Happy Go Lucky est constitué de trois lignes de crêtes de direction NW-SE, reliées entre elles vers le Sud où elles forment un vaste plateau latéritique. L’altitude varie entre 300 et 600 m.
- L'amas SANTA MARIA constitue la portion Ouest de la cuvette de la fosse SAINT PIERRE située sur le plateau de Thio. - L'amas LOUISE est dans la continuité Nord de Santa Maria.
- Le gisement de GRAND SAINT PIERRE est situé au cœur du Plateau de Thio sur la rive gauche de la rivière Thio.
(Rapport_declaration2020_Ressources&Reserves_JORC_THIO_210331_PLAN5&10ANS_final)


Le plateau de Thio est constitué d’un ensemble de péridotites constitué de harzburgites et de dunites partiellement serpentinisées où dominent principalement les harzburgites. Au sein de cet ensemble, s’intercalent parfois des niveaux centimétriques de pyroxénolites et des niveaux dunitiques qui eux, peuvent atteindre des épaisseurs de plusieurs dizaines de mètres. Ces différents éléments définissent le rubanement. Les directions et pendages moyens mesurés sur le rubanement sont de 125°E à pendage 40°N sur l’ensemble du plateau, avec une intensité variable et croissante du NE vers le SW.
Ce massif repose sur un substratum volcanique basaltique (Paléocène – Eocène) selon un contact anormal souligné par une silicification intense de la semelle constituée de serpentinites mylonitisées. 
(Ra-11-0497_C_PLT_PE_V2)
")
  with tabs[1]:
      st.write(f"Contenu de l'onglet 'tata' pour la date {selected_date}")
    



st.button("True of False, but back to False on next run")
