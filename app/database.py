from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./tasks.db" #Crea conexion a SQLite 

engine = create_engine( #Creamos la conexion central, configuracion del motor
    DATABASE_URL, connect_args={"check_same_thread": False} #Para permitir conexion multihilo
)


SessionLocal = sessionmaker( #Define como se crean las sesiones
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base() #Define como se crean los modelos
