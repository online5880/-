import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


def count_plot(df: pd.DataFrame, column_name: str) -> px.histogram:
    fig = px.histogram(
        data_frame=df,
        x=column_name,
        title=f"Count plot of {column_name}",
        category_orders={column_name: df[column_name].value_counts().index},
    )
    return fig


def histogram_plot(df: pd.DataFrame, column_name: str) -> px.histogram:
    fig = px.histogram(data_frame=df,
                       x=column_name,
                       title=f"Histogram plot of {column_name}")
    return fig


def plot_df(df):
    fig_list = list()

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            fig = histogram_plot(df, column)
        elif pd.api.types.is_object_dtype(df[column]):
            fig = count_plot(df, column)
        fig_list.append(fig)
        return fig_list
