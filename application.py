#  Date: 2021.03.01
#  Author: dharapx
#  Feel free to use this code
#  ------------------------------------------------------------------------------------------------
# This is an API. which are having four end points to perform the CRUD operation with SQLite
#  ------------------------------------------------------------------------------------------------
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="task Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_task_details', response_model=List[schema.Task_Schema])
def retrieve_all_task_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    task = crud.get_tasks(db=db, skip=skip, limit=limit)
    return task


@app.post('/add_new_task', response_model=schema.Task_Schema)
def add_new_task(task: schema.Task_Schema, db: Session = Depends(get_db)):
    task_id = crud.get_task_by_task_id(db=db, task_id=task.id)
    if task_id:
        raise HTTPException(status_code=400, detail=f"task id {task.id} already exist in database: {task_id}")
    return crud.add_task_details_to_db(db=db, task=task)


@app.delete('/delete_task_by_id')
def delete_task_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_task_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_task_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_task_details', response_model=schema.Task_Schema)
def update_task_details(sl_id: int, update_param: schema.Task_Schema, db: Session = Depends(get_db)):
    details = crud.get_task_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_task_details(db=db, details=update_param, sl_id=sl_id)