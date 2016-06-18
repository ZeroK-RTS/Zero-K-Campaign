image textimg prologue2 = MakeTitleText("19 days, 9 hours before the Stasis", 32)

label prologue2_intro:
    # TODO: scenery
    play music soundtracks["March"]
    scene cg prologue2 desertbase with fade
    "Fort Hathor. One of the second-to-last defense nodes of the Empire short of the Throne world itself."
    "Even this adjunct node bustles like an overturned ant nest. Construction bots scramble to shore up the defenses, while AFVs assemble into battlegroups to meet the enemy head-on."
    ada "Home sweet home. Looks like everyone's busy."
    ada "Now we just need to go find the Colonel and see how we can make ourselves useful."
    play sound "sfx/explosion/ex_small14.wav"
    "???" "CAEDMON!!" with hpunch
    "I just about jump out of my skin at the booming voice. Ugh... at least with the direct neural feed my eardrums aren't physically hurt... though I'll probably get a migraine if this keeps up."
    scene cg prologue2 desertbase2 with dissolve
    ada "Yes, Colonel?"
    imperialColonel "What do you think you're doing back here, eh? Desertion, cowardice in the face of the enemy... If we weren't so shorthanded, I'd have you executed on the spot!"
    sophia "The position was lost, Colonel. Failing to withdraw would only have resulted in the destruction of a critical command unit."
    imperialColonel "SILENCE! Who permitted you to speak, AI?"
    "Ugh, not this again. Aethelred's one of those goddamn Trueborns who've been calling the shots in the Empire ever since Saktoth the Great's reign. 
     Which means that nothing a mere toaster – or a mutant like me – could have any possible value for him."
    "It might be tolerable if he was actually any good at his job, even if only for a baseline. As it is, me and Sophia could easily outmaneuver him in our sleep."
    "Unfortunately, even if I was allowed to tell him what I really think of his pompous buffoonery, we don't have time for this right now."
    ada "I apologize, Colonel. Please allow me to redeem myself in service of the Emperor."
    imperialColonel "Hmph. What use could I possibly find for one such as you?" 
    imperialColonel "...Still, the outpost in sector 13, 2 requires an FARP. See to it at once."
    ada "Aye, aye, sir!"
    imperialColonel "And I need not remind you that further cowardice will not be tolerated. Understood, captain?"
    ada "Yes, sir."
    "I give the face on my display a picture-perfect salute. He snorts, and says nothing more before cutting the connection."
    scene cg prologue2 desertbase with dissolve
    ada "...Pusbag."
    sophia "Do you intend to move out soon, friend Ada?"
    ada "Why? This is an utter misuse of our capabilities."
    sophia "Nevertheless, we have our orders. It is now up to us to carry them out to the best of our ability."
    ada "Hmph, it's not like I have anything better to do."
    "...I just wish I knew if it'll all matter in the end."
    
    stop music fadeout 1
    scene bg blank with fade
    
