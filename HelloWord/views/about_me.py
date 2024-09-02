import streamlit as st
from forms.contact import contact_form

# st.write("# Profile")

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/pabroa_me.jpg", width=280)

with col2:
    st.title(":green[Jhon Lorenz E. Pabroa]", anchor=False)
    st.write("\n")
    st.subheader("BS - Information Technology 4th Year Student", anchor=False, help="Cebu Institute of Technology - University")

    st.write(
        "_Strives to learn more about IT-related areas despite surface level information._"
    )

    if st.button("✉️ Contact Me"):
        show_contact_form()