# PROTIP: the _(string) means translation
# see https://www.renpy.org/doc/html/translation.html#translation-actions-functions-and-variables

init python:
    class Planet:
        def __init__(self, name, pos, size, mapSize, missions, image, background):
            self.name = name
            self.pos = pos
            self.size = size
            self.mapSize = mapSize
            self.missions = missions
            self.image = image
            self.background = background
            self.flavorText = ""
            self.type = _("<NO DATA>")
            self.radius = _("<NO DATA>")
            self.primary = _("<NO DATA>")
            self.primaryType = _("<NO DATA>")
            self.gravity = _("<NO DATA>")
            self.defRating = _("<NO DATA>")
            
        def SetPrimaryAndType(self, primary, type):
            self.primary = primary
            self.primaryType = type
    
    class Mission:
        def __init__(self, name, text, scriptLabel):
            self.name = name
            self.text = text
            self.scriptLabel = scriptLabel
    
    def isMissionUnlocked(mission):
        return mission in store.missionsUnlocked
        
    def isMissionCompleted(mission):
        return mission in store.missionsCompleted
        
    def shouldShowPlanet(planet):
        #print(store.missionsUnlocked)
        if getattr(planet, "alwaysVisible", False):
            return True
        for mission in planet.missions:
            if isMissionUnlocked(mission):
                return True
        return False
        
    def hasIncompleteMissions(planet):
        for mission in planet.missions:
            if not isMissionCompleted(mission):
                return True
        return False

init python:      
    planets = {
        "sunrise" : {
            "fenghuang" : Planet(_("42 Fenghuang"), (0.2, 0.8), (259, 259), (48, 48), ["episode1"], "images/planets/barren01.png", "images/bg/space/20.jpg")
        }
    }
    missions = {
        "sunrise" : {
            "episode1" : Mission(_("Awakening"), _("Awaken from stasis"), "episode1_intro")
        }
    }
    
    store.missionsCompleted = {}
    store.missionsUnlocked = {}

init python:
        planets["sunrise"]["fenghuang"].type = _("Asteroid")
        planets["sunrise"]["fenghuang"].radius = "213 km"
        planets["sunrise"]["fenghuang"].gravity = "0.0072 g"
        planets["sunrise"]["fenghuang"].SetPrimaryAndType(_("Yangtze"), "K3")
        planets["sunrise"]["fenghuang"].defRating = "0.2"
        planets["sunrise"]["fenghuang"].flavorText = _("This lonely asteroid was the site of one of the Promethean's greatest victories over the Empire. "
                                                                    "The Free Machines lured three auxiliary legions (and even an Imperial Vanguard cohort) here, then surrounded and annihilated them. "
                                                                    "Today, feral robots scavenge the corpses from Fenghuang's unweathered surface.")
        
        