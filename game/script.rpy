# ============================================================
# stuff
# ============================================================

init python:
    SCREENSIZE_X = config.screen_width
    SCREENSIZE_Y = config.screen_height
    CENTER_TUPLE = (0.5, 1.0, 0.5, 1.0)

define dissolveFast = Dissolve(0.2)
define dissolveExtraFast = Dissolve(0.1)

init python:
    def CloseNavigation():
        #if not renpy.get_screen("main_menu"):
            Return()
        #else:
        #    Hide("navigation")

# ============================================================
# ============================================================

# The game starts here.
label start:
    stop music fadeout 1
    jump intro

label missionStart(missionName, **kwargs):
    play sound "sfx/weapon/blade/blade_swing.wav"
    show preBattleText at truecenter, chapterTitleAnim
    pause
    stop music fadeout 1
    scene bg blank with blinds
    
    if kwargs["tutorial"]:
        menu:
            "Skip the tutorial mission?"
            "Yes":
                return 1
            "No":
                pass
                
    elif kwargs["skippable"]:
        menu:
            "Skip this mission?"
            "Yes":
                return 1
            "No":
                pass
            
    call run_spring(missionName)
    $renpy.block_rollback() 
    return _return 

label gameOver:
    scene cg mainmenu grayscale with fade
    show gameOverText at truecenter with dissolve
    pause
    scene bg blank with pixellate
    return

label chapterEnd:
    #scene cg mainmenu video
    scene bg blank
    show zklogo at truecenter   #topleft
    with fade
    pause
    scene bg blank with fade
    return

label splashscreen:
    scene bg blank with Fade(1,0,1)
    $ renpy.movie_cutscene("videos/splash.webm")
    return