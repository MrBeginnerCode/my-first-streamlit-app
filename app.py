!pip install streamlit
!pip install protobuf==3.20.0
import streamlit as st

st.title("GIẢI PHƯƠNG TRÌNH BẬC NHẤT")
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
  if a==0 and a!=b:
    st.success('Phương trình vô nghiệm')
  elif a==0 and b==0:
    st.success('Phương trình vô số nghiệm')
  else:
    result =-b/a
    st.success(f'Phương trình có 1 nghiệm {result}')
