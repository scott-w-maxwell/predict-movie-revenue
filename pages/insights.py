import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

import pandas as pd
import numpy as np

#import data
df = pd.read_csv('https://raw.githubusercontent.com/scottwmwork/datasets/master/tmdb_5000_movies.csv')

#Create columns out of release date column
df['release_date'] = pd.to_datetime(df['release_date'],infer_datetime_format = True)
df['release_year'] = df['release_date'].dt.year
df['release_month'] = df['release_date'].dt.month
df['release_day'] = df['release_date'].dt.month
df = df.drop(columns = 'release_date')

def wrangle(X):
  
  X = X.copy()
  X = X.reset_index()

  #Engineer features:
  #create feature for genre

  genre = []
  for x in X['genres']:
    if x == '[]':
      genre.append(np.nan)
    elif "Documentary" in x:
      genre.append("Documentary")
    elif "Animation" in x:
      genre.append("Animation")
    elif "Horror" in x:
      genre.append("Horror")
    elif "Science Fiction" in x:
      genre.append("Science Fiction")
    elif "Comedy" in x:
      genre.append("Comedy")
    elif "Drama" in x:
      genre.append("Drama")
    elif "Action" in x:
      genre.append("Action")
    else:
      genre.append("Other")

  X['genre'] = genre
  return X
df_new = wrangle(df)

top_movies_temp = df.sort_values(by = 'revenue').tail()
top_movies = pd.DataFrame()
top_movies['title'] = top_movies_temp.title
top_movies['release_year'] = top_movies_temp.release_year
top_movies['revenue'] = top_movies_temp.revenue


#Create plot
import plotly.express as px
fig1 = px.scatter_3d(df, x = 'release_year',y = 'budget', z = 'revenue', custom_data = 'title', color = 'revenue',opacity=0.7,size_max=8, title = 'Revenue of Movies<br>Based on Budget and Release Year', template = 'plotly_dark')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights

            We can see from this 3 Dimensional Graph that a movie's budget and release year greatly 
            influence a movie's revenue. You may notice at the top of this graph is the movie called "Avatar" that 
            came out in 2009 which had a budget of 237 million USD and produce 2.79 billion USD at the box office.
            
            """
        ),
        
    ],
    md=4,
)


column2 = dbc.Col(
    [
        dcc.Graph(figure=fig1)
    ]
)

layout = dbc.Row([column1, column2])