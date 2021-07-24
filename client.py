from sender import send_message
from receiver import get_messages
import threading
import time

after = time.time()
login = input('Enter your login: ')
send_message('system', f'{login} join')
while True:
    x = threading.Thread(target=send_message, args=(login,))
    x.start()
    after = get_messages(after, login)
