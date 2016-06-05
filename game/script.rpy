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
    jump prologue

label missionStart(missionName):
    stop music fadeout 1
    play sound "sfx/weapon/blade/blade_swing.wav"
    scene bg blank with blinds
    
    call run_spring(missionName)
    $renpy.block_rollback()
    
    return _return

label gameOver:
    scene cg mainmenu grayscale with fade
    show gameOverText at truecenter with dissolve
    pause
    scene bg blank with pixellate
    return

label splashscreen:
    scene bg blank with Fade(1,0,1)
    $ renpy.movie_cutscene("videos/splash.webm")
    return