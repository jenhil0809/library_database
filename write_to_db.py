from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import Author, Book, Publisher
from datetime import date

engine = create_engine('sqlite:///library.sqlite', echo=True)

auth_1 = Author(name="Henry A")
auth_2 = Author(name="Lilly C")
auth_3 = Author(name="John M")
auth_4 = Author(name="Mary H")
auth_5 = Author(name="Erika L")
pub_1 = Publisher(name="Publisher1")
pub_2 = Publisher(name="Publisher2")
pub_3 = Publisher(name="Publisher3")
book_1 = Book(title="ABC", isbn="1234567890111",num_pages=91, pub_date=date(2012,10,30), pub_id=1)
book_2 = Book(title="ABC", isbn="1236567890111",num_pages=21, pub_date=date(2021,1,1), pub_id=2)
book_3 = Book(title="ABC", isbn="0190190192222",num_pages=115, pub_date=date(2005,3,21), pub_id=1)
book_4 = Book(title="ABC", isbn="0987654321111",num_pages=260, pub_date=date(1986,7,20), pub_id=3)
book_5 = Book(title="ABC", isbn="5468201920109",num_pages=87, pub_date=date(1992,11,19), pub_id=3)
book_1.author.append(auth_1)
book_1.author.append(auth_2)
book_2.author.append(auth_1)
book_3.author.append(auth_4)
book_4.author.append(auth_5)
book_5.author.append(auth_3)

with Session(engine) as sess:
    sess.add(book_1)
    sess.add(book_2)
    sess.add(book_3)
    sess.add(book_4)
    sess.add(book_5)
    sess.commit()