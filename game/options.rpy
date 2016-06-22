﻿## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python:
    ## This controls where the VN looks for Spring engine files.
    ## TODO: needs Linux support
    # My Games/Spring/campaign/game/../../engine/100.0
    SPRING_DIR = "D:/Games/Spring/engine/100.0" #"sys.path[0]/../../engine/100.0"
    
    ## TODO: untested
    ## If engine was not downloaded with ZKL, tell it where to find Spring data dir
    SPRING_DATADIR = None      #"../"      # "C:/Users/Rattlesnark/Documents/My Games/Spring"

init -1 python hide: 
    ## These control the width and height of the screen.
    ## Changing this would require redoing the UI or at least implementing resizing, don't touch it!

    config.screen_width = 1280
    config.screen_height = 768

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Zero-K: Sunrise"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "Zero-K Sunrise"
    config.version = "0.1"
    
    config.developer = True
    config.autoreload = False

    #########################################
    # Themes

    ## We then want to call a theme function. theme.roundrect is
    ## a theme that features the use of rounded rectangles.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.diamond(
        ## Theme: Diamond
        ## Color scheme: City Lights

        ## The color of an idle widget face.
        widget = "#359d98",

        ## The color of a focused widget face.
        widget_hover = "#2e5860",

        ## The color of the text in a widget.
        widget_text = "#9de0ad",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#e5fcc2",

        ## The color of a disabled widget face.
        disabled = "#638e89",

        ## The color of disabled widget text.
        disabled_text = "#594f4f",

        ## The color of informational labels.
        label = "#e5fcc2",

        ## The color of a frame containing widgets.
        frame = "#345960",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "cg mainmenu video",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "cg mainmenu grayscale",
        #gm_root = "#0008",
        
        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = True,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = "images/ui/textwindow.png"

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 8
    style.window.right_padding = 8
    style.window.top_padding = 8
    style.window.bottom_padding = 8

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 150


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    # style.default.font = "DejaVuSans.ttf"

    ## The default size of text.

    style.default.size = 24

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to True if the game has voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    # config.main_menu_music = "main_menu_theme.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.
    config.help = "README.html"


    #########################################
    ## Transitions.
    ## See https://www.renpy.org/doc/html/config.html#transitions for help

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = dissolveFast

    ## Used between screens of the game menu.
    config.intra_transition = dissolveFast

    ## The transition used when entering the game menu from the main menu, as is done when clicking "Load Game" or "Preferences".
    config.main_game_transition = dissolveFast

    ## The transition that is used to display the main menu after leaving the game menu. 
    ## This is used when the load and preferences screens are invoked from the main menu, 
    ## and it's also used when the user picks "Main Menu" from the game menu.
    config.game_main_transition = dissolveFast

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = Fade(0,0,1)

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = Fade(1,0,1)

    ## Used when a game is loaded.
    config.after_load_transition = dissolve

    ## Used when the window is shown.
    config.window_show_transition = dissolve

    ## Used when the window is hidden.
    config.window_hide_transition = dissolve

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = dissolve

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = dissolve

    ## Used when yesno is shown.
    config.enter_yesno_transition = None

    ## Used when the yesno is hidden.
    config.exit_yesno_transition = None

    ## Used when entering a replay
    config.enter_replay_transition = None

    ## Used when exiting a replay
    config.exit_replay_transition = None

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = None

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
python early:
    config.save_directory = "Zero-K Sunrise-1464616045"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 50

    ## The default auto-forward time setting.

    config.default_afm_time = 10

    #########################################
    ## More customizations can go here.
    
    config.window_icon = "images/ZK_logo_128.png"

## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "Zero-K-Sunrise"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Sunrise"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    