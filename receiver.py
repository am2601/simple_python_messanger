import requests
import datetime


def print_messages(all_messages):
    for message in all_messages:
        message_time = datetime.datetime.fromtimestamp(message['time'])
        print(f"{message['login']}:", end=' ')
        print(message['text'])


def get_messages(after, login):
    response = requests.get(
        url='http://127.0.0.1:5000/get',
        params={'after': after}
    )
    return_messages = response.json()['return_messages']
    for i in return_messages:
        if i['login'] == login:
            return_messages.remove(i)
    if return_messages:
        print_messages(return_messages)
        after = return_messages[-1]['time']
    return after
