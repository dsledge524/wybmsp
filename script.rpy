﻿# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the name of the character.
init python:       
    import random
    current_question_idx = 0  # Index of the current question
    user_score = 0  # Number of correct answers
    user_answer = 0
    question_data = None
    correct_answers = 0
    
    from random import shuffle

    def generate_question():
        # Define operation types (e.g., addition, subtraction, multiplication, division)
        operations = ["+", "-", "*", "/"]
        
        # Set difficulty range (e.g., numbers between 1 and 10)
        min_value = 1
        max_value = 10
        
        # Randomly choose two numbers and an operation
        num1 = random.randint(min_value, max_value)
        num2 = random.randint(min_value, max_value)
        operation = random.choice(operations)
        
        # Construct the question based on the chosen operation
        if operation == "+":
            question = "What is " + str(num1) + " + " + str(num2) + "?"
            answer = num1 + num2
        elif operation == "-":
            question = "What is " + str(num1) + " - " + str(num2) + "?"
            answer = num1 - num2
        elif operation == "*":
            question = "What is " + str(num1) + " * " + str(num2) + "?"
            answer = num1 * num2
        elif operation == "/":
            # Ensure whole number division
            while num1 % num2 != 0:
                num1 = random.randint(min_value, max_value)
                num2 = random.randint(min_value, max_value)
            question = "What is " + str(num1) + " / " + str(num2) + "?"
            answer = num1 // num2  # Integer division
        
        # Generate answer choices
        choices = [answer - 2, answer + 3, answer, answer + 1]

        #shuffle(choices)  # Shuffle the answer choices

        #global correct_answer
        correct_answer = answer
        

        
        # Return the question and shuffled answer choices as a dictionary
        question_data = {
            'question': question,
            'a1': str(choices[0]),
            'a2': str(choices[1]),
            'a3': str(choices[2]),
            'a4': str(choices[3]),
            'correct_answer': correct_answer
        }
        return question_data





screen q1_nav():
    add "blankStudy"
    modal True

    # Call the generate_question function and store its result in a variable
    python:
        question_data = generate_question()
  

    # Display the question
    text question_data["question"]:
        xpos 106
        ypos 800

    # Display answer choices using textbuttons
    textbutton question_data["a1"] xpos 540 ypos 1060 action Jump("wrong")
    textbutton question_data["a2"] xpos 540 ypos 1300 action Jump("wrong")
    textbutton question_data["a3"] xpos 540 ypos 1530 action Jump("correct")
    textbutton question_data["a4"] xpos 540 ypos 1760 action Jump("wrong")
    

    
            

label check_answer:
    #$ correct_answer
    if int(user_answer) == question_data[correct_answer]:
        $ user_score += 1
        jump correct
    else:
        jump wrong




#initializing images?
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
   
    call screen meet_nav


#Meeting lily
label lily:
    show lilymeet
    #convo bt u and lily no menu
    l "Oh, hello. I'm Lily. You're new right?"
    y "Yep, I'm [player_name]. This is my first day!"
    l "OMG! Welcome!"
    l "I'm actually president of the Math Club, you're totally welcome to join
    - or if you ever need Math help- I'm your gal!"
    y "Thanks! I'll keep that in mind"
    l "Well [player_name], it was nice to meet you. I gotta run to a club meeting, but I hope I see you around!"

    call screen meet_nav

#after clicking "i dont want to talk to anyone else" button
label postMeet:
    show hallway 
    n "Oop, there's the bell. Better hurry to class!"
    "*hours later*"
    n "Whew! You completed your lessons for the day, but it's clear that 
    you'll need to study hard to keep up with your classmates..."

    call screen study_nav
    
#Lily Character page where you can talk or study
label lilyCharacter:
    show lilyCharPage
    call screen character_nav
    #show lilyCharPage
    #show lilyCharPage
    #n "you made it here"
    #call screen character_nav
    #STILL NEED TO MAKE THIS SCREEN IN SCREENS outline down by other screens in screens.rpy


label lilyStudy:

    #hide lilyCharPage
    scene blankStudy
    #$ generate_question()
    
    call screen q1_nav
    



label correct:
    scene black
    $ correct_answers += 1
    n "Correct! Tap to continue"
    #n "You've answered [correct_answers] questions correct"
    if correct_answers % 5 == 0:
        jump endStudy
    else:
        jump lilyStudy
    

label wrong:
    scene black
    n "Wrong answer. Tap to continue"
    n "Your answer was [user_answer] The correct answer was [correct_answer]" 
    jump lilyStudy



label endStudy:
    l "You've answered [correct_answers] questions correctly! Would you like to continue?"
    pass
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
