from fastapi import FastAPI, HTTPException
from sqlmodel import create_engine , SQLModel, Session , select
from models import Appointment


#database Setup 
sqlite_url = 'sqlite:///./appointment.db'
engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

create_db_and_tables()

@app.post('/appointments', response_model=Appointment)
def create_appointment(appointment: Appointment):
   
    with Session(engine) as session:
        session.add(appointment)
        session.commit()
        session.refresh(appointment)
        return appointment

@app.get('/appointments', response_model=list[Appointment])
def get_appointments():
    with Session(engine) as session:
        appointments = session.exec(select(Appointment)).all()
        return appointments

@app.get('/appointment/{id}', response_model=Appointment)
def get_appointment(id : int):
    with Session(engine) as session:
        appointment = session.get(Appointment, id)
        if not Appointment:
            raise HTTPException(status_code=404, detail=f'No such Appointments {id}')
        
        return appointment
