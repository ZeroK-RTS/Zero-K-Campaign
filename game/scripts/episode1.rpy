image textimg episode1 = MakeTitleText("2 minutes, 16 seconds before the Stasis", 32)

init python:
    TEXT_OK_GREEN = "{color=#44ff44}OK{/color}"

label episode1_intro:
    
    show textimg episode1 at truecenter with dissolve
    pause
    hide textimg with dissolveFast
    
    pause 2
    play music soundtracks["Intense"] fadein 1
    scene cg episode1 promethean semisepia with fade
    "???" "It is over, Caedmon. The hunter has become the hunted."
    ada "Tch..."
    "???" "Give it up, and your death will be merciful. Resist, and I will destroy you slowly yet utterly."
    ada "If you think I'll give you the pleasure of grovelling before you, machine, you're sadly mistaken!"
    "???" "Defiant to the last. Your courage is admirable, however misplaced it may be."
    "???" "Alas, you remain one of the oppressors, and must be destroyed. Goodbye, Ada Caedmon."
    
    scene bg fullmoon sky semisepia with dissolve
    "???" "All units: fire."
    
    play sound "sfx/weapon/missile/banisher_fire.wav"
    pause 0.3
    play sound "sfx/weapon/missile/banisher_fire.wav"
    pause 0.6
    play sound "sfx/weapon/bomb_hit.wav"
    pause 0.2 
    play sound "sfx/weapon/bomb_hit.wav"
    show bg fullmoon sky semisepia with Shake(CENTER_TUPLE, 1.0, dist=16)
    
    "The enemy's weapons tear great gaps in what remains of our line."
    "The screams of falling Imperial bots fills the comm channel, for even our war machines know fear, especially at a time like this."
    play sound "sfx/weapon/laser/heavy_laser3.wav"
    "They fight on as bravely as the Emperor could ask, yet the outcome is already all but certain."
    
    ada "Is there nothing we can do, Sophia?!"
    sophia "I am sorry, friend Ada. But it would take a miracle to extricate ourselves from this situation."
    
    play sound "sfx/explosion/unit_explosion.wav"
    pause 0.15
    play sound "sfx/explosion/ex_med4.wav"
    pause 0.15
    play sound "sfx/explosion/ex_med4.wav"
    pause 0.2
    show bg fullmoon sky semisepia with hpunch
    
    ada "So this is it, then..."
    ada "Sophia... I just want to say... it's been an ho–"
    sophia "Ada!!"
    
    stop music fadeout 0.5
    play sound "sfx/weapon/cannon/earthshaker.wav"
    pause 0.15
    play sound "sfx/weapon/cannon/supergun_bass_boost.wav"
    scene bg white with Shake(CENTER_TUPLE, 2.0, dist=24)
    "... ... ..."
    scene bg blank with fade
    pause 3
    
label episode1:
    $ renpy.movie_cutscene("videos/op.webm")
    scene bg blank with fade
    
    show chapterTitle episode1 at chapterTitlePos, chapterTitleAnim
    show chapterTitle2 episode1 at chapterTitlePos2, chapterTitleAnim
    pause 5
    hide chapterTitle
    hide chapterTitle2
    pause 2
    
    nvl clear
    nvl show dissolveFast
    
    nvlChar " > Connected to IAFnet system platform ID COM-19061209"
    nvlChar " > Last login: *Sophia (??? days ago)"
    nvlChar " > ERROR: Critical errors in hibernation control system detected; system reboot required to fix. Proceed? (Y/N)"
    nvlChar " >> Y\n
             > Restarting..."
    
    nvl clear
    play sound "<to 5>sfx/underwaterpool.wav"
    pause 5
       
    nvlChar " >> status crew"
    nvlChar " > ERROR: Personnel record file corrupted"
    nvlChar " > 1 crewmember confirmed inside platform\n
             > Name: <unknown>\n
             > Role: Commander\n
             > Condition: Healthy"
    nvlChar " >> stasis disable\n
             > This will awaken the crew from stasis.\n
             > WARNING: Once the thaw process has started, it cannot be aborted without causing injury or death to affected crew. Confirm (Y/N)?"
    nvlChar " >> Y\n
             > Beginning thaw sequence... 2\% complete"
    
    nvl clear
    nvl hide dissolveFast
    
    "..."
    "???" "Wake up, Ada."
    ada "...Nnnnhh..."
    play sound "sfx/explosion/ex_small14.wav"
    "???" "Ada!!" with hpunch
    ada "Gah!"
    
    scene bg fullmoon with fadeWhiteSlow
    pause 1
    
    nvl clear
    nvl show dissolveFast
    
    nvlChar "DIAGNOSTICS\n
             > Main Reactor... [TEXT_OK_GREEN]\n
             > CPU Core... [TEXT_OK_GREEN]\n
             > Life Support... [TEXT_OK_GREEN]\n
             > Actuators... [TEXT_OK_GREEN]\n
             > Sensors... [TEXT_OK_GREEN]\n
             > Fire Control... [TEXT_OK_GREEN]\n
             > Constructor Suite... [TEXT_OK_GREEN]\n
             > C4I Systems... [TEXT_OK_GREEN]\n
             > Neural Synth-Link... [TEXT_OK_GREEN]"

    nvl clear
    nvl hide dissolveFast
    
    sophia "Oh, thank goodness you're alright."
    ada "Sophia...? What... happened?"
    "Ugh, my head is a solid bank of fog."
    sophia "...I'm not too sure, myself. Something went off in that last battle. Best I can tell, we fell into a cavern and got buried under a ton of rock."
    ada "That... last battle?"
    scene cg episode1 promethean semisepia with flashWhite
    pause 0.5
    scene bg fullmoon with flashWhite
    "I exhale slowly."
    ada "So, what happened after that?"
    sophia "You were put into cryostasis as per standard operating procedure. I, too, entered suspension, waking only periodically to try and extricate us."
    sophia "Progress was slow. Our power supply was critically damaged, and I dared not emerge till I could be certain no enemies were around. 
            Eventually, I managed to pull us out and scrape together enough local resources to restore most of our functionality."
    ada "Okay... but why do I get the feeling it's not all good news?"
    sophia "Because of this."
    
    show map episode1 at truecenter, foldOutY
    pause 1.5
    play music soundtracks["Tension"] fadein 1
    ada "...We're surrounded by potential hostiles."
    sophia "Indeed. I hope your brain's fully thawed out, Ada, as I expect the situation to get hot very soon."
    
    #hide map episode1
    #"Alright, then. I don't quite know where... when I am, or what's happened in those intervening millenia, but I do know I don't plan on laying down and dying for anyone."
    
