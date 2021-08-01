import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Title import Title
from numpy.random.mtrand import rand
import chart_studio.plotly as py
import plotly.graph_objects as go
import numpy as np

app = dash.Dash()

#Creating random data
np.random.seed(101)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

#Creating a plotly graph
app.layout = html.Div([dcc.Graph(id='scatterplot1',
                                    figure={
                                        'data':[
                                            go.Scatter(
                                                x=random_x,
                                                y=random_y,
                                                mode='markers',
                                                marker={
                                                    'size':12,
                                                    'color': 'rgb(51,204,153)',
                                                    'symbol':'pentagon',
                                                    'line':{'width':2},
                                                }
                                            )],
                                        'layout':go.Layout(title='First Scatter Plot',
                                                            xaxis={'title':'Title1 on The X Axis'}
                                        )}
),                      dcc.Graph(id='scatterplot2',
                                    figure={
                                        'data':[
                                            go.Scatter(
                                                x=random_x,
                                                y=random_y,
                                                mode='markers',
                                                marker={
                                                    'size':10,
                                                    'color': 'rgb(200,204,53)',
                                                    'symbol':'pentagon',
                                                    'line':{'width':2},
                                                }
                                            )],
                                        'layout':go.Layout(title='Second Scatter Plot',
                                                            xaxis={'title':'Title2 on The X Axis'}
                                        )}
)])

if __name__ == '__main__':
    app.run_server()