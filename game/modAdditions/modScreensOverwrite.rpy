# vbox:
#     align(0.28, 0.185)
#     text "{color=#fff}Save Name:{/color}"
#     input:
#         yalign 0.05
#         value VariableInputValue("save_name")

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:
            textbutton _("Mod Options") action Show("modOptions")

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if main_menu:
            textbutton _("Oscar's Gallery") action [ui.callsinnewcontext("galleryNameChange"), Show("sceneGalleryMenu")]

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

screen save():

    tag menu

    use file_slots(_("Save"))
    
    vbox:
        align(0.28, 0.185)
        text "{color=#fff}Save Name:{/color}"
        input:
            yalign 0.05
            value VariableInputValue("save_name")
