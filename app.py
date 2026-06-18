import streamlit as st
import plotly.express as px
from queries import (
    top_manufacturers_by_sales,
    avg_price_by_vehicle_type,
    top_fuel_efficient_cars,
    top_models_by_resale_value,
    horsepower_vs_price
)

# ── Page Config ──
st.set_page_config(page_title="Car Sales KPI Dashboard", page_icon="🚗", layout="wide")

# ── Custom CSS ──
st.markdown("""
<style>
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background: #0A0A0A; }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111111 0%, #0D0D0D 100%);
        border-right: 1px solid #1F1F1F;
    }
    section[data-testid="stSidebar"] * { color: #E0E0E0 !important; }
    .app-header {
        display: flex; align-items: center; gap: 18px;
        padding: 12px 0 28px 0; border-bottom: 1px solid #1F1F1F;
        margin-bottom: 20px;
    }
    .app-logo {
        width: 44px; height: 44px; border-radius: 12px;
        background: linear-gradient(135deg, #E30B1E 0%, #B80A18 100%);
        display: flex; align-items: center; justify-content: center;
        font-weight: 800; font-size: 22px; color: #fff;
    }
    .app-title { font-size: 26px; font-weight: 700; color: #FFFFFF; letter-spacing: -0.5px; }
    .app-subtitle { font-size: 13px; font-weight: 500; color: #888; margin-top: 2px; }
    .chart-box {
        background: #111111; border: 1px solid #1D1D1D; border-radius: 16px;
        padding: 20px; margin-bottom: 14px;
    }
    .chart-box h3 { font-size: 15px; font-weight: 600; color: #FFFFFF; margin: 0 0 8px 0; }
    [data-testid="stMetric"] { background: #111; border: 1px solid #1D1D1D; border-radius: 12px; padding: 12px 16px; }
    [data-testid="stMetric"] label { color: #888 !important; font-size: 11px; font-weight: 500; text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

# ── Header ──
st.markdown("""
<div class="app-header">
    <div class="app-logo">🚗</div>
    <div>
        <div class="app-title">Car Sales KPI Dashboard</div>
        <div class="app-subtitle">Global Market Analysis | 30 Manufacturers | Real Dataset</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── KPI Metric Cards ──
df1 = top_manufacturers_by_sales()
df2 = avg_price_by_vehicle_type()
df3 = top_fuel_efficient_cars()
df4 = top_models_by_resale_value()
df5 = horsepower_vs_price()

total_sales = df1["Total_Sales"].sum()
avg_price = df2["Avg_Price"].mean()
top_brand = df1.iloc[0]["Manufacturer"]
best_resale = df4.iloc[0]["Model"]

c1, c2, c3, c4 = st.columns(4)
c1.metric("💰 Total Sales", f"{total_sales:,.0f}k units")
c2.metric("💵 Avg Car Price", f"${avg_price:,.1f}k")
c3.metric("🏆 Top Brand", top_brand)
c4.metric("♻️ Best Resale", best_resale)

st.markdown("")

# ── Tabs ──
t1, t2, t3, t4, t5 = st.tabs(["Sales", "Pricing", "Fuel Efficiency", "Resale Value", "Performance"])

# Tab 1 — Sales
with t1:
    st.markdown('<div class="chart-box"><h3>Top 10 Manufacturers by Total Sales</h3>', unsafe_allow_html=True)
    fig = px.bar(df1, x="Manufacturer", y="Total_Sales",
                 color="Total_Sales", color_continuous_scale="Blues",
                 labels={"Total_Sales": "Total Sales (thousands)"})
    fig.update_layout(template="plotly_dark", paper_bgcolor="#111111", plot_bgcolor="#111111",
                      font_color="#CCC", height=400, margin=dict(l=0, r=0, t=10, b=10))
    fig.update_xaxes(gridcolor="#1F1F1F")
    fig.update_yaxes(gridcolor="#1F1F1F")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 2 — Pricing
with t2:
    st.markdown('<div class="chart-box"><h3>Average Price by Vehicle Type</h3>', unsafe_allow_html=True)
    fig = px.bar(df2, x="Vehicle_type", y="Avg_Price",
                 color="Avg_Price", color_continuous_scale="Reds",
                 labels={"Avg_Price": "Average Price (thousands)", "Vehicle_type": "Type"})
    fig.update_layout(template="plotly_dark", paper_bgcolor="#111111", plot_bgcolor="#111111",
                      font_color="#CCC", height=400, margin=dict(l=0, r=0, t=10, b=10))
    fig.update_xaxes(gridcolor="#1F1F1F")
    fig.update_yaxes(gridcolor="#1F1F1F")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 3 — Fuel Efficiency
with t3:
    st.markdown('<div class="chart-box"><h3>Top 10 Most Fuel Efficient Cars</h3>', unsafe_allow_html=True)
    fig = px.bar(df3, x="Fuel_efficiency", y="Model", orientation="h",
                 color="Fuel_efficiency", color_continuous_scale="Greens",
                 labels={"Fuel_efficiency": "Fuel Efficiency (MPG)"})
    fig.update_layout(template="plotly_dark", paper_bgcolor="#111111", plot_bgcolor="#111111",
                      font_color="#CCC", height=400, margin=dict(l=0, r=0, t=10, b=10))
    fig.update_xaxes(gridcolor="#1F1F1F")
    fig.update_yaxes(gridcolor="#1F1F1F")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 4 — Resale Value
with t4:
    st.markdown('<div class="chart-box"><h3>Top 10 Models by Resale Value</h3>', unsafe_allow_html=True)
    fig = px.treemap(df4, path=["Manufacturer", "Model"],
                     values="resale_value", color="resale_value",
                     color_continuous_scale="RdYlGn",
                     labels={"resale_value": "Resale Value (thousands)"})
    fig.update_layout(template="plotly_dark", paper_bgcolor="#111111",
                      font_color="#CCC", height=400, margin=dict(l=0, r=0, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 5 — Performance
with t5:
    st.markdown('<div class="chart-box"><h3>Horsepower vs Price by Manufacturer</h3>', unsafe_allow_html=True)
    fig = px.scatter(df5, x="Horsepower", y="Price_in_thousands",
                     color="Manufacturer", size="Horsepower",
                     hover_data=["Model"],
                     labels={"Price_in_thousands": "Price (thousands)"})
    fig.update_layout(template="plotly_dark", paper_bgcolor="#111111", plot_bgcolor="#111111",
                      font_color="#CCC", height=400, margin=dict(l=0, r=0, t=10, b=10))
    fig.update_xaxes(gridcolor="#1F1F1F")
    fig.update_yaxes(gridcolor="#1F1F1F")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ──
st.markdown("""
<div style="text-align:center;padding:20px 0 0 0;border-top:1px solid #1F1F1F;margin-top:20px;">
    <span style="color:#555;font-size:12px;">Car Sales KPI Dashboard | Built with Streamlit & Plotly | Real market data</span>
</div>
""", unsafe_allow_html=True)