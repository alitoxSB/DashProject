import plotly.offline as pyo
import plotly.graph_objs as go

datos = [11,12,45,12,45,29,56,23,19,65,25,26,19,30,23,45,23,5,6,74,32,12,34,56,21]

data = [go.Box(y=datos)]
layout = go.Layout(title="Box Plot")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='bloxplot.html')
