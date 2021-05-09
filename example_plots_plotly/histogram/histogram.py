import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import subplots

dff=[1,2,3,4,5,6,7,8,8,8,8,8,8,9,9,9,7,4,3,2,1,13,4,2,2,3,4,5,6,3,4,1,11,12]

data = [go.Histogram(x=dff, xbins=dict(start=0,end=13,size=2), histnorm='probability')]
layout = go.Layout(title='Histogram of density planets')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='density.html')