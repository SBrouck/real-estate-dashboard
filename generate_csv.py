import pandas as pd

data = [
    {"id": 1, "city": "Lyon", "purchase_price": 250000, "monthly_rent": 1000, "monthly_expenses": 150, "property_tax": 1200, "size_sqm": 55, "year_built": 2005},
    {"id": 2, "city": "Marseille", "purchase_price": 180000, "monthly_rent": 850, "monthly_expenses": 100, "property_tax": 900, "size_sqm": 48, "year_built": 1998},
    {"id": 3, "city": "Paris", "purchase_price": 400000, "monthly_rent": 1600, "monthly_expenses": 200, "property_tax": 1800, "size_sqm": 40, "year_built": 1975},
    {"id": 4, "city": "Nantes", "purchase_price": 220000, "monthly_rent": 950, "monthly_expenses": 120, "property_tax": 1100, "size_sqm": 52, "year_built": 2010},
    {"id": 5, "city": "Bordeaux", "purchase_price": 270000, "monthly_rent": 1100, "monthly_expenses": 130, "property_tax": 1300, "size_sqm": 50, "year_built": 2008},
    {"id": 6, "city": "Toulouse", "purchase_price": 210000, "monthly_rent": 900, "monthly_expenses": 110, "property_tax": 950, "size_sqm": 45, "year_built": 2003},
    {"id": 7, "city": "Lille", "purchase_price": 200000, "monthly_rent": 880, "monthly_expenses": 105, "property_tax": 970, "size_sqm": 46, "year_built": 2000},
    {"id": 8, "city": "Strasbourg", "purchase_price": 230000, "monthly_rent": 920, "monthly_expenses": 120, "property_tax": 1000, "size_sqm": 47, "year_built": 2002},
    {"id": 9, "city": "Rennes", "purchase_price": 240000, "monthly_rent": 940, "monthly_expenses": 130, "property_tax": 1150, "size_sqm": 49, "year_built": 2011},
    {"id": 10, "city": "Montpellier", "purchase_price": 260000, "monthly_rent": 970, "monthly_expenses": 140, "property_tax": 1250, "size_sqm": 51, "year_built": 2007}
]

df = pd.DataFrame(data)
df.to_csv("data/sample_properties.csv", index=False)
print("CSV generated successfully.")
