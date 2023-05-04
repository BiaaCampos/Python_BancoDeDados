import mysql.connector

def cria_estrutura(sql, conexao, tabela):
    try:
        conexao.execute(sql)
    except mysql.connector.Error as err:
        print("Erro ao criar tabela: ", tabela)
        print("Mensagem de erro: ", err)
        exit()

# Cria uma conexão com o banco de dados
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gib_modas"
    )
    cursor = conexao.cursor()
except:
    print("Erro ao conectar com o banco de dados")
    exit()

cria_estrutura("CREATE TABLE gerente (id INT NOT NULL, nome VARCHAR(50) NOT NULL, PRIMARY KEY (id))", cursor, "Gerente")

cria_estrutura("CREATE TABLE funcionario (id INT NOT NULL AUTO_INCREMENT, nome VARCHAR(50) NOT NULL, telefone varchar(12) NOT NULL, PRIMARY KEY (id)", cursor, "Funcionario")

cria_estrutura("CREATE TABLE clientes (cpf VARCHAR(11) NOT NULL,nome_completo VARCHAR(100) NOT NULL,data_nascimento DATE NOT NULL,email VARCHAR(100) NOT NULL, PRIMARY KEY (cpf)", cursor, "CLIENTES")

cria_estrutura("CREATE TABLE produto (id INT PRIMARY KEY, nome_produto VARCHAR(50), valor FLOAT NOT NULL, descricao varchar(100) NOT NULL, PRIMARY KEY (id)", cursor, "Produtos")

cria_estrutura("CREATE TABLE pedido (id INT NOT NULL AUTO_INCREMENT, valor_total FLOAT, data_pedido DATE, cliente_cpf VARCHAR(11), produto_id INT, FOREIGN KEY (produto_id) REFERENCES produto(id), FOREIGN KEY (cliente_cpf) REFERENCES clientes(cpf)", cursor, "Pedido")

cria_estrutura("CREATE TABLE itens_pedido (numero_pedido INT, quantidade INT, preco_unitario FLOAT, preco_total FLOAT, PRIMARY KEY (numero_pedido), FOREIGN KEY (id_pedido) REFERENCES pedido(id)", cursor, "ITENS_PEDIDO")

cria_estrutura("CREATE TABLE pagamento (id_pagamento INT, numero_, FOREIGN KEY (id_produto) REFERENCES produto(id)", cursor, "Pagamento")

cria_estrutura("CREATE TABLE estoque (id_estoque INT, nome_produto VARCHAR(50), quantidade_estoque INT, FOREIGN KEY (id_produto) REFERENCES produto(id)", cursor, "Estoque")

cria_estrutura("CREATE TABLE fornecedor (id_fornecedor INT, nome_fornecedor VARCHAR(50), PRIMARY KEY (id_fornecedor)", cursor, "Fornecedor")



print("***********")
print("ESTRUTURA CRIADA COM SUCESSO!")
print("***********")