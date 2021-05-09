import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('dataset-limpo.csv')
df=df.head(1000)

map_box_access = 'pk.eyJ1IjoiYWxpdG94c2IiLCJhIjoiY2tuaDVnOGc4MjRuYzJub295bmQyNWhndyJ9.i6J_x3V7zE2XZhVw2EsOLA'

fig = go.Figure(go.Scattermapbox(
    lon = df['longitude'],
    lat = df['latitude'],
    marker=go.scattermapbox.Marker(
        size=df['id']/1000,
        color=df['id.1']/1000
    )
))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=map_box_access,
        center=dict(
            lat=-23.43702,
            lon=-46.715887
        ),
        zoom=5
        )

)

pyo.plot(fig, filename='geomap.html')