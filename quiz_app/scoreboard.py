from .color import *
import pickle
import os

class Scoreboard(object):

    def __init__(self, username, score):
        self.create_scoreboard()
        self.scoreboard = self.load_scoreboard()
        self.username = username
        self.score = score
        self.save_score_to_file(username, score)
        self.show_scoreboard()

    def create_scoreboard(self):
        try:
            with open('scoreboard.pkl', 'rb') as f:
                file = pickle.load(f)
        except FileNotFoundError:
            scoreboard_file = 'scoreboard.pkl'
            open(scoreboard_file, 'x')
            

    def save_score_to_file(self, username, score):
        new_score = [username, score]
        with open('scoreboard.pkl','ab') as f:
            pickle.dump(new_score, f)
        self.scoreboard = self.load_scoreboard() # reloads the scoreboard

    def load_scoreboard(self):
        load_scoreboard = []
        with open('scoreboard.pkl', 'rb') as f:
            while True:
                try:
                    score = pickle.load(f)
                except EOFError:
                    break
                load_scoreboard.append(score)
            sorted_scoreboard = sorted(load_scoreboard, key = lambda x: x[1], reverse=True)
        return sorted_scoreboard

    def show_scoreboard(self):
        
        self.scoreboard = self.load_scoreboard()
        print('============ Scoreboard ============')
        for x, y in enumerate(self.scoreboard):
            name = self.scoreboard[x][0]
            score = self.scoreboard[x][1]
            a = print(str(x+1) + '.', color_green + 'Name:' + color_end, name, '|', color_red + 'Score:' + color_end, score)
        return a
    
