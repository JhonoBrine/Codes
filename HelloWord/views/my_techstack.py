import streamlit as st

st.title(":orange[Technology Stack] 🖥️", anchor=False)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.write("_Jhon Pabroa's :red[current expertise] or :red[knowledge] about technologies in developing or deploying a software application or system._")

with col2:
    st.link_button("My GitHub Profile", "https://github.com/JhonoBrine", use_container_width=True)

def output_language_result(languages):
    for language, percentage in languages.items():
        st.write(f"{language}: {percentage}%")
        st.progress(percentage / 100)

st.subheader("Programming Languages ⌨️")
languages = {
    "Java": 46,
    "Python": 30,
    "JavaScript": 34,
    "C": 28,
}

output_language_result(languages)

st.divider()

st.subheader("Other 🖱️")
st.write("##### Framework")
other_languages_1 = {
    "ReactJS": 40,
    "JavaSpringboot": 46
}

output_language_result(other_languages_1)

st.write("\n")
st.write("\n")
st.write("\n")

st.write("##### Designing Tool")

other_languages_2 = {
    "CSS": 20,
    "HTML": 20
}

output_language_result(other_languages_2)

st.write("\n")
st.write("\n")
st.write("\n")

st.write("##### Database")

other_languages_3 = {
    "MySQL": 32
}

output_language_result(other_languages_3)

st.write("\n")
st.write("\n")
st.write("\n")

st.write("##### Microsoft Office Skills")

other_languages_4 = {
    "Word": 52,
    "Powerpoint": 45,
    "Excel": 56
}

output_language_result(other_languages_4)
