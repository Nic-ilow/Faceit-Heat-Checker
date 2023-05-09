import requests
from scripts.creds import headers

def elo_discrep(all_stats,p_team,p_elo):


    enemy_elo = 0

    teams = abs(p_team - 1)
    for i in range(len(all_stats['rounds'][0]['teams'][teams]['players'])):
        player = all_stats['rounds'][0]['teams'][teams]['players'][i]['player_id']
        player_details = requests.get('https://open.faceit.com/data/v4/players/{}'.format(player),
                                      headers=headers).json()
        enemy_elo += float(player_details['games']['csgo']['faceit_elo'])

    enemy_elo /= len(all_stats['rounds'][0]['teams'][teams]['players'])

    return (enemy_elo-p_elo)