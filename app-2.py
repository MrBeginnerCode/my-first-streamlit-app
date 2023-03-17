from matplotlib.pyplot import xkcd
import streamlit as st
import plotly
import sklearn
import pickle
filename = 'model.pickle'

model = pickle.load(open(filename, "rb"))
st.title("Revenue Prediction")
x = st.number_input('Input Temperature')
x = x.reshape(1,-1)
if st.button('Predict'):
  y_pred = model.predict(x)
  st.write("Revenue Prediction")
  st.success(y_pred)