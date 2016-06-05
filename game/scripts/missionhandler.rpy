# ============================================================
# Missions manager
# ============================================================
   

# ============================================================
# functions
init python:
    import os
    import subprocess
    import sys
    import traceback
    import json
    import platform
    from StringIO import StringIO

    # moved to options.rpy
    #SPRING_DIR = sys.path[0] + "/spring"    
    #SPRING_DIR = "D:/Games/Spring/engine/100.0" # TODO put in config somewhere somehow
    #SPRING_DIR = renpy.loader.transfn("../spring")
    
    EXECUTABLE_PATH = SPRING_DIR + "/spring"
    EXECUTABLE_PATH_WIN = EXECUTABLE_PATH + ".exe"
    SCRIPT_DIR = sys.path[0] + "/game/missions/scripts/"
    SCRIPT_FILENAME_TEMP = "_script.txt"
    SCRIPT_PATH_TEMP = SPRING_DIR + "/" + SCRIPT_FILENAME_TEMP
    RESULTS_PATH = SPRING_DIR + "/" + "mission_results.json"
    #RESULTS_PATH = SPRING_DIR + "/" + "results.py"
    #RESULTS_PATH_COMPILED = SPRING_DIR + "/" + "results.pyo" # dunno if necessary to delete this as well

    sys.path.append(SPRING_DIR)
    
    # TODO: write modules, special flags
    def getStartscriptSubstDict(missionName):
        dict = {}
        return dict
        
    def writeStartscript(missionName):
        scriptRaw = open(SCRIPT_DIR + missionName + ".txt", 'r')
        s = ""
        for line in scriptRaw:
            s += line
        s = s % getStartscriptSubstDict(missionName)
        scriptRaw.close()
        script = open(SCRIPT_PATH_TEMP, 'w')
        script.write(s)
        script.close()
    
    def removeResultFiles():
        try:
            os.remove(RESULTS_PATH)
            #os.remove(RESULTS_PATH_COMPILED)
        except:
            print("Warning: failed to delete results file")
            print("File may already not exist, or may be in use")
            
    def writeEnvVars():
        s = ""
        d = dict(os.environ)
        for key, value in sorted(d.items()):
            s += key + "=" + value + "\n"
        testFile = open(SPRING_DIR + "/envVars.txt", 'w');
        testFile.write(s)
        testFile.close()

label run_spring(missionName):    
    # $ writeEnvVars()  # debug
    
    while True:
        python:
            removeResultFiles()
            writeStartscript(missionName)
            #envVars = dict(os.environ.copy())
            if "SDL_VIDEODRIVER" in os.environ:
                del os.environ["SDL_VIDEODRIVER"]
            if platform.system() == 'Windows':
                executablePath = EXECUTABLE_PATH_WIN
            else:
                executablePath = EXECUTABLE_PATH
            subprocess.call([executablePath, SCRIPT_PATH_TEMP, "--"])    #"--isolation"
    
        # parse results
        # for some reason this breaks when moved to its own function >:|
        python:
            loadSuccess = False
            try:
                #execfile(RESULTS_PATH)
                with open(RESULTS_PATH) as resultsJSON:
                    combatResults = json.load(resultsJSON)
                    print(combatResults)
                    loadSuccess = True
            except:
                print("Failed to load data from Spring")
                traceback.print_stack()
                combatResults = {"result":None}
        if loadSuccess == True:
            if combatResults["result"] == "defeat":
                return 0
            elif combatResults["result"] == "victory":
                return 1
            elif combatResults["result"] == "draw":
                return -1
        
        menu:
            "Error loading combat results."
            "Abort":
                return -1
            "Retry":
                $ print("Retrying mission")
            "Ignore":
                return 1
    
        