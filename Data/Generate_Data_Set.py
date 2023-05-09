import requests
from scripts.creds import headers
import numpy as np

match_ids = []
outcomes = [] # 0 means team 1 wins, 1 means team 2 wins
start_time = []

start_id = '1-d71dc4bf-dfc2-4c07-979b-22581d04ce73'
current_match = start_id
match_count = 0
doofus_count = 0
while len(match_ids) < 1e3:
    match_count += 1
    match_details = requests.get('https://open.faceit.com/data/v4/matches/{}'.format(current_match),
                             headers=headers).json()

    match_ids.append(current_match)
    start_time.append(match_details['started_at'])

    winner = match_details['results']['winner']
    if winner == 'faction1':
        outcomes.append(0)
    else:
        outcomes.append(1)


    ###  GETTING A NEW MATCH TO GATHER DATA FROM
    counter = 0
    while current_match in match_ids:
        player_choice = np.random.randint(10)
        if player_choice < 5:
            p_id = match_details['teams']['faction1']['roster'][player_choice]['player_id']
        else:
            p_id = match_details['teams']['faction2']['roster'][player_choice%5]['player_id']

        p_history = requests.get('https://open.faceit.com/data/v4/players/{}/history'.format(p_id),
                     headers=headers).json()

        comp_name = '2v2'
        comp_type = 'championship'
        num_players = 1
        while comp_name[:3] == '2v2'\
                or comp_name[:3].lower() == 'ser' or\
                comp_type == 'championship' or\
                comp_type == 'quick_match' or\
                num_players != 5:
            match_num = np.random.randint(len(p_history['items']))
            current_match = p_history['items'][match_num]['match_id']
            comp_name = p_history['items'][match_num]['competition_name']
            comp_type = p_history['items'][match_num]['competition_type']
            num_players = len(p_history['items'][match_num]['teams']['faction1'])
        if counter>0:
            print(counter)
        counter += 1

    print('We have gathered data from ', match_count, 'matches')

