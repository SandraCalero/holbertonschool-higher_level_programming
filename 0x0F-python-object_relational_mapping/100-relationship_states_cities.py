#!/usr/bin/python3
"""Script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa"""

from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine
from sys import argv


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

    new_state = State(name='California')
    new_city = City(name='San Francisco', state_id=new_state.id)
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()
    session.close()
