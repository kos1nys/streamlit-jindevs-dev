import streamlit as st

dataTab, memeTab = st.tabs(["Данные", "Мемы"])

with dataTab:
    with st.expander("Описание"):
        st.write("""
    
    """)
        with open("storage/images/i.webp", "rb") as f:
            st.download_button("Скачать косинуса", f, "i.webp")

with memeTab:
    st.write("ГыГы")

st.success('This is a success message!', icon="✅")

st.badge("В разработке", icon=":material/code:", color="gray")