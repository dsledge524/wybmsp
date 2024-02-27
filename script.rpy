# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the name of the character.

#initializing images?
init:
    image lilymeetbutton = "lilymeetbutton.png"
    image lilyStudyButton = "lilyStudyButton.png"
    image doneMeet = "doneMeet.png"
    image lilyCharPage = "lilyCharPage.png"

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
    show bg school

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
    show lilyCharPage
    #show lilyCharPage
    #n "you made it here"
    #call screen character_nav
    #STILL NEED TO MAKE THIS SCREEN IN SCREENS outline down by other screens in screens.rpy

label lilyStudy:
    hide lilyCharPage
    show bg hallway
    show lilymeet
    n "YOU ARE AT LILY STUDY PAGE"
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # This ends the game.

    return



#label start:
#    #name chooser thing
#    $ quick_menu = False
#    $ player_name = ""
#    show screen enterName 
#    scene bg cloud
#    $ _preferences.afm_enable = False #turn off auto
#    $ ui.interact() #we are using this to stop the the game, but unfortunately skip and auto will ignore this so that's why we disabled skip and auto

    #now we create the label continue to jump here after we decide the name
#    return



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # This ends the game.

#    return
    #l "I hope your first day is going well! What class are you most excited for?"
    #menu:
    #    "English":
    #        pass
    #    "Math":
    #        pass
            #jump("lilyhappy")
    #    "Umm...none?":
    #        pass

