import streamlit as st
import joblib
jk=joblib.load('IRIS FLOWER')  
st.title('SPECIES CLASSIFIER')
ip=st.text_input('enter details')
op=jk.predict([ip])
if st.button ('Predict'):    
  st.button(op[0])     
