from sqlalchemy import Integer, String, create_engine, insert, select, delete
from sqlalchemy.orm import mapped_column, declarative_base, Mapped

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)


engine = create_engine("sqlite:///zarma_orm.db")
connection = engine.connect()

users_insert_data = [{"name": "Ivan", "age": 10},
                     {"name": "Boris", "age": 55},
                     {"name": "Georgiy", "age": 30},
                     {"name": "Pavel", "age": 31}]
stmt_insert_users = (
    insert(User)
    .values(users_insert_data)
)
connection.execute(stmt_insert_users)
connection.commit()

stmt_select_users_older_30 = (
    select(User.name, User.age)
    .filter(User.age > 30)
)
users = connection.execute(stmt_select_users_older_30).fetchall()
print(users)

stmt_drop_users = (
    delete(User)
)

connection.execute(stmt_drop_users)
connection.commit()
