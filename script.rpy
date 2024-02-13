# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the name of the character.
init:
    image lilymeetbutton = "lilymeetbutton.png"
    image doneMeet = "doneMeet.png"




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
    show lily meet

    l "Oh, hello. I'm Lily. You're new right?"

    y "Yep, this is my first day!"
    l "OMG! Welcome!"
    l "I hope your first day is going well! What class are you most excited for?"
    menu:
        "English":
            pass
        "Math":
            pass
            #jump("lilyhappy")
        "Umm...none?":
            pass




label postMeet:
    pass
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

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
