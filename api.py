import os
import requests
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

client_id = " this is rest api key "
client_secret = " this is client secret key "
domain = "http://localhost:4000"
redirect_uri = domain + "/redirect"
kauth_host = "https://kauth.kakao.com"
kapi_host = "https://kapi.kakao.com"
message_template = '{"object_type":"text","text":"Hello, world!","link":{"web_url":"https://developers.kakao.com","mobile_web_url":"https://developers.kakao.com"}}'
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/authorize")
def authorize():
    scope_param = ""
    if request.args.get("scope"):
        scope_param = "&scope=" + request.args.get("scope")
    return redirect(
        "{0}/oauth/authorize?response_type=code&client_id={1}&redirect_uri={2}{3}".format(kauth_host, client_id,
                                                                                          redirect_uri, scope_param))


@app.route("/redirect")
def redirect_page():
    data = {'grant_type': 'authorization_code',
            'client_id': client_id,
            'redirect_uri': redirect_uri,
            'client_secret': client_secret,
            'code': request.args.get("code")}
    resp = requests.post(kauth_host + "/oauth/token", data=data)
    session['access_token'] = resp.json()['access_token']
    return redirect("/?login=success")


@app.route("/profile")
def profile():
    headers = {'Authorization': 'Bearer ' + session.get('access_token', '')}
    resp = requests.get(kapi_host + "/v2/user/me", headers=headers)
    return resp.text


@app.route("/friends")
def friends():
    headers = {'Authorization': 'Bearer ' + session.get('access_token', '')}
    resp = requests.get(kapi_host + "/v1/api/talk/friends", headers=headers)
    return resp.text


@app.route("/message")
def message():
    headers = {'Authorization': 'Bearer ' + session.get('access_token', '')}
    data = {
        'template_object': message_template}
    resp = requests.post(kapi_host + "/v2/api/talk/memo/default/send", headers=headers, data=data)
    return resp.text


@app.route("/friend-message")
def friends_message():
    headers = {'Authorization': 'Bearer ' + session.get('access_token', '')}
    data = {
        'receiver_uuids': '[{0}]'.format(request.args.get("uuid")),
        'template_object': message_template}
    resp = requests.post(kapi_host + "/v1/api/talk/friends/message/default/send", headers=headers, data=data)
    return resp.text


@app.route("/logout")
def logout():
    headers = {'Authorization': 'Bearer ' + session.get('access_token', '')}
    resp = requests.post(kapi_host + "/v1/user/logout", headers=headers)
    return resp.text


@app.route("/unlink")
def unlink():
    headers = {'Authorization': 'Bearer ' + session.get('access_token', '')}
    resp = requests.post(kapi_host + "/v1/user/unlink", headers=headers)
    return resp.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=4000)