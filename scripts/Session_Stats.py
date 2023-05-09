import requests
from scripts.creds import headers
from scripts.stat_finder import stat_finder

def session(p_id, nick, configured_time):

    parameters = {'game': 'csgo', 'from': int(configured_time-(60*60*6)), 'to': int(configured_time)}
    history = requests.get('https://open.faceit.com/data/v4/players/{}/history'.format(p_id),
                           params=parameters,
                           headers=headers).json()

    stats = stat_finder(history, nick)

    return stats
