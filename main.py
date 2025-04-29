from etl.extract import load_data
from etl.transform import calculate_kpis
from analysis.visualizations import plot_sales_per_store

df = load_data("data/store_sales.csv")
df = calculate_kpis(df)
plot_sales_per_store(df)
