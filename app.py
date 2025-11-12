import streamlit as st
import pandas as pd

df = pd.read_csv("byu_football_stats_2025.csv")

st.title("BYU Football Stats")
st.line_chart(df, y=["thirdDownEff", "fourthDownEff"])

df["possessionTime"] = df["possessionTime"].apply(lambda x: x/60)
st.markdown("## What about their posession time?")
st.line_chart(df, y=["possessionTime", "opponent_score", "byu_score"])
