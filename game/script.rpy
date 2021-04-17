# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Arianna")
define m = Character("Matteo")

# The game starts here.

label start:

    "{i}Matteo and me met through mutual friends."
    "{i}I've met several times before but never alone, so one day he invited me out together for a drink."


    scene bg room

    "{i}It's so loud here, I hope it was the right decision to come to the club tonight."
    "{i}There are so many people... I wonder how I can find Matteo among them."
    "{i}I should be at home, finishing the project that is due Monday. And yet here I am, looking for a person I have never met alone before."
    "{i}I hope we will find some topics to talk about. Oh god, I am nervous, where is Matteo?"

    show matteo happy

    m "Hi Arianna!" 
    a "Oh hey Matteo, it's good to see you"
    m "You too! How are you?"
    a "I am good, what about you?"
    m "Very good, now that I found you. Let's go to the bar, I need a drink"
    a "Ok"

    scene bg bar

    show matteo happy

    m "I am getting a Mojito, what about you?"
    a "I really don't like alcohol very much"
    m "Don't worry a Mojito doesn't really taste like alcohol. You will see that you will like it a lot. This place has the best Mojito's in town!"

    menu:
        "I guess one will be fine...":
            jump mojito_yes

        "No, I really shouldn't drink":
            jump mojito_no

    label mojito_yes:
    "{i}I am not sure if I should drink, I usually don't respond well to alcohol."
    "{i}But I guess the drink will make me feel more confident and less shy"
    a "Ok, let's try"
    m "Two mojitos please!"
    jump dance

    label mojito_no:
    m "Two mojitos please!"
    "{i}Oh well, now he already bought me one so I guess I should drink it. I don't want to be rude."
    jump dance

    label dance:
    a "Thanks for the drink, you were right, it was actually good!"
    m "I told you so. By the way, you look great tonight, I like your dress"
    a "Oh, thank you"
    m "Let's go dance!"

    scene bg room

    show matteo happy

    m "This is fun"
    a "Yes, I love that song"
    a "I am thirsty, I really need some water after all this dancing"
    m "Sure, let's get another drink"
    a "Haha, no I will just get a cold glass of water"
    m "C'mon, let's get another mojito!"
    "{i}I do really like Matteo and I don't want to disappoint him, but should I get another drink?"

    menu:
        "Yes, one last drink":
            jump second_drink_yes

        "No, I have to work tomorrow!":
            jump second_drink_no

    label second_drink_yes:
    a "Alright let’s get another drink. Just one more though!"
    m "Great! Two more mojitos here!"
    scene bg night road
    show matteo happy
    m "You know it's getting so crowded in here. Do you feel like going to my house for a little while?"
    a "Ok, but only for a little bit, because I have work early in the morning."
    jump matteo_house
    
    label second_drink_no:
    a "No thank you Matteo, I have work early tomorrow. I had a good evening but I am getting tired."
    scene bg night road
    show matteo happy
    m "Alright, let's get out of here. Do you feel like going to my house for a little while?"
    a "Ok, but only for a little while."
    jump matteo_house

    label matteo_house:
        "{i}work in progress"

    return
