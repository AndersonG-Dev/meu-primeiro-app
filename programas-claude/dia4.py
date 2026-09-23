import sqlite3

# conectar ao banco de dados
conn = sqlite3.connect('dia4.db')
cursor = conn.cursor()

# criar tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco REAL,
        quantidade INTEGER
    )
''')
conn.commit()
print("Banco criado com sucesso!")

# inserir apenas se a tabela estiver vazia
cursor.execute('SELECT COUNT(*) FROM produtos')
total = cursor.fetchone()[0]

if total == 0:
    produtos = [
        ('Notebook', 3500.00, 5),
        ('Mouse', 150.00, 20),
        ('Teclado', 200.00, 15),
        ('Monitor', 1200.00, 8),
    ]
    cursor.executemany('''
        INSERT INTO produtos (nome, preco, quantidade)
        VALUES (?, ?, ?)
    ''', produtos)
    conn.commit()
    print(f"4 produtos inseridos!")
else:
    print("Produtos já cadastrados!")

#consultar produtos // no caso um executavel para eu puxar dados
cursor.execute ('SELECT * FROM produtos')
resultado = cursor.fetchall()

for produto in resultado:
    print(f"{produto[1]} -R${produto[2]} - {produto[3]} unidades" )