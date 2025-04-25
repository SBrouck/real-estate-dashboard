import pandas as pd

def calculate_gross_yield(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["annual_rent"] = df["monthly_rent"] * 12
    df["gross_yield"] = (df["annual_rent"] / df["purchase_price"]) * 100
    return df

def calculate_net_yield_and_cashflow(df: pd.DataFrame, vacancy_rate: float = 0.0) -> pd.DataFrame:
    """
    Computes net yield and cash flow, adjusted by vacancy rate (in %).
    """
    df = df.copy()
    monthly_vacancy_loss = df["monthly_rent"] * (vacancy_rate / 100)
    effective_rent = df["monthly_rent"] - monthly_vacancy_loss

    df["net_annual_rent"] = (effective_rent - df["monthly_expenses"] - (df["property_tax"] / 12)) * 12
    df["net_yield"] = (df["net_annual_rent"] / df["purchase_price"]) * 100
    df["monthly_cashflow"] = effective_rent - df["monthly_expenses"] - (df["property_tax"] / 12)

    return df

