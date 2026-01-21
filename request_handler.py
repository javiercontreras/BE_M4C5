from fastapi import FastAPI
import patient_service
from models import PatientModel

app = FastAPI()

@app.get("/patient/{patient_id}")
def patient_details(patient_id: str):
    result = patient_service.get_patient(patient_id)
    return result


@app.post("/patient")
def add_patient(patient: PatientModel):
    patient_service.add_patient(patient)
    print(patient.id)