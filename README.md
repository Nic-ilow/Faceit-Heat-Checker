A set of python scripts to evaluate Faceit player performance in their recent gaming session (within 6 hours of a match room being created). This works on past games as well as games that have just been configured. To use this you must manually edit the match_id in the Main file to correspond to the match id that you want to look at.

Your lobbies match id is the string at the end of the lobby url. e.g.
lobby url: csgo/room/1-1074f5cf-16e4-42f9-9a3a-07b79c9c32b0
match id: 1-1074f5cf-16e4-42f9-9a3a-07b79c9c32b0

From there you can run the script, it will take anywhere up to 1 minute, and the data file will be an Pandas Dataframe containing K/D, K/R, Matches, Wins, Performance, in that order. If Matches is -1 it means the player has not played any matches within the last 6 hours. As a result I apply average players statistics to them, i.e. K/D=1, K/R=0.72, Performance=1