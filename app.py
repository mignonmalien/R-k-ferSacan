import streamlit as st
st.set_page_config(page_title="ScanFer", page_icon="🔩", layout="centered")
st.title("🔩 ScanFer V2")
st.caption("Calcul poids fer avec étiquette pro")
FORMULES = {
    "Tube Rond": lambda d, e: 0.02466 * e * (d - e),
    "T.Carré": lambda a, e: 0.00785 * e * (4*a - 4*e),
    "F.Plat": lambda l, e: 0.00785 * l * e,
    "Cornière L": lambda a, b, t: 0.00785 * t * (a + b - t)
type_fer = st.selectbox("1. Type de fer", list(FORMULES.keys()))
if type_fer == "Tube Rond":
    d = st.number_input("Diamètre extérieur mm", 10, 200, 20)
    e = st.number_input("Épaisseur mm", 1.0, 10.0, 1.10, 0.05)
    etiquette = f"Tube rond {int(d)}x{e}"
    poids_ml = FORMULES[type_fer](d, e) 
elif type_fer == "T.Carré":
    a = st.number_input("Côté mm", 10, 150, 40)
    e = st.number_input("Épaisseur mm", 1.0, 8.0, 2.0, 0.1)
    etiquette = f"Tube carré {int(a)}x{e}"
    poids_ml = FORMULES[type_fer](a, e)   
elif type_fer == "F.Plat":
    l = st.number_input("Largeur mm", 20, 200, 50)
    e = st.number_input("Épaisseur mm", 2, 20, 5)
    etiquette = f"Plat {int(l)}x{int(e)}"
    poids_ml = FORMULES[type_fer](l, e)    
else:
    a = st.number_input("Aile 1 mm", 20, 150, 50)
    b = st.number_input("Aile 2 mm", 20, 150, 50)
    t = st.number_input("Épaisseur mm", 2, 12, 5)
    etiquette = f"Cornière L{int(a)}x{int(b)}x{int(t)}"
    poids_ml = FORMULES[type_fer](a, b, t)
longueur = st.number_input("2. Longueur en m", 1.0, 12.0, 6.0, 0.5)
prix_kg = st.number_input("3. Prix fer FCFA/kg", 600, 800, 650, 10)
poids_total = poids_ml * longueur
prix_total = poids_total * prix_kg
st.divider()
st.subheader(f"📋 {etiquette}")
col1, col2, col3 = st.columns(3)
col1.metric("Poids/ml", f"{round(poids_ml,3)} kg")
col2.metric("Poids total", f"{round(poids_total,2)} kg")
col3.metric("Prix total", f"{int(prix_total):,} FCFA")
