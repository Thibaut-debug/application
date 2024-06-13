import streamlit as st
import pyodbc


# Définir le nom et le logo de l'application
st.set_page_config(
    page_title="IUT School",
    page_icon="C:\\Users\\Thibaut Alex\\Documents\\VisualCodeEditor\\python\\logo_IUT.png",
)


# Créer une connexion à la base de données

def create_conn():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=NOTEBOOK\SQLEXPRESS;'
        'DATABASE=étudiants_IUT;'
        'UID=Thibaut;'
        'PWD=alexthibaut;'
        'Trusted_Connection=yes;'  # Utilisez l'authentification Windows
    )
    return conn

# Insérer des données dans la table élèves
def insert_data(nom, age, matricule, filiere, salle):
    conn = create_conn()
    cursor = conn.cursor()
    query = "INSERT INTO étudiants (nom, age, matricule, filiere, salle) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (nom, age, matricule, filiere, salle))
    conn.commit() 
    conn.close()

# Créer l'interface utilisateur de Streamlit
def create_ui():
    st.title("Formulaire d'inscription des étudiants de IUT Douala NIV 1 Fi & Fa")
    
    nom = st.text_input("Nom")
    age = st.number_input("Âge", min_value=1, max_value=100)
    matricule = st.text_input("Matricule")
    filiere = st.selectbox("Filière", ["Genie Informatique", "Genie Electrique Et Informatique indistruielle", "Genie Bio Médical", "Genie Résau et Télécommunication"])
    salle = st.text_input("Salle")
    
    if st.button("Soumettre"):
        insert_data(nom, age, matricule, filiere, salle)
        st.success("Les données ont été insérées avec succès dans la base de données.")

create_ui()
