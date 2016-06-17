image textimg episode1 = MakeTitleText("2 minutes, 16 seconds before the Stasis", 32)

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
    nvlChar " > Last login: *Sophia on 29 Dec 3722 (1,111,425 days ago)"
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
    
    "To be continued..."