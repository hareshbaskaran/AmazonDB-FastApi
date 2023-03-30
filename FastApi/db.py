from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#import postgresql connection link below
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Dertuport0208@localhost/Amazon-FastApi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()