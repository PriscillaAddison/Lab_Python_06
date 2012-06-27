"""class Player:
    def __init__(self,firstname,lastname,team = None):
        self.firstname = firstname
        self.lastname = lastname
        self.scores = [0,0,1,0,1]
        self.team = team

    def add_score(self,score):
        self.scores.append(score)
        
    def total_score(self):
        t=0
        for i in self.scores:
            t = t + i
        return t
        
    def average_score(self):

        return self.total_score()/float(len(self.scores))

soccer = Player('Torres','Fernando')
print soccer.lastname,soccer.firstname
print soccer.total_score()
print soccer.average_score()
"""
"""class Team:
    def __init__(self,name,league,manager_name,points):
        self.name = name
        self.league = league
        self.manager_name = manager_name
        self.points = points
        self.players = []

    def add_player(self,player):
        self.players.append(player)

    def __str__(self):
        i=''
        if i==spain:
            print 'Spanish Player:\n'
        elif i==portugal:
            print 'Portugese Player:\n'
        return 'Name of Player: '+self.name+'\nName of League: '+self.league+'\nManagers of manager:'+self.manager_name+'\nScored points:'+self.points+'\n'
spain = Team('Torres','Premier','Fiifi Boadu','26')
portugal = Team('Ronaldo','Champions','Gity Adu','49')

print spain
print portugal
spain.add_player('Torres')
portugal.add_player('Ronaldo')
print spain.players
"""
import datetime
class Match:
 
    def __init__(self,home_team,away_team,date):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.home_scores = {'Torres':5,'Gayooyo':7}
        self.away_scores = {'Fiifi':6,'Hans':9}
    
    def home_score(self):
        hs=0
        for i in self.home_scores.values():
            hs = hs + i
        if hs==0:
            return 0
        else:
            return hs
        
        
    def away_score(self):
        s=0
        for i in self.away_scores.values():
            s = s + i
        if s==0:
            return 0
        else:
            return s

    def winner(self):
        if self.home_score() > self.away_score():
            return 'winner is: ', self.home_team
        elif self.away_score() > self.home_score():
             return 'winner is: ', self.away_team        

match = Match('HOL','BH',(datetime.date(2012,6,21)))
print match.home_score()
print match.away_score()
print match.winner()






































