import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
df = pd.read_csv('imdb_top_1000.csv')
df = df.head(100)
df = df.sort_values(by='IMDB_Rating', ascending=False)

#data = [go.Bar(x=df['Series_Title'],
               #y=df['IMDB_Rating'])]

trace1 = go.Bar(x=df['Series_Title'],y=df['IMDB_Rating'], name='Rating', marker={'color':'#ff1c7c'})

trace2 = go.Bar(x=df['Series_Title'], y=df['Meta_score'], name='Meta Score', marker={'color':'#1cbaff'})

layout = go.Layout(title='Calificacion de sieres',
                   xaxis=dict(title='Nombre de serie'),
                   yaxis=dict(title='calificacion'),
                   #barmode='stack' #--> Para apilarlas
                   )

data = [trace1, trace2]

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar_plot.html')