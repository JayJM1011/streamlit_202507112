import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('House_Price_40p.pkl','rb'))
st.title("House Price Prediction")

Car = int(st.text_input("Enter Car Parking Spots: ","2"))
LandSize = float(st.text_input("Enter LandSize: ","558"))
BuildingArea= float(st.text_input("Enter BuildingArea: ","1000"))
YearBuilt= int(st.text_input("Enter YearBuilt: ","2000"))

featureInput = np.array([[Car,LandSize,BuildingArea,YearBuilt]])

price = model.predict(featureInput)

st.write(f'Hello, *World!* House Price : {price}')