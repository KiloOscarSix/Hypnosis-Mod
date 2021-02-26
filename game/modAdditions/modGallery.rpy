init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = int(len(filter(lambda s: s.char == char, galleryItems)) / 8) + 1
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

define unknown = GalleryItem("Leah", "thursdaynight", "leah bjbellypre.webp", {"chooseleah":True})
define unknown = GalleryItem("Leah", "nextstep", "leah hotel4.webp", {"ashleyyes":True})
define unknown = GalleryItem("Leah", "galleryScene3", "al cg8.webp", {"both":True})
define unknown = GalleryItem("Leah", "galleryScene17", "leahbed1.webp")
define unknown = GalleryItem("Leah", "dols", "leahbs.webp")
define unknown = GalleryItem("Leah", "ml", "lbr2.webp", {"brittany":True})
define unknown = GalleryItem("Leah", "coolio", "ashdown2.webp")
define unknown = GalleryItem("Leah", "galleryScene61", "leahbig1.webp", {"leahf":False})
define unknown = GalleryItem("Leah", "galleryscene21", "Episode 11/alashleysroom5.webp", {"both":True, "beth":True})
define unknown = GalleryItem("Leah", "galleryscene37", "Episode 12/leahapartment4.webp")
define unknown = GalleryItem("Leah", "nojennep12", "Episode 12/leahtwelvebr1.webp")
define unknown = GalleryItem("Leah", "galleryScene47", "bg bedroom3.webp")

define unknown = GalleryItem("Ashley", "galleryScene1", "ashley tf1.webp")
define unknown = GalleryItem("Ashley", "galleryScene4", "al beda20.webp")
define unknown = GalleryItem("Ashley", "bulletproof", "astripes8.webp", {"fashley":True, "chooseleah":True})
define unknown = GalleryItem("Ashley", "galleryScene3", "al cg8.webp", {"both":True})
define unknown = GalleryItem("Ashley", "galleryScene2", "a bs3.webp", {"chooseleah":True, "both":True})
define unknown = GalleryItem("Ashley", "coolio", "ashdown2.webp", {"preg":True})
define unknown = GalleryItem("Ashley", "galleryScene50", "a bs1.webp")
define unknown = GalleryItem("Ashley", "galleryscene21", "Episode 11/alashleysroom5.webp", {"both":True, "beth":True})
define unknown = GalleryItem("Ashley", "galleryScene38", "Episode 12/abcouch8.webp")
define unknown = GalleryItem("Ashley", "galleryScene29", "Episode 12/ashcuddle4.webp", {"beth":False, "chooseleah":True})
define unknown = GalleryItem("Ashley", "galleryScene40", "Episode 13/locker1.webp", {"beth":True})
define unknown = GalleryItem("Ashley", "galleryScene41", "Episode 13/13ashcouch1.webp", {"badass":True})
define unknown = GalleryItem("Ashley", "nextday13", "Episode 13/13ashroom3.webp", {"badguy":True, "addictive":True})

