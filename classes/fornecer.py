from configuracoes.base_declarativa import Base
from configuracoes.conectar import Conectar
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from classes.fornecedor import Fornecedor
from classes.produtos import Produtos

# Relacionamento N x M entre Produtos e Fornecedor
class Fornecer(Base):
    __tablename__ = 'fornecer'

    data_compra = Column(String, primary_key=True)
    id_produto = Column(Integer, ForeignKey(Produtos.id), nullable=False)
    produto = relationship("Produtos")
    codigo_fornecedor = Column(Integer, ForeignKey(Fornecedor.codigo), nullable=False)
    fornecedor = relationship("Fornecedor")

    def __repr__(self):
        return f'Fornecer [data da compra = {self.data_compra}, id do produto = {self.id_produto}, codigo do fornecedor = {self.codigo_fornecedor}]'

    # SELECT * FROM fornecer
    def getFornecer(self):
        with Conectar() as con:
            data = con.session.query(Fornecer).all()
            return data

    # INSERT INTO fornecer (data_compra, id_produto, codigo_fornecedor) VALUES (?, ?, ?)
    def setFornecer(self, data, id_produto, codigo_fornecedor):
        with Conectar() as con:
            data_insert = Fornecer(data_compra = data, id_produto = id_produto, codigo_fornecedor = codigo_fornecedor)
            con.session.add(data_insert)
            con.session.commit()

    def deleteFornecer(self, data, id_produto, codigo_fornecedor):
        with Conectar() as con:
            con.session.query(Fornecer).filter(Fornecer.data_compra == data, Fornecer.id_produto == id_produto, Fornecer.codigo_fornecedor == codigo_fornecedor).delete()
            con.session.commit()