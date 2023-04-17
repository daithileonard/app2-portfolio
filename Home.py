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
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Bibendum enim facilisis gravida neque convallis a cras semper. A iaculis at erat pellentesque adipiscing. Tempor orci eu lobortis elementum nibh tellus. Adipiscing at in tellus integer. Dui id ornare arcu odio ut sem nulla pharetra diam. Nunc scelerisque viverra mauris in aliquam sem. Maecenas ultricies mi eget mauris pharetra et ultrices neque. Pellentesque pulvinar pellentesque habitant morbi. Sem fringilla ut morbi tincidunt augue. Quam id leo in vitae turpis massa sed elementum.
"""
st.subheader(footer)