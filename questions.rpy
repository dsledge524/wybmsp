# This script contains the questions used in this trivia game. 


# Defining questions:


init python:

    """
    A class for questions. 
    """
    class Question(object):

        """
        A constructor for a Question object. 
        @param question         a string containing the question
        @param a1               a string containing the first answer choice
        @param a2               a string containing the second answer choice
        @param a3               a string containing the third answer choice
        @param a4               a string containing the fourth answer choice
        @param correct          a string containing the same text for the correct answer choice
        @param point_value      an integer representing the question's point value (default is 1)
        """
        def __init__(self, question, a1, a2, a3, a4, correct, point_value = 1):
            self.question = question
            self.a1 = a1
            self.a2 = a2
            self.a3 = a3
            self.a4 = a4
            self.correct = correct
            self.point_value = point_value



# Instantiating Question objects:


# Don't forget to append these questions to question_list in question_list.rpy!


define q1 = Question(question = "2 + 2?",
                        a1 = "0",
                        a2 = "1",
                        a3 = "4",
                        a4 = "5",
                        correct = "4")


define q2 = Question(question = "12 / 4",
                        a1 = "3",
                        a2 = "6",
                        a3 = "4",
                        a4 = "O",
                        correct = "3")   


define q3 = Question(question = "Which of the following is NOT \na work by William Shakespeare?",
                        a1 = "Pyramus and Thisbe",
                        a2 = "Coriolanus",
                        a3 = "The Merry Wives of Windsor",
                        a4 = "Hamlet",
                        correct = "Pyramus and Thisbe")   


define q4 = Question(question = "In computer science and engineering, \nwhat does CPU stand for?",
                        a1 = "Computational Performance Utility",
                        a2 = "Creation Payload U-turn",
                        a3 = "C-type Pass Under",
                        a4 = "Central Processing Unit",
                        correct = "Central Processing Unit")   


define q5 = Question(question = "In Greek mythology, who was known for having \nwinged sandals?",
                        a1 = "Hermes",
                        a2 = "Apollo",
                        a3 = "Iris",
                        a4 = "Artemis",
                        correct = "Hermes")   


define q6 = Question(question = "What is the atomic number of oxygen?",
                        a1 = "16",
                        a2 = "7",
                        a3 = "8",
                        a4 = "10",
                        correct = "8")  


define q7 = Question(question = "In what literary location would you find \nHeathcliff and the Earnshaw family?",
                        a1 = "Wuthering Heights",
                        a2 = "221B Baker Street",
                        a3 = "Hundred Acre Wood",
                        a4 = "Prince Edward Island",
                        correct = "Wuthering Heights")  


define q8 = Question(question = "Capsaicin is primarily associated \nwith what sensation?",
                        a1 = "Sweetness",
                        a2 = "Creaminess",
                        a3 = "Stickiness",
                        a4 = "Spiciness",
                        correct = "Spiciness")  



# Don't forget to append these question objects to question_list in question_list.rpy!