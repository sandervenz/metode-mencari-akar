import streamlit as st
import numpy as np
from sympy import sympify
from pandas import DataFrame

import logic

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Metode Mencari Akar",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar berisi info anggota
with st.sidebar:
    st.title("📒 Metode Mencari Akar")
    st.markdown("---")
    st.markdown(
        """
        🔎 Anggota Kelompok 3 Rekayasa Komputasional

        * **Afiq Antariksa Gunawan** (NPM: 50422108)
        * **Akbar Nurrajab** (NPM: 50422143)
        * **Muhammad Rifqi Khalif Moebarra** (NPM: 51422146)
        * **Raedo Deva Novalino** (NPM: 51422317)
        * **Sander** (NPM: 51422505)
        * **Vincent Junico Gunawan** (NPM: 51422608)
        """
    )

# Fungsi tiap metode
def tampil_bisection():
    with st.expander("Detail Metode Bagi Dua", expanded=True):
        st.subheader("Pendekatan Bisection")
        st.write("Bisection membagi interval untuk mempersempit pencarian akar secara sistematis.")

        col_input, col_output = st.columns([1, 2])

        with col_input:
            persamaan = st.text_input("Tentukan fungsi (dalam x):", "x**2 - 4", key="bisection_func")
            batas_kiri = st.text_input("Nilai batas bawah:", "0.0", key="bisection_a")
            batas_kanan = st.text_input("Nilai batas atas:", "5.0", key="bisection_b")
            toleransi = st.text_input("Toleransi error:", "0.01", key="bisection_e")
            tombol = st.button("Proses Bisection", key="btn_bisection")

        with col_output:
            if tombol:
                try:
                    a = float(batas_kiri)
                    b = float(batas_kanan)
                    e = float(toleransi)
                    akar, riwayat = logic.biseksi(a, b, persamaan, e)
                    st.metric(label="Akar Ditemukan", value=f"{akar:.6f}")
                    df = DataFrame(riwayat, columns=["a", "c", "b", "f(a)", "f(c)", "f(b)", "interval"])
                    st.dataframe(df, use_container_width=True)
                except Exception as err:
                    st.error(f"Error: {err}")

def tampil_regula():
    with st.expander("Detail Metode Regula Falsi", expanded=True):
        st.subheader("Pendekatan Regula Falsi")
        st.write("Regula Falsi menggunakan pendekatan linear dari dua titik berbeda untuk mencari akar fungsi.")

        col_input, col_output = st.columns([1, 2])

        with col_input:
            f_expr = st.text_input("Fungsi (dalam x):", "x**2 - 4", key="regula_func")
            a = st.text_input("Nilai awal a:", "0.0", key="regula_a")
            b = st.text_input("Nilai awal b:", "5.0", key="regula_b")
            e = st.text_input("Toleransi:", "0.01", key="regula_e")
            tombol = st.button("Proses Regula Falsi", key="btn_regula")

        with col_output:
            if tombol:
                try:
                    a_val = float(a)
                    b_val = float(b)
                    e_val = float(e)
                    akar, log = logic.regula_falsi(a_val, b_val, f_expr, e_val)
                    st.metric(label="Akar Ditemukan", value=f"{akar:.6f}")
                    df = DataFrame(log, columns=["a", "c", "b", "f(a)", "f(b)", "f(c)", "galat"])
                    st.dataframe(df, use_container_width=True)
                except Exception as err:
                    st.error(f"Error: {err}")

