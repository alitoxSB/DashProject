import dash
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df_cars = pd.read_csv('/example_plots_plotly/scatterplot/carprices.csv')

#Primero definimos el grafico de scatter, con la ayuda de la libreria PLotly.graph_objs
data_plot = [go.Scatter(x = df_cars['Mileage'],
            y = df_cars['Sell Price($)'],
            mode = 'markers')]

#segundo declaramos el layout, esto es el diseno que queremos darle.
layout_plot = go.Layout(title = "Car prices",
                   xaxis = dict(title='Mileage'),
                   yaxis = dict(title='Sell price'),
                   )

#Declaramos la figura donde le decimos cual es el data plot y el layout plot
fig = go.Figure(data=data_plot, layout=layout_plot)

#Finalmente creamos el archivo HTML para mostrar el plot.
pyo.plot(fig, filename='Plot_cars.html')






