import streamlit as st

st.title("Hello World!")

x = st.text_input("Favourite Movie?")
st.write(f"Your favourite movie is: {x}")
