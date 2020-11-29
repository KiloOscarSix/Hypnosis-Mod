init python:
    gr = "{color=#0f0}"
    red = "{color=#f00}"
    blue = "{color=#00f}"
    BoyfriendPath = "{color=#0f0}[Boyfriend Path]"
    GoodBoyfriendPath = "{color=#0f0}[Boyfriend/Good Path]"
    BadassPath = "{color=#0f0}[Badass Path]"

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("changeIngameNames") text_style "modTextButtonHeader"

        textbutton "Change Gallery Names" action ui.callsinnewcontext("changeGalleryNames") text_style "modTextButtonHeader"

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)

label changeGalleryNames:
    python:
        persistent.galleryName = renpy.input("What's your name?", default="Kyle").strip()
        persistent.galleryNickname = renpy.input("What's your nickname?", default="Banana Man").strip()
    menu:
        mod "Do the girls call you Master/Daddy?"
        "Yes":
            $ persistent.galleryMaster = True
        "No":
            $ persistent.galleryMaster = False
    mod "Gallery names successful changed"
    return

label changeIngameNames:
    mod "Make sure to do this in the save you wish to change names for."
    python:
        persistent.name = name = renpy.input("What's your name?", default="Kyle").strip()
        persistent.nickname = nickname = renpy.input("What's your nickname?", default="Banana Man").strip()
    mod "Names successful changed"
    return
