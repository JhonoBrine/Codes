import streamlit as st

st.title("Hobbies 🎮🎧", anchor=False)
st.write("_Mostly the games I play most of the time when I am bored or I have time._")
# FIRST SECTION: GAMES
st.divider()

st.header("Game Profiles")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.subheader("Steam Profile")
    st.image("assets/fuwawa_burn.png", width=135)
    st.link_button("Jon's Profile", "https://steamcommunity.com/id/JonLeonardo/")

with col2:
    st.subheader("Roblox Profile")
    st.image("assets/noFilter.webp", width=150)
    st.link_button("jhonlorenz's Profile", "https://www.roblox.com/users/42846564/profile")

# Creating a list of games

st.write("\n")
st.write("\n")
st.write("\n")

st.subheader("Games I've Played")

col1, col2 = st.columns(2)
games = [
    {
        "game_name": "Left 4 Dead 2",
        "img_path": "assets/l4d2_icon.png",
        "game_link": "https://store.steampowered.com/app/550/Left_4_Dead_2/"
    },
    {
        "game_name": "Terraria",
        "img_path": "assets/terraria_icon.png",
        "game_link": "https://store.steampowered.com/app/105600/Terraria/"
    },
    {
        "game_name": "Guild Wars 2",
        "img_path": "assets/gw2_icon.png",
        "game_link": "https://store.steampowered.com/app/1284210/Guild_Wars_2/"
    },
    {
        "game_name": "Borderlands 2",
        "img_path": "assets/bl2_icon.png",
        "game_link": "https://store.steampowered.com/app/49520/Borderlands_2/"
    },
    {
        "game_name": "Deep Rock Galactic",
        "img_path": "assets/drg_icon.png",
        "game_link": "https://store.steampowered.com/app/548430/Deep_Rock_Galactic/"
    },
    {
        "game_name": "The Killing Antidote",
        "img_path": "assets/killingantidote.png",
        "game_link": "https://store.steampowered.com/app/2254890/The_Killing_Antidote/"
    },
]

with st.container(height=450):

    for i, game in enumerate(games):
        
        with st.container(border=True):
            cols = st.columns([1, 4])

            with cols[0]:
                st.image(game['img_path'], width=125)
            
            with cols[1]:
                st.markdown(f"**<span style='font-size:24px;'><a href=\"{game['game_link']}\" style='text-decoration:none; color:#d33682;'>{game['game_name']}</a></span>**", unsafe_allow_html=True)

        if i < len(games) - 1:
            st.divider()
