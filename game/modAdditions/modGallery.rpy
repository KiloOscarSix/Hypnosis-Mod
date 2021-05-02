init python:
    import math
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = int(math.floor(len(filter(lambda s: s.char == char, galleryItems))/8)) + 1
            print(self.pageNum)
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = "/images/{}".format(thumbnail)
            galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

    GalleryItem("Leah", "thursdaynight", "leah bjbellypre.webp", {"chooseleah":True})
    GalleryItem("Leah", "nextstep", "leah hotel4.webp", {"ashleyyes":True})
    GalleryItem("Leah", "galleryScene3", "al cg8.webp", {"both":True})
    GalleryItem("Leah", "galleryScene17", "leahbed1.webp")
    GalleryItem("Leah", "dols", "leahbs.webp")
    GalleryItem("Leah", "ml", "lbr2.webp", {"brittany":True})
    GalleryItem("Leah", "coolio", "ashdown2.webp")
    GalleryItem("Leah", "galleryScene61", "leahbig1.webp", {"leahf":False})
    GalleryItem("Leah", "galleryscene21", "Episode 11/alashleysroom5.webp", {"both":True, "beth":True})
    GalleryItem("Leah", "galleryscene37", "Episode 12/leahapartment4.webp")
    GalleryItem("Leah", "nojennep12", "Episode 12/leahtwelvebr1.webp")
    GalleryItem("Leah", "galleryScene47", "bg bedroom3.webp")
    GalleryItem("Leah", "galleryScene65", "Endings/lapt5.webp")

    GalleryItem("Ashley", "galleryScene1", "ashley tf1.webp")
    GalleryItem("Ashley", "galleryScene4", "al beda20.webp")
    GalleryItem("Ashley", "bulletproof", "astripes8.webp", {"fashley":True, "chooseleah":True})
    GalleryItem("Ashley", "galleryScene3", "al cg8.webp", {"both":True})
    GalleryItem("Ashley", "galleryScene2", "a bs3.webp", {"chooseleah":True, "both":True})
    GalleryItem("Ashley", "coolio", "ashdown2.webp", {"preg":True})
    GalleryItem("Ashley", "galleryScene50", "a bs1.webp")
    GalleryItem("Ashley", "galleryscene21", "Episode 11/alashleysroom5.webp", {"both":True, "beth":True})
    GalleryItem("Ashley", "galleryScene38", "Episode 12/abcouch8.webp")
    GalleryItem("Ashley", "galleryScene29", "Episode 12/ashcuddle4.webp", {"beth":False, "chooseleah":True})
    GalleryItem("Ashley", "galleryScene40", "Episode 13/locker1.webp", {"beth":True})
    GalleryItem("Ashley", "galleryScene41", "Episode 13/13ashcouch1.webp", {"badass":True})
    GalleryItem("Ashley", "nextday13", "Episode 13/13ashroom3.webp", {"badguy":True, "addictive":True})
    GalleryItem("Ashley", "galleryScene65", "Endings/lapt5.webp")
    GalleryItem("Ashley", "galleryScene70", "Endings/aptv4.webp")

    GalleryItem("Grace", "threesome", "gl tubf10.webp", {"grace":False, "jennmean":True})
    GalleryItem("Grace", "throwintowel", "grace couchstand9.webp", {"jennmean":True})
    GalleryItem("Grace", "galleryScene9", "grace out7.webp")
    GalleryItem("Grace", "galleryScene19", "lfktub2.webp", {"grace":True, "glthreesome":True, "laurarom":True, "daphne":True})
    GalleryItem("Grace", "galleryScene51", "gracemovies1.webp")
    GalleryItem("Grace", "galleryScene11", "gracebr3.webp", {"laura":False, "daphne":True})
    GalleryItem("Grace", "galleryScene53", "gcruise15.webp", {"glthreesome":True, "gcum":True, "leahf":False, "brittany":True})
    GalleryItem("Grace", "galleryScene55", "gtits5.webp", {"preg":True})
    GalleryItem("Grace", "galleryScene57", "gmess3.webp", {"glthreesome":True})
    GalleryItem("Grace", "galleryScene58", "lifeboat7.webp", {"gracelove":True, "preg":True})
    GalleryItem("Grace", "galleryScene59", "lez16.webp")
    GalleryItem("Grace", "nextskies", "sexbed1.webp", {"kassie":False})
    GalleryItem("Grace", "galleryScene62", "gracenews8.webp")
    GalleryItem("Grace", "galleryScene63", "gracepreg1.webp", {"glthreesome":True, "jennmean":True, "lifeboat":True})
    GalleryItem("Grace", "galleryscene24", "Episode 11/glbath3.webp", {"hatelaura":True, "callcory":False})
    GalleryItem("Grace", "galleryScene33", "Episode 13/13gracehouse10.webp", {"preg":True, "lauretoldyou":False})
    GalleryItem("Grace", "triochoice", "Episode 13/hlocker2.webp", {"gracerom":True, "hcum":True, "jenn":True, "jennice":False, "beth":True})
    GalleryItem("Grace", "galleryScene66", "Endings/apt8.webp")
    GalleryItem("Grace", "galleryScene74", "Endings/gracestrip2.webp", {"huge":True})

    GalleryItem("Laura", "didntlaura", "lk10.webp", {"laurarom":True})
    GalleryItem("Laura", "threesome", "gl tubf10.webp", {"grace":False, "jennmean":True})
    GalleryItem("Laura", "galleryScene16", "laura bed3.webp")
    GalleryItem("Laura", "followlaura", "laura br3.webp", {"laurarom":True})
    GalleryItem("Laura", "galleryScene19", "lfktub2.webp", {"grace":True, "glthreesome":True, "laurarom":True, "daphne":True})
    GalleryItem("Laura", "badtimelaura", "lneked1.webp")
    GalleryItem("Laura", "timetraveler", "lauraconvo13.webp")
    GalleryItem("Laura", "galleryscene24", "Episode 11/glbath3.webp", {"hatelaura":True, "callcory":False})
    GalleryItem("Laura", "galleryscene25", "Episode 11/lbrtub11.webp")
    GalleryItem("Laura", "galleryScene54", "croom1.webp")
    GalleryItem("Laura", "galleryScene56", "mexico6.webp", {"glthreesome":False})
    GalleryItem("Laura", "galleryScene59", "lez16.webp")
    GalleryItem("Laura", "galleryScene60", "cruisetub2.webp", {"lifeboat":False})
    GalleryItem("Laura", "toots", "laurabra2.webp")
    GalleryItem("Laura", "galleryScene46", "lcock1.webp")
    GalleryItem("Laura", "galleryScene48", "laurahoteltf4.webp")
    GalleryItem("Laura", "galleryScene69", "Endings/laurabwe7.webp")
    GalleryItem("Laura", "galleryScene73", "Endings/laurafuckable1.webp")

    GalleryItem("Jenn", "admitjennsexy", "jenn onknees6.webp")
    GalleryItem("Jenn", "smart2", "jenn day12.webp", {"jenn":True})
    GalleryItem("Jenn", "galleryScene14", "jennbr16.webp", {"jennice":False})
    GalleryItem("Jenn", "galleryScene13", "jlsroom5.webp", {"jenn":True, "kissgrace":True, "jennice":False, "jennpreg":True})
    GalleryItem("Jenn", "galleryScene49", "backseat.webp")
    GalleryItem("Jenn", "galleryScene15", "jennint18.webp", {"laura":False, "jennpreg":True, "jennice":False})
    GalleryItem("Jenn", "preview", "Episode 12/hjclass24.webp", {"jennpreg":True})
    GalleryItem("Jenn", "galleryScene32", "Episode 12/japartment10.webp", {"jennpreg":True})
    GalleryItem("Jenn", "triochoice", "Episode 13/hlocker2.webp", {"gracerom":True, "hcum":True, "jenn":True, "jennice":False, "beth":True})
    GalleryItem("Jenn", "galleryScene66", "Endings/apt8.webp")
    GalleryItem("Jenn", "galleryScene71", "Endings/jennbath10.webp", {"hpregs":True, "huge":True, "lactation":True, "preg":True})

    GalleryItem("Brittany", "icmi", "b br13.webp", {"grace":True})
    GalleryItem("Brittany", "galleryScene6", "bdark3.webp", {"bcum":True})
    GalleryItem("Brittany", "britbangbang", "britbr2.webp")
    GalleryItem("Brittany", "galleryScene7", "britbed2.webp", {"laurarom":True, "bcum":True})
    GalleryItem("Brittany", "galleryScene8", "brit br2.webp", {"bbaby":False, "bcum":True})
    GalleryItem("Brittany", "galleryScene26", "britnotpreg7.webp", {"bcum":False})
    GalleryItem("Brittany", "galleryScene27", "britroombig4.webp", {"preg":True})
    GalleryItem("Brittany", "galleryScene28", "backseat.webp", {"brittany":True, "preg":False})
    GalleryItem("Brittany", "britend", "Episode 12/backalley6.webp", {"preg":True})
    GalleryItem("Brittany", "galleryScene42", "britpreg5.webp", {"hypbrit":True, "bcum":True})
    GalleryItem("Brittany", "okaybrit", "Endings/bapt3.webp")

    GalleryItem("Rachel", "gorachel", "rachdown5.webp")
    GalleryItem("Rachel", "fuckrachel", "rachair6.webp", {"rachdrunk":False})
    GalleryItem("Rachel", "bullsonparade", "rachel fridge3.webp", {"rachel":True, "rcum":True})
    GalleryItem("Rachel", "galleryScene18", "rachwall1.webp")
    GalleryItem("Rachel", "galleryScene34", "Episode 13/rachelhouse18.webp")
    GalleryItem("Rachel", "rachelnow", "Episode 13/rachelpark12.webp", {"rcum":True})

    GalleryItem("Other", "pushforward", "haleybed5.webp")
    GalleryItem("Other", "galleryScene12", "ht13.webp", {"haley":True, "hcum":True})
    GalleryItem("Other", "galleryScene59", "lez16.webp")
    GalleryItem("Other", "haleyvisit", "haleyhuge7.webp", {"hcum":True, "bigtits":True, "brittany":True, "gracefuck":False})
    GalleryItem("Other", "galleryScene23", "Episode 11/daphbath11.webp", {"jennmean":True, "callrachel":False})
    GalleryItem("Other", "galleryScene30", "Episode 12/bethhall9.webp")
    GalleryItem("Other", "galleryScene31", "Episode 12/hclass19.webp")
    GalleryItem("Other", "galleryScene39", "Episode 12/haleybedspread.webp")
    GalleryItem("Other", "galleryScene43", "Episode 13/beth134.webp", {"gracerom":True})
    GalleryItem("Other", "fuckbeth", "Episode 13/bethsroom18.webp")
    GalleryItem("Other", "bethblowie", "Episode 13/bethbr13.webp", {"bethbj":True})
    GalleryItem("Other", "galleryScene44", "Episode 13/bethsroom20.webp")
    GalleryItem("Other", "galleryScene36", "Episode 13/tifhome17.webp", {"tifriendzone":True})
    GalleryItem("Other", "galleryScene45", "Episode 13/bailey13.webp")
    GalleryItem("Other", "triochoice", "Episode 13/hlocker2.webp", {"gracerom":True, "hcum":True, "jenn":True, "jennice":False, "beth":True})
    GalleryItem("Other", "galleryScene64", "Endings/hapt6.webp", {"hcum":True, "preg":True})
    GalleryItem("Other", "galleryScene67", "Episode 13/btgg3.webp")
    GalleryItem("Other", "galleryScene68", "Endings/haleybwe4.webp")
    GalleryItem("Other", "fucktiffanyapt", "Endings/aptv1.webp")
    GalleryItem("Other", "onbailey", "Episode 13/bailey6.webp")
    GalleryItem("Other", "galleryScene72", "Endings/haleyjd8.webp")
    GalleryItem("Other", "galleryScene75", "Episode 13/btgg3.webp")
    GalleryItem("Other", "galleryScene76", "Endings/ghcouch9.webp")
    GalleryItem("Other", "tifanending", "Endings/tifkitchen1.webp")
    GalleryItem("Other", "lauraccepted", "Endings/aptpool30.webp")

