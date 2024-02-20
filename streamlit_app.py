import streamlit as st
import time
import pandas as pd

# login.user_info()

def spacer(n, line=True) :
  for i in range(n+1):
    st.write("")
  if line :
    "---"

"# Bienvenue sur les fiches amas 🎈"

st.sidebar.write("Choix du site :")
selected_site  = st.sidebar.selectbox("selection du site :", ["Thio Plateau","Thio Camps des sapins", "Népoui", "Kouaoua"], index=1)
if selected_site == "Thio Plateau":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["GSP", "Santa Maria", "Clémence", "Belvédère"], index=1)
if selected_site == "Thio Camps des sapins":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["GSP", "Santa Maria", "Clémence", "Belvédère"], index=1)
if selected_site == "Népoui":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["GSP", "Santa Maria", "Clémence", "Belvédère"], index=1)
if selected_site == "Kouaoua":
  selected_amas  = st.sidebar.selectbox("selection du site :", ["GSP", "Santa Maria", "Clémence", "Belvédère"], index=1)

selected_date  = st.sidebar.selectbox("Date de MAJ de la fiche :", ["2023","2024"], index=1)

if st.sidebar.button("Thio Plateau"):
    st.write("Vous avez appuyé sur le Bouton 1")

if st.sidebar.button("Bouton 2"):
    st.write("Vous avez appuyé sur le Bouton 2")

if st.sidebar.button("Bouton 3"):
    st.write("Vous avez appuyé sur le Bouton 3")
    



st.button("True of False, but back to False on next run")
