#!/usr/bin/python3
"""Script that lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(mysql_username, mysql_password,
                                  database_name, pool_pre_ping=True))

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    query = session.query(City.id, City.name, State.name)\
        .join(State)\
        .order_by(City.id).all()
    for city in query:
        print(f'{city.id}: {city[1]} -> {city[2]}')

    session.close()
