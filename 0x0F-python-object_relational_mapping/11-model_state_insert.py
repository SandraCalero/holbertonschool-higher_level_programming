#!/usr/bin/python3
"""Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print('{}'.format(new_state.id))

    session.close()
