#  Date: 2021.03.01
#  Author: dharapx
#  Feel free to use this code
#  -------------------------------------------------------------------------------
#  Here we are having methods for CRUD operation
#  -------------------------------------------------------------------------------

from sqlalchemy.orm import Session
import model
import schema


def get_task_by_task_id(db: Session, task_id: str):
    """
    This method will return single task details based on task_id
    :param db: database session object
    :param task_id: task id only
    :return: data row if exist else None
    """
    return db.query(model.Task).filter(model.Task.id == task_id).first()


def get_task_by_id(db: Session, sl_id: int):
    """
    This method will return single task details based on id
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: data row if exist else None
    """
    return db.query(model.Task).filter(model.Task.id == sl_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    """
    This method will return all task details which are present in database
    :param db: database session object
    :param skip: the number of rows to skip before including them in the result
    :param limit: to specify the maximum number of results to be returned
    :return: all the row from database
    """
    return db.query(model.Task).offset(skip).limit(limit).all()


def add_task_details_to_db(db: Session, task: schema.Task_Schema):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db
    :param db: database session object
    :param task: Object of class schema.taskAdd
    :return: a dictionary object of the record which has inserted
    """
    task_details = model.Task(
        
        title = task.title,
        note = task.note,
        isCompleted = task.isCompleted,
        date = task.date,
        startTime = task.startTime,
        endTime = task.endTime,
        color = task.color,
        remind = task.remind,
        repeat = task.repeat
    )
    db.add(task_details)
    db.commit()
    db.refresh(task_details)
    return model.Task(**task.dict())


def update_task_details(db: Session, sl_id: int, details: schema.Task_Schema):
    """
    this method will update the database
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :param details: Object of class schema.Updatetask
    :return: updated task record
    """
    db.query(model.Task).filter(model.Task.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Task).filter(model.Task.id == sl_id).first()


def delete_task_details_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on primary key
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: None
    """
    try:
        db.query(model.Task).filter(model.Task.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
