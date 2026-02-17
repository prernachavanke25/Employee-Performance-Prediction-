from fastapi import FastAPI
from pydantic import BaseModel
import pickle
final_employee_model = pickle.load(open('final_employee_model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))
class employee_performance(BaseModel):
    years_at_company:int
    sick_days:int
    monthly_salary:int
    training_hours:int
    department_enc:int
    work_hours_per_week:int
    projects_handled:int
    promotions:int
    education_level_enc:int
    job_title_enc:int
    

app = FastAPI()

@app.get('/')
def Welcome():
    return{'message':'Welcome in CodeSpyder'}

@app.post('/predict')
def predict(obj1:employee_performance):
    q = [[obj1.years_at_company,obj1.sick_days,obj1.monthly_salary,obj1.training_hours,obj1.department_enc,obj1.work_hours_per_week,obj1.projects_handled,obj1.promotions,obj1.education_level_enc,obj1.job_title_enc]]
    q_scaled = scaler.transform(q)
    yp = final_employee_model.predict(q_scaled)[0]
    ak = round(yp,2)
    return{'predicted_performance':ak}
