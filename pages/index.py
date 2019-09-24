import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predicting Movie Revenue

            Using machine learning, you can predict the revenue a movie based on budget, genre, and year.
            
            This may be useful for a variety of reasons such as movie producers who want to come up with a new idea for a movie that will create a large amount of revenue. It could also be useful for those interested in the profit a future movie that has been announced might make.
            """
        ),
        dcc.Link(dbc.Button('Call To Action', color='primary'), href='/predictions')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        # dcc.Graph(figure=fig),
        html.Img(src='assets/Movies.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])