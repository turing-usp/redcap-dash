import dash_bootstrap_components as dbc
import dash_trich_components as dtc
import dash_core_components as dcc
import dash_html_components as html
import dash
import plotly.graph_objs as go
from dash.dependencies import State, Input, Output
from utils.data import df

print(df.head())


def menu_callback(app):
    @app.callback(
        Output('graph_output', 'figure'),
        [Input('plot-dropdown', 'value')]
    )
    def update_output(value):

        figure = None

        if value == 'bp':
            print(value)
            figure = go.Figure()
            figure.add_trace(go.Bar(
                                    x = df['idade'],
                                    y = df['tabagismo'],
                                    width = 2
                                )
                             )

        if value == "sp":
            print(value)
            figure = go.Figure()
            figure.add_trace(go.Scatter(
                                    x = df['idade'],
                                    y = df['tabagismo'],
                                    mode='markers'
                                )
                             )

        if value == "lp":
            print(value)
            figure = go.Figure()
            figure.add_trace(go.Scatter(
                                    x = df['idade'],
                                    y = df['tabagismo'],
                                    mode='lines'
                                )
                             )

        return figure


def menu_title_callback(app):
    @app.callback(
        Output('graph_title', 'children'),
        [Input('plot-dropdown', 'value')]
    )
    def update_output(value):

        name = None

        if value == 'bp':
            name = "Barplot"

        if value == "sp":
            name = "Scatterplot"

        if value == "lp":
            name = "Lineplot"

        return name
