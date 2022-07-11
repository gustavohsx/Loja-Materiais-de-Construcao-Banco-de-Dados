from configuracoes.base_declarativa import Base
from configuracoes.conectar import Conectar
from sqlalchemy import Column, String, Integer

class Cliente(Base):
    __tablename__ = "cliente"

    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    cpf = Column(Integer, primary_key=True)

    def __repr__(self):
        return f'Cliente [nome = {self.nome}, cpf = {self.cpf}, telefone = {self.telefone}, endereco = {self.endereco}]'
    
    # SELECT * FROM cliente
    def getCliente(self):
        with Conectar() as con:
            data = con.session.query(Cliente).all()
            return data
    
    def getClienteByCpf(self, cpf):
        with Conectar() as con:
            data = con.session.query(Cliente).filter(Cliente.cpf == cpf).all()
            return data

    # INSERT INTO cliente (nome, cpf, telefone, endereco) VALUES (?, ?, ?, ?)
    def setCliente(self, nome, cpf, telefone, endereco):
        with Conectar() as con:
            data_insert = Cliente(telefone = telefone, endereco = endereco, nome = nome, cpf = cpf)
            con.session.add(data_insert)
            con.session.commit()

    # 
    def updateCliente(self, cpf, telefone, endereco):
        with Conectar() as con:
            con.session.query(Cliente).filter(Cliente.cpf == cpf).update({ "telefone" : telefone, "endereco" : endereco })
            con.session.commit()

    # 
    def deleteCliente(self, cpf):
        with Conectar() as con:
            con.session.query(Cliente).filter(Cliente.cpf == cpf).delete()
            con.session.commit()