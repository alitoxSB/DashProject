import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
df = pd.read_csv('GME_stock.csv')

#Primero definimos el grafico de line, con la ayuda de la libreria PLotly.graph_objs
line_close = go.Scatter(x=df['date'],
                   y=df['close_price'],
                   mode='lines',
                   name='Cierre'
                   )

line_open = go.Scatter(x=df['date'],
                   y=df['open_price'],
                   mode='lines',
                   name='Apertura'
                   )

data = [line_close,line_open]

layout = go.Layout(title="GME Stocks prices",
                   xaxis=dict(title='Fecha'),
                   yaxis=dict(title='Precio de cierre'))

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='line_plot.html')