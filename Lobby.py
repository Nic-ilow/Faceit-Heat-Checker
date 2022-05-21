def lobby_info(match_id):
    import requests
    from creds import headers

    current_match = requests.get('https://open.faceit.com/data/v4/matches/{}'.format(match_id), headers=headers).json()
    start_time = current_match['configured_at']
    team_1_nicks = []
    team_1_ids = []
    team_1_game_ids = []
    for i in range(5):
        team_1_nicks.append(current_match['teams']['faction1']['roster'][i]['nickname'])
        team_1_game_ids.append(current_match['teams']['faction1']['roster'][i]['game_player_id'])
        team_1_ids.append(current_match['teams']['faction1']['roster'][i]['player_id'])

    team_2_nicks = []
    team_2_game_ids = []
    team_2_ids = []
    for i in range(5):
        team_2_nicks.append(current_match['teams']['faction2']['roster'][i]['nickname'])
        team_2_game_ids.append(current_match['teams']['faction2']['roster'][i]['game_player_id'])
        team_2_ids.append(current_match['teams']['faction2']['roster'][i]['player_id'])

    all_p_ids = team_1_ids + team_2_ids
    all_g_ids = team_1_game_ids + team_2_game_ids
    all_nicks = team_1_nicks + team_2_nicks

    return all_p_ids, all_g_ids, all_nicks, start_time