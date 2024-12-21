import dash
from dash import html
import feffery_antd_components as fac
import dash_bootstrap_components as dbc

dash.register_page(path='/page1', name='page1')

layout = dbc.Container([
    html.Div('Page1')
])