#!/usr/bin/python3
"""This script is listing all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy.sql.expression import null
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import session, sessionmaker
from sys import argv

if __name__ == "__main__":

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(mysql_username, mysql_password,
                                  database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)\
            .filter(State.id == 1)
    if (State is not null):
        for state in query:
                print("{}: {}".format(state.id, state.name))
    else:
        print('Nothing')
            
    session.close()
