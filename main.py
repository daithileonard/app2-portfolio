import streamlit as st

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

footer = """
This is a label but it doesnt fit into the columns created above, This is a label but it doesnt fit into the columns created above
"""
st.subheader(footer)