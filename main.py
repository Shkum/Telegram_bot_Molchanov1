import requests
import misk




token = misk.token

# https://api.telegram.org/bot6055721431:AAFojZYoqPa_ZyicvRB3Qy9kagkkAUIWsYU/getUpdates

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



def main():
    print(get_message())
    # d = get_updates()

    # with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()

