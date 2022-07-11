from configuracoes.base_declarativa import Base
from configuracoes.conectar import Conectar
from sqlalchemy import Column, String, Integer

class Fornecedor(Base):
    __tablename__ = "fornecedor"

    telefone = Column(String, nullable=False)
    codigo = Column(Integer, primary_key=True)
    endereco = Column(String, nullable=False)
    nome = Column(String, nullable=False)

    def __repr__(self):
        return f'Fornecedor [nome = {self.nome}, codigo = {self.codigo}, telefone = {self.telefone}, endereco = {self.endereco}]'
    
    # SELECT * FROM fornecedor
    def getFornecedor(self):
        with Conectar() as con:
            data = con.session.query(Fornecedor).all()
            return data

    # INSERT INTO fornecedor (nome, telefone, endereco) VALUES (?, ?, ?)
    # Codigo nao inserido como parametro porque é incrementado automaticamente
    def setFornecedor(self, nome, telefone, endereco):
        with Conectar() as con:
            data_insert = Fornecedor(telefone = telefone, endereco = endereco, nome = nome)
            con.session.add(data_insert)
            con.session.commit()

    # 
    def updateFornecedor(self, nome, telefone, endereco):
        with Conectar() as con:
            con.session.query(Fornecedor).filter(Fornecedor.nome == nome).update({ "telefone" : telefone , "endereco" : endereco })
            con.session.commit()
            
    # 
    def deleteFornecedor(self, nome):
        with Conectar() as con:
            con.session.query(Fornecedor).filter(Fornecedor.nome == nome).delete()
            con.session.commit()