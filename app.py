import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import requests
import plotly.graph_objs as go
from collections import deque
import plotly

X1 = deque(maxlen=20)
X1.append(1)
Y1 = deque(maxlen=20)
Y1.append(0)
X2 = deque(maxlen=20)
X2.append(1)
Y2 = deque(maxlen=20)
Y2.append(0)
X3 = deque(maxlen=20)
X3.append(1)
Y3 = deque(maxlen=20)
Y3.append(0)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

app.layout = html.Div([
    html.Div([html.H1('Spike'),
              html.H6('Who\'s Where Now'),
              ],
             style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row(
        [
            dbc.Col(dcc.Input(id='subreddit-1', type='text', placeholder='Add a subreddit', debounce=True)),
            dbc.Col(dcc.Input(id='subreddit-2', type='text', placeholder='Add a subreddit', debounce=True)),
            dbc.Col(dcc.Input(id='subreddit-3', type='text', placeholder='Add a subreddit', debounce=True)),
        ], style={'textAlign': 'center'}
    ),
    dbc.Row(
        [
            dbc.Col(
                html.Div(
                    dcc.Graph(id='graph-1', animate=True,
                              style={
                                  'height': 500,
                                  'width': 500,
                              }),
                ),
            ),
            dbc.Col(
                html.Div(
                    dcc.Graph(id='graph-2', animate=True,
                              style={
                                  'height': 500,
                                  'width': 500,
                              })
                )
            ),
            dbc.Col(
                html.Div(
                    dcc.Graph(id='graph-3', animate=True,
                              style={
                                  'height': 500,
                                  'width': 500,
                              })
                )
            ),
        ]
    ),
    dcc.Interval(
        id='graph-update',
        interval=5000,
        n_intervals=0
    ),
    dbc.Row(
        [
            dbc.Col(html.Div(id='chosen-subreddit-1')),
            dbc.Col(html.Div(id='chosen-subreddit-2')),
            dbc.Col(html.Div(id='chosen-subreddit-3')),
        ], style={'text-align': 'center'}
    )
])


@app.callback(
    Output('chosen-subreddit-1', 'children'),
    [Input('subreddit-1', 'value')])
def subreddit_input_1(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('graph-1', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit-1', 'children')])
def update_graph_scatter_1(n, subreddit):
    url_1 = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = requests.get(url_1, headers={'user-agent': 'Web App:Spike:v0.0.1: By /u/SpikeDevTom'})
    response = r.json()
    converted_users = int(format(response["data"]["accounts_active"]))
    X1.append(X1[-1] + 1)
    Y1.append(converted_users)

    data = plotly.graph_objs.Scatter(
        x=list(X1),
        y=list(Y1),
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X1), max(X1)]),
                                                yaxis=dict(range=[min(Y1), max(Y1)]), )}


@app.callback(
    Output('chosen-subreddit-2', 'children'),
    [Input('subreddit-2', 'value')])
def subreddit_input_2(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('graph-2', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit-2', 'children')])
def update_graph_scatter_2(n, subreddit):
    url_2 = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = requests.get(url_2, headers={'user-agent': 'Web App:Spike:v0.0.1: By /u/SpikeDevTom'})
    response = r.json()
    converted_users = int(format(response["data"]["accounts_active"]))
    X2.append(X2[-1] + 1)
    Y2.append(converted_users)

    data = plotly.graph_objs.Scatter(
        x=list(X2),
        y=list(Y2),
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X2), max(X2)]),
                                                yaxis=dict(range=[min(Y2), max(Y2)]), )}


@app.callback(
    Output('chosen-subreddit-3', 'children'),
    [Input('subreddit-3', 'value')])
def subreddit_input_3(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('graph-3', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit-3', 'children')])
def update_graph_scatter_3(n, subreddit):
    url_3 = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = requests.get(url_3, headers={'user-agent': 'Web App:Spike:v0.0.1: By /u/SpikeDevTom'})
    response = r.json()
    converted_users = int(format(response["data"]["accounts_active"]))
    X3.append(X3[-1] + 1)
    Y3.append(converted_users)

    data = plotly.graph_objs.Scatter(
        x=list(X3),
        y=list(Y3),
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X3), max(X3)]),
                                                yaxis=dict(range=[min(Y3), max(Y3)]), )}


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False)
