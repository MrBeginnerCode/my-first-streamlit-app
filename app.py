import numpy as np
import streamlit as st
import plotly
import sklearn
import pickle
filename = 'model-2.pickle'

model = pickle.load(open(filename, "rb"))
st.title("Revenue Prediction")
x = st.number_input('Input Temperature')
x = np.array(x)
x = x.reshape(1,-1)
if st.button('Predict'):
  y_pred = model.predict(x)
  st.write("Revenue Prediction")
  st.success(y_pred[0][0])
