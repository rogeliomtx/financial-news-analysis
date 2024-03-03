import streamlit as st
import pandas as pd
from ft_model import predict_label, topics


# Load app
st.title('Finantial news categorization')

df = pd.read_csv("scrapper/forbes.csv")
option = st.selectbox(
    'Select a saved message', df
)
st.text("or")
message = st.text_area(
    "Write a message to analyze",
    key="message"
)

btn = st.button("Analyze")

if btn:
    text = message or option
    st.markdown(
        f"""
        ```
        {text}
        > The message is about: {predict_label(text)}
        ```
        """
    )

# Table of possible labels
st.subheader("Possible topics")
table_topics = [value for value in topics.values()]
df = pd.DataFrame(table_topics, columns=["Possible topics"])
st.table(df)