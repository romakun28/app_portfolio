import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photos1.png", )

with col2:
    st.title("Ron Tolero")
    content = """Hi I am Ron Tolero: I am a python student trying to become a web developer and data scientist in the 
    future I have worked different careers throughout my professional endeavors. I've been a Therapist, a Teacher, 
    a Company Agent and a Barista. I hope that in the new things I am trying to learn, it can help me breakthrough once
    again to a new and wonderful career. """
    st.info(content)

content2 = """Below you can find some of the apps I have built in python. Feel free to contact me!"""
st.write(content2)  # (st.text) the font is normal unlike using write which gives off a semi bold font

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")