define unknown = GalleryItem("Grace", "threesome", "gl tubf10.webp", {"grace":False, "jennmean":True})
define unknown = GalleryItem("Grace", "throwintowel", "grace couchstand9.webp", {"jennmean":True})
define unknown = GalleryItem("Grace", "galleryScene9", "grace out7.webp")
define unknown = GalleryItem("Grace", "galleryScene19", "lfktub2.webp", {"grace":True, "glthreesome":True, "laurarom":True, "daphne":True})
define unknown = GalleryItem("Grace", "galleryScene51", "gracemovies1.webp")
define unknown = GalleryItem("Grace", "galleryScene11", "gracebr3.webp", {"laura":False, "daphne":True})
define unknown = GalleryItem("Grace", "galleryScene53", "gcruise15.webp", {"glthreesome":True, "gcum":True, "leahf":False, "brittany":True})
define unknown = GalleryItem("Grace", "galleryScene55", "gtits5.webp", {"preg":True})
define unknown = GalleryItem("Grace", "galleryScene57", "gmess3.webp", {"glthreesome":True})
define unknown = GalleryItem("Grace", "galleryScene58", "lifeboat7.webp", {"gracelove":True, "preg":True})
define unknown = GalleryItem("Grace", "galleryScene59", "lez16.webp")
define unknown = GalleryItem("Grace", "nextskies", "sexbed1.webp", {"kassie":False})
define unknown = GalleryItem("Grace", "galleryScene62", "gracenews8.webp")
define unknown = GalleryItem("Grace", "galleryScene63", "gracepreg1.webp", {"glthreesome":True, "jennmean":True, "lifeboat":True})
define unknown = GalleryItem("Grace", "galleryscene24", "Episode 11/glbath3.webp", {"hatelaura":True, "callcory":False})
define unknown = GalleryItem("Grace", "galleryScene33", "Episode 13/13gracehouse10.webp", {"preg":True, "lauretoldyou":False})
define unknown = GalleryItem("Grace", "triochoice", "Episode 13/hlocker2.webp", {"gracerom":True, "hcum":True, "jenn":True, "jennice":False, "beth":True})

define unknown = GalleryItem("Laura", "didntlaura", "lk10.webp", {"laurarom":True})
define unknown = GalleryItem("Laura", "threesome", "gl tubf10.webp", {"grace":False, "jennmean":True})
define unknown = GalleryItem("Laura", "galleryScene16", "laura bed3.webp")
define unknown = GalleryItem("Laura", "followlaura", "laura br3.webp", {"laurarom":True})
define unknown = GalleryItem("Laura", "galleryScene19", "lfktub2.webp", {"grace":True, "glthreesome":True, "laurarom":True, "daphne":True})
define unknown = GalleryItem("Laura", "badtimelaura", "lneked1.webp")
define unknown = GalleryItem("Laura", "timetraveler", "lauraconvo13.webp")
define unknown = GalleryItem("Laura", "galleryscene24", "Episode 11/glbath3.webp", {"hatelaura":True, "callcory":False})
define unknown = GalleryItem("Laura", "galleryscene25", "Episode 11/lbrtub11.webp")
define unknown = GalleryItem("Laura", "galleryScene54", "croom1.webp")
define unknown = GalleryItem("Laura", "galleryScene56", "mexico6.webp", {"glthreesome":False})
define unknown = GalleryItem("Laura", "galleryScene59", "lez16.webp")
define unknown = GalleryItem("Laura", "galleryScene60", "cruisetub2.webp", {"lifeboat":False})
define unknown = GalleryItem("Laura", "toots", "laurabra2.webp")
define unknown = GalleryItem("Laura", "galleryScene46", "lcock1.webp")
define unknown = GalleryItem("Laura", "galleryScene48", "laurahoteltf4.webp")

define unknown = GalleryItem("Jenn", "admitjennsexy", "jenn onknees6.webp")
define unknown = GalleryItem("Jenn", "smart2", "jenn day12.webp", {"jenn":True})
define unknown = GalleryItem("Jenn", "galleryScene14", "jennbr16.webp", {"jennice":False})
define unknown = GalleryItem("Jenn", "galleryScene13", "jlsroom5.webp", {"jenn":True, "kissgrace":True, "jennice":False, "jennpreg":True})
define unknown = GalleryItem("Jenn", "galleryScene49", "backseat.webp")
define unknown = GalleryItem("Jenn", "galleryScene15", "jennint18.webp", {"laura":False, "jennpreg":True, "jennice":False})
define unknown = GalleryItem("Jenn", "preview", "Episode 12/hjclass24.webp", {"jennpreg":True})
define unknown = GalleryItem("Jenn", "galleryScene32", "Episode 12/japartment10.webp", {"jennpreg":True})
define unknown = GalleryItem("Jenn", "triochoice", "Episode 13/hlocker2.webp", {"gracerom":True, "hcum":True, "jenn":True, "jennice":False, "beth":True})

