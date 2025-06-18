import streamlit as st
age = st.number_input("enter the patients age: ")
illiness = st.number_input("enter the iliness type (e.g emergency, routine, etc.):")
if iliness == "emergency" and age > 70 :
  treatiment = "priority treatment"
  else :
  treatment = "regural treatment"
st.write(f "the patient requres [treatment]")