def tampil_iterasi():
    with st.expander("Detail Iterasi Titik Tetap", expanded=True):
        st.subheader("Iterasi Titik Tetap")
        st.write("Menggunakan fungsi transformasi g(x) untuk mencari akar dengan pendekatan berulang.")

        col_input, col_output = st.columns([1, 2])

        with col_input:
            x_mulai = st.text_input("Nilai awal x:", "0.0", key="iterasi_x0")
            iter_max = st.number_input("Batas iterasi maksimum:", value=100, key="iterasi_max")
            e = st.text_input("Toleransi:", "0.01", key="iterasi_e")
            tombol = st.button("Proses Iterasi", key="btn_iterasi")

        with col_output:
            if tombol:
                try:
                    x0_val = float(x_mulai)
                    e_val = float(e)
                    kol1, kol2, kol3 = st.columns(3)
                    with kol1:
                        r1 = logic.iterasi_sederhana(x0_val, "sqrt(2*x + 3)", e_val, iter_max)
                        st.metric("Akar: √(2x + 3)", f"{r1:.6f}")
                    with kol2:
                        r2 = logic.iterasi_sederhana(x0_val, "3 / (x - 2)", e_val, iter_max)
                        st.metric("Akar: 3 / (x - 2)", f"{r2:.6f}")
                    with kol3:
                        r3 = logic.iterasi_sederhana(x0_val, "(x**2 - 3) / 2", e_val, iter_max)
                        st.metric("Akar: (x² - 3)/2", f"{r3:.6f}")
                except Exception as err:
                    st.error(f"Error: {err}")

def tampil_newton():
    with st.expander("Detail Metode Newton-Raphson", expanded=True):
        st.subheader("Metode Newton-Raphson")
        st.write("Metode berbasis turunan fungsi untuk memperkirakan akar dengan cepat.")

        col_input, col_output = st.columns([1, 2])

        with col_input:
            fungsi = st.text_input("Fungsi:", "x - exp(-x)", key="newton_func")
            x_awal = st.text_input("Nilai awal x:", "0.0", key="newton_x0")
            e = st.text_input("Toleransi:", "0.00001", key="newton_e")
            tombol = st.button("Proses Newton-Raphson", key="btn_newton")

        with col_output:
            if tombol:
                try:
                    f_expr = sympify(fungsi)
                    x0_val = float(x_awal)
                    e_val = float(e)
                    akar, data = logic.newton_raphson(x0_val, f_expr, e_val)
                    st.metric(label="Akar Ditemukan", value=f"{akar:.6f}")
                    df = DataFrame(data, columns=["x", "f(x)", "f'(x)", "x selanjutnya", "error"])
                    st.dataframe(df, use_container_width=True)
                except Exception as err:
                    st.error(f"Error: {err}")

def tampil_secant():
    with st.expander("Detail Metode Secant", expanded=True):
        st.subheader("Metode Secant")
        st.write("Metode ini memperkirakan akar dengan menggunakan dua tebakan awal dan tanpa memerlukan turunan.")

        col_input, col_output = st.columns([1, 2])

        with col_input:
            f_input = st.text_input("Fungsi (dalam x):", "x**2 - 4", key="secant_func")
            x0 = st.text_input("Nilai x pertama:", "0.0", key="secant_x0")
            x1 = st.text_input("Nilai x kedua:", "5.0", key="secant_x1")
            eps = st.text_input("Toleransi:", "0.01", key="secant_e")
            tombol = st.button("Proses Secant", key="btn_secant")

        with col_output:
            if tombol:
                try:
                    x0_val = float(x0)
                    x1_val = float(x1)
                    e_val = float(eps)
                    hasil, langkah = logic.secant(x0_val, x1_val, f_input, e_val)
                    st.metric(label="Akar Ditemukan", value=f"{hasil:.6f}")
                    df = DataFrame(langkah, columns=["x_prev", "x_curr", "f(x_prev)", "f(x_curr)", "x_next", "error"])
                    st.dataframe(df, use_container_width=True)
                except Exception as err:
                    st.error(f"Error: {err}")


# Navigasi tabs utama
tabs = st.tabs(["Bagi Dua", "Regula Falsi", "Iterasi Titik Tetap", "Newton Raphson", "Secant"])

with tabs[0]:
    tampil_bisection()

with tabs[1]:
    tampil_regula()

with tabs[2]:
    tampil_iterasi()

with tabs[3]:
    tampil_newton()

with tabs[4]:
    tampil_secant()
