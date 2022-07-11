from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Conectar:

    def __init__(self) -> None:
        self.__conection_string = 'mysql+pymysql://root:12345@localhost:3306/loja'
        self.__engine = self.__create_database_engine()
        self.session = None
    
    def __create_database_engine(self):
        engine = create_engine(self.__conection_string) # echo=True
        return engine

    def __enter__(self):
        sessionmake = sessionmaker(bind=self.__engine)
        self.session = sessionmake()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()