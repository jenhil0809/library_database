from sqlalchemy import Column, Integer, String, Date, CHAR, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


books_authors = Table('books_authors',
                      Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('author_id', ForeignKey('authors.id')),
    Column('book_id', ForeignKey('books.id')),
    UniqueConstraint('author_id', 'book_id')
)


class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    books = relationship('Book', backref='books')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    isbn = Column(CHAR(13), nullable=False)
    num_pages = Column(Integer, nullable=False)
    pub_date = Column(Date, nullable=False)
    pub_id = Column(Integer, ForeignKey('publishers.id'), nullable=False)
    author = relationship('Author', secondary=books_authors, backref='books')


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, autoincrement=True)
    book = relationship('Author', secondary=books_authors, backref='authors')