import streamlit as st

st.set_page_config(page_title="ScanFer", page_icon="🔩", layout="centered")
st.title("🔩 ScanFer V1")
st.caption("Calcul poids fer - 100% précis")

FORMULES = {
    "T.Rond": lambda d: 0.006165 * d * d,
    "T.Carré": lambda a: 0.00785 * a * a, 
    "F.Plat": lambda l, e: 0.00785 * l * e,
    "Cornière L": lambda a, b, t: 0.00785 * t * (a + b - t)
}

type_fer = st.selectbox("1. Type de fer", list(FORMULES.keys()))

if type_fer == "T.Rond":
    d = st.number_input("Diamètre mm", 6, 50, 12)
    poids_ml = FORMULES[type_fer](d)
elif type_fer == "T.Carré":
    a = st.number_input("Côté mm", 10, 100, 40)
    poids_ml = FORMULES[type_fer](a)
elif type_fer == "F.Plat":
    l = st.number_input("Largeur mm", 20, 200, 50)
    e = st.number_input("Épaisseur mm", 3, 20, 5)
    poids_ml = FORMULES[type_fer](l, e)
else:
    a = st.number_input("Aile 1 mm", 20, 150, 50)
    b = st.number_input("Aile 2 mm", 20, 150, 50)
    t = st.number_input("Épaisseur mm", 3, 12, 5)
    poids_ml = FORMULES[type_fer](a, b, t)

longueur = st.number_input("2. Longueur en m", 1.0, 12.0, 6.0, 0.5)
prix_kg = st.number_input("3. Prix fer FCFA/kg", 600, 800, 650, 10)

poids_total = poids_ml * longueur
prix_total = poids_total * prix_kg

st.divider()
col1, col2 = st.columns(2)
col1.metric("Poids total", f"{round(poids_total,2)} kg")
col2.metric("Prix total", f"{int(prix_total):,} FCFA")

st.divider()
st.warning("📄 Devis PDF + Logo + Prix auto = ScanFer Pro 1000f/mois")
st.caption("WhatsApp: Ton numéro ici")
