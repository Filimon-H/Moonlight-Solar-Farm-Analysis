import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Solar Farm Insights", layout="wide")

# Title
st.title("🌞 Solar Farm Analysis Dashboard")

# Load data
data_path = r"C:\Users\User\Desktop\Week_0\Moonlight-Solar-Farm-Analysis\Data\merged_solar_data.csv"

@st.cache_data
def load_data(path):
    df = pd.read_csv(path, parse_dates=["Timestamp"])
    return df

df_all = load_data(data_path)

# Sidebar filters
st.sidebar.header("🔧 Filters")

# Select countries
countries = df_all["Country"].unique().tolist()
selected_countries = st.sidebar.multiselect("Select Countries", countries, default=countries)

# Select metric
metrics = ['GHI', 'DNI', 'DHI']
selected_metric = st.sidebar.selectbox("Select Solar Metric", metrics)

# Filter dataset
filtered_df = df_all[df_all["Country"].isin(selected_countries)]

# Tabs
tab1, tab2 = st.tabs(["📊 Boxplot", "📈 Regions"])

with tab1:
    st.subheader(f"{selected_metric} Distribution by Country")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=filtered_df, x="Country", y=selected_metric, palette="Set2", ax=ax)
    st.pyplot(fig)

with tab2:
    st.subheader(f"Top 10 Averages of {selected_metric}")
    if "Region" in filtered_df.columns:
        top_df = (
            filtered_df.groupby(["Country", "Region"])[selected_metric]
            .mean()
            .reset_index()
            .sort_values(by=selected_metric, ascending=False)
            .head(10)
        )
    else:
        top_df = (
            filtered_df.groupby("Country")[selected_metric]
            .mean()
            .reset_index()
            .sort_values(by=selected_metric, ascending=False)
        )

    st.dataframe(top_df, use_container_width=True)
