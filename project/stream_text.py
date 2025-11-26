import streamlit as st

#title
st.title("Data Visual")

#header
header = "Thailand"
st.header(f"Data {header}")

st.subheader("Subheader")

st.markdown("Markdown **text**")
st.markdown("# Header 1")
st.markdown("## Header 2")

st.caption("Caption")

#code block
st.code("""import pandas as pd""")

st.text("Text")

st.latex("X = 2")

st.text("Above")
st.divider()
st.text("Bottom")

st.write('## Some text')