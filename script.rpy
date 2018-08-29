# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("")
define r = Character("You")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # These display lines of dialogue.

    r "Wh-...Where am I?"
    
    scene bg horror
    
    with Dissolve (2)
    
    r "What is this place? It looks like an hallway..."
    
    show main
    
    with Dissolve (1.5)
    
    r "AAAHHH!! What the fuck!"

    e "Hello there, dear reader. May I introduce you to the Project Eternal Nightmare?"
    
    r " Wh-...What is an eternal nightmare????"
    
    e " It's a nightmare with no end. You can't escape or wake up from this nightmare."
    
    r "A-..And why am I here?"
    
    e "We chose 10 People from all around the globe in order to test this project. You are just very,very lucky."
    
    hide main
    
    with Dissolve (3)
    
    r "Oh god. I still wonder what this place is. It looks like an hallway built in an Hospital. Maybe I will find some thing when i walk down this hallway. He said there are 
       10 people, so 9 other should be here."
    
    e "As i walk down the Hallway, I hear weird noises. They seem to come from a romm on the other end of the hallway. I decide to look what is causing those noises. 
       As i get nearer i can hear, what this noise is. It's something like a chainsaw."
    
    e "I finally see the door and gently open it a bit. I just took a quick look but was unable to see anything."
    
    e "I decided to fully open the door."
    
    scene bg horror 2
    
    with Dissolve (1.5)
    
    r "O-..Oh God. What the hell is this?"
    
    scene bg horror
    
    with dissolve (0.5)
    
    e "I instanly slammed the door but i still has to vomit. I just lay there for 2 more minutes crying and thinking, what this could be."
    
    r "I-... I think i understand the Project now. It just shows you things, which are usually seen in nightmares. Bu-..But why this? WHYYYY???" 
       
    
    
   
       
    # This ends the game.

    return
