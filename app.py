import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import requests
import plotly.graph_objs as go
from collections import deque
import plotly

X1 = deque(maxlen=20)
X1.append(0)
Y1 = deque(maxlen=20)
Y1.append(0)

X2 = deque(maxlen=20)
X2.append(0)
Y2 = deque(maxlen=20)
Y2.append(0)

X3 = deque(maxlen=20)
X3.append(0)
Y3 = deque(maxlen=20)
Y3.append(0)

X4 = deque(maxlen=20)
X4.append(0)
Y4 = deque(maxlen=20)
Y4.append(0)

X5 = deque(maxlen=20)
X5.append(0)
Y5 = deque(maxlen=20)
Y5.append(0)

X6 = deque(maxlen=20)
X6.append(0)
Y6 = deque(maxlen=20)
Y6.append(0)

header = {'user-agent': 'Web App:Spike:v0.0.1: By /u/SpikeDevTom'}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

app.layout = html.Div([
    html.Div([html.H1('Spike'),
              html.H6('Who\'s Where Now'),
              ],
             style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Container([
        dbc.Row(
            [
                dbc.Col(dcc.Input(id='subreddit-1', type='text', placeholder='Add a subreddit', debounce=True)),
                dbc.Col(dcc.Input(id='subreddit-2', type='text', placeholder='Add a subreddit', debounce=True)),
                dbc.Col(dcc.Input(id='subreddit-3', type='text', placeholder='Add a subreddit', debounce=True)),
            ], no_gutters=True,
        )
    ], style={'margin': 'auto'}),

    dbc.Container([
        dbc.Row(
            [
                dbc.Col(dcc.Input(id='subreddit-4', type='text', placeholder='Add a subreddit', debounce=True)),
                dbc.Col(dcc.Input(id='subreddit-5', type='text', placeholder='Add a subreddit', debounce=True)),
                dbc.Col(dcc.Input(id='subreddit-6', type='text', placeholder='Add a subreddit', debounce=True)),
            ], no_gutters=True,
        )
    ], style={'margin': 'auto'}),
    
    dbc.Container([
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph-1', animate=True,
                                  style={
                                      'height': 400,
                                      'width': 400,
                                  }),
                    ),
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph-2', animate=True,
                                  style={
                                      'height': 400,
                                      'width': 400,
                                  })
                    )
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph-3', animate=True,
                                  style={
                                      'height': 400,
                                      'width': 400,
                                  })
                    )
                ),
            ], style={'vertical-align': 'middle'}
        ),
    ]),
  
    dbc.Container([
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph-4', animate=True,
                                  style={
                                      'height': 400,
                                      'width': 400,
                                  }),
                    ),
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph-5', animate=True,
                                  style={
                                      'height': 400,
                                      'width': 400,
                                  })
                    )
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph-6', animate=True,
                                  style={
                                      'height': 400,
                                      'width': 400,
                                  })
                    )
                ),
            ], style={'vertical-align': 'middle'}
        ),
    ]),
    dcc.Interval(
        id='graph-update',
        interval=30000,
        n_intervals=0
    )
])


@app.callback(
    Output('chosen-subreddit-1', 'children'),
    [Input('subreddit-1', 'value')])
def subreddit_input_1(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('graph-1', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit-1', 'children')])
def update_graph_1(n, subreddit):
    if subreddit is None:
        raise PreventUpdate
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    converted_users = process_data(url)
    X1.append(X1[-1] + 1)
    Y1.append(converted_users)

    data = plotly_graph(X1, Y1)

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X1), max(X1)]),
                                                yaxis=dict(range=[min(Y1), max(Y1)]), )}


@app.callback(
    Output('chosen-subreddit-2', 'children'),
    [Input('subreddit-2', 'value')])
def subreddit_input_2(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('graph-2', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit-2', 'children')])
def update_graph_2(n, subreddit):
    if subreddit is None:
        raise PreventUpdate
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    converted_users = process_data(url)
    X2.append(X2[-1] + 1)
    Y2.append(converted_users)

    data = plotly_graph(X2, Y2)

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X2), max(X2)]),
                                                yaxis=dict(range=[min(Y2), max(Y2)]), )}


@app.callback(
    Output('chosen-subreddit-3', 'children'),
    [Input('subreddit-3', 'value')])
def subreddit_input_3(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('graph-3', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit-3', 'children')])
def update_graph_3(n, subreddit):
    if subreddit is None:
        raise PreventUpdate
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    converted_users = process_data(url)
    X3.append(X3[-1] + 1)
    Y3.append(converted_users)

    data = plotly_graph(X3, Y3)

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X3), max(X3)]),
                                                yaxis=dict(range=[min(Y3), max(Y3)]), )}


@app.callback(
    Output('chosen-subreddit-4', 'children'),
    [Input('subreddit-4', 'value')])
def subreddit_input_4(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('graph-4', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit-4', 'children')])
def update_graph_4(n, subreddit):
    if subreddit is None:
        raise PreventUpdate
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    converted_users = process_data(url)
    X4.append(X4[-1] + 1)
    Y4.append(converted_users)

    data = plotly_graph(X4, Y4)

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X4), max(X4)]),
                                                yaxis=dict(range=[min(Y4), max(Y4)]), )}


@app.callback(
    Output('chosen-subreddit-5', 'children'),
    [Input('subreddit-5', 'value')])
def subreddit_input_5(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('graph-5', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit-5', 'children')])
def update_graph_5(n, subreddit):
    if subreddit is None:
        raise PreventUpdate
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    converted_users = process_data(url)
    X5.append(X5[-1] + 1)
    Y5.append(converted_users)

    data = plotly_graph(X5, Y5)

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X5), max(X5)]),
                                                yaxis=dict(range=[min(Y5), max(Y5)]), )}


@app.callback(
    Output('chosen-subreddit-6', 'children'),
    [Input('subreddit-6', 'value')])
def subreddit_input_6(submitted_subreddit):
    return submitted_subreddit


@app.callback(Output('graph-6', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('chosen-subreddit-6', 'children')])
def update_graph_6(n, subreddit):
    if subreddit is None:
        raise PreventUpdate
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    converted_users = process_data(url)
    X6.append(X6[-1] + 1)
    Y6.append(converted_users)

    data = plotly_graph(X6, Y6)

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X6), max(X6)]),
                                                yaxis=dict(range=[min(Y6), max(Y6)]), )}


def process_data(url):
    r = requests.get(url, headers=header)
    response = r.json()
    converted_users = int(format(response["data"]["accounts_active"]))
    return converted_users


def plotly_graph(X, Y):
    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )
    return data


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False)
