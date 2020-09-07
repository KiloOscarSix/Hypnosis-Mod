init python:
    import requests
    import hashlib
    import logging

    def isUpToDate(fileName, url):
        f = open(fileName, "r")
        file = f.read()
        f.close()
        hash = hashlib.sha256((file).encode('utf-8')).hexdigest()

        urlcode = requests.get(url).text
        urlhash = hashlib.sha256((urlcode).encode('utf-8')).hexdigest()

        if hash == urlhash:
            return True
        else:
            return False

    modConfigPath = os.path.join(os.getcwd(), "game", "oscarAdditions", "modConfig.txt")

    def updateChecker():
        if renpy.variant("mobile"):
            return False
        if not isUpToDate(modConfigPath, "https://raw.githubusercontent.com/KiloOscarSix/Hypnosis-OscarSix-s-Mod/master/game/oscarAdditions/modConfig.txt"):
            return True
        return False
