from sqlalchemy import create_engine
from model import Base

engine = create_engine('sqlite:///library.sqlite', echo=True)
Base.metadata.create_all(engine)