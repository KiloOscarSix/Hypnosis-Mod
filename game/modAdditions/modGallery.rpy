init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, pageNum, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = pageNum
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

define unknown = GalleryItem("Leah", 1, "thursdaynight", "leah bjbellypre.webp", {"chooseleah":True})
define unknown = GalleryItem("Leah", 1, "nextstep", "leah hotel4.webp", {"ashleyyes":True})
define unknown = GalleryItem("Leah", 1, "galleryScene3", "al cg8.webp", {"both":True})
define unknown = GalleryItem("Leah", 1, "galleryScene17", "leahbed1.webp")
define unknown = GalleryItem("Leah", 1, "dols", "leahbs.webp")
define unknown = GalleryItem("Leah", 1, "ml", "lbr2.webp", {"brittany":True})
define unknown = GalleryItem("Leah", 1, "galleryScene5", "ashdown2.webp")
define unknown = GalleryItem("Leah", 1, "galleryscene21", "Episode 11/alashleysroom5.webp", {"both":True, "beth":True})

define unknown = GalleryItem("Ashley", 1, "galleryScene1", "ashley tf1.webp")
define unknown = GalleryItem("Ashley", 1, "galleryScene4", "al beda20.webp")
define unknown = GalleryItem("Ashley", 1, "bulletproof", "astripes8.webp", {"fashley":True, "chooseleah":True})
define unknown = GalleryItem("Ashley", 1, "galleryScene3", "al cg8.webp", {"both":True})
define unknown = GalleryItem("Ashley", 1, "galleryScene2", "a bs3.webp", {"chooseleah":True, "both":True})
define unknown = GalleryItem("Ashley", 1, "galleryScene5", "ashdown2.webp", {"preg":True})
define unknown = GalleryItem("Ashley", 1, "galleryscene21", "Episode 11/alashleysroom5.webp", {"both":True, "beth":True})
define unknown = GalleryItem("Ashley", 1, "galleryScene29", "Episode 12/ashcuddle4.webp")

define unknown = GalleryItem("Grace", 1, "threesome", "gl tubf10.webp", {"grace":False, "jennmean":True})
define unknown = GalleryItem("Grace", 1, "throwintowel", "grace couchstand9.webp")
define unknown = GalleryItem("Grace", 1, "galleryScene9", "grace out7.webp")
define unknown = GalleryItem("Grace", 1, "galleryScene19", "lfktub2.webp", {"grace":True, "glthreesome":True, "laurarom":True, "daphne":True})
define unknown = GalleryItem("Grace", 1, "galleryScene11", "gracebr3.webp", {"laura":False, "daphne":True})
define unknown = GalleryItem("Grace", 1, "sneakygrace", "gcruise15.webp", {"glthreesome":True, "gcum":True})
define unknown = GalleryItem("Grace", 1, "galleryscene24", "Episode 11/glbath3.webp", {"hatelaura":True, "callcory":False})
define unknown = GalleryItem("Grace", 1, "galleryScene33", "Episode 13/13gracehouse10.webp")

define unknown = GalleryItem("Laura", 1, "didntlaura", "lk10.webp", {"laurarom":True})
define unknown = GalleryItem("Laura", 1, "threesome", "gl tubf10.webp", {"grace":False, "jennmean":True})
define unknown = GalleryItem("Laura", 1, "galleryScene16", "laura bed3.webp")
define unknown = GalleryItem("Laura", 1, "followlaura", "laura br3.webp", {"laurarom":True})
define unknown = GalleryItem("Laura", 1, "galleryScene19", "lfktub2.webp", {"grace":True, "glthreesome":True, "laurarom":True, "daphne":True})
define unknown = GalleryItem("Laura", 1, "badtimelaura", "lneked1.webp")
define unknown = GalleryItem("Laura", 1, "timetraveler", "lauraconvo13.webp")
define unknown = GalleryItem("Laura", 1, "galleryscene24", "Episode 11/glbath3.webp", {"hatelaura":True, "callcory":False})
define unknown = GalleryItem("Laura", 2, "galleryscene25", "Episode 11/lbrtub11.webp")

define unknown = GalleryItem("Jenn", 1, "admitjennsexy", "jenn onknees6.webp")
define unknown = GalleryItem("Jenn", 1, "smart2", "jenn day12.webp", {"jenn":True})
define unknown = GalleryItem("Jenn", 1, "galleryScene14", "jennbr16.webp", {"jennice":False})
define unknown = GalleryItem("Jenn", 1, "galleryScene13", "jlsroom5.webp", {"jenn":True, "kissgrace":True, "jennice":False, "jennpreg":True})
define unknown = GalleryItem("Jenn", 1, "galleryScene15", "jennint18.webp", {"laura":False, "jennpreg":True, "jennice":False})
define unknown = GalleryItem("Jenn", 1, "galleryScene32", "Episode 12/japartment10.webp")

define unknown = GalleryItem("Brittany", 1, "icmi", "b br13.webp", {"grace":True})
define unknown = GalleryItem("Brittany", 1, "galleryScene6", "bdark3.webp", {"bcum":True})
define unknown = GalleryItem("Brittany", 1, "britbangbang", "britbr2.webp")
define unknown = GalleryItem("Brittany", 1, "galleryScene7", "britbed2.webp", {"laurarom":True, "bcum":True})
define unknown = GalleryItem("Brittany", 1, "galleryScene8", "brit br2.webp", {"bbaby":False, "bcum":True})
define unknown = GalleryItem("Brittany", 1, "galleryScene26", "britnotpreg7.webp", {"bcum":False})
define unknown = GalleryItem("Brittany", 1, "galleryScene27", "britroombig4.webp", {"preg":True})
define unknown = GalleryItem("Brittany", 1, "galleryScene28", "backseat.webp", {"brittany":True, "preg":False})
define unknown = GalleryItem("Brittany", 2, "britend", "Episode 12/backalley6.webp", {"preg":True})

define unknown = GalleryItem("Rachel", 1, "gorachel", "rachdown5.webp")
define unknown = GalleryItem("Rachel", 1, "fuckrachel", "rachair6.webp", {"rachdrunk":False})
define unknown = GalleryItem("Rachel", 1, "bullsonparade", "rachel fridge3.webp", {"rachel":True, "rcum":True})
define unknown = GalleryItem("Rachel", 1, "galleryScene18", "rachwall1.webp")
define unknown = GalleryItem("Rachel", 1, "galleryScene34", "Episode 13/rachelhouse18.webp")
define unknown = GalleryItem("Rachel", 1, "rachelnow", "Episode 13/rachelpark12.webp", {"rcum":True})

define unknown = GalleryItem("Other", 1, "pushforward", "haleybed5.webp")
define unknown = GalleryItem("Other", 1, "galleryScene12", "ht13.webp", {"haley":True, "hcum":True})
define unknown = GalleryItem("Other", 1, "galleryScene23", "Episode 11/daphbath11.webp", {"jennmean":True, "callrachel":False})
define unknown = GalleryItem("Other", 1, "galleryScene30", "Episode 12/bethhall9.webp")
define unknown = GalleryItem("Other", 1, "galleryScene31", "Episode 12/hclass19.webp")
define unknown = GalleryItem("Other", 1, "galleryScene36", "Episode 13/tifhome17.webp")



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
