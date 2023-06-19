import numpy as np
import matplotlib.pyplot as plt
import csv
import easygui

# Data judul
judul1 = " Time Independent Schrodinger Equation (TISE)"
judul2 = 'Sumur Potensial Tak Berhingga Satu Dimensi'
print()
print('=' * 112)
print(judul1.center(111))
print(judul2.center(111))
print('=' * 112)
# Data menu
pilihan_menu = {
    1: 'Menunjukkan Grafik Representasi Persamaan Gelombang',
    2: 'Menampilkan Tiap Orde Energi Eksitasi',
    3: 'Keluar'
}
# GUI input
input_values = easygui.multenterbox(
    'Masukkan nilai a (length of well) dan m (mass of electron):',
    fields=['a (length of well) (m)', 'm (mass of electron)(Kg)']
)
a = float(input_values[0])
m = float(input_values[1])
N = 1000
x = np.linspace(0, a, N + 1)
Delta_x = x[1] - x[0]

hbar = 1.0546e-34

# Membentuk matriks M
M = np.diag(-2 * np.ones(N - 1)) + np.diag(np.ones(N - 2), 1) + np.diag(np.ones(N - 2), -1)

# Membentuk matriks Hamiltonian H
H = -hbar ** 2 / (2 * m) * 1 / (Delta_x) ** 2 * M

# Metode Pangkat  untuk nilai dan vektor eigen
I = np.eye(N - 1)
A = H - 1000 * I
psi = np.ones(N - 1)
tolerance = 1e-6
max_iterations = 1000

for i in range(max_iterations):
    psi_new = np.linalg.solve(A, psi)
    psi_new = psi_new / np.linalg.norm(psi_new)  # Normalisasi vektor
    if np.linalg.norm(psi_new - psi) < tolerance:
        break
    psi = psi_new

E = np.dot(np.dot(psi.T, H), psi)

def printMenu():
    choices = []
    for key, value in pilihan_menu.items():
        choices.append(value)
    choice = easygui.buttonbox('DAFTAR PILIHAN MENU', choices=choices)
    return choice

# Fungsi psi yang sebenarnya
def wave_equation(n, x):
    return np.sqrt(2 / a) * np.sin(n * np.pi * x / a)

def pilihan_menu_1():
    plt.figure(figsize=(10, 8))
    for n in range(1, 7):
        plt.plot(x[1:-1], wave_equation(n, x[1:-1]) ** 2, label='psi^2_{}'.format(n))
        plt.legend()
    plt.show()

# Menghitung energi
def menu_2_true_energy(n):
    return hbar ** 2 * np.pi ** 2 * n ** 2 / (2 * m * a ** 2)

def pilihan_menu_2():
    for n in range(6):
        true_energy_discrete = menu_2_true_energy(n)
        print('True energy-{}: {:.40f} eV'.format(n+1,true_energy_discrete))

    energies = []
    for n in range(6):
        true_energy_discrete = menu_2_true_energy(n)
        energies.append(true_energy_discrete)

    simpan_csv = easygui.buttonbox('Apakah Anda ingin menyimpan energi ke dalam file CSV?', choices=['Ya', 'Tidak'])
    if simpan_csv == 'Ya':
        filename = 'energies.csv'
        try:
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Energy'])
                writer.writerows([[energy] for energy in energies])
            easygui.msgbox('Energies saved to {}'.format(filename))
        except IOError:
            easygui.msgbox('Failed to save energies to {}'.format(filename))

# Program Utama/Managerial Program
if __name__ == '__main__':
    while True:
        choice = printMenu()
        if choice == pilihan_menu[1]:
            pilihan_menu_1()
        elif choice == pilihan_menu[2]:
            pilihan_menu_2()
        elif choice == pilihan_menu[3]:
            easygui.msgbox("Sampai jumpa kembali")
            exit()
        else:
            easygui.msgbox("Pilihan tidak valid. Silakan pilih menu yang tersedia.")