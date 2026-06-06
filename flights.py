import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Seoul Travel Dashboard", layout="wide")

# 2. Data Preparation
dob = pd.to_datetime('1989-08-01')
trips = [
    {"Date": "2010-06-10", "Return": "2010-07-20", "Carrier": "Korean Melbourne Travel", "Group": 1},
    {"Date": "2011-07-09", "Return": "2011-09-16", "Carrier": "Korean Air", "Group": 1},
    {"Date": "2013-12-11", "Return": "2014-02-18", "Carrier": "AirAsia", "Group": 1},
    {"Date": "2016-01-10", "Return": "2016-04-07", "Carrier": "AirAsia", "Group": 1},
    {"Date": "2018-01-06", "Return": "2018-01-27", "Carrier": "Singapore Airlines", "Group": 2},
    {"Date": "2022-07-31", "Return": "2022-08-12", "Carrier": "Cathay Pacific", "Group": 1},
    {"Date": "2024-03-18", "Return": "2024-04-17", "Carrier": "Singapore Airlines", "Group": 4},
    {"Date": "2025-09-13", "Return": "2025-10-15", "Carrier": "Singapore Airlines", "Group": 4},
    {"Date": "2026-04-08", "Return": "2026-04-25", "Carrier": "Cathay Pacific", "Group": 4}
]

df = pd.DataFrame(trips)
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Age'] = ((df['Date'] - dob).dt.days / 365.25).round(1)
df['Duration'] = (pd.to_datetime(df['Return']) - df['Date']).dt.days

# 3. Sidebar Filters (The "Dropbox" functionality)
st.sidebar.header("Filter Your Travels")
year_list = ["All"] + sorted(df['Year'].unique().tolist())
selected_year = st.sidebar.selectbox("Select Year", year_list)

carrier_list = ["All"] + sorted(df['Carrier'].unique().tolist())
selected_carrier = st.sidebar.selectbox("Select Carrier", carrier_list)

# Applying Filters
filtered_df = df.copy()
if selected_year != "All":
    filtered_df = filtered_df[filtered_df['Year'] == selected_year]
if selected_carrier != "All":
    filtered_df = filtered_df[filtered_df['Carrier'] == selected_carrier]

# 4. Main Dashboard Layout
st.title("🇰🇷 My Seoul Travel Journey (2010 - 2026)")
st.markdown("---")

# Row 1: The Main Timeline (Big)
st.subheader("Interactive Travel Timeline")
fig_timeline = px.scatter(
    filtered_df, x="Age", y=range(1, len(filtered_df) + 1),
    size="Duration", color="Carrier", hover_name="Date",
    labels={"y": "Trip Sequence", "Age": "Age at Departure"},
    size_max=60, template="plotly_white", height=500
)
fig_timeline.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')))
st.plotly_chart(fig_timeline, use_container_width=True)

# Row 2: Smaller Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Stay Duration (Days)")
    fig_dur = px.bar(filtered_df, x="Age", y="Duration", color="Carrier")
    st.plotly_chart(fig_dur, use_container_width=True)

with col2:
    st.subheader("Group Size Trend")
    fig_grp = px.line(filtered_df, x="Date", y="Group", markers=True)
    st.plotly_chart(fig_grp, use_container_width=True)

# Data Table
with st.expander("View Raw Data"):
    st.write(filtered_df)