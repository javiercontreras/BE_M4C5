import sqlite3
from domain import Patient

def get_patient(patient_id):
    
    con = sqlite3.connect('tf_backend_api.db')
    #cur ejectura la consulta
    cur = con.cursor()
    res = cur.execute('SELECT * FROM patient WHERE patient_id_pk = ?', (patient_id,)).fetchone()
    
    return Patient(res[0], res[1], res[2]).__dict__()