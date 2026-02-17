import streamlit as st
import requests
import json
st.title('Employee Performance Prediction App')
years_at_company = st.text_input('Enter Years At Company:')
sick_days = st.text_input('Enter Sick Days:')
monthly_salary = st.text_input('Enter Monthly Salary:')
training_hours = st.text_input('Enter Training Hours:')
department_enc = st.text_input('Enter Department Encoded:')
work_hours_per_week = st.text_input('Enter Work Hours Per Week:')
projects_handled= st.text_input('Enter Projects Handled:')
promotions= st.text_input('Enter Promotions:')
education_level_enc= st.text_input('Enter Education Level Encoded:')
job_title_enc = st.text_input('Enter Job Title Encoded:')
if st.button('SUBMIT'):
    obj1 = json.dumps({"years_at_company":int(years_at_company),"sick_days":int(sick_days),"monthly_salary":int(monthly_salary),"training_hours":int(training_hours),"department_enc":int(department_enc),"work_hours_per_week":int(work_hours_per_week),"projects_handled":int(projects_handled),"promotions":int(promotions),"education_level_enc":int(education_level_enc),"job_title_enc":int(job_title_enc)})
    url = 'http://127.0.0.1:8000/predict'
    response = requests.post(url=url,data=obj1)
    st.success(response.text)
