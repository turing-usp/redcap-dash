import dash_bootstrap_components as dbc
import dash_trich_components as dtc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output, State
import awswrangler as wr
from utils.constants import APP_LOGO

path = "s3://turing-redcap-dashboard/dataset/"

df = wr.s3.read_parquet(path, dataset=True)


# add callback for toggling the collapse on small screens

dropdown = dcc.Dropdown(
    id = 'plot-dropdown',
    options = [
        {'label': 'Barplot', 'value': 'bp'},
        {'label': 'Mapplot', 'value': 'mp'},
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
        dbc.DropdownMenu(
            label = "Menu",
            id = "menu-dropdown",
            children=[
                dbc.DropdownMenuItem("Barplot"),
                dbc.DropdownMenuItem("Scatterplot"),
                dbc.DropdownMenuItem("Mapplot")
            ]
        )
    ],
    color="dark",
    dark=True
    ),
    dcc.Graph(
        id = 'samplechart',
        figure={
            'data' : [
                go.Bar(
                    x = df['idade'],
                    y = df['tabagismo'],
                    width = 2
                )
            ],
            'layout' : go.Layout(
                title = 'Scatterplot of age and tabagism',
                xaxis = {'title' : 'Age'},
                yaxis = {'title': 'Profit'}
            )
        }
    ),
    html.Div(id='output')
])
