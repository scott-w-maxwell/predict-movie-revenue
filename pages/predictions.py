import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from joblib import load
pipeline = load('assets/linear_regression.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Release Year'), 
        dcc.Slider(
            id='ReleaseYear', 
            min=1955, 
            max=2055, 
            step=1, 
            value=2018, 
            marks={n: str(n) for n in range(1960,2060,10)}, 
            className='mb-5', 
        ), 
        html.Div(id='YearSliderValue',className='mb-5'),
                        
        dcc.Markdown('#### Budget'),
        dcc.Slider(
            id='Budget', 
            min=1000000, 
            max=500000000, 
            step=5, 
            value=1000000, 
            marks={
              1000000:'$1m',
              125000000:'$125m',
              250000000:'$250m',
              375000000:'$375m‬',
              500000000:'$500m'
            }, 
            className='mb-5', 
        ),

        html.Div(id='BudgetSliderValue',className='mb-5'),

        dcc.Markdown('#### Genre'), 
        dcc.Dropdown(
            id='Genre', 
            options = [
                {'label': 'Science Fiction', 'value': 'Science Fiction'}, 
                {'label': 'Comedy', 'value': 'Comedy'}, 
                {'label': 'Action', 'value': 'Action'}, 
                {'label': 'Drama', 'value': 'Drama'}, 
                {'label': 'Documentary', 'value': 'Documentary'}, 
            ], 
            value = 'Action', 
            className='mb-5', 
        ), 

    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H6('Predicted Revenue:', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)


#### Auto Update
import pandas as pd

@app.callback(
    dash.dependencies.Output('YearSliderValue', 'children'),
    [dash.dependencies.Input('ReleaseYear', 'value')])
def update_output(value):
    return 'Selected: {}'.format(value)


@app.callback(
    dash.dependencies.Output('BudgetSliderValue', 'children'),
    [dash.dependencies.Input('Budget', 'value')])
def update_outputs(value):
    return 'Selected: ${}'.format(value)

@app.callback(
    Output('prediction-content', 'children'),
    [Input('ReleaseYear', 'value'), Input('Budget', 'value'), Input('Genre','value')],
)
def predict(ReleaseYear, Budget,Genre):
    df = pd.DataFrame(
        columns=['budget', 'original_language', 'runtime', 'status', 'release_year', 'title_changed', 'length_of_title',
       'genre_first_listed'], 
        data=[[Budget, 'en',107,'Released',ReleaseYear,0,15, Genre]]
    )
    y_pred = round(pipeline.predict(df)[0],2)
    # print("$",y_pred)
    return f'${y_pred:.0f}'

layout = dbc.Row([column1, column2])