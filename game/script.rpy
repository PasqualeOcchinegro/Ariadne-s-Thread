# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Arianna")
define m = Character("Matteo")
define k = Character("Kim")

# The game starts here.

label start:

    "{i}Matteo and me met through mutual friends."
    "{i}I've met several times before but never alone, so one day he invited me out together for a drink."

    scene bg disco club

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

    scene bg lounge bar

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

    scene bg disco club

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

    scene bg matteos house

    a "I like your house! It feels really cozy in here"

    show matteo happy

    m "Thanks, please make you feel at home. I will make us another Mojito. What music can I play for you?"
    a "I will choose something from all your vinyls."
    a "This one is a classic. The smiths, great I will play that one"
    m "Here you go, cheers!"
    a "Cheers!"
    m "You are very beautiful and I had an amazing evening with you. May I kiss you."
    "{i}We kissed."
    m "Arianna, I want to be with you. Please stay here for the night."
    "{i}I do like Matteo and I don't want to say no because what if he will lose interest in me."

    menu:
        "Stay for the night":
            jump stay_yes

        "Don't stay":
            jump stay_no


    label stay_yes:

    a "Alright I will stay here for the night."
    "{i}I slept with him. We started dating"
    jump ariannas_house


    label stay_no:

    a "I will go home tonight. We just met Matteo, I do like you but I need to get to know you better first."

    show matteo sad

    m "Oh come on! We know each other very well. But ok, I will take you home now"
    a "Thank you"
    jump mountain_cabin


    label ariannas_house:

    scene bg ariannas house

    show matteo happy

    m "I like being with you a lot! I can't stand it not beeing with you."
    a "Oh Matteo, that's so cute."
    m "I would love to have you, even when we are not together. What if we make a video of us together?"
    a "I don't know, that is a bit weird. What if you show it to someone else?"
    m "I would never do that. Don't you trust me?"
    a "I do, but can you promise?"
    m "Yes, I promise you. The video is just between you and me!"
    "{i}I am not sure if I should say yes. I don't want to end up naked on the internet. It just doesn't feel right, but I don't want to disappoint Matteo."

    menu:
        "Ok, let's make the video":
            jump video_yes

        "Don't make the video":
            jump video_no


    label video_yes:
    
    scene bg black

    "{i}A few days have passed since then. I have been busy with work and wasn't able to meet Matteo."
    "{i}I was working on a project for the company when i got a call."

    scene bg office

    a "Hi Matteo, is everything fine?"
    m "Hey, why can't you find time to meet me. I am your boyfriend! I want to see you."
    a "I am so sorry, but we are working on this project at work that is due next week."
    a "Also, I am at work right now so I can't really talk to you but I promise to call back tonight!"
    "{i}I closed the call and returned on my work, when a friend of mine, Kim, sent me a message."
    k "Hi Arianna, I was with Jon and he showed me a video from a group chat."
    k "I'm sorry, I don't really know how to tell you this, but it's you sleeping with Matteo in the video."
    k "I thought you should know. I am always here to talk xxx"
    "{i}I called Matteo back instantly"
    a "HOW COULD YOU???? YOU PROMISED ME YOU WOULDN'T SHOW OUR LITTLE VIDEO TO ANYONE"
    m "Well, its my video after all, I took it so I can do anything I want with it."
    a "You liar, you promised me not to show it to anyone!"
    m "But I didn't see you for days. I am annoyed with you."
    "{i}I started crying hangs up with phone."
    "{i}I hated him. I didn't know how could he do that to me."
    "{i}I decided that I didn't want to see Matteo ever again."

    scene bg black

    "{i}But during the following days I was constantly showered with messages from an apologizing Matteo and flowers found on my office desk."
    "{i}He said he was a fool and that he lost his mind only because he couldn't be with me."
    "{i}After the yet another flower bouquet at my office my co-workers told me that i should forgive him, give him another chance, but they don't know what he did to me..."
    "{i}Matteo has been cute sending me so many text messages and presents. But can I forgive hime for what he has done to me?"
    "{i}Kim told me to report him to the police and get help in the Anti-violence center. Maybe I should consider that."

    menu:
        "Give Matteo another chance":
            jump last_chance_yes

        "Report Matteo to the police":
            jump last_chance_no

    label video_no:
    jump mountain_cabin

    label mountain_cabin:

    scene bg black

    "{i}The next day I recieved a message from Matteo"
    m "Hi, I am sorry for being rude yesterday night. I was just sad that you already wanted to go home."
    m "I wanted to spend more time with you because I like you a lot. Please lets meet again very soon."
    "{i}Thats's so sweet of him to apologize. I really like Matteo as well. I think I'll call him and ask if we can meet tonight again."
    "{i}Time has passed since then, and now we are in a relationship." 
    "{i}We even decided to pass the easter holidays in the mountains alone."

    scene bg cabin 

    show matteo happy

    m "Good morning my princess"
    a "Good morning"
    m "It was so nice to have you just by myself last night."
    a "Haha, yes, but don't get used to it!"

    show matteo angry 

    m "What do you mean?? Why are you laughing about that. You are mine! Does it make you laugh that I want you only for myself?"
    "{i}What's going on, why is Matteo so possessive. I really don't think this is a healthy relationship."

    menu:
        "Tell Matteo his behaviour is too possessive":
            jump last_chance_yes

        "Matteo is a little bit possessive but it's cute that he loves me so much":
            jump last_chance_yes

    label last_chance_no:
    
    scene bg black

    "Sharing an intimate video is unacceptable. Maybe I should listen to Kim and go to the Police to report Matteo. But that would be embarrassing... I am not sure what to do."
    "A few weeks later. Arianna is still in the relationship with Matteo, even though the relationship doesn't make her feel good. She struggels to get out of the relationship."
    "What you have seen in this game is an example of stalking and abusive relationships. In many cases, violence in abusive relationships follows a predictable cycle."
    jump END


    label last_chance_yes:

    scene bg black
    
    "{i}Matteo and I have been in a relationship for two months now. We see each other nearly every day."

    scene bg bar

    "{i}One afternoon I was hanging out with some friends when he called me."
    m "Arianna, where are you?? I am at your house but you are not home."
    a "I am at a Bar with my co-workers. They texted me a few hours ago and we wanted to celebrate the project we completed. I am sorry I didn't tell you..."
    m "What, why are you with them? You should be spending your time with me instead. We are in a relationship, you only need me in your life"
    a "But why can't I just spend one evening with my friends?"
    m "Because I love you and I want you to show me that you love me too. Please, make me happy and just hang out with me."
    "{i}Maybe Matteo is right, I should be with him. I am neglecting him"

    scene bg black

    "{i}One year after Matteo and I started dating, I moved in to Matteos house."

    scene bg matteos house 

    "{i}I really don't feel like it is the right decision to move in with Matteo already, but he asked me every day and I just couldn't say no any longer."
    "{i}Since I moved in Matteo has been controling every step I take. He is even listening to my phone calls. Every time I call a friend, he gets angry with me."
    "{i}I don't dare to call them anymore because he gets so mad. The only place where I am still free is my mind."
    "{i}One evening Matteo came home from work while i was on my phone."

    show matteo angry

    m "No, hang up your phone call, now! I am home now, i had a long day at work and the dinner is not ready??"
    a "But I was at work as well and I just came home."
    m "I told you to stop working. You have to keep up with the house work. I can't believe that dinner isn't even ready yet."
    a "How am I supposed to handle work and household at the same time? And I love my job."
    "{i}Matteo slapped me and left the house slamming the door."
    "{i}I made him so mad again. I am really scared. Maybe I should try the anti-violence center that Kim recommended." 
    "{i}But maybe it will all be fine and Matteo will never do it again. What should I do?"

    menu:
        "Go to the anti-violence center":
            jump anti_violence_yes

        "Stay in Matteo's House":
            jump anti_violence_no
    

    label anti_violence_yes:
    
    scene bg black 

    "{i}I started attending an anti-violence center and since then i've become aware that I had a toxic relationship with Matteo."
    "What you have seen in this game is an example of stalking and violent relationships."
    jump END


    label anti_violence_no:
    
    scene bg black

    "{i}I sat down and started crying"
    "{i}Our relationship continued and the violent attacks repeated themselves every now and then."
    "{i}After the attacks Matteo is always apologizing and very kind towards me."
    "{i}He also takes me on some trips to the sea and the mountains but then he starts beeing violent again."
    "{i}The relationship doesn't make me feel good, but I struggle to get out of it."
    "What you have seen in this game is an example of stalking and abusive relationships. In many cases, violence in abusive relationships follows a predictable cycle."
    jump END


    label END:
    "The “cycle of violence” consists of three phases that repeat themselves constantly.
    The first is the tension building phase. In this phase, the relationship starts of being fine but then tension begins to build up.
    The second stage is the actual explosion phase where the physical abuse occurs.
    The last phase is called the honeymoon phase. In this phase of the cycle of violence, the abuser shows kind and loving behavior towards the victim."

    return
