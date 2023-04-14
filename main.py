import streamlit as st
import pandas
from PIL import Image

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Daithí O' Lionáird")
    content = """
    something about me
    many lines"""
    st.info(content)

df = pandas.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image('images/1.png')
        # image(Image.open('images/1.png'))

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])

footer = """
This is a label but it doesnt fit into the columns created above, This is a label but it doesnt fit into the columns created above
"""
st.subheader(footer)