import dash_bootstrap_components as dbc
import dash_trich_components as dtc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output, State
from utils.constants import APP_LOGO
from utils.data import df
# add callback for toggling the collapse on small screens

dropdown = dcc.Dropdown(
    id = 'plot-dropdown',
    options = [
        {'label': 'Barplot', 'value': 'bp'},
        {'label': 'Lineplot', 'value': 'lp'},
        {'label': 'Scatterplot', 'value': 'sp'}
    ],
    value = 'bp'
)


layout = html.Div([
    dbc.Navbar(
        [
            html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=APP_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Hospital das Clínicas",
                                            className="ml-2",
                                            style={'font-family': 'Rockwell',
                                                   'font-size': '30px'})),
                ],
                align="center",
                no_gutters=True,
            ),
        ),
        dropdown,
    ],
    color="dark",
    dark=True
    ),
    html.H1(id="graph_title"),
    dcc.Graph(id='graph_output'),
    html.Div(id='menu_output')
])
