def stat_finder(history, nick):
    import requests
    from creds import headers
    from Elo_Discrep import elo_discrep
    from Performance_Calc import Performance
    import numpy as np

    tot_k = 0
    tot_d = 0
    tot_kr = 0
    k = 0
    d = 0
    kr = 0
    kd = 0
    perf_score = []
    p_team = 0
    p_elo = 0
    num_recent_matches = len(history['items'])
    num_wins = 0
    for match_num in range(num_recent_matches):
        match_id = history['items'][match_num]['match_id']
        all_stats = requests.get('https://open.faceit.com/data/v4/matches/{}/stats'.format(match_id),
                                 headers=headers).json()

        team1_id = history['items'][match_num]['teams']['faction1']['team_id']
        if all_stats['rounds'][0]['teams'][0]['team_id'] == team1_id:
            teams = [0, 1]
        else:
            teams = [1, 0]




        for team in teams:

            for i in range(len(all_stats['rounds'][0]['teams'][team]['players'])):

                if nick == all_stats['rounds'][0]['teams'][team]['players'][i]['nickname']:

                    k = float(all_stats['rounds'][0]['teams'][team]['players'][i]['player_stats']['Kills'])
                    d = float(all_stats['rounds'][0]['teams'][team]['players'][i]['player_stats']['Deaths'])
                    if d == 0:
                        d = 1
                    kd = k / d
                    kr = float(all_stats['rounds'][0]['teams'][team]['players'][i]['player_stats']['K/R Ratio'])
                    p_team = int(team)
                    num_wins += int(all_stats['rounds'][0]['teams'][0]['team_stats']['Team Win'])

                    if match_num == 0:
                        player = all_stats['rounds'][0]['teams'][team]['players'][i]['player_id']
                        player_details = requests.get('https://open.faceit.com/data/v4/players/{}'.format(player),
                                                      headers=headers).json()
                        p_elo = float(player_details['games']['csgo']['faceit_elo'])

        discrep = elo_discrep(all_stats, p_team, p_elo)

        tot_k += k
        tot_d += d
        tot_kr += kr

        perf_score.append(Performance(kd, kr, discrep))

    if tot_d == 0:
        tot_d = 1

    if num_recent_matches == 0:
        num_recent_matches = -1
        tot_kr = 0.72
        tot_kd = 1
        perf_score = 1
    else:
        tot_kr /= num_recent_matches
        perf_score = np.mean(perf_score)
        tot_kd = tot_k / tot_d

    return [tot_kd, tot_kr, num_recent_matches, num_wins,  perf_score]
