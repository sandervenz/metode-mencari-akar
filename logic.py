import numpy as np
from sympy import Symbol, lambdify

variabel = Symbol('x')
MAX_ITERASI = 30

def masih_lebih_lebar(jarak, batas_galat):
    return jarak >= batas_galat

def cari_titik_potong(x0, x1, fx0, fx1):
    return np.float64(((fx1 * x0) - (fx0 * x1)) / (fx1 - fx0))

def selisih_error(nilai_baru, nilai_lama):
    return np.abs(nilai_baru - nilai_lama)

def biseksi(x_kiri, x_kanan, ekspresi_fungsi, galat, riwayat=None):
    if riwayat is None:
        riwayat = []

    x_kiri, x_kanan = np.float64(x_kiri), np.float64(x_kanan)
    fungsi = lambdify(variabel, ekspresi_fungsi)
    fx_kiri, fx_kanan = fungsi(x_kiri), fungsi(x_kanan)

    if fx_kiri * fx_kanan > 0:
        return np.float64(0), riwayat

    titik_tengah = (x_kiri + x_kanan) / 2
    fx_tengah = fungsi(titik_tengah)

    if fx_kiri * fx_tengah < 0:
        lebar_interval = titik_tengah - x_kiri
        riwayat.append([x_kiri, titik_tengah, x_kanan, fx_kiri, fx_tengah, fx_kanan, lebar_interval])
        if masih_lebih_lebar(lebar_interval, galat):
            return titik_tengah, riwayat.copy()
        return biseksi(x_kiri, titik_tengah, ekspresi_fungsi, galat, riwayat)

    elif fx_kiri * fx_tengah > 0:
        lebar_interval = x_kanan - titik_tengah
        riwayat.append([x_kiri, titik_tengah, x_kanan, fx_kiri, fx_tengah, fx_kanan, lebar_interval])
        if masih_lebih_lebar(lebar_interval, galat):
            return titik_tengah, riwayat.copy()
        return biseksi(titik_tengah, x_kanan, ekspresi_fungsi, galat, riwayat)

def regula_falsi(x0, x1, ekspresi_fungsi, galat, histori=None):
    if histori is None:
        histori = []

    x0, x1 = np.float64(x0), np.float64(x1)
    fungsi = lambdify(variabel, ekspresi_fungsi)
    fx0, fx1 = fungsi(x0), fungsi(x1)

    c = cari_titik_potong(x0, x1, fx0, fx1)
    fx_c = fungsi(c)
    galat_aktual = np.abs(fx_c)

    histori.append([x0, c, x1, fx0, fx1, fx_c, galat_aktual])

    if galat_aktual > galat:
        if fx0 * fx_c < 0:
            return regula_falsi(x0, c, ekspresi_fungsi, galat, histori)
        elif fx0 * fx_c > 0:
            return regula_falsi(c, x1, ekspresi_fungsi, galat, histori)

    return c, histori.copy()

def iterasi_sederhana(x_awal, fungsi_gx, galat, iterasi_maksimum=MAX_ITERASI):
    g = lambdify(variabel, fungsi_gx)
    nilai_x = np.float64(x_awal)

    for _ in range(iterasi_maksimum):
        nilai_berikut = g(nilai_x)
        if np.isinf(nilai_berikut):
            return np.inf

        err = selisih_error(nilai_berikut, nilai_x)
        if err <= galat:
            return nilai_berikut

        nilai_x = nilai_berikut

    print("Iterasi maksimum tercapai tanpa konvergensi.")
    return np.inf

def newton_raphson(x_awal, fungsi_fx, galat, catatan=None):
    if catatan is None:
        catatan = []

    nilai_x = np.float64(x_awal)
    f = lambdify(variabel, fungsi_fx)
    turunan_f = lambdify(variabel, fungsi_fx.diff(variabel))

    fx = f(nilai_x)
    dfx = turunan_f(nilai_x)

    x_baru = nilai_x - (fx / dfx)
    err = selisih_error(x_baru, nilai_x)

    catatan.append([nilai_x, fx, dfx, x_baru, err])

    if err >= galat:
        return newton_raphson(x_baru, fungsi_fx, galat, catatan)

    return x_baru, catatan.copy()

def secant(x_lama, x_skrg, fungsi_fx, galat, jejak=None):
    if jejak is None:
        jejak = []

    x_lama, x_skrg = np.float64(x_lama), np.float64(x_skrg)
    f = lambdify(variabel, fungsi_fx)

    y_lama, y_skrg = f(x_lama), f(x_skrg)

    if y_skrg == y_lama:
        return np.inf, jejak

    x_baru = x_skrg - (y_skrg * (x_skrg - x_lama)) / (y_skrg - y_lama)
    err = selisih_error(x_baru, x_skrg)

    jejak.append([x_lama, x_skrg, y_lama, y_skrg, x_baru, err])

    if err > galat:
        return secant(x_skrg, x_baru, fungsi_fx, galat, jejak)

    return x_baru, jejak.copy()
