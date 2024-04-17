# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the name of the character.
init python:       
    import random
    from typing import List, Tuple
    #current_question_idx = 0  # Index of the current question
    user_score = 0  # Number of correct answers
    user_index = None
    correct_index = None
    #question_data = dict
    correct_answers = 0
    from random import shuffle
    current_question_index = 0
    question_data : Tuple[str, List[int], int]
    question_data = ("", [], 0)

    # questions = [
    #     {
    #         'question': "What is 2 + 2?",
    #         'choices': [3, 4, 5, 6],
    #         'correct_index': 1  # Index of the correct answer in the choices list
    #     },
    #     {
    #         'question': "What is 5 - 3?",
    #         'choices': [1, 2, 3, 4],
    #         'correct_index': 1
    #     },
    #     {
    #         'question': "What is 3 * 4?",
    #         'choices': [9, 10, 11, 12],
    #         'correct_index': 3
    #     },
    #     {
    #         'question': "What is 10 / 2?",
    #         'choices': [2, 3, 4, 5],
    #         'correct_index': 3
    #     },
    #     # Add more questions here as needed
    # ]


    questions = [
        ("What is 2 + 2?", [3, 4, 5, 6], 1),  # Tuple format: (question, choices, correct_index)
        ("What is 5 - 3?", [1, 2, 3, 4], 1),
        ("What is 3 * 4?", [9, 10, 11, 12], 3),
        ("What is 10 / 2?", [2, 3, 4, 5], 3),
        # Add more questions here as needed
    ]


# screen that displays the questions and answers
screen q1_nav():
    add "blankStudy"
    modal True
    python:
        question_data = random.choice(questions)
        question = question_data[0]
        choices = question_data[1]
        correct_index = question_data[2]
        
# Display the question
    text question:
        xpos 106
        ypos 800
    imagebutton idle "backButton":
        action Jump("endStudy")

    textbutton str(choices[0]) xpos 540 ypos 1060 action SetVariable("user_index", 0) , SetVariable("correct_index", question_data[2]) , Jump("check_answer")
    textbutton str(choices[1]) xpos 540 ypos 1290 action SetVariable("user_index", 1) , SetVariable("correct_index", question_data[2]) ,Jump("check_answer")
    textbutton str(choices[2]) xpos 540 ypos 1520 action SetVariable("user_index", 2) , SetVariable("correct_index", question_data[2]) ,Jump("check_answer")
    textbutton str(choices[3]) xpos 540 ypos 1750 action SetVariable("user_index", 3) , SetVariable("correct_index", question_data[2]) ,Jump("check_answer")
    
    
    # python:
    #     if user_index == correct_index:
    #         Jump("correct")
    #     else:
    #         Jump("wrong")
    # # Display answer choices using textbuttons
#     textbutton str(question_data["choices"][0]) xpos 540 ypos 1060 action SetVariable("user_index", 0), Jump("check_answer")
#     textbutton str(question_data["choices"][1]) xpos 540 ypos 1300 action SetVariable("user_index", 1), Jump("check_answer")
#     textbutton str(question_data["choices"][2]) xpos 540 ypos 1530 action SetVariable("user_index", 2), Jump("check_answer")
#     textbutton str(question_data["choices"][3]) xpos 540 ypos 1760 action SetVariable("user_index", 3), Jump("check_answer")
        

label check_answer:
    $ check = correct_index
    if user_index == check:
        $ user_score += 1
        jump correct
    else:
        l "[user_index] and [check]" 
        jump wrong


    #$ current_question_index += 1 


#initializing images
init:
    image lilymeetbutton = "lilymeetbutton.png"
    image lilyStudyButton = "lilyStudyButton.png"
    image doneMeet = "doneMeet.png"
    image lilyCharPage = "lilyCharPage.png"
    image blankStudy = "blankStudy.png"
    image userAnswer1 = "userAnswer1.png"
    image userAnswer2 = "userAnswer2.png"
    image userAnswer3 = "userAnswer3.png"
    image userAnswer4 = "userAnswer4.png"
    image lilywrongpage = "lilywrongpage.png"
    image lilycorrectpage = "lilycorrectpage.png"
    image hallway = "Hallway.png"
    image backButton = "backButton.png"
    image pinkBG = "pinkBG.png"
    image takeBack = "noTakeMeBackButton.png"
    image studyMore = "yesStudyMoreButton.png"

#declaring and defining characters
define l = Character("Lily")
define n = Character("narrator")
define y = Character("you")


# The game starts here.

label start:
    #name chooser thing
    $ quick_menu = False
    $ player_name = ""
    show screen enterName 
    scene bg cloud
    $ _preferences.afm_enable = False #turn off auto
    $ ui.interact() #we are using this to stop the the game, but unfortunately skip and auto will ignore this so that's why we disabled skip and auto

