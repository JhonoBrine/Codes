import streamlit as st
from forms.contact import contact_form
from styles.styles_func import styled_experience

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- INTRO SECTION ---

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("assets/pabroa_me.jpg", width=280, )

with col2:
    st.title(":green[Jhon Lorenz E. Pabroa]", anchor=False)
    st.write("\n")
    st.header("BS - Information Technology 4th Year Student", anchor=False, help="Cebu Institute of Technology - University")

    st.write(
        "_Strives to learn more about IT-related areas despite surface level information._"
    )

    if st.button("✉️ Contact Me"):
        show_contact_form()

# --- SUMMARY ---

# --- ACADEMIC EXPERIENCES ---

st.write("\n")
st.write("\n")
st.write("\n")
st.subheader("Academic Experiences", anchor=False)
st.write("\n")

# this variable stores a dictionary
academic_experiences = [
    {
        "school": "Cebu Institute of Technology - University",
        "date": "August 2024 - Present",
        "course": "Capstone and Research 2",
        "role": "Backend Developer / Database Manager",
        "image": "assets\Cebu_Institute_of_Technology_University_logo.png",
        "link": "https://www.cit.edu",
        "project": "Tower of Words",
        "github_link": "https://github.com/satou0419/tower-of-words_repository",
        "web_link": "https://tower-of-words.vercel.app/"
    },
    {
        "school": "Cebu Institute of Technology - University",
        "date": "January 2024 - May 2024",
        "course": "Capstone and Research 1",
        "image": "assets\Cebu_Institute_of_Technology_University_logo.png",
        "role": "Backend Developer / Database Manager",
        "link": "https://www.cit.edu",
        "project": "Tower of Words",
        "github_link": "https://github.com/satou0419/tower-of-words_repository",
        "web_link": "https://tower-of-words.vercel.app/"
    },
]

for i, experience in enumerate(academic_experiences):
    with st.expander(label=experience['course'], expanded=True):
        cols = st.columns([1, 4])

        with cols[0]:
            st.image(experience['image'], width=125)

        with cols[1]:
            st.markdown(f"**<span style='font-size:24px;'><a href=\"{experience['link']}\" style='text-decoration:none; color:#d33682;'>{experience['school']}</a></span>**", unsafe_allow_html=True)
            st.write(f" ##### {experience['course']}")
            st.write(f" ###### _{experience['role']}_")
            st.write(f"{experience['date']}")

            col1, col2, col3 = st.columns([3, 1, 1])

            with col1:
                st.write(f"{experience['project']}")

            with col2:
                st.link_button("Github", experience['github_link'], type="primary")

            # This one checks if web_link is None or "". That's the way I understood it and read it 

            if experience.get('web_link'):
                with col3:   
                    st.link_button("Website", experience['web_link'], type="secondary")


    if i < len(academic_experiences) - 1:
        st.divider()