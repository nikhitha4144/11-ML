import streamlit as st
import numpy as np
import joblib
model = joblib.load("Rent.pkl")

st.title("House Rent Prediction Model")
st.image("dataset-cover.jpg")
Size=st.number_input("Please enter Size",min_value =100, step = 50) 
BHK = st.selectbox("BHK",["1","2","3","4","5"])
Furnishing_Status = st.selectbox("Furnishing Status",["Unfurnished","Semi_Furnished","Furnished"])
Tenant_Preferred = st.selectbox("Tenant Preferred	",["Bachelors","Bachelors/Family","Family"])

if Furnishing_Status == "Unfurnished":
    Furnishing_Status = 0
elif Furnishing_Status == "Semi-Furnished":
    Furnishing_Status = 1
else:  # Furnished
    Furnishing_Status = 2

if Tenant_Preferred == "Family":
    Tenant_Preferred = 0
elif Tenant_Preferred == "Bachelor":
    Tenant_Preferred = 1
else:  
    Tenant_Preferred = 2

Size = float(Size)
BHK = int(BHK)
Furnishing_Status = int(Furnishing_Status)
Tenant_Preferred = int(Tenant_Preferred)

if st.button("Predict"):
    result = model.predict([[Size,BHK,Furnishing_Status,Tenant_Preferred]])
    st.write(f"The predicted House Rent is ${result[0]:.2f}")