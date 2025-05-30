import numpy as np
from sympy import Symbol, lambdify

x = Symbol('x')
N_MAKS = 30


def cek_lebar(lebar, toleransi):
    return lebar >= toleransi


def hitung_c(a, b, f_a, f_b):
    return np.float64(((f_b * a) - (f_a * b)) / (f_b - f_a))


def hitung_error(x_baru, x_lama):
    return np.abs(x_baru - x_lama)


def biseksi(a, b, f_x, toleransi, datas=None):
    if datas is None:
        datas = []

    a, b = np.float64(a), np.float64(b)
    f_func = lambdify(x, f_x)
    f_a, f_b = f_func(a), f_func(b)

    if f_a * f_b > 0:
        return np.float64(0), datas

    c = (a + b) / 2
    f_c = f_func(c)

    if f_c * f_a < 0:
        lebar = c - a
        datas.append([a, c, b, f_a, f_c, f_b, lebar])
        if cek_lebar(lebar, toleransi):
            return c, datas.copy()
        return biseksi(a, c, f_x, toleransi, datas)

    elif f_c * f_a > 0:
        lebar = b - c
        datas.append([a, c, b, f_a, f_c, f_b, lebar])
        if cek_lebar(lebar, toleransi):
            return c, datas.copy()
        return biseksi(c, b, f_x, toleransi, datas)


def regula_falsi(a, b, f_x, toleransi, datas=None):
    if datas is None:
        datas = []

    a, b = np.float64(a), np.float64(b)
    f_func = lambdify(x, f_x)
    f_a, f_b = f_func(a), f_func(b)

    c = hitung_c(a, b, f_a, f_b)
    f_c = f_func(c)
    error = np.abs(f_c)

    datas.append([a, c, b, f_a, f_b, f_c, error])

    if error > toleransi:
        if f_c * f_a < 0:
            return regula_falsi(a, c, f_x, toleransi, datas)
        elif f_c * f_a > 0:
            return regula_falsi(c, b, f_x, toleransi, datas)

    return c, datas.copy()


def iterasi_sederhana(x_awal, f_x, toleransi, max_iter=N_MAKS):
    func = lambdify(x, f_x)
    x_sekarang = np.float64(x_awal)

    for _ in range(max_iter):
        x_berikut = func(x_sekarang)
        if np.isinf(x_berikut):
            return np.inf

        error = hitung_error(x_berikut, x_sekarang)
        if error <= toleransi:
            return x_berikut

        x_sekarang = x_berikut

    print("Maksimum iterasi tercapai tanpa konvergensi.")
    return np.inf


def newton_raphson(x_awal, f_x, toleransi, datas=None):
    if datas is None:
        datas = []

    x_sekarang = np.float64(x_awal)
    f_func = lambdify(x, f_x)
    f_prime_func = lambdify(x, f_x.diff(x))

    f_val = f_func(x_sekarang)
    f_prime = f_prime_func(x_sekarang)

    x_berikut = x_sekarang - (f_val / f_prime)
    error = hitung_error(x_berikut, x_sekarang)

    datas.append([x_sekarang, f_val, f_prime, x_berikut, error])

    if error >= toleransi:
        return newton_raphson(x_berikut, f_x, toleransi, datas)

    return x_berikut, datas.copy()


def secant(x_sebelum, x_sekarang, f_x, toleransi, datas=None):
    if datas is None:
        datas = []

    x_sebelum, x_sekarang = np.float64(x_sebelum), np.float64(x_sekarang)
    f_func = lambdify(x, f_x)

    y_sebelum, y_sekarang = f_func(x_sebelum), f_func(x_sekarang)

    if y_sekarang == y_sebelum:
        return np.inf, datas

    x_berikut = x_sekarang - (y_sekarang * (x_sekarang - x_sebelum)) / (y_sekarang - y_sebelum)
    error = hitung_error(x_berikut, x_sekarang)

    datas.append([x_sebelum, x_sekarang, y_sebelum, y_sekarang, x_berikut, error])

    if error > toleransi:
        return secant(x_sekarang, x_berikut, f_x, toleransi, datas)

    return x_berikut, datas.copy()
