from Imports import *

match_id = '1-0fb9bd77-fbf8-4a65-92e5-be9666fb1039'

# Get current matchrooms player info
all_p_ids, all_g_ids, all_nicks, configured_time = lobby_info(match_id)


avg_kd = []
avg_kr = []
session_performance = []
lobby_ses_dat = []

for idx in range(len(all_p_ids)):
    p_id = all_p_ids[idx]
    g_id = all_g_ids[idx]
    nick = all_nicks[idx]

    ses_dat = session(p_id, nick, configured_time)
    lobby_ses_dat.append(ses_dat)

columns = ['K/D', 'K/R', '# Matches', '# Wins', 'Performance']
lobby_ses_dat = np.array(lobby_ses_dat)
data = pd.DataFrame(data=lobby_ses_dat, index=all_nicks, columns=columns)