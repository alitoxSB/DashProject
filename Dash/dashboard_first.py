import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

#cargamos los datos
df = pd.read_csv('/home/alejandro/PycharmProjects/DashProject/Dash/SP500_data_.csv')

#creamos el diccionario de colores
colors={
    'background':'#000814',
    'text':'#F8F9FA'
}
#Creamos el plotly.graph
data_date_close = [go.Scatter(x=df['Date'],
                              y=df['Close'],
                              mode='lines')]
#Contruimos el Layout
layaout_data_close = go.Layout(title='SP500 Cotization',
                               xaxis=dict(title='fecha'),
                               yaxis=dict(title='SP500 Valor'))

#Creamos el plotly.graph 2
data_volume = [go.Bar(x=df['Date'],
                      y=df['Volume'])]

#Contruimos el Layout 2
data_volume_layout = go.Layout(title='SP500 Volumen',
                               xaxis=dict(title='Fecha'),
                               yaxis=dict(title='Volumen'))

#Definicion del Layout de la app a partir de componentes HTML.
app.layout = html.Div([
    html.Label('Seleccion'),
    dcc.Dropdown(
        options=[
            {'label': 'Apertura', 'value': 'Open'},
            {'label': 'Cierre', 'value': 'Close'},
        ],
        value='Close'
    ),
    dcc.Graph(id='lineplot',
              figure={'data':data_date_close,
                      'layout':layaout_data_close
            }
              ),
    dcc.Graph(id='barplot',
              figure={'data':data_volume,
                      'layout':data_volume_layout}
              )],
    style={'backgroundColor':colors['background']}
)
if __name__ == '__main__':
    app.run_server()