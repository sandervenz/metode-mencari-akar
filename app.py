import streamlit as st
import views.views as views

SELECTION = ""

st.set_page_config(
    page_title="Metode Mencari Akar",
    page_icon="📒",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📒 Aplikasi Metode Mencari Akar")

with st.sidebar:
    st.title("Menu Navigasi")
    SELECTION = st.selectbox(
        "Pilih Metode",
        ("Home", "Bagi Dua", "Regula Falsi", "Iterasi Titik Tetap", "Newton Raphson", "Secant")
    )

with st.container():
    if SELECTION == "Home":
        views.display_home()
    elif SELECTION == "Bagi Dua":
        views.display_bisection()
    elif SELECTION == "Regula Falsi":
        views.display_regula_falsi()
    elif SELECTION == "Iterasi Titik Tetap":
        views.display_iterasi_sederhana()
    elif SELECTION == "Newton Raphson":
        views.display_newton_raphson()
    elif SELECTION == "Secant":
        views.display_secant()