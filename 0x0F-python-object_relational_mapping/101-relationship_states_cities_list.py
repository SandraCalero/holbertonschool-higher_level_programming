#!/usr/bin/python3
"""Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
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

    query = session.query(State).order_by(State.id).all()
    for state in query:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f'    {city.id}: {city.name}')

    session.close()
