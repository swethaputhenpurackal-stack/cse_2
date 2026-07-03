import streamlit as st

#take a user Input\
name= st.text_input("enter your name")

st.title("take the input")

if st.button("submit"):
  st.write(f"print the name:{name}")
