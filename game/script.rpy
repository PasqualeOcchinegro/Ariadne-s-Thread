# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Arianna", color="#AB77FF")
define m = Character("Matteo", color="229FB5")
define k = Character("Kim", color="#F2DD6E")
define ah = Character("Arianna (to herself)", color="#AB77FF")

# The game starts here.

label start:
    play music "audio//vntrack.mp3" volume 0.1
    "{i}Matteo and Arianna met through mutual friends."
    "{i}They've met several times before but never alone, so one day he invited her out for a drink."
    scene bg disco club
    ah "It's so loud here, I hope it was the right decision to come to the club tonight."
    ah "There are so many people... I wonder how I can find Matteo among them."
    ah "...I should be at home, finishing the project that is due Monday. And yet here I am, looking for a person I have never met alone before."
    ah "I hope we will find some topics to talk about. Oh god, I am nervous, where is Matteo?"
    show matteo happy
    m "Hi Arianna!" 
    a "Oh! Matteo! It's good to see you!"
    m "You too! How are you?"
    a "I am fine, thanks, what about you?"
    m "Very good, now that I found you. Let's go to the bar, I need a drink."
    a "Sure!"
    scene bg lounge bar
    show matteo happy
    m "I am getting a Mojito, what about you?"
    a "Actually I don't like alcohol very much."
    m "Don't worry! A Mojito doesn't really taste like alcohol. You will see that you will like it a lot. This place has the best Mojito's in town!"
    
    menu:
        "Accept the drink":
            jump mojito_yes

        "Refuse the offer":
            jump mojito_no


    label mojito_yes:
    ah "I am not sure if I should drink, I usually don't respond well to alcohol."
    ah "But I guess the drink will make me feel more confident and less shy."
    a "Ok, let's try!"
    m "Two mojitos please!"
    jump dance

    
    label mojito_no:
    m "Two mojitos please!"
    ah "Oh, he already bought me one, I guess I should drink it. I don't want to be rude."
    jump dance

    
    label dance:
    a "Thanks for the drink, you were right, it was actually good!"
    m "Told you. By the way, you look great tonight, your dress is lovely!"
    a "Oh, thank you"
    m "Let's go dance, shall we?"
    scene bg disco club
    show matteo happy
    m "I'm having so much fun with you tonight!"
    a "Me too, I love that song!"
    a "But now I'm quite thirsty, I really need some water after all this dancing."
    m "Sure, let's get another drink!"
    a "Haha, no I will just get a cold glass of water."
    m "C'mon, let's get another mojito!"
    ah "The first drink was fine, and I don't want to disappoint Matteo, but I'm not sure if i should get another drink."
    
    menu:
        "Drink another mojito":
            jump second_drink_yes

        "Turn down the second drink":
            jump second_drink_no

    
    label second_drink_yes:
    a "Alright let’s get another drink. Just one more though!"
    m "Great! Two more mojitos here!"
    scene bg night road
    show matteo happy
    m "You know, it's getting so crowded in here. Do you feel like going to my house for a little while?"
    a "Ok, but only for a little bit, I need to wake up early tomorrow."
    m "Great! I'll go take the car then."
    jump matteo_house
    
    
    label second_drink_no:
    a "No thank you Matteo, I have work early tomorrow. I had a good evening but I am getting tired."
    scene bg night road
    show matteo happy
    m "Alright, let's get out of here. Do you feel like going to my house for a little while?"
    a "Ok, but only for a little while."
    m "Nice!"
    jump matteo_house

    
    label matteo_house:
    scene bg matteos house
    a "I like your house! It feels really cozy in here"
    show matteo happy
    m "Thanks, please make you feel at home. I will make us another Mojito."
    m "Want to put up some music meanwhile?"
    a "Sure! I will choose something from your vinyls."
    a "Oh, The Smiths! This one is a classic. I'll go for this one."
    m "Here you go, cheers!"
    a "Cheers!"
    m "You are very beautiful, and I had an amazing evening with you."
    "{i}They kissed."
    m "Arianna, I want to be with you. Please stay here for the night."
    ah "That was sudden, but I can't say I don't like him too..."
    ah "what should I do?"
    
    menu:
        "Stay with him for the night":
            jump stay_yes

        "Go home":
            jump stay_no

    
    label stay_yes:
    "{i}They kissed again."
    scene bg black
    "{i}After that night Arianna and Matteo started dating."
    "{i}One night, they met at Arianna's house."
    jump ariannas_house


    label stay_no:
    a "Sorry, I will go home tonight. We just met Matteo, I do like you but I need to get to know you better first."
    show matteo angry
    m "Oh come on! We know each other very well. But ok, I will take you home if that's what you want."
    a "Thank you."
    scene bg black
    "{i}The next day she received a message from Matteo."
    scene bg smartphone
    m "Hi, I am sorry for being rude yesterday night. I was just sad that you already wanted to go home."
    m "I wanted to spend more time with you because I like you a lot. Please let's meet again very soon."
    ah "Thats's so sweet of him to apologize. He really is an handsome guy."
    ah "I think I'll call him and ask if we can meet tonight again."
    jump mountain_cabin


    label ariannas_house:
    scene bg ariannas house
    show matteo happy
    m "When I'm with you i feel in heaven! I can't stand not beeing with you."
    a "Oh Matteo, that's so cute."
    m "I would love to see you, even when we are not together. What if we make a video of us?"
    a "I don't know, that's a bit weird. What if you show it to someone else?"
    m "I would never do that. Don't you trust me?"
    a "I do, but can you promise?"
    m "Yes, I promise you. The video is just between you and me!"
    ah "I am not sure if I should say yes. I don't want to end up naked on the internet."
    ah "It just doesn't feel right, but I don't want to disappoint Matteo."
    
    menu:
        "Accept the proposal":
            jump video_yes

        "Don't make the video":
            jump video_no


    label video_yes:
    scene bg black
    "{i}A few days have passed since then. Arianna had been busy with work and she wasn't able to meet Matteo."
    "{i}One day, she was working on a project for the company when she got a call."
    scene bg office
    a "Hi Matteo, is everything fine?"
    m "Hey, why can't you find time to meet me. I am your boyfriend! I want to see you."
    a "I am so sorry, but we are working on this project at work that is due next week."
    a "Also, I am at work right now so I can't really talk to you but I promise to call back tonight!"
    "{i}She closed the call and returned to her work, when a friend of her, Kim, sent her a message."
    k "Hi Arianna, I was with John and he showed me a video from a group chat."
    k "I'm sorry, I don't really know how to tell you this, but it's you sleeping with Matteo in the video."
    k "I thought you should know. I am always here to talk if you want xx"
    "{i}She instantly called Matteo back"
    a "HOW COULD YOU???? YOU PROMISED ME YOU WOULDN'T SHOW OUR VIDEO TO ANYONE"
    m "Well, its my video after all, I took it so I can do anything I want with it."
    a "You liar, you promised me not to show it to anyone!"
    m "But I didn't see you for days. This behaviour of yours is annoying. I just did what i felt was right."
    "{i}As she put down her phone she started crying."
    ah "I hate him. How could he do that to me?"
    ah "I don't want to see Matteo ever again."
    scene bg flowers
    "{i}During the following days she was constantly showered with apologizing messages from Matteo."
    "{i}Every morning a new bouquet of flowers was left on her office desk."
    "{i}He said he was a fool and that he was losing his mind because he couldn't be with her."
    "{i}After yet another flower bouquet at her office her co-workers started telling her that she should forgive him, give him another chance."
    ah "I understand what they are thinking, but they don't know what he did to me..."
    ah "Still, Matteo has been sweet sending me so many text messages and presents." 
    ah "Am I a bad person for not forgiving him?"
    ah "Kim told me to report him to the postal police and get help in the Anti-violence center. Maybe I should consider that."
    
    menu:
        "Think about it for a few days":
            jump last_chance_yes

        "Report Matteo to the postal police":
            jump last_chance_no


    label video_no:
    a "Sorry, I'm still uncertain about it, it's not about you, but i really don't feel confident in doing that."
    show matteo angry
    m "Ok, never mind, forget I even asked that."
    scene bg black
    "{i}The next day she received a message from Matteo."
    scene bg smartphone
    m "Hi, I am sorry for being rude yesterday night. I was just sad that I couldn't always stay with you."
    m "I wanted to spend more time with you because I like you a lot. Please let's meet again very soon."
    ah "Thats's so sweet of him to apologize. He really is an handsome guy."
    ah "I think I'll call him and ask if we can meet tonight again."
    jump mountain_cabin


    label mountain_cabin:
    scene bg black
    "{i}Time has passed since then. They started dating" 
    "{i}They decided to pass the Easter holidays in the mountains alone."
    scene bg cabin 
    show matteo happy
    m "Good morning my princess!"
    a "Good morning!"
    m "It was so nice to have you just for myself last night."
    a "Haha, yes, but don't get used to it!"
    show matteo angry 
    m "What do you mean? Why are you laughing about that. You are mine! Does it make you laugh that I want you only for myself?"
    ah "What's going on, why is Matteo acting like this?"
    ah "Thinking about it, this is not the first time he behaves completely different from what I'm used to."
    ah "Maybe is just a phase, this is just the way he shows his affection to me."
    ah "I'm torn... What should I do?"

    menu:
        "Start considering breaking up with him":
            jump mountain_ending_no

        "Stay with him":
            jump mountain_ending_yes


    label mountain_ending_no:
    ah "He's becoming more and more oppressive, I don't know if I should break with him."
    ah "The thing is, I'm actually quite scared, for now I'll endure until the end of this trip."
    scene bg black
    "{i}The holiday eventually came to an end but Arianna didn't find the courage to break up with Matteo."
    "{i}She thought that maybe she was the one at fault, and indulging Matteo would change the things between them."
    jump last_chance_yes

    label mountain_ending_yes:
    ah "His behaviour is really strange, but he is so sweet to be caring about me!"
    scene bg black
    "{i}The holiday eventually came to an end, with Arianna and Matteo closer then ever."
    jump last_chance_yes


    label last_chance_no:
    scene bg black
    ah "Sharing an intimate video is unacceptable. Maybe I should listen to Kim and report Matteo to the postal police."
    ah "But that would be embarrassing... I am not sure what to do."
    "{i}A few weeks passed. Arianna is still in a relationship with Matteo."
    "{i}And even though his behaviour grew to be more and more violent and oppressive she struggles to get out of it."
    jump END


    label last_chance_yes:
    scene bg black
    "{i}Matteo and Arianna have been in a relationship for two months now. They see each other nearly every day."
    scene bg bar
    "{i}One afternoon she was hanging out with some friends when he called her."
    m "Arianna, where are you? I am at your house but you are not home."
    a "I am in a bar with my co-workers. They texted me a few hours ago and we wanted to celebrate the project we completed. I am sorry I didn't tell you..."
    m "What, why are you with them? You should be spending your time with me instead. We are in a relationship, you only need me in your life."
    a "But why can't I just spend one evening with my friends?"
    m "Because I love you and I want you to show me that you love me too. Please, make me happy and just hang out with me."
    ah "...Maybe Matteo is right. I am neglecting him."
    scene bg black
    "{i}One year after Matteo and Arianna started dating, she moved into Matteo's house."
    scene bg matteos house 
    ah "I really didn't feel like it was the right decision to move in with Matteo so soon."
    ah "But he asked me every day and I just couldn't say no any longer."
    "{i}Since she moved in, Matteo has been controlling every her step."
    "{i}He listened to her phone calls, and became aggressive every time she called a friend."
    "{i}She didn't dare calling them anymore when he was near, fearing his reaction."
    "{i}One evening Matteo came home from work while Arianna was on her phone."
    show matteo angry
    m "Hang up your phone call, now! I am home now, I had a long day at work and the dinner is not ready?"
    a "But I was at work as well and I just came home."
    m "I told you to stop working. You have to keep up with the house work. I can't believe that dinner isn't ready yet."
    a "How am I supposed to handle work and household at the same time? And I love my job."
    "{i}He slapped her."
    "{i}Then he left the house slamming the door."
    ah "I made him so mad again... I am really scared. Maybe I should try the anti-violence center that Kim recommended." 
    ah "But maybe it will all be fine and Matteo will never do it again. What should I do?"

    menu:
        "Go to the anti-violence center":
            jump anti_violence_yes

        "Stay in Matteo's House":
            jump anti_violence_no
    

    label anti_violence_yes:
    scene bg black 
    "{i}She started visiting regularly an anti-violence center and since then she became aware that she had a toxic relationship with Matteo."
    jump END


    label anti_violence_no:
    scene bg black
    "{i}She sat down and started crying"
    "{i}Their relationship continued and the violent attacks repeated themselves every now and then."
    "{i}After the attacks Matteo is always apologizing and kind towards her."
    "{i}Sometimes he took her on some trips to the sea and the mountains but inevitably he would show his violent side again and again."
    "{i}The relationship didn't make Arianna feel good, but she struggled to get out of it."
    jump END


    label END:
    scene bg black
    "What you have seen in this game is an example of stalking and abusive relationships."
    "In many cases, violence in abusive relationships follows a predictable cycle."
    scene bg cycle
    "The “Cycle of Violence” developed by Lenore E. Walker consists of three phases that repeat themselves constantly."
    "The first is the tension building phase. In this phase, the relationship starts of being fine but then tension begins to build up."
    "The second stage is the actual explosion phase where the physical abuse occurs."
    "The last phase is called the honeymoon phase. In this phase of the cycle of violence, the abuser shows kind and loving behavior towards the victim."
    "Are you or someone you care about in an abusive relationship? Learn about domestic abuse in the following links."
    "www.netyx.it is a website created by health and social care professionals that offers information and guidance for people dealing with complicated or difficult relationships."
    "{a=http://stannefuori.it/}StanneFuori{/a} is an italian website that provides help in cases of domestic violence and abuse and explains how to deal with a violent situation."
    "Thank you for playing."

    return
