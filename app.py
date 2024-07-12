from dash import Dash, Input, Output, html, dcc
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import numpy as np

dash_app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app = dash_app.server

dash_app.layout = html.Div([
    html.P("Dit is een test")
])

if __name__ == '__main__':
    dash_app.run_server(debug=True)