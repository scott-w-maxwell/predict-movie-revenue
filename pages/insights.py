import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

import pandas as pd

#import data
df = pd.read_csv('https://raw.githubusercontent.com/scottwmwork/datasets/master/tmdb_5000_movies.csv')

#Create columns out of release date column
df['release_date'] = pd.to_datetime(df['release_date'],infer_datetime_format = True)
df['release_year'] = df['release_date'].dt.year
df['release_month'] = df['release_date'].dt.month
df['release_day'] = df['release_date'].dt.month
df = df.drop(columns = 'release_date')

#Create plot
import plotly.express as px
fig1 = px.scatter_3d(df, x = 'release_year',y = 'budget', z = 'revenue', color = 'revenue',opacity=0.7,size_max=8, title = 'Revenue of Movies 1916-2017')
fig2 = px.scatter(df, x = 'budget', y ='revenue', color = 'revenue', trendline = 'ols', title = 'Revenue of Movies 1920-2017 based on budget')
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            
            As we can see from the 3d graph, the release year and budget effect the revenue quite heavily.
            """
        ),
    ],
    md=4,
)


column2 = dbc.Col(
    [
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2)
    ]
)

layout = dbc.Row([column1, column2])