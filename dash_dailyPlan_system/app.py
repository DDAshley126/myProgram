import dash
from dash import Dash, html
from server import app
import dash_bootstrap_components as dbc


app.layout = dbc.Container([
    html.Div('test'),
    dash.page_container
])


if __name__ == '__main__':
    app.run_server(debug=True)
