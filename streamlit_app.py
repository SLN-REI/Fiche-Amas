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
  
selected_date  = st.sidebar.selectbox("Date de MAJ de la fiche :", ["2023", "2024"], index=1)

if st.sidebar.button("voir la fiche"):
  st.write("Vous consultez le site de",selected_site,"et l'amas",selected_amas, "sur l'année",selected_date)  
  tabs = st.tabs(["toto", "tata"])
  
  with tabs[0]:
      st.write(f"Contenu de l'onglet 'toto' pour la date {selected_date}")
  with tabs[1]:
      st.write(f"Contenu de l'onglet 'tata' pour la date {selected_date}")
    



st.button("True of False, but back to False on next run")
