**Main:**

A set of python scripts to evaluate Faceit player performance in their recent gaming session (within 6 hours of a match room being created). This works on past games as well as games that have just been configured. 


**How to use:**

To use this you must manually edit the match_id in the Main file to correspond to the match id that you want to look at. Your lobbies match id is the string at the end of the lobby url. e.g.

lobby url: csgo/room/1-1074f5cf-16e4-42f9-9a3a-07b79c9c32b0

match id: 1-1074f5cf-16e4-42f9-9a3a-07b79c9c32b0


**What you get out of it:**

The data variable will be an Pandas Dataframe containing *K/D*, *K/R*, *Matches*, *Wins*, *Performance*, in that order. 

If Matches is -1 it means the player has not played any matches within the last 6 hours. As a result I apply average players statistics to them, i.e. K/D=1, K/R=0.72, Performance=1


**Data Folder:**

Here I have inclduing an .ipynb file that consisted of me attempting to make use of machine learning and statistics from 1000 Faceit CSGO games to predict the outcome of a game based on the players within each team. The data files are included as well, there are 2 sets, those ending with *2* include the individual statistics of each player within each game, whereas the others include mean statistics of each team only.


**Conclusion**

My conclusion from this project is that *INDIVIDUAL STATS DON'T MATTER*. CSGO is a heavily team based game, and your kills and deaths alone are not a strong indicator of team success, even making use of elo discrepancy does not help.

Ultimately it's still fun to look at stats, and see if you're fragging and how well you're doing today, and if it's against generally better players or not.