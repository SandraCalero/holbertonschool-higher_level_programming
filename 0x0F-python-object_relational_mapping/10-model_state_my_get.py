#!/usr/bin/python3
"""This script is printing the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_to_search = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(mysql_username, mysql_password,
                                  database_name, pool_pre_ping=True))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)\
        .filter(State.name == state_name_to_search)\
        .first()
    if query is not None:
        print("{}".format(query.id))
    else:
        print('Not found')

    session.close()
