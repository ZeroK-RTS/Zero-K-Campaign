# ============================================================
# BACKGROUNDS
# ============================================================
image bg blank = "images/bg/blank.png"
image bg white = "images/bg/white.png"
image bg fieldsofisis = "images/bg/fields_of_isis.png"  #im.Scale("images/bg/fields_of_isis.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg fieldsofisis sky = "images/bg/fields_of_isis_sky.png" #im.Scale("images/bg/fields_of_isis_sky.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg glacies = "images/bg/glacies.png"
image bg glacies sky = "images/bg/glacies_sky.png"

# ============================================================
# CG
# ============================================================   
image cg mainmenu = "images/cg/mainmenu.png"
image cg mainmenu video = Movie(channel="mainmenuvid", play="videos/mainmenu.avi")
image cg mainmenu grayscale = im.Grayscale("images/cg/mainmenu.png")

image cg prologue1 ada = "images/cg/prologue1_ada_intro.png"
image cg prologue1 rebelvehicles = "images/cg/prologue1_rebelvehicles.png"
image cg prologue1 transport1 = "images/cg/prologue1_transport_1.png"
image cg prologue1 transport2 = "images/cg/prologue1_transport_2.png"
image cg prologue1 transport3 = "images/cg/prologue1_transport_3_alt.png"

image cg prologue2 ada = "images/cg/prologue2_ada_water.png"

# ============================================================
# CHARACTERS
# ============================================================
define ada = Character("Ada", color = '#0df5f3')
define sophia = Character("Sophia", color = '#008080')
define imperial = Character("Imperial Unit", color = '#9600FF')
define imperialColonel = Character("Colonel Aethelred", color = '#9600FF')
define rebels = Character("Rebel Units", color = '#FF4141')
define nvlChar = Character("", kind=nvl)

# ============================================================
# ANIMATIONS
# ============================================================
transform chapterTitlePos:
    xalign 0.42 yalign 0.36
    
transform chapterTitlePos2:
    xalign 0.58 yalign 0.5

transform chapterTitleAnim(dt = 0.5):
    on show:
        alpha 0 xzoom 4 yzoom 2
        linear dt alpha 1 xzoom 1 yzoom 1
    on hide:
        alpha 1 xzoom 1 yzoom 1
        linear dt alpha 0 xzoom 4 yzoom 2
    
    
# ============================================================
# TITLE TEXTS
# ============================================================
init python:
    def MakeTitleText(text, size=48):
        return Text(text=text, size=size, outlines={(2,"#222",3,3)})

image zklogo = "images/zk_logo.png"

image zklogo mainmenu:
    "images/zk_logo.png"
    xalign 0.3 ypos 0.2 yanchor 0.5 alpha 0 xzoom 0
    linear 0.15 xalign 0.5 alpha 1 xzoom 1

image titleSunrise:
    0.4
    Text("sunrise", size=64, outlines={(2,"#222",3,3)})
    xalign 0.8 ypos 0.32 yanchor 0.5 alpha 0 xzoom 0 
    linear 0.15 xalign 0.7 alpha 1 xzoom 1

image gameOverText = Text("game over", size=48, outlines={(2,"#222",3,3)})
    
image preBattleText = Text("PREPARE FOR BATTLE", size=64, outlines={(3,"#222",2,2)})

image chapterTitle prologue1 = MakeTitleText("Prologue 1")
image chapterTitle2 prologue1 = MakeTitleText("Blood Dawn")

image chapterTitle prologue2 = MakeTitleText("Prologue 2")
image chapterTitle2 prologue2 = MakeTitleText("Cold Path")

image chapterTitle episode1 = MakeTitleText("Episode 1")
image chapterTitle2 episode1 = MakeTitleText("Awakening")

# ============================================================
# MUSIC
# ============================================================
init python:
    soundtracks = {
        "Evacuation (Action)" : "<to 103>music/Evacuation (Action).mp3",
        "Inspiring" : "<to 106>music/Inspiring.mp3",
        "Intro" : "<to 71>music/Intro.mp3",
        "Intense" : "<to 86.5>music/Intense.mp3",
        "March" : "<to 66>music/March.mp3",
        "March (alt)" : "<to 146.3>music/March (alt).mp3",
        "Suspense" : "<to 113.3>music/Suspense.mp3",
        "Tension" : "<to 71.6>music/Tension.mp3",
    }

# ============================================================
# OTHER STUFF
# ============================================================