define unknown = GalleryItem("Brittany", "icmi", "b br13.webp", {"grace":True})
define unknown = GalleryItem("Brittany", "galleryScene6", "bdark3.webp", {"bcum":True})
define unknown = GalleryItem("Brittany", "britbangbang", "britbr2.webp")
define unknown = GalleryItem("Brittany", "galleryScene7", "britbed2.webp", {"laurarom":True, "bcum":True})
define unknown = GalleryItem("Brittany", "galleryScene8", "brit br2.webp", {"bbaby":False, "bcum":True})
define unknown = GalleryItem("Brittany", "galleryScene26", "britnotpreg7.webp", {"bcum":False})
define unknown = GalleryItem("Brittany", "galleryScene27", "britroombig4.webp", {"preg":True})
define unknown = GalleryItem("Brittany", "galleryScene28", "backseat.webp", {"brittany":True, "preg":False})
define unknown = GalleryItem("Brittany", "britend", "Episode 12/backalley6.webp", {"preg":True})
define unknown = GalleryItem("Brittany", "galleryScene42", "britpreg5.webp", {"hypbrit":True, "bcum":True})

define unknown = GalleryItem("Rachel", "gorachel", "rachdown5.webp")
define unknown = GalleryItem("Rachel", "fuckrachel", "rachair6.webp", {"rachdrunk":False})
define unknown = GalleryItem("Rachel", "bullsonparade", "rachel fridge3.webp", {"rachel":True, "rcum":True})
define unknown = GalleryItem("Rachel", "galleryScene18", "rachwall1.webp")
define unknown = GalleryItem("Rachel", "galleryScene34", "Episode 13/rachelhouse18.webp")
define unknown = GalleryItem("Rachel", "rachelnow", "Episode 13/rachelpark12.webp", {"rcum":True})

define unknown = GalleryItem("Other", "pushforward", "haleybed5.webp")
define unknown = GalleryItem("Other", "galleryScene12", "ht13.webp", {"haley":True, "hcum":True})
define unknown = GalleryItem("Other", "galleryScene59", "lez16.webp")
define unknown = GalleryItem("Other", "haleyvisit", "haleyhuge7.webp", {"hcum":True, "bigtits":True, "brittany":True, "gracefuck":False})
define unknown = GalleryItem("Other", "galleryScene23", "Episode 11/daphbath11.webp", {"jennmean":True, "callrachel":False})
define unknown = GalleryItem("Other", "galleryScene30", "Episode 12/bethhall9.webp")
define unknown = GalleryItem("Other", "galleryScene31", "Episode 12/hclass19.webp")
define unknown = GalleryItem("Other", "galleryScene39", "Episode 12/haleybedspread.webp")
define unknown = GalleryItem("Other", "galleryScene43", "Episode 13/beth134.webp", {"gracerom":True})
define unknown = GalleryItem("Other", "fuckbeth", "Episode 13/bethsroom18.webp")
define unknown = GalleryItem("Other", "bethblowie", "Episode 13/bethbr13.webp", {"bethbj":True})
define unknown = GalleryItem("Other", "galleryScene44", "Episode 13/bethsroom20.webp")
define unknown = GalleryItem("Other", "galleryScene36", "Episode 13/tifhome17.webp", {"tifriendzone":True})
define unknown = GalleryItem("Other", "galleryScene45", "Episode 13/bailey13.webp")
define unknown = GalleryItem("Other", "triochoice", "Episode 13/hlocker2.webp", {"gracerom":True, "hcum":True, "jenn":True, "jennice":False, "beth":True})



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
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/modAdditions/images/button.png"
                hover Transform(im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/modAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/modAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in galleryMenu:
            vbox:
                imagebutton:
                    action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="Unknown"):
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/modAdditions/images/button.png"
                hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/modAdditions/images/button.png"
                    hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for galleryItem in galleryItems:
            if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                imagebutton:
                    action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                    idle Transform(galleryItem.thumbnail, zoom=0.2)
                    hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
