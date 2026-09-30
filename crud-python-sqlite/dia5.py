import sqlite3
import os

conn = sqlite3.connect('dia5.db')
cursor = conn.cursor()

#criando tabela
cursor.execute(''' CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
        )
''')
conn.commit()
print("sua tabela de protudos esta criada!")

#aqui iremos por os input para pedir os dados dos produtos
nome = str(input("Qual o nome do produto? "))
preco = float(input(f"Qual o valor do {nome}? "))
quant = int(input(f"Qual a quantidade do {nome}? "))
os.system('clear')
print(f"produto: {nome}\nPreço: R${preco:,.2f}\nQuantidade {quant}")
cursor.execute('''INSERT INTO produtos (nome, preco, quantidade)
              VALUES (?, ?, ?) ''' , (nome, preco, quant))
conn.commit()
cursor.execute ('SELECT * FROM produtos')
resultado = cursor.fetchall()

for produto in resultado:
    print(f"{produto[1]} - R${produto[2]:,.2f} - {produto[3]} unidades")