import dash
from dash import html
import feffery_antd_components as fac
import dash_bootstrap_components as dbc
from dash_dailyPlan_system.assets.config import CONTAINER_STYLE


dash.register_page(__name__, path='/', name='home')

layout = dbc.Container([
    fac.AntdDatePicker(
        id='month-select',
        prefix=fac.AntdIcon(icon='antd-calendar'),
        value='2024年10月',
        picker='month',
        format='YYYY年MM月'
    ),
    dbc.Row([html.Div(id='monthly-title', className='title-style')], className='container-frame'),
    dbc.Row([
        dbc.Col([
            fac.AntdTable(
                columns=[
                    {
                        'title': '本月计划',
                        'dataIndex': '本月计划'
                    },
                    {
                        'title': '细分事项',
                        'dataIndex': '细分事项'
                    },
                    {
                        'title': '完成度',
                        'dataIndex': '完成度'
                    },
                ],
            )
        ], width=7),
        dbc.Col([
            dbc.Row([html.Div('11111')], style=CONTAINER_STYLE),
            dbc.Row([html.Div('22222222')], style=CONTAINER_STYLE)
        ], style={'row-gap': '10px'}, width=4),
    ], style={'column-gap': '15px'}),
])
