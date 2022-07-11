from configuracoes.base_declarativa import Base
from configuracoes.conectar import Conectar
from sqlalchemy import Column, String, Integer, Float

class Produtos(Base):
    __tablename__ = "produtos"

    nome = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f'Produtos [id = {self.id}, nome = {self.nome}, valor = {self.valor}, tipo = {self.tipo}]'
    
    # SELECT * FROM produtos
    def getProduto(self):
        with Conectar() as con:
            data = con.session.query(Produtos).all()
            return data
    
    def getProdutoByName(self, nome):
        with Conectar() as con:
            return con.session.query(Produtos).filter(Produtos.nome == nome).all()

    # INSERT INTO produto (nome, valor, tipo) VALUES(?, ?, ?)
    # ID nao inserido como parametro porque é incrementado automaticamente
    def setProduto(self, nome, valor, tipo):
        with Conectar() as con:
            data_insert = Produtos(nome = nome, valor = valor, tipo = tipo)
            con.session.add(data_insert)
            con.session.commit()

    # 
    def updateProduto(self, nome, valor):
        with Conectar() as con:
            con.session.query(Produtos).filter(Produtos.nome == nome).update({ "valor" : valor })
            con.session.commit()

    # 
    def deleteProduto(self, id):
        with Conectar() as con:
            con.session.query(Produtos).filter(Produtos.id == id).delete()
            con.session.commit()