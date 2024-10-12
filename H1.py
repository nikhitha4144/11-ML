import streamlit as st
import numpy as np
import joblib
model = joblib.load("Rent.pkl")

st.title("House Rent Prediction Model")
Size=st.number_input("Please enter Size",min_value =100.0, step = 50.0) # 22
BHK = st.selectbox("Sex",["1","2","3","4","5"]) # Male
Furnishing Status=st.selectbox("Furnishing Status",["0","1","2"]) # Yes
Tenant Preferred=st.selectbox("Tenant Preferred	",["0","1","2"]) # Sun
Bedroom=st.selectbox("Bedroom",["1","2","3","4","5","6","7","8","9","10"]) # Dinner

# gender = st.selectbox("Sex",["Male","Female"]) # Male
# smoker=st.selectbox("smoker",["Yes","No"]) # Yes
# day=st.selectbox("day",["Thur","Fri","Sat","Sun"]) # Sun
# time=st.selectbox("time",["Lunch","Dinner"]) # Dinner

gender_value = 0 if gender == "Male" else 1
smoker_value = 0 if smoker=="Yes" else 1
day_value = {"Thur":0, "Fri":1,"Sat":2,"Sun":3}[day]
time_value = 0 if time =="Lunch" else 1

if st.button("Predict"):
    result = model.predict([[total_bill,gender_value,smoker_value,day_value,time_value,size]])
    st.write(f"The predicted tip amount is ${result[0]:.2f}")