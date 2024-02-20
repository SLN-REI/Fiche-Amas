import streamlit as st
from f import login
import time
import pandas as pd

login.user_info()

def spacer(n, line=True) :
  for i in range(n+1):
    st.write("")
  if line :
    "---"

"# Bienvenue sur les fiches amas 🎈"

st.sidebar.write("Choix du site :")
selected_date  = st.sidebar.selectbox("Date de MAJ de la fiche :", ["2023","2024"], index=1)

if st.sidebar.button("Thio Plateau"):
    st.write("Vous avez appuyé sur le Bouton 1")

if st.sidebar.button("Bouton 2"):
    st.write("Vous avez appuyé sur le Bouton 2")

if st.sidebar.button("Bouton 3"):
    st.write("Vous avez appuyé sur le Bouton 3")
    



st.button("True of False, but back to False on next run")

with st.expander("Plus de parametres") :
"Plein de widgets"
