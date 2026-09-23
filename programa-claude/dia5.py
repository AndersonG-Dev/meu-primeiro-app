import sqlite3
conn = sqlite3.connect ('dia5.db')
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