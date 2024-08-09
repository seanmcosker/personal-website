import streamlit as st
from st_social_media_links import SocialMediaIcons

st.title("All my Links")



social_media_links = [
    "https://www.linkedin.com/in/sean-mcosker/",
    "https://github.com/seanmcosker"
]

social_media_icons = SocialMediaIcons(social_media_links)

social_media_icons.render()