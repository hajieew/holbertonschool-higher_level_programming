#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create the database connection engine
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 1. Find all State objects with the letter 'a' in their name
    # .like('%a%') is equivalent to SQL LIKE '%a%'
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # 2. Delete each found object from the session
    for state in states_to_delete:
        session.delete(state)

    # 3. Commit the changes to make them permanent in the database
    session.commit()

    # Close the session
    session.close()
