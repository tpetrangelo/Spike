#!/usr/bin/env python
import praw
from flask import Flask, abort, request, render_template, url_for
import requests
import requests.auth


CLIENT_ID = '8u4U4079k2ir3g'
CLIENT_SECRET = 'hB-jP41agCJb8MvF1-hn_Akt4-s'
REDIRECT_URI = "http://localhost:65010/reddit_callback"

app = Flask(__name__, template_folder='templates')

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     redirect_uri=REDIRECT_URI,
                     user_agent="Web App:Spike:v0.0.1: By /u/SpikeDevTom")



def base_headers():
    return {"User-Agent": user_agent()}


def user_agent():
    return 'Web App:Spike:v0.0.1: By /u/SpikeDevTom'


@app.route('/')
def homepage():
    text = '<a href="%s">Authenticate with reddit</a>'
    return text % make_authorization_url()


@app.route('/reddit_callback')
def reddit_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        abort(403)
    code = request.args.get('code')
    access_token = reddit.auth.authorize(code)
    '''
    subreddits = list(reddit.user.subreddits(limit=None))

    for subreddit in subreddits:
        subreddit_information = get_subreddit_ratio(subreddit.display_name, reddit)

        ratio = round(subreddit_information['ratio'], 2)

        active_users = subreddit_information['active_users']
        subscriber_count = subreddit_information['subscriber_count']
        print("%s --> %s%% of users (%s out of %s)" % (subreddit, ratio, f'{active_users:,}', f'{subscriber_count:,}'))
    '''
    return render_template('index.html', username=reddit.user.me())


def get_subreddit_ratio(sub_name, reddit_instance):
    subreddit = reddit_instance.subreddit(sub_name)
    active_users = subreddit.active_user_count
    subscriber_count = subreddit.subscribers
    ratio = (active_users / subscriber_count) * 100
    return {'ratio': ratio, 'active_users': active_users, 'subscriber_count': subscriber_count}


def save_created_state(state):
    pass


def is_valid_state(state):
    return True


def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI}
    headers = base_headers()
    response = requests.post("https://ssl.reddit.com/api/v1/access_token",
                             auth=client_auth,
                             headers=headers,
                             data=post_data)
    token_json = response.json()
    return token_json["access_token"]


def make_authorization_url():
    url = reddit.auth.url(["mysubreddits", "read", "identity"], "...", "permanent")
    return url




if __name__ == '__main__':
    app.run(debug=True, port=65010)
