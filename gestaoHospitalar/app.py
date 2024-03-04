from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__) #ABRINDO FLASK

# Conexão com o banco de dados
conn = sqlite3.connect('gestao_hospitalar.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER,
               sexo TEXT,
               cpf TEXT UNIQUE,
               endereco TEXT,
               telefone TEXT
    )
''')

conn.commit()
conn.close()

@app.route('/')

def index():
    conn = sqlite3.connect('gestao_hospitalar.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pacientes')
    pacientes = cursor.fetchall()
    conn.close()
    return render_template('index.html', pacientes=pacientes)

@app.route('/novo_paciente', methods=['GET', 'POST'])
def novo_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        sexo = request.form['sexo']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        telefone = request.form['telefone']

        # SINCRONIZAÇÃO BANCO DE DADOS
