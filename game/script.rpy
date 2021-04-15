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

    "{i}It's so loud here, I hope it was the right decision to come to the club tonight"
    "{i}and there are so many people here. I wonder how I can find Matteo between all these people..."
    "{i}I should be at home, finishing the project that is due Monday. And yet here I am, looking for a person I have never met alone before"
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
    a "I would like to order two Mojitos please!"

    "{i}I am not sure if I should drink, I usually don't respond well to alcohol"
    "{i}But Matteo already paid for my drink so it would be rude to not drink it"
    "{i}I guess the drink will make me feel more confident and less shy"

    m "Arianna, you look very good, I like your dress"
    a "Oh, thank you"
    m "Let's go dance!"


    scene bg room

    a "Matteo, I am thirsty, I really need some water after all this dancing"

    show matteo happy

    m "Sure, let's get another drink"
    a "Haha, no I will just get a cold glass of water"
    m "No no, let's get another Mojito"

    "{i}I do really like Matteo and don't want to disappoint him, should I get another drink with him?"
    "{i}But I do have work to do and need to get up early tomorrow so should I say no and go home?"

    a "Alright let’s get another drink."


    scene bg night road

    a "Thank you for tonight Matteo. I had a good time but I have to go home now"
    
    show matteo happy

    m "It was wonderful tonight, what if you come to my house for a while? I want to stay with you a little more"

    "{i}I really need to go home now, but at the same time i want to be with him a little longer..."
    "{i}What should i do?"

    menu:
        "Accept and go with him":
            jump choice_1

        "Refuse and go home":
            jump choice_2

    label choice_1:
        a "Ok, why not"
        m "Wonderful! I'll go take the car, wait here!"
        jump done_1

    label choice_2:
        a "Sorry, but it's too late and tomorrow i need to wake up early"
        m "C'mon! just for a while! I'll go take the car, you think about it"
        jump done_1
    
    label done_1
     "{1}Work In Progress"

    return
