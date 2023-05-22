import streamlit as st
import pandas
from PIL import Image

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/linked1.jpg")

with col2:
    st.title("Daithí O' Lionáird")
    content = """
    Daithí is an experienced engineer with a strong track record in the IT industry. With a passion for new technologies, ensuring software quality and driving efficient testing processes. Daithí has successfully led and contributed to numerous projects throughout his career. His expertise spans various domains, including E2E environments, 3rd party vendor onboarding and integration, API automation, data migration, and system upgrades. Daithí's commitment to delivering high-quality results, combined with his technical skills and leadership abilities, make him a valuable asset to any organisation.
    https://www.linkedin.com/in/daithiolionaird/
    """
    st.info(content)

df = pandas.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

footer = """
Lorem ipsum dolor s id o
"""
st.subheader(footer)