import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.title("✈️ Dashboard Eindpresentatie ✈️")

st.markdown("""
Welkom!\n
\n
Bij ons Dashboard over onze eindpresenatie als alles lukt in ieder geval....
\n
""")
st.sidebar.title("Luchthaven")
language = st.sidebar.radio(label="", options=["Schiphol", "Maastricht"])
