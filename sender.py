import requests


def send_message(login, text=''):
    if text == '':
        text = input()
    response = requests.post(
        url='http://127.0.0.1:5000/send',
        json={'login': login, 'text': text},
    )
