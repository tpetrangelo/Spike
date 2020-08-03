# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests
import plotly.graph_objs as go
from collections import deque
import plotly
import random

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(0)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([html.H1('Spike'),
              html.H6('Who\'s Where Now'),
              html.Br(),
              dcc.Input(id='input-subreddits', type='text', placeholder='Add a subreddit', debounce=True), ],
             style={'textAlign': 'center'}),
    html.Hr(),
    html.Div(id='chosen-subreddit'),
    dcc.Graph(id='live-graph', animate=True),
    dcc.Interval(
        id='graph-update',
        interval=2000,
        n_intervals=0
    ),
])


@app.callback(
    Output('chosen-subreddit', 'children'),
    [Input('input-subreddits', 'value')])
def subreddit_input(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit', 'children')])
def update_graph_scatter(n, subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = requests.get(url, headers={'user-agent': 'Web App:Spike:v0.0.1: By /u/SpikeDevTom'})
    response = r.json()
    converted_users = int(format(response["data"]["accounts_active"]))
    X.append(X[-1] + 1)
    Y.append(converted_users)

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                yaxis=dict(range=[min(Y), max(Y)]), )}


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False)
