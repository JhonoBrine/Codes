import streamlit as st
import os

file = "D:\$FILES\SCHOOL_FILES\#Fourth_Year\First_Semester\CSIT342_Industry_Elective_3\Codes\HelloWord\streamlit_app.py"
thisfile = os.path.abspath(file)
if ('/' in thisfile): os.chdir(os.path.dirname(thisfile))

# -- PAGE SETUP ---


profile_1_page= st.Page(
    page="HelloWord/views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

profile_2_page= st.Page(
    page="HelloWord/views/my_techstack.py",
    title="Techstack",
    icon=":material/description:",
)

profile_3_page= st.Page(
    page="HelloWord/views/my_hobbies.py",
    title="Hobbies",
    icon=":material/sports_esports:",
)

test_only_1_page = st.Page(
    page="HelloWord/views/hello_world_test.py",
    title="Hello World Test",
    icon=":material/bug_report:",
)

test_only_2_page = st.Page(
    page="HelloWord/views/video_test.py",
    title="Video Test",
    icon=":material/bug_report:",
)

test_only_3_page = st.Page(
    page="HelloWord/views/change_background_color_wheel.py",
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

st.sidebar.write("\n")

st.sidebar.write("Testing Sidebar Audio and Video with Autoplay True")
st.sidebar.video("https://www.youtube.com/watch?v=vyAV1Z-81oU")

st.sidebar.caption("Granblue Fantasy OST - Lyria MP3")
st.sidebar.audio("HelloWord/assets/audio/lyria_gbf-ost.m4a", autoplay=True)
# -- RUN NAVIGATION ---
pg.run()