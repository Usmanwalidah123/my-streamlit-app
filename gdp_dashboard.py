import streamlit as st
import pandas as pd
import plotly.express as px

# Taken Dashboard
st.title("GDP Dashboard")

st.write("""
### Simple GDP Dashboard Example

Wannan misali ne kawai da ke nuna yadda ake iya yin dashboard mai sauƙi
domin nuna bayanan GDP na wasu ƙasashe.
""")

# Samu bayanan (misali, dictionary na ƙasashe da GDP)
data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India'],
    'GDP (Trillions USD)': [22.9, 16.9, 5.1, 4.2, 3.2]
}

# Mayar da bayanan zuwa DataFrame
df = pd.DataFrame(data)

# Nuna DataFrame a Streamlit
st.write("#### GDP Table")
st.dataframe(df)

# Zana chart da Plotly
fig = px.bar(
    df, 
    x='Country', 
    y='GDP (Trillions USD)', 
    title='GDP by Country'
)

# Nuna chart a Streamlit
st.plotly_chart(fig)