#now we create the label continue to jump here after we decide the name
label continue:
    $ player_name = player_name.strip() #removes spaces at the end

    if player_name == "":
        $ player_name="Josh" #will be used if player types nothing

    hide screen enterName

    $ quick_menu = True
    $ _skipping = True

    #show screen say(n, player_name)
    scene bg school

    "Hello [player_name]. Welcome to Pointcrest Academy!"
    "You're joining the class late, so you'll need to study extra hard to keep up with your peers."

    "Before your lesson starts, you mill about the common space and see many new faces."
     
    call screen meet_character


#Meeting lily
label lily:
    show lilymeet1:
        ypos .2
    #convo bt u and lily no menu
    l "Oh, hello. I'm Lily. You're new right?"
    y "Yep, I'm [player_name]. This is my first day!"
    l "OMG! Welcome!"
    l "I'm actually president of the Math Club, you're totally welcome to join
    - or if you ever need Math help- I'm your gal!"
    y "Thanks! I'll keep that in mind"
    l "Well [player_name], it was nice to meet you. I gotta run to a club meeting, but I hope I see you around!"
    
    call screen meet_character

#after clicking "i dont want to talk to anyone else" button
label postMeet:
    show hallway 
    n "Oop, there's the bell. Better hurry to class!"
    "*hours later*"
    n "Whew! You completed your lessons for the day, but it's clear that 
    you'll need to study hard to keep up with your classmates..."

    #call screen study_nav
    jump study_character

label study_character:
    call screen study_nav
    
#Lily Character page where you can talk or study
label lilyCharacter:
    show lilyCharPage
    call screen character_nav

label lilyStudy:
    #hide lilyCharPage
    scene blankStudy
    #$ generate_question()
    
    call screen q1_nav
    


label correct:
    scene lilycorrectpage
    $ correct_answers += 1
    l "Correct! Tap to continue"
    #n "You've answered [correct_answers] questions correct"
    if correct_answers % 5 == 0:
        jump endStudy
    else:
        jump lilyStudy
    

label wrong:
    scene lilywrongpage
    l "Wrong answer. Tap to continue"
    #n "Your answer was [user_answer] The correct answer was [correct_answer]" 
    jump lilyStudy

screen endStudy:
    modal True

    text "You've answered [correct_answers] questions correctly! Would you like to continue?"
    
    imagebutton idle "studyMore":
        action Jump("lilyStudy")

    imagebutton idle "takeBack":
        action Call("study_character")



label endStudy:
    scene pinkBG
    call screen endStudy
    # generate questions $ n: "You answered " + str(correct_answers) + " questions correctly!"
    # ... (rest of your endStudy label code)

return



# return
            #l "I hope your first day is going well! What class are you most excited for?"
            #menu:
            #    "English":
            #        pass
            #    "Math":
            #        pass
                    #jump("lilyhappy")
            #    "Umm...none?":
            #        pass
        #       python:
        #        
# this is the function that generates questions
    # def generate_question():
    #     # Define operation types (e.g., addition, subtraction, multiplication, division)
    #     operations = ["+", "-", "*", "/"]
        
    #     # Set difficulty range (e.g., numbers between 1 and 10)
    #     min_value = 1
    #     max_value = 10
        
    #     # Randomly choose two numbers and an operation
    #     num1 = random.randint(min_value, max_value)
    #     num2 = random.randint(min_value, max_value)
    #     operation = random.choice(operations)
        
    #     # Construct the question based on the chosen operation
    #     if operation == "+":
    #         question = "What is " + str(num1) + " + " + str(num2) + "?"
    #         answer = num1 + num2
    #     elif operation == "-":
    #         question = "What is " + str(num1) + " - " + str(num2) + "?"
    #         answer = num1 - num2
    #     elif operation == "*":
    #         question = "What is " + str(num1) + " * " + str(num2) + "?"
    #         answer = num1 * num2
    #     elif operation == "/":
    #         # Ensure whole number division
    #         while num1 % num2 != 0:
    #             num1 = random.randint(min_value, max_value)
    #             num2 = random.randint(min_value, max_value)
    #         question = "What is " + str(num1) + " / " + str(num2) + "?"
    #         answer = num1 // num2  # Integer division
        
    #     # Generate list of answer choices
    #     choices = [answer - 2, answer + 3, answer, answer + 1]
    #     random.shuffle(choices)

    #     correct_index = choices.index(answer)


        
    #     # Return the question and shuffled answer choices as a dictionary
    #     question_data = {
    #         'question': question,
    #         'choices': choices,
    #         'correct_index': correct_index
    #     }
    #     return question_data