init python:
    galleryCharacter = ""
    galleryPageNumber = 1

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1
        return

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1
        return

    sceneGalleryMenuDict = {
    "galleryMenu": [
    ["Leah", "/images/leah hotel1.webp"],
    ["Ashley", "/images/a room3.webp"],
    ["Grace", "/images/grace bowling1.webp"],
    ["Laura", "/images/blshowdown1.webp"],
    ["Jenn", "/images/jenn outside1.webp"],
    ["Brittany", "/images/brit1.webp"],
    ["Rachel", "/images/rachall6.webp"],
    ["Other", "/images/hal5.webp"],
    ],
    "Leah": {
    1: [
    ["thursdaynight", {"chooseleah":True}, "/images/leah bjbellypre.webp"], # 4852
    ["nextstep", {"ashleyyes":True}, "/images/leah hotel4.webp"], # 5541
    ["galleryScene3", {"both":True}, "/images/al cg8.webp"], # 13954
    ["galleryScene17", {}, "/images/leahbed1.webp"], # 19435
    ["dols", {}, "/images/leahbs.webp"], # 19697
    ["ml", {"brittany":True}, "/images/lbr2.webp"],
    ["galleryScene5", {}, "/images/ashdown2.webp"],
    ["galleryscene21", {"both":True, "beth":True}, "/images/Episode 11/alashleysroom5.webp"],
    ],
    },
    "Ashley": {
    1: [
    ["galleryScene1", {}, "/images/ashley tf1.webp"], # 2950
    ["galleryScene4", {}, "/images/al beda20.webp"], # 6846
    ["bulletproof", {"fashley":True, "chooseleah":True}, "/images/astripes8.webp"], # 12172
    ["galleryScene3", {"both":True}, "/images/al cg8.webp"], # 13954
    ["galleryScene2", {"chooseleah":True, "both":True}, "/images/a bs3.webp"], # 14158
    ["galleryScene5", {"preg":True}, "/images/ashdown2.webp"],
    ["galleryscene21", {"both":True, "beth":True}, "/images/Episode 11/alashleysroom5.webp"],
    ["galleryScene29", {}, "/images/Episode 12/ashcuddle4.webp"],
    ],
    },
    "Grace": {
    1: [
    ["threesome", {"name":persistent.galleryName, "nickname":persistent.nickname, "grace":False, "jennmean":True}, "/images/gl tubf10.webp"], # 16741
    ["throwintowel", {"name":persistent.galleryName, "nickname":persistent.nickname}, "/images/grace couchstand9.webp"], # 18211
    ["galleryScene9", {"name":persistent.galleryName, "nickname":persistent.nickname}, "/images/grace out7.webp"], # 27292
    ["galleryScene19", {"name":persistent.galleryName, "nickname":persistent.nickname, "grace":True, "glthreesome":True, "laurarom":True, "daphne":True}, "/images/lfktub2.webp"], # 30902
    ["galleryScene11", {"name":persistent.galleryName, "nickname":persistent.nickname, "laura":False, "daphne":True}, "/images/gracebr3.webp"], # 32280
    ["sneakygrace", {"name":persistent.galleryName, "nickname":persistent.nickname, "glthreesome":True, "gcum":True}, "/images/gcruise15.webp"],
    ["galleryscene24", {"hatelaura":True, "callcory":False}, "/images/Episode 11/glbath3.webp"],
    ],
    },
    "Laura": {
    1: [
    ["didntlaura", {"name":persistent.galleryName, "nickname":persistent.nickname, "laurarom":True}, "/images/lk10.webp"], # 15153
    ["threesome", {"name":persistent.galleryName, "nickname":persistent.nickname, "grace":False, "jennmean":True}, "/images/gl tubf10.webp"], # 16741
    ["galleryScene16", {"name":persistent.galleryName, "nickname":persistent.nickname}, "/images/laura bed3.webp"], # 17023
    ["followlaura", {"name":persistent.galleryName, "nickname":persistent.nickname, "laurarom":True}, "/images/laura br3.webp"], # 25773
    ["galleryScene19", {"name":persistent.galleryName, "nickname":persistent.nickname, "grace":True, "glthreesome":True, "laurarom":True, "daphne":True}, "/images/lfktub2.webp"], # 30902
    ["badtimelaura", {"name":persistent.galleryName, "nickname":persistent.nickname}, "/images/lneked1.webp"], # 33294
    ["timetraveler", {"name":persistent.galleryName, "nickname":persistent.nickname}, "/images/lauraconvo13.webp"], # 33408
    ["galleryscene24", {"hatelaura":True, "callcory":False}, "/images/Episode 11/glbath3.webp"],
    ],
    2: [
    ["galleryscene25", {}, "/images/Episode 11/lbrtub11.webp"],
    ],
    },
    "Jenn": {
    1: [
    ["admitjennsexy", {"name":persistent.galleryName, "nickname":persistent.nickname}, "/images/jenn onknees6.webp"], # 3865
    ["smart2", {"name":persistent.galleryName, "nickname":persistent.nickname, "jenn":True}, "/images/jenn day12.webp"], # 9068
    ["galleryScene14", {"name":persistent.galleryName, "nickname":persistent.nickname, "jennice":False}, "/images/jennbr16.webp"], # 23249
    ["galleryScene13", {"name":persistent.galleryName, "nickname":persistent.nickname, "jennice":False, "jennpreg":True}, "/images/jlsroom5.webp"], # 27825
    ["galleryScene15", {"name":persistent.galleryName, "nickname":persistent.nickname, "laura":False, "jennpreg":True, "jennice":False}, "/images/jennint18.webp"], # 32735
    ["galleryScene32", {}, "/images/Episode 12/japartment10.webp"],
    ],
    },
    "Brittany": {
    1: [
    ["icmi", {"name":persistent.galleryName, "nickname":persistent.nickname, "grace":True}, "/images/b br13.webp"], # 20499
    ["galleryScene6", {"bcum":True}, "/images/bdark3.webp"], # 21089
    ["britbangbang", {}, "/images/britbr2.webp"], # 25996
    ["galleryScene7", {"laurarom":True, "bcum":True}, "/images/britbed2.webp"], # 31465
    ["galleryScene8", {"bbaby":False, "bcum":True}, "/images/brit br2.webp"], # 34260
    ["galleryScene26", {"bcum":False}, "/images/britnotpreg7.webp"], # Needs image
    ["galleryScene27", {"preg":True}, "/images/britroombig4.webp"], # 34260
    ["galleryScene28", {"brittany":True, "preg":False}, "/images/backseat.webp"], # 34260
    ],
    2: [
    ["britend", {"preg":True}, "/images/Episode 12/backalley6.webp"],
    ],
    },
    "Rachel": {
    1: [
    ["gorachel", {"name":persistent.galleryName, "nickname":persistent.nickname}, "/images/rachdown5.webp"], # 22813
    ["fuckrachel", {"name":persistent.galleryName, "nickname":persistent.nickname, "rachdrunk":False}, "/images/rachair6.webp"], # 24150
    ["bullsonparade", {"name":persistent.galleryName, "nickname":persistent.nickname, "rachel":True, "rcum":True}, "/images/rachel fridge3.webp"], # 26743
    ["galleryScene18", {"name":persistent.galleryName, "nickname":persistent.nickname}, "/images/rachwall1.webp"], # 33154
    ],
    },
    "Other": {
    1: [
    ["pushforward", {}, "/images/haleybed5.webp"], # 24366
    ["galleryScene12", {"haley":True, "hcum":True}, "/images/ht13.webp"],
    ["galleryscene23", {"jennmean":True, "callrachel":False}, "/images/Episode 11/daphbath11.webp"],
    ["galleryScene30", {}, "/images/Episode 12/bethhall9.webp"],
    ["galleryScene31", {}, "/images/Episode 12/hclass19.webp"],
    ],
    },
    }

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
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "galleryHeader"
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
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action ShowMenu("sceneCharacterMenu"), Hide("sceneGalleryMenu"), SetVariable("galleryCharacter", i[0])
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "galleryBody"
                    xcenter 0.5

screen sceneCharacterMenu():
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "galleryHeader"
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
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "galleryBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"name":persistent.galleryName, "nickname":persistent.nickname, "master":persistent.galleryMaster}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)
