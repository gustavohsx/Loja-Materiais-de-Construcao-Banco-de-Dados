# Loja Materiais de Construcao Banco de Dados


Desenvolvedores:
  Gustavo Xavier - gustavohsx07@gmail.com;
  Joao Victor - jjvbsilva@hotmail.com;

Para este projeto, usamos a ORM SQLAlchemy para Python, e o banco de dados feito usando o MySQL Workbench.


### Requisitos para rodar o projeto:


Ter o Python 3.10 instalado. Caso não tenha, link para download:

https://www.python.org/downloads/

Ter o MySQL Workbench instalado. Caso não tenha, link para download:

https://dev.mysql.com/downloads/workbench/

Ter o driver PyMySQL instalado. Caso não tenha, instale através do comando via terminal:

### pip install PyMySQL

Ter a biblioteca e ORM SQLAlchemy instalada. Caso não tenha, instale através do comando via terminal:

### pip install SQLAlchemy

Com todos os requisitos satisfeitos, precisará importar o banco de dados para o MySQL Workbench.

Concluída a importação e com o serviço MySQL rodando, conseguirá acessar o Banco de Dados localmente.

Tabelas:

Estamos usando três entidades sendo elas: Fornecedor, Produtos e Cliente.
Possuímos dois relacionamentos sendo eles: Fornecer e Adquirir. Ambos irão virar tabela por conterem atributos.
Fornecer: relacionamento entre Produtos e Fornecedor - N x M
Adquirir: relacionamento entre Produtos e Cliente - N x 1
Na herança optamos por usar apenas uma tabela, a tabela “Produtos”, onde nela adicionamos o atributo “tipo” que define se será verificado a “Construção” ou o “Utilitário”.

Cliente(cpf, nome, endereco, telefone)
Produtos(id, nome, valor, tipo)
Fornecedor(codigo, nome, telefone, endereco)
fornecer(data_compra, codigo_fornecedorFK, id_produtoFK)
adquirir(data_compra, cpf_clienteFK, id_produtoFK)


### Sobre o código:

O código foi dividido em pastas:

classes: onde estão todas as classes que manipulam o banco de dados;
configuracoes: onde está a conexão com a ORM SQLAlchemy;

### NÃO SE ESQUEÇA DE TROCAR O USUÁRIO E A SENHA PARA CONECTAR AO BANCO DE DADOS!

Troque o root pelo seu usuário e 12345 pela sua senha MySQL.
Caso necessário, troque a porta do localhost.
