import pandas as pd

def calculate_kpis(df):
    df["Sales_per_Sqm"] = df["Store_Sales"] / df["Store_Area"]
    df["Sales_per_Customer"] = df["Store_Sales"] / df["Daily_Customer_Count"]
    df["Items_per_Sqm"] = df["Items_Available"] / df["Store_Area"]
    return df

if __name__ == "__main__":
    print("transform.py geladen")