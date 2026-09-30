import sqlite3
import os

conn = sqlite3.connect('dia6.db')
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

os.system('clear')

while True: 
    print("1 - Cadastrar produto") 
    print("2 - Lista dos produtos cadastrados")
    print("3 - Sair do programa")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        nome = str(input("Digite o nome do produto: "))
        preco = float(input(f"Digite o preço do {nome}: "))
        quant = int(input(f"Digite a quantidade do {nome}: "))
        os.system('clear')
        print(f"Produto {nome}\nPreço: R${preco:,.2f}\nQuantidade: {quant}")
        cursor.execute('''INSERT INTO produtos (nome, preco, quantidade)
                       VALUES (?, ?, ?)''', (nome, preco, quant))
        conn.commit()

    elif opcao == "2":
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        for produto in produtos:
            print(f"Nome: {produto[1]} | Preço: R${produto[2]:,.2f} | Quantidade: {produto[3]}")
    elif opcao == "3":
        conn.close()
        break