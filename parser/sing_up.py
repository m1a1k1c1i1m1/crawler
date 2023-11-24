import requests
from random import choice
from string import ascii_uppercase
from loguru import logger as log
import re
import json
from time import sleep

name = ''.join(choice(ascii_uppercase) for i in range(5)).lower()

headers = {'Content-Type': 'application/json'}
email = f'{name}@mailforspam.com'
url = f'https://www.mailforspam.com/mail/{name}/1'
url_sing_in = "https://api.av.by/auth/login/sign-in"

post_body = {
    "email": email,
    "name": "Максим",
    "password": "Faren12345",
    "userEula": {
        "accepted": "true"
    }
}

body = {
    "login": email,
    "password": "Faren12345"
}




def sing_up():
    loop_flag = True
    req_registretions = requests.post('https://api.av.by/auth/email/sign-up', json=post_body)
    log.info('запрос отправили для перехода после регистрации')
    while loop_flag == True:
        req_email = requests.get(url).content.decode()
        log.info('скачали страницу с сообщением')
        url_av = re.search(r"https://av\.by/confirm-registration\?token=\w+", req_email)
        if url_av != None:
            requests_sing_up = requests.get(url_av.group(0))
            if requests_sing_up.status_code == 200:
                sing_in = requests.post(url_sing_in, json=body, headers=headers).content.decode('utf-8')
                user = json.loads(sing_in)
                loop_flag = False
                log.info('пользователь зарегистрирован')
                return user['apiKey']
        else:
            log.info('нет еще сообщения')
            sleep(2)
