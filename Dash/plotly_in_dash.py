import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
df = pd.read_csv('/home/alejandro/PycharmProjects/DashProject/example_plots_plotly/lineplot/GME_stock.csv')

#creamos el app de dash
app = dash.Dash()

colors = {'background':'#111111', 'text':'#7FDBFF'}

#creamos el objeto plotly.graph
data1 = [go.Scatter(x=df['date'],
                   y=df['close_price'],
                   mode='lines',
                   marker = dict(
                       size=12,
                       symbol='circle',
                       line={'width':3}
                   ))]
layout1 = go.Layout(title="GME Stocks prices",
                   xaxis=dict(title='Fecha'),
                   yaxis=dict(title='Precio de cierre'))

data2 = [go.Scatter(x=df['date'],
                   y=df['close_price'],
                   mode='lines',
                   marker = dict(
                       size=12,
                       symbol='circle',
                       line={'width':3}
                   ))]
layout2 = go.Layout(title="GME Stocks prices",
                   xaxis=dict(title='Fecha'),
                   yaxis=dict(title='Precio de cierre'))

app.layout = html.Div([dcc.Graph(id='scatterplot',
                                 figure={'data':data1,
                                         'layout':layout1}
                        ),
                                dcc.Graph(id='scatterplot2',
                                 figure={'data':data2,
                                         'layout':layout2}
                        )
                        ])

if __name__ == '__main__':
    app.run_server(port=8000)
