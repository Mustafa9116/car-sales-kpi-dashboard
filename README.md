# car-sales-kpi-dashboard
An automotive market analytics dashboard evaluating global sales, pricing, and resale metrics.
A clean, interactive data dashboard built to analyze global automotive market trends across 30 major manufacturers. I wanted to build something that takes raw, complex dataset numbers and turns them into clean, instantly understandable business insights.

🔗 **Live App:** [car-sales-kpi-dashboard.streamlit.app](https://car-sales-kpi-dashboard.streamlit.app/)

![Dashboard Preview](Screenshot%202026-06-18%20at%202.27.20%E2%80%AFPM.png)

---

### The High-Level Numbers
The landing page gives a quick snapshot of the global market baselines:
* **Total Sales:** 6,363k units tracking overall market volume.
* **Average Price:** Sitting at around $27.0k.
* **Top Brand:** Ford takes the crown for total units sold.
* **Best Resale Asset:** The Carrera Cabrio stands out for holding its value.

### Deep Dives (The Tabs)
I split the deeper analytics into 5 specific views so you don't get hit with a wall of data all at once:
1. **Sales:** Focuses on volume. Includes a gradient bar chart showing the Top 10 Manufacturers by Total Sales.
2. **Pricing:** Breaks down market positioning, pricing tiers, and average costs across brands.
3. **Fuel Efficiency:** Tracks consumer efficiency trends and how different manufacturers stack up mechanically.
4. **Resale Value:** Looks at depreciation curves to see which cars actually hold their value over time.
5. **Performance:** Compares engine specs and horsepower against actual market demand.

### Tech Stack
* **Frontend & Framework:** Streamlit (Python) + custom dark theme adjustments.
* **Data Handling:** Pandas & NumPy for data parsing and cleaning.
* **Plots:** Plotly Express / Altair for the interactive, dynamic charts.

---

### Local Setup

If you want to run this locally on your machine, it's pretty straightforward:

1. Clone the repo:
```bash
git clone [https://github.com/yourusername/car-sales-kpi-dashboard.git](https://github.com/yourusername/car-sales-kpi-dashboard.git)
cd car-sales-kpi-dashboar
