#!/usr/bin/python3
"""list all states and cities"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).\
        filter(State.id == City.state_id).all()
    for city, state in query:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()