define galleryMenu = [
    ["Leah", "/images/leah hotel1.webp"],
    ["Ashley", "/images/a room3.webp"],
    ["Grace", "/images/grace bowling1.webp"],
    ["Laura", "/images/blshowdown1.webp"],
    ["Jenn", "/images/jenn outside1.webp"],
    ["Brittany", "/images/brit1.webp"],
    ["Rachel", "/images/rachall6.webp"],
    ["Other", "/images/hal5.webp"],
]

default galleryPageNumber = 1
default scopeDict = {}

label galleryNameChange:
    default persistent.galleryName = ""
    default persistent.galleryNickname = ""
    default persistant.galleryMaster = ""
    if persistent.galleryName == "":
        $ persistent.galleryName = renpy.input("Enter your name: ")
    if persistent.galleryNickname == "":
        $ persistent.galleryNickname = renpy.input("Enter your nickname: ")
    if persistent.galleryMaster == "":
        menu:
            "OscarSix" "Do the girls call you Master/Daddy?"
            "Yes":
                $ persistent.galleryMaster = True
            "No":
                $ persistent.galleryMaster = False

    $ scopeDict = {"name":persistent.galleryName, "nickname":persistent.nickname, "master":persistent.galleryMaster}
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for i in galleryMenu:
                vbox:
                    imagebutton:
                        action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                        idle Transform(i[1], zoom=0.2)
                        hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                    text i[0]:
                        style "modTextBody"
                        xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="None"):
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            if galleryPageNumber == 1:
                action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
            else:
                action Function(galleryDecreasePageNumber)
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

        if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
            imagebutton:
                action Function(galleryIncreasePageNumber)
                idle "/modAdditions/images/nextButton.png"
                hover im.MatrixColor("/modAdditions/images/nextButton.png", im.matrix.brightness(0.2))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for galleryItem in galleryItems:
                if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                    imagebutton:
                        action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                        idle Transform(galleryItem.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(galleryItem.thumbnail, 15), zoom=0.2)
