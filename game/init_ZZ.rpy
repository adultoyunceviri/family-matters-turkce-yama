

label pfstart:
    $ suppress_overlay = False
    $ quick_menu = True
    show screen quick_menu

    python:
        config.label_overrides.pop("start")
    jump start



label pf_after_load:
    $ suppress_overlay = False
    $ quick_menu = True
    show screen quick_menu

    python:
        config.label_overrides.pop("after_load")
    if renpy.has_label("after_load"):
        call after_load
    return




init 999:




    style say_dialogue:
        color "#FFFFFF"
        outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]



    style say_label:
        outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]



    style input_prompt:
        color "#FFFFFF"
        outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]



    style input:
        color "#FFFFFF"
        outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]




    style quick_button_text:
        background None
        color "#FFFFFF"
        font "MainFont.ttf"
        size int(21)



    style quick_button is default:
        background None
        xpadding 25










    $ quick_menu = True
    $ suppress_overlay = False



screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Touch Screen Gestures") action SetScreenVariable("device", "keyboard")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Yukarı Kaydırma")
        text _("Kayıt Ekranını Açar")

    hbox:
        label _("Aşağı Kaydırma")
        text _("Arayüzü Gizle")

    hbox:
        label _("Sola Kaydırma")
        text _("Atla")

    hbox:
        label _("Sağa Kaydırma")
        text _("Geri Al")

    hbox:
        label _("Yukarı ve Aşağı Kaydırma")
        text _("Otomatik İlerlemeyi Açar Kapatır")






style pref_vbox:
    variant "medium"
    xsize 675



screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0
        textbutton _("{b}Geri") action Rollback()
        textbutton _("{b}Gizle") action HideInterface()
        textbutton _("{b}Atla") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("{b}Oto") action Preference("auto-forward", "toggle")
        textbutton _("{b}Kayıt") action ShowMenu('save')
        textbutton _("{b}Yükle") action ShowMenu('load')
        textbutton _("{b}H.Kayıt") action QuickSave()
        textbutton _("{b}H.Yükle") action QuickLoad()
        textbutton _("{b}Menü") action ShowMenu()




init python:
    config.gestures = { "n" : "game_menu",
                        "s" : "hide_windows",
                        "w" : "rollback",
                        "e" : "skip",
                        "n_s": "toggle_afm"}






screen input(prompt):
    variant "touch"
    style_prefix "input"
    hbox:
        yalign 0.1
        window:
            has vbox:
                xalign gui.dialogue_text_xalign
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"



style input_prompt:
    color "#FFFFFF"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]



style input:
    color "#FFFFFF"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]






default persistent.say_window_alpha = 0.0
default persistent.pref_text_size = 33






screen say(who, what):
    style_prefix "say"

    window:

        if who is not None:

            window:
                background None
                style "namebox"
                text who id "who"

        background Transform(style.window.background, alpha=persistent.say_window_alpha)
        id "window"
        text what id "what" size persistent.pref_text_size

    if not renpy.variant("tv"):
        add SideImage() xalign 0.0 yalign 1.0



screen quick_menu():


    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0
        textbutton _("{b}Geri") action Rollback()
        textbutton _("{b}Gizle") action HideInterface()
        textbutton _("{b}Atla") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("{b}Oto") action Preference("auto-forward", "toggle")
        textbutton _("{b}Kayıt") action ShowMenu('save')
        textbutton _("{b}Yükle") action ShowMenu('load')
        textbutton _("{b}H.Kayıt") action QuickSave()
        textbutton _("{b}H.Yükle") action QuickLoad()
        textbutton _("{b}Menü") action ShowMenu()


init -1 python:

    config.character_id_prefixes.append('namebox')

    renpy.register_style_preference("window", "def", style.window, "background", Image("gui/textbox.png", xalign=0.5, yalign=1.0))
    renpy.register_style_preference("say_label", "trans", style.say_label, "outlines", [ (3, "#111", 0, 0) ])
    renpy.register_style_preference("say_label", "def", style.say_label, "outlines", [ (3, "#111", 0, 0) ])

    renpy.register_style_preference("say_dialogue", "trans", style.say_dialogue, "outlines", [ (3, "#111", 0, 0) ])
    renpy.register_style_preference("say_dialogue", "def", style.say_dialogue, "outlines", [ (3, "#111", 0, 0) ])



screen preferences():
    tag menu


    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))



            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Textbox Opaklığı: %s %%" % (int(persistent.say_window_alpha * 100)))

                    bar value FieldValue(object=persistent, field='say_window_alpha', range=1.0, max_is_zero=False, style=u'slider', offset=0, step=.01)

                    label _("Yazı Boyutu: %s" % (persistent.pref_text_size))

                    bar value FieldValue(object=persistent, field='pref_text_size', range=(gui.text_size * 2), max_is_zero=False, style=u'slider', offset=0, step=1)

                    textbutton _("Sıfırla"):
                        action [SetVariable("persistent.pref_text_size", 33)]

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")



                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
