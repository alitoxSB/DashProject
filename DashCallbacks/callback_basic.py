import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id="Mi-input",value="valor inicial",type="text"),
    html.Div(id="Mi-salida")
])

@app.callback(
    Output("Mi-salida","children"),
    [Input("Mi-input","value")]
)
def actualizar_div(valor_entrada):
    return 'Has insertado : "{}"'.format(valor_entrada)

if __name__ == '__main__':
    app.run_server(port=8010)