# app.py

import streamlit as st
from eda.analysis import load_data, clean_data, top_crops_by_production, yield_trend, production_heatmap
import plotly.express as px

st.title("🌾 AgriData Explorer: Indian Agriculture Dashboard")

# Load and clean data
df = load_data('data/crop_production.csv')
df = clean_data(df)

# Sidebar filters
year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()), index=-1)
crop = st.sidebar.selectbox("Select Crop", df['Crop'].unique())

# Display top crops by production
st.subheader(f"Top 10 Crops by Production in {year}")
top_crops = top_crops_by_production(df, year)
fig1 = px.bar(top_crops, x=top_crops.index, y=top_crops.values, labels={'x': 'Crop', 'y': 'Total Production'})
st.plotly_chart(fig1)

# Yield trend over years
st.subheader(f"Yield Trend for {crop}")
yield_data = yield_trend(df, crop)
fig2 = px.line(yield_data, x='Year', y='Yield', title=f'Yield Trend of {crop}')
st.plotly_chart(fig2)

# Production by state heatmap
st.subheader("Production by State")
heatmap_data = production_heatmap(df)
fig3 = px.choropleth(
    heatmap_data,
    locations="State",
    locationmode="geojson-id",
    geojson="https://raw.githubusercontent.com/plotly/datasets/master/india-states.geojson",
    color="Production",
    title="State-wise Crop Production",
    featureidkey="properties.ST_NM"
)
st.plotly_chart(fig3)
