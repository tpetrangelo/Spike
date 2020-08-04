import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import requests
import plotly.graph_objs as go
from collections import deque
import plotly

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(0)

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
        interval=15000,
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
def subreddit_input(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('graph-1', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit-1', 'children')])
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
