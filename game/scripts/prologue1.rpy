image textimg prologue1 = MakeTitleText("29 days, 13 hours before the Stasis")

label prologue1_intro:
    $ renpy.movie_cutscene("videos/op.webm")
    scene bg blank with fade
    
    show chapterTitle prologue1 at chapterTitlePos, chapterTitleAnim
    show chapterTitle2 prologue1 at chapterTitlePos2, chapterTitleAnim
    pause 5
    hide chapterTitle
    hide chapterTitle2
    pause 2
    
    "The tenth Planetwars."
    "The tenth of a series of conflicts in which leaders unleashed great armies of robots upon the galaxy, tearing it asunder in the name of ideology, justice or power."
    "One of them, the Empire Reborn, came to dominate the galaxy at the end of the last war, and spread its hegemony throughout the stars."
    "But the Imperial golden age has come and gone. Now turmoil and dissension saps its strength from within, and the Empire's many enemies pour over its borders in a flood, sweeping all before them."
    "Now, the crisis is coming to a head..."
    
    show textimg prologue1 at truecenter with dissolve
    pause
    hide textimg with dissolveFast
    
    play music soundtracks["Evacuation (Action)"]
    scene bg fieldsofisis with fade
    
    imperial "Rebel units approaching! Range 700!"
    ada "Tch... I was hoping we'd have a little more time."
    
    play sound "sfx/weapon/cannon/cannon_fire5.wav"
    pause 0.15
    play sound "sfx/weapon/cannon/cannon_fire5.wav"
    pause 0.4
    play sound "sfx/weapon/cannon/cannon_fire5.wav"
    pause 0.15
    play sound "sfx/weapon/cannon/cannon_fire5.wav"
    pause 0.5
    play sound "sfx/explosion/ex_med4.wav"
    pause 0.15 
    play sound "sfx/explosion/ex_med4.wav"
    show bg fieldsofisis with Shake(CENTER_TUPLE, 1.0, dist=16)
    pause 1
    
    scene cg prologue1 rebelvehicles with dissolve
    play sound "sfx/reply/vehicle_move.wav"
    "The rebel army surges upon the loyalist position guarding the pass in a wave of steel."
    #play sound "sfx/weapon/laser/heavy_laser3.wav"
    "The defenders are well-entrenched, and they fight valiantly, even desperately. But their enemies seem without limit."
    "Armored vehicles press on through a hail of energy fire, grinding the corpses of friend and foe alike beneath their wheels."
    "Their war chant broadcasts on all channels."
    rebels "DEATH TO THE FALSE EMPEROR\nDEATH TO THE FALSE EMPEROR\nDEATH TO THE FALSE EMPEROR"
    
    play sound "sfx/explosion/ex_small14.wav"
    ada "You're the ones serving the false Emperor!!" with hpunch
    sophia "You know they can't hear you, right?"
    
    scene cg prologue1 ada with dissolve
    "My name is Ada Eveline Caedmon. Captain, 13th Imperial Auxiliary Cohort."
    "For years I've served the Emperor of Earth, battling rebels, invaders and pretenders in his name."
    "Now I've come to this barren land with my trusted AI aide Sophia, in the hope of buying a little more time for the defenders of the Throne world to prepare for the final onslaught."
    #"There may not be an empire for me to serve much longer, but until that moment comes to pass, I will stand and fight!"
    
    scene bg fieldsofisis with dissolve
    play sound "sfx/explosion/ex_med4.wav"
    show bg fieldsofisis with Shake(CENTER_TUPLE, 1.0, dist=16)
    
    ada "Damn. There's millions of them."
    sophia "Enemy artillery is thirteen clicks out. The situation will soon become untenable."
    ada "Reinforcements?"
    sophia "None can arrive till we've been shelled for at least three minutes. And given the situation on the rest of the front, none may arrive at all. We should withdraw while we can."
    ada "I don't like the idea of cutting and running while someone else dies to cover my retreat."
    sophia "How do you feel about both you and them dying, friend Ada?"
    "That's Sophia for you. She's nice and really helpful, but at times she can be a real smartass without even trying."
    ada "Ugh... Fine. Transport, prepare for a hot extraction."
    
    scene cg prologue1 transport1 with dissolve
    imperial "Copy that. Transport is– Mud spike! Enemy SAM detected!"
    play sound "sfx/weapon/missile/missile_fire3.wav"
    scene cg prologue1 transport2 with dissolve
    pause 0.5
    play sound "sfx/weapon/missile/missile_fire3.wav"
    pause 0.5
    scene bg fieldsofisis sky with dissolve
    pause 0.5
    play sound "sfx/explosion/ex_med6.wav"
    show bg fieldsofisis sky with vpunch        #Shake(CENTER_TUPLE, 1.0, dist=16)
    
    sophia "It seems we are surrounded, friend Ada. I can only assume the 11th cohort has been broken."
    ada "Wonderful. I don't suppose you have another way out of here?"
    sophia "We do have a second transport. There's still time; we need to fight out way through the flanking forces and get to the secondary extraction point."
    
    scene cg prologue1 ada with dissolve
    ada "All right, then. Come and get me, you usurping dogs!"
    
    call missionStart("sunrise_prologue1", True)
    
    if _return == 0:
        jump gameOver
    if _return == -1:
        return
    
    play music soundtracks["Inspiring"]
    scene cg prologue1 transport3 with Fade(1, 0, 1)
    ada "Alright, let's get out of here!"
    sophia "We'll head for Fort Hathor. Let our efforts have bought them time enough to stop the rebels here."
    
    stop music fadeout 1
    call chapterEnd
    
    "Until next time..."
    scene bg blank with fade
    
    return