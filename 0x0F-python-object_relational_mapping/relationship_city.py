#!/usr/bin/python3
"""
contains the definition of a city
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    Attributes:
        id: city identifier
        name: city name
        state_id : state identifier (FK)
    """
    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
