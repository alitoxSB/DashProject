import dash
import dash_core_components as dcc
import dash_html_components as html

#creamo al app dash
app = dash.Dash()

#Definimos el diccionario para utilizar los colores dentro de la app
colors = {'background':'#111111', 'text':'#7FDBFF'}

#Definimos el layout de la app a partir de componentes HTML y core.
app.layout = html.Div(children=[
    html.H1(children='Primer Dashboard con Dash',
            style={
                'textAlign':'center',
                'color':colors['text']
            }),
    html.Div(children='Dash: Framework para apps con Python',
             style={
                 'textAlign':'center',
                 'color':colors['text']}
             ),
    dcc.Graph(
        id='ejemplo',
        figure={
            'data':[
                {'x':[1,2,3,4,5], 'y':[5,6,7,8,9], 'type':'bar','name':'MA'},
                {'x':[1,2,3,4,5], 'y':[5,6,7,8,9], 'type':'bar','name':'BA'}],
            'layout':{
                'title':'Comparativa Madrid - Barcelona',
                'lot_bgcolor':colors['background'],
                'paper_bgcolor':colors['background'],
                'font':{'color':colors['text']}
            }
        }
    )
],
    style={'backgroundColor':colors['background']} #Div global con el estilo
)

if __name__ == '__main__':
    app.run_server(port=8000)