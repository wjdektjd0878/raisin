from flask import Flask, redirect, request, session, url_for
from google_auth_oauthlib.flow import Flow
from pip._vendor import requests
import json


app = Flask(__name__)
app.secret_key = 'jungdasungraisin'  # 이 부분은 실제 앱에서는 보안상 이유로 공유하면 안됩니다.

webClientId = ''
clientSecret = ''
serverUrl = 'localhost'


@app.route('/')
def index():
    if 'credentials' not in session:
        return redirect('authorize')

    credentials = session['credentials']

    resp = requests.post(f'{serverUrl}/login_with_token', data={'id_token': credentials['id_token']})

    return resp.text


@app.route('/authorize')
def authorize():
    flow = Flow.from_client_config(
        client_config={
            "web": {
                "client_id": webClientId,
                "client_secret": clientSecret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [
                    "https://localhost:5000/oauth2callback"
                ],
                "scope": "https://www.googleapis.com/auth/userinfo.profile"
            }
        },
        scopes=['openid', 'email', 'profile'],
        redirect_uri=url_for('oauth2callback', _external=True)
    )

    authorization_url, state = flow.authorization_url()

    session['state'] = state

    return redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
    state = session['state']

    flow = Flow.from_client_config(
        client_config={
            "web": {
                "client_id": webClientId,
                "client_secret": clientSecret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [
                    "https://localhost:5000/oauth2callback"
                ],
                "scope": "https://www.googleapis.com/auth/userinfo.profile"
            }
        },
        scopes=['openid', 'email', 'profile'],
        state=state,
        redirect_uri=url_for('oauth2callback', _external=True)
    )

    flow.fetch_token(authorization_response=request.url)

    session['credentials'] = credentials = flow.credentials.to_json()

    credentials = json.loads(credentials)

    with open('credentials.json', 'w') as json_file:
        json_file.write(credentials)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
