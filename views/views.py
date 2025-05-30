import streamlit as st
import controllers.methods as methods
import numpy as np

from sympy import sympify
from pandas import DataFrame

def display_home():
    # Judul Utama Aplikasi
    st.markdown("---")

    # Pendahuluan dan Deskripsi Aplikasi
    st.markdown(
        """
        Aplikasi ini membantu Anda memahami dan membandingkan metode numerik populer untuk menemukan akar fungsi matematika secara interaktif. Masukkan fungsi, atur parameter, dan lihat langkah per langkah proses pencarian akarnya.

        Proyek ini merupakan bagian dari pemenuhan tugas akhir mata kuliah **Rekayasa Komputasional** (Semester 6) 
        di Jurusan Informatika, Fakultas Teknologi Industri, Universitas Gunadarma.
        """
    )
    st.markdown("---")

    # Informasi Tim Pengembang (dapat dibuat lebih ringkas dengan expander)
    st.markdown(
        """
        🔎 Tim Pengembang (Kelompok 3 Rekayasa Komputasional)

        * **Afiq Antariksa Gunawan** (NPM: 50422108)
        * **Akbar Nurrajab** (NPM: 50422143)
        * **Muhammad Rifqi Khalif Moebarra** (NPM: 51422146)
        * **Raedo Deva Novalino** (NPM: 51422317)
        * **Sander** (NPM: 51422505)
        * **Vincent Junico Gunawan** (NPM: 51422608)
        """
    )
    
    st.markdown("---")

    # Menggunakan kolom untuk tampilan yang lebih rapi
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Metode Tertutup")
        st.markdown(
            """
            Metode memerlukan interval awal [a, b] yang mengapit akar.
            - **Metode Bagi Dua (Bisection Method)**
            - **Metode Regula Falsi (False Position Method)**
            """
        )

    with col2:
        st.subheader("Metode Terbuka")
        st.markdown(
            """
            Metode menggunakan tebakan awal, konvergensi lebih cepat tapi tidak selalu pasti.
            - **Metode Iterasi Titik Tetap**
            - **Metode Newton-Raphson**
            - **Metode Secant**
            """
        )
    
    st.markdown("---")

    # Petunjuk Penggunaan Dashboard
    st.info(
        """
        💡 **Panduan Penggunaan:**
        Pilih metode dari menu sidebar, masukkan fungsi dan parameter, lalu klik tombol hitung untuk melihat hasil dan proses iterasi.
        """,
        icon="ℹ️"
    )
    
    st.markdown("---")

    st.caption("Proyek Rekayasa Komputasional - 2025 | Jurusan Informatika | Universitas Gunadarma")


def display_bisection():
    st.subheader("Metode Bagi Dua")
    st.write("Metode Bagi Dua adalah metode numerik untuk mencari akar dari fungsi dengan cara membagi interval menjadi dua bagian dan memilih bagian yang mengandung akar.")
    
    # Input for function
    func = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input for interval
    a = st.text_input("Masukkan nilai a:", value="0.0")
    a = np.float64(a)
    b = st.text_input("Masukkan nilai b:", value="5.0")
    b = np.float64(b)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
    disp_datas = st.empty()
    
    if st.button("Hitung"):
        result, datas = methods.biseksi(a, b, func, e)
        hasil.write(f"Hasil Akar : {result}")
        df_datas = DataFrame(datas, columns=["a", "c", "b", "f(a)", "f(c)", "f(b)", "lebar"])
        disp_datas.dataframe(df_datas, use_container_width=True)
        
def display_regula_falsi():
    st.subheader("Metode Regula Falsi")
    st.write("Metode Regula Falsi adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan garis lurus antara dua titik pada grafik fungsi.")
    
    # Input for function
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input for interval
    a = st.text_input("Masukkan nilai a:", value="0.0")
    a = np.float64(a)
    b = st.text_input("Masukkan nilai b:", value="5.0")
    b = np.float64(b)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
    disp_datas = st.empty()
    
    if st.button("Hitung"):
        result, datas = methods.regula_falsi(a, b, f_x, e)
        hasil.write(f"Hasil Akar : {result}")
        df_datas = DataFrame(datas, columns=["a", "c", "b", "f(a)", "f(b)", "f(c)", "e"])
        disp_datas.dataframe(df_datas, use_container_width=True)
        
def display_iterasi_sederhana():
    st.subheader("Metode Iterasi Titik Tetap")
    st.write("Metode Iterasi Titik tetap adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan iterasi.")
    
    st.markdown(
        """
            #### ***Permasalahan : x^2 - 2x - 3 =0***
        """
    )
    
    st.write("Ada 3 kemungkinan yang dapat digunakan untuk menyelesaikan permasalahan di atas, yaitu:")
    st.markdown(
        """
            - x = sqrt(2x + 3)
            - x = 3 / (x - 2)
            - x = (x^2 - 3) / 2
        """
    )
    
    x_initial = st.text_input("Masukkan nilai x awal:", value="0.0")
    x_initial = np.float64(x_initial)
    max_iter = st.number_input("Masukkan jumlah iterasi maksimum:", value=100)
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    cols = st.empty()
    
    if st.button("Hitung"):
        col1, col2, col3 = cols.columns(3)
        
        with col1:
            result1 = methods.iterasi_sederhana(x_initial, "sqrt(2*x + 3)", e, max_iter)
            col1.metric(f"Hasil Akar (x = sqrt(2x + 3))", result1, border=True)
        with col2:
            result2 = methods.iterasi_sederhana(x_initial, "3 / (x - 2)", e, max_iter)
            col2.metric(f"Hasil Akar (x = 3 / (x - 2))", result2, border=True)
        with col3:
            result3 = methods.iterasi_sederhana(x_initial, "(x**2 - 3) / 2", e, max_iter)
            col3.metric(f"Hasil Akar (x = (x^2 - 3) / 2)", result3, border=True)

def display_newton_raphson():
    st.subheader("Metode Newton Raphson")
    st.write("Metode Newton Raphson adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan turunan fungsi.")
    
    # Input for function
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x - exp(-x)")
    f_x = sympify(f_x)
    
    # Input for initial guess
    x0 = st.text_input("Masukkan nilai x awal:", value="0.0")
    x0 = np.float64(x0)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.00001")
    e = np.float64(e)
    
    hasil = st.empty()
    disp_datas = st.empty()
    
    if st.button("Hitung"):
        result, datas = methods.newton_raphson(x0, f_x, e)
        hasil.write(f"Hasil Akar : {result}")
        
        df_datas = DataFrame(datas, columns=["x_r", "f(x)", "f'(x)", "x_r+1", "e"])
        disp_datas.dataframe(df_datas, use_container_width=True)

def display_secant():
    st.subheader("Metode Secant")
    st.write("Metode Secant adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan dua titik pada grafik fungsi.")
    
    # Input for function
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input for initial guesses
    x0 = st.text_input("Masukkan nilai x0:", value="0.0")
    x0 = np.float64(x0)
    x1 = st.text_input("Masukkan nilai x1:", value="5.0")
    x1 = np.float64(x1)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
    disp_data = st.empty()
    
    if st.button("Hitung"):
        result, datas = methods.secant(x0, x1, f_x, e)
        hasil.write(f"Hasil Akar : {result}")
        
        df_datas = DataFrame(datas, columns=["x_r-1", "x_r", "f(x_r-1)", "f(x_r)", "x_r+1", "e"])
        disp_data.dataframe(df_datas, use_container_width=True)