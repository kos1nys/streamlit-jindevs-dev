import streamlit as st

dataTab, memeTab = st.tabs(["Данные", "Мемы"])

with dataTab:
    with st.expander("Описание"):
        st.write("""
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint atque labore enim, iusto repellat assumenda ut dolorum? Minus, officiis natus, aperiam voluptatibus mollitia doloribus pariatur, dignissimos quia nesciunt dolorum provident voluptates molest
    """)
        with open("storage/images/i.webp", "rb") as f:
            st.download_button("Скачать косинуса", f, "i.webp")

with memeTab:
    st.write("ГыГы")

st.success('This is a success message!', icon="✅")

st.badge("В разработке", icon=":material/code:", color="gray")