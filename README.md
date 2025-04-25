# 🏠 Real Estate Investment Dashboard

🔗 **Live App** → [Launch the Streamlit app](https://real-estate-dashboard-ffkxqbyp6y6ybe6ildsv3q.streamlit.app)

---

## Project Overview

During my internship as a Real Estate Investment Analyst at **Mantu**, I was responsible for automating the data extraction and analysis of a €200M real estate portfolio. The goal was to centralize operational and financial indicators in a single, dynamic dashboard to support efficient portfolio management.

While the original project was developed in Power BI, this public version recreates part of the logic and analytics in **Python and Streamlit**, to demonstrate my ability to:

- Automate financial and operational reporting
- Perform data analysis across multiple dimensions (KPI, filters, visualizations)
- Package and deploy a complete data product independently

This project is designed to be relevant for roles such as **Business Analyst**, **Data Analyst**, **Data Scientist**, or **Data Engineer**, and showcases my technical versatility in building end-to-end data solutions.

---

## Features

- Upload your own real estate dataset (CSV or Excel)
- Compute key performance indicators:
  - Gross Yield
  - Net Yield (adjustable via vacancy rate)
  - Monthly Cashflow
- Interactive filters (city, price, surface area)
- Visual dashboards:
  - Yield distribution
  - Yield by city
  - Property map by location
- Fully deployable Streamlit app

---

## 📂 Input File Format

To use this dashboard, upload a `.csv` or `.xlsx` file with the following column headers:

| Column Name        | Description                       | Example            |
|--------------------|-----------------------------------|--------------------|
| `city`             | City where the property is located | Paris              |
| `purchase_price`   | Property purchase price (€)        | 250000             |
| `monthly_rent`     | Monthly rental income (€)          | 1000               |
| `monthly_expenses` | Recurring monthly charges (€)      | 200                |
| `property_tax`     | Annual property tax (€)            | 900                |
| `size_sqm`         | Surface area (sqm)                 | 60                 |

A sample dataset is provided in the `/data/` folder.

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/SBrouck/real-estate-dashboard.git
cd real-estate-dashboard
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Then open your browser at: `http://localhost:8501`

---

## 👋 About Me

Hi! I'm Sacha Brouck — a real estate & data enthusiast passionate about making investment insights more accessible and actionable through technology.

I love building intuitive tools that bridge business logic and technical execution. Whether it's Power BI, Python or Streamlit, I'm all about creating clear, data-driven workflows that actually get used.

Currently based in Seattle, I'm open to opportunities across the US in roles such as Business Analyst, Data Analyst, Data Scientist or Data Engineer.

Feel free to connect, collaborate or just have a chat — always happy to exchange ideas!

GitHub: https://github.com/SBrouck

LinkedIn: www.linkedin.com/in/sacha-brouck

Mail: sbrouck@uw.edu / sachabrou@gmail.com
