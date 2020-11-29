init python:
    modGame = "{}".format(config.name)
    modGameLink = "https://www.patreon.com/OscarSix"

screen modOutOfDate:
    modal True
    zorder 100
    add "#23272a"

    vbox:
        xcenter 0.5
        ycenter 0.5
        spacing 50

        text "{size=64}A new version of {b}Oscar's [modGame] Mod{/b} is now available.\nClick the Download Now button to download the new update." text_align 0.5 xcenter 0.5 ycenter 0.5
        hbox:
            spacing 100
            xcenter 0.5

            textbutton "Download Now":
                action OpenURL("{}".format(modGameLink))
            textbutton "Ask Me Later":
                action Hide("modOutOfDate")

label before_main_menu:

    if updateChecker():
        show screen modOutOfDate

    return
