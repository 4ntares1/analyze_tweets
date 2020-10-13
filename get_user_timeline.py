import json
from requests_oauthlib import OAuth1Session


class GetTwitterData:
    def __init__(self):
        Consumer_key = ''
        Consumer_secret = ''
        Access_token = ''
        Access_token_secret = ''

        self.twitter = OAuth1Session(Consumer_key, Consumer_secret,
                                     Access_token, Access_token_secret)

    def get_user_timeline(self, user_handle, count=10):
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        params = {'screen_name': user_handle, 'count': count}
        twitter = self.twitter
        res = twitter.get(url, params=params)

        user_timeline = json.loads(res.text)

        tweets_data = []
        for tweet in user_timeline:
            tweets_data.append(tweet['text'] + '\n')

        return tweets_data

    def get_user_name(self, user_handle):
        url = 'https://api.twitter.com/1.1/users/show.json'
        params = {'screen_name': user_handle}
        res = self.twitter.get(url, params=params)

        user_data = json.loads(res.text)

        return user_data['name']


def write_data(user_name, tweets_text):
    fname = user_name + '_user_timeline.txt'
    with open(fname, mode='w', encoding='utf-8') as f:
        f.write('\n'.join(tweets_text))


if __name__ == '__main__':
    print('Please enter twitter handle')
    user_handle = input('@').rstrip()
    user_handle = '@' + user_handle

    print('\nHow many data do you want to use?')
    count = int(input().rstrip())

    data = GetTwitterData()
    write_data(data.get_user_name(user_handle),
               data.get_user_timeline(user_handle, count))