label prologue2:
    $ renpy.movie_cutscene("videos/op.webm")
    
    show chapterTitle prologue2 at chapterTitlePos, chapterTitleAnim
    show chapterTitle2 prologue2 at chapterTitlePos2, chapterTitleAnim
    pause 5
    hide chapterTitle
    hide chapterTitle2
    pause 2
        
    play music soundtracks["Intro"]
    
    nvl clear
    nvl show dissolveFast
    
    show factionicon empire at truecenter, spinY with dissolve
    
    nvlChar "Hundreds of years ago, the Legate Saktoth led the Imperial Vanguard Legion in battle against the foes of a burning Empire."
    nvlChar "He crushed the pirates threatening the imperial borders, then joined forces with the human purity advocates of the True Born to subdue the rebellious Free Machines. 
     With these martial triumphs under his banner, he was crowned Emperor."
    nvlChar "The Trueborns were given positions of power in reward for their assistance, and soon came to dominte the new order's politics. 
     In time, the genetically augmented citizens and even those of the great noble houses soon found themselves targets of persecution. 
     The AIs, already little trusted by their human masters, were further constrained; only the necessity of their continued function prevented their outright destruction."
    nvlChar "Still, Saktoth I's reign was a peaceful and well-regarded time, and the worst excesses had yet to take root. 
     After his death, however, the imperial hierarchy ossified, and the structure began to crumble under the weight of a succession of weak emperors."
    nvlChar "In time, those who had felt the boot or the yoke of the old Empire began plotting vengeance. 
             Revolts and invasions broke out across the Imperial borders, the fires of war spreading to seemingly even the most quiet corners of the galaxy.
             \nLike here..."

    nvl clear
    nvl hide dissolveFast
    hide factionicon with dissolve
    stop music fadeout 1
    pause 1
    
    show textimg prologue2 at truecenter with dissolve
    pause
    hide textimg with dissolveFast
    
    play music "sfx/ambience/outdoor-windy-ambience.ogg" fadein 0.5
    scene bg glacies with fade
    "The wind howls over the snowscaped valley. Even inside my climate-controlled cockpit, I can feel the cold biting into my face."
    "After that last debacle, the 13th has been moved out to the lonely little world of CB-135. The rebels have been stopped – for now – but now the Free Machines are closing in."
    "An advance force has been confirmed in this sector. Command has dispatched us here to perform a reconnaisance-in-force and turn back the enemy incursion if we can."
    "They didn't say it in so many words, but it's not hard to see that ultimately we're just delaying them. The Empire has made too many enemies, and they've been allowed to grow too strong."
    "Still, I have a job to do. Tomorrow can worry about itself."
    "Besides, if we put up a good fight, we might even drag the war out long enough for a negotiated settlement... Ha! That'll be the day."
    sophia "No sign of the enemy just yet. We have an opportunity to dig in and prepare for the upcoming engagement."
    ada "They probably decided to stay home. Even the Machines know better than to come to this iceball."
    sophia "Outside air temperature is only 254 K, friend Ada."
    ada "That's negative 19 degrees C!"
    sophia "Negative 19.25°C, friend Ada. Precision is important in such matters."
    ada "Ugh. Look, it's really cold, alright?"
    
    scene cg prologue2 ada with dissolve
    ada "Actually, why isn't the river frozen?"
    sophia "It's not actually a river. It's an... elongated lake formed in a recessed channel when local geothermal activity melted the snow. Actually, I think at least one end connects to an underground aquifer as well."
    ada" Interesting."
    "I'd admit, it's actually quite pretty. Calming, even."
    "The whole valley is like that, really. It's too bad it won't be that way for much longer now."
    show bg glacies sky with dissolve
    ada "...Well, we'd better get ready. If the Machines really are here, it's only a matter of time... and I don't intend to run away again."
    
label prologue2_battle:
    call missionStart("sunrise_prologue2", tutorial=True)
    
    if _return == 0:
        jump gameOver
    if _return == -1:
        return    

label prologue2_outro:
    show bg glacies with fade
    play sound "sfx/explosion/ex_med4.wav"
    show bg glacies with Shake(CENTER_TUPLE, 1.0, dist=16)
    #play music "sfx/ambience/outdoor-windy-ambience.ogg"
    
    ada "And that's the last of them."
    sophia "I would have expected a larger enemy presence..."
    
    play sound {"sfx/message_team.wav", "sfx/message_team.wav"}
    imperial "Sector HQ to 13th Cohort, come in! 13th Cohort–"
    ada "HQ, 13th Actual. We've encountered and–"
    play music soundtracks["Tension"]
    imperial "Forget that! The enemy is headed for Hadrian! The Promethean has been sighted! I repeat, the Promethean has been sighted!"
    ada "...!"
    sophia "It appears this was merely a feint."
    "The leader of the Free Machines? Leading an invasion into imperial territory himself?"
    "This is bad. Really bad."
    ada "Orders, command?"
    imperial "All units are to return to Hadrian at once. Command wants the incursion stopped here and the Promethean neutralized. Do you copy?"
    ada "Copy, command. Returning to base."
    scene bg blank with fade
    ada "Well, Sophia, our weekend just got a whole lot more interesting."
    
    stop music fadeout 1
    call chapterEnd
    
    jump episode1_intro
    
    return