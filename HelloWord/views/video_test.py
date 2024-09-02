import streamlit as st


st.title("Video Test 🎥", anchor=False)
st.write("Playing around with streamlit documents lmao.")

videos = {
    "TJ Monterde - Dating Tayo": "https://www.youtube.com/watch?v=dKnIPbMlmNo",
    "December Avenue - Huling Sandali": "https://www.youtube.com/watch?v=MyMmB7vnO9c",
    "December Avenue - Kung ‘Di Rin Lang Ikaw (ft. Moira Dela Torre)": "https://www.youtube.com/watch?v=P1pwbnzbe7g",
    "Kathang Isip by Ben & Ben": "https://www.youtube.com/watch?v=uQ6jKuDRZUs",
    "Nickelback - Far Away": "https://www.youtube.com/watch?v=8UHBkWrzZ-Q"
}

select_video = st.selectbox("Choose a video to play!", list(videos.keys()))

video = videos[select_video]

st.video(video, autoplay=True)

st.divider()

st.write("This one just went inside my brain, if those are possible above... Why not this? 😉")
st.write("Enter the URL of the video!")
input_video = st.text_input("")

if input_video:
    st.video(input_video)
