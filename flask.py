from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/result', methods=['POST'])
def result():
    # Mendapatkan nilai a dan m dari input pengguna
    a = float(request.form['a'])
    m = float(request.form['m'])

    # Kode lainnya (mulai dari inisialisasi parameter hingga menghitung energi dan kesalahan relatif)
    # ...
    # ...

    return render_template('result.html', x=x[1:-1], psi_squared=psi_squared, true_psi_squared=true_psi_squared)

if __name__ == '__main__':
    app.run()
