import sqlite3
import os

conn = sqlite3.connect('dia10.db')
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
    try:
        nome = str(input("Digite o nome do produto: "))
        preco = float(input(f"Digite o preço do {nome}: "))
        quant = int(input(f"Digite a quantidade do {nome}: "))
        os.system('clear')
        print(f"Produto {nome}\nPreço: R${preco:,.2f}\nQuantidade: {quant}")
        cursor.execute('''INSERT INTO produtos (nome, preco, quantidade)
                    VALUES (?, ?, ?)''', (nome, preco, quant))
        conn.commit()   
    except ValueError:
        print("\nErro: Você digitou um caractere inválido. Use apenas números para preço e quantidade!\n")
    
def list_products():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]:,.2f} | Quantidade: {produto[3]}")

def delete_product():
    print("\n--- Excluir Produto ---")
    list_products()

    try:
        id_produto = int(input("\nDigite o id do produto que deseja excluir: "))
        
        cursor.execute("DELETE FROM produtos WHERE id = ?",(id_produto,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"\nOK: Produto ID {id_produto} foi excluído com sucesso!")
        else:
            print(f"\nERROR: Não foi encontrado nenhum produto com o ID {id_produto}.")

    except ValueError:
        print("\nERROR: O usuário digitou caracteres não permitidos.")

def update_produto():
    print("\n--- Atualizar produto ---")
    list_products()
    
    try:
        id_produto = int(input("\nDigite o ID do produto que deseja atualizar: "))
        
        novo_preco = float(input("\nDigite o novo preço: "))
        nova_quant = int(input("\nDigite a nova quantidade do produto: "))
        
        cursor.execute('''UPDATE produtos
                       SET preco = ?, quantidade = ?
                       WHERE id = ? ''', (novo_preco, nova_quant, id_produto))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"\nProduto ID{id_produto} atualizado com sucesso!")
        else:
            print(f"\nNenhum produto com a ID {id_produto} foi encontrado.")
    except ValueError:
        print("\nERROR: Use apenas numeros para o ID, preço ou quantidade!")
        
def main():
    create_table()
    os.system('clear')

    while True:
        print("\n1 - Cadastrar produto")
        print("2 - Lista dos produtos cadastrados")
        print("3 - Excluir produto")
        print("4 - Atualizar produto")
        print("5 - Sair do programa")
        
        escolha = input("Escolha: ")
        
        if escolha == '1':
            insert_product()
        elif escolha == '2':
            list_products()
        elif escolha == '3':
            delete_product()
        elif escolha == '4':
            update_produto()
        elif escolha == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()