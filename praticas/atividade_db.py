import sqlite3
conexao  = sqlite3.connect('alunos')

cursor = conexao.cursor()

### CRIAÇÃO DE TABELAS 

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

### INSERIR DADOS

#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Andrea", 25, "Administracao")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Vera", 53, "Radiologia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Carlos", 29, "Sistemas")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Valdinar", 40, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Bruno", 17, "Engenharia")')


### CONSULTAS BÁSICAS:

#cursor.execute('SELECT * FROM alunos')

#cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

#cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')

#cursor.execute('SELECT count(id) FROM alunos')


### Atualização e Remoção:

#cursor.execute('UPDATE alunos SET idade=55 WHERE id=2')

#cursor.execute('DELETE FROM alunos WHERE id=1')

### Criar uma Tabela e Inserir Dados

#cursor.execute('CREATE TABLE clientes(id PK, nome VARCHAR(100), idade INT, saldo FLOAT)')

#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Andrea", 25, 23.67)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "lurdes", 53, 500.0)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Carlos", 29, 100.0)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "alceu", 40, 30.0)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Bruno", 17, 49.89)')

### Consultas e Funções Agregadas:

#visualizar = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

#visualizar = cursor.execute('SELECT sum(saldo) FROM clientes as SALDO ')

#cursor.execute('SELECT id, nome, MAX(saldo) AS maior_saldo FROM clientes GROUP BY id, nome ORDER BY maior_saldo DESC LIMIT 1;')

#cursor.execute('SELECT count(nome) FROM clientes AS qtd GROUP BY nome HAVING saldo > 1000 ')


#Atualização e Remoção com Condições:

#cursor.execute('UPDATE clientes SET nome="Rodrigues" WHERE id=4')

#cursor.execute('DELETE FROM clientes WHERE id=2')

### Junção de Tabelas:

#cursor.execute('CREATE TABLE compras(id PK, client_id FK, produto VARCHAR(100), valor FLOAT)')

#cursor.execute('INSERT INTO compras(id, client_id, produto, valor ) VALUES(1, 1, "arroz", 30.50 )')
#cursor.execute('INSERT INTO compras(id, client_id, produto, valor ) VALUES(2, 3, "feijão", 3.50 )')
#cursor.execute('INSERT INTO compras(id, client_id, produto, valor ) VALUES(4, 5, "petisco", 2.50 )')


#cursor.execute('SELECT nome, produto, valor FROM clientes INNER JOIN compras ON clientes.id = compras.client_id ')




conexao.commit()
conexao.close()