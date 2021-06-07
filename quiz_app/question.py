import numpy as np
from .scoreboard import Scoreboard
from .color import *

class Question(object):
    def __init__(self, questions, question_limit):
        self.questions = questions
        self.question_limit = question_limit
        self.startQuiz()
    
    def startQuiz(self):
        print("Welcome to our quiz app!")
        #print("Please select one of the following numbers in order to continue:")
        print("Please enter your name:")

        self.user_name = input()

        print("Greetings, " + font_bold + color_header + self.user_name + color_end + "!")
        print("Now we're going to start our quiz.\nGood luck!")
        print("===============================================")

        self.mainQuiz(self.questions)

    def mainQuiz(self, questions):
        
        self.question_count = 0
        self.correct_answer_count = 0

        np.random.shuffle(questions)

        
        for x, y in enumerate(questions):
            question = questions[x][0]
            answer_a = questions[x][1]
            answer_b = questions[x][2]
            answer_c = questions[x][3]
            answer_d = questions[x][4]
            answer_correct = questions[x][5]
            explanation = questions[x][6]
            if x == self.question_limit:
                break
            
            print(font_bold + color_header + str(x+1) + ". " + question + color_end)
            print(color_red + ' ', answer_a + color_end)
            print(color_blue + ' ', answer_b + color_end)
            print(color_yellow + ' ', answer_c + color_end)
            print(color_green2 + ' ', answer_d + color_end)

            self.question_count += 1

            user_answer = input('Enter your answer: ')
            
            self.validate_answer(user_answer, answer_correct, explanation)

            print("===============================================")    

        self.post_game_rating(self.correct_answer_count)    

        

    def validate_answer(self, user_answer, answer_correct, explanation):
            if user_answer.upper() == answer_correct.upper():
                print(color_green + "Correct!" + color_end)
                self.correct_answer_count += 1
                print(color_green + font_bold +  explanation + color_end)
            else:
                print(color_red + "Wrong!" + color_end)
                print(color_red + font_bold +  explanation + color_end)

            

    def post_game_rating(self, correct_answer_count):
        score_rating = self.correct_answer_count / self.question_count * 100 

        print("Score:", int(score_rating))
        if score_rating < 50:
            print("Better luck next time, " + font_bold + color_header + self.user_name + color_end + "!")
        elif score_rating == 100:
            print("Perfect! 10/10")
        else:
            print("Good job!")

        print("You answered " + str(correct_answer_count) + " questions out of " + str(self.question_count) + " correctly.")
        
        x = input('Would you like to save your score? (Yes/No)\n')
        if x.upper() == 'YES':
            Scoreboard(self.user_name, int(score_rating))
    
            


   
        