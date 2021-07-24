from flask import Flask, request, abort
import time
import datetime
import json
import bots

app = Flask(__name__)

all_messages = [
    {
        'login': 'login',
        'text': 'text',
        'time': time.time()
    }
]


@app.route("/")
def server_info():
    return "<a href='/status'>Server info</a>"


@app.route("/status")
def status():
    names = []
    for message in all_messages:
        if message['login'] not in names:
            names.append(message['login'])
    status = {
        "status": "true",
        "name": "messanger",
        "number of members": len(names),
        "number of messages": len(all_messages),
        "time": str(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d-%H.%M.%S"))
    }
    return json.dumps(status)


@app.route("/send", methods=['POST'])
def send_message():
    data = request.json
    if not isinstance(data, dict):
        return abort(400)
    if 'login' not in data or 'text' not in data:
        return abort(400)

    login = data['login']
    text = data['text']

    if not isinstance(login, str) or not isinstance(text, str):
        return abort(400)
    if not (0 < len(login) < 30):
        return abort(400)
    if not (0 < len(text) < 100):
        return abort(400)

    message = {
        'login': login,
        'text': text,
        'time': time.time()
    }
    all_messages.append(message)
    names = []
    for message in all_messages:
        if message['login'] not in names:
            names.append(message['login'])
    server_status = []
    server_status.append(len(names))
    server_status.append(len(all_messages))
    x = bots.check_on_commands(text, login, server_status)
    if x != None:
        all_messages.append(x)

    return {'ok': True}


@app.route("/get")
def get_messages():
    try:
        klient_time = float(request.args['after'])
    except:
        return abort(400)

    return_messages = []
    for message in all_messages:
        if message['time'] > klient_time:
            return_messages.append(message)
    return {"return_messages": return_messages[:50]}


app.run()
