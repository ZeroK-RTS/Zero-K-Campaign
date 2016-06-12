# ============================================================
# BACKGROUNDS
# ============================================================
image bg blank = "images/bg/blank.png"
image bg fieldsofisis = im.Scale("images/bg/fields_of_isis.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg fieldsofisis sky = im.Scale("images/bg/fields_of_isis_sky.png", SCREENSIZE_X, SCREENSIZE_Y)

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


# ============================================================
# CHARACTERS
# ============================================================
define ada = Character("Ada", color = '#0df5f3')
define sophia = Character("Sophia", color = '#008080')
define imperial = Character("Imperial Unit", color = '#9600FF')
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
    def MakeTitleText(text):
        return Text(text=text, size=32, outlines={(2,"#222",3,3)})

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
image chapterTitle2 prologue1 = MakeTitleText(chapterTitles["prologue1"])

image chapterTitle prologue2 = MakeTitleText("Prologue 2")
image chapterTitle2 prologue2 = MakeTitleText(chapterTitles["prologue2"])

# ============================================================
# MUSIC
# ============================================================
init python:
    soundtracks = {
        "Intro" : "<to 71>music/Intro.mp3",
        "Evacuation (Action)" : "<to 103>music/Evacuation (Action).mp3",
        "Inspiring" : "<to 106>music/Inspiring.mp3",
    }

# ============================================================
# OTHER STUFF
# ============================================================
