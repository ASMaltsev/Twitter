import tweepy
import time
import pickle5 as pickle
import requests
import logging
from datetime import datetime

# telegram
token = '1597295765:AAEDlJoeTV_d2c-6ftkMoJi0Rd-0F1YD5XY'
chat_id_test = '-514373830'
chat_id_main = '-505095884'

# twitter
twitter_open_key = 'JzmIdfXOWGnSNfPKGryj8KHkQ'
twitter_secret_key = '1uvwjxOSnYgJwIik6oCL4nclzVIRgPzgaR4jgkbGuUfOOGwOT6'

twitter_token_open = '1380934730657505281-VquvHeQiG9VdXr3zzuF9nvQalmlgCf'
twitter_token_secret = 'jgCjdNrzmHJoQnafJnBi1PGGBwSmC47nC7clnhNbUuY94'


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


def get_friends(people: list, api_twitter):
    dict_friends = {}
    for person in people:
        friends = []
        logger.info(f'Get info for = {person}')
        try:
            for friend in tweepy.Cursor(api_twitter.friends_ids, person).items():
                friends.append(friend)
            dict_friends[person] = friends
        except:
            print(f'Error for {person}')
    return dict_friends


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('main')
    while True:
        logger.info('Start')
        auth = tweepy.OAuthHandler(twitter_open_key, twitter_secret_key)
        auth.set_access_token(twitter_token_open, twitter_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
        old_friends = load_obj('friends')

        current_friends = {}

        for k, v in old_friends.items():
            dict_friends = get_friends(v, api)
            current_friends[k] = dict_friends

        bot = BotHandler(token)

        for name, sets in old_friends.items():
            logger.info(f'NEW FRIENDS FOR {name.upper()}')
            if name == 'test_s' or name == 'test_d':
                bot.send_message(chat_id=chat_id_test, text=f'NEW FRIENDS FOR {name.upper()}')
            else:
                bot.send_message(chat_id=chat_id_main, text=f'NEW FRIENDS FOR {name.upper()}')
            text = ''
            for k, v in sets.items():
                new_friends_for_person = set(current_friends[name][k]) - set(v)
                new_friends_array = []
                if len(new_friends_for_person) > 0:
                    for i in range(0, len(new_friends_for_person), 50):
                        try:
                            users = api.lookup_users(user_ids=list(new_friends_for_person)[i: i + 50])
                            for u in users:
                                new_friends_array.append(u.screen_name)
                        except tweepy.error.TweepError as e:
                            logger.error(e)
                if len(new_friends_array) > 0:
                    text += f'{k} --> {new_friends_array}\n'

            logger.info(text)
            if name == 'test_s' or name == 'test_d':
                bot.send_message(chat_id=chat_id_test, text=text)
            else:
                bot.send_message(chat_id=chat_id_main, text=text)
        save_obj(current_friends, 'friends')
        logger.info('Update friends}')
        logger.info(f'Go to sleep, utcnow = {datetime.utcnow()}')
        time.sleep(300)
