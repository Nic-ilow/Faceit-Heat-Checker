def team_info(match_id):
    import numpy as np
    from Lobby import lobby_info
    from Session_Stats import session
    all_p_ids, all_g_ids, all_nicks, configured_time = lobby_info(match_id)

    lobby_ses_dat = []

    for idx in range(len(all_p_ids)):
        p_id = all_p_ids[idx]
        nick = all_nicks[idx]

        ses_dat = session(p_id, nick, configured_time)
        lobby_ses_dat.append(ses_dat)


    lobby_ses_dat = np.array(lobby_ses_dat)
    '''
    #Deprecated
    t1_kd = np.mean(lobby_ses_dat[:5,0])
    t2_kd = np.mean(lobby_ses_dat[5:,0])
    t1_kr = np.mean(lobby_ses_dat[:5,1])
    t2_kr = np.mean(lobby_ses_dat[5:,1])
    t1_perf = np.mean(lobby_ses_dat[:5,3])
    t2_perf = np.mean(lobby_ses_dat[5:,3])
    '''

    return lobby_ses_dat
