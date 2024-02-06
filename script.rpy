# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the name of the character.

define e = Character("Eric")
define n = Character("narrator")

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

    show screen say(n, player_name)
    scene bg cloud
    #n "Hi [player_name]."

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

#label continue:
#    $ player_name = player_name.strip() #removes spaces at the end
#
#    if player_name == "":
#        $ player_name="Josh" #will be used if player types nothing
##
#    hide screen enterName
#
#    $ quick_menu = True
#    $ _skipping = True

    #show screen say(n, player_name)
    #scene bg school

#    "Hello [player_name]. Welcome to Pointcrest Academy!"
#    "You’re joining the class late, so you’ll need to study extra hard to keep up with your peers."
#    "Before your lesson starts, you mill about the common space and see many new faces.  "

#    scene bg hallway

#    menu:
#        "Who do you approach?"
#
#        "Eric":
#            jump eric
#
#        "Lily":
#            jump lily

#label eric:
#    show eric meet

#    e "Oh, hello. I'm Eric. You're new right?"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # This ends the game.

#    return
