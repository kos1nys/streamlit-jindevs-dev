import streamlit as st

with open("storage/images/i.webp", "rb") as f:
    st.download_button("Скачать косинуса", f)

st.badge("В разработке", icon=":material/code:", color="gray")