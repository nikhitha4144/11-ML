import streamlit as st
import numpy as np
import joblib
model = joblib.load("Rent.pkl")

st.title("House Rent Prediction Model")
Size=st.number_input("Please enter Size",min_value =100.0, step = 50.0) # 22
BHK = st.selectbox("Sex",["1","2","3","4","5"]) # Male
Furnishing_Status = st.selectbox("Furnishing Status",["1","0","2"]) # Yes
Tenant_Preferred = st.selectbox("Tenant Preferred	",["0","1","2"]) # Sun
Bedroom=st.selectbox("Bedroom",["1","2","3","4","5","6","7","8","9","10"]) # Dinner

# gender = st.selectbox("Sex",["Male","Female"]) # Male
# smoker=st.selectbox("smoker",["Yes","No"]) # Yes
# day=st.selectbox("day",["Thur","Fri","Sat","Sun"]) # Sun
# time=st.selectbox("time",["Lunch","Dinner"]) # Dinner

g
if st.button("Predict"):
    result = model.predict([[Size,Furnishing_Status,Tenant_Preferred,Bedroom,]])
    st.write(f"The predicted House Rent is ${result[0]:.2f}")