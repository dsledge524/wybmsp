# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the name of the character.
init python:       
    import random
    current_question_idx = 0  # Index of the current question
    correct_answers = 0  # Number of correct answers
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
        #division BUT need to figure how to do only whole number division
        #elif operation == "/":
            #question = "What is " + str(num1) + " / " + str(num2) + "?"
            #    answer = num1 / num2
            # ... (similar logic for multiplication and division)
        # else:
        # Handle division by zero case (optional)
            # return generate_question()  # Re-generate if division by zero
        # Return the question and answer as a dictionary
        questionText = question
        return {
            'question': str(questionText),
            'a1': str(answer - 2),  # Incorrect answer (distractor)
            'a2': str(answer + 3),  # Incorrect answer (distractor)
            'a3': str(answer),       # Correct answer
            'a4': str(answer + 1)  # Incorrect answer (distractor)
        }

    def process_answer(player_response):
        global correct_answers  # Access global variable
        current_question = generate_question()  # Generate a new question
        if player_response == current_question["correct"]:
        #play sound ding
            n: "Correct! You got it right!"
            correct_answers += 1
        else:
        #play sound wrong
            n: "That's incorrect. The answer was " + current_question["correct"] + "."
#initializing images?
init:
    image lilymeetbutton = "lilymeetbutton.png"
    image lilyStudyButton = "lilyStudyButton.png"
    image doneMeet = "doneMeet.png"
    image lilyCharPage = "lilyCharPage.png"
    image blankStudy = "blankStudy.png"
   
$ import question_list

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
    #show lilymeet
    n "YOU ARE AT LILY STUDY PAGE"
    #n "Alright, let's test your math skills!"
     

    # this is where I want the questions to start 
    #$ questionData = generate_question()
    #n "[questionData[question]]"








label endStudy:
    # generate questions $ n: "You answered " + str(correct_answers) + " questions correctly!"
    # ... (rest of your endStudy label code)

return

#this was the stuff i was trying to use rand for questions


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

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
        #        import random
        #        current_question_idx = 0  # Index of the current question
        #        correct_answers = 0  # Number of correct answers
        #        def generate_question():
                    # Define operation types (e.g., addition, subtraction, multiplication, division)
        #            operations = ["+", "-", "*", "/"]
                    # Set difficulty range (e.g., numbers between 1 and 10)
        #            min_value = 1
        #            max_value = 10
                    # Randomly choose two numbers and an operation
        #            num1 = random.randint(min_value, max_value)
        #            num2 = random.randint(min_value, max_value)
        #            operation = random.choice(operations)
                    
                    # Construct the question based on the chosen operation
        #            if operation == "+":
        #                question = "What is " + str(num1) + " + " + str(num2) + "?"
        #                answer = num1 + num2
        #            elif operation == "-":
        #                question = "What is " + str(num1) + " - " + str(num2) + "?"
        #                answer = num1 - num2
        #            elif operation == "*":
        #                question = "What is " + str(num1) + " * " + str(num2) + "?"
        #                answer = num1 * num2
                    #division BUT need to figure how to do only whole number division
                    #elif operation == "/":
                    #    question = "What is " + str(num1) + " / " + str(num2) + "?"
                    #    answer = num1 / num2
                    # ... (similar logic for multiplication and division)
        #            else:
                        # Handle division by zero case (optional)
        #                return generate_question()  # Re-generate if division by zero
                    # Return the question and answer as a dictionary
        #            return {
        #                "question": question,
        #                "a1": str(answer - 2),  # Incorrect answer (distractor)
        #                "a2": str(answer + 3),  # Incorrect answer (distractor)
        #                "a3": str(answer),       # Correct answer
        #                "a4": str(answer + 1),  # Incorrect answer (distractor)
        #            }

        #        def process_answer(player_response):
        #            global correct_answers  # Access global variable
        #            current_question = generate_question()  # Generate a new question
        #            if player_response == current_question["correct"]:
        #                #play sound ding
        #                n: "Correct! You got it right!"
        #                correct_answers += 1
        #            else:
        #                #play sound wrong
        #                n: "That's incorrect. The answer was " + current_question["correct"] + "."
