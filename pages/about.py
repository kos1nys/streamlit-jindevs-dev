import streamlit as st

with st.expander("Описание"):
    st.write("""
Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint atque labore enim, iusto repellat assumenda ut dolorum? Minus, officiis natus, aperiam voluptatibus mollitia doloribus pariatur, dignissimos quia nesciunt dolorum provident voluptates molest
""")
    with open("storage/images/i.webp", "rb") as f:
        st.download_button("Скачать косинуса", f, "i.webp")



st.badge("В разработке", icon=":material/code:", color="gray")