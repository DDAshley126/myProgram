from dash import Output, Input, callback


@callback(
    Output('monthly-title', 'children'),
    Input('month-select', 'value')
)
def update(value):
    return f'{value}月度复盘'