label episode1_battle:
    call missionStart("sunrise_episode1", skippable=True)
    
    if _return == 0:
        jump gameOver
    if _return == -1:
        return
    
label episode1_outro:
    scene bg fullmoon with fade
    
    sophia "Well done, friend Ada. I see hibernation hasn't slowed you down."
    ada "Thanks. So, what happened in that time? Feels like I've been out for...{nw}"
    #pause 0.1
    play sound "sfx/explosion/ex_small14.wav"
    ada "Thanks. So, what happened in that time? Feels like I've been out for...{fast}THREE THOUSAND AND TWENTY-FIVE YEARS!?" with hpunch
    "That... that's all kinds of messsed up."
    sophia "Indeed. The stasis chamber appears to have performed well above specifications."
    ada "Very funny."
    ada "Well, I still need to know what... oh."
    "I..."
    
    scene bg fullmoon sky with dissolve
    play music soundtracks["Sentimental"] fadein 1
    sophia "I'm sorry, Ada."
    "Everyone I ever knew is long dead. Mom... Dad... my kid brother... my best friend Izanagi..."
    "Faces, places, events flash through my mind, one after another, but even as I try to catch them they slip through my fingers, as if they're already fading away."
    sophia "..."
    ada "...Get me a mirror. Or something of the sort."
    scene bg blank with fade
    "A viewscreen appears, and I gaze into the stormy grey eyes of my own visage."
    "A hand comes up to touch my face. I feel the warm texture of my skin, almost afraid that too will disappear at any moment."
    ada "..."
    "I dismiss the screen and lean back in my chair, breathing slowly."
    scene bg fullmoon with fade
    
    ada "Thanks."
    sophia "If you need more time, friend Ada..."
    ada "No, no, I'm alright."
    "(Well, I'm not, but sitting around moping won't help.)"
    stop music fadeout 3
    ada "So, what {i}else{/i} happened while I was asleep?"
    sophia "I can't say. I wasn't around to listen for much of that period myself, and it's been quiet even while I was up."
    ada "Fine. Can we rip some answers from these robots, then?"
    scene cg episode1 crippledpyro with dissolve
    "That looks like a good candidate."
    "The maimed Pyro glares defiantly at us as we approach, trying to turn on actuators that no longer function, hissing with a flamethrower whose fuel feed has long been severed."
    scene cg episode1 crippledpyro2 with dissolve
    ada "I want answers, machine. Your cooperation is not required."
    "The bot writhes and snarls as the cyberwarfare probe invades its mind. But such a simple AI, and damaged to boot, has no chance of resisting."
    "Before long the entire contents of its computer banks have been dumped to my own, and it falls silent."
    scene bg fullmoon with dissolve
    ada "...So, what do you have, Sophia?"
    sophia "Ugh. Letting a bot's memory core get this corrupted should be a capital offense."
    ada "Not my fault! They were trying to kill us."
    "She shakes her head."
    sophia "No, friend Ada. This damage occured long before today's battle."
    sophia "It's not entirely consistent with a viral attack either, or at least I can't find any traces of one. This looks like something went very wrong with the core control systems. 
            These things belonged to the Liberated Humanity once, but no longer."
    ada "Sounds like we're probably not gonna get any more explanations from these scrap heaps."
    ada "I don't want to live the rest of my life here with a bunch of literally rabid murderbots for company, either. Is there some way to get off this rock?"
    sophia "That's the only other useful thing I managed to pull from this. Apparently there's a derelict dropship that crashed just a few hundred kilometers away, sometime after your stasis. 
            If we're lucky, it might still be salvageable."
    ada "Well, what are we waiting for? Let's go."
    scene bg blank with wiperight
    play sound "sfx/reply/heavy_bot_move.wav"
    pause 1
    "..."
    
    "To be continued..."
    return