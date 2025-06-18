from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy import ÷



# Database configuration (modify these values)
DB_USER = "nayankumar"
DB_PASSWORD = "nayankumar1998"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "myfastdb"  # or "my-database" (use one consistently)

# SQLAlchemy engine (pure SQLAlchemy, no psycopg2)
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base =declarative_base()


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


