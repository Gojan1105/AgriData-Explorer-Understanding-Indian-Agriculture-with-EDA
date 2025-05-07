# eda/analysis.py

import pandas as pd
import plotly.express as px

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    df.dropna(inplace=True)
    df.columns = df.columns.str.strip()
    df['Year'] = df['Year'].astype(int)
    return df

def top_crops_by_production(df, year=None):
    if year:
        df = df[df['Year'] == year]
    return df.groupby('Crop')['Production'].sum().sort_values(ascending=False).head(10)

def yield_trend(df, crop):
    df_crop = df[df['Crop'] == crop]
    return df_crop.groupby('Year')['Yield'].mean().reset_index()

def production_heatmap(df):
    return df.groupby('State')['Production'].sum().reset_index()
