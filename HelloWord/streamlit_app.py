import streamlit as st



# -- PAGE SETUP ---


profile_1_page= st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

profile_2_page= st.Page(
    page="views/my_techstack.py",
    title="Techstack",
    icon=":material/description:",
)

profile_3_page= st.Page(
    page="views/my_hobbies.py",
    title="Hobbies",
    icon=":material/sports_esports:",
)

test_only_1_page = st.Page(
    page="views/hello_world_test.py",
    title="Hello World Test",
    icon=":material/bug_report:",
)

test_only_2_page = st.Page(
    page="views/video_test.py",
    title="Video Test",
    icon=":material/bug_report:",
)

test_only_3_page = st.Page(
    page="views/change_background_color_wheel.py",
    title="Color Wheel Test",
    icon=":material/palette:",
)
# --- NAGIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[profile_page_default, test_only_1_page])

# --- NAVIGATION SETUP (WITH SECTIONS) ---

pg = st.navigation(
    {
        "Info": [profile_1_page, profile_2_page, profile_3_page],
        "Testing Pages": [test_only_1_page, test_only_2_page, test_only_3_page],
    }
)

# --- SHARED ON ALL PAGES

st.logo("HelloWord/assets/IndustryElective3Logo.png")
st.sidebar.text("Created by Jhon Lorenz E. Pabroa")
st.sidebar.text("For CSIT342 - Industry Elective 3")
st.sidebar.link_button("GitHub Repo", "https://github.com/JhonoBrine/Codes")
# -- RUN NAVIGATION ---
pg.run()