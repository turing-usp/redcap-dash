from dash import Dash
import dash_bootstrap_components as dbc

from src.layout import layout
from src.callbacks import menu_callback, menu_title_callback


app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="RedCap"
)

menu_callback(app)
menu_title_callback(app)

app.layout = layout

if __name__ == '__main__':
    app.run_server(port=4050)
