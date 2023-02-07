import requests
import misk

token = misk.token


URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    message = {'chat_id': chat_id,
               'text': message_text}
    return message


def send_message(chat_id, text="Your message received ..."):
    url = URL + f'sendmessage?chat_id={chat_id}&text={text}'
    requests.get(url)


def main():
    answer = get_message()
    chat_id = answer['chat_id']
    send_message(chat_id, 'what do you want for dinner')


if __name__ == '__main__':
    main()

