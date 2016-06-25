# ============================================================
# GALAXY MAP
# ============================================================
label missionSelect(lbl):
    stop music fadeout 1
    scene bg blank with Fade(1,0,0)
    jump expression lbl

label galaxyMap(trans=dissolve):
    $renpy.transition(trans)
    scene galaxy
    $renpy.call_screen("galaxymap_buttons")
    return

# adapted from Sunrider
screen galaxymap_buttons:

    modal True

    for planetName, planet in planets[store.campaign].iteritems():
        if shouldShowPlanet(planet):
            imagebutton:
                xanchor 0.5 yanchor 0.5
                action Function(renpy.call, "planetZoom", planet)
                idle im.Scale(planet.image, planet.mapSize[0], planet.mapSize[1])
                hover im.MatrixColor(im.Scale(planet.image, planet.mapSize[0], planet.mapSize[1]), im.matrix.brightness(0.5))
                pos planet.pos
            text ("{color=" + ("#fff" if hasIncompleteMissions(planet) else "#aee") + "}" + planet.name 
                + "{/color}") xpos planet.pos[0] yoffset (-(planet.mapSize[1]/2 + 8)) ypos planet.pos[1] size 20 xanchor 0.5 yanchor 0.5

label planetZoom(planet):
    show galaxy at zoomInGalaxy(planet.pos)
    show expression planet.background at zoomInFromGalaxy(planet.pos) as bg
    show expression planet.image at planetZoomIn(planet) as planet
    $renpy.transition(Dissolve(1))
    $renpy.call_screen("planetDetails", planet)
    
screen planetDetails(planet):
    
    modal True
    
    frame:
        id "planetDetails"
        xalign 0.95 yalign 0.5 xmaximum 0.7 ymaximum 0.7 xpadding 8 ypadding 8
        background "planetDetailsFrame"
        
        textbutton _("Close") action Function(renpy.call, "galaxyMap", dissolve) xalign 0.98 yalign 0.98
        
        vbox:
            first_spacing 24
            text "{b}" + planet.name.upper() + "{/b}" xalign 0.02 yalign 0.02 size 32
  
            vbox:
                text "{b}Type{/b}: " + planet.type size 24
                text "{b}Radius{/b}: " + planet.radius size 24
                text "{b}Gravity{/b}: " + planet.gravity size 24
                text "{b}Primary{/b}: " + planet.primary + (" (" + planet.primaryType + ")") size 24
                text "{b}Def. rating{/b}: " + planet.defRating size 24
                null height 24
                text planet.flavorText size 20
                
                #text "{b}Populated{/b}: " + ("Yes" if planet.populated else "No")
            
            null height 24
            
            vbox:
                for mission in planet.missions:
                    $ missionDef = missions[store.campaign][mission]
                    textbutton ((_("(completed) ") if isMissionCompleted(mission) else "") + _(missionDef.text)) action Function(renpy.call, "missionSelect", missionDef.scriptLabel) xfill True