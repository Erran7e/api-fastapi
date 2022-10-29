#  Date: 2021.03.01
#  Author: dharapx
#  Feel free to use this code
#  --------------------------------------------------------------------------------------------
# A data model in a database should be relational which means it is described by tables.
# The data describes how the data is stored and organized.
# A data model may belong to one or more schemas, usually, it just belongs to one schema
#  --------------------------------------------------------------------------------------------
from sqlalchemy import Boolean, Column, Integer, String
from db_handler import Base


class Task(Base):
    __tablename__ = "Task"
    id  = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    title = Column(String(255), index=True, nullable=False)
    note = Column(String(255), index=True, nullable=True)
    isCompleted = Column(Integer, index=True, nullable=False)
    date = Column(String(255), index=True, nullable=False)
    startTime = Column(String(255), index=True, nullable=False)
    endTime = Column(String(255), index=True, nullable=False)
    color = Column(Integer, index=True, nullable=False)
    remind = Column(Integer, index=True, nullable=False)
    repeat = Column(String(255), index=True, nullable=False)
