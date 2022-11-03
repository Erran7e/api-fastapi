#  Date: 2021.03.01
#  Author: dharapx
#  Feel free to use this code
#  --------------------------------------------------------------------------------
# A schema is a collection of database objects that are logically grouped together.
# These can be anything, tables, views, stored procedure etc.
# Schemas are typically used to logically group objects in a database.
#  ---------------------------------------------------------------------------------
from typing import Optional
from pydantic import BaseModel


class Task_Schema(BaseModel):
   
    title : str
    note : Optional[str] = None
    isCompleted : int
    date : str
    startTime : str
    endTime : str
    color : int
    remind : int
    repeat : str
    class Config:
     orm_mode = True
