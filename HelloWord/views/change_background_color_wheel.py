import streamlit as st

st.title("Color Wheel 🎨", anchor=False)
st.write("This one might become like the ones you see in google, the Canva one and the like.")



current_color = st.color_picker("Pick a Color", "#fff")

st.write("The current color is", current_color)

# Came from chatgpt, because me nono CCS that much even tho I played it very much well during 3rd Year lmao. I don't know how to Inline CSS
st.markdown(
    f"""
    <p style="color: {current_color}; background-color: {current_color}; padding: 10px; border-radius: 5px; height: 500px">
    </p>
    """,
    unsafe_allow_html=True
)