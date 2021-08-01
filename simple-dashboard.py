import dash
import dash_core_components as dcc
import dash_html_components as html
import chart_studio.plotly as py
from dash_html_components.Title import Title
from pandas.core.algorithms import mode
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("C:/Users/mohit/Downloads/Plotly-Dashboards-with-Dash-master/Data/OldFaithful.csv")
# print(df.head())
print(df.columns)

xnum = df['X']
ynum = df['Y']

app = dash.Dash()

#Define Graph Object
G1 = dcc.Graph(id='simple1', figure={
    'data':[go.Scatter(
        x=xnum,
        y=ynum,
        mode='markers'
    )],
    'layout':go.Layout(title="Old Faithful Eruption Intervals v Durations",
                        xaxis={'title':'Duration of erruption (minutes)'},
                        yaxis={'title':'Interval to next eruption (minutes)'},)
})

app.layout = html.Div([G1], title="My Plot",)

if __name__ == '__main__':
    app.run_server()