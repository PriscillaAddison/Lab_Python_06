class Player:
    def __init__(self,firstname,lastname,team = None):
        self.firstname = firstname
        self.lastname = lastname
        self.scores = [5,2,10]
        self.team = team

    def add_score(self,score):
        self.scores.append(score)
        
    def total_score(self):
        t=0
        for i in self.scores:
            t = t + i
        print t

    def average_score(self):
        self.average_score


soccer = Player('twumwa','jasper','hhjh')
soccer.total_scores
