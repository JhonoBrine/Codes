import streamlit as st



# -- PAGE SETUP ---


profile_page_default= st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)



test_only_1_page = st.Page(
    page="views/hello_world_test.py",
    title="Hello World Test",
    icon=":material/bug_report:",
)


# --- NAGIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[profile_page_default, test_only_1_page])

# --- NAVIGATION SETUP (WITH SECTIONS) ---

pg = st.navigation(
    {
        "Info": [profile_page_default],
        "Testing Pages": [test_only_1_page],
    }
)

# --- SHARED ON ALL PAGES

st.logo("assets/IndustryElective3Logo.png")
st.sidebar.text("Created by Jhon Lorenz E. Pabroa")
st.sidebar.text("For CSIT342 - Industry Elective 3")

# -- RUN NAVIGATION ---
pg.run()