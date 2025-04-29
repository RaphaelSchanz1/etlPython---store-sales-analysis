import plotly.express as px

def plot_sales_per_store(df):
    fig = px.bar(df, x="Store ID ", y="Store_Sales", title="Umsatz pro Filiale")
    fig.write_html("output/charts/store_sales.html")
    return fig
