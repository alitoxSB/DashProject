import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from plotly import subplots

df = pd.read_csv('delhi.csv')
df = df.head(1000)

layout = go.Layout(title = 'Heatmap temperature New Delhi India')

trace2 = go.Heatmap(x=df['moonrise'],y=df['date_time'],z=df['maxtempC'].values.tolist(), colorscale='Jet')
trace1 = go.Heatmap(x=df['moonrise'],y=df['date_time'],z=df['maxtempC'].values.tolist())

fig2 = subplots.make_subplots(rows=1,cols=2, subplot_titles=['normal', 'jet'],shared_yaxes=False)

fig2.append_trace(trace1,1,1)
fig2.append_trace(trace2,1,2)

pyo.plot(fig2, filename='heatmap_subplot.html')