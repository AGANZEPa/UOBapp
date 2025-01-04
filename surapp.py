
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Titre de l'application
st.title(" Modele adapté à l'UOB Bukavu pour la Régénération des cartes des étudiants ")

st.title(" BIENVENU A L'UOB BUKAVU")

st.write("entrer votre identité.")

# Champs pour les informations de l'étudiant entrant dans le caractere texte
nom = st.text_input("Nom:")
post_nom = st.text_input("Post Nom:")
prenom = st.text_input("Prénom:")
date_naissance = st.date_input("Date de Naissance:")
adresse = st.text_input("Adresse:")
nationalite = st.text_input("Nationalité:")
matrice = st.text_input("Matrice:")
faculte = st.text_input("Faculté:")
annee_academique = st.text_input("Année Académique:")

# Téléchargeur de fichiers pour la photo de passeport
uploaded_photo = st.file_uploader("Téléchargez votre photo de passeport", type=["jpg", "jpeg", "png"])

# Téléchargeur de fichiers pour le logo de l'université
uploaded_logo = st.file_uploader("Téléchargez le logo de l'université", type=["jpg", "jpeg", "png"])

# Fonction pour générer la carte d'étudiant
def generate_student_card():
    # Dimensions de la carte
    card_width = 600
    card_height = 400

    # Créer une image blanche
    card = Image.new('RGB', (card_width, card_height), 'white')
    
    # Dessiner sur la carte
    draw = ImageDraw.Draw(card)
    
    # Ajouter le logo de l'université
    if uploaded_logo is not None:
        logo = Image.open(uploaded_logo).resize((100, 100))
        card.paste(logo, (20, 20))

    # Ajouter les informations de l'étudiant
    text_x = 150
    draw.text((text_x, 30), f"Nom: {nom}", fill="black")
    draw.text((text_x, 60), f"Post Nom: {post_nom}", fill="black")
    draw.text((text_x, 90), f"Prénom: {prenom}", fill="black")
    draw.text((text_x, 120), f"Date de Naissance: {date_naissance}", fill="black")
    draw.text((text_x, 150), f"Adresse: {adresse}", fill="black")
    draw.text((text_x, 180), f"Nationalité: {nationalite}", fill="black")
    draw.text((text_x, 210), f"Matrice: {matrice}", fill="black")
    draw.text((text_x, 240), f"Faculté: {faculte}", fill="black")
    draw.text((text_x, 270), f"Année Académique: {annee_academique}", fill="black")

    # Ajouter la photo de passeport
    if uploaded_photo is not None:
        photo = Image.open(uploaded_photo).resize((100, 100))
        card.paste(photo, (20, 150))

    return card

# Bouton pour générer la carte d'étudiant
if st.button("Générer la Carte d'Étudiant"):
    if all([nom, post_nom, prenom, adresse, nationalite, matrice, faculte, annee_academique]):
        student_card = generate_student_card()
        st.image(student_card, caption='Carte d\'Étudiant', use_column_width=True)
    else:
        st.warning("Veuillez remplir tous les champs avant de générer la carte.")

# Instructions pour le téléchargement
st.write("Pour télécharger votre carte d'étudiant, faites une capture d'écran.")

# Developpeur
st.write(" Developpeur AGANZE CIRHAKARHULA Patrick.")
st.write(" Supervisé par Ass. Albert AGISHA")


