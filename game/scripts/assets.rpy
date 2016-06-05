# ============================================================
# BACKGROUNDS
# ============================================================
image bg blank = "images/bg/blank.png"
image bg fieldsofisis = im.Scale("images/bg/fields_of_isis.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg fieldsofisis sky = im.Scale("images/bg/fields_of_isis_sky.png", SCREENSIZE_X, SCREENSIZE_Y)

# ============================================================
# CG
# ============================================================
image titleSunrise:
    0.4
    Text("sunrise", size=64, outlines={(2,"#222",3,3)})
    xalign 0.8 ypos 0.32 yanchor 0.5 alpha 0 xzoom 0 
    linear 0.15 xalign 0.7 alpha 1 xzoom 1

image zklogo mainmenu:
    "images/zk_logo.png"
    xalign 0.3 ypos 0.2 yanchor 0.5 alpha 0 xzoom 0
    linear 0.15 xalign 0.5 alpha 1 xzoom 1
    
image gameOverText:
    Text("game over", size=48, outlines={(2,"#222",3,3)})
    
image cg mainmenu = "images/cg/mainmenu.png"
image cg mainmenu video = Movie(channel="mainmenuvid", play="videos/mainmenu.avi")
image cg mainmenu grayscale = im.Grayscale("images/cg/mainmenu.png")

image cg prologue1 ada = "images/cg/prologue1_ada_intro.png"
image cg prologue1 rebelvehicles = "images/cg/prologue1_rebelvehicles.png"
image cg prologue1 transport1 = "images/cg/prologue1_transport_1.png"
image cg prologue1 transport2 = "images/cg/prologue1_transport_2.png"


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

transform chapterTitleAnim:
    on show:
        alpha 0 xzoom 4 yzoom 2
        linear 0.5 alpha 1 xzoom 1 yzoom 1
    on hide:
        alpha 1 xzoom 1 yzoom 1
        linear 0.5 alpha 0 xzoom 4 yzoom 2
    
    
# ============================================================
# TITLE TEXTS
# ============================================================
image chapterTitle prologue1 = Text("Prologue 1", size=32, outlines={(2,"#222",3,3)})
image chapterTitle2 prologue1 = Text(chapterTitles["prologue1"], size=64, outlines={(2,"#222",3,3)})

# ============================================================
# OTHER STUFF
# ============================================================

