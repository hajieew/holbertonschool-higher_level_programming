#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get database credentials from arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve both State and City objects
    # Build JOIN logic by matching their ids in the filter
    results = session.query(State, City).filter(State.id == City.state_id)\
                     .order_by(City.id.asc()).all()

    # Print results in the required format
    # Format: <state name>: (<city id>) <city name>
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
