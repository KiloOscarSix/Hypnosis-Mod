init python:
    modGame = "{}".format(config.name)
    modGameLink = "https://www.patreon.com/OscarSix"

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start("oscarUpdateAlert")

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if main_menu:
            textbutton _("Oscars Gallery") action [ui.callsinnewcontext("galleryNameChange"), ShowMenu("sceneGalleryMenu")]

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)

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
                action Return()

label oscarUpdateAlert:
    if updateChecker():
        call screen modOutOfDate

    jump start
