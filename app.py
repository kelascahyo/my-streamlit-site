import streamlit as st
import pandas as pd
import numpy as np

st.title("🚀 My First Streamlit Web App")

st.write("This app was built using Python and is hosted on GitHub!")

# Create a sample data frame
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Stock A', 'Stock B', 'Stock C']
)

st.line_chart(data)
