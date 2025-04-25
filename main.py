import streamlit as st
import pandas as pd
import plotly.express as px
from app.logic import calculate_gross_yield, calculate_net_yield_and_cashflow

# Static coordinates for city map
CITY_COORDS = {
    "Lyon": (45.75, 4.85),
    "Marseille": (43.30, 5.37),
    "Paris": (48.85, 2.35),
    "Nantes": (47.22, -1.55),
    "Bordeaux": (44.84, -0.58),
    "Toulouse": (43.60, 1.44),
    "Lille": (50.63, 3.06),
    "Strasbourg": (48.58, 7.75),
    "Rennes": (48.11, -1.67),
    "Montpellier": (43.61, 3.88),
}

# Page config
st.set_page_config(page_title="Real Estate Investment Dashboard", layout="wide")

# Header
st.title("Real Estate Investment Dashboard")
st.markdown("Analyze and simulate the profitability of real estate investments with interactive filters and KPIs.")
st.markdown("**Created by Sacha Brouck** — [GitHub](https://github.com/SBrouck)")

# File upload
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    df = calculate_gross_yield(df)

    # Sidebar filters
    st.sidebar.header("Filters")
    cities = df["city"].unique().tolist()
    selected_cities = st.sidebar.multiselect("Select cities", options=cities, default=cities)

    price_min = int(df["purchase_price"].min())
    price_max = int(df["purchase_price"].max())
    selected_price = st.sidebar.slider("Purchase price range", price_min, price_max, (price_min, price_max))

    size_min = int(df["size_sqm"].min())
    size_max = int(df["size_sqm"].max())
    selected_size = st.sidebar.slider("Size (sqm)", size_min, size_max, (size_min, size_max))

    st.sidebar.markdown("---")
    vacancy_rate = st.sidebar.slider("Vacancy rate (%)", 0.0, 20.0, 5.0, step=0.5)

    # Filtered data
    filtered_df = df[
        (df["city"].isin(selected_cities)) &
        (df["purchase_price"] >= selected_price[0]) &
        (df["purchase_price"] <= selected_price[1]) &
        (df["size_sqm"] >= selected_size[0]) &
        (df["size_sqm"] <= selected_size[1])
    ]

    filtered_df = calculate_net_yield_and_cashflow(filtered_df, vacancy_rate=vacancy_rate)

    # Table
    st.subheader("Filtered Properties")
    st.dataframe(filtered_df)

    # KPI
    st.subheader("Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Gross Yield (%)", f"{filtered_df['gross_yield'].mean():.2f}")
    col2.metric("Net Yield (%)", f"{filtered_df['net_yield'].mean():.2f}")
    col3.metric("Monthly Cash Flow (€)", f"{filtered_df['monthly_cashflow'].mean():.2f}")
    col4.metric("Number of Properties", len(filtered_df))

    # Visualizations
    st.subheader("Visualizations")

    avg_yield_by_city = (
        filtered_df.groupby("city")["gross_yield"]
        .mean()
        .reset_index()
        .sort_values(by="gross_yield", ascending=False)
    )

    fig1 = px.bar(
        avg_yield_by_city,
        x="city",
        y="gross_yield",
        title="Average Gross Yield by City",
        labels={"gross_yield": "Gross Yield (%)", "city": "City"},
        text_auto=".2f"
    )
    fig1.update_layout(template="simple_white")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.histogram(
        filtered_df,
        x="gross_yield",
        nbins=8,
        title="Distribution of Gross Yield (%)",
        labels={"gross_yield": "Gross Yield (%)"},
    )
    fig2.update_layout(
        template="simple_white",
        yaxis=dict(rangemode="tozero"),
        bargap=0.1
    )
    mean_yield = filtered_df["gross_yield"].mean()
    fig2.add_vline(x=mean_yield, line_dash="dash", line_color="red")
    fig2.add_annotation(x=mean_yield, y=0, text=f"Mean: {mean_yield:.2f}%", showarrow=False, font=dict(size=12, color="red"))
    st.plotly_chart(fig2, use_container_width=True)

    # Map
    st.subheader("Property Map (city-based)")
    if "city" in filtered_df.columns:
        map_df = filtered_df.copy()
        map_df["lat"] = map_df["city"].map(lambda c: CITY_COORDS.get(c, (None, None))[0])
        map_df["lon"] = map_df["city"].map(lambda c: CITY_COORDS.get(c, (None, None))[1])
        map_df = map_df.dropna(subset=["lat", "lon"])
        st.map(map_df[["lat", "lon"]])
