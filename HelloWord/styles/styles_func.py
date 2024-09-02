import streamlit as st

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('styles/styles.css')

def styled_experience(school, link, course, role, image, date, project):
    return f"""
    <div class="experience-container">
        <img src="{image}" class="experience-image" alt="{school}" />
        <div class="experience-content">
            <h3><a href="{link}" class="experience-school">{school}</a></h3>
            <p class="experience-course">{course}</p>
            <p class="experience-role">{role}</p>
            <p class="experience-date">{date}</p>
            <p class="experience-project">{project}</p>
        </div>
    </div>
    """