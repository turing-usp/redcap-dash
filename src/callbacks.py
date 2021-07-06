import dash_bootstrap_components as dbc
import dash_trich_components as dtc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import State, Input, Output


def menu_callback(app):
    @app.callback(
        Output('output', 'children'),
        Input('menu-dropdown', 'value')
    )
    def update_output(value):
        return 'The current plot is {}'.format(value)
