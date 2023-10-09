from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib

matplotlib.use("TkAgg")

load_dotenv()

API_KEY = os.environ['OPENAI_API_KEY']

llm = OpenAI(api_token=API_KEY)
pandas_ai = PandasAI(llm)

st.set_page_config(page_title="SAP Data Analysis", layout="wide")
st.title("Analyze SAP Data with OpenAI")

uploaded_file = st.file_uploader("Upload SAP data for analysis", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                bar = st.progress(0)
                st.write(pandas_ai.run(df, prompt=prompt))
                bar.progress(100)
        else:
            st.error("Please enter a prompt.")