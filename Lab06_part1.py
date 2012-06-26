"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure
import datetime
player_stats={'rooney':(datetime.date(2012,6,23),2),
              'rooney':(datetime.date(2012,6,25),2),
              'ronaldo':(datetime.date(2012,6,19),0),
              'ronaldo':(datetime.date(2012,6,20),3),
              'torres':(datetime.date(2012,6,21),0),
              'torres':(datetime.date(2012,6,21),1)}
print player_stats
   
## implement highest_score
def highest_score(player_stats):
             for i in player_stats():
                 n=0
                 if n>2:
                     print n
    



## implement highest_score_for_player



## implement highest_scorer






































