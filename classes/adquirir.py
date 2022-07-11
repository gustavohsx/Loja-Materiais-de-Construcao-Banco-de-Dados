from configuracoes.base_declarativa import Base
from configuracoes.conectar import Conectar
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from classes.cliente import Cliente
from classes.produtos import Produtos

# Relacionamento 1 x M entre Cliente e Produtos
class Adquirir(Base):
    __tablename__ = "adquirir"

    data_compra = Column(String, primary_key=True)
    id_produto = Column(Integer, ForeignKey(Produtos.id), nullable=False)
    produtos = relationship("Produtos")
    cpf_cliente = Column(Integer, ForeignKey(Cliente.cpf), nullable=False, unique=True)
    cliente = relationship("Cliente")

    def __repr__(self):
        return f'Adquirir [data da compra = {self.data_compra},  id do produto = {self.id_produto}, cpf do cliente = {self.cpf_cliente}]'
    
    # SELECT * FROM adquirir
    def getAdquirir(self):
        with Conectar() as con:
            data = con.session.query(Adquirir).all()
            return data

    # INSERT INTO adquirir (data, id_produto, cpf_cliente) VALUES (?, ?, ?)
    def setAdquirir(self, data, id_produto, cpf_cliente):
        with Conectar() as con:
            data_insert = Adquirir(data_compra = data, id_produto = id_produto, cpf_cliente = cpf_cliente)
            con.session.add(data_insert)
            con.session.commit()

    def deleteAdquirir(self, data, id_produto, cpf_cliente):
        with Conectar() as con:
            con.session.query(Adquirir).filter(Adquirir.data_compra == data, Adquirir.id_produto == id_produto, Adquirir.cpf_cliente == cpf_cliente).delete()
            con.session.commit()