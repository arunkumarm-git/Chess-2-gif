import streamlit as st


def other_tools():
    for i in range(6):  # For space
        st.write(" ")

    st.link_button("Vibe with chess", "https://vibewithchess.com")
    st.link_button("Chess review", "https://chessvibe.onrender.com/")
    st.link_button("AI chess arbiter", "https://aichessarbiter.streamlit.app/")
