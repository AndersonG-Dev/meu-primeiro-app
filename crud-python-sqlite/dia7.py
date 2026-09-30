import sqlite3
import os

conn = sqlite3.connect('dia7.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
    )''')
    conn.commit()

def insert_product():
    nome = str(input("Digite o nome do produto: "))
    preco = float(input(f"Digite o preço do {nome}: "))
    quant = int(input(f"Digite a quantidade do {nome}: "))
    os.system('clear')
    print(f"Produto {nome}\nPreço: R${preco:,.2f}\nQuantidade: {quant}")
    cursor.execute('''INSERT INTO produtos (nome, preco, quantidade)
                   VALUES (?, ?, ?)''', (nome, preco, quant))
    conn.commit()   

def list_products():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(f"Nome: {produto[1]} | Preço: R${produto[2]:,.2f} | Quantidade: {produto[3]}")

def main():
    create_table()
    print("Sua tabela de produtos está criada!")
    os.system('clear')

    while True: 
        print("1 - Cadastrar produto") 
        print("2 - Lista dos produtos cadastrados")
        print("3 - Sair do programa")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            insert_product()
        elif opcao == "2":
            list_products()
        elif opcao == "3":
            conn.close()
            break

if __name__ == "__main__":
    main()