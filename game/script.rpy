define perv = Character('Çeviri Ekibi', color="#000000")
###CHARACTERS###
define bro = ""
define b = Character ("[bro]", color="#808080")
define v = Character("Vicky", color="#da70d6")
define vSide = Character("Vicky", color="#da70d6", image = "vicky", window_left_padding=25)
define n = Character("Nicole", color="#1e90ff")
define nSide = Character("Nicole", color="#1e90ff", image = "nicole", window_left_padding=25)
define j = Character("Julie", color="#228b22")
define jSide = Character("Julie", color="#228b22", image = "julie", window_left_padding=25)
define s = Character("Scarlett", color="#DC143C")
define m = Character("[momUpper]", color="#DAA520")
define c = Character("Koordinatör", color="#2f4f4f")
define rocco = Character("?????", color="#201345")
define nacho = Character("?????", color="#ff6e00")


###SIDE_IMAGES###
image side vicky initial = Image("images/faces/vicky/vicky_init.png", xoffset=-15, yoffset=15)
image side nicole initial = Image("images/faces/nicole/nicole_init.png", xoffset=-20, yoffset=20)
image side julie initial = Image("images/faces/julie/julie_init.png", xoffset=-15, yoffset=5)

###INCEST_SECTION###
init:
    $ incestEnabled = 0
    $ family = "ev halkı"
    $ mom = "ev sahibesi"
    $ momUpper = "EV SAHİBESİ"
    $ sis = "ev arkadaşı"
    $ son = "tenant"
    $ brother = "ev arkadaşı"
    $ siblings = "oda arkadaşı"
    $ children = "tenants"
    $ father = "ev sahibi"

###VARIABLES###
    $ kissFlash = Fade(.25, 0, .75, color="#FF69B4")
    $ kissFlashLong = Fade(.25, 1.0, 2.0, color="#FF69B4")
    $ cumFlash = Fade (.25, 0, .75, color="#FFFFFF")
    $ cumFlashLong = Fade (.25, 1.0, 2.0, color="#FFFFFF")
    $ killFlash = Fade (.25, 0, .75, color="#FF0000")
    $ config.rollback_enabled = True


#SPLASHSCREEN###
label splashscreen3:
    python:
        _preferences.set_volume('music', 0.5)
        renpy.restart_interaction()
    scene black
    with Pause(2)
    show disc with Dissolve (1.0)
    with Pause(4)
    hide disc with Dissolve (1.0)
    with Pause(2)
    show pervLogo at truecenter with Dissolve (1.0)
    with Pause(2)
    hide pervLogo with Dissolve (1.0)
    with Pause(1)
    return

###IMAGES###
image pervLogo = "res/perv.png"
image title = "res/title.png"
image disc = "res/disclaimer.png"

image gOver = "res/go.png"
image gOver1 = "res/go1.png"
image gOver2 = "res/go2.png"
image gOver3 = "res/go3.png"

image bg enterName = "images/ep1/0ps.png"
image bg 1ps = "images/ep1/1ps.png"
image bg 2ps = "images/ep1/2ps.png"
image bg 3ps = "images/ep1/3ps.png"
image bg 4ps = "images/ep1/4ps.png"
image bg 5c1ps = "images/ep1/5c1ps.png"
image bg 5c2ps = "images/ep1/5c2ps.png"
image bg 6ps = "images/ep1/6ps.png"
image bg 7ps = "images/ep1/7ps.png"
image bg 8ps = "images/ep1/8ps.png"
image bg 9ps = "images/ep1/9ps.png"
image bg 10ps = "images/ep1/10ps.png"
image bg 11ps = "images/ep1/11ps.png"
image bg 12ps = "images/ep1/12ps.png"
image bg 13ps = "images/ep1/13ps.png"
image bg 14ps = "images/ep1/14ps.png"
image bg 15ps = "images/ep1/15ps.png"
image bg 16ps = "images/ep1/16ps.png"
image bg 17ps = "images/ep1/17ps.png"
image bg 18ps = "images/ep1/18ps.png"
image bg 19ps = "images/ep1/19ps.png"
image bg 20ps = "images/ep1/20ps.png"
image bg 21ps = "images/ep1/21ps.png"
image bg 21_ps = "images/ep1/21_ps.png"
image bg 22ps = "images/ep1/22ps.png"
image bg 23ps = "images/ep1/23ps.png"
image bg 24ps = "images/ep1/24ps.png"
image bg 25ps = "images/ep1/25ps.png"

image bg Hallway1ps = "images/ep1/Hallway1ps.png"
image bg Hallway2c3ps = "images/ep1/Hallway2c3ps.png"
image bg Hallway2ps = "images/ep1/Hallway2ps.png"
image bg h00 = "images/ep1/h00.png"
image bg h01 = "images/ep1/h01.png"
image bg h02 = "images/ep1/h02.png"
image bg h03 = "images/ep1/h03.png"
image bg h04 = "images/ep1/h04.png"
image bg h05 = "images/ep1/h05.png"
image bg h10 = "images/ep1/h10.png"
image bg h11 = "images/ep1/h11.png"
image bg h12 = "images/ep1/h12.png"
image bg h13 = "images/ep1/h13.png"
image bg h14 = "images/ep1/h14.png"
image bg h20 = "images/ep1/h20.png"
image bg h21 = "images/ep1/h21.png"
image bg h22 = "images/ep1/h22.png"
image bg h23 = "images/ep1/h23.png"
image bg h30 = "images/ep1/h30.png"
image bg h31 = "images/ep1/h31.png"
image bg h32 = "images/ep1/h32.png"
image bg h40 = "images/ep1/h40.png"
image bg h41 = "images/ep1/h41.png"
image bg h50 = "images/ep1/h50.png"
image bg Hallway4c4ps = "images/ep1/Hallway4c4ps.png"
image bg Hallway5ps = "images/ep1/Hallway5ps.png"
image bg Hallway6ps = "images/ep1/Hallway6ps.png"

image bg Airport2 = "images/ep1/Airport2.png"
image bg Airport3 = "images/ep1/Airport3.png"
image bg Airport4 = "images/ep1/Airport4.png"
image bg Airport4Bag = "images/ep1/Airport4Bag.png"
image bg Parking1c1ps = "images/ep1/Parking1c1ps.png"
image bg Parking1c2ps = "images/ep1/Parking1c2ps.png"
image bg Parking2ps = "images/ep1/Parking2ps.png"
image bg Parking3ps = "images/ep1/Parking3ps.png"

image bg athome1c1ps = "images/ep1/athome1c1ps.png"
image bg athome1c3ps = "images/ep1/athome1c3ps.png"
image bg athome2c3_ = "images/ep1/athome2c3_.png"
image bg athome2c3ps = "images/ep1/athome2c3ps.png"
image bg athome2c4ps = "images/ep1/athome2c4ps.png"
image bg athome4c4ps = "images/ep1/athome4c4ps.png"
image bg athome5c6ps = "images/ep1/athome5c6ps.png"
image bg athome6c2ps = "images/ep1/athome6c2ps.png"
image bg athome7c1ps = "images/ep1/atHome7c1ps.png"
image bg athome8c2ps = "images/ep1/athome8c2ps.png"
image bg athome9c6ps = "images/ep1/athome9c6ps.png"
image bg athome10c5ps = "images/ep1/athome10c5ps.png"

image bg fclubc1ps = "images/ep1/fclubc1ps.png"
image bg fclubc1psarms1 = "images/ep1/fclubc1psarms1.png"
image bg fclubc1psarms1 = "images/ep1/fclubc1psarms1.png"
image bg fclubc1psarms2 = "images/ep1/fclubc1psarms2.png"
image bg fclubc1psarms3 = "images/ep1/fclubc1psarms3.png"
image bg fclubc1pslegs1 = "images/ep1/fclubc1pslegs1.png"
image bg fclubc1pslegs2 = "images/ep1/fclubc1pslegs2.png"
image bg fclubc1pslegs3 = "images/ep1/fclubc1pslegs3.png"
image bg fclubc1pstorso1 = "images/ep1/fclubc1pstorso1.png"
image bg fclubc1pstorso2 = "images/ep1/fclubc1pstorso2.png"
image bg fclubc1pstorso3 = "images/ep1/fclubc1pstorso3.png"
image bg fclubc2c1ps = "images/ep1/fclub2c1ps.png"
image bg fclubc3c2ps = "images/ep1/fClub3c2ps.png"

image bg athome11c1ps = "images/ep1/athome11c1ps.png"
image bg athome12c1ps = "images/ep1/athome12c1ps.png"
image bg athome14c1ps = "images/ep1/athome14c1ps.png"
image bg athome15c1ps = "images/ep1/athome15c1ps.png"
image bg athome16c1ps = "images/ep1/athome16c1ps.png"
image bg athome17c1ps = "images/ep1/athome17c1ps.png"
image bg athome18c2ps = "images/ep1/athome18c2ps.png"
image bg athome19c1ps = "images/ep1/athome19c1ps.png"

###SCRIPT###
label start:
    stop music fadeout 2.0
    window hide
    scene black with Dissolve (2.0)
    $ renpy.pause(2.0, hard=True)
    scene bg enterName with Dissolve (2.0)
    call nameSelection from _call_nameSelection
    call incestModifier from _call_incestModifier
    jump episode1
    $ renpy.pause()
    return

label nameSelection:
    $ renpy.pause()
    $ bro = renpy.input("Lütfen istediğiniz adı girip 'Enter' tuşuna basın.")
    $ bro = bro.strip()
    return

label incestModifier:
        perv "Hello there, [bro]!"
        perv "During the game it is possible to go back by scrolling mouse-wheel upwards"
        perv "To hide the interface press mouse-wheel button"
        perv "Right click allows switching between the game and the menu"
        perv "Now it's time to give a name for some other characters of this game..."
        extend "Of course if you want to..."
        $ renpy.pause()

        perv "Default name of the first character is Julie({color=#228b22}housemate{/color})"
        perv "Would you like to change it ?"
        menu:
            "Yes":
                $ sis = renpy.input("Lütfen istediğiniz adı girip 'Enter' tuşuna basın...")
                $ sis = sis.strip()
                $ sis = sis.lower()
                perv "Now the name of the first character is Julie({color=#228b22}%(sis)s{/color})"
                if (sis == "sis") or (sis == "sister"):
                    $ incestEnabled = 1
                    perv "Excellent choices made %(incestEnabled)s out of 2"
                    extend "\nWay to GO ! :)"
                else:
                    perv "Got it..."
                    $ incestEnabled = 0
            "No":
                $ incestEnabled = 0
                perv "As you wish.."
                perv "Name of the first character remains Julie({color=#228b22}%(sis)s{/color})"

        perv "Almost there..One more left.."
        perv "Default name of the second character is Roxanne({color=#DAA520}landlady{/color})"
        perv "Would you like to change it ?"
        menu:
            "Yes":
                $ mom = renpy.input("Lütfen istediğiniz adı girip 'Enter' tuşuna basın..")
                $ mom = mom.strip()
                $ mom = mom.lower()
                perv "Now the name of the second character is Roxanne({color=#DAA520}%(mom)s{/color})"
                if (mom == "mom") or (mom == "mother"):
                    $ incestEnabled += 1
                    perv "Excellent choices made %(incestEnabled)s out of 2"
                    if (incestEnabled == 2):
                        extend "\nMy Congratulations ! You are awesome :)"
                        perv "Enjoy the game..."
                    else:
                        perv "Something wrong with the name of the first character.."
                        extend "\nplease consider going back using mousewheel and rename to something more appropriate.."
                        $ renpy.pause()
                        $ renpy.pause()
                        $ renpy.pause()
                        perv "Okay.."
                        $ incestEnabled = 0
                else:
                    if (incestEnabled == 1):
                        perv "Half of the way have been passed already..."
                        extend "\nplease consider renaming last character to something more appropriate..."
                        $ renpy.pause()
                        $ renpy.pause()
                        $ renpy.pause()
                        perv "Okay.."
                        $ incestEnabled = 0
                    else:
                        perv "Got it..."
                        $ incestEnabled = 0
            "No":
                if (incestEnabled == 1):
                    perv "Half of the way have been passed already..."
                    extend "\nplease consider renaming last character to something more appropriate..."
                    $ renpy.pause()
                    $ renpy.pause()
                    $ renpy.pause()
                $ incestEnabled = 0
                perv "As you wish.."
                perv "Name of the second character remains Roxanne({color=#DAA520}%(mom)s{/color})"
                perv "Have fun !"

        if (incestEnabled == 2):
            $ family = "family"
            $ mom = "mom"
            $ momUpper = "MOM"
            $ sis = "sister"
            $ son = "son"
            $ daughter = "daughter"
            $ brother = "brother"
            $ siblings = "siblings"
            $ children = "children"
            $ father = "father"
        else:
            $ family = "household"
            $ mom = "landlady"
            $ momUpper = "LANDLADY"
            $ sis = "housemate"
            $ son = "tenant"
            $ daughter = "tenant"
            $ brother = "housemate"
            $ siblings = "roommates"
            $ children = "tenants"
            $ father = "landlord"

        return
####################################################EPISODE_1##################################################

label episode1:

    scene black with Dissolve (2.0)
    $ renpy.pause()
    b "That was wonderful..You are an amazing girl Vicky.."
    $ renpy.pause()
    scene bg 1ps with Dissolve(2.0)
    $ renpy.pause()
    v "Thank you honey..I'm glad you liked it.."
    $ renpy.pause()
    v "Is it just me or something bothers you ?"
    b "Why ?"
    v "I don't know..You seem a little concerned today..We girls always notice these things.."
    b "Maybe.."
    v "It's okay..you can tell me what happened.."
    $ renpy.pause()
    b "Nevermind..I'm okay thanks.."
    v "Okay..So.."
    scene bg 2ps with fade
    $ renpy.pause()
    v "I guess we still have some time don't we.."
    $ renpy.pause()
    v "Ahm..How about.."
    scene bg 3ps with Dissolve(1.5)
    $ renpy.pause()
    "*Vicky's foot gently touches your dick*"
    v "We make a little quickie.."
    $ renpy.pause()
    b "Interesting proposal..\nToo bad I'm out of 'Two Pump Champions League'.."
    scene bg 2ps with Dissolve(1.0)
    v "Come on..it is not what I mean.."
    b "I know.."
    $ renpy.pause()
    v "Well..I've run out of options..\nDo you have something on your mind ?"

    $ ep1shower = 0
    $ ep1kiss = 0
    $ ep1comeHere = 0

    scene bg 3ps with Dissolve(1.0)

    menu ep1vicky:
        "Kiss" if ep1kiss == 0:
            $ ep1kiss += 1
            b "How about a farewell kiss ?"
            scene bg 2ps with Dissolve(1.0)
            v "You never give up on it, do you ?"
            b "Who knows..maybe you've changed your mind.."
            v "[bro].."
            b "I mean..I totally agree with 'No glove - no love' thing..\nbut a kiss.."
            v "It is not a thing, these are my rules [bro]..my principles.."
            v "It's not something you change everyday.."
            b "Okay..I'm sorry..I didn't mean to offend you.."
            v "Thank you.."
            jump ep1vicky
        "Shower" if ep1shower == 0:
            $ ep1shower += 1
            b "Don't waste your time.."
            if ep1kiss == 0:
                scene bg 2ps with Dissolve(1.0)
            b "If you want you can go and take a shower..you can save yourself some time..and..feel free to leave earlier.."
            v "Oh honey..it is so nice of you.."
            scene bg 1ps with fade
            $ renpy.pause()
            b "Oh..?"
            v "I know it's..kind of..unprofessional..but.."
            v "You are not like..other..clients.."
            b "What makes you think so ?"
            v "I don't know..I just feel it.."
            v "If I only knew more about you.."
            b "I don't think this is a good idea.."
            v "Why not ? We still have some time anyway.."
            jump revelation
        "Come here" if ep1comeHere == 0:
            $ ep1comeHere += 1
            b "Come closer.."
            if ep1kiss == 0:
                scene bg 2ps with Dissolve(1.0)
            b "Please lie down next to me..like you did"
            v "Like this..?"
            scene bg 1ps with fade
            $ renpy.pause()
            b "Yes..thank you.."
            b "I like your presence..it is good to have someone next to you.."
            v "Sure.."
            b "It pacifies and calms me down when you are around.."
            v "You know..I just realized how little I know about you.."
            b "Maybe it's not so bad..the less you know the less you feel..You don't get attached to anyone.."
            v "But [bro]..you already did..You just said that.."
            b "I know..and I shouldn't have.."
            v "We might not have other time for this..but we have it now.."
            b "What are you talking about ?"
            $ renpy.pause()
            jump revelation

    label revelation:
        v "Please tell me more about you..\nWhat do you do ?"
        b "Why do you want to find it out so eagerly ?"
        v "Well..you know exactly what I do for living.."
        b "It doesn't count.."
        v "Okay..feel free to ask me any personal question..\nI promise to answer honestly.."
        b "It is not serious..I won't be able to check if it's true anyway.."
        v "Are you saying that you don't trust me..?"
        b "No. I do trust you..probably more than anyone else in this city.."
        v "So why not telling me ?"
        b "Okay..I provide not quite legal services so to say..just like you.."
        v "Really.. ?"
        b "I mean they are not legal..I'm not providing Escort service"
        v "Why not ? You are such a handsome.."
        b "Are you fucking with me..?"
        v "I'm sorry..just kidding !"
        v "Tell me more ! What kind of services ? What makes you doing it ?"
        b "It is not fair. You are asking too many questions..yet answered none by the way"
        v "Okay. What do you want to know about me ?"
        $ renpy.pause()

        $ ep1m2r = 0
        menu ep1m2:
            "Are they real ?" if ep1m2r == 0:
                $ ep1m2r += 1
                b "I was wondering if your breasts are real.."
                v "Are you serious ?"
                b "Yeah.."
                v "Of course they real..I thought it is always easy to differ fake ones.."
                b "Just wanted to make sure.."
                v "Right.."
                jump ep1m2
            "Why Escort ?":
                b "What made a girl like you to come into this business ?"
        v "That is a good question..I had a very difficult childhood..\nOr I should better say I did not have one.."
        v "I'm an orphan so I had nobody to care about me..The orphanage doesn't count - that is different.."
        b "I'm sorry.."
        v "That is okay. There was a good side of it. Later I realized that I don't have to care about anybody either.."
        v "The life in orphanage taught me to rely on myself only..And I'm thankful for that...."
        v "After the graduation I had to decide what to do next..I wanted to study in the university but I had no money, so I had to find a job to pay the bills, you know.."
        b "So you started to provide Escort services right away ?"
        v "No. At first I worked in a cafe. Salary was small but at least I started to make some money.."
        v "Some time later I noticed an open vacancy of waitress at the most prestigious restaurant in this city"
        v "I successfully passed the interview and was hired..but even working at that place I knew that it will take a long time before I gather all needed money for my study.."
        b "I see.."
        $ renpy.pause()
        v "One day a gorgeous woman visited the restaurant, I happened to serve the food for her. We started talking and..I'm not going into details but.."
        extend "\nEventually she helped me to start working in Escort.."
        b "Interesting.."
        extend "What about university ?"
        v "Of course I'm not planning to do Escort for the rest of my life.."
        extend "I almost gathered the whole sum to pay for the university.."
        extend "\nBut until then I have to work this way.."
        v "Okey, your turn.."
        b "It is funny but we are pretty much alike..\nI had to start working very early..when I barely finished the school.."
        b "The city I grew up in was small..so.."
        extend "\nFinding a job for a guy without an education was a hard task.."
        extend "\nImpossible if you wanted to make decent amount of money legaly.."
        b "There was only one option.."
        extend "Illegal one.."
        extend "\nSo I ended up in this city.."
        v "Wow..I even didn't know that we have so much in common.."
        b "Yeah..I guess..But.."
        extend "With an exception that I have people who cared about me.."
        extend "\nThey still count on me..and I can't leave them.."
        b "Because no one will help them except me.."
        extend "But all I can do to help is send them money.."
        v "I don't quite understand..\nAnd probably never will, I've never been in such situation.."
        b "Just imagine that there are some people..which you really care about.."
        extend "\nAnd now it is your responsibility to help them and provide those people safety.."
        b "Unfortunately.."
        extend "the only way to do this and be closer to them.."
        extend "\nIs by staying away from them.."
        b "Irony is a heartless bitch, isn't it.."
        v "These people you're talking about.."
        extend "Who are they ?"
        extend "\nIs this your [family] ?"
        b "Okay that is enough for today.."
        extend "Get up.."
        scene bg 4ps with fade
        $ renpy.pause()
        v "Oh..?"
        b "I've already said to much.."
        extend ""
        v "I'm sorry..I didn't want to.."
        b "Vicky I don't want to be rude but.."
        extend "\nYou had better take a shower, and in the meanwhile I'll call you a taxi"
        v "Okay..Thank you..If you want you can join me in the shower.."
        b ".."
        v "Fine.."
        $ renpy.pause()
        scene black with Dissolve (1.5)
        $ renpy.pause()
        b "Hey Vicky.."
        extend "about our further meetings.."
        v "Yes..?"
        scene bg 5c2ps with Dissolve (1.5)
        $ renpy.pause()
        b "I know that I've paid you in advance for few dates..but.."
        scene bg 5c1ps with fade
        $ renpy.pause()
        v "By the way you still owe me 100$ for my lingerie !"
        b "What ?"
        v "I can't find my red panties.."
        extend "The last time they were on my was.."
        extend "\nWhen we had sex in your car.."
        b "Yes..I remember that.."
        extend "You can take the money from the advance.."
        v "We didn't finish it that day.."
        extend "\nDo you remember what happened next ?"
        b "Not really.."
        v "You left in a hurry with my panties in your car because of an urgent call from work !"
        b "Oh.."
        v "Do you always leave girls without panties in the center of the city..?"
        extend " Or it's just me that lucky..?"
        b "Well.."
        extend "From the other hand I bet you didn't have problems catching a cab, did you ?"
        v "Asshole..)"
        b "Okay..I'm asshole, but it is not about that right now.."
        v "What is it about ?"
        $ renpy.pause()
        b "It is about our meetings..The situation is changed..so"
        scene bg 6ps with fade
        $ renpy.pause()
        b "For a while we should stop.."
        scene bg 7ps
        "*{i}{b}PHONE RINGING{/b}{/i}*"
        $ renpy.pause()
        scene bg 5c1ps with fade
        v "Who is calling this late..? Is this from your work..?"
        $ renpy.pause()
        b "I'm sorry Vicky..it is extremely important call I must answer..\nWould you please.."
        v "Oh don't worry honey I'm leaving..I'll be in the shower.."
        b "Thank you.."
        scene bg 7ps with fade
        jump ep1phone
        $ renpy.pause()
        return

    screen phoneDrawer1:
        imagemap:
            ground "images/ep1/7ps.png"
            hotspot (680, 608, 195, 123) clicked Return ("phone") hovered ShowTransient("imgHider", img="images/ep1/8ps.png") unhovered Hide("imgHider")
            hotspot (336, 774, 376, 263) clicked Return ("drawer") hovered ShowTransient("imgHider", img="images/ep1/9ps.png") unhovered Hide("imgHider")

    screen imgHider(img):
        add img pos (0,0)

    label ep1phone:

        call screen phoneDrawer1
        $ result = _return
        if result == "phone":
            jump coord1
        if result == "drawer":
            jump ep1dnt
        return

    screen phoneDrawer2:
        imagemap:
            ground "images/ep1/10ps.png"
            hotspot (680, 608, 195, 123) clicked Return ("phone") hovered ShowTransient("imgHider", img="images/ep1/12ps.png") unhovered Hide("imgHider")
            hotspot (172,769,420,2483) clicked Return ("stuff") hovered ShowTransient("imgHider", img="images/ep1/11ps.png") unhovered Hide("imgHider")

    label ep1dnt:
        scene bg 10ps with dissolve
        call screen phoneDrawer2
        $ result = _return
        if result == "phone":
            scene bg 7ps with dissolve
            jump coord1
        if result == "stuff":
            b "{i}I don't need this right now..{/i}"
            jump idnt
        return

    screen phoneDrawer3:
        imagemap:
            ground "images/ep1/7ps.png"
            hotspot (680, 608, 195, 123) clicked Return ("phone") hovered ShowTransient("imgHider", img="images/ep1/8ps.png") unhovered Hide("imgHider")

    label idnt:
        scene 7ps with dissolve
        call screen phoneDrawer3
        $ result = _return
        if result == "phone":
            jump coord1
        return

    screen ep1coord:
        imagemap:
            ground "images/ep1/13ps.png"
            hotspot (795, 577, 44, 60) clicked Return ("coord") hovered ShowTransient("imgHider", img="images/ep1/14ps.png") unhovered Hide("imgHider")

    screen ep1stuff:
        imagemap:
            ground "images/ep1/19ps.png"
            hotspot (336, 774, 376, 263) clicked Return ("drawer") hovered ShowTransient("imgHider", img="images/ep1/20ps.png") unhovered Hide("imgHider")

    screen ep1stuff2:
        imagemap:
            ground "images/ep1/21ps.png"
            hotspot (172,769,420,2483) clicked Return ("stuff") hovered ShowTransient("imgHider", img="images/ep1/22ps.png") unhovered Hide("imgHider")

    label coord1:
        scene bg 13ps with fade
        $ renpy.pause()
        b "{i}Better not to make them wait..{/i}"
        call screen ep1coord

        scene black with Dissolve (1.0)
        $ renpy.pause()
        $ renpy.notify ("10 dakika sonra..")
        $ renpy.pause()
        scene bg 15ps with Dissolve (1.5)
        $ renpy.pause()
        b "How bad is it..?"
        c "It is hard to tell right now.."
        extend "\nAll we know by this time is that 'Big guys' decided to change the 'chips on the gaming table'.."
        scene bg 16ps with fade
        $ renpy.pause()
        c "It is directly related to our business. That is why general meeting has been announced.."
        extend "The Boss demands everyone's presence because he will leave the city tomorrow for negotiations"
        c "And there is a high possibility that soon new guys will control this city.."
        b "I understand..But I asked for this day off beforehand.."
        extend "I need to take care about some things.."
        c "You know there is no such term as 'vacation' in our business..Don't you ?"
        scene bg 17ps with fade
        $ renpy.pause()
        b "Of course I know but this is just one day.."
        c "And this is just a {b}general meeting{/b}.."
        extend "\nLook..I know that you never let us down.."
        extend "\nBut if you won't come  you can be sure that it is your first time.."
        b "Even so..?"
        b "Can you at least tell me how long will it take ?"
        scene bg 18ps with fade
        $ renpy.pause()
        c "I don't know..Listen I'm not going to persuade you.."
        extend "\nI'm not your babysitter and it is not a phone call talk either.."
        v "[bro].."
        b "{i}Talking to Vicky:{/i} Just a second.."
        v "I just wanted.."
        c "Everyone who won't come will be under suspicion.."
        v "To ask about.."
        b "{i}Talking to Vicky:{/i} Please wait few minutes.."
        v "There is a car waiting for me.."
        c "Your absence will draw an attention.."
        extend "\nWe have information that some of our guys have been compromised.."
        extend "\nI genuinely believe you are not one of them.."
        extend "Am I right ?"
        v "I guess next time as usual..?"
        b "No.."
        c "No ?!"
        v "No ?!"
        b "I mean yes..of course.."
        c "Good.."
        extend "\nI don't know what things you have to take care about.."
        extend "But I'm sure they aren't that important than this one.."
        extend "\nSo listen carefully.."
        v "Okay..don't bother seeing me off.."
        extend "\nI have the keys.."
        extend "bye honey.."
        "{i}Vicky leaves..{/i}"
        scene bg 19ps with fade
        $ renpy.pause()
        c "Take the car, take the 'stuff' and be at the place in half an hour.."
        extend "\nI told you everything you need to know.."
        extend "\nDecide for yourself.."
        "{i}{b}END OF CALL{/b}{/i}"
        $ renpy.pause()
        b "{i}Damn it !{/i}"
        call screen ep1stuff
        scene bg 21ps with dissolve
        call screen ep1stuff2
        scene bg 21_ps
        $ renpy.pause ()
        b "{i}Ready.."
        "{i}{b}PHONE REMINDER{/b}{/i}"
        scene bg 24ps with fade
        $ renpy.pause()
        b "{i}Of course..{/i}"
        $ renpy.pause()
        scene black with Dissolve (1.5)
        $ renpy.pause()
        $ renpy.notify("Sonraki sabah..")
        $ renpy.pause()
        jump ep1morning
        return

    label ep1morning:
        scene bg 25ps with Dissolve (1.5)
        $ renpy.pause()
        b "{i}Fortunatelly everything went well last night.."
        b "{i}But I had better hurry if I don't want to get late.."
        $ renpy.pause()

        menu:
            "Go to the airport":
                scene black with Dissolve (1.5)
        $ renpy.pause()
        scene bg Hallway1ps with Dissolve (1.5)
        $ renpy.pause()
        n "Pooh..Two bags is definitely to much.."
        $ renpy.pause()
        menu:
            "Lock the door":
                scene bg Hallway2c3ps with fade
        $ renpy.pause()
        b "{i}It is Ms. Nicole.."
        extend "very kind woman..and friendly neighbor.."
        b "{i}Ever since I moved in here she still lives alone.."
        $ renpy.pause()
        scene bg Hallway2ps with fade
        $ renpy.pause()
        n "Where are the keys.."
        extend "I hope they didn't fall down to the bottom of the bag.."
        $ renpy.pause()
        menu:
            "Say hello":
                b "Morning Ms. Nicole.."
        scene bg h00 with hpunch
        n "Oops !"
        $ renpy.pause()
        n "I'm such a clumsy.."
        menu:
            "Help":
                jump ep1help
            "Walk away":
                scene bg Hallway6ps with fade
                b "{i}I would gladly help her but I have no time for this.."
                extend "\nI need to get to the airport in time.."
                n "..."
                $ renpy.pause ()
                jump ep1airport
        return

    screen ep1helpScr:
        imagemap:
            ground "images/ep1/h00.png"
            hotspot (736,734,30,35) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/h01.png") unhovered Hide("imgHider")
            hotspot (750,774,30,30) clicked Jump("ep1help") hovered ShowTransient("imgHider", img="images/ep1/h02.png") unhovered Hide("imgHider")
            hotspot (638,765,50,60) clicked Jump("ep1help") hovered ShowTransient("imgHider", img="images/ep1/h03.png") unhovered Hide("imgHider")
            hotspot (691,830,60,60) clicked Jump("ep1help") hovered ShowTransient("imgHider", img="images/ep1/h04.png") unhovered Hide("imgHider")
            hotspot (490,850,50,65) clicked Jump("ep1help") hovered ShowTransient("imgHider", img="images/ep1/h05.png") unhovered Hide("imgHider")


    label ep1help:
        call screen ep1helpScr
        scene bg h10 with dissolve
        jump ep1help2
        return

    screen ep1help2Scr:
        imagemap:
            ground "images/ep1/h10.png"
            hotspot (750,774,30,30) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/h11.png") unhovered Hide("imgHider")
            hotspot (638,765,50,60) clicked Jump("ep1help2") hovered ShowTransient("imgHider", img="images/ep1/h12.png") unhovered Hide("imgHider")
            hotspot (691,830,60,60) clicked Jump("ep1help2") hovered ShowTransient("imgHider", img="images/ep1/h13.png") unhovered Hide("imgHider")
            hotspot (490,850,50,65) clicked Jump("ep1help2") hovered ShowTransient("imgHider", img="images/ep1/h14.png") unhovered Hide("imgHider")

    label ep1help2:
        call screen ep1help2Scr
        scene bg h20 with dissolve
        jump ep1help3
        return

    screen ep1help3Scr:
        imagemap:
            ground "images/ep1/h20.png"
            hotspot (638,765,50,60) clicked Return("item") hovered ShowTransient("imgHider", img="images/ep1/h21.png") unhovered Hide("imgHider")
            hotspot (691,830,60,60) clicked Jump("ep1help3") hovered ShowTransient("imgHider", img="images/ep1/h22.png") unhovered Hide("imgHider")
            hotspot (490,850,50,65) clicked Jump("ep1help3") hovered ShowTransient("imgHider", img="images/ep1/h23.png") unhovered Hide("imgHider")

    label ep1help3:
        call screen ep1help3Scr
        scene bg h30 with dissolve
        jump ep1help4
        return

    screen ep1help4Scr:
        imagemap:
            ground "images/ep1/h30.png"
            hotspot (691,830,60,60) clicked Return("item") hovered ShowTransient("imgHider", img="images/ep1/h31.png") unhovered Hide("imgHider")
            hotspot (490,850,50,65) clicked Jump("ep1help4") hovered ShowTransient("imgHider", img="images/ep1/h32.png") unhovered Hide("imgHider")

    label ep1help4:
        call screen ep1help4Scr
        scene bg h40 with dissolve
        jump ep1help5
        return
    screen ep1help5Scr:
        imagemap:
            ground "images/ep1/h40.png"
            hotspot (490,850,50,65) clicked Return("item") hovered ShowTransient("imgHider", img="images/ep1/h41.png") unhovered Hide("imgHider")

    label ep1help5:
        call screen ep1help5Scr
        scene bg h50 with dissolve
        jump ep1hallway
        return

    label ep1hallway:
        $ renpy.pause()
        scene black with Dissolve (1.5)
        b "Here you go Ms. Nicole.."
        extend "\nLooks like sometimes two hands is just not enough, right ?"
        scene bg Hallway4c4ps with Dissolve(1.5)
        $ renpy.pause()
        n "Thank You [bro].."
        extend "Actually it is your fault))"
        b "Is it ?"
        n "Yeah..you spoiled me.."
        extend "You help me to carry the bags too often.."
        n "Now I can't carry two bags by myself.."
        b "Okay.."
        extend "\nWell..From now on I will let you to carry my bags along with yours.."
        extend "\n4 bags will do the trick"
        n "Ha-ha..You are so funny [bro]"
        b "Just kidding.."
        b "You know it is not a big deal.."
        extend "\nespecially since we are neighbors.."
        n "Right.."
        b "Okay Ms. Nicole it was nice to see you I have to.."
        n "[bro].."
        extend "It is just Nicole..How many times I need to tell you this.."
        b "I'm sorry..I always forget about that.."
        n "It is not like you have some memory issues.."
        extend ""
        extend "\nMaybe you think that I'm too old "
        extend "for you..?"
        b "Of course not..I just can't figure out how old you are.."
        extend "\nIt is either 18 or 20 right ? Because you look so amazing.."
        n "Oh..You're just saying that.."
        b "I mean it"
        n ".."
        n "Thank you.."
        extend "[bro].."
        extend "I'm terribly uncomfortable asking you but.."
        n "Could you please take a look at my computer again ?"
        b "It doesn't work ?"
        n "Yeah..And the thing is now I don't have money to give it to the service center.."
        extend "\nI can't do my work without it..so could you please fix it one more time ?"
        extend ""
        n "I will pay you.."
        extend "somehow.."
        extend "later.."
        b "Unfortunatelly I can't help you now.."
        extend "\nI need to pick up my.."
        extend ""
        extend "somebody from the airport..After that I also have plans.."
        n "It is okay..I understand.."
        b "How about tomorrow ? I think I'll have some time for that.."
        n "Great ! Just give me a call to make sure I'm at home okay ?"
        b "Yeah.."
        n "Wait ! Do you have my phone number ?"
        b "Uhm..I guess I don't.."
        n "Okay write it down.."
        extend "\n+1 800..."
        scene black with Dissolve (1.5)
        $ renpy.pause()
        "{i}Nicole's phone number gained"
        $ renpy.pause ()
        scene bg Hallway5ps with Dissolve (1.5)
        $ renpy.pause()
        b "Okay Nicole have a nice day.."
        n "Bye [bro].."
        extend "call me.."
        jump ep1airport
        return

    screen ep1air:
        imagemap:
            ground "images/ep1/Airport4.png"
            hotspot (88,874,900,210) clicked Return("item") hovered ShowTransient("imgHider", img="images/ep1/Airport4Bag.png") unhovered Hide("imgHider")


    label ep1airport:
        scene black with Dissolve (1.5)
        $ renpy.pause ()
        $ renpy.notify("Daha sonra Havaalanında..")
        $ renpy.pause()
        scene bg Airport2 with Dissolve(1.5)
        $ renpy.pause()
        b "{i}Okay these are the right gates.."
        extend  "I have to find Julie right now.."
        b "{i}Oh..there she is sitting on a bench.."
        extend "\nI wonder how she's changed...."
        extend "It's been more than 5 years.."
        b "{i}I can't believe how fast the time goes in this city.."
        extend ""
        b "{i}Will she recognize me after all this time..?"
        b "{i}What should I say to her..?"
        b "{i}'Hey it's me, [bro].."
        extend "You may remember me as your [brother].."
        extend "\nBut it's okay if you don't..'"
        b "{i}'It's me who has been writing emails and sending money all this time..'"
        b "..."
        b "{i}Shit..That is stupid..{\i}"
        extend "Why I am so nervous.."
        b "{i}I guess there is no way to prepare for this conversation.."
        "{i}{b}AIRPORT SPEAKER:{/b}{/i} {i}\nEnding on boarding the flight New York - Los Angeles.."
        b "{i}Okay ! Come what may !"
        menu:
            "Approach":
                scene black with Dissolve (1.5)
        $ renpy.pause()
        scene bg Airport3 with Dissolve (1.5)
        $ renpy.pause()
        "{i}{b}Guy:{/b}{/i}\nHey baby.."
        extend "on a scale of 1 to America..how free are you tonight ?"
        $ renpy.pause()
        j "What is your name ?"
        "{b}{i}Felixx:{/i}{/b}\nChicks call me 'Felixx'.."
        j "You can't get them to stop..?"
        "{b}{i}Felixx:{/i}{/b}\nWhaaat..?"
        j "That is bad.."
        extend "Don't let them do that to you..that is rude.."
        "{b}{i}Felixx:{/i}{/b}\nLook..are you alone here ?"
        extend " I can give you a ride to the city.."
        extend "\nAnd maybe later.."
        extend "you will want to ride something else, girl.."
        j "Not interested.."
        "{b}{i}Felixx:{/i}{/b}\nI don't get it.."
        extend "Are you a lesbian or what ?"
        b "Hi Julie !"
        scene bg Airport4 with dissolve
        b "Sorry I'm a little late..those traffic jams are just a nightmare.."
        j "Hi.."
        b ".."
        b "Ahm..Looks like something is going on between to of you..\nDid I miss something..?"
        j "No, you are right in time..party is just about to start.."
        b "What party ?"
        j "Well..It seems like Felixx and his dick are inviting everyone to hang out with them on a party..\nToo bad that no one else came..and we need to go too..so.."
        j "These guys have to enjoy each other's company tete-a-tete.."
        "{b}{i}Felixx:{/i}{/b}\nWTF..?!"
        j "Would you mind helping me with my bag [bro] ?"
        call screen ep1air
        b "Let's go.."
        scene black with Dissolve (1.5)
        jump ep1parking
        return
    label ep1parking:

        $car_lied = 0

        $ renpy.pause()
        $ renpy.notify("Daha Sonra Park'ta..")
        $ renpy.pause()
        scene bg Parking1c1ps with Dissolve (1.5)
        $ renpy.pause()
        b "Here we go.."
        extend "\nHand me your suitcase..I'll put all this stuff in the trunk.."
        j "Wow..I didn't know you have a car.."
        extend "\nIs this yours ?"
        menu:
            "Yes (Lie)":
                $ car_lied += 1
                b "Yeah..Why ?"
                j "It is..quite unexpectedly.."
                extend "\nI didn't think you can afford that luxurious car.."
                b "Well..I'm working here you know..I'm making a lot of money.."
                j "Good for you.."
                scene bg Parking1c2ps with fade
                $ renpy.pause()
                b "You can take off your hoodie if you want.."
                extend "it is not cold inside.."
                j "Okay.."
                b "Hop in on the back seat.."
                scene black with Dissolve (1.5)
                $ renpy.pause()
                b "How are you doing over there ?"
                j "Comfortable.."
                b "That is good..Let's go then ?"
                j "Yeah.."
                scene bg Parking2ps with Dissolve (1.5)
                $ renpy.pause()
                j "[bro]..how long does it take to get to your apartment ?"
                b "Ahm..Probably half an hour..if we are lucky with traffic of course.."
                j "Okay.."
                b "Right..So if you want to use WC now is the best time to visit it.."
                j "No I'm good.."
                b "Great.."
                $ renpy.pause()
                j "Wait a second..what is this..on the floor.."
                b "{i}Shit..I hope those are not blood stains.."
                j "Almost got it.."
                b "Leave it Julie.."
                extend "\nHow was your flight by the way..?"
                $ renpy.pause()
                scene bg Parking3ps with dissolve
                j "What the hell ?!"
                $ renpy.pause()
                b "{i}Shit..Vicky's panties.."
                b "It is not mine.."
                j "No shit ?!"
                extend ""
                b "Okay..I.."
                extend "I lied..this is not my car.."
                extend "It's company's car that is shared among many people.."
                extend "and apparently some other driver lost it.."
                j "I do not even know what's worse.."
                extend "\nthat you already lied to me so fast after 5 years.."
                extend "\nor"
                extend "\nthat the people from your work forget their panties at the back seat.."
                j "God ! What kind of work is that ?!"
                b "Well..I'm sorry.."
                extend "I just wanted to impress you.."
                j "Get us home please..I don't want to talk about it anymore.."
                jump ep1atHome
            "No (Truth)":
                b "I wish it was..No, it is my company's car.."
                b "It is shared among many people.."
                extend "but today I requested to use it in order to pick you from the airport.."
                j "I see.."
                scene bg Parking1c2ps with fade
                $ renpy.pause()
                b "You can take off your hoodie if you want..it is not cold inside.."
                j "Okay.."
                b "Hop in on the back seat.."
                scene black with Dissolve (1.5)
                $ renpy.pause()
                b "How are you doing over there ?"
                j "Comfortable.."
                b "That is good.."
                extend "Let's go then ?"
                j "Yeah.."
                scene bg Parking2ps with Dissolve (1.5)
                $ renpy.pause()
                j "[bro]..how long does it take to get to your apartment ?"
                b "Ahm..Probably half an hour..if we are lucky with traffic of course.."
                j "Okay.."
                b "Right..So if you want to use WC now is the best time to visit it.."
                j "No I'm good.."
                b "Great.."
                $ renpy.pause()
                j "Wait a second..what is this..on the floor.."
                b "{i}Shit..I hope those are not blood stains.."
                j "Almost got it.."
                b "Leave it Julie.."
                extend "\nHow was your flight by the way..?"
                $ renpy.pause()
                scene bg Parking3ps with dissolve
                j "What the hell ?!"
                $ renpy.pause()
                b "{i}Shit..Vicky's panties.."
                b "It is not mine.."
                j "Well that is a relief.."
                extend "because I was just about to start worrying about you.."
                b "Throw them on the floor.."
                extend "They will find their owner anyway.."
                j "Right.."
                extend "Could you repeat please.."
                extend "What exactly your work is about ?"
                b "Oh come on Julie.."
                extend "You are a big girl..maybe someone.."
                extend "\nhad a good time on that back seat.."
                j "In that case I will take another seat.."
                extend "please open the front door for me.."
                b "Sure.."
                j "And let's go to your place already..Shall we ?"
                b ".."
                jump ep1atHome
        return

    screen ep1atHomeScr:
        imagemap:
            ground "images/ep1/19ps.png"
            hotspot (336, 774, 376, 263) clicked Return ("drawer") hovered ShowTransient("imgHider", img="images/ep1/20ps.png") unhovered Hide("imgHider")

    screen ep1atHome2Scr:
        imagemap:
            ground "images/ep1/21ps.png"
            hotspot (172,769,420,2483) clicked Return ("stuff") hovered ShowTransient("imgHider", img="images/ep1/22ps.png") unhovered Hide("imgHider")


    label ep1atHome:
        scene black with Dissolve (1.5)
        $ renpy.pause()
        $ renpy.notify("Daha sonra evde..")
        $ renpy.pause()
        scene bg athome1c1ps with Dissolve(1.5)
        $ renpy.pause()
        b "Here it is..make yourself at home.."
        if car_lied == 1:
            j "Please tell me that this is your apartment.."
            extend "\nBecause I don't want to find a dead body under the couch.."
            extend "\nAnd find out that someone from your co-workers forgot it there.."
        else:
            j "So is this is your place ?"
        b "No..the company also provides me this place.."
        extend "It is small but comfy.."
        b "Here is everything you need.."
        extend "Kitchen..TV..Wi-Fi, of course..\nThe password is 'perv2k16'..whatever that means.."
        scene bg athome1c3ps with fade
        $ renpy.pause()
        b "The door next to you is a bathroom.."
        extend "and this one is the bedroom.."
        b "You will be sleeping in here so..I will bring your bags to the bedroom.."
        j "Where will you sleep ?"
        b "Oh..I will be sleeping on a couch right here.."
        extend "for now.."
        j "For now..?"
        b "I mean while you are here.."
        j "What if I wanted to sleep in this room.."
        b "Oh..I'm afraid that is not a good idea because.."
        extend "I may get a call from work in the middle of the night.."
        extend "\nAnd I will have to go..so..I don't want to wake you up every time.."
        j "I see.."
        b "Just a second..I need to pick up some stuff from the bedroom and..it will be all in your disposal.."
        j "Okay.."
        extend "I'll take a shower then.."
        b "Oh..almost forgot..I'm going to the gym after..but"
        extend "\nDon't be scared it is nearby..so I will come back in an hour.."
        j "[bro]..You are talking to me like I'm a kid.."
        b "Sorry..It is just so unusual that you are adult now.."
        b "Oh..There is a food in the fridge so you won't die from starving.."
        j "That's good news.."
        b "Ok..see you around.."
        j "Yep.."
        $ renpy.pause()
        scene black with dissolve
        $ renpy.pause()
        scene bg 19ps with Dissolve (1.5)
        b "{i}Okay I need to take my stuff.."
        extend "Julie should not see it.."
        call screen ep1atHomeScr
        scene bg 21ps with dissolve
        call screen ep1atHome2Scr
        scene bg 23ps with dissolve
        b "{i}Got it.."
        b "{i}It is time to go to the gym.."
        extend "I start to losing the shape because of missed trainings.."
        extend ""
        menu:
            "Go to Gym":
                $ renpy.pause()
        j "[bro]..Are you still here..?"
        b "{i}What is wrong..?"
        jump ep1athome2
        return

    label ep1athome2:
        $bathroom_naked = 0

        scene black with Dissolve (1.5)
        $ renpy.pause()
        b "Yes..I'm here Julie..What happened ?"
        $ renpy.pause()
        scene bg athome2c3_ with Dissolve (1.5)
        $ renpy.pause()
        j "Come here please.."
        b "Yes I'm here.."
        $ renpy.pause()
        scene bg athome2c3ps with dissolve
        $ renpy.pause()
        j "I forgot to take a towel.."
        extend "could you bring it to me please..?"
        j "It is somewhere in my bags.."
        extend ""
        b "Julie there are plenty of towels in the bathroom.."
        j "I didn't find any..so..get me my towel.."
        extend "please.."
        scene bg athome2c4ps with fade
        $ renpy.pause()
        b "Julie I won't rummage through your stuff plus I don't have time for that.."
        extend "\nI'm usually at the gym by this time.."
        j "Do you want to leave me this wet or what..?"
        extend ""
        menu:
            "Come in":
                $ bathroom_naked += 1
                $ renpy.pause()
                $ renpy.pause()
                scene bg athome4c4ps with vpunch
                j "HEY !!!"
                extend " What the hell ?!"
                $ renpy.pause()
                b "Relax..I just want to show you where the towels are.."
                j "Are you out of your mind ?!"
                extend " I'm completely NAKED !"
                $ renpy.pause()
                b "You said you couldn't find any..?"
                j "I can't believe this !"
                scene bg athome5c6ps with fade
                $ renpy.pause()
                b "Here they are.."
                extend "You can pick any you like.."
                extend "\nThey are all new.."
                j "Hello ! Do you think this is okay to break in like this ?!"
                b "That's it..I'm leaving now.."
                extend "\nCall me next time when something more urgent happens.."
                extend "\nLike if you couldn't find a toilet paper.."
                j "Tsk.."
                $ renpy.pause()
                jump ep1gym
            "Stay outside":
                b "Of course not..I'll help you to find towels.."
                extend "it is good that I don't have a big bathroom.."
                j "You are not helping !"
                b "Okay..okay.."
                $ renpy.pause()
                b "Do you see the mirror..?"
                scene bg athome6c2ps with fade
                $ renpy.pause()
                j "Yes.."
                b "Okay..that means no one has stolen it yet.."
                j "What ?"
                b "Nothing.."
                extend "okay..now.."
                extend "there is a sink right below the mirror.."
                scene bg athome7c1ps with fade
                $ renpy.pause()
                j "Yeah I see it.."
                b "Good.."
                b "Now get down and open the cabinet that is below the sink.."
                scene bg athome8c2ps with fade
                $ renpy.pause()
                j "Okay.."
                b "Wait !"
                extend " Don't open it like a door.."
                j "Excuse me ?!"
                b "You might break the roller mechanism.."
                extend "And all our efforts will be vain...."
                extend "\nInstead push it towards the right side.."
                b "It will slide easily.."
                extend ""
                j "Got it.."
                scene bg athome9c6ps with fade
                $ renpy.pause()
                j "I've found it..Thanks.."
                b "It was difficult but you were doing great.."
                j "You know..usually people keep that kind of stuff in sight.."
                b "Maybe.."
                j "Okay I'm going out.."
                scene black with Dissolve (1.5)
                $ renpy.pause()
                j "So..are you going to the gym..?"
                scene bg athome10c5ps with Dissolve (1.5)
                $ renpy.pause()
                b "Yeah..you have my phone number so feel free to call me if you need something.."
                j "Okay.."
                b "Okay.."
                extend "See you.."
                $ renpy.pause()
                jump ep1gym
        return

    screen ep1gym1ArmScr:
        imagemap:
            ground "images/ep1/FClubc1ps.png"
            hotspot (176,202,57,38) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/FClubc1psArms1.png") unhovered Hide("imgHider")

    screen ep1gym2ArmScr:
        imagemap:
            ground "images/ep1/FClubc1ps.png"
            hotspot (1532,138,90,308) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/FClubc1psArms2.png") unhovered Hide("imgHider")

    screen ep1gym3ArmScr:
        imagemap:
            ground "images/ep1/FClubc1ps.png"
            hotspot (545,107,90,157) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/FClubc1psArms3.png") unhovered Hide("imgHider")

    screen ep1gym1LegsScr:
        imagemap:
            ground "images/ep1/FClubc1ps.png"
            hotspot (1676,373,113,126) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/FClubc1psLegs1.png") unhovered Hide("imgHider")

    screen ep1gym2LegsScr:
        imagemap:
            ground "images/ep1/FClubc1ps.png"
            hotspot (112,207,63,34) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/FClubc1psLegs2.png") unhovered Hide("imgHider")

    screen ep1gym3LegsScr:
        imagemap:
            ground "images/ep1/FClubc1ps.png"
            hotspot (476,976,241,103) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/FClubc1psLegs3.png") unhovered Hide("imgHider")

    screen ep1gym1TorsoScr:
        imagemap:
            ground "images/ep1/FClubc1ps.png"
            hotspot (594,165,335,45) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/FClubc1psTorso1.png") unhovered Hide("imgHider")

    screen ep1gym2TorsoScr:
        imagemap:
            ground "images/ep1/FClubc1ps.png"
            hotspot (833,84,133,67) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/FClubc1psTorso2.png") unhovered Hide("imgHider")

    screen ep1gym3TorsoScr:
        imagemap:
            ground "images/ep1/FClubc1ps.png"
            hotspot (112,348,118,268) clicked Return ("item") hovered ShowTransient("imgHider", img="images/ep1/FClubc1psTorso3.png") unhovered Hide("imgHider")


    label ep1gym:
        $strength = 6
        scene black with Dissolve (1.5)
        $ renpy.pause()
        $ renpy.notify("Daha sonra Spor Salonunda..")
        $ renpy.pause()
        scene bg fclubc1ps with Dissolve(1.5)
        $ renpy.pause()
        "{i}Here you can train your strength parameter.."
        extend "\nRight now it is [strength] out of 10"
        "{i}This parameter will be crucial later in the game so please don't forget to visit the gym from time to time :)"
        menu:
            "Finish automatically":
                "Time is money !"
                jump ep1FinishTraining
            "Proceed manually":
                "No pain, no gain !"
        menu:
            "Arms training":
                b "{i}Let's do this !"
        call screen ep1gym1ArmScr
        "{i}Arms training complete 1 out of 3"
        call screen ep1gym2ArmScr
        "{i}Arms training complete 2 out of 3"
        call screen ep1gym3ArmScr
        "{i}Arms training complete !"
        menu:
            "Legs training":
                b "{i}Let's do this !"
        call screen ep1gym1LegsScr
        "{i}Legs training complete 1 out of 3"
        call screen ep1gym2LegsScr
        "{i}Legs training complete 2 out of 3"
        call screen ep1gym3LegsScr
        "{i}Legs training complete !"
        menu:
            "Torso training":
                b "{i}Let's do this !"
        call screen ep1gym1TorsoScr
        "{i}Torso training complete 1 out of 3"
        call screen ep1gym2TorsoScr
        "{i}Torso training complete 2 out of 3"
        call screen ep1gym3TorsoScr
        "{i}Torso training complete !"
        b "{i}Okay..That is enough for today.."
        extend "\nThat was a good training !"
        menu ep1FinishTraining:
            "Finish":
                b "{i}Time to go home"
        $strength += 1
        "{i}Your strength has grown.."
        extend "{i}\nCurrent:[strength] out of 10"
        $ renpy.pause()
        scene black with Dissolve (1.5)
        $ renpy.pause()
        scene bg fclubc2c1ps with Dissolve (1.5)
        $ renpy.pause()
        b "{i}Why I'm feeling like I've missed something.."
        extend "\nMaybe it's because of Julie..Probably I just worry about how it all will turn out.."
        b "{i}I don't want her to get hurt because of my work.."
        b "{i}That is strange, nobody called me today.. I can't even recall when is was so quiet.."
        b "{i}Let's hope this is not a calm before the storm.."
        "{b}{i}PHONE MESSAGE{/i}{/b}"
        b "{i}Speak of the devil.."
        scene bg fclubc3c2ps with fade
        $ renpy.pause()
        b "OH SHIT !!!"
        jump ep1final
        return
    label ep1final:
        scene black with Dissolve (1.5)
        $ renpy.pause()
        $ renpy.notify("Bu arada evde..")
        $ renpy.pause()
        scene bg athome11c1ps with Dissolve (1.5)
        $ renpy.pause()
        j "{i}Boring.."
        j "{i}I wonder why Scarlett is always busy when I call her.."
        extend "Maybe she is having an affair and cheating on me..?"
        j "{i}No..that is a bullshit.."
        extend "\nShe would never do something like this to me.."
        scene bg athome12c1ps with dissolve
        $ renpy.pause()
        j "{i}Oh..?"
        scene bg athome14c1ps with dissolve
        $ renpy.pause()
        j "{i}Finally !"
        scene bg athome15c1ps with dissolve
        j "Hi sexy !"
        extend "\nI was calling you like a dozen of times.."
        $ renpy.pause()
        j "Oh..I see.."
        j "Me ? Yeah..I'm already at my [brother]'s place.."
        extend "\nWait a second..Someone is calling on the second line.."
        j "Uh..nevermind it is him.. I won't be answering I want to talk to you.."
        j "Worrying ?! Who ? [bro] ?! "
        extend "\nHe is selfish and not worrying about anybody.."
        extend "\nHe just treats his [sis] like a kid.."
        j "What ?!"
        extend "\nI don't know..He is fine..I guess.."
        j "I'm not jealous !"
        extend "\nOkay you will see for yourself if he is hot or not when you come back to the city.."
        j "By the way when will it be..? I'm missing you so much.."
        scene bg athome16c1ps with Dissolve (1.25)
        $ renpy.pause()
        j "Do you want to know what I'm doing right now..?"
        extend "\nOh.."
        $ renpy.pause()
        j "Yeah..I like to do this when I'm talking to you on the phone..Ah.."
        extend "\nYour voice gives me goosebumps.."
        j "Ah..Yeah..Mhh.."
        extend "\nYes I'm such a naughty girl.."
        j "I love when you talk dirty to me.."
        extend "\nIt turns me on..Ah.."
        j "Please come back soon..I want you so bad.."
        "{b}{i}DOOR OPENS"
        scene bg athome17c1ps with dissolve
        $ renpy.pause()
        j "Oops..someone has openend the door.."
        extend "It is probably [bro]..\nI'll call you back, darling..Bye.."
        $ renpy.pause()
        scene black with dissolve
        $ renpy.pause()
        scene bg athome18c2ps with dissolve
        $ renpy.pause()
        v "Hi there!"
        extend " I'm surprised!"
        j "He..Hello.."
        extend "Are you..looking for somebody..?"
        v "[bro] didn't tell me that someone else will join today's party.."
        j "What..?"
        extend " What party..?"
        v "Hm.."
        extend "It does not look like him.."
        j "Excuse me..but..who are you..?"
        $ renpy.pause()
        scene bg athome19c1ps with fade
        $ renpy.pause()
        v "Who am I ?"
        extend "\nDo you really want to know ?"
        jump episode2
        return
####################################################EPISODE_2##################################################
    image bg atHome20c5ps = "images/ep2/atHome20c5ps.png"
    image bg atHome21c3_ps = "images/ep2/atHome21c3_ps.png"
    image bg atHome22c4ps = "images/ep2/atHome22c4ps.png"
    image bg atHome23c4ps = "images/ep2/atHome23c4ps.png"
    image bg atHome24c2_ps = "images/ep2/atHome24c2_ps.png"
    image bg atHome24c2ps = "images/ep2/atHome24c2ps.png"
    image bg atHome25c2_ps = "images/ep2/atHome25c2_ps.png"
    image bg atHome25c2ps = "images/ep2/atHome25c2ps.png"
    image bg atHome26c2_ps = "images/ep2/atHome26c2_ps.png"
    image bg atHome26c2ps = "images/ep2/atHome26c2ps.png"
    image bg atHome27c2_ps = "images/ep2/atHome27c2_ps.png"
    image bg atHome27c2ps = "images/ep2/atHome27c2ps.png"
    image bg atHome28c2_ps = "images/ep2/atHome28c2_ps.png"
    image bg atHome28c2ps = "images/ep2/atHome28c2ps.png"
    image bg atHome30c3ps = "images/ep2/atHome30c3ps.png"
    image bg atHome29c3ps = "images/ep2/atHome29c3ps.png"
    image bg atHome31c3ps = "images/ep2/atHome31c3ps.png"
    image bg atHome32c4ps = "images/ep2/atHome32c4ps.png"
    image bg atHome33c5ps = "images/ep2/atHome33c5ps.png"
    image bg atHome33c6_ps = "images/ep2/atHome33c6_ps.png"

    image bg m1c1_1ps = "images/ep2/m1c1_1ps.png"
    image bg m1c1_ps = "images/ep2/m1c1_ps.png"
    image bg m1c1ps = "images/ep2/m1c1ps.png"
    image bg m1c6 = "images/ep2/m1c6.png"
    image bg m1c6_ = "images/ep2/m1c6_.png"
    image bg m2c7ps = "images/ep2/m2c7ps.png"
    image bg m3c8ps = "images/ep2/m3c8ps.png"
    image bg m4c8_ps = "images/ep2/m4c8_ps.png"
    image bg m4c8ps = "images/ep2/m4c8ps.png"

    image bg atHome34c1ps = "images/ep2/atHome34c1ps.png"
    image bg atHome35c5ps = "images/ep2/atHome35c5ps.png"
    image bg atHome36c2ps = "images/ep2/atHome36c2ps.png"
    image bg atHome36c3ps = "images/ep2/atHome36c3ps.png"
    image bg atHome37c4ps = "images/ep2/atHome37c4ps.png"
    image bg atHome38c6ps = "images/ep2/atHome38c6ps.png"
    image bg atHome39c7_ps = "images/ep2/atHome39c7_ps.png"
    image bg atHome40c1ps = "images/ep2/atHome40c1ps.png"
    image bg atHome41c1ps = "images/ep2/atHome41c1ps.png"
    image bg atHome41c2ps = "images/ep2/atHome41c2ps.png"
    image bg atHome41c3ps = "images/ep2/atHome41c3ps.png"
    image bg atHome41c7ps = "images/ep2/atHome41c7ps.png"
    image bg atHome42c3ps = "images/ep2/atHome42c3ps.png"
    image bg atHome43c3ps = "images/ep2/atHome43c3ps.png"
    image bg atHome44c3ps = "images/ep2/atHome44c3ps.png"
    image bg atHome45c3ps = "images/ep2/atHome45c3ps.png"
    image bg atHome46c3ps = "images/ep2/atHome46c3ps.png"
    image bg atHome47c3_ps = "images/ep2/atHome47c3_ps.png"
    image bg atHome47c3ps = "images/ep2/atHome47c3ps.png"
    image bg atHome48c3ps = "images/ep2/atHome48c3ps.png"
    image bg atHome49c3_ps = "images/ep2/atHome49c3_ps.png"
    image bg atHome49c3ps = "images/ep2/atHome49c3ps.png"
    image bg atHome50c3ps = "images/ep2/atHome50c3ps.png"
    image bg atHome51c3ps = "images/ep2/atHome51c3ps.png"
    image bg atHome52c3ps = "images/ep2/atHome52c3ps.png"
    image bg atHome53c3ps = "images/ep2/atHome53c3ps.png"
    image bg atHome54c3_ps = "images/ep2/atHome54c3_ps.png"
    image bg atHome54c3ps = "images/ep2/atHome54c3ps.png"
    image bg atHome55c3ps = "images/ep2/atHome55c3ps.png"
    image bg atHome55c3_ps = "images/ep2/atHome55c3_ps.png"
    image bg atHome56c3_ps = "images/ep2/atHome56c3_ps.png"
    image bg atHome56c3ps = "images/ep2/atHome56c3ps.png"
    image bg atHome57c3_ps = "images/ep2/atHome57c3_ps.png"
    image bg atHome57c3ps = "images/ep2/atHome57c3ps.png"
    image bg atHome58c3ps = "images/ep2/atHome58c3ps.png"
    image bg atHome59c3ps = "images/ep2/atHome59c3ps.png"
    image bg atHome60c3ps = "images/ep2/atHome60c3ps.png"

    image bg atHome61c1_ps = "images/ep2/atHome61c1_ps.png"
    image bg atHome61c1ps = "images/ep2/atHome61c1ps.png"
    image bg atHome62c2ps = "images/ep2/atHome62c2ps.png"
    image bg atHome63c3_ps = "images/ep2/atHome63c3_ps.png"
    image bg atHome63c3ps = "images/ep2/atHome63c3ps.png"
    image bg atHome64c3_ps = "images/ep2/atHome64c3_ps.png"
    image bg atHome64c3ps = "images/ep2/atHome64c3ps.png"
    image bg atHome65c3ps = "images/ep2/atHome65c3ps.png"

    image bg fr1c2ps = "images/ep2/fr1c2ps.png"
    image bg fr1c5ps = "images/ep2/fr1c5ps.png"
    image bg fr3c7_ps = "images/ep2/fr3c7_ps.png"
    image bg fr4c9_ps = "images/ep2/fr4c9_ps.png"
    image bg fr5c6_ps = "images/ep2/fr5c6_ps.png"
    image bg fr6c10_ps = "images/ep2/fr6c10_ps.png"
    image bg fr7c3ps = "images/ep2/fr7c3ps.png"
    image bg fr8c1_ps = "images/ep2/fr8c1_ps.png"
    image bg fr8c1ps = "images/ep2/fr8c1ps.png"
    image bg fr9c2ps = "images/ep2/fr9c2ps.png"
    image bg fr9c4_ps = "images/ep2/fr9c4_ps.png"
    image bg fr10c3ps = "images/ep2/fr10c3ps.png"
    image rooms3_ps = "images/ep2/rooms3_ps.png"
    image rooms3ps = "images/ep2/rooms3ps.png"

    label episode2:
        # vSide initial "1"
        # nSide initial "1"
        # jSide initial "1"
        scene bg atHome21c3_ps with fade
        v "Hm..."
        $ renpy.pause ()
        v "What would be the correct way to say this.."
        scene bg atHome20c5ps with fade
        $ renpy.pause()
        v "Well.."
        v "My name is Vicky and.."
        $ renpy.pause()
        j "Okay.."
        scene bg atHome22c4ps with fade
        $ renpy.pause()
        v "Damn.."
        extend "I haven't thought that it would be so difficult to say this.."
        $ renpy.pause()
        v "I'm a sl.."
        "{b}{i}DOOR OPENS{/b}{/i}"
        scene bg atHome23c4ps with dissolve
        $ renpy.pause()
        b "Hi, Girls!"
        v "Hi, [bro].."
        extend "I was just about to introduce myself to your little friend.."
        b "She is my girlfriend"
        j "Ah..That explains everything."
        extend "\nYou just didn't tell me that you have one.."
        v "Me too.. Who is she ?"
        b "Very funny Vicky.."
        extend "I love your sense of humor.."
        v ".."
        b "Julie, meet my girlfriend Vicky"
        b "Vicky, this is my younger [sis] Julie.."
        extend ""
        v "Younger [sis]..?"
        j "A pleasure to meet you, Vicky.."
        v "Oh, Julie.."
        extend "the pleasure is all mine.."
        $ renpy.pause()
        b "Let's go to the kitchen, girls.."
        extend "Would you like something to drink..?"
        scene black with Dissolve(1.0)
        $ renpy.notify("Bir an sonra..")
        $ renpy.pause()
        scene bg atHome25c2ps with Dissolve (2.0)
        $ renpy.pause()
        v "A girlfriend, huh..?"
        j "[bro], why you didn't tell me earlier that you have such a beautiful girlfriend ?"
        scene bg atHome25c2_ps with dissolve
        v "Thank you, Julie.."
        extend "It is very sweet of you.."
        $ renpy.pause()
        b "I just wanted to make a surprise.."
        scene bg atHome25c2ps with dissolve
        v "Really..?"
        b "I mean by introducing you to each other like this.."
        scene bg atHome24c2_ps with dissolve
        v "I guess the surprise exceeded all of your expectations didn't it..?"
        b "Indeed.."
        scene bg atHome25c2ps with dissolve
        j "I was scared at the beginning..But it was fun anyway ha-ha.."
        scene bg atHome24c2_ps with dissolve
        j "By the way, how long are you together ?"
        scene bg atHome24c2ps with dissolve
        v "Couple of months.."
        b "Couple of weeks!"
        scene bg atHome25c2ps with dissolve
        j "Oh..?"
        v ".."
        b "Depending on how to count.."
        extend "You know..from first date or from first.."
        v "Yeah..I still can't believe it took you so long.."
        j "Wow..That is impressive anyway.."
        scene bg atHome24c2_ps with dissolve
        j "I mean..It's only couple of month and you've already decided to live together.."
        b "We haven't.."
        scene bg atHome24c2ps with dissolve
        v "[bro] gave me the keys just in case.."
        b "Yeah..you know.."
        extend "\nKind of 'Don’t Put All Your Eggs in One Basket' stuff.."
        scene bg atHome25c2_ps with dissolve
        j "I see.."
        extend "So it looks like you trust each other enough.."
        v "Oh yeah.."
        scene bg atHome24c2ps with dissolve
        v "The trust is crucial in our relationships.."
        scene bg atHome24c2_ps with dissolve
        v "Right, [bro]..?"
        b "For sure.."
        j "How did you guys meet ?"
        scene bg atHome24c2ps with dissolve
        v "This is an amazing story, Julie.."
        j "Really ?"
        v "Yeah..[bro] why don't you tell..?"
        scene bg atHome25c2ps with dissolve
        $ renpy.pause()
        b "{i}Shit..{/i}"
        menu:
            "Come up with something":
                b "Well..it was at the night bar.."
                extend "\nI visit the place few times a month to rest.."
                extend "after work.."
                b "But that day at bar counter was an incredibly beautiful girl.."
                v ".."
                b "She was so gorgeous that other girls were no match for her.."
                j "It was Vicky..?"
                b "No, it was a barmaid.."
                v "Asshole))"
                b "Of course it was Vicky.."
                b "So.."
                extend "As I was saying, "
                extend "she was so amazing that I even started to think that she might be.."
                extend "One of the escort service representative.."
                scene bg atHome24c2_ps with dissolve
                j "By the way, I've heard few creepy stories about those women.."
                scene bg atHome24c2ps with dissolve
                j "Some of them a pretty dangerous people.."
                v "That is true.."
                scene bg atHome25c2_ps with dissolve
                j "There are rumors that they use sleeping pills on a clients.."
                extend "\nThen rob the victims and leave them with the handcuffs fastened to the bed.."
                v "That is not true.."
                scene bg atHome24c2ps with dissolve
                j "Oh my favourite story is when a woman tied up a client who refused to pay and then.."
                extend "\nShe cut off his balls and threw them out from the window !"
                b "Julie !"
                scene bg atHome25c2_ps with dissolve
                j "What ?! I'm not making this up.."
                v "That is.."
                extend "an interesting story.."
                scene bg atHome25c2ps with dissolve
                $ renpy.pause ()
                j "Sorry, I've interrupted you..Please continue.."
                b "Yeah..Ahm.."
                extend "I saw some jerk started to molest Vicky..\nSo I decided to intervene.."
                scene bg atHome25c2_ps with dissolve
                v "The guy looked like he just wanted to buy me a drink.."
                b "It wasn't like that..I saw him started groping you.."
                scene bg atHome24c2_ps with dissolve
                v "I could defend myself..I had electro shocker in my bag.."
                j "Wow"
                b "Oh yeah..I perfectly remembered it.."
                scene bg atHome24c2ps with dissolve
                v "I stunned them both just in case.."
                scene bg atHome25c2_ps with dissolve
                j "No way !"
                b "Yeah.."
                v "It all ended up with someone called the police and.."
                scene bg atHome25c2ps with dissolve
                b "Other guy was taken to the police station.."
                b "Cops found at him unregistered weapon.."
                v "Right..And as an apology I offered to buy [bro] a drink.."
                b "Yeah..That is how we met.."
                scene bg atHome24c2_ps with dissolve
                j "Unbelievable..What a story.."
                extend "Sounds like a scene from an action movie"
                scene bg atHome24c2ps with dissolve
                v "Agree.."
                $ renpy.pause()
                b "Okay that is enough questions.."
                extend "\nI feel like I'm at the middle of interrogation"
                scene bg atHome25c2_ps with dissolve
                j "Ok..I'm just being curious.."
            "Change the topic":
                b "Come on Julie.."
                extend "Why don't you tell Vicky at least something about you ?"
                scene bg atHome25c2_ps with dissolve
        v "Yeah..Julie what about you ?"
        extend "\n[bro] didn't tell me much about his [family].."
        j "It's not surprising.."
        scene bg atHome24c2_ps with dissolve
        j "He probably acted like he doesn't have one.."
        b "..."
        scene bg atHome24c2ps with dissolve
        v "So Julie..What are you up to ? Do you have any plans ?"
        j "Yeah I'm going to study at the local university, I've successfully passed the entrance exams already"
        j "But the dormitory still closed for summer holidays so.."
        extend "\nI had to stay at [bro] place"
        j "Anyway, since I'm going to spend next few years in this city I'd like to get know it better.."
        v "I see.."
        j "Unfortunately there is a little problem.."
        extend "\nLooks like that [bro] is always busy with his work.."
        extend "\nAnd..My only friend in this city currently at home.."
        j "She will return only in a few days..so..I don't know who will help me out with exploring the city.."
        v "Oh don't worry Julie..I'll keep you company.."
        j "Really ?"
        v "Sure, I will arrange a city tour for you and will show you the main places that we, girls, need to know.."
        b "Ahm Vicky.."
        scene bg atHome24c2_ps with dissolve
        b "Do you think this is good idea..?"
        v "Why not ?"
        v "Do you want her sittig at home this all time ?"
        j "No ! It is boooooooring.."
        v "Or.."
        extend "You would rather take her with you to the work..?"
        b "No.."
        j "Probably it is even more boring.."
        scene bg atHome24c2ps with dissolve
        v "So it is decided.."
        extend "Tomorrow at the morning we will go to my favourite clothing boutique.."
        v "And then we will go to the cafe to eat something.."
        extend "\nWhat do you say ?"
        j "Cool !\nI'm in !"
        j "I can't wait !"
        v "But only if your [brother] is okay with this.."
        scene bg atHome25c2_ps with dissolve
        j "Pleeeeease, [bro].."
        $ renpy.pause()
        b "{i}It doesn't look like I have much of a choice.."
        $ renpy.pause()
        menu:
            "Agree":
                b "Okay, I don't mind about this idea.."
        scene bg atHome24c2ps with dissolve
        j "Yay !"
        b "Vicky.."
        scene bg atHome24c2_ps with dissolve
        v "Yes ?"
        b "Only clothing store and cafe please.."
        extend "\nNo funny business.."
        v "Of course..You know me.."
        $ renpy.pause()
        scene bg atHome25c2_ps with dissolve
        j "Oh, almost forgot..I need to open a bank account in order to pay for the university and dormitory.."
        v "Well, I think [bro] will help you with this.."
        scene bg atHome25c2ps with dissolve
        b "Yeah..I just didn't think yet what exact bank to choose.."
        extend ""
        v "But you told me yourself that you have a couple friends in the most secure bank in this city.."
        v "Why not choose it for Julie..?"
        scene bg atHome24c2_ps with dissolve
        v "I'm planning to transfer all my money to that bank as well.."
        j "By the way, the payment for the dormitory must be done beforehand.."
        scene bg atHome25c2_ps with dissolve
        j "So we need to deal with it as soon as possible.."
        b "When the dormitory opens, once again..?"
        scene bg atHome26c2_ps with dissolve
        j "Why ?"
        extend "\nAm I bothering you already ?"
        b "What..? No.."
        j "Are you sure ?"
        extend " Maybe I'm causing you a lot of troubles..?"
        scene bg atHome26c2ps with dissolve
        v "Oops.."
        j "You would rather get rid of me, wouldn't you..?"
        b "Julie, it's not like that.."
        b "I just.."
        scene bg atHome27c2_ps with dissolve
        j "Because it looks exactly like that to me.."
        j "I almost started to think that you care about someone except yourself.."
        b "Julie, please.."
        scene bg atHome27c2ps with dissolve
        j "So far you've been doing good by following [father]'s steps.."
        v "Wow..I guess I had a lot of coffee.."
        b "Our [father] has nothing to do with it.."
        b "I'm not going to leave you now.."
        j "Of course you're not. You will leave us later."
        scene bg atHome27c2_ps with dissolve
        v "Excuse me.. Nature calls.."
        scene bg atHome30c3ps with fade
        $ renpy.pause()
        b "Julie, I know I've been acting weird but.."
        scene bg atHome28c2_ps with fade
        j "But what ?!"
        j "Our [mom] told me that at first [father] was sending some money and messages as well.."
        j "And then he disappeared forever.."
        scene bg atHome28c2ps with dissolve
        j "Looks like in our [family] men are all the same.."
        b "Julie, please listen to me.."
        scene bg atHome28c2_ps with dissolve
        j "No wonder if all men are like this !"
        j "If you want to know it was [mom]'s idea send me to live with you.."
        b "{i}I must change the topic..Here is a good chance.."
        b "By the way, how is she ? How is [mom] ?"
        scene bg atHome28c2ps with dissolve
        j "Oh you don't know, do you ?"
        j "Of course..How do you know.."
        extend "\nIt is extremely exceeds your 'once per month limit' to talk with us, right ?"
        b ".."
        scene bg atHome28c2_ps with dissolve
        j "By the way, [mom] told me that you were against the idea me living with you.."
        j "You even offered to rent a hotel room for me.."
        extend "\nHow generous of you.."
        b "I.."
        scene bg atHome28c2ps with dissolve
        j "You know what, [mom] wanted us to live as a [family] at least for a short time.."
        j "Because we all know that otherwise you wouldn't find a time to meet with me, even living in the same city.."
        b ".."
        scene bg atHome28c2_ps with dissolve
        j "I'll be honest.."
        extend "\nI did not want to come to you at all.."
        extend "I'm doing it for [mom].."
        scene bg atHome29c3ps with fade
        $ renpy.pause()
        b "Julie, listen..I'm sorry.."
        extend "I really am.."
        scene bg atHome28c2ps with fade
        b "I know that I've been missing and not been with you and [mom] all this time.."
        extend "\nAnd.."
        b "All this situation looks like I want to leave you and break off all relations with you.."
        extend "\nBut.."
        b "Deeply inside I want absolutely else.."
        extend "\nI'm not like that at all.."
        scene bg atHome28c2_ps with dissolve
        j "I don't know what is going on deeply inside, [bro].."
        extend "\nI can only judge by what is on the surface.."
        scene bg atHome28c2ps with dissolve
        b ".."
        $ renpy.pause()
        scene bg atHome28c2_ps with dissolve
        j "I don't want to talk about this anymore..It's been a long day and I'm tired.."
        extend "\nI'll go take a walk before the sleep.."
        b "Be careful..It's already dark outside.."
        j "Don't worry, I bet they have the light at the store.."
        scene bg atHome28c2ps with dissolve
        $ renpy.pause()
        scene black with Dissolve (2.0)
        $ renpy.notify("Bir an sonra..")
        $ renpy.pause()
        b "{i}I wonder where is Vicky.."
        b "{i}She wanted to visit the bathroom.."
        b "{i}Is she still there..?!"
        $ renpy.pause()
        menu:
            "Check the bathroom":
                $ config.rollback_enabled = False
                $ renpy.pause()
                "{i}{b}THE BATHROOM IS EMPTY"
                b "{i}Hm..probably she is at the bedroom.."
                extend "But why.."
                extend "\nWhat is she doing there..?"
                menu:
                    "Go to the bedroom":
                        b "{i}Let's find this out"
                        $ renpy.pause()
                        scene bg atHome33c5ps with Dissolve (2.0)
            "Check the bedroom":
                $ config.rollback_enabled = False
                $ renpy.pause()
                scene bg atHome31c3ps with Dissolve (2.0)
                $ renpy.pause()
                b "{i}What a view.."
                extend "Vicky's on her knees.."
                $ renpy.pause()
                b "{i}I wonder what is she doing over there..?"
                menu:
                    "Ask":
                        b "Hey, Vicky.."
                        extend "Do you need some help..?"
                scene bg atHome32c4ps with fade
                $ renpy.pause()
                v "Oh..?!"
                extend " No.."
                $ renpy.pause()
                v "I didn't hear you come in.."
                b "The door was opened so.."
                scene bg atHome33c5ps with fade
        $ renpy.pause()
        v "Oh, [bro]..You scared me.."
        menu:
            "What are you doing here ?":
                v "Ahm..I.."
        v "I was checking.."
        extend "Ahm.."
        extend "If there is some of my.."
        b ".."
        v "Maybe I left some of my lingerie here.."
        extend "\nYou know..by any chance.."
        b "Good point."
        extend " Especially since Julie will be sleeping at this room..and.."
        extend "\nShe has found your panties on the back seat of the car.."
        v "Oh, I hope it didn't cause any problems.."
        b "It was okay..So have you found anything in the room ?"
        v "No..I guess the room is good to go.."
        extend "No worries.."
        b "Good.."
        $ renpy.pause()
        b "Look..Ahm..Thank you for playing along with the girlfriend role.."
        extend "\nI appreciate it.."
        v "Don't mention it.."
        b "And also thank you for the tomorrow's excursion for Julie.."
        extend "\nI couldn't show her all this girlish places better than you anyway.."
        v "It is okay. You paid for my time anyway."
        v "How the time is spent is a whole different story altogether.."
        $ renpy.pause()
        v "By the way how is Julie..?"
        b "I guess she is fine..We slightly quarreled and she went for a walk.."
        b "But she will be okay, she is not a whiny girl.."
        v "That is good.."
        $ renpy.pause()
        b "Yeah..Sorry that you had to witness this [family] drama.."
        b "I tried to tell you yesterday that we need to stop seeing each other for some time because of Julie arrival.."
        b "But.."
        extend "It totally slipped my mind after the call.."
        extend "\nAnd after that general meeting.."
        $ renpy.pause()
        v "General meeting..? Is this from your work again..?"
        b "Yeah.."
        v "Would you tell me..?"
        b "Nevermind.."
        extend "There is no use of this information for you anyway.."
        v "I see.."
        extend "So you trust me enough to keep a company for your [sis].."
        extend "\nBut not enough to tell why exactly I need to look after her..?"
        $ ep2VickyTold = 0
        menu:
            "Tell":
                $ config.rollback_enabled = False
                $ ep2VickyTold += 1
                b "Okay.."
                b "I work for a very serious people.."
                extend "They have huge impact in this city.."
                b "But there is always a 'bigger fish'.."
                extend "\nAnd this one doesn't look like friendly at all.."
                b "It is hard to tell right now how it all will turn out.."
                b "But it is possible that the showdown will be in the city.."
                v "And what is your role in all this..?"
                b "I just do what needs to be done.."
            "Don't tell":
                $ config.rollback_enabled = False
                b "I'm sorry Vicky.."
                extend "It will be safer for you not to know it.."
                v "Is it so dangerous..?"
        "{b}{i}PHONE MESSAGE{/i}{/b}"
        scene bg atHome33c6_ps with fade
        $ renpy.pause()
        b "I need to go.."
        v ".."
        b "Come on, I'll give you a ride to the center.."
        v "Okay.."
        scene black with Dissolve (2.0)
        $ renpy.notify("Bu akşamdan sonra..")
        $ renpy.pause()
        scene bg m1c1ps with Dissolve (2.0)
        $ renpy.pause()
        b "{i}I'm just in time.."
        $ renpy.pause()
        b "{i}Main lights are off which means that security cameras are disabled for 10 minutes.."
        b "{i}Everything seems okay.."
        extend "Except.."
        extend "I don't see the supplier.."
        $ renpy.pause()
        b "{i}It is strange..We usually meet here at the loading area.."
        extend ""
        menu:
            "Look for the Supplier":
                b "{i}I'd better find him quick.."
        jump ep2m1

    screen ep2m1Scr:
        imagemap:
            ground "images/ep2/m1c1ps.png"
            hotspot (1424,522,132,57) clicked Return("spot") hovered ShowTransient("imgHider", img="images/ep2/m1c1_1ps.png") unhovered Hide("imgHider")
            hotspot (767,708,374,352) clicked Return("stairs") hovered ShowTransient("imgHider", img="images/ep2/m1c1_ps.png") unhovered Hide("imgHider")

    label ep2m1:
        call screen ep2m1Scr
        $ result = _return
        if result == "spot":
            b "{i}He must be somewhere nearby.."
        if result == "stairs":
            b "{i}This stairs lead to the exit.."
            extend "\nI have to take the package first.."
            jump ep2m1
        scene bg m1c6 with fade
        b "{i}Maybe he is at the office room.."
        extend "\nI don't have time for checking whole warehouse anyway.."
        jump ep2m2
        return

    screen ep2m2Scr:
        imagemap:
            ground "images/ep2/m1c6.png"
            hotspot (246,375,107,239) clicked Return("door") hovered ShowTransient("imgHider", img="images/ep2/m1c6_.png") unhovered Hide("imgHider")

    label ep2m2:
        call screen ep2m2Scr
        b "{i}I can't see anything from here.."
        extend "I need to get closer.."
        scene black with dissolve
        $ renpy.pause()
        menu:
            "Open the door":
                scene bg m3c8ps with fade
        "{b}Supplier:{/b}\nI wasn't aware of it..Since when it has changed ?"
        extend ""
        b "Hey.."
        scene bg m4c8ps with dissolve
        "{b}Supplier:{/b}\nEvening, [bro].."
        extend "Everything is ready.."
        b "Great.."
        $ renpy.pause()
        "{b}Supplier:{/b}\nLooks like it is the last time I'm helping your guys.."
        b "Why is that ?"
        "{b}Supplier:{/b}\nI'm pretty sure you know why.."
        extend "Take the package, see you later.."
        extend "\nMaybe.."
        $ config.rollback_enabled = True
        $ renpy.pause()
        menu:
            "Look inside":
                b "Who are you talking to here..?"
                "{b}Supplier:{/b}\n..."
                $ renpy.pause()
                scene bg m2c7ps with fade
                $ renpy.pause()
                rocco "..."
                b "..."
                "{b}Supplier:{/b}\nOkay, [bro], I think you'd better leave.."
                extend "\nDon't forget the package.."
                scene bg m4c8ps with fade
            "Take the package":
                b "Okay.."

        screen ep2m3Scr:
            imagemap:
                ground "images/ep2/m4c8ps.png"
                hotspot (1019,752,140,284) clicked Return("case") hovered ShowTransient("imgHider", img="images/ep2/m4c8_ps.png") unhovered Hide("imgHider")

        call screen ep2m3Scr
        b "Good buy, pal.."
        extend "Take care.."
        "{b}Supplier:{/b}\nYou too.."
        scene black with dissolve
        $ renpy.pause()
        scene bg m1c1ps with dissolve
        b "{i}It's time to go home.."

        screen ep2m4Scr:
            imagemap:
                ground "images/ep2/m1c1ps.png"
                hotspot (767,708,374,352) clicked Return("stairs") hovered ShowTransient("imgHider", img="images/ep2/m1c1_ps.png") unhovered Hide("imgHider")

        call screen ep2m4Scr
        scene black with Dissolve (2.0)
        $ renpy.notify("Bir an sonra..")
        $ renpy.pause()
        b "{i}I need to inform Coordinator that I received the package.."
        b "{i}They won't like what supplier said.."
        $ renpy.pause()
        b "{i}It will be better if I leave the package in the trunk.."
        extend "\nJulie must not see it"
        $ renpy.notify("Daha sonra evde..")
        $ renpy.pause()
        jump ep2atHome
        return

    label ep2atHome:
        scene bg atHome34c1ps with Dissolve (2.0)
        $ renpy.pause()
        b "{i}I hope Julie is already.."
        b "{i}What..?"
        $ renpy.pause()
        scene bg atHome35c5ps with fade
        $ renpy.pause()
        j "{i}Z-z-z..."
        $ renpy.pause()
        b "{i}Why is she sleeping here.."
        extend "\nShe probably forgot that I've prepared bedroom for her.."
        j "{i}Z-z-z..."
        $ renpy.pause()
        menu:
            "Come closer":
                scene bg atHome36c3ps with fade
        $ renpy.pause()
        b "{i}Poor thing probably tired after a rough day.."
        j "{i}Z-z-z..."
        b "{i}Long flight is really exhausting.."
        scene bg atHome36c2ps with fade
        $ renpy.pause()
        b "{i}From the other hand she will be sleeping very deeply.."
        j "{i}Z-z-z..."
        b "{i}But it is still better in the bedroom.."
        extend "The couch is not for young ladies that is for sure.."
        extend "\nBesides, I might need to go again.."
        j "{i}Z-z-z..."
        scene bg atHome37c4ps with fade
        $ renpy.pause()
        b "{i}I guess I'll have to carry her to the bedroom.."
        extend "\nHope she won't wake up.."
        j "{i}Z-z-z..."
        $ renpy.pause()
        menu:
            "Take her":
                scene black with Dissolve (2.0)
        b "{i}Okay.."
        extend "Carefully.."
        extend "\nNice and slow.."
        $ renpy.pause()
        b "{i}Here we go.."
        scene bg atHome38c6ps with Dissolve (2.0)
        $ renpy.pause()
        j "{i}Z-z.."
        b "{i}She is so light and tiny.."
        b "{i}Looks like her heavy temper 'weighs' more than her body.."
        $ renpy.pause()
        scene bg atHome39c7_ps with fade
        $ renpy.pause()
        j "{i}Z-z.."
        b "{i}Almost there, Julie.."
        $ renpy.pause()
        scene black with Dissolve (2.0)
        $ renpy.pause()
        jump ep2bedroom
        return

    label ep2bedroom:
        menu:
            "Lay her on the bed":
                b "{i}That's it.."
                extend "Like this.."
        b "{i}Much better.."
        scene bg atHome40c1ps with Dissolve (2.0)
        $ renpy.pause()
        j "{i}Z-z.."
        $ renpy.pause()
        menu:
            "Confess":
                b "{b}{i}Whispering:{/i}{/b}\nI'm sorry, Julie.."
                extend "I know why you're so mad at me.."
        b "{b}{i}Whispering:{/i}{/b}\nIf you only knew.."
        scene bg atHome41c1ps with dissolve
        $ renpy.pause()
        b "{b}{i}Whispering:{/i}{/b}\nEverything I've been doing and.."
        extend "been behaving like that.."
        extend "\nIs solely for your safety.."
        scene bg atHome41c2ps with fade
        $ renpy.pause()
        j "{i}Z-z.."
        b "{b}{i}Whispering:{/i}{/b}\nI'll never forgive myself if.."
        extend "something bad happens with you or [mom] because of me.."
        $ renpy.pause()
        scene bg atHome41c7ps with fade
        $ renpy.pause()
        b "{b}{i}Whispering:{/i}{/b}\nI didn't want this kind of life.."
        extend "\nIt is unpredictable and dangerous.."
        extend "\nEspecially for those who you love.."
        scene bg atHome41c1ps with fade
        $ renpy.pause()
        b "{b}{i}Whispering:{/i}{/b}\nUnfortunately..life is unfair.."
        extend "and it is not about what we want.."
        extend "\nIt is about what we have to deal with.."
        $ renpy.pause()
        b "{b}{i}Whispering:{/i}{/b}\nMaybe one day I'll tell you everything.."
        extend "I hope you will understand.."
        scene bg atHome40c1ps with dissolve
        b "{b}{i}Whispering:{/i}{/b}\nBut not today.."
        extend "Today I want you to know that.."
        extend "\nI will do everything to protect you and [mom].."
        extend "\nWhatever it takes.."
        scene bg atHome41c3ps with fade
        $ renpy.pause()
        j "{i}Z-z.."
        $ renpy.pause()
        menu:
            "Come closer":
                scene bg atHome42c3ps with dissolve
                $ renpy.pause()
                b "{i}It is already late.."
                extend "I guess I need to leave her sleep.."
        j "{i}Z-z.."
        b "{i}Oh..One last thing.. "
        $ renpy.pause()
        menu:
            "Touch her hair":
                $ renpy.pause()
                scene bg atHome43c3ps with Dissolve (1.0)
        scene bg atHome44c3ps with Dissolve(1.0)
        $ renpy.pause()
        b "{i}That's better.."
        scene bg atHome45c3ps with dissolve
        j "{i}z-z.."
        $ renpy.pause()
        b "{i}She is so cute and innocent.."
        extend "\nLike a little angel.."
        $ renpy.pause()

        $ config.rollback_enabled = False
        $ ep2kissForehead = 0
        $ ep2kissLips = 0
        $ ep2touchBoobie = 0

        menu ep2Julie:
            "Kiss lips":
                $ config.rollback_enabled = False
                $ ep2kissLips += 1
                $ renpy.pause()
                scene bg atHome48c3ps with Dissolve (0.75)
                scene bg atHome48c3ps with Fade(.25, 0, .75, color="#FF69B4")
                $ renpy.pause()
                b "{i}Wow.."
                extend "That's amazing.."
                $ renpy.pause()
                j "{i}z-z.."
                b "{i}Her lips are so soft and sweet.."
                extend "\nUnbelievable.."
                $ renpy.pause()
                j "{i}z.."
                b "{i}I wonder how it will feel if I use my tongue.."
                extend "Or.."
                extend "\nNo..Probably it would be too much.."
                j "{i}z.."
                $ renpy.pause()
                menu:
                    "Use tongue":
                        $ config.rollback_enabled = False
                        scene bg atHome48c3ps with Fade(.25, 0, .75, color="#FF69B4")
                        $ renpy.pause()
                        b "{i}Mmm.."
                        extend "That sweet and slippery tongue of hers.."
                        extend ""
                        extend "\nIncredible.."
                        j "{i}z.."
                        $ renpy.pause()
                        b "{i}I know one more thing.."
                        extend "Which could be even more soft and wet.."
                        $ renpy.pause()
                        menu:
                            "Touch pussy":
                                $ renpy.pause()
                                b "{i}Right between her legs.."
                                extend "\nUnder this beautiful black panties.."
                                scene bg atHome47c3ps with Dissolve (1.5)
                        j "Mah.."
                        j "z.."
                        b "{i}Here we go.."
                        extend "Nice and slow.."
                        scene bg atHome47c3_ps with Dissolve (1.25)
                        scene bg atHome47c3ps with Dissolve (1.25)
                        scene bg atHome47c3_ps with Dissolve (1.25)
                        scene bg atHome47c3ps with Dissolve (1.25)
                        $ renpy.pause()
                        j "Mah.."
                        b "{i}I bet she put them on purpose.."
                        extend "\nWhy else wear black lingerie if you have no one to show it to.."
                        j "{i}z.."
                        scene bg atHome47c3_ps with Dissolve (1.25)
                        scene bg atHome47c3ps with Dissolve (1.25)
                        scene bg atHome47c3_ps with Dissolve (1.25)
                        scene bg atHome47c3ps with Dissolve (1.25)
                        $ renpy.pause ()
                        menu:
                            "Push tongue":
                                scene bg atHome47c3ps with Fade(.25, 0, .75, color="#FF69B4")
                                "{i}{b}You push it deeper in Julie's mouth..{/b}{/i}"
                        j "{i}Mh.."
                        b "{i}Yes.."
                        extend "You wanted to seduce me, didn't you..?"
                        j "{i}Mh.."
                        scene bg atHome47c3_ps with Dissolve (1.25)
                        scene bg atHome47c3ps with Dissolve (1.25)
                        scene bg atHome47c3_ps with Dissolve (1.25)
                        scene bg atHome47c3ps with Dissolve (1.25)
                        b "{i}Sleeping half naked on the couch and wearing sexy lingerie.."
                        extend ""
                        extend "\nKnowing that I'm going to sleep there.."
                        extend ""
                        scene bg atHome47c3_ps with Dissolve (1.25)
                        scene bg atHome47c3ps with Dissolve (1.25)
                        scene bg atHome47c3_ps with Dissolve (1.25)
                        scene bg atHome47c3ps with Dissolve (1.25)
                        b "{i}Naughty girl.."
                        j "{i}mh.."
                        menu:
                            "Speed up":
                                scene bg atHome47c3_ps with Dissolve (0.75)
                        scene bg atHome47c3ps with Dissolve (0.75)
                        scene bg atHome47c3_ps with Dissolve (0.75)
                        scene bg atHome47c3ps with Dissolve (0.75)
                        scene bg atHome47c3_ps with Dissolve (0.75)
                        scene bg atHome47c3ps with Dissolve (0.75)
                        scene bg atHome47c3_ps with Dissolve (0.75)
                        j ".."
                        b "{i}Oh..I feel how this pussy is getting more wet.."
                        extend "\nSoon these panties will be completely soaked.."
                        scene bg atHome47c3ps with Dissolve (0.75)
                        scene bg atHome47c3_ps with Dissolve (0.75)
                        scene bg atHome47c3ps with Dissolve (0.75)
                        scene bg atHome47c3_ps with Dissolve (0.75)
                        scene bg atHome47c3ps with Dissolve (0.75)
                        scene bg atHome47c3_ps with Dissolve (0.75)
                        b "{i}Holy shit.."
                        extend "My dick is hard as rock right now.."
                        $ renpy.pause()
                        scene bg atHome49c3ps with dissolve
                        $ renpy.pause()
                        b "{i}How do you like if shove my finger right in your sweet little pussy, Julie.."
                        extend "\nI bet you will beg for something more thick afterwards.."
                        scene bg atHome49c3_ps with Dissolve (0.75)
                        scene bg atHome49c3ps with Dissolve (0.75)
                        scene bg atHome49c3_ps with Dissolve (0.75)
                        scene bg atHome49c3ps with Dissolve (0.75)
                        scene bg atHome49c3_ps with Dissolve (0.75)
                        scene bg atHome49c3ps with Dissolve (0.75)
                        b "{i}But I want you to say it yourself.."
                        extend "\nI'm going to tease you until you beg me to shove it in.."
                        menu:
                            "Speed up":
                                scene bg atHome49c3_ps with Dissolve (0.5)
                        scene bg atHome49c3ps with Dissolve (0.5)
                        scene bg atHome49c3_ps with Dissolve (0.5)
                        scene bg atHome49c3ps with Dissolve (0.5)
                        scene bg atHome49c3_ps with Dissolve (0.5)
                        scene bg atHome49c3ps with Dissolve (0.5)
                        b "{i}Here it goes, little [sis].."
                        extend "\nJust say 'Please stick it in, [brother]' and come for me.."
                        b "{i}I know you're not sleeping anymore.."
                        menu:
                            "Speed up":
                                scene bg atHome49c3_ps with Dissolve (0.25)
                        scene bg atHome49c3ps with Dissolve (0.25)
                        scene bg atHome49c3_ps with Dissolve (0.25)
                        scene bg atHome49c3ps with Dissolve (0.25)
                        scene bg atHome49c3_ps with Dissolve (0.25)
                        scene bg atHome49c3ps with Dissolve (0.25)
                        scene bg atHome49c3_ps with Dissolve (0.25)
                        scene bg atHome49c3ps with Dissolve (0.25)
                        b "{i}Come for me.."
                        extend "Come for your [brother] like a little slut that you are !"
                        scene bg atHome49c3_ps with Dissolve (0.25)
                        scene bg atHome49c3ps with Dissolve (0.25)
                        scene bg atHome49c3_ps with Dissolve (0.25)
                        scene bg atHome49c3ps with Dissolve (0.25)
                        scene bg atHome49c3_ps with Dissolve (0.25)
                        scene bg atHome49c3ps with Dissolve (0.25)
                        scene bg atHome60c3ps with Fade (.125, 0, .125, color="#C4C4C4")
                        scene bg atHome60c3ps with vpunch
                        scene bg atHome60c3ps with vpunch
                        scene bg atHome60c3ps with vpunch
                        j "GET YOUR FILTHY HANDS OFF ME YOU FUCKING CREEP !!!"
                        jump gameOver
                    "Don't use":
                        $ config.rollback_enabled = False
                        b "{i}No wet kisses.."
                        extend "\nOnly tender and sweet touching of lips.."
                        $ renpy.pause()
                        j "{i}z.."
                        j "{i}.."
                        b "{i}Oh, Julie.."
                        extend "I can feel your warm breath on my face.."
                        extend "{i}\nI almost forgot what a kiss looks like.."
                        j "{i}.."
                        j "{i}Mh..?"
                        scene bg atHome50c3ps with Dissolve (1.0)
                        $ renpy.pause()
                        b "{i}Oops.."
                        extend "\nShe's woke up.."
                        scene bg atHome51c3ps with Dissolve (1.0)
                        $ renpy.pause()
                        j "[bro].."
                        b "{i}That is awkward.."
                        extend "What should I say..?"
                        menu:
                            "Keep silent":
                                $ config.rollback_enabled = False
                                b ".."
                                j ".."
                                j "What do you think you're doing..?"
                                b "I.."
                                extend "I don't know what I was thinking.."
                                j ".."
                                b "I just wanted to say good night..and.."
                                j "And..?"
                                b "I..I'm sorry.."
                                extend "\nI think I'd better leave.."
                                b "Good night.."
                                menu:
                                    "Leave":
                                        scene black with Dissolve (2.0)
                                        $ renpy.pause()
                                        jump ep2morning
                            "Apologize":
                                $ config.rollback_enabled = False
                                b "I'm sorry, Julie.."
                                b "I just wanted to say good night and wish you sweet dreams.."
                                j "What does it have to do with my lips anyway..?!"
                                b "I'm sorry.."
                                j "It was pretty creepy.."
                                b "I.."
                                extend "I didn't mean it like that.."
                                b "I wanted to give you a little good night kiss that's all.."
                                j "Well you did.."
                                extend "Even too much.."
                                $ renpy.pause()
                                b "I think I'd better leave.."
                                b "Good night.."
                                menu:
                                    "Leave":
                                        scene black with Dissolve (2.0)
                                        $ renpy.pause()
                                        jump ep2morning
                jump ep2morning
            "Touch boobies" if ep2touchBoobie == 0:
                $ config.rollback_enabled = False
                $ ep2touchBoobie += 1
                b "{i}Do I really want to do this..?"
                extend "\nShe is my [sis] after all.."
                $ renpy.pause()
                menu:
                    "Yes":
                        $ ep2touchBoobie += 1
                        $ renpy.pause()
                        scene bg atHome53c3ps with dissolve
                        $ renpy.pause()
                        b "{i}Wow.."
                        extend "What a nice little boobie.."
                        j "{i}z-z.."
                        $ renpy.pause()
                        b "{i}I think it won't be a big deal if I play with it for a little.."
                        $ renpy.pause()
                        menu:
                            "Play with it":
                                scene bg atHome54c3_ps with Dissolve (1.0)
                        $ renpy.pause()
                        j "{i}z-z.."
                        b "{i}Holy shit.."
                        extend "Small elastic titties.."
                        extend "\All natural.."
                        scene bg atHome55c3_ps with dissolve
                        $ renpy.pause()
                        b "{i}Her skin is so smooth.."
                        scene bg atHome54c3_ps with Dissolve (0.75)
                        scene bg atHome55c3_ps with Dissolve (0.75)
                        scene bg atHome54c3_ps with Dissolve (0.75)
                        scene bg atHome55c3_ps with Dissolve (0.75)
                        scene bg atHome54c3_ps with Dissolve (0.75)
                        scene bg atHome55c3_ps with Dissolve (0.75)
                        b "{i}I can't believe I'm doing this.."
                        j "{i}z-z.."
                        scene bg atHome54c3_ps with Dissolve (0.75)
                        scene bg atHome55c3_ps with Dissolve (0.75)
                        scene bg atHome54c3_ps with Dissolve (0.75)
                        scene bg atHome55c3_ps with Dissolve (0.75)
                        b "{i}They are as good as Vicky's.."
                        extend "\nBut much younger.."
                        j "{i}z-z.."
                        scene bg atHome54c3_ps with Dissolve (0.75)
                        scene bg atHome55c3_ps with Dissolve (0.75)
                        scene bg atHome54c3_ps with Dissolve (0.75)
                        scene bg atHome55c3_ps with Dissolve (0.75)
                        b "{i}It will be unforgivable if I don't squeeze them at least slightly.."
                        scene bg atHome54c3_ps with Dissolve (0.75)
                        scene bg atHome55c3_ps with Dissolve (0.75)
                        scene bg atHome54c3_ps with Dissolve (0.75)
                        scene bg atHome55c3_ps with Dissolve (0.75)
                        menu:
                            "Squeeze":
                                scene bg atHome54c3ps with Dissolve (0.75)
                        j "{i}Ah.."
                        b "{i}Oops.."
                        $ renpy.pause()
                        $ renpy.pause()
                        j "{i}z-.."
                        b "{i}Looks like it's okay to continue.."
                        scene bg atHome55c3ps with Dissolve (0.75)
                        scene bg atHome54c3ps with Dissolve (0.75)
                        scene bg atHome55c3ps with Dissolve (0.75)
                        scene bg atHome54c3ps with Dissolve (0.75)
                        b "{i}I can feel the warm from her breast in my palm.."
                        extend "\nWhat a pleasent feeling.."
                        scene bg atHome55c3ps with Dissolve (0.75)
                        scene bg atHome54c3ps with Dissolve (0.75)
                        scene bg atHome55c3ps with Dissolve (0.75)
                        scene bg atHome54c3ps with Dissolve (0.75)
                        b "{i}Definitely better than Vicky's.."
                        scene bg atHome55c3ps with Dissolve (0.75)
                        j "{i}Oh.."
                        j "{i}z-.."
                        j "{i}z.."
                        "{i}{b}Julie starts to breath heavily..{/b}{i}"
                        scene bg atHome56c3ps with dissolve
                        $ renpy.pause()
                        b "{i}Wow..she is getting into it.."
                        b "{i}Those nipples have swelled so fast.."
                        b "{i}I wish I could suck on them right now.."
                        j "{i}z.."
                        b "{i}But what if she wakes up..?"
                        extend "\nIt will be the end.."
                        b "{i}Damn..the temptation is so strong.."
                        extend "\nMy dick is already hard.."
                        b "{i}Maybe she will help me get off.."
                        b "{i}What should I do..?"
                        menu:
                            "Continue":
                                b "{i}Nah..She won't wake up.."
                                extend "She's tired and sleeps very deep.."
                                b "{i}Anyway, by the time she wakes up I will have her aroused enough.."
                                extend "\nShe couldn't resist me.."
                                extend "\nThere is nothing to worry about.."
                                scene bg atHome56c3_ps with Dissolve (0.75)
                                scene bg atHome56c3ps with Dissolve (0.75)
                                scene bg atHome56c3_ps with Dissolve (0.75)
                                scene bg atHome56c3ps with Dissolve (0.75)
                                j "Ah..."
                                b "{i}Yes..Good girl.."
                                scene bg atHome56c3_ps with Dissolve (0.75)
                                scene bg atHome56c3ps with Dissolve (0.75)
                                scene bg atHome56c3_ps with Dissolve (0.75)
                                scene bg atHome56c3ps with Dissolve (0.75)
                                b "{i}We will have a lot of fun when you wake up.."
                                scene bg atHome56c3_ps with Dissolve (0.75)
                                scene bg atHome56c3ps with Dissolve (0.75)
                                scene bg atHome56c3_ps with Dissolve (0.75)
                                scene bg atHome56c3ps with Dissolve (0.75)
                                scene bg atHome56c3_ps with Dissolve (0.75)
                                scene bg atHome56c3ps with Dissolve (0.75)
                                j "Ooh.."
                                j ".."
                                scene bg atHome57c3ps with dissolve
                                $ renpy.pause()
                                j ".."
                                b "Wake up, Julie.."
                                j "Whaaat.."
                                extend "[bro]..?"
                                scene bg atHome57c3_ps with Dissolve (1.0)
                                $ renpy.pause()
                                b "Yes, baby.."
                                extend ""
                                b "Did you like me playing with your boobie..?"
                                extend "\nI have something for my little [sis] to play with as well.."
                                menu:
                                    "Open the fly":
                                        play sound "music/sounds/jeansZipper.mp3"
                                        "{b}{i}Zipper opens"
                                scene bg atHome58c3ps with dissolve
                                j "What ?! No !"
                                extend " Oh my god, [bro]..What are you doing ?!.."
                                j "Please don't hurt me.."
                                $ renpy.pause()
                                b "I won't hurt you, Julie.. I just want to play.."
                                scene bg atHome58c3ps with hpunch
                                j "HEEEEEEEEEEEEEEEEEEEEELP !!!"
                                jump gameOver
                            "Stop":
                                b "{i}No..that is enough.."
                                extend "What was I thinking..?!"
                                extend "\nShe is my lovely little [sis].."
                                $ renpy.pause()
                                b "{i}I'd better leave her alone.."
                                menu:
                                    "Leave":
                                        scene bg atHome59c3ps with Dissolve (1.5)
                                        $ renpy.pause()
                                        j "{i}z.."
                                        scene black with Dissolve (2.0)
                                        $ renpy.pause()
                                        jump ep2morning
                    "No":
                        jump ep2Julie
                jump ep2morning
            "Kiss forehead":
                $ config.rollback_enabled = False
                $ ep2kissForehead += 1
                scene bg atHome46c3ps with dissolve
                $ renpy.pause()
                j "z-.."
                $ renpy.pause()
                scene bg atHome45c3ps with dissolve
                $ renpy.pause()
                b "Good night, little one.."
                extend "\nSweet dreams.."
                extend ""
                j "z.."
                $ renpy.pause()
                menu:
                    "Leave":
                        scene bg atHome52c3ps with Dissolve (1.5)
                        $ renpy.pause()
                        j ".."
                        $ renpy.pause()
                        scene black with Dissolve (2.0)
                        $ renpy.pause()
                        jump ep2morning
        return

    label ep2morning:
        $ config.rollback_enabled = True
        $ renpy.notify ("Sonraki Sabah..")
        $ renpy.pause()
        j "[bro].."
        extend "Are you sleeping..?"
        $ renpy.pause()
        j "Wake up.."
        scene bg atHome61c1_ps with Dissolve (2.0)
        b "{i}Yawning.."
        extend "\nOh..Whaat..What's the matter..?"
        $ renpy.pause()
        scene bg atHome61c1ps with Dissolve (1.5)
        $ renpy.pause ()
        j "Good morning, [brother].."
        b "Morning, Julie.."
        extend "I didn't hear you get up.."
        scene bg atHome62c2ps with fade
        $ renpy.pause ()
        j "Of course you didn't.."
        extend "\nYou were snoring like a big wild hog, ha-ha.."
        b "What ?!"
        extend "\nYou've got to be kidding me.."
        j "I'm serious.."
        menu:
            "Get up":
                scene bg atHome63c3ps with fade
        $ renpy.pause()
        j "Well, maybe not like a big hog.."
        extend "\nIt was more like a little one, ha-ha.."
        b "That is interesting.."
        extend "\nI didn't know that I do snore.."
        j "How would you know, ha-ha.."
        b "Strange..I usually sleep very lightly.."
        extend "\nI should have heard you walking.."
        j "Well..I tried to walk quietly on tiptoe.."
        extend "\nSo you can count it as an excuse.."
        $ renpy.pause ()
        if ep2kissForehead == 1:
            b "{i}Oh..What is going on with my head.."
            extend "\nWhere does this headache come from.."
            scene bg atHome64c3ps with dissolve
            j "By the way, I've made some breakfast for you.."
            extend "\nIt's on the plate.."
            $ renpy.pause()
            scene bg atHome64c3_ps with dissolve
            b "Oh..Thank you Julie.."
            extend "It's very nice of you "
            scene bg atHome63c3_ps with dissolve
            j "You are welcome, [bro].."
            extend "\nIt is least I can do.."
            j "I don't want to be freeloader, you know.."
            b "Thanks.."
            $ renpy.pause()
            b "Julie, why did you fall asleep here on the couch yesterday..?"
            extend "\nYou don't like the bedroom or something..?"
            j "Of course not.."
            extend "I just.."
            extend "\nWas doing a video call with my friend.."
            j "And the Wi-Fi signal is more strong in this room.."
            b "Oh..I see.."
            j "Yeah, then I just dozed off.."
            $ renpy.pause()
            b "I had to carry you to the bedroom.."
            extend "\nHope you don't mind.."
            j "I've noticed.."
            extend "No, I don't mind.."
            extend "\nThank you for that by the way.."
            $ renpy.pause()
            j "Well, I guess I need to go.."
            extend "\nVicky is awaiting for me outside.."
            b "Vicky..?"
            j "Don't you remember ?"
            extend "\nWe are going for a girlish trip across the city.."
            j "That is why I woke you up.."
            extend "\nSo that you do not worry where am I.."
            b "Oh, right.."
            extend "Almost forgot.."
            j "Yep.."
            b "Well..Even though a girlish trip sounds interesting, but I think I'll pass.."
            j "Who said we are inviting you, ha-ha.."
            b "Just kidding.."
            scene bg atHome65c3ps with dissolve
            j "Okay, [bro]..See you later.."
            b "Say hello to Vicky..And.."
            extend "\nBe careful.."
            j "I will.."
            extend "Bye.."
            scene black with Dissolve (2.0)
            jump ep2store
        else:
            scene bg atHome63c3_ps with dissolve
            b "{i}Oh..What is going on with my head.."
            extend "\nWhere does this headache come from.."
            $ renpy.pause()
            menu:
                "Talk about yesterday" if ep2kissLips == 1:
                    b "Julie, why did you fall asleep here on the couch yesterday..?"
                    extend "\nYou don't like the bedroom or something..?"
                    j "Oh no.."
                    extend "\nI was on my phone.."
                    j "And Wi-Fi signal is more strong in this room.."
                    extend "\nThat is it.."
                    j "Then I just dozed off.."
                    b "Oh..I see.."
                    extend "\nAbout what happened in the bedroom.."
                    j "Oh, forget about it.."
                    extend "Although it was creepy..It's not a big deal.."
                    extend "\nJust don't do that again, okay ?"
                    b "Okay.."
                    j "The bed in the bedroom is indeed much comfortable than this couch.."
                    j ".."
                    b ".."
            j "Well, I guess I need to go.."
            extend "\nVicky is awaiting for me outside.."
            b "Vicky..?"
            j "Don't you remember ?"
            extend "\nWe are going for a girlish trip across the city.."
            j "That is why I woke you up.."
            b "Oh, right.."
            extend "Almost forgot.."
            j "Yep.."
            b "Well..Even though a girlish trip sounds interesting, but I think I'll pass.."
            j "Ha-ha, who said we are inviting you.."
            b "Just kidding.."
            scene bg atHome65c3ps with dissolve
            j "Okay, [bro]..Bye.."
            b "Say hello to Vicky..And.."
            extend "\nBe careful.."
            j "I will.."
            scene black with Dissolve (2.0)
            jump ep2store
        return

    label ep2store:
        $ renpy.notify("Daha Sonra Butikte..")
        $ renpy.pause()
        scene bg fr1c2ps with Dissolve (2.0)
        $ renpy.pause()
        v "Here we are, Julie. "
        extend "This is the place.."
        j "Nice, I like it here !"
        $ renpy.pause()
        scene bg fr1c5ps with fade
        $ renpy.pause()
        v "So.."
        extend "Have you been to stores like this before..?"
        j "No, not really."
        extend " The clothes in such stores are very expensive"
        v "That is true, but don't worry.."
        extend "Your [brother] took care about it.."
        j "Really ?! That is cool !"
        v "Yeah..So.."
        extend "\nIt is pretty straightforward: "
        v "You can pick any clothes you want, don't forget to check that the size is yours.."
        v "Then you go to any fitting room.."
        extend ""
        extend "\nJust make sure that it is unoccupied.."
        j "The doors don't close from the inside ?"
        v "No.."
        extend "Administration has removed all door locks recently, due to.."
        extend "\nAhm.."
        extend "\nFrequent public sex incidents in the fitting rooms..So.."
        j "Great !"
        v "..."
        j "I mean.."
        extend "gosh.."
        extend "what a perverts.."
        v "Well, that is basically it. Let me know if you need something, okay ?"
        j "Yeah, sure.."
        scene black with Dissolve(2.0)
        $ renpy.notify("Bir süre sonra..")
        $ renpy.pause()
        scene bg fr3c7_ps with Dissolve (2.0)
        $ renpy.pause()
        v "{i}Well, these panties look good.."
        extend "\nThe fabric is pleasant to touch.."
        v "{i}Looks like it is silk.."
        extend "\nI guess I'll take them along with the bra"
        scene bg fr4c9_ps with hpunch
        j "Hold it right there !"
        v "What ?!"
        j "Ha-ha.."
        scene fr5c6_ps with fade
        $ renpy.pause()
        j "This is Vice Squad Police !"
        extend " Ha-ha.."
        v "Oh..I see.."
        extend "\nLet's play.."
        j "No games here ! \nSpecial officer Julie is at work !"
        extend " Ha-ha.."
        $ renpy.pause()
        v "But.."
        extend "Officer Julie.."
        scene bg fr6c10_ps with fade
        $ renpy.pause()
        v "Did I.."
        extend "violate something..?"
        $ renpy.pause()
        scene bg fr9c2ps with hpunch
        v "Ooh !"
        j "Of course you did !"
        extend " Ha-ha.."
        $ renpy.pause()
        scene bg fr10c3ps with fade
        $ renpy.pause()
        v "What exactly did I violate, officer..?"
        j "It is illegal to wear such beautiful breasts !"
        $ renpy.pause()
        scene bg fr8c1ps with fade
        $ renpy.pause()
        j "Especially naked !"
        $ renpy.pause()
        v "I'm sorry, officer.."
        extend "I didn't know that.."
        scene bg fr10c3ps with fade
        j "This.."
        scene bg fr7c3ps with dissolve
        v "Ah.."
        j "This is extremely dangerous for others !"
        $ renpy.pause()
        v "Can we..do something about it, officer..?"
        scene bg fr8c1ps with fade
        j "I will have to search you.."
        extend "I suspect that you hide something even more dangerous.."
        v "No..I don't hide anything.."
        j "Do you refuse to cooperate ?!"
        scene bg fr9c4_ps with fade
        $ renpy.pause()
        v "Ah..No, officer..I don't.."
        extend "\nIf you insist.."
        $ renpy.pause()
        scene bg fr7c3ps with fade
        j "That is better.."
        extend "Now.."
        extend "I wonder.."
        $ renpy.pause()
        scene rooms3_ps with Dissolve (0.75)
        v "Oh.."
        $ renpy.pause()
        j "What are you hiding under these panties ?"
        $ renpy.pause()
        j "I bet there is something interesting !"
        scene rooms3ps with dissolve
        v "Ah.."
        $ renpy.pause()
        scene bg fr8c1_ps with fade
        $ renpy.pause()
        j "Am I right..?"
        jump episode3
        return

####################################################EPISODE_3##################################################

    image bg cafe1c2ps = "images/ep3/cafe1c2ps.png"
    image bg cafe1c3ps = "images/ep3/cafe1c3ps.png"
    image bg cafe2c4ps = "images/ep3/cafe2c4ps.png"
    image bg cafe3c1_ps = "images/ep3/cafe3c1_ps.png"
    image bg cafe3c1ps = "images/ep3/cafe3c1ps.png"
    image bg cafe4c1ps = "images/ep3/cafe4c1ps.png"
    image bg cafe5c4_ps = "images/ep3/cafe5c4_ps.png"
    image bg cafe5c4ps = "images/ep3/cafe5c4ps.png"
    image bg cafe6c4_ps = "images/ep3/cafe6c4_ps.png"
    image bg cafe6c4ps = "images/ep3/cafe6c4ps.png"
    image bg cafe7c1ps = "images/ep3/cafe7c1ps.png"
    image bg cafe7c4_ps = "images/ep3/cafe7c4_ps.png"
    image bg cafe7c4ps = "images/ep3/cafe7c4ps.png"

    image bg fClub4c3ps = "images/ep3/fClub4c3ps.png"
    image bg fClub5c2ps = "images/ep3/fClub5c2ps.png"
    image bg fClub6c1ps = "images/ep3/fClub6c1ps.png"
    image bg fClub7c2ps = "images/ep3/fClub7c2ps.png"
    image bg fClub8c3ps = "images/ep3/fClub8c3ps.png"
    image bg fClub8c4ps = "images/ep3/fClub8c4ps.png"
    image bg fClub9c3ps = "images/ep3/fClub9c3ps.png"
    image bg fClub10c5ps = "images/ep3/fClub10c5ps.png"
    image bg fClub11c5ps = "images/ep3/fClub11c5ps.png"
    image bg fClub12c5ps = "images/ep3/fClub12c5ps.png"
    image bg fClub13c6_ps = "images/ep3/fClub13c6_ps.png"
    image bg fClub13c6ps = "images/ep3/fClub13c6ps.png"
    image bg fClub14c6_1ps = "images/ep3/fClub14c6_1ps.png"
    image bg fClub14c6_2ps = "images/ep3/fClub14c6_2ps.png"
    image bg fClub14c6ps = "images/ep3/fClub14c6ps.png"
    image bg fClub14c6_ps = "images/ep3/fClub14c6_ps.png"
    image bg fClub15c6_ps = "images/ep3/fClub15c6_ps.png"
    image bg fClub15c6ps = "images/ep3/fClub15c6ps.png"
    image bg fClub16c8ps = "images/ep3/fClub16c8ps.png"
    image bg fClub17c8ps = "images/ep3/fClub17c8ps.png"
    image bg fClub18c7_ps = "images/ep3/fClub18c7_ps.png"
    image bg fClub18c7ps = "images/ep3/fClub18c7ps.png"
    image bg fClub19c7ps = "images/ep3/fClub19c7ps.png"
    image bg fClub20c9ps = "images/ep3/fClub20c9ps.png"
    image bg fClub21c11ps = "images/ep3/fClub21c11ps.png"
    image bg fClub22c15ps = "images/ep3/fClub22c15ps.png"
    image bg fClub23c16ps = "images/ep3/fClub23c16ps.png"
    image bg fClub24c16ps = "images/ep3/fClub24c16ps.png"
    image bg fClub25c10ps = "images/ep3/fClub25c10ps.png"
    image bg fClub26c10ps = "images/ep3/fClub26c10ps.png"
    image bg fClub27c10ps = "images/ep3/fClub27c10ps.png"

    image bg fr12c3ps = "images/ep3/fr12c3ps.png"
    image bg fr13c10ps = "images/ep3/fr13c10ps.png"
    image bg fr14c4ps = "images/ep3/fr14c4ps.png"
    image bg fr15c2ps = "images/ep3/fr15c2ps.png"
    image bg fr16c12ps = "images/ep3/fr16c12ps.png"
    image bg fr17c1_ps = "images/ep3/fr17c1_ps.png"
    image bg fr17c1ps = "images/ep3/fr17c1ps.png"
    image bg fr18c1_1ps = "images/ep3/fr18c1_1ps.png"
    image bg fr18c1_2ps = "images/ep3/fr18c1_2ps.png"
    image bg fr18c1_ps = "images/ep3/fr18c1_ps.png"
    image bg fr18c1ps = "images/ep3/fr18c1ps.png"
    image bg fr19c12_ps = "images/ep3/fr19c12_ps.png"
    image bg fr19c12ps = "images/ep3/fr19c12ps.png"
    image bg fr20c12ps = "images/ep3/fr20c12ps.png"
    image bg fr21_c4ps = "images/ep3/fr21_c4ps.png"
    image bg fr21c4_ps = "images/ep3/fr21c4_ps.png"
    image bg fr21c4ps = "images/ep3/fr21c4ps.png"
    image bg fr22c5ps = "images/ep3/fr22c5ps.png"
    image bg fr23c6ps = "images/ep3/fr23c6ps.png"
    image bg fr24c4ps = "images/ep3/fr24c4ps.png"

    image bg hallway7c4ps = "images/ep3/hallway7c4ps.png"
    image bg hallway8c5ps = "images/ep3/hallway8c5ps.png"
    image bg hallway9c5_ps = "images/ep3/hallway9c5_ps.png"
    image bg hallway10c5ps = "images/ep3/hallway10c5ps.png"

    image bg nApt0c3ps = "images/ep3/nApt0c3ps.png"
    image bg nApt1c3ps = "images/ep3/nApt1c3ps.png"
    image bg nApt2c2ps = "images/ep3/nApt2c2ps.png"
    image bg nApt3c2ps = "images/ep3/nApt3c2ps.png"
    image bg nApt4c4_Cps = "images/ep3/nApt4c4_Cps.png"
    image bg nApt4c4_Lps = "images/ep3/nApt4c4_Lps.png"
    image bg nApt4c4ps = "images/ep3/nApt4c4ps.png"
    image bg nApt5c5ps = "images/ep3/nApt5c5ps.png"
    image bg nApt6c1ps = "images/ep3/nApt6c1ps.png"
    image bg nApt6c7ps = "images/ep3/nApt6c7ps.png"
    image bg nApt7c6ps = "images/ep3/nApt7c6ps.png"
    image bg nApt8c6ps = "images/ep3/nApt8c6ps.png"
    image bg nApt9c9ps = "images/ep3/nApt9c9ps.png"
    image bg nApt10c8ps = "images/ep3/nApt10c8ps.png"
    image bg nApt11c11ps = "images/ep3/nApt11c11ps.png"
    image bg nApt12c10ps = "images/ep3/nApt12c10ps.png"
    image bg nApt12c12ps = "images/ep3/nApt12c12ps.png"
    image bg nApt13c14ps = "images/ep3/nApt13c14ps.png"
    image bg nApt14c14ps = "images/ep3/nApt14c14ps.png"
    image bg nApt15c10ps = "images/ep3/nApt15c10ps.png"
    image bg nApt16c13ps = "images/ep3/nApt16c13ps.png"
    image bg nApt17c13ps = "images/ep3/nApt17c13ps.png"
    image bg nApt18c14ps = "images/ep3/nApt18c14ps.png"
    image bg nApt19c14ps = "images/ep3/nApt19c14ps.png"
    image bg nApt20c14ps = "images/ep3/nApt20c14ps.png"
    image bg nApt21c15ps = "images/ep3/nApt21c15ps.png"
    image bg nApt22c10ps = "images/ep3/nApt22c10ps.png"
    image bg nApt23c10ps = "images/ep3/nApt23c10ps.png"

    image bg store1c3ps = "images/ep3/store1c3ps.png"
    image bg store2c4ps = "images/ep3/store2c4ps.png"
    image bg store3c2ps = "images/ep3/store3c2ps.png"
    image bg store3c4ps = "images/ep3/store3c4ps.png"
    image bg store3c4psGum = "images/ep3/store3c4psGum.png"
    image bg store3c4psLeft = "images/ep3/store3c4psLeft.png"
    image bg store3c4psRight = "images/ep3/store3c4psRight.png"
    image bg store4c5ps = "images/ep3/store4c5ps.png"
    image bg store4c5psChips = "images/ep3/store4c5psChips.png"
    image bg store4c5psLeft = "images/ep3/store4c5psLeft.png"
    image bg store4c5psMid = "images/ep3/store4c5psMid.png"
    image bg store4c5psPancake = "images/ep3/store4c5psPancake.png"
    image bg store4c5psSpray = "images/ep3/store4c5psSpray.png"
    image bg store5c6ps = "images/ep3/store5c6ps.png"
    image bg store5c6psMid = "images/ep3/store5c6psMid.png"
    image bg store5c6psPaper = "images/ep3/store5c6psPaper.png"
    image bg store5c6psRight = "images/ep3/store5c6psRight.png"
    image bg store5c6psSyrup = "images/ep3/store5c6psSyrup.png"
    image bg store5c6psTowels = "images/ep3/store5c6psTowels.png"
    image bg store5c9f3_ps = "images/ep3/store5c9f3_ps.png"
    image bg store5c9f3leftps = "images/ep3/store5c9f3leftps.png"
    image bg store5c9f3ps = "images/ep3/store5c9f3ps.png"
    image bg store5c9f3rightps = "images/ep3/store5c9f3rightps.png"
    image bg store6c7f2_ps = "images/ep3/store6c7f2_ps.png"
    image bg store6c7f2leftps = "images/ep3/store6c7f2leftps.png"
    image bg store6c7f2ps = "images/ep3/store6c7f2ps.png"
    image bg store6c7f2rightps = "images/ep3/store6c7f2rightps.png"
    image bg store7c8f1_ps = "images/ep3/store7c8f1_ps.png"
    image bg store7c8f1_psH = "images/ep3/store7c8f1_psH.png"
    image bg store7c8f1_psMilk = "images/ep3/store7c8f1_psMilk.png"
    image bg store7c8f1ps = "images/ep3/store7c8f1ps.png"
    image bg store7c8f1psMilk = "images/ep3/store7c8f1psMilk.png"
    image bg store7c8f1rightps = "images/ep3/store7c8f1rightps.png"
    image bg store7c8f1rightpsMilk = "images/ep3/store7c8f1rightpsMilk.png"
    image bg store8c10f4_ps = "images/ep3/store8c10f4_ps.png"
    image bg store8c10f4_psH = "images/ep3/store8c10f4_psH.png"
    image bg store8c10f4_psMeat = "images/ep3/store8c10f4_psMeat.png"
    image bg store8c10f4leftps = "images/ep3/store8c10f4leftps.png"
    image bg store8c10f4leftpsMeat = "images/ep3/store8c10f4leftpsMeat.png"
    image bg store8c10f4ps = "images/ep3/store8c10f4ps.png"
    image bg store8c10f4psMeat = "images/ep3/store8c10f4psMeat.png"
    image bg store8c10f4rightps = "images/ep3/store8c10f4rightps.png"
    image bg store8c10f4rightpsMeat = "images/ep3/store8c10f4rightpsMeat.png"
    image bg store9c11f5_ps = "images/ep3/store9c11f5_ps.png"
    image bg store9c11f5_psEggs = "images/ep3/store9c11f5_psEggs.png"
    image bg store9c11f5_psH = "images/ep3/store9c11f5_psH.png"
    image bg store9c11f5leftps = "images/ep3/store9c11f5leftps.png"
    image bg store9c11f5leftpsEggs = "images/ep3/store9c11f5leftpsEggs.png"
    image bg store9c11f5ps = "images/ep3/store9c11f5ps.png"
    image bg store9c11f5psEggs = "images/ep3/store9c11f5psEggs.png"
    image bg store10c3ps = "images/ep3/store10c3ps.png"
    image bg store11c3ps = "images/ep3/store11c3ps.png"
    image bg store12c1ps = "images/ep3/store12c1ps.png"
    image bg store12c2ps = "images/ep3/store12c2ps.png"
    image bg store13c2_1ps = "images/ep3/store13c2_1ps.png"
    image bg store13c2_2ps = "images/ep3/store13c2_2ps.png"
    image bg store13c2_ps = "images/ep3/store13c2_ps.png"
    image bg store13c2ps = "images/ep3/store13c2ps.png"
    image bg store14c2ps = "images/ep3/store14c2ps.png"
    image bg store14c2ps = "images/ep3/store14c2ps.png"
    image bg store15c3_ps = "images/ep3/store15c3_ps.png"
    image bg store15c3ps = "images/ep3/store15c3ps.png"
    image bg store15c5ps = "images/ep3/store15c5ps.png"
    image bg store16c5ps = "images/ep3/store16c5ps.png"
    image bg store17c2_1ps = "images/ep3/store17c2_1ps.png"
    image bg store17c2_2ps = "images/ep3/store17c2_2ps.png"
    image bg store17c2_3ps = "images/ep3/store17c2_3ps.png"
    image bg store17c2_ps = "images/ep3/store17c2_ps.png"
    image bg store17c2ps = "images/ep3/store17c2ps.png"
    image bg store18c2_ps = "images/ep3/store18c2_ps.png"
    image bg store18c2ps = "images/ep3/store18c2ps.png"
    image bg store19c2_ps = "images/ep3/store19c2_ps.png"
    image bg store19c2ps = "images/ep3/store19c2ps.png"
    image bg store19c2ps = "images/ep3/store19c2ps.png"
    image bg store20c7ps = "images/ep3/store20c7ps.png"
    image bg store21c8ps = "images/ep3/store21c8ps.png"
    image bg store22c9ps = "images/ep3/store22c9ps.png"
    image bg store23c10ps = "images/ep3/store23c10ps.png"

    label episode3:
        scene rooms3ps with fade
        $ renpy.pause()
        scene bg fr12c3ps with Dissolve(0.75)
        v "Alright, Julie, that is enough, You won."
        scene bg fr13c10ps with fade
        $ renpy.pause()
        v "It's better stop this 'game' before we are thrown out of here."
        v "We don't need these problems."
        scene bg fr14c4ps with fade
        $ renpy.pause()
        j "Ha-ha, it was fun wasn't it ?"
        v "Maybe.."
        j "Come on, I know you were into it. Your nipples are hard !"
        v "A little bit. But it's just because it's cold out here."
        j "Yeah, right, ha-ha!"
        v "Alright, alright..You naughty girl, ha-ha!"
        scene bg fr15c2ps with fade
        $ renpy.pause()
        j "Do you like the outfit that I've found ? I haven't found any shoes for it, though."
        v "Yeah, there is no shoes in here, only clothing. But apart from that 'Sexy Cop' is an interesting choice, I like it."
        j "Look at these stockings, they are amazing. I already love this store !"
        v "Yes, great choice, men love stockings. It is win-win option if you want to seduce someone you like."
        j "I don't care if it's what men love or not, I'm interested in girls' opinion. What do you think ?"
        v "Oh..I see. Me personally love stockings too, very sexy.."
        j "Good, then it's decided, I'll buy them.."
        extend "I just need to take off this outfit."
        scene bg fr16c12ps with fade
        $ renpy.pause()
        v "Ahm, Julie..Wouldn't you rather use your own fitting room ?"
        j "Oh come on Vicky, don't be so grouchy. I've seen you naked, it will be fair if you see me as well."
        v "But Julie, the administration will kick us out when they see us naked in the same room."
        j "Don't worry, they won't."
        v "It is public order disturbance"
        scene bg fr17c1ps with fade
        $ renpy.pause()
        j "We are not doing anything illegal, right ? At least for now.."
        scene bg fr17c1_ps with dissolve
        j "We could say that you are my [mom], you are very like her by the way."
        v "..."
        scene bg fr18c1_ps with dissolve
        j "And we could say that you are helping me to choose clothes for my first date, for example."
        scene bg fr17c1ps with dissolve
        v "Don't be ridiculous Julie! They won't believe that I'm your [mom]. And, besides, what a [mom] would be completely naked in front of her own daughter ?!"
        scene bg fr17c1_ps with dissolve
        j "Yeah, you are probably right. They won't believe this.."
        scene bg fr17c1ps with dissolve
        j "Oh, I know, we will tell that you are my older [sis] !"
        v "Are you serious ?"
        j "Why not ? I will tell them that you are my sexy hot [sis] with a body of a goddess ! I would touch it all day long.."
        scene bg fr18c1_2ps with dissolve
        "{i}Julie touches Vicky's belly..."
        v "Julie.."
        j "By the way what is your secret ? Are you doing any sport ?"
        v "Yes, I'm doing Yoga."
        j "Cool ! Today I will ask [bro] to take me to the gym he is attending. I want to look just like you !"
        scene bg fr18c1ps with dissolve
        v "Julie, please do not take offense. I appreciate your attention but I'm just not into girls.. And I'm dating your [brother] anyway so..Even if I were.."
        scene bg fr18c1_1ps with dissolve
        j "Don't sweat it, I have a girlfriend too, she is just out of the city"
        v "Well, then I don't understand why you can't change the clothes in your room instead of making up this whole 'older [sis]' story and getting us into troubles.."
        j "Oh, I just want to try on the same panties as you are wearing. Where did you find them ?"
        scene bg fr19c12_ps with fade
        $ renpy.pause()
        v "What ? Ahm..I barely found them myself, looks like these are the last ones."
        scene bg fr19c12ps with dissolve
        j "What a pity..They seem really nice"
        v "Don't get sad, the store is getting new shipment tomorrow. We can come again and check if they have more of these.."
        j "How about these ones ?"
        scene bg fr19c12_ps with dissolve
        v "I beg you a pardon ?"
        j "I know you've found them first, but, can I at least try them on ?"
        scene bg fr20c12ps with dissolve
        v "Julie.."
        j "Please, Vicky, I will behave, I promise.."
        v "I don't know..I think this is a bad idea, I mean, they most likely will not fit you"
        j "Yeah, I guess you are right..I don't have that perfect, hourglass body type as you have anyway. My hips ain't curvy enough for these panties, they probably would just fell down on the floor.."
        $ renpy.pause()
        scene bg fr19c12_ps with dissolve
        v "You know, what if I'm totally wrong ? Try them on !"
        j "Really ?"
        v "Yeah, give it a try !"
        scene bg fr21_c4ps with fade
        $ renpy.pause()
        j "These panties are amazing.."
        v "It turned out I was wrong, they do look good at you. By the way, I have to admit that it is very curvy butt you have ! I could only dream of this when I was at your age."
        j "Thanks, Vicky ! It is my [mom]'s genes, she looked the same in her 18."
        j "Eh..It's too bad there is no more panties like these. But you've seen them first, so.."
        v "They are yours !"
        scene bg fr21c4_ps with dissolve
        j "What ?"
        v "I already have plenty of underwear anyway, so take them."
        scene bg fr21c4ps with dissolve
        v "Let it be my little gift for you."
        j "Oh my god, Vicky !"
        scene bg fr23c6ps with fade
        j "Thank You, Thank You, Thank You !!!"
        j "You are the best, Vicky ! I wish you really were my older [sis].."
        v "There, there Julie, it's just a panties. Are you always so happy of gifts ?"
        $ renpy.pause()
        scene bg fr22c5ps with fade
        j "Of course, I love gifts ! Who doesn't ?"
        v "Hm, why do I have a feeling that you just needed an excuse to lean on and rub my breasts ?"
        $ renpy.pause()
        j "I don't know what you are talking about..I just wanted to hug and warm you up, cause you said that it is cold out here."
        v "Ha-ha, you are cunning little one !"
        j "Aha.."
        scene bg fr24c4ps with fade
        $ renpy.pause()
        v "Are you hungry ? I know great cafe nearby.."
        j "Yes, I would eat something."
        v "Let's go then !"
        v "And don't forget your gift."
        j "Thank you.."
        scene black with Dissolve (2.0)
        jump ep3store
        return

    label ep3store:
        $ renpy.notify ("O esnada..")
        $ renpy.pause()
        scene bg store1c3ps with dissolve
        b "{i}It's time to buy some groceries. Now there are two of us and it looks like that Julie has a big appetite as for a little girl.
        It's probably hormones, puberty and all that stuff. Young growing body, what can I say.."
        b "{i}Let's see. First of all I need to buy the meat, eggs and milk. Maybe some pancakes with raspberry syrup will be a good option as dessert."
        b "{i}As I remember, Julie loves chocolate chips, so I can pamper her with it. What else..Oh, a chewing gum, of course."
        b "{i}Also I've run out of some household goods, such as bath tissue, paper towels and cleaning spray."
        b "{i}I guess that is all. Okay, I'll start with the most necessary goods."
        scene bg store3c2ps with fade
        b "{i}These are the refrigerators. Meat, milk and eggs should be somewhere here"
        menu:
            "Skip":
                b "{i}Peace of cake.."
                jump ep3cashbox
            "Gather":
                b "{i}I hope there's something left"
                jump ep3fridges
        return

    screen ep3fridgesScr:
        imagemap:
            ground "images/ep3/store3c2ps.png"
            hotspot (91,120,902,831) clicked Return("fridge1") hovered ShowTransient("imgHider", img="images/ep3/store3c2ps_1.png") unhovered Hide("imgHider")
            hotspot (1046,89,359,560) clicked Return("fridge2") hovered ShowTransient("imgHider", img="images/ep3/store3c2ps_2.png") unhovered Hide("imgHider")
            hotspot (1452,94,167,445) clicked Return("fridge3") hovered ShowTransient("imgHider", img="images/ep3/store3c2ps_3.png") unhovered Hide("imgHider")
            hotspot (1669,91,98,379) clicked Return("fridge4") hovered ShowTransient("imgHider", img="images/ep3/store3c2ps_4.png") unhovered Hide("imgHider")
            hotspot (1808,96,67,267) clicked Return("fridge5") hovered ShowTransient("imgHider", img="images/ep3/store3c2ps_5.png") unhovered Hide("imgHider")

    label ep3fridges:
        call screen ep3fridgesScr

        $ ep3MilkDone = 0
        $ ep3MeatDone = 0
        $ ep3EggsDone = 0

        $ result = _return
        if result == "fridge1":
            jump ep3fridge1
        if result == "fridge2":
            jump ep3fridge2
        if result == "fridge3":
            jump ep3fridge3
        if result == "fridge4":
            jump ep3fridge4
        if result == "fridge5":
            jump ep3fridge5
        return

    screen ep3fridge1Scr:
        imagemap:
            ground "images/ep3/store7c8f1ps.png"
            hotspot (483,21,1022,622) clicked Return("fridge") hovered ShowTransient("imgHider", img="images/ep3/store7c8f1_ps.png") unhovered Hide("imgHider")
            hotspot (1770,774,152,306) clicked Return("moveRight") hovered ShowTransient("imgHider", img="images/ep3/store7c8f1rightps.png") unhovered Hide("imgHider")
            hotspot (856,118,43,126) clicked Return("milk") hovered ShowTransient("imgHider", img="images/ep3/store7c8f1_psH.png") unhovered Hide("imgHider")

    screen ep3fridge1MilkDoneScr:
        imagemap:
            ground "images/ep3/store7c8f1psMilk.png"
            hotspot (483,21,1022,622) clicked Return("fridge") hovered ShowTransient("imgHider", img="images/ep3/store7c8f1_psMilk.png") unhovered Hide("imgHider")
            hotspot (1770,774,152,306) clicked Return("moveRight") hovered ShowTransient("imgHider", img="images/ep3/store7c8f1rightpsMilk.png") unhovered Hide("imgHider")

    label ep3fridge1:
        if ep3MilkDone == 1:
            scene bg store7c8f1psMilk
            call screen ep3fridge1MilkDoneScr
            $ result = _return
            if result == "fridge":
                scene bg store7c8f1_psMilk
                b "{i}I already have it"
                jump ep3fridge1
            if result == "moveRight":
                jump ep3fridge2
        else:
            scene bg store7c8f1ps
            call screen ep3fridge1Scr
            $ result = _return
            if result == "milk":
                scene bg store7c8f1_psMilk
                b "{i}Got it"
                $ ep3MilkDone = 1
                if ep3EggsDone + ep3MeatDone + ep3MilkDone == 3:
                    jump ep3storePhase2
                jump ep3fridge1
            if result == "moveRight":
                jump ep3fridge2
            if result == "fridge":
                scene bg store7c8f1_ps
                b "{i}I need to get some milk first"
                jump ep3fridge1
        return

    screen ep3fridge2Scr:
        imagemap:
            ground "images/ep3/store6c7f2ps.png"
            hotspot (414,13,1121,630) clicked Return("fridge") hovered ShowTransient("imgHider", img="images/ep3/store6c7f2_ps.png") unhovered Hide("imgHider")
            hotspot (1650,778,274,297) clicked Return("moveRight") hovered ShowTransient("imgHider", img="images/ep3/store6c7f2rightps.png") unhovered Hide("imgHider")
            hotspot (4,777,224,292) clicked Return("moveLeft") hovered ShowTransient("imgHider", img="images/ep3/store6c7f2leftps.png") unhovered Hide("imgHider")

    label ep3fridge2:
        scene bg store6c7f2ps
        call screen ep3fridge2Scr
        $ result = _return
        if result == "fridge":
            scene bg store6c7f2_ps
            b "{i}This one is empty"
            jump ep3fridge2
        if result == "moveRight":
            jump ep3fridge3
        if result == "moveLeft":
            jump ep3fridge1
        return

    screen ep3fridge3Scr:
        imagemap:
            ground "images/ep3/store5c9f3ps.png"
            hotspot (414,13,1121,630) clicked Return("fridge") hovered ShowTransient("imgHider", img="images/ep3/store5c9f3_ps.png") unhovered Hide("imgHider")
            hotspot (1650,778,274,297) clicked Return("moveRight") hovered ShowTransient("imgHider", img="images/ep3/store5c9f3rightps.png") unhovered Hide("imgHider")
            hotspot (4,777,224,292) clicked Return("moveLeft") hovered ShowTransient("imgHider", img="images/ep3/store5c9f3leftps.png") unhovered Hide("imgHider")

    label ep3fridge3:
        scene bg store5c9f3ps
        call screen ep3fridge3Scr
        $ result = _return
        if result == "fridge":
            scene bg store5c9f3_ps
            b "{i}This one is empty"
            jump ep3fridge3
        if result == "moveRight":
            jump ep3fridge4
        if result == "moveLeft":
            jump ep3fridge2
        return

    screen ep3fridge4Scr:
        imagemap:
            ground "images/ep3/store8c10f4ps.png"
            hotspot (414,13,1121,630) clicked Return("fridge") hovered ShowTransient("imgHider", img="images/ep3/store8c10f4_ps.png") unhovered Hide("imgHider")
            hotspot (1620,776,307,304) clicked Return("moveRight") hovered ShowTransient("imgHider", img="images/ep3/store8c10f4rightps.png") unhovered Hide("imgHider")
            hotspot (4,777,342,291) clicked Return("moveLeft") hovered ShowTransient("imgHider", img="images/ep3/store8c10f4leftps.png") unhovered Hide("imgHider")
            hotspot (1070,152,79,87) clicked Return("meat") hovered ShowTransient("imgHider", img="images/ep3/store8c10f4_psH.png") unhovered Hide("imgHider")

    screen ep3fridge4MeatDoneScr:
        imagemap:
            ground "images/ep3/store8c10f4psMeat.png"
            hotspot (414,13,1121,630) clicked Return("fridge") hovered ShowTransient("imgHider", img="images/ep3/store8c10f4_psMeat.png") unhovered Hide("imgHider")
            hotspot (1620,776,307,304) clicked Return("moveRight") hovered ShowTransient("imgHider", img="images/ep3/store8c10f4rightpsMeat.png") unhovered Hide("imgHider")
            hotspot (4,777,342,292) clicked Return("moveLeft") hovered ShowTransient("imgHider", img="images/ep3/store8c10f4leftpsMeat.png") unhovered Hide("imgHider")

    label ep3fridge4:
        if ep3MeatDone == 1:
            scene bg store8c10f4psMeat
            call screen ep3fridge4MeatDoneScr
            $ result = _return
            if result == "fridge":
                scene bg store8c10f4_psMeat
                b "{i}I already have it"
                jump ep3fridge4
            if result == "moveRight":
                jump ep3fridge5
            if result == "moveLeft":
                jump ep3fridge3
        else:
            scene bg store8c10f4ps
            call screen ep3fridge4Scr
            $ result = _return
            if result == "meat":
                scene bg store8c10f4_psMeat
                b "{i}Got it"
                $ ep3MeatDone = 1
                if ep3EggsDone + ep3MeatDone + ep3MilkDone == 3:
                    jump ep3storePhase2
                jump ep3fridge4
            if result == "moveRight":
                jump ep3fridge5
            if result == "fridge":
                scene bg store8c10f4_ps
                b "{i}I need to get some meat first"
                jump ep3fridge4
            if result == "moveLeft":
                jump ep3fridge3
        return

    screen ep3fridge5Scr:
        imagemap:
            ground "images/ep3/store9c11f5ps.png"
            hotspot (414,13,1121,630) clicked Return("fridge") hovered ShowTransient("imgHider", img="images/ep3/store9c11f5_ps.png") unhovered Hide("imgHider")
            hotspot (4,777,393,298) clicked Return("moveLeft") hovered ShowTransient("imgHider", img="images/ep3/store9c11f5leftps.png") unhovered Hide("imgHider")
            hotspot (1106,312,83,61) clicked Return("eggs") hovered ShowTransient("imgHider", img="images/ep3/store9c11f5_psH.png") unhovered Hide("imgHider")

    screen ep3fridge5EggsDoneScr:
        imagemap:
            ground "images/ep3/store9c11f5psEggs.png"
            hotspot (414,13,1121,630) clicked Return("fridge") hovered ShowTransient("imgHider", img="images/ep3/store9c11f5_psEggs.png") unhovered Hide("imgHider")
            hotspot (4,777,393,298) clicked Return("moveLeft") hovered ShowTransient("imgHider", img="images/ep3/store9c11f5leftpsEggs.png") unhovered Hide("imgHider")

    label ep3fridge5:
        if ep3EggsDone == 1:
            scene bg store9c11f5psEggs
            call screen ep3fridge5EggsDoneScr
            $ result = _return
            if result == "fridge":
                scene bg store9c11f5_psEggs
                b "{i}I already have it"
                jump ep3fridge5
            if result == "moveLeft":
                jump ep3fridge4
        else:
            scene bg store9c11f5ps
            call screen ep3fridge5Scr
            $ result = _return
            if result == "eggs":
                scene bg store9c11f5_psEggs
                b "{i}Got it"
                $ ep3EggsDone = 1
                if ep3EggsDone + ep3MeatDone + ep3MilkDone == 3:
                    jump ep3storePhase2
                jump ep3fridge5
            if result == "fridge":
                scene bg store9c11f5_ps
                b "{i}I need to get some eggs first"
                jump ep3fridge5
            if result == "moveLeft":
                jump ep3fridge4
        return

    label ep3storePhase2:

        $ ep3SprayDone = 0
        $ ep3PancakesDone = 0
        $ ep3ChipsDone = 0
        $ ep3GumDone = 0
        $ ep3SyrupDone = 0
        $ ep3TissueDone = 0
        $ ep3TowelsDone = 0

        b "{i}Half of the way is passed. Let's see what else I need to buy.."
        scene bg store5c6ps with fade
        b "{i}Okay so, cleaning spray, pancakes, chocolate chips, chewing gum, raspberry syrup, bath tissue and paper towels are left"
        b "{i}It should be easy"
        menu:
            "Skip":
                b "{i}Easy"
                jump ep3cashbox
            "Gather":
                b "{i}The goods must be somewhere nearby"
                jump ep3storeLeftStand
        return

    screen ep3storeLeftStandScr:
        imagemap:
            ground "images/ep3/store5c6ps.png"
            hotspot (268,318,52,93) clicked Return("syrup") hovered ShowTransient("imgHider", img="images/ep3/store5c6psSyrup.png") unhovered Hide("imgHider")
            hotspot (361,577,97,144) clicked Return("towels") hovered ShowTransient("imgHider", img="images/ep3/store5c6psTowels.png") unhovered Hide("imgHider")
            hotspot (1194,604,92,104) clicked Return("tissue") hovered ShowTransient("imgHider", img="images/ep3/store5c6psPaper.png") unhovered Hide("imgHider")
            hotspot (672,492,292,118) clicked Return("mid") hovered ShowTransient("imgHider", img="images/ep3/store5c6psMid.png") unhovered Hide("imgHider")
            hotspot (741,299,219,52) clicked Return("right") hovered ShowTransient("imgHider", img="images/ep3/store5c6psRight.png") unhovered Hide("imgHider")

    label ep3storeLeftStand:
        scene bg store5c6ps
        call screen ep3storeLeftStandScr
        $ result = _return
        if result == "syrup":
            if ep3SyrupDone == 0:
                b "{i}Got it"
                $ ep3SyrupDone = 1
                if ep3SyrupDone + ep3SprayDone + ep3PancakesDone + ep3ChipsDone + ep3GumDone + ep3TissueDone + ep3TowelsDone == 7:
                    b "{i}Okay, this is the last one. I should go to the cashier now."
                    jump ep3cashbox
                jump ep3storeLeftStand
            else:
                b "{i}I don't need more of this"
                jump ep3storeLeftStand
        if result == "towels":
            if ep3TowelsDone == 0:
                b "{i}Got it"
                $ ep3TowelsDone = 1
                if ep3SyrupDone + ep3SprayDone + ep3PancakesDone + ep3ChipsDone + ep3GumDone + ep3TissueDone + ep3TowelsDone == 7:
                    b "{i}Okay, this is the last one. I should go to the cashier now."
                    jump ep3cashbox
                jump ep3storeLeftStand
            else:
                b "{i}I don't need more of this"
                jump ep3storeLeftStand
        if result == "tissue":
            if ep3TissueDone == 0:
                b "{i}Got it"
                $ ep3TissueDone = 1
                if ep3SyrupDone + ep3SprayDone + ep3PancakesDone + ep3ChipsDone + ep3GumDone + ep3TissueDone + ep3TowelsDone == 7:
                    b "{i}Okay, this is the last one. I should go to the cashier now."
                    jump ep3cashbox
                jump ep3storeLeftStand
            else:
                b "{i}I don't need more of this"
                jump ep3storeLeftStand
        if result =="mid":
            scene bg store3c4ps with fade
            jump ep3storeMidStand
        if result == "right":
            scene bg store4c5ps with fade
            jump ep3storeRightStand
        return

    screen ep3storeMidStandScr:
        imagemap:
            ground "images/ep3/store3c4ps.png"
            hotspot (736,500,50,72) clicked Return("gum") hovered ShowTransient("imgHider", img="images/ep3/store3c4psGum.png") unhovered Hide("imgHider")
            hotspot (4,828,265,236) clicked Return("left") hovered ShowTransient("imgHider", img="images/ep3/store3c4psLeft.png") unhovered Hide("imgHider")
            hotspot (1669,825,247,244) clicked Return("right") hovered ShowTransient("imgHider", img="images/ep3/store3c4psRight.png") unhovered Hide("imgHider")

    label ep3storeMidStand:
        call screen ep3storeMidStandScr
        $ result = _return
        if result == "gum":
            if ep3GumDone == 0:
                b "{i}Got it"
                $ ep3GumDone = 1
                if ep3SyrupDone + ep3SprayDone + ep3PancakesDone + ep3ChipsDone + ep3GumDone + ep3TissueDone + ep3TowelsDone == 7:
                    b "{i}Okay, this is the last one. I should go to the cashier now."
                    jump ep3cashbox
                jump ep3storeMidStand
            else:
                b "{i}I don't need more of this"
                jump ep3storeMidStand
        if result == "right":
            scene bg store4c5ps with fade
            jump ep3storeRightStand
        if result == "left":
            scene bg store5c6ps with fade
            jump ep3storeLeftStand
        return

    screen ep3storeRightStandScr:
        imagemap:
            ground "images/ep3/store4c5ps.png"
            hotspot (506,148,39,78) clicked Return("chips") hovered ShowTransient("imgHider", img="images/ep3/store4c5psChips.png") unhovered Hide("imgHider")
            hotspot (1700,147,92,109) clicked Return("pancake") hovered ShowTransient("imgHider", img="images/ep3/store4c5psPancake.png") unhovered Hide("imgHider")
            hotspot (1418,569,61,149) clicked Return("spray") hovered ShowTransient("imgHider", img="images/ep3/store4c5psSpray.png") unhovered Hide("imgHider")
            hotspot (951,496,312,125) clicked Return("mid") hovered ShowTransient("imgHider", img="images/ep3/store4c5psMid.png") unhovered Hide("imgHider")
            hotspot (959,285,227,48) clicked Return("left") hovered ShowTransient("imgHider", img="images/ep3/store4c5psLeft.png") unhovered Hide("imgHider")

    label ep3storeRightStand:
        call screen ep3storeRightStandScr
        $ result = _return
        if result == "chips":
            if ep3ChipsDone == 0:
                b "{i}Got it"
                $ ep3ChipsDone = 1
                if ep3SyrupDone + ep3SprayDone + ep3PancakesDone + ep3ChipsDone + ep3GumDone + ep3TissueDone + ep3TowelsDone == 7:
                    b "{i}Okay, this is the last one. I should go to the cashier now."
                    jump ep3cashbox
                jump ep3storeRightStand
            else:
                b "{i}I don't need more of this"
                jump ep3storeRightStand
        if result == "pancake":
            if ep3PancakesDone == 0:
                b "{i}Got it"
                $ ep3PancakesDone = 1
                if ep3SyrupDone + ep3SprayDone + ep3PancakesDone + ep3ChipsDone + ep3GumDone + ep3TissueDone + ep3TowelsDone == 7:
                    b "{i}Okay, this is the last one. I should go to the cashier now."
                    jump ep3cashbox
                jump ep3storeRightStand
            else:
                b "{i}I don't need more of this"
                jump ep3storeRightStand
        if result == "spray":
            if ep3SprayDone == 0:
                b "{i}Got it"
                $ ep3SprayDone = 1
                if ep3SyrupDone + ep3SprayDone + ep3PancakesDone + ep3ChipsDone + ep3GumDone + ep3TissueDone + ep3TowelsDone == 7:
                    b "{i}Okay, this is the last one. I should go to the cashier now."
                    jump ep3cashbox
                jump ep3storeRightStand
            else:
                b "{i}I don't need more of this"
                jump ep3storeRightStand
        if result == "mid":
            scene bg store3c4ps with fade
            jump ep3storeMidStand
        if result == "left":
            scene bg store5c6ps with fade
            jump ep3storeLeftStand
        return

    label ep3cashbox:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra mağazada..")
        $ renpy.pause()
        scene bg store2c4ps with dissolve
        b "{i}Wow, it's Nicole. It's been a while since we met at the store. I should come and say 'hello' to her, maybe she needs my help with the bag."
        define cashier = Character("Cashier", color="#000000")
        cashier "Is this all your purchase ?"
        n "Yes, that is all"
        cashier "Okay. Would you like to donate 1%% of your purchase to charity ?"
        scene bg store10c3ps with fade
        n "Yes, as usual. There are always some people who are less fortunate than us, right ?"
        $ renpy.pause()
        cashier "Okay. Just a minute please."
        n "Sure"
        cashier "By the way, sorry for inconvenience, some of our goods are out of stock. We have delivery delay from the supplier."
        n "Oh, it's okay. I've found everything I need."
        cashier "I'm glad to hear it."
        extend " Oops, looks like the connection with recipient bank is lost, I'll try again. Sorry.."
        n "No problem, take your time."
        $ renpy.pause()
        nacho "Hey, cashier lady, really quick. Give me two packs of 'Lucky Punch' cigarettes and hurry up!"
        scene bg store11c3ps with dissolve
        n "..."
        n "Excuse me, Sir..There is a queue here"
        scene bg store12c1ps with fade
        nacho "What is the matter, hottie ?! No need to be so nervous."
        nacho "Are you in a hurry or you got your periods ?"
        $ renpy.pause()
        scene bg store11c3ps with fade
        n "..."
        nacho "Well, well, well what do we have here..Looks like I was right."
        scene store13c2ps with fade
        n "Put it back please.."
        nacho "Can't help your leaking, huh ?"
        scene bg store13c2_ps with dissolve
        nacho "Well you are lucky, baby. Cause I've got something that will definitely help you with this problem, at least for the next 9 months."
        scene bg store13c2_2ps with dissolve
        nacho "But you have to ask me really gently."
        scene bg store14c2ps with dissolve
        scene bg store13c2_1ps with Dissolve (0.25)
        scene bg store12c2ps with Dissolve (0.25)
        $ renpy.pause()
        scene bg store15c3_ps with fade
        n "{i}Sob.."
        scene bg store15c3ps with Dissolve (0.75)
        $ renpy.pause()
        cashier "Sir, I have to ask you leave.."
        nacho "Mind your own business!"
        n "..."
        nacho "Oh, don't get sad, baby. Come with me and I'll make you happy again."
        scene bg store15c5ps with fade
        $ renpy.pause()
        nacho "Let's go beautiful, you will like it, I promise. I know you want it and I know how strong your desire, chicks always want to get fucked during their periods, you're just afraid to admit this.."
        scene bg store16c5ps with dissolve
        n "Please don't touch me..Take your cigarettes and go away..\n{i}Sob-sob.."
        extend ""
        $ renpy.music.play("music/enemyThemeShort.mp3", channel=1, loop=True, fadein=7)
        b "I'll say {b}just go away{/b}. You know, they say:\n'Smoking is injurious to health'."
        scene bg store17c2_ps with fade
        n "[bro]..?"
        $ renpy.pause()
        nacho "Who the hell are you, punk ?!"
        extend "\nDo you know what is really injurious to health ? It's be fucking nosy piece of shit!"
        scene bg store17c2ps with dissolve
        nacho "So stay the fuck out of this or I guarantee you big problems ! Do you understand ?"
        scene bg store17c2_ps with dissolve
        $ renpy.pause()
        b "{i}This big guy looks like a serious opponent to fight. And I'm far from my best physical shape right now. Plus this strange headache doesn't go away since morning. \nDamn.."
        b "{i}One my mistake will be critical.."
        b "{i}For the other hand I could use the surprise effect in my favour and strike him first.."
        b "{i}But again, if something goes wrong I will endanger not only myself but Nicole as well.."
        b "{i}What should I do ?"
        $ ep3NachoBeaten = 0
        menu:
            "Call the police":
                $ renpy.music.stop(channel=1, fadeout=10.0)
                b "Let's see what police will say about this."
                cashier "If you don't leave Sir, I will call them right away !"
                scene bg store18c2ps with dissolve
                n "Yeah, that is right ! Let them teach him good manners."
                scene bg store18c2_ps with dissolve
                nacho "Fuck this shit ! Fuck you all ! I'm leaving this shitty store !"
                scene bg store19c2ps with dissolve
                nacho "Hey, I remembered your face, punk ! If I were you, I would hope we don't meet again."
                b "I hope we do.."
                scene bg store17c2_ps with dissolve
                n "..."
                jump ep3Hallway
            "Other way...":
                jump ep3StoreFight
        $ renpy.pause()
        return

    screen ep3StoreFightLChinScr:
        imagemap:
            ground "images/ep3/store17c2_ps.png"
            hotspot (932,173,64,54) clicked Return("chin") hovered ShowTransient("imgHider", img="images/ep3/store17c2_1ps.png") unhovered Hide("imgHider")

    screen ep3StoreFightRChinScr:
        imagemap:
            ground "images/ep3/store17c2_ps.png"
            hotspot (995,173,77,49) clicked Return("chin") hovered ShowTransient("imgHider", img="images/ep3/store17c2_2ps.png") unhovered Hide("imgHider")

    screen ep3StoreFightForeheadScr:
        imagemap:
            ground "images/ep3/store17c2_ps.png"
            hotspot (957,11,122,68) clicked Return("forehead") hovered ShowTransient("imgHider", img="images/ep3/store17c2_3ps.png") unhovered Hide("imgHider")

    label ep3StoreFight:
        $ ep3NachoBeaten = 1
        b "{i}To knockout him I must go {b}only{/b} for the head. Series of three fast strikes should be enough."
        call screen ep3StoreFightLChinScr
        call screen ep3StoreFightRChinScr
        call screen ep3StoreFightForeheadScr
        b "You now, actually solving the problems is my job"
        scene bg store19c2_ps with dissolve
        play sound "music/sounds/femaleGasps.mp3"
        n "Oh.."
        play sound "music/sounds/punchFace2.mp3"
        scene bg store20c7ps with Fade(0.1, 0.1, 0.35, color="#fff")
        play sound "music/sounds/punchFace.mp3"
        scene bg store21c8ps with Fade(0.1, 0.1, 0.35, color="#fff")
        play sound "music/sounds/kneeKick.mp3"
        scene store22c9ps with Fade(0.1, 0.1, 0.35, color="#fff")
        play sound "music/sounds/bodyFall.mp3"
        scene bg store23c10ps with Fade(0.1, 1.5, 1.5, color="#fff")
        $ renpy.music.stop(channel=1, fadeout=10.0)
        b "..."
        b "Smoking is indeed injurious to health.."
        nacho "{b}{i}*Knocked Out*{/i}{/b}"
        jump ep3Hallway
        return

    label ep3Hallway:
        $ renpy.music.stop(channel=1, fadeout=0.0)
        scene black with Dissolve (2.0)
        $ renpy.notify ("Bir süre sonra...")
        $ renpy.pause()
        scene bg hallway7c4ps with dissolve
        n "I see, so Julie is your younger [sis]. I thought that this cute little girl is your girlfriend or something."
        b "No"
        $ renpy.pause()
        n "Ehm.. Thanks again [bro], for everything."
        scene bg hallway8c5ps with fade
        b "Don't mention it, It's least I can do for you"
        $ renpy.pause()
        n "..."
        n "[bro], I feel terribly awkward by asking you, but.."
        n "Do you recall me telling you about the problem with my computer ?"
        menu:
            "Yes":
                b "Yes, I do. I haven't forgot about your request."
                b "Yesterday just was a really busy day, I didn't have a chance to stop by."
                b "Unfortunately now I don't have it either. I need to cook a dinner, Julie will come back soon and she most likely will be hungry"
            "No":
                b "Not really. Why ?"
                scene bg hallway9c5_ps with dissolve
                n "Hm, looks like I only wanted to tell you about it, but never actually told.."
                n "Anyway, my PC doesn't start for some reason, and I need it for my work."
                scene bg hallway8c5ps with dissolve
                n "So I was wondering if you could do your 'magic' like the last time ? I would take it to the repair service but unfortunately right now I'm a bit short of money.."
                b "Sure, I'll gladly help"
                b "But now I don't have enough time, I need to cook a dinner. Julie will come back soon and she most likely will be hungry."
        scene bg hallway10c5ps with dissolve
        n "You're such a caring big [brother], that is so sweet..."
        b "Yeah thanks but, back to your request - hopefully I will be free at the evening, so I can stop by and see what is wrong with your PC. Is that okay ?"
        n "Sounds good to me. Just give me a call beforehand, okay ?"
        b "Okay, so see you later, Nicole ?"
        n "Yes. I'll be waiting for you, [bro]..."
        $ renpy.pause()
        jump ep3cafe
        return

    label ep3cafe:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Bu arada kafede...")
        $ renpy.pause()
        scene bg cafe1c3ps with dissolve
        v "Sorry to hear that, I didn't know that your [father] left the [family] the day you were born.."
        v "It must be difficult to realize that such a thing happened on your birthday. I hope you don't take it personally. I mean, it doesn't look like a coincidence, but it is definitely not your fault."
        scene bg cafe1c2ps with fade
        j "I'm okay Vicky, it's been 18 years already. I'm trying not to think about it "
        v "Did your [family] try to find him ?"
        j "We reported to the police about his missing, but they didn't find any clue about where he might be or is he still alive.."
        j "I never saw him personally, [mom] only showed me his photos. [bro] resembles him a lot by the way, [mom] always says that they are like twins, only with a 25 years difference.."
        scene bg cafe6c4ps with fade
        v "I see. Well, if he really just left the [family], that is good that [bro] inherited only your [father]'s appearance, not his nature.."
        j "Yeah, I guess.."
        scene bg cafe3c1ps with fade
        $ renpy.pause()
        j "Shortly after [father] was completely gone, we faced with the money issue, [mom] had to find a second job, because teacher's salary was not enough for the three of us. She always told us that it's gonna be alright, we just need to believe, care about each other and do everything that depends on us."
        scene bg cafe3c1_ps with dissolve
        j "She tried to earn as much money as possible and we barely had enough, however [mom] physically could not do everything else. We saw each other only at the early morning and sometimes at late night before the sleep. So, basically [bro] was babysitting me, doing most of the chores and cooking food."
        scene bg cafe3c1ps with dissolve
        j "As a result his grades at school started getting lower and in addition to lack of money the college option for [bro] was impossible."
        j "By the time [bro] graduated from school I was old enough to stay at home by myself, so he started working as well"
        scene bg cafe6c4_ps with fade
        v "..."
        scene bg cafe6c4ps with dissolve
        v "What happened next ?"
        j "Later on [bro] somehow found a job in this city. They've paid for his relocation and it's been more than 5 years since he is here. As time went by we began to talk less and less. Our communication was lowered to the one email per month, sometimes even one and a half.. But [bro] never stopped sending us money."
        scene bg cafe3c1ps with fade
        j "Eventually [mom] left the second job and started to spend more time with me because I was going to leave for the college. With [bro]'s help we saved up enough money to pay for my study, so.."
        scene bg cafe3c1_ps with dissolve
        j "Here I am."
        $ renpy.pause()
        v "I'm sorry Julie, I didn't know that your childhood was so hard. But I'm sure that [bro] did his best to replace you [father] and at the same time remain a good [brother]."
        j "It's okay, [bro] really was kind of a [father] figure to me, we got along very well. But I got so mad at him when he left us, just like our [father] !"
        v "Now you understand, that [bro] did it for your good, it was probably the best option at that moment."
        scene bg cafe3c1ps with dissolve
        j "I guess you are right, but I still don't understand why he behaved so weird.."
        scene bg cafe2c4ps with fade
        v "I think he had his reasons, but this is not the point. The main thing is that now you are together again, and you know that he cares about you."
        $ renpy.pause()
        scene bg cafe4c1ps with fade
        j "You are right, Vicky !"
        j "It is so easy to talk to you, I feel like I know you my entire life. I can't believe that we've just met. Your charisma and confidence are so impressive !"
        j "Not to mention how amazing you look !"
        j "What kind of 'sorcery' is this ?"
        scene bg cafe2c4ps with fade
        v "Thanks Julie, I can say the same things about you and I'm glad that we've met !"
        j "So would you share with me your secret ?"
        $ renpy.pause()
        scene bg cafe6c4ps with dissolve
        v "..."
        scene bg cafe5c4_ps with dissolve
        v "I have a lot of stories to tell about myself, Julie. But now isn't right time for them. I also had to face with many difficulties in the past, but that taught me a lot of important lessons that I will never forget..."
        scene bg cafe5c4ps with dissolve
        v "The most important lesson I've learned is one about human nature."
        v "..."
        v "Everyone is driven by sex, money or power at the certain point of time. Sometimes it is all three of them together..."
        v "So to say, every human is a puzzle of these needs. Therefore the sooner you solve it, the sooner you will have the whole picture about who is in front of you."
        scene bg cafe5c4_ps with dissolve
        v "But some puzzles can't be solved that simple, you will have to give back something in return. It can be something unimportant, but it also can be the most valuable thing you have, and I'm not talking about money right now."
        scene bg cafe5c4ps with dissolve
        v "There are only two questions you have to ask yourself and understand what {b}you{/b} really want and how far you are willing to go to get what you want..."
        scene bg cafe6c4ps with dissolve
        v "..."
        v "You are smart and insistent girl, Julie. Looks like you know what you want and you always go for it no matter what. But the world is a very mean and nasty place, so one day something may turn out for you really bad."
        v "That is why you always have to be carefull with your ambitions and intentions..."
        j "Wow..."
        v "..."
        scene bg cafe7c4ps with dissolve
        v "Oops, looks like I am being really serious about it.."
        v "Anyway, fortunately for us, girls, there are only two of three needs we ought to determine about a man. Third one is already known."
        j "What do you mean by that ?"
        scene bg cafe7c4_ps  with dissolve
        v "Come on Julie, don't you know ? It is sex ! Men always want to have sex. It is their nature, where do you think all these 'sugar daddies' came from ? Or maybe you ever happened to hear something about 'sugar mommies' ?"
        scene bg cafe7c1ps with fade
        j "Hm, I guess... Just never thought about it."
        v "Okay, that is enough for today, looks like I blew up your mind with all this information. Let's go, I'll take you home before [bro] started worrying about you."
        scene bg cafe4c1ps with dissolve
        j "Yes, it is already afternoon and I still want to ask [bro] take me to the gym that he's attending. Hopefully, there is a place for doing yoga."
        v "That is right, Julie. Otherwise this pizza slice will turn from a moment on the lips to a lifetime on the hips, ha-ha"
        j "Yeah and my cute little butt will turn into cute fat little butt, ha-ha"
        jump ep3gym
        return

    label ep3gym:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra spor salonunda...")
        $ renpy.pause()
        scene bg fClub5c2ps with dissolve
        b "We are at the place. This is a locker room, you can change your clothes and leave your bag in any locker, I think none of them are locked."
        $ renpy.pause()
        j "Is this a women's locker room ?"
        menu:
            "Yes":
                scene fclub4c3ps with fade
                j "So you think it's okay for you come in here like this ?"
                $ renpy.pause()
            "No":
                scene fclub4c3ps with fade
                j "So you've brought me to the man's one or what ?"
                $ renpy.pause()
        b "Ahm..."
        b "It doesn't really matter actually. No one has been here for a long time. This is the gym of our...'company', long time ago there were a lot of people here, but now it seems like no one from my 'colleagues' shows much interest in healthy lifestyle."
        j "I see."
        j "So there will be only two of us here ?"
        b "Most likely, yes."
        j "..."
        j "Okay."
        b "..."
        b "Ahm, while you're changing I'll turn on the lights at the hall and make sure that everything is okay over there."
        j "No peeking !"
        b "..."
        scene black with Dissolve (2.0)
        $ renpy.notify ("Bir süre sonra..")
        $ renpy.pause()
        scene bg fClub6c1ps with dissolve
        b "{i}Looks like everything is okay. I haven't been paying attention that there are fitballs, yoga mats and other fitness stuff."
        b "{i}Why criminals like us would ever need anything apart of barbells and dumbbells ? Looks like the boss does have sense of humor..."
        b "{i}..."
        b "{i}Damn, maybe this wasn't a good idea to bring Julie over here. Too risky, what if someone of my 'colleagues' shows up ? It will be fucking bad..."
        scene bg fClub6c1ps with vpunch
        b "{i}Shit, this is a serious mistake I've made. I will have to tell Julie that this is the last time we are at this gym..."
        j "Wow, this gym is quite a big. I'm nearly lost..."
        b "I'm right here Ju..."
        scene bg fClub7c2ps with Dissolve (1.0)
        $ renpy.pause()
        b "..."
        j "..."
        j "What is the matter, [bro] ? Has the cat got your tongue ?"
        b "{i}Holy shit..."
        scene bg fClub8c4ps with fade
        j "Is something wrong ?"
        b "Julie...What happened to your clothes ?"
        j "I've changed it..."
        scene bg fClub8c3ps with fade
        b "I can see that but...Isn't this one just...a bit..."
        scene bg fClub9c3ps with dissolve
        j "What ? You don't like it...?"
        $ ep3ClothingLiked = 0
        menu:
            "I do like it":
                $ ep3ClothingLiked = 1
                b "Yes I like it, I just think that it's a little bit revealing for the gym, don't you think ?"
                scene bg fClub10c5ps with fade
                j "Yeah, you are right. The top is definitely too small."
                j "It seems like I grew up in 'some places' quite a bit, haha"
                $ renpy.pause ()
                b "The shorts look good but still too small for your...For you."
                scene bg fClub11c5ps with dissolve
                j "Yeah, they are so narrow. I thought that I couldn't put them on, it was so hard."
                b "Well, it's good that no one else is here. I would rather nobody saw you in this outfit."
                j "Jealous ?"
                $ renpy.pause ()
                b "'Worry' is a more suitable word in this situation."
                j "Well, you could buy me new clothes if you're so worried about it."
                b "Sure, I'll add it to my 'To-do list' right away."
            "I don't like it":
                b "No, this is absolutely unacceptable ! I'm sorry to say that but you look like a little {b}{i}slut{/i}{/b} in this outfit. Don't you have something more appropriate to wear ?"
                scene bg fClub10c5ps with fade
                j "Well, I agree it may be a little bit revealing and small. It's been a long time since I put it on. It probably got shortened after the laundry..."
                b "Jeez, do you have something else to put on ?"
                $ renpy.pause ()
                scene bg fClub11c5ps with dissolve
                j "No..."
                b "But you've been to the store with Vicky, why did not you buy a suitable sport outfit for yourself ?"
                j "Well, firstly, I didn't know that this clothes is too small for me, and secondly the store is selling kind of other type of outfit..."
                j "But hey, I bought myself a panties and fishnets ! Thanks to you by the way !"
                $ renpy.pause ()
                b "{i}Vicky...Of course, what was I hoping for ?!"
                j "Come on [bro], I think you are overreacting, there is no one except us anyway. I'll buy myself new clothes for gym, I promise"
                b "Fine..."
        scene bg fClub12c5ps with dissolve
        j "Okay, the workout won't make it itself, right ?"
        b "That is why you are here, Julie..."
        scene black with Dissolve (1.5)
        scene bg fClub13c6ps with Dissolve (1.5)
        j "One.."
        scene bg fClub15c6ps with dissolve
        j "Two.."
        scene bg fClub13c6ps with dissolve
        j "Three.."
        scene bg fClub15c6ps with dissolve
        j "Four.."
        j "Pooh! It's harder than I thought it would..."
        j "Ah.."
        scene bg fClub13c6ps with Dissolve (1.0)
        scene bg fClub15c6ps with Dissolve (1.0)
        scene bg fClub13c6ps with Dissolve (1.0)
        scene bg fClub15c6ps with Dissolve (1.0)
        b "{i}Damn, I have to admit that she is so sexy right now."
        scene bg fClub13c6ps with dissolve
        j "One.."
        scene bg fClub15c6ps with dissolve
        j "Two.."
        b "{i}Wait what am I thinking ?! Are you even hearing yourself, [bro] ?! It may be sexy {b}outfit{/b} but she is my {b}[sis]{/b} so throw this shit out of your head right now !"
        scene bg fClub13c6ps with dissolve
        j "Three.."
        scene bg fClub15c6ps with dissolve
        j "Four.."
        scene bg fClub13c6ps with dissolve
        j "One.."
        scene bg fClub15c6ps with dissolve
        j "Two.."
        j "..."
        scene bg fClub13c6ps with dissolve
        j "Hey [bro], what about you ? You don't seem you are going to workout today..."
        scene bg fClub15c6ps with dissolve
        b "No, I'm not. Today is my resting day"
        scene bg fClub13c6ps with dissolve
        j "Oh, I see..."
        scene bg fClub15c6_ps with dissolve
        b "By the way Julie, who told you that doing workout without warming-up is a good idea ?"
        scene bg fClub13c6_ps with dissolve
        j "Without a what ?"
        scene bg fClub15c6_ps with dissolve
        b "Stretching, warm-up whatever. It is a really important part of a workout, you have to prepare your body before the exercising. Otherwise you could hurt yourself or get trauma."
        scene bg fClub14c6_ps with dissolve
        j "Haha, don't be ridiculous, [bro]. I'm not like 100 years old grandma."
        scene bg fClub14c6_2ps with dissolve
        j "It's for grandpa like you the warm-up is probably the only way to avoid hospitalization during the workout, haha."
        scene bg fClub14c6_1ps with dissolve
        j "My body is young and firm."
        scene bg fClub14c6_2ps with dissolve
        j "And It doesn't need any additional stretching or whatever."
        scene bg fClub13c6ps with dissolve
        j "Just look at how strong my legs are. And that's just the beginning."
        scene bg fClub15c6ps with dissolve
        b "Suit yourself Julie, I just wanted to give an advice"
        scene bg fClub13c6ps with dissolve
        j "One.."
        scene bg fClub15c6ps with dissolve
        j "Two.."
        j "Thanks...I think that is enough for this exercise"
        j "Time to pump up my buttocks now !"
        b "..."
        scene bg fClub17c8ps with fade
        j "One.."
        scene bg fClub16c8ps with dissolve
        j "Two.."
        scene bg fClub17c8ps with dissolve
        j "Three.."
        scene bg fClub16c8ps with dissolve
        j "Four.."
        b "{i}Holy shit !"
        scene bg fClub17c8ps with dissolve
        j "Ah.."
        scene bg fClub16c8ps with dissolve
        j "It burns.."
        scene bg fClub17c8ps with dissolve
        j "No pain, no gain Julie !"
        scene bg fClub16c8ps with dissolve
        b "{i}Oh my god, I'm starting to get hard.."
        scene bg fClub17c8ps with dissolve
        j "You will have the best butt in the city Julie, come on, few more times !"
        scene bg fClub16c8ps with dissolve
        b "{i}No way.. I'm turned on by my own little [sis].. Am I out of my mind ?! I think I'd better leave before Julie notices my..condition.."
        scene bg fClub18c7_ps with fade
        j "Hey [bro], are you going to stand there and stare at me all day long ?!"
        scene bg fClub18c7ps with dissolve
        b "{i}Shit!"
        scene bg fClub18c7_ps with dissolve
        j "Because I have a feeling like..."
        scene bg fClub18c7ps with dissolve
        j "Are you checking me out or what ?"
        $ ep3checkingOut = 0
        menu:
            "Yes":
                $ ep3checkingOut = 1
                b "Yes I'm, so what ? You have an alluring sexy butt, Julie..."
                scene bg fClub19c7ps with dissolve
                j "..."
                b "{i}Okay, that was a mistake, I shouldn't have said it."
                b "Anyway, I don't want to distract you so I'm leaving. You will find me at the locker room if you need anything."
                j "..."
            "No":
                b "What are you talking about ?"
                scene bg fClub18c7_ps with dissolve
                j "Like you're checking out my butt..."
                b "The only thing I'm checking is whether your exercise technique is correct. But if it disturbs you I'll leave. I'm going to the locker room, call me if you need anything."
                j "..."
        scene black with Dissolve (1.0)
        $ renpy.pause()
        j "Ouch, ouch, ouch !"
        scene bg fClub20c9ps with hpunch
        j "Oh no no no !"
        b "Huh ?"
        scene bg fClub20c9ps with vpunch
        j "It hurts, It hurts !!!"
        scene bg fClub21c11ps with hpunch
        b "What happened, where does it hurt ?"
        j "{b}{i}Whines...{/i}{/b}\nIt's here, {i}sob-sob{/i}, right here, my thigh ! It burns like a fire and I can't move it, it's so painful..{i}sob-sob{/i}"
        b "Understood, it is spasm. Quickly, lay on your back, we need to straighten your leg as quick as possible ! Try to bend tip of your toe towards you, I will help you."
        $ renpy.pause()
        scene bg fClub22c15ps with fade
        j "Ah..."
        $ renpy.pause()
        b "How does it feel ?"
        j "Slightly better..."
        b "Good, we need to straighten it as much as we can. I will try to push your hip down and pull up your foot at the same time, ready ?"
        j "Ah, I think so..."
        scene bg fClub26c10ps with fade
        $ renpy.pause()
        b "Is that okay, Julie ?"
        j "Yes, the pain is fading away..."
        b "That means that we are doing everything right."
        j "I guess, ah..."
        $ ep3pussyTouched = 0
        menu:
            "Stop":
                b "That's it Julie, just sit like this for a few minutes. There is nothing to worry about."
                scene bg fClub23c16ps with fade
                j "Thank you, [bro]... What would I do without you ?"
                b "Warming-up, maybe ? Now you see what could happen. I think that is enough for today."
                j "Sorry. Too bad I didn't listen to your advice. From now on no workout without a stretching..."
                b "That's my girl."
                $ renpy.pause()
                jump ep3Nicole
            "Continue":
                scene bg fClub25c10ps with dissolve
                j "Ah.."
                j "That feels really good.."
                j "Now I can barely feel the pain.."
                b "That is because my hand is on your.."
                $ renpy.pause()
                b "It is at the base of your hip joint, there is no way I could straighten your leg anymore.."
                j "Oh.."
                menu:
                    "Stop":
                        b "That's it Julie, just sit like this for a few minutes. There is nothing to worry about."
                        scene bg fClub23c16ps with fade
                        j "Thank you, [bro]... What would I do without you ?"
                        b "Warming-up, maybe ? Now you see what could happen. I think that is enough for today."
                        j "Sorry. Too bad I didn't listen to your advice. From now on no workout without a stretching..."
                        b "That's my girl."
                        $ renpy.pause()
                        jump ep3Nicole
                    "Continue":
                        $ ep3pussyTouched = 1
                        scene bg fClub27c10ps with Dissolve (1.0)
                        j "Ah !"
                        b "{i}This moan was not caused by the pain, it was definitely a moan of pleasure. Damn, what is wrong me ?! Am I really sexually attracted to my little [sis] ?! No [bro], it's just this outfit and few days without a sex that's all."
                        j "[bro]..What are you.."
                        $ renpy.pause()
                        scene bg fClub25c10ps with dissolve
                        b "That's it Julie, just sit like this for a few minutes. There is nothing to worry about."
                        if ep2touchBoobie + ep3checkingOut == 3:
                            j "Wait a second..."
                            j "Did you just touched my pussy on purpose ?"
                            b "What ?"
                            scene bg fClub24c16ps with fade
                            j "Moment ago you said that you were checking me out, now you're touching my pussy...Of course, now I see the whole picture ! The last night wasn't just a dream, you really groped my breasts while I was asleep, didn't you ?!"
                            b "I was just.."
                            scene bg fClub24c16ps with vpunch
                            j "I can't believe this.. You are fucking pervert, you know that ?!"
                            j "Get your filthy hands off me !"
                            jump gameOver
                        else:
                            scene bg fClub23c16ps with fade
                            j "Thank you, [bro]... What would I do without you ?"
                            b "Warming-up, maybe ? Now you see what could happen. I think that is enough for today."
                            j "Sorry. Too bad I didn't listen to your advice. From now on no workout without a stretching..."
                            b "That's my girl."
                            $ renpy.pause()
                            jump ep3Nicole
        return

    label ep3Nicole:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Akşamın ilerleyen saatlerinde...")
        $ renpy.pause()
        b "{i}Ok, so Julie is sleeping at home she really needs some rest. I'm surprised that I didn't get any calls from work today, whole day without it feels a bit strange... Anyway, that means that I have some free time and I should call Nicole as I promised."
        menu:
            "Call":
                n "Oh hello again, [bro]. Yes I'm at home, come over."
                b "You can open the door, I'm on my way."
                n "Okay."
        $ renpy.pause()
        scene bg nApt0c3ps with Dissolve (1.5)
        b "Evening, Nicole. I hope it's not too late, I just couldn't come earlier."
        n "It's okay [bro], don't worry. I've just returned home too."
        $ renpy.pause()
        scene bg nApt1c3ps with dissolve
        n "Come on in, make yourself at home !"
        n "How's Julie ? Did she like the city ?"
        b "Yeah, she's been to the most interesting places, so there is no chances she wouldn't like it."
        b "By the way it's a nice and comfy place you have here."
        n "Thanks, but unfortunately it's not mine, I'm paying a rent."
        b "Oh, I see"
        $ renpy.pause()
        n "Are you going to stand there whole night ? I don't bite [bro], haha. The PC is on the table and now if you will excuse me I would like to change my clothes..."
        b "Sure, no problem. I will take a look in the meanwhile."
        n "..."
        b "I mean what is wrong with your PC."
        n "Haha"
        menu:
            "Come in":
                scene bg nApt2c2ps with fade
        n "Oh, where are my manners ? I didn't even offer you a drink. Would you like something ?"
        b "No, I'm good, thanks."
        n "Are you sure ? I have a bottle of wine and really good whisky.."
        b "I might have to drive a car today, so thanks, but 'No thanks'."
        n "I see..."
        $ renpy.pause()
        scene bg nApt3c2ps with dissolve
        n "Anyway, feel free to ask me if you need anything. I'll be right back in few minutes..."
        b "Okay."
        $ renpy.pause()
        scene bg nApt4c4ps with fade
        b "{i}Damn, she is so cute. The kindest woman I ever met... Okay back to business, [bro]. Here is the laptop on the table."
        b "{i}Hold on.. What is that, under the TV ?"
        jump ep3Nicole2
        return

    screen ep3Nicole2Scr:
        imagemap:
            ground "images/ep3/nApt4c4ps.png"
            hotspot (603,640,149,102) clicked Return("pc") hovered ShowTransient("imgHider", img="images/ep3/nApt4c4_Lps.png") unhovered Hide("imgHider")
            hotspot (1611,625,62,58) clicked Return("cam") hovered ShowTransient("imgHider", img="images/ep3/nApt4c4_Cps.png") unhovered Hide("imgHider")

    label ep3Nicole2:
        call screen ep3Nicole2Scr
        $ result = _return
        if result == "pc":
            b "{i}Whatever, the real problem is the computer"
        if result == "cam":
            scene bg nApt6c1ps with fade
            b "{i}A camera ? It's pointing right at the couch.. What the.."
            b "Nicole, I didn't know that you are making photos. Is this your hobbie ?"
            n "Yes.. I mean, no.. It was my hobbie but now it's more like a job to me, I decided to change the profession some time ago so.. By the way you can take a look at some of my photos at the wall."
            scene bg nApt6c7ps with fade
            b "..."
            n "Do you like them ?"
            b "They are amazing.."
            n "Thanks, I'm still far from the professional shoots, but I just recently started doing it so I think that's okay."
            b "I didn't think that someone's first photos can be that good at the very beginning.."
            n "That is crazy, right ? My buyers say that I have a talent for it !"
            b "You really do.."
            b "..."
            b "{i}Time to get back to the laptop"
        scene bg nApt8c6ps with fade
        b "{i}So what is wrong with it this time ? I should probably ask Nicole more about it and what she's already tried."
        b "Nicole, could you please tell me what exactly is wrong with it ? Did you try to use troubleshooting or something like this ?"
        n "No, I didn't try anything. I don't even know where this 'troubleshooting' is. The problem is the PC just won't start. Once I get the 'Welcome screen' it freezes and I have to restart it but it doesn't help, the same happens over and over again..."
        b "Understood"
        b "{i}Looks like it's the issue with the 'Startup'. Let's try to fix this."
        scene bg nApt5c5ps with fade
        $ ep3startupRepairDone = 0
        menu:
            "Open BIOS Settings":
                b "{i}Maybe I could find something useful here ?"
                menu:
                    "UEFI Firmware Settings":
                        b "{i}Holy crap, why there is only 'so few' options ?!"
                        menu:
                            "Exit BIOS":
                                b "{i}Probably the best option"
                                jump ep3Nicole3
                            "CPU Config":
                                b "{i}No way...there is even more options. Exit now !"
                                jump ep3Nicole3
                            "IDE Config":
                                b "{i}No way...there is even more options. Exit now !"
                                jump ep3Nicole3
                            "SuperIO Config":
                                b "{i}No way...there is even more options. Exit now !"
                                jump ep3Nicole3
                            "ACPI Config":
                                b "{i}No way...there is even more options. Exit now !"
                                jump ep3Nicole3
                            "Next page":
                                b "{i}Luckily there is only two pages"
                                menu:
                                    "Hyper Transport Config":
                                        b "{i}No way...there is even more options. Exit now !"
                                        jump ep3Nicole3
                                    "IPMI 2.0 Config":
                                        b "{i}No way...there is even more options. Exit now !"
                                        jump ep3Nicole3
                                    "MPS Config":
                                        b "{i}No way...there is even more options. Exit now !"
                                        jump ep3Nicole3
                                    "PCI Express Config":
                                        b "{i}No way...there is even more options. Exit now !"
                                        jump ep3Nicole3
                                    "System message":
                                        "{i}{b}{color=#00FF00}PPU{/color}{/b} is coming... watch out for the {b}{color=#ff0000}RDHDS{/color}{/b}... critical kernel error {color=#0000FF}0x0000001A{/color}... please stand by..."
                                        b "{i}What is that supposed to mean ?!"
                                        jump ep3Nicole3
                                    "USB Config":
                                        b "{i}No way...there is even more options. Exit now !"
                                        jump ep3Nicole3
                    "Load System Defaults":
                        b "{i}Sometimes it helps, who knows maybe this time is the lucky one ?"
                        b "{i}Save changes and restart"
                        jump ep3Nicole3
                    "Exit BIOS":
                        b "{i}Nah, probably there is nothing that might help me"
                        b "{i}Exit and restart"
                        jump ep3Nicole3
            "Boot into Safe Mode":
                b "{i}Maybe I could find something useful here ?"
                menu:
                    "Continue using PC in safe mode":
                        b "{i}..."
                        jump ep3Nicole3
                    "Command prompt":
                        b "{i}What am I supposed to type  in here, 'Please work' ?"
                        jump ep3Nicole3
                    "Troubleshoot":
                        b "{i}That is more like it..."
                        menu:
                            "System restore":
                                b "{i}How about this one ?"
                                b "{i}..."
                                b "{i}... ..."
                                jump ep3Nicole3
                            "Startup repair":
                                $ ep3startupRepairDone = 1
                                b "{i}How about this one ?"
                                b "{i}..."
                                b "{i}... ..."
                                jump ep3Nicole3
                            "Startup settings":
                                b "{i}How about this one ?"
                                b "{i}..."
                                b "{i}... ..."
                                jump ep3Nicole3
        return

    label ep3Nicole3:
        if ep3startupRepairDone == 1:
            b "{i}Looks like it helped !"
            jump ep3Nicole4
        else:
            b "{i}Damn, it didn't help at all, still freezes. Restart..."
            menu ep3ScrewYouWin10:
                "Open BIOS Settings":
                    b "{i}Maybe I could find something useful here ?"
                    menu:
                        "UEFI Firmware Settings":
                            b "{i}Holy crap, why there is only 'so few' options ?!"
                            menu:
                                "Exit BIOS":
                                    b "{i}Probably the best option"
                                    jump ep3Nicole3
                                "CPU Config":
                                    b "{i}No way...there is even more options. Exit now !"
                                    jump ep3Nicole3
                                "IDE Config":
                                    b "{i}No way...there is even more options. Exit now !"
                                    jump ep3Nicole3
                                "SuperIO Config":
                                    b "{i}No way...there is even more options. Exit now !"
                                    jump ep3Nicole3
                                "ACPI Config":
                                    b "{i}No way...there is even more options. Exit now !"
                                    jump ep3Nicole3
                                "Next page":
                                    b "{i}Luckily there is only two pages"
                                    menu:
                                        "Hyper Transport Config":
                                            b "{i}No way...there is even more options. Exit now !"
                                            jump ep3Nicole3
                                        "IPMI 2.0 Config":
                                            b "{i}No way...there is even more options. Exit now !"
                                            jump ep3Nicole3
                                        "MPS Config":
                                            b "{i}No way...there is even more options. Exit now !"
                                            jump ep3Nicole3
                                        "PCI Express Config":
                                            b "{i}No way...there is even more options. Exit now !"
                                            jump ep3Nicole3
                                        "System message":
                                            "{i}{b}{color=#00FF00}PPU{/color}{/b} is coming... watch out for the {b}{color=#ff0000}RDHDS{/color}{/b}... critical kernel error {color=#0000FF}0x0000001A{/color}... please stand by..."
                                            b "{i}What is that supposed to mean ?!"
                                            jump ep3Nicole3
                                        "USB Config":
                                            b "{i}No way...there is even more options. Exit now !"
                                            jump ep3Nicole3
                        "Load System Defaults":
                            b "{i}Sometimes it helps, who knows maybe this time is the lucky one ?"
                            b "{i}Save changes and restart"
                            jump ep3Nicole3
                        "Exit BIOS":
                            b "{i}Nah, probably there is nothing that might help me"
                            b "{i}Exit and restart"
                            jump ep3Nicole3
                "Boot into Safe Mode":
                    b "{i}Maybe I could find something useful here ?"
                    menu:
                        "Continue using PC in safe mode":
                            b "{i}..."
                            b "{i}... ..."
                            jump ep3Nicole3
                        "Command prompt":
                            b "{i}What am I supposed to type  in here, 'Please work' ?"
                            jump ep3Nicole3
                        "Troubleshoot":
                            b "{i}That is more like it..."
                            menu:
                                "System restore":
                                    b "{i}How about this one ?"
                                    b "{i}..."
                                    b "{i}... ..."
                                    jump ep3Nicole3
                                "Startup repair":
                                    $ ep3startupRepairDone = 1
                                    b "{i}How about this one ?"
                                    b "{i}..."
                                    b "{i}... ..."
                                    b "{i}... ... ..."
                                    jump ep3Nicole3
                                "Startup settings":
                                    b "{i}How about this one ?"
                                    b "{i}..."
                                    b "{i}... ..."
                                    jump ep3Nicole3
        return

    label ep3Nicole4:
        $ ep3NicoleHandjobDone = 0
        scene bg nApt8c6ps with fade
        b "Hey, Nicole ! I have a good news for you ! Looks like I've fixed it. It was a bit tricky but eventually I've made it !"
        n "..."
        scene bg nApt7c6ps with Dissolve (2.0)
        n "I'm glad to hear it, [bro]. What would I do without you...?"
        $ renpy.pause()
        scene bg nApt9c9ps with fade
        b "{i}Oh my God !"
        $ renpy.pause()
        n "Ahm..I'm so clumsy when it comes to computers.."
        b "Nicole... You look so"
        $ ep3NicoleLooksHot = 0
        menu:
            "Adorable":
                b "Adorable.."
            "Beautiful":
                b "Beautiful.."
            "Fucking Hot":
                $ ep3NicoleLooksHot = 1
                b "Fucking hot and sexy.."
        n "Ahm, thank you [bro].."
        scene bg nApt10c8ps with fade
        b "{i}I can't believe this, Nicole is almost naked in front of me.."
        b "{i}Looks like she's a bit nervous though. Probably it's because she might be thinking she's too old for me, she is at the same age as my [mom]."
        $ renpy.pause()
        n "Ahm..."
        b "{i}I need to break the ice !"
        b "Come on Nicole, please sit beside me. Your legs are amazing but you should give them a little rest."
        n "Right..."
        scene bg nApt11c11ps with fade
        b "{i}That's better. I wonder if she's wearing any panties under this dress."
        $ renpy.pause()
        n "[bro]... I know that I promised to thank you not only with the words... But unfortunately I don't have enough money right now... So..."
        scene bg nApt12c12ps with fade
        b "{i}She is leaning towards me. Nicole... If she only knew how badly I want her right now."
        $ renpy.pause()
        n "I thought if you could just wait for a while until I get paid... Or maybe we could come up with some sort of... "
        menu:
            "Kiss her":
                play sound ("music/sounds/kiss.mp3")
                scene bg nApt13c14ps with kissFlash
        n "Mwah!"
        b "{i}Yes, Nicole"
        n "{i}Ah, mwa..."
        b "{i}Her lips are soft like velvet"
        b "{i}She is still a bit strained, let's add some heat"
        menu:
            "Use tongue":
                play sound ("music/sounds/wetKiss.mp3")
        scene bg nApt14c14ps with dissolve
        n "{i}Mwaaah..moan.."
        b "{i}Yes, give me that sweet tongue.."
        b "{i}That is incredible what she does with it.."
        n "{i}slurp..mwah.."
        b "{i}She's put her hand on my leg..."
        scene bg nApt17c13ps with fade
        n "{i}oh, mwah.. slurp.."
        b "{i}That's it Nicole, just like that.. Move your hand towards my dick.. You do know it is already hard as rock for you.. "
        $ renpy.pause()
        if ep3NachoBeaten == 0:
            b "{i}Huh ? What happened...?!"
            scene bg nApt15c10ps with fade
            n "I... I'm sorry [bro]..."
            b "What is wrong Nicole ?"
            n "I... I feel so stupid now... "
            b "Why did I do something wrong ?"
            n "No, it's me not you... I'm just... Oh my god I feel like I'm a little stupid girl right now, I thought that I can do it, but I was wrong... I'm sorry [bro], but I'm really not ready for this yet... "
            $ renpy.pause()
            b "Sure, take your time Nicole. There is no need to rush."
            scene bg nApt12c10ps with dissolve
            n "Thank you [bro]. I knew you would understand... It's just really difficult for me to be so close with someone again... "
            n "I promise I'll tell you everything when I'm ready... It's just not today..."
            b "I understand..."
            n "Thanks again [bro], you are a good guy..."
            b "..."
            b "I think I'd better leave now. Good night, Nicole."
            n "Good night, [bro]..."
            jump episode4
        else:
            if ep3NicoleLooksHot == 1:
                b "{i}Huh ? What happened...?!"
                scene bg nApt15c10ps with fade
                n "I... I'm sorry [bro]..."
                b "What is wrong Nicole ?"
                n "I... I feel so stupid now... "
                b "Why did I do something wrong ?"
                n "No, it's me not you... I'm just... Oh my god I feel like I'm a little stupid girl right now, I thought that I can do it, but I was wrong... I'm sorry [bro], but I'm really not ready for this yet... "
                $ renpy.pause()
                b "Sure, take your time Nicole. There is no need to rush."
                scene bg nApt12c10ps with dissolve
                n "Thank you [bro]. I knew you would understand... It's just really difficult for me to be so close with someone again... "
                n "I promise I'll tell you everything when I'm ready... It's just not today..."
                b "I understand..."
                n "Thanks again [bro], you are a good guy..."
                b "..."
                b "I think I'd better leave now. Good night, Nicole."
                n "Good night, [bro]..."
                jump episode4
            else:
                $ ep3NicoleHandjobDone = 1
                scene bg nApt16c13ps with dissolve
                n "{i}Oh..mwah..slurp.."
                b "{i}That's a good girl, caress it gently. Feel it throbbing just for you."
                n "{i}Mmm..wah..slurp.."
                b "{i}I can't hold it any longer, I have to take off the pants or will blow my load right inside"
                menu:
                    "Take off the pants":
                        play sound ("music/sounds/jeansZipper.mp3")
                        scene bg nApt23c10ps with fade
                        play sound ("music/sounds/femaleGasps.mp3")
                        n "Oh my god [bro] ! It's huge ! I've never seen that big one in my entire life..."
                        b "It's just for you, Nicole."
                        $ renpy.pause()
                        n "I... I don't know what to say, [bro]"
                        b "You don't have to say anything, just play with it for a bit."
                        b "{i}Or wrap it with your soft sexy lips"
                        n "I'm not ready for this [bro], I'm sorry. It all just happened so fast..."
                        n "But I can't let you go with a blue balls either, so..."
                        scene bg nApt22c10ps with Dissolve (1.5)
                        n "Would you mind this kind of compromise...?"
                        $ renpy.pause()
                        scene bg nApt19c14ps with fade
                        b "{i}Oh shit! Her grip is soft and stiff at the same time, how could that be even possible ?! I can feel the warmth from her tender hand on my shaft."
                        $ renpy.pause()
                        scene bg nApt18c14ps with Dissolve (0.75)
                        n "How about that...?"
                        b "Oh my God, Nicole ! I think no man would ever told you 'No' with his dick in your hand, it's so amazing."
                        play sound ("music/sounds/femaleGiggle.mp3")
                        n "It's my special handjob technique. I call it 'Gentle thumb'..."
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        b "Oh shit, Nicole ! Your thumb glides along so good, it's incredible how it flickers my glans each time !"
                        b "Please don't stop..."
                        scene bg nApt22c10ps with fade
                        n "I'll stop only when you blow your load of a hot sticky cum on my hand..."
                        b "Oh, shit I think it won't take long with such a dirty talking..."
                        scene bg nApt19c14ps with fade
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt22c10ps with fade
                        n "So you are a fan of dirty talk, huh ?"
                        n "How about this..."
                        scene bg nApt19c14ps with fade
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        n "I don't want you to think of me as a whore... But.."
                        scene bg nApt22c10ps with fade
                        n "Today at the store when you kicked the shit out of that jerk I got so excited..."
                        b "Oh shit..."
                        scene bg nApt19c14ps with fade
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt22c10ps with fade
                        n "Too bad I wasn't wearing any panties..."
                        b "Oh fuck... And why do you think it's bad ?"
                        scene bg nApt19c14ps with fade
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        n "Because on our way home I was only thinking about..."
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        scene bg nApt19c14ps with Dissolve (0.75)
                        scene bg nApt18c14ps with Dissolve (0.75)
                        n "If you noticed the wet spot on my jeans between my legs or not..."
                        b "Oh Fuck ! You did it ! I'm comming !"
                        scene bg nApt19c14ps with Dissolve (0.5)
                        scene bg nApt18c14ps with Dissolve (0.5)
                        scene bg nApt19c14ps with Dissolve (0.5)
                        scene bg nApt18c14ps with Dissolve (0.5)
                        scene bg nApt19c14ps with Dissolve (0.5)
                        scene bg nApt18c14ps with Dissolve (0.5)
                        b "AAAAAAAAAAAAARGH !!!"
                        scene bg nApt18c14ps with cumFlash
                        scene bg nApt19c14ps with cumFlash
                        scene bg nApt18c14ps with cumFlash
                        scene bg nApt20c14ps with cumFlash
                        scene bg nApt20c14ps with vpunch
                        scene bg nApt20c14ps with vpunch
                        b "Fuck !"
                        n "Oh my god [bro] ! It so much cum !"
                        scene bg nApt21c15ps with fade
                        b "Holy shit... Ms. Nicole, it was the best handjob in my entire life..."
                        n "It's just Nicole, remember...?"
                        $ renpy.pause()
                        jump episode4
        return

####################################################EPISODE_4##################################################

    image bg atHome66c1ps = "images/ep4/atHome66c1ps.png"
    image bg atHome66c5ps = "images/ep4/atHome66c5ps.png"
    image bg atHome67c1ps = "images/ep4/atHome67c1ps.png"
    image bg atHome68c2ps = "images/ep4/atHome68c2ps.png"
    image bg atHome69c2ps = "images/ep4/atHome69c2ps.png"
    image bg atHome70c6ps = "images/ep4/atHome70c6ps.png"
    image bg atHome71c6ps = "images/ep4/atHome71c6ps.png"
    image bg atHome72c7ps = "images/ep4/atHome72c7ps.png"
    image bg atHome73c4ps = "images/ep4/atHome73c4ps.png"
    image bg atHome74c8ps = "images/ep4/atHome74c8ps.png"
    image bg atHome74c9ps = "images/ep4/atHome74c9ps.png"
    image bg atHome74c10ps = "images/ep4/atHome74c10ps.png"
    image bg atHome75c4ps = "images/ep4/atHome75c4ps.png"
    image bg atHome76c4ps = "images/ep4/atHome76c4ps.png"
    image bg atHome76c4_ps = "images/ep4/atHome76c4_ps.png"
    image bg atHome77c4ps = "images/ep4/atHome77c4ps.png"
    image bg atHome78c4ps = "images/ep4/atHome78c4ps.png"
    image bg atHome79c4ps = "images/ep4/atHome79c4ps.png"
    image bg atHome80c4ps = "images/ep4/atHome80c4ps.png"
    image bg atHome81c4ps = "images/ep4/atHome81c4ps.png"
    image bg atHome82c6ps = "images/ep4/atHome82c6ps.png"
    image bg atHome82c7ps = "images/ep4/atHome82c7ps.png"
    image bg atHome82c9ps = "images/ep4/atHome82c9ps.png"
    image bg atHome82c10ps = "images/ep4/atHome82c10ps.png"
    image bg atHome83c7ps = "images/ep4/atHome83c7ps.png"
    image bg atHome84c6ps = "images/ep4/atHome84c6ps.png"
    image bg atHome85c11ps = "images/ep4/atHome85c11ps.png"
    image bg atHome86c12ps = "images/ep4/atHome86c12ps.png"
    image bg atHome87c13ps = "images/ep4/atHome87c13ps.png"
    image bg atHome88c14ps = "images/ep4/atHome88c14ps.png"
    image bg atHome89c16ps = "images/ep4/atHome89c16ps.png"
    image bg atHome90c11ps = "images/ep4/atHome90c11ps.png"
    image bg atHome90c13ps = "images/ep4/atHome90c13ps.png"
    image bg atHome90c14ps = "images/ep4/atHome90c14ps.png"
    image bg atHome91c14ps = "images/ep4/atHome91c14ps.png"

    image bg streets0c4ps = "images/ep4/streets0c4ps.png"
    image bg streets1c5ps = "images/ep4/streets1c5ps.png"
    image bg streets2c7ps = "images/ep4/streets2c7ps.png"
    image bg streets3c7ps = "images/ep4/streets3c7ps.png"
    image bg streets4c2ps = "images/ep4/streets4c2ps.png"
    image bg streets5c1ps = "images/ep4/streets5c1ps.png"
    image bg streets6c1ps = "images/ep4/streets6c1ps.png"
    image bg streets6c1ps_ = "images/ep4/streets6c1ps_.png"
    image bg streets7c1ps = "images/ep4/streets7c1ps.png"
    image bg streets8c1ps = "images/ep4/streets8c1ps.png"
    image bg streets8c1ps_ = "images/ep4/streets8c1ps_.png"
    image bg streets9c1ps = "images/ep4/streets9c1ps.png"

    image bg m5c4ps = "images/ep4/m5c4ps.png"
    image bg m5c4ps_ = "images/ep4/m5c4ps_.png"
    image bg m6c5ps = "images/ep4/m6c5ps.png"
    image bg m6c7ps = "images/ep4/m6c7ps.png"
    image bg m6c9ps = "images/ep4/m6c9ps.png"
    image bg m7c11ps = "images/ep4/m7c11ps.png"
    image bg m8c10ps = "images/ep4/m8c10ps.png"
    image bg m9_c7ps = "images/ep4/m9_c7ps.png"
    image bg m9c7_ps = "images/ep4/m9c7_ps.png"
    image bg m9c7ps = "images/ep4/m9c7ps.png"
    image bg m10c5ps = "images/ep4/m10c5ps.png"
    image bg m11c5ps = "images/ep4/m11c5ps.png"
    image bg m12_c5ps = "images/ep4/m12_c5ps.png"
    image bg m12c5ps = "images/ep4/m12c5ps.png"
    image bg m13_c9ps = "images/ep4/m13_c9ps.png"
    image bg m13c8ps = "images/ep4/m13c8ps.png"
    image bg m13c9ps = "images/ep4/m13c9ps.png"

    image bg nBar1c1ps = "images/ep4/nBar1c1ps.png"
    image bg nBar2c2ps = "images/ep4/nBar2c2ps.png"
    image bg nBar3c2ps = "images/ep4/nBar3c2ps.png"
    image bg nBar4c2ps = "images/ep4/nBar4c2ps.png"
    image bg nBar4c2_ps = "images/ep4/nBar4c2_ps.png"
    image bg nBar5c2_ps = "images/ep4/nBar5c2_ps.png"
    image bg nBar5c2ps = "images/ep4/nBar5c2ps.png"
    image bg nBar6c1ps = "images/ep4/nBar6c1ps.png"
    image bg nBar7c2ps = "images/ep4/nBar7c2ps.png"
    image bg nBar8c3ps = "images/ep4/nBar8c3ps.png"
    image bg nBar9c3ps = "images/ep4/nBar9c3ps.png"
    image bg nBar10c3ps = "images/ep4/nBar10c3ps.png"

    image bg streets10c4ps = "images/ep4/streets10c4ps.png"
    image bg streets11c6ps = "images/ep4/streets11c6ps.png"
    image bg streets11c7ps = "images/ep4/streets11c7ps.png"
    image bg streets11c8ps = "images/ep4/streets11c8ps.png"
    image bg streets12c10ps = "images/ep4/streets12c10ps.png"
    image bg streets12c11ps = "images/ep4/streets12c11ps.png"
    image bg streets13c10ps = "images/ep4/streets13c10ps.png"
    image bg streets14c8ps = "images/ep4/streets14c8ps.png"
    image bg streets14c11ps = "images/ep4/streets14c11ps.png"
    image bg streets14c12ps = "images/ep4/streets14c12ps.png"
    image bg streets15_c7ps = "images/ep4/streets15_c7ps.png"
    image bg streets15c7ps = "images/ep4/streets15c7ps.png"
    image bg streets15c9ps = "images/ep4/streets15c9ps.png"
    image bg streets16c9ps = "images/ep4/streets16c9ps.png"
    image bg streets17_c13ps = "images/ep4/streets17_c13ps.png"
    image bg streets17c13ps = "images/ep4/streets17c13ps.png"
    image bg streets18_1c14ps = "images/ep4/streets18_1c14ps.png"
    image bg streets18_c14ps = "images/ep4/streets18_c14ps.png"
    image bg streets18_c15ps = "images/ep4/streets18_c15ps.png"
    image bg streets18c14ps = "images/ep4/streets18c14ps.png"
    image bg streets18c14psCum = "images/ep4/streets18c14psCum.png"
    image bg streets19c13_ps = "images/ep4/streets19c13_ps.png"
    image bg streets19c13ps = "images/ep4/streets19c13ps.png"
    image bg streets20c13_ps = "images/ep4/streets20c13_ps.png"
    image bg streets20c13ps = "images/ep4/streets20c13ps.png"
    image bg streets21c18ps = "images/ep4/streets21c18ps.png"
    image bg streets22c16_ps = "images/ep4/streets22c16_ps.png"
    image bg streets22c16ps = "images/ep4/streets22c16ps.png"
    image bg streets23_c17__ps = "images/ep4/streets23_c17__ps.png"
    image bg streets23_c17_ps = "images/ep4/streets23_c17_ps.png"
    image bg streets23_c17ps = "images/ep4/streets23_c17ps.png"
    image bg streets23c17ps = "images/ep4/streets23c17ps.png"
    image bg streets24c16ps = "images/ep4/streets24c16ps.png"
    image bg streets25c15ps = "images/ep4/streets25c15ps.png"
    image bg streets26c16ps = "images/ep4/streets26c16ps.png"
    image bg streets27_c16ps = "images/ep4/streets27_c16ps.png"
    image bg streets27c16ps = "images/ep4/streets27c16ps.png"
    image bg streets28c17ps = "images/ep4/streets28c17ps.png"
    image bg streets29_c17ps = "images/ep4/streets29_c17ps.png"
    image bg streets29c17ps = "images/ep4/streets29c17ps.png"

    image bg atHome92c2ps = "images/ep4/atHome92c2ps.png"
    image bg atHome93c1ps = "images/ep4/atHome93c1ps.png"
    image bg atHome93c1_ps = "images/ep4/atHome93c1_ps.png"
    image bg atHome94c1ps = "images/ep4/atHome94c1ps.png"
    image bg atHome95_c3ps = "images/ep4/atHome95_c3ps.png"
    image bg atHome95c3ps = "images/ep4/atHome95c3ps.png"
    image bg atHome95c3ps_ = "images/ep4/atHome95c3ps_.png"
    image bg atHome96c3ps = "images/ep4/atHome96c3ps.png"
    image bg atHome96_c3ps = "images/ep4/atHome96_c3ps.png"
    image bg atHome97c3ps = "images/ep4/atHome97c3ps.png"

    image bg dream1c2ps = "images/ep4/dream1c2ps.png"
    image bg dream2c1ps = "images/ep4/dream2c1ps.png"
    image bg dream3c1ps = "images/ep4/dream3c1ps.png"
    image bg dream3c3ps = "images/ep4/dream3c3ps.png"
    image bg dream4c2ps = "images/ep4/dream4c2ps.png"
    image bg dream5c4ps = "images/ep4/dream5c4ps.png"
    image bg dream6c4_ps = "images/ep4/dream6c4_ps.png"
    image bg dream6c4ps = "images/ep4/dream6c4ps.png"
    image bg dream7c4ps = "images/ep4/dream7c4ps.png"
    image bg dream8c2ps = "images/ep4/dream8c2ps.png"
    image bg dream9c2_ps = "images/ep4/dream9c2_ps.png"
    image bg dream9c2ps = "images/ep4/dream9c2ps.png"
    image bg dream10c2ps = "images/ep4/dream10c2ps.png"
    image bg dream11c2_ps = "images/ep4/dream11c2_ps.png"
    image bg dream11c2ps = "images/ep4/dream11c2ps.png"
    image bg dream11c2ps_1 = "images/ep4/dream11c2ps_1.png"
    image bg dream11c2ps_2 = "images/ep4/dream11c2ps_2.png"
    image bg dream12c6ps = "images/ep4/dream12c6ps.png"
    image bg dream13c1_ps = "images/ep4/dream13c1_ps.png"
    image bg dream13c1ps = "images/ep4/dream13c1ps.png"
    image bg dream14c1ps = "images/ep4/dream14c1ps.png"
    image bg dream15c1ps = "images/ep4/dream15c1ps.png"
    image bg dream16c1_1ps = "images/ep4/dream16c1_1ps.png"
    image bg dream16c1_ps = "images/ep4/dream16c1_ps.png"
    image bg dream16c1ps = "images/ep4/dream16c1ps.png"

    image bg streets1c5psN = "images/ep4/streets1c5psN.png"
    image bg streets3c7psN = "images/ep4/streets3c7psN.png"
    image bg streets7c1psN = "images/ep4/streets7c1psN.png"
    image bg m6c9psN = "images/ep4/m6c9psN.png"

    init python:
        diss = Dissolve(.75, alpha=True)
        def Ani(img_name, frames, delay=.1, loop=True, reverse=False, effect=diss, start=0, ext="png", **properties):
            if img_name:
                args = []
                for i in range(start, start + frames):
                    if ext is None:
                        args.append(renpy.easy.displayable(img_name + str(i)))
                    else:
                        args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
                    if reverse or loop or (i < start + frames - 1):
                        args.append(delay)
                        args.append(effect)
                    if reverse:
                        for i in range(start + frames - 2, start, -1):
                            if ext is None:
                                args.append(renpy.easy.displayable(img_name + str(i)))
                            else:
                                args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
                                if loop or (i > start + 1):
                                    args.append(delay)
                                    args.append(effect)
                return anim.TransitionAnimation(*args, **properties)
            return None

    init:
        image ep4hj = Ani("ep4/ep4hj", 2, 1.0, True, False)

    label episode4:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra evde...")
        $ renpy.pause()
        b "{i}Wow, what a day..."
        b "{i}Looks like it will be the first day without any urgent things that should be taken care of. This all seems really strange considering what is going on and what might happen in the foreseeable future."
        b "{i}Also I still didn't get any further instructions about what should I do with the 'package'. I never really cared about such things, I was just doing my job, but now I wonder what is inside of it..."
        b "{i}Damn, I hope that bosses will come up to an agreement. I think nobody wants starting a war... But what if it's inevitable ? What if this is just a matter of time ?"
        b "{i}Too many questions without an answer..."
        b "{i}I should probably call it a day. It's a late night already and I'm tired."
        $ renpy.pause()
        b "{i}Strange, Julie didn't close the door... I don't want to wake her up but I need to check if everything is okay."
        menu:
            "Enter the bedroom":
                scene bg atHome66c1ps with Dissolve (1.5)
        $ renpy.pause()
        j "..."
        b "{i}Looks like everything is ok, Julie is sleeping like a baby..."
        scene bg atHome66c5ps with fade
        b "{i}She is so cute, defenseless and innocent right now. I won't forgive myself if anything happens to her because of me."
        $ renpy.pause()
        b "{i}Okay, it's time for me to go sleeping as well.."
        b "{i}{b}Whispering:{/b}{/i}\nSweet dreams, Julie..."
        scene bg atHome66c1ps with fade
        menu:
            "Go to sleep":
                scene bg atHome67c1ps with Dissolve (1.0)
        j "[bro]..? Is that you ?"
        b "{i}Huh..?"
        menu:
            "Turn around":
                scene bg atHome68c2ps with fade
        b "Julie.. I'm sorry I woke you up, I just wanted to check if everything is okay."
        scene bg atHome69c2ps with Dissolve (1.25)
        j "It's okay, you didn't wake me. I wasn't sleeping, I just..can't fall asleep.."
        b "Why..? Is something bothering you ?"
        scene bg atHome71c6ps with fade
        j "No, not really..It's nothing serious just my leg still a bit sore..and there are few things I wanted to ask you about.."
        scene bg atHome70c6ps with dissolve
        j "Please come in and take a seat beside me.. It won't take long.."
        b "Sure Julie, I'm always here for you.."
        scene bg atHome72c7ps with fade
        b "Why don't you move your leg towards me, I'll massage it and in the meanwhile you'll tell me what's the deal."
        j "Oh, [bro] you don't have to.. It's okay, really.."
        scene bg atHome73c4ps with fade
        b "Come on, it's the least I can do for my little [sis]."
        j "Okay.."
        scene bg atHome74c8ps with fade
        b "Here you go it will ease the sore."
        j "Oh, thank you, [bro].."
        scene bg atHome74c9ps with fade
        b "How does it feel, Julie..?"
        j "Mmm..That's exactly what I needed.."
        scene bg atHome74c10ps with fade
        b "{i}It's amazing.. Her skin is so smooth and soft.. Just gliding along and massaging her thigh is so incredibly pleasant.."
        j "Mmm..Just like that, [bro].."
        scene bg atHome75c4ps with fade
        b "So..What's up ?"
        j "Mmm..."
        $ renpy.pause()
        b "Julie..?"
        scene bg atHome76c4ps with Dissolve (0.75)
        j "Oops, looks like I was floating on cloud nine, ha ha.. It just feels so good. Your hands so strong and gentle at the same time..Your warm palms gave me goosebumps, I literally melted.."
        b "I'm glad to hear it, baby"
        scene bg atHome76c4_ps with dissolve
        j "Ahm.."
        j "I'm not quite comfortable to ask you about it.. It concerns the money.. It's not about our forthcoming visit to the bank.."
        j "I mean.. You already did a lot for me and.. Now I just feel.."
        b "Come on, Julie, just say it. Do you need some money ?"
        scene bg atHome76c4ps with dissolve
        j "Yeah, you see Scarlett arrives to the city tomorrow but unfortunatelly I'm a bit short of money.."
        $ ep4moneyScarlett = 0
        $ ep4moneyWhy = 0
        menu ep4money:
            "Who is Scarlett ?" if ep4moneyScarlett == 0:
                $ ep4moneyScarlett += 1
                scene bg atHome78c4ps with dissolve
                j "She is the best! Scarlett is my girlfriend and my lover.. I can't wait to introduce you to each other, hope you will like her !"
                b "Wow..That was quite of 'coming out' right now, wasn't it..?"
                scene bg atHome77c4ps with dissolve
                j "Oh, come on [bro]... It's 2k18 outside, a lot of people are open minded to that kind of stuff.."
                b "I guess..I mean, I just didn't know that {b}You{/b} are lesbian.."
                j "Well, that is good that we figured that out, right ?"
                scene bg atHome76c4ps with dissolve
                jump ep4money
            "Why do you need the money ?" if ep4moneyWhy == 0:
                $ ep4moneyWhy += 1
                scene bg atHome76c4_ps with dissolve
                j "We wanted to visit some cafes and city malls, maybe clothing stores.. You know, girlish places.."
                j "There are still some money left that [mom] gave me.. I just don't think that it will be enough.. So I was wondering if I could ask you about some extra money until I start earn them myself.."
                scene bg atHome76c4ps with dissolve
                jump ep4money
            "Sure":
                scene bg atHome78c4ps with dissolve
                j "Really ?"
                b "Of course, I fully understand the situation. We are [family] after all, and we must take care of each other.."
        b "You can ask me anything you want, Julie. If you ever need something just tell me. I will do everything I can.."
        scene bg atHome76c4ps with dissolve
        j "[bro].."
        b "I've been away for too long, Julie.. But now I will be here with you and for you.."
        scene bg atHome79c4ps with Dissolve(0.75)
        j "I don't know what to say.. I mean, of course I'm thankful but.. At the same time I feel so ashamed.. I want to apologize, [bro].."
        $ renpy.pause()
        j "You've been helping us all this time and..I..I was just so selfish.."
        j "I'm really sorry for what I've said that day.. I didn't mean it.. I was so wrong about you.. I.. {i}*sob*{/i}"
        b "Hey stop it right now, Julie ! Look at me... We don't need a flood here, right ?"
        scene bg atHome80c4ps with Dissolve(0.75)
        j "Huh, right..{i}*sob*{/i}"
        $ renpy.pause()
        b "I'm the one who should apologize. It is true. I really distanced myself and was acting weird, but.. I did it only because I want you and [mom] be safe.."
        scene bg atHome73c4ps with Dissolve(0.75)
        j "But why..? Is it your job..? Is it THAT dangerous..?"
        b "{i}I can't tell her that I'm a criminal, at least not right now.. I barely returned our good old relations and I don't want to fuck everything up again.."
        b "{i}I need to change the topic. I'll tell her the truth but present it like a joke.. Hopefully it will work.."
        b "Yes Julie, it's really dangerous and super-duper secret. No one should know about it! So I won't tell you a thing either!"
        scene bg atHome77c4ps with dissolve
        j "Hm..Let me guess. You are a spy and if I find out what you're doing you will have to kill me, right ? Ha-ha.."
        b "Exactly.."
        scene bg atHome81c4ps with dissolve
        j "Ha-ha, looks like someone forgot what a kicked ass looks like!"
        scene bg atHome82c10ps with vpunch
        b "Ouch.."
        j "Ha-ha, not so tough now, huh ? Tell me who you are working for, ha-ha !"
        $ renpy.pause()
        scene bg atHome82c9ps with fade
        b "It is illegal! I want to call my lawyer!"
        j "No lawyer will help you ! Only sincere confession may ease your fate ! But even the confession doesn't change the fact that I kicked your ass again, like the good old days, ha-ha"
        $ renpy.pause()
        scene bg atHome82c7ps with fade
        j "Surrender, it is your last chance ! Ha-ha.."
        $ ep4JulieWon = 0
        $ ep4JulieShirtTold = 0
        menu:
            "Let Julie win":
                $ ep4JulieWon += 1
                scene bg atHome83c7ps with vpunch
                b "Okay, okay you got me !"
                j "Ha-ha, you probably forgot after all this time that fighting with me is pointless."
                $ renpy.pause()
                b "{i}Oops, looks like she didn't notice that the shirt slipped down.."
                b "{i}Should I tell her ?"
                scene bg atHome82c6ps with fade
                menu:
                    "Yes":
                        $ ep4JulieShirtTold += 1
                        b "Ahm Julie, I understand that you won but shouldn't your breasts remain covered even after winning ?"
                        j "What ? Ha-ha"
                        scene bg atHome84c6ps with dissolve
                        j "Oops! Yeah you are right, that is too much even for a winner.."
                        "{b}{i}*PHONE RINGS*{/i}{/b}"
                        b "Ok Julie, let me get up. I need to answer the call.."
                        scene bg atHome85c11ps with fade
                        $ renpy.pause()
                        c "Bring the package to the warehouse again. You have only 30 minutes, so don't get late. Any questions later. {i}{b}*End of the call*{/b}{/i}"
                        b "..."
                        scene bg atHome86c12ps with fade
                        $ renpy.pause()
                        b "I'm sorry Julie, but I need to go."
                        j "What..? Why..?"
                        b "It's my work. Go to sleep baby, it's already late."
                        j "But I don't want to ! We are just started having fun.."
                        b "I'm sorry but I can't stay."
                        j "No.. Don't go.."
                        b "I have no choice."
                        j "Let me at least give you a hug before you go.."
                        scene bg atHome87c13ps with fade
                        $ renpy.pause()
                        j "When will you come back..?"
                        b "Don't worry, little one. Go to sleep and the next time you wake up I will probably be back."
                        j "Promise..?"
                        b "I..I hope that I'll be back by that time."
                        play sound ("music/sounds/kiss.mp3")
                        scene bg atHome89c16ps with kissFlash
                        scene bg atHome87c13ps with fade
                        j "Come back soon, okay..?"
                        b "I'll try, Julie."
                        scene bg atHome88c14ps with fade
                        j "Be careful, [bro].."
                        b "Sweet dreams, baby."
                        jump ep4street
                    "No":
                        b "..."
                        j "Ha-ha..I've been missing this, [bro].."
                        j "How long have we not been fooling around like that ?"
                        b "Like 5 years, maybe more.."
                        j "Right..Ha-ha.."
                        $ renpy.pause()
                        j "What..what are you looking at ?"
                        b "Nothing!"
                        scene bg atHome84c6ps with dissolve
                        j "Oops..It has been long time indeed. Back then I didn't have these, ha-ha.."
                        "{b}{i}*PHONE RINGS*{/i}{/b}"
                        b "Ok, Julie, I need to answer the call.."
                        scene bg atHome85c11ps with fade
                        $ renpy.pause()
                        c "Bring the package to the warehouse again. You have only 30 minutes, so don't get late. Any questions later. {i}{b}*End of the call*{/b}{/i}"
                        b "..."
                        scene bg atHome86c12ps with fade
                        $ renpy.pause()
                        b "I'm sorry Julie, but I need to go."
                        j "What..? Why..?"
                        b "It's my work. Go to sleep baby, it's already late."
                        j "But I don't want to ! We are just started having fun.."
                        b "I'm sorry but I can't stay."
                        j "Okay.. Let me at least give you a hug.."
                        scene bg atHome87c13ps with fade
                        $ renpy.pause()
                        b "Good night and sweet dreams, Julie."
                        j "Be careful, [bro].."
                        jump ep4street
            "Overpower her":
                scene bg atHome90c11ps with vpunch
                j "Ouch !"
                b "Nah, that is not going to happen, Julie.."
                j "[bro]..You are hurting me.."
                scene bg atHome90c13ps with vpunch
                b "You do realize that I can win using only one hand, don't you..?"
                j "Ah..I thought we are just fooling around, but looks like you are taking it too serious.."
                scene bg atHome90c14ps with fade
                $ renpy.pause()
                b "So whose ass is kicked now, huh ?"
                j "Okay, you won.. Let me go now.."
                b "You forgot something.."
                j "Please..? Please let me go, [bro].."
                b "Actually that is not all, I want you to admit your defeat by giving me a kiss.."
                scene bg atHome91c14ps with dissolve
                $ renpy.pause()
                j "W-what..? You can't be serious.."
                b "I'm absolutely serious.. I just want you to learn the lesson about who's in charge here.."
                scene bg atHome90c14ps with dissolve
                j "Now you are starting to scare me, [bro]..."
                b "..."
                "{b}{i}*PHONE RINGS*{/i}{/b}"
                b "Relax, Julie..You should have seen the look on your face, ha-ha.."
                menu:
                    "Answer the call":
                        scene bg atHome86c12ps with fade
                c "Bring the package to the warehouse again. You have only 30 minutes, so don't get late. Any questions later. {i}{b}*End of the call*{/b}{/i}"
                b "I have to go, Julie."
                j "Okay.."
                b "Good night."
                j "..."
                jump ep4street
        $ renpy.pause()
        return

    label ep4street:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Birkaç dakika sonra...")
        $ renpy.pause()
        $ renpy.music.set_volume(0.25, delay=0, channel=1)
        $ renpy.music.play("music/drivingTheme.mp3", channel=1, loop=True)
        play sound ("music/sounds/carDrive1.mp3")
        scene bg streets1c5ps with dissolve
        $ renpy.pause()
        b "{i}I need to hurry up, the warehouse is at the other side of the city.."
        b "{i}It will be fucking hard to get there in 30 minutes, usually they inform me about such things one hour before.."
        b "{i}I wonder why they decided to change it."
        b "{i}Maybe the decision to inform as late as possible was made in order to avoid information spread among other members of the gang."
        scene bg streets0c4ps with fade
        play sound ("music/sounds/carDrive2.mp3")
        b "{i}But that leads to the conclusion that someone else will be at the warehouse except me. What if there will be someone who is snitch..? What if this is just a trap..?"
        b "{i}Shit, all this stuff looks very suspicious.."
        b "{i}Anyway, I will get the answers very soon.. Better keep my gun loaded.."
        menu:
            "Full throttle":
                scene bg streets2c7ps with fade
        play sound ("music/sounds/carDrive1.mp3")
        b "{i}At least the road is empty, the city is asleep.."
        b "{i}So far so good, I will get in time to the place if nothing bad happens.."
        menu:
            "Speed up":
                $ renpy.music.set_volume(1.0, delay=0, channel=3)
                $ renpy.music.play("music/sounds/policeSiren.mp3", channel=3, loop=True)
        play sound ("music/sounds/carDrive3.mp3")
        scene bg streets3c7ps with dissolve
        $ renpy.pause()
        b "{i}Shit Shit Shit !!!"
        b "{i}I knew there is nothing good in a rush !"
        define police = Character("Officer", color="#0000CD")
        police "Pull over, now !"
        b "{i}I doubt I can get away from them. It will only draw more police patrols and I don't want extra attention."
        $ renpy.music.stop(channel=3, fadeout=5.0)
        b "{i}Fuck, it seems like I don't have any other choice, I have to stop the car.."
        scene bg streets4c2ps with fade
        play sound ("music/sounds/carDoorClose.mp3")
        $ renpy.music.play("music/sounds/engineWorking.mp3", channel=3, loop=True)
        b "{i}Damn, they hold their hands on the guns, I'd better hide mine before they notice it.. Shooting is not an option in this situation.."
        b "{i}I need to calm down and play it cool.. Hopefully they just give me the ticket and let me go.."
        menu:
            "Roll down the window":
                play sound ("music/sounds/rollDownWindow.mp3")
        $ renpy.music.set_volume(1.5, delay=0, channel=3)
        $ renpy.music.play("music/sounds/engineWorking.mp3", channel=3, loop=True)
        scene bg streets6c1ps_ with Fade (1.5, 1.5, 1.5, color='#000000')
        police "Good night, Sir"
        b "Greetings.. May I ask why am I being stopped, officer..?"
        police "You ignored the demand of stop sign and were driving far above existing speed limit."
        b "Did I..?"
        scene bg streets6c1ps with dissolve
        police "May I see your driver's license and registration please."
        b "Sure, let me just take it out from my pocket.."
        police "Slowly please, no sudden movements."
        b "Here you go, officer.."
        scene bg streets5c1ps with dissolve
        police "..."
        scene bg streets6c1ps with dissolve
        police "Here are your documents Mr.[bro]."
        scene bg streets6c1ps_ with dissolve
        police "May I ask what is the reason of your rush ?"
        b "{i}Shit.. I need to come up with something really quick !"
        $ renpy.pause()
        b "Oh, you see my wife at the hospital gives birth right now, I want to support her and be there.."
        police "I understand, however it isn't an excuse for violating driving restrictions."
        b "You are absolutely right officer, I'm ready to pay the fine.."
        police "You wouldn't mind if I took a quick search of the vehicle would you ?"
        b "What for ?"
        police "This area is know by high traffic of weapon transportation. I have to check that you don't have anything illegal in your car."
        b "{i}Fuck.. If they open the trunk and see the package they will definitely want to know what is inside of it. But even I don't know what is there.."
        b "Officer, please. I explained you the situation, I'm in a hurry. Why don't you just write down the ticket for me and I will promise to drive without violation..?"
        police "Sir, please step out of the car and open the trunk. It won't take long, unless you're hiding something illegal of course."
        b "{i}I'm screwed.. Shit.. What should I do..?!"
        scene bg streets7c1ps with dissolve
        police "Sir, I won't ask you again! Please step out of the car and open the trunk, now!"
        b "Okay, officer. As you wish."
        menu:
            "Open the trunk":
                b "{i}This is the end.. As soon as I open the trunk and they see the suitcase they will put on handcuffs on me.."
                b "{i}Then they will find the gun in my car.. I don't have permission on it.. Fuck.."
                $ renpy.pause()
            "Get the gun":
                b "{i}If I reach for the gun really quick I might have a chance to shoot this officer first, but there is no way I could do the same to another one.."
                b "{i}He is doing his job.. And I'll just exchange my life on his.. It makes no sense"
                $ renpy.pause()
        play sound ("music/sounds/distantGunshots.mp3")
        scene bg streets8c1ps with dissolve
        "{i}{b}*distant gunshots*{/b}{/i}"
        $ renpy.pause()
        b ".."
        police ".."
        play sound ("music/sounds/distantGunshots.mp3")
        define police2 = Character ("Officer 2", color = "#0000CD")
        police2 "Did you hear it ?"
        police "Yes"
        "{i}{b}Radio:{/b}{/i}\nAll units, we have an information about the gunshots near old concrete factory. Please respond, over."
        police2 "It's only few blocks away from here"
        scene bg streets9c1ps with dissolve
        police "I know, get in the car. You'll drive."
        police2 "Got it"
        scene bg streets8c1ps_ with dissolve
        police "Dispatcher, this is unit 36 we are on our way to the factory. Estimated time of arrival is 3 minutes, over."
        "{i}{b}Radio:{/b}{/i}\nRoger that, unit 36"
        "{i}{b}Radio:{/b}{/i}\nThis is unit 27, we will cover you, 36. Contact in 7 minutes, over."
        scene bg streets6c1ps_ with dissolve
        b "What should I do officer..?"
        police "You could go to your wife, Sir. Just drive safely from now on. Good night."
        b "Thank You.."
        $ renpy.music.stop(channel=3, fadeout=3.0)
        $ renpy.music.stop(channel=1, fadeout=5.0)
        jump ep4warehouse
        return

    screen ep4warehouseScr:
        imagemap:
            ground "images/ep4/m5c4ps.png"
            hotspot (1350,432,154,172) clicked Return("PC") hovered ShowTransient("imgHider", img="images/ep4/m5c4ps_.png") unhovered Hide("imgHider")

    label ep4warehouse:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra depoda...")
        $ renpy.pause()
        b "{i}Shit, that was so fucking close.. A good reminder for what this work is all about.."
        b "{i}But I'm 5 minutes late.. I need to call them and tell that I'm at the place.. "
        menu:
            "Enter the warehouse":
                scene bg m6c7ps with Dissolve (1.0)
        b "Yes, that is me. I know I'm late.. Had to deal with the police.."
        c "Did you bring the package ?"
        b "Wait a second.."
        menu:
            "Come closer":
                $ renpy.music.set_volume(0.75, delay=0, channel=3)
                $ renpy.music.play("music/warehouseTheme.mp3", channel=3, loop=True)
        scene bg m6c9ps with fade
        b "What the fuck ?!"
        scene bg m7c11ps with vpunch
        c "What's the matter ?!"
        b "Looks like they are dead!"
        c "What is going on over there ?!"
        b "I don't know, I can't see shit from here !"
        c "Listen to me, [bro]. I need you to give me a clear picture about the situation. You were supposed to meet with Bob, Mikey and Antonio at the warehouse."
        b "I see two bodies on the floor. I need to take a closer look."
        c "Be careful, there are still might be hostile folks"
        menu:
            "Come down":
                scene black with dissolve
        c "Report"
        b "Oh my god.. It's.. It's Bob and Mikey.. "
        c "How are they..?"
        b "They are dead.."
        scene bg m8c10ps with Dissolve(1.5)
        c "Are you sure..?"
        b "They do not breathe.."
        scene black with Dissolve (1.5)
        c "Shit.. What about Antonio.. ?"
        b "I don't see him"
        c "Okay here is what I want you to do. We probably don't have much time, so try to find any clues about what happened here. If I were you I would start from the office, the warehouse has dozen of security cameras throughout the perimeter. But first make sure that you are alone over there."
        b "Got it"
        scene bg m5c4ps with fade
        b "I'm in the office, the warehouse is empty."
        c "Good. Is the package with you ?"
        b "Yeah, why ?"
        c "Just always keep your eyes on it. The package is the priority number one."
        b "What is so important about it ?"
        c "We'll talk about it later. Now you need to gain access to the cameras. Whoever killed the guys, either turned cameras off or left them working, which means that you are caught on a footage and now you need to delete it."
        b "Right, there is a computer over here. Let's see what I can do."
        c "Call me back when you are done. {b}{i}End of the call{/i}{/b}"
        call screen ep4warehouseScr
        scene bg m9c7ps with fade
        $ renpy.pause()
        b "{i}Shit.. The computer is locked.. I need the password.."
        menu ep4password:
            "Enter the password":
                $ password = renpy.input("Lütfen şifreyi girip 'Enter' tuşuna basın.")
                $ password = password.strip()
                $ password = password.lower()
                if password == "cw":
                    jump ep4warehouse2
                else:
                    "Wrong Password. Try again."
                    jump ep4password
            "Remind the password":
                "{i}Corrins Lwilson{/i}"
                b "{i}The company name..?"
                b "{i}Hm.."
                jump ep4password
        $ renpy.pause()
        return

    label ep4warehouse2:
        "{i}{color=#00FF00}Access Granted{/color}{/i}"
        b "{i}Here we go"
        b "{i}Now I need to find the video from security cameras.."
        menu ep4Computer:
            "Reports":
                b "{i}It looks like a financial information regarding company's revenues and expenses.."
                jump ep4Computer
            "Supplies":
                b "{i}It is info about dates, quantity and size of upcoming goods deliveries from suppliers.."
                jump ep4Computer
            "Security":
                b "{i}That's exactly what I need.."
                menu:
                    "Cameras status":
                        "CAM_01 is {color=#FF0000}Offline{/color}, CAM_02 is {color=#FF0000}Offline{/color}, CAM_03 is {color=#FF0000}Offline{/color}, \nCAM_04 is {color=#FF0000}Offline{/color}, CAM_05 is {color=#00FF00}Online{/color}, CAM_06 is {color=#FF0000}Offline{/color}, \nCAM_07 is {color=#FF0000}Offline{/color}, CAM_08 is {color=#00FF00}Online{/color}, CAM_09 is {color=#FF0000}Offline{/color}."
        b "{i}Okay let's rewind the video at the time I supposed to be here initially. It would've been around 01:30 AM if cops hadn't stopped me.."
        b "{i}Damn, it's a footage with an interval of 15 seconds, I expected to view the video record.."
        b "{i}Well, I guess it's better than nothing at all.."
        menu:
            "Watch the record":
                scene bg m10c5ps with fade
        b "{i}Okay here is Bob and Mikey.. Alive.."
        b "{i}There is no sign of Antonio, though.."
        b "{i}Let's see what happened next.."
        scene bg m11c5ps with fade
        b "{i}What is it..? Some guy entered the warehouse.. Alone .. ?"
        b "{i}It's not Antonio.. That is strange.."
        b "{i}Looks like Bob and Mikey noticed him but they didn't react anyhow.."
        b "{i}Maybe they knew him..?"
        scene bg m12c5ps with fade
        b "{i}What is going on over there.. Where is the rest of the enemies..? I didn't notice any signs of a gunfire, which means that there must be someone else who attacked Bob and Mikey from behind or.. I don't know.."
        b "{i}There is no chance this guy alone could beat them both at the same time.. Bob and Mikey were the best fighters in our gang.."
        scene bg m12_c5ps with fade
        b "{i}..."
        b "{i}That is.. That is impossible.."
        b "{i}It's just 15 seconds.. I can't believe it.."
        b "{i}He probably had a knife or some other kind of hidden weapon.. But I didn't notice any stab wounds either.. What the hell happened there ?!"
        b "{i}Maybe I can get a better look from another camera..?"
        menu:
            "Switch camera":
                scene bg m13c8ps with fade
        b "{i}Wait a second.. This face looks familiar to me.."
        b "{i}Let's zoom in the image a bit.. Here we go.."
        scene bg m13c9ps with dissolve
        b "{i}I've seen this guy before with Antonio.. At this very warehouse.. Shit.. That who is a snitch.. Now I see the whole picture.."
        b "{i}It's time to call and tell them what I've found out."
        scene bg m9c7_ps with fade
        b "That is me.. I found out what happened here."
        c "Report"
        b "It was a trap, looks like that Antonio sold us out. I didn't see him on the video. It all happened in less than 2 minutes. There was only one guy. It's hard to believe but he has no weapon, at least it wasn't a gun."
        c "How did this guy look like..?"
        b "Bald, tall, solid. I would say there was nothing special about him except.."
        b "He alone beat both Bob and Mikey, it all happened in a blink of an eye"
        b "There is no signs of a gunfire, so it was just a fistfight ?! It doesn't make any sense.. I mean, how is that.."
        c "Shit.. Looks like they outpaced us.."
        b "What are you talking about ?"
        c "Listen to me, make sure that you delete the video record from the cameras and get the hell out of there. Then make anonymous call to the police and tell them about dead bodies at the warehouse.. At this point cops actually might be more usefull with the investigation."
        c "But the most important thing is the suitcase. It must not fall into the wrong hands, understand ? Protect it by any cost !"
        b "Oh for fucks sake, what the hell is in this suitcase ?!"
        c "I can't tell you this information.."
        scene bg m9_c7ps with vpunch
        b "Bullshit! Of course you can!"
        b "Listen, I understand that it's my job to risk and deal with any kind of illegal and serious shit. But here is the thing. At first the cops almost got me because I was rushing here like a crazy delivering your fucking package."
        b "Then I discover two dead bodies killed almost instantly by a guy with his bare hands. I think he wouldn't mind to take the suitcase from my dead body as well if I wasn't late !"
        b "And what a great news you are telling me ! All you can say is 'I won't tell you what's inside, but keep your eyes on the package and protect it by any cost...'"
        scene bg m9_c7ps with vpunch
        b "Screw this shit!"
        b "I think it's just a bit fucking impolite saying to me 'I can't tell you this information'! I could already be dead and your fucking package would've been lost for you. Oh, and you know the thing is that there is at least one more man who knew about this meeting, it is {b}You{/b}!"
        b "If you don't trust me, why should I trust you ?"
        c "Okay, [bro]. I'll tell you what's inside, but please, get to the safe place first. I understand that you are tired and shocked right now. Go get some rest, it's all for today. I'll call you later. {i}{b}End of call{/b}{/i}"
        scene bg m9_c7ps with vpunch
        b "Fuck!"
        scene bg m9c7ps with dissolve
        b "{i}..."
        b "{i}I need to calm down.."
        b "{i}Delete the file, call the police and get the hell out of here"
        extend "."
        extend "."
        extend "."
        b "{i}Done.."
        b "{i}Shit, I need a drink.."
        $ renpy.music.stop(channel=3, fadeout=3.0)
        jump ep4Bar
        return

    label ep4Bar:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra barda...")
        $ renpy.pause()
        b "{i}Probably the best place to clear my head, relax and forget about all this shit.. Damn.."
        scene bg nBar1c1ps with Dissolve (1.5)
        b "{i}Whoa, what a surprise, that is Vicky over there.."
        menu:
            "Order a drink":
                scene black with dissolve
                b "Double whiskey with the bottle please.. I'll take it with me.."
                "{b}{i}Bartender:{/i}{/b}\nJust a moment.."
        scene bg nBar4c2_ps with dissolve
        b "Hi, Vicky. Working late, huh ?"
        v "Hi, [bro]. I didn't know that you drink alcohol. Are you that much of a drinker ?"
        b "Well, I figured out that today is a fucking good time to start.."
        scene bg nBar2c2ps with Dissolve (0.75)
        v "Ha-ha, just don't tell me that you are going to drive after that."
        b "Honestly, I don't fucking care right now.."
        b "By the way, where is everyone..?"
        scene bg nBar7c2ps with dissolve
        v "Yeah.. This place is dead tonight. Actually, I was going to leave but since you are here we could chit-chat a bit.. Usually I have at least someone buying me a drink by this time, but today it's like.."
        "{b}{i}Bartender:{/i}{/b}\nHere is your drink Sir, please.."
        b "I can't argue with that.. Usually I don't have that much shit happened as well.."
        scene bg nBar5c2_ps with dissolve
        v "Huh..? Is something wrong..?"
        scene bg nBar8c3ps with fade
        b "Everything is wrong.."
        b "Shit.."
        menu:
            "Drink":
                scene bg nBar10c3ps with dissolve
                play sound ("music/sounds/swallowSound.mp3")
        scene bg nBar9c3ps with dissolve
        b "Damn.."
        scene bg nBar5c2_ps with fade
        v "What happened, [bro]..?"
        b "It's everything.. It's me and you, and my work, and..Julie.."
        scene bg nBar5c2ps with dissolve
        v "Is she okay ?"
        b "..."
        scene bg nBar6c1ps with fade
        b "Yes, she is fine.. It's just.. Listen we can't pretend that we are a couple we had to stop seeing each other. And also I want to ask you forget about this 'friendship' with Julie.."
        b "At least for now.. I need to figure out what is going on.."
        scene bg nBar3c2ps with fade
        v "I don't understand, but.. If you say so.."
        $ ep4VickyTold = 0
        menu:
            "Tell her":
                $ ep4VickyTold += 1
                if ep4VickyTold == 1:
                    b "Do you remember I told you what my work is all about..?"
                b "30 minutes ago I found two dead bodies at the warehouse.."
                scene bg nBar5c2_ps with dissolve
                scene black with Dissolve (2.0)
                $ renpy.notify ("Birkaç dakika sonra...")
                $ renpy.pause()
                scene bg nBar3c2ps with fade
                v "Oh my god.."
                b "Yeah.. And believe it or not but I've never killed anyone before. Nonetheless I suspect that soon I will have to.. There be whole a lot of deaths throughout the city because of this war.."
                b "The only thing I care about is my [family].. I always wanted them to stay out of my reckless life, not in the middle.."
                b "I don't know what could happen.. That is my biggest concern.."
            "Don't tell her":
                b "Yeah, just believe me that things are very hard for me right now.."
                v "I see.."
        v "..."
        scene bg nBar5c2_ps with dissolve
        v "You look so anxious and exhausted.. I've never seen you like that.. I can't imagine what you are going through right now.. Bad things tend to happen, but.."
        b "Yeah, whatever.. I'll probably just go home, I need to deal with this bottle.."
        scene bg nBar4c2ps with dissolve
        v "Hey.. I have a better idea.."
        v "I think I have something that might cheer you up a bit.. Let's go, follow me, we'll use the back door.."
        b "Okay.."
        jump ep4alley
        return

    label ep4alley:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Birkaç dakika sonra...")
        $ renpy.pause()
        scene bg streets10c4ps with fade
        b "What are you up to, Vicky ? Why use the back door ?"
        v "Relax, [bro]. It's a surprise.."
        b "Recently I learned that I do not like surprises"
        b "{i}Damn, what do I really know about her ? What if she is not what she says she is ? She could easily be one of them.."
        b "{i}Am I exaggerating things ? But for the other hand who can I trust after what happened ?!"
        scene bg streets11c6ps with fade
        v "What's the matter, [bro]..? You seem a little nervous. Don't you trust me anymore ?"
        b "Honestly ?"
        scene bg streets11c7ps with fade
        b "I don't know what to say.."
        v "The other day you said that you trust me more than anyone in this city, didn't you ?"
        b "I did, but the issue of trust becomes more serious. Don't take it personally, Vicky."
        scene bg streets11c8ps with fade
        v "You can't live like that trusting no one. It will become a paranoia. You need to have at least someone you could talk to"
        b "Let's  pretend that you are this someone.. There is nothing you could help me with anyway.."
        v "You are wrong.. I have a lot of connections with people whose word is not the last in the city.. I could at least provide you some useful information.."
        b "Why do you give a damn, Vicky.. It's not your problems anyway.."
        if ep4VickyTold == 1:
            v "It's simple, if things really that bad, then sooner or later it may concern escort business as well.. And as I remember you told that we are very much alike. I don't care that you are criminal because deep inside I see that you are a good guy and I just want to help.."
        else:
            v "I just want to help"
        v "Besides, if I had wanted any harm for you, I would already have done something.. I had plenty of time to do this.."
        scene bg streets12c10ps with fade
        b "It's just words.. How long do we need to go..?"
        scene bg streets12c11ps with fade
        v "Relax, we are almost there. Get ready for the fun part !"
        b "{i}What the.."
        scene bg streets13c10ps with hpunch
        scene bg streets14c8ps with hpunch
        b "What the hell, Vicky ?!"
        v "Hush, big guy.. Relax.. You still remember what I do for living, don't you ?"
        b "..."
        scene bg streets14c11ps with fade
        v "I just want to help you forget what happened today, that is all.."
        b "Vicky.. I told you that we had to stop doing this.."
        scene bg streets14c12ps with fade
        v "Do you want me to beg for it..? Please, [bro].. For the sake of old times.."
        v "There are still some money you paid me in advance for the service anyway it will be enough for the handjob.. I'm not used to be a debtor.."
        scene bg streets15c7ps with fade
        b "You don't have to do this, Vicky.."
        v "I want to.. Consider this as farewell gift.. Just warn me when you are about to cum, okay ?"
        b "Okay.."
        scene bg streets15c9ps with fade
        v "You see, I was hoping that today I'm gonna get fucked really hard.."
        scene bg streets16c9ps with dissolve
        b "You don't say.."
        v "I wanted it to be you who would be fucking me right now.. Because no one fucks me like you do.."
        scene bg streets15_c7ps with fade
        v "I'm so horny right now.. What about you, [bro]..? Is your cock already hard for me ?"
        b "Check for yourself, naughty girl"
        v "Ha-ha, give it to me"
        play sound ("music/sounds/jeansZipper.mp3")
        scene bg streets18_c15ps with fade
        v "Yes.. As always rock hard.. Hot and throbbing.."
        v "I'm gonna miss this huge thick cock of yours.."
        b "Shit.."
        scene bg streets18_1c14ps with fade
        $ renpy.pause()
        v "Fuck, just look at how big this cock is.."
        scene bg streets18_c14ps with dissolve
        v "Too bad you didn't fuck my ass with your cock.. I would like you be the first who will shove his cock in my tight little butthole.."
        b "Yeah.."
        scene bg streets18_1c14ps with Dissolve(0.75)
        scene bg streets18_c14ps with Dissolve(0.75)
        scene bg streets19c13_ps with fade
        v "I want you to have it your way with me when you'll be fucking my ass.."
        b "Really..?"
        scene bg streets19c13ps with dissolve
        v "Yes.. I will probably be screaming from the pain because of the size of your cock.."
        b "I'm sure you will.."
        scene bg streets20c13ps with dissolve
        show ep4hj
        v "I'll be begging you to stop, but you won't.. You'll just shut my mouth with your hand and will start fucking me even harder and faster.."
        v "I would want you to pull my hair and slap my ass when you go balls deep.."
        b "Oh, Vicky.."
        v "And I would really like it.. Do you know why..? Because I'm just a slut and you can do with me whatever you want.."
        b "Fuuuuuck.."
        hide ep4hj
        scene bg streets17_c13ps with dissolve
        "{i}Vicky tightens the grip on the glans"
        b "Ah.."
        v "You can't imagine how bad I want this cock right now..The best cock that ever been inside of me.."
        b "Yeah..?"
        scene bg streets21c18ps with fade
        $ renpy.pause()
        v "I want your cock so bad, that I could even agree to do it without a condom.. I would go against all my principles.."
        v "Because true whore shouldn't have any.. I would greedily suck on your cock when you pull it out from my ass"
        scene bg streets22c16_ps with fade
        v "Do you like it when I glide my thumb along the frenulum ?"
        b "Fuck yes.."
        scene bg streets22c16ps with dissolve
        v "Ha-ha..It's written on your face that you're about to cum.."
        b "Not yet, baby.. Keep stroking it.."
        scene bg streets23c17ps with fade
        v "I would want to feel it throbbing inside my warm slutty mouth when you will be cumming.."
        scene bg streets23_c17_ps with dissolve
        v "You could grab my head with your hands and shove it deeper in my mouth with each stroke until I gag and can't breathe.."
        scene bg streets23c17ps with dissolve
        v "My mascara would go messy because of tears.. Just imagine the look on my face when you blow your load right down in my throat.. I couldn't breathe until I swallow every single drop of your hot cum.."
        b "Vicky.. Fuck.."
        v "You'd love it, wouldn't you..?"
        scene bg streets23_c17__ps with dissolve
        v "Whoa, here is the precum.. I wonder what it tastes like.."
        $ renpy.pause()
        scene bg streets23_c17ps with dissolve
        v "You know, I also wouldn't mind if you would cum on my pretty face.."
        scene bg streets23_c17__ps with dissolve
        v "Actually I like that kind of men.. It shows their dominance over me.."
        scene bg streets23_c17ps with dissolve
        v "And I want to be submissive little slut for my master.."
        b "Oh, fuck Vicky.."
        scene bg streets23_c17__ps with dissolve
        v "The highest reward for me is when my master smears the cum over my face with his dick.. I could even climax from that.."
        v "Because that reminds me who I really am - just a fucking dirty whore.."
        b "{i}Fuck I'm about to cum. Should I warn her ?"
        $ ep4VickyWarned = 0
        menu:
            "???":
                b "Argh !!! You did it, slut ! Take it on your pretty face !"
                scene black with dissolve
                v "What..? Wait !!!"
                b "AAAAAAAAAAAAAAAARGH !!!"
                scene black with cumFlash
                scene black with cumFlash
                scene black with cumFlashLong
                v "What the Fuck, [bro] ?!"
                scene bg streets27c16ps with Dissolve (1.5)
                b "Shit, that was intense.."
                v "Are you out of your fucking mind ?! Why did you do that ?!"
                b "What are you talking about ? Isn't that what you wanted ?"
                v "I was talking dirty to help you get off, you had to warn me !!! How am I supposed to..work the rest of the night like this ?!"
                b "Come on, Vicky. The place is dead anyway.. I thought you were going home"
                v "Fuck you, [bro] ! Don't you dare to call me, understand ?!"
                b "Whatever.."
                $ renpy.pause()
                jump ep4ending
            "???":
                b "Give your slutty mouth to me !"
                scene bg streets28c17ps with hpunch
                v "{i}Mmmpff ?!?!?!?"
                b "That's right, bitch ! Wrap your lips around my cock and take it like a good girl !"
                scene bg streets29c17ps with hpunch
                scene bg streets29c17ps with hpunch
                v "{i}Mmmmghh..."
                scene bg streets29c17ps with hpunch
                b "Aaaaaaaargh ! Yes ! Right down in the throat, fuck !"
                scene bg streets29c17ps with hpunch
                v "mmmmghh....."
                scene bg streets29c17ps with hpunch
                scene bg streets29c17ps with cumFlash
                scene bg streets29_c17ps with cumFlashLong
                b "FUUUUUUUUUUUUUUUCK !!!"
                play sound ("music/sounds/swallowSound.mp3")
                v "{i}gulp..."
                $ renpy.pause()
                scene black with Dissolve(1.0)
                b "Oh yes, baby. That was awesome !"
                v "{i}Cough-cough.."
                v "Why did you do that..? You had to warn me, [bro].."
                scene bg streets27_c16ps with Dissolve (1.5)
                b "What are you talking about..? Isn't that what you wanted..?"
                v "I didn't expect this from you [bro].. That is meanly. Ater all that I did for you, you treat me like a shit, I didn't deserve that.."
                b "Ahm, okay.. I'm sorry, I guess.."
                v "I don't want to talk with you anymore, goodbye.."
                $ renpy.pause()
                jump ep4ending
            "Warn her":
                $ ep4VickyWarned += 1
                b "Fuck Vicky, I am about to cum !"
                scene bg streets24c16ps with fade
                v "Okay, thanks for letting me know.."
                b "Almost there !"
                scene bg streets18_1c14ps with fade
                scene bg streets18_c14ps with dissolve
                b "Aaargh ! I'm comming !!!"
                v "Cum for me, [bro]. I want it so bad !"
                scene bg streets18_c14ps with cumFlash
                scene bg streets18_c14ps with cumFlash
                scene bg streets18c14psCum with cumFlashLong
                b "Fuuuuuuuuuuuuuck !!!"
                v "Oh my.. It's so much cum.."
                scene bg streets17c13ps with fade
                v "You always cum so hard.. Honestly it kind of turns me on.."
                b "Damn, Vicky, you are the best in such things.."
                play sound ("music/sounds/kiss.mp3")
                scene bg streets26c16ps with kissFlash
                scene bg streets25c15ps with fade
                b "Wow.. What was that ?"
                v "Well, you did ask for the kiss, didn't you ?"
                b "I thought you are serious about doing such things with the clients.."
                v "I guess I'm willing to make an exception for my favourite one.. Just.. Don't forget about me, okay ? If you ever need something feel free to call me, deal ?"
                b "Deal.. Do you want me to drive you home..?"
                v "No, I live nearby so thanks.."
                v "Good night, [bro].."
                $ renpy.pause()
                jump ep4ending
        $ renpy.pause()
        return

    label ep4ending:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra evde...")
        $ renpy.pause()
        scene bg atHome92c2ps with dissolve
        b "{i}Better keep the package nearby.. I wonder what is inside of it. I mean it {b}must{/b} be something valualbe.."
        b "{i}They told me to expect the call, but what if there will be no call.. Damn, considering the size of the package it could easily be a bomb! And I brought it right in my house.."
        scene bg atHome93c1ps with fade
        b "{i}Fuck it, I'll try to open the suitcase. At least I need to try.."
        menu:
            "Try to open":
                play sound ("music/sounds/click.mp3")
        scene bg atHome93c1_ps with dissolve
        b "{i}That was pretty easy.. Hm.. That pad in the middle looks like a fingerprint reader.."
        b "{i}And of course it won't accept my prints, that would be really easy. But I need to make sure"
        menu:
            "Scan":
                play sound ("music/sounds/errorSound.mp3")
        scene bg atHome94c1ps with dissolve
        b "{i}Well, the miracle did not happen as I expected. At least I tried."
        b "{i}Damn..What time is it ?! I should take the shower and call it a day."
        scene black with Dissolve (2.0)
        $ renpy.notify ("15 dakika sonra..")
        $ renpy.pause()
        scene bg atHome95c3ps with dissolve
        b "{i}Z-z-z..."
        $ renpy.music.set_volume(0.5, delay=0, channel=1)
        $ renpy.music.play("music/sounds/heartBeat.mp3", channel=1, loop=True, fadein=5)
        $ renpy.music.set_volume(0.75, delay=0, channel=3)
        $ renpy.music.play("music/nightmareTheme.mp3", channel=3, loop=True, fadein=5)
        scene black with Dissolve (2.0)
        play sound ("music/sounds/carDrive2.mp3")
        scene bg streets1c5psN with Dissolve(2.5)
        $ renpy.pause()
        $ renpy.music.set_volume(0.75, delay=0, channel=4)
        $ renpy.music.play("music/sounds/policeSiren.mp3", channel=4, loop=False, fadein=0)
        scene bg streets3c7psN with Dissolve(2.5)
        $ renpy.pause()
        $ renpy.music.stop(channel=4, fadeout=1.0)
        scene bg streets7c1psN with Dissolve(2.5)
        $ renpy.pause()
        play sound ("music/sounds/distantGunshots1.mp3")
        scene bg m6c9psN with cumFlashLong
        $ renpy.pause()
        play sound ("music/sounds/footsteps.mp3")
        scene bg m13c9ps with Dissolve(2.5)
        $ renpy.pause()
        play sound ("music/sounds/kneeKick.mp3")
        scene bg m13_c9ps with hpunch
        scene bg m13_c9ps with hpunch
        scene black with cumFlashLong
        $ renpy.music.stop(channel=1, fadeout=3.0)
        $ renpy.music.stop(channel=3, fadeout=3.0)
        $ renpy.pause()
        v "Calm down.."
        v "It's just a bad day.."
        $ renpy.music.set_volume(0.25, delay=0, channel=1)
        $ renpy.music.play("music/sexyTheme.mp3", channel=1, loop=True, fadein=15)
        scene bg dream1c2ps with Dissolve(2.0)
        $ renpy.pause()
        v "I know exactly what will help you to relax [bro].."
        v "That is good that you already hard for us.."
        b "Us..?"
        scene bg dream2c1ps with Dissolve(2.5)
        v "Yeah, today I've brought with me my student.."
        b "..."
        v "Come in, darling.. Don't be shy.."
        v "Your [brother] is waiting for you.."
        scene bg dream3c1ps with Dissolve(2.5)
        j "Hi, [bro]..."
        b "Julie ?!"
        scene bg dream3c3ps with Dissolve(2.5)
        j "I hope you don't mind if I join today's party, do you..?"
        b "..."
        v "Of course he doesn't, silly.. No man would say 'No' to you, Julie.."
        v "Make yourself comfortable and take a seat beside me.. Today I'm going to teach you an important lesson.."
        j "As you say, Vicky.."
        scene bg dream4c2ps with Dissolve(2.5)
        j "Oh my.. It's so big !"
        v "That's right, girl.. Whenever your mouth is empty always compliment his dick, say how bad you want it inside of you.."
        j "I don't know if I could take it.. It's so huge !"
        v "Good girl.. But you forgot about something.."
        j "Right ! That is my bra.. I need to take it off before giving a head unless I was told to keep it on, right..?"
        scene bg dream5c4ps with Dissolve(2.5)
        v "Exactly.."
        b "Oh fuck.."
        j "Honestly I'm a bit nervous, Vicky.. I've never had a chance to touch a cock before.. I'm not sure what to do.. But it turns me on so bad, I guess I'm getting wet.."
        v "Today you have a great opportunity to suck a real one, Julie.. Watch and learn.."
        scene bg dream6c4_ps with Dissolve(1.5)
        v "Always start with a little tease.. Don't try to wrap your mouth around the cock right away, there is no need to rush.. Use your tongue and watch the expression on his face.. It will tell you everything you need to know.."
        b "Oh yes.."
        scene bg dream6c4ps with dissolve
        j "Am I allowed to touch myself during blowjob..?"
        v "Sure thing, don't forget to play with yourself while you are sucking a cock.. Thus you are showing that you are horny and enjoy this as much as he does.."
        scene bg dream6c4_ps with dissolve
        j "I'm so horny right now.."
        scene bg dream7c4ps with dissolve
        v "Slide your tongue along the glans a bit, just show him how wet and warm your little mouth is.."
        scene bg dream6c4ps with dissolve
        $ renpy.pause()
        scene bg dream7c4ps with dissolve
        $ renpy.pause()
        scene bg dream6c4ps with dissolve
        b "Oh fuck.."
        scene bg dream8c2ps with Dissolve(2.5)
        v "Make sure to maintain the eye contact as much as possible, this shows that you are a good girl and adore to suck.."
        j "I am all wet right now, Vicky.."
        v "Me too, darling.. But now it's all about his pleasure, not ours.."
        v "After you've teased him with your tongue, slowly start to wrap your lips around the glans.. Give it a gentle kiss.."
        play sound ("music/sounds/kiss.mp3")
        scene bg dream8c2ps with kissFlash
        v "He will start begging you to put it in your mouth.."
        scene bg dream9c2_ps with dissolve
        j "Ah.."
        v "Hold a second.. Give him one last tease.."
        b "Oh fuck.."
        j "So hot.."
        scene bg dream9c2ps with dissolve
        v "And right before he asks to put it in, you do it gently and submissively. Take the cock like a good girl.."
        scene bg dream11c2ps with kissFlash
        v "{i}slurp..."
        j "Oh my god, Vicky ! There is a fire between my legs right now, I want to touch myself so bad.."
        b "FUCK!"
        scene bg dream11c2_ps with dissolve
        v "{i}slurp.."
        scene bg dream11c2ps with dissolve
        $ renpy.pause()
        scene bg dream11c2_ps with dissolve
        v "Mmmm..."
        scene bg dream9c2ps with dissolve
        v "{i}Mwah..{/i}This cock is so hard and throbbing.. I love the way it tastes.."
        b "Holy shit, Vicky.."
        j "Ah.."
        scene bg dream9c2_ps with dissolve
        v "I want you to know Julie, that there is something called \n{b}{i}Royal Blowjob"
        scene bg dream9c2ps with dissolve
        j "Sounds interesting.. What is this..?"
        v "It's when you gag on the cock, like you take it right down your throat as deep as you can.. "
        j "Wow.. I didn't know that it's even possible.."
        v "With the size of your [brother]'s cock it's really very hard.. But practice makes perfect, so train as much as possible.."
        scene bg dream9c2_ps with dissolve
        v "The highest skill is to lick the balls when the whole shaft is throbbing inside of you.."
        j "Oh, fuck.. I already want to try it !"
        b "Oh yeah.."
        scene bg dream11c2ps_2 with Dissolve(1.0)
        scene bg dream11c2ps_1 with Dissolve(1.0)
        scene bg dream11c2ps_2 with Dissolve(1.0)
        scene bg dream11c2ps with Dissolve(1.0)
        scene bg dream11c2ps_2 with Dissolve(1.0)
        scene bg dream11c2ps_1 with Dissolve(1.0)
        scene bg dream11c2ps_2 with Dissolve(1.0)
        scene bg dream11c2ps with Dissolve(1.0)
        b "Oh fuck, girls.. I'm about to cum soon.."
        j "Mmmm.. I want this cock so bad.."
        v "{i}slurp..slurp.."
        scene bg dream11c2ps_2 with Dissolve(1.0)
        scene bg dream11c2ps_1 with Dissolve(1.0)
        scene bg dream11c2ps_2 with Dissolve(1.0)
        scene bg dream11c2ps with Dissolve(1.0)
        scene bg dream11c2ps_2 with Dissolve(1.0)
        scene bg dream11c2ps with cumFlash
        scene bg dream11c2ps_2 with cumFlash
        scene bg dream11c2ps_1 with cumFlash
        scene bg dream12c6ps with cumFlashLong
        scene bg dream12c6ps with vpunch
        scene bg dream12c6ps with vpunch
        scene bg dream12c6ps with vpunch
        b "Aaaaargh !!! Fuuuuuuuck !!!"
        scene bg dream13c1_ps with Dissolve(2.5)
        j "Oh my god, Vicky.. Did [bro] just came in your mouth ?!"
        v "Yaeh.. Aaa.. Fee for youelf, arling.."
        b "Fuck, baby.."
        scene bg dream13c1ps with dissolve
        v "Auways fhow ow auch u ike it uhen he caymes in you outh.."
        j "[bro], will you come in my mouth as well..?"
        b "Oh, Julie.."
        play sound ("music/sounds/swallowSound.mp3")
        scene bg dream14c1ps with dissolve
        j "Did you just.. Swallow all of it..?"
        scene bg dream15c1ps with Dissolve(1.0)
        v "Mwaaah.. Of course, darling.. You have to be really careful, Julie.. You don't want to spill any single drop of your [brother]'s precious hot cum, do you..?"
        j "Do I always have to swallow..?"
        scene bg dream16c1_ps with dissolve
        v "Of course you do, Julie.. You want to be a good girl, don't you ?"
        j "Yes.."
        v "Good girls {b}always{/b} swallow, darling.."
        v "So.. What do you think.. Are you ready to suck this cock now..?"
        scene bg dream16c1ps with dissolve
        j "I guess I am, Vicky.."
        v "Then get down on your knees and show your [brother] how much you love him.."
        j "Okay.."
        b "Oh my.."
        scene bg dream16c1_1ps with dissolve
        v "Get ready for round 2, [bro]..."
        $ renpy.pause()
        $ renpy.music.stop(channel=1, fadeout=5.0)
        "{b}{i}PHONE RINGING"
        scene black with Dissolve(2.5)
        $ renpy.pause()
        scene bg atHome95c3ps_ with Dissolve(2.5)
        "{b}{i}PHONE RINGING"
        scene bg atHome95_c3ps with dissolve
        b "{i}What the hell.."
        menu:
            "Answer the call":
                scene bg atHome96c3ps with dissolve
        c "Are you safe ?"
        b "Yeah, I'm at home.."
        c "Is the package still with you ?"
        b "Of course it is. Are you going to tell me what's inside or not ?"
        c "I've tracked that you tried to open it with your fingerprint"
        b "Yeah, so what ? It didn't accept my prints, I don't have access anyway.."
        c "Actually you are the only one who has it.."
        scene bg atHome96_c3ps with dissolve
        b "What ?!"
        c "You just need to combine your prints with the right sequence"
        c "Try it now"
        menu:
            "Open the suitcase":
                scene bg atHome97c3ps with Dissolve(2.5)
        c "How does it look, [bro] ?"
        b "What the hell is this stuff..?!"
        jump episode5
        return

####################################################EPISODE_5##################################################

    image bg atHome98c4ps = "images/ep5/atHome98c4ps.png"
    image bg atHome99c4ps = "images/ep5/atHome99c4ps.png"
    image bg atHome100c4ps = "images/ep5/atHome100c4ps.png"
    image bg atHome101c4ps = "images/ep5/atHome101c4ps.png"
    image bg atHome102c4ps = "images/ep5/atHome102c4ps.png"
    image bg atHome103c1ps = "images/ep5/atHome103c1ps.png"
    image bg atHome103c6ps = "images/ep5/atHome103c6ps.png"
    image bg atHome104c5ps = "images/ep5/atHome104c5ps.png"
    image bg atHome105c7ps = "images/ep5/atHome105c7ps.png"
    image bg atHome105c8ps = "images/ep5/atHome105c8ps.png"
    image bg atHome106c7ps = "images/ep5/atHome106c7ps.png"
    image bg atHome107c9ps = "images/ep5/atHome107c9ps.png"
    image bg atHome108c9ps = "images/ep5/atHome108c9ps.png"
    image bg atHome109_c8ps = "images/ep5/atHome109_c8ps.png"
    image bg atHome109c8ps = "images/ep5/atHome109c8ps.png"
    image bg atHome110c9ps = "images/ep5/atHome110c9ps.png"
    image bg atHome110c10ps = "images/ep5/atHome110c10ps.png"
    image bg atHome110c11ps = "images/ep5/atHome110c11ps.png"
    image bg atHome111c12ps = "images/ep5/atHome111c12ps.png"
    image bg atHome111c13ps = "images/ep5/atHome111c13ps.png"
    image bg atHome111c15ps = "images/ep5/atHome111c15ps.png"
    image bg atHome112c1ps = "images/ep5/atHome112c1ps.png"
    image bg atHome113c1ps = "images/ep5/atHome113c1ps.png"
    image bg atHome114c3ps = "images/ep5/atHome114c3ps.png"
    image bg atHome115_c3ps = "images/ep5/atHome115_c3ps.png"
    image bg atHome115c3ps = "images/ep5/atHome115c3ps.png"
    image bg atHome116_c2ps = "images/ep5/atHome116_c2ps.png"
    image bg atHome116c2ps = "images/ep5/atHome116c2ps.png"
    image bg atHome117_c4ps = "images/ep5/atHome117_c4ps.png"
    image bg atHome117c4ps = "images/ep5/atHome117c4ps.png"
    image bg atHome118_c5ps = "images/ep5/atHome118_c5ps.png"
    image bg atHome118_c6ps = "images/ep5/atHome118_c6ps.png"
    image bg atHome118c6ps = "images/ep5/atHome118c6ps.png"
    image bg atHome119c5ps = "images/ep5/atHome119c5ps.png"
    image bg atHome120c8ps = "images/ep5/atHome120c8ps.png"
    image bg atHome121_c8ps = "images/ep5/atHome121_c8ps.png"
    image bg atHome121c8ps = "images/ep5/atHome121c8ps.png"
    image bg atHome122c6ps = "images/ep5/atHome122c6ps.png"
    image bg atHome123c6ps = "images/ep5/atHome123c6ps.png"
    image bg atHome124_c6ps = "images/ep5/atHome124_c6ps.png"
    image bg atHome124c6ps = "images/ep5/atHome124c6ps.png"
    image bg atHome125c7ps = "images/ep5/atHome125c7ps.png"
    image bg atHome126c5ps = "images/ep5/atHome126c5ps.png"
    image bg atHome126c9ps = "images/ep5/atHome126c9ps.png"
    image bg atHome127c2ps = "images/ep5/atHome127c2ps.png"
    image bg atHome127c4ps = "images/ep5/atHome127c4ps.png"
    image bg atHome128c3ps = "images/ep5/atHome128c3ps.png"
    image bg atHome129c5ps = "images/ep5/atHome129c5ps.png"
    image bg atHome130_c6ps = "images/ep5/atHome130_c6ps.png"
    image bg atHome130c6ps = "images/ep5/atHome130c6ps.png"
    image bg atHome131c7_ps = "images/ep5/atHome131c7_ps.png"
    image bg atHome131c7ps = "images/ep5/atHome131c7ps.png"
    image bg atHome132_c7ps = "images/ep5/atHome132_c7ps.png"
    image bg atHome132c6ps = "images/ep5/atHome132c6ps.png"
    image bg atHome132c7ps = "images/ep5/atHome132c7ps.png"
    image bg atHome133_c8ps = "images/ep5/atHome133_c8ps.png"
    image bg atHome133c6ps = "images/ep5/atHome133c6ps.png"

    image bg nApt24c5ps = "images/ep5/nApt24c5ps.png"
    image bg nApt25c6ps = "images/ep5/nApt25c6ps.png"
    image bg nApt26c6ps = "images/ep5/nApt26c6ps.png"
    image bg nApt27c1ps = "images/ep5/nApt27c1ps.png"
    image bg nApt28c1ps = "images/ep5/nApt28c1ps.png"
    image bg nApt29c1ps = "images/ep5/nApt29c1ps.png"
    image bg nApt30_c2ps = "images/ep5/nApt30_c2ps.png"
    image bg nApt30c2ps = "images/ep5/nApt30c2ps.png"
    image bg nApt31c3ps = "images/ep5/nApt31c3ps.png"
    image bg nApt31_c3ps = "images/ep5/nApt31_c3ps.png"
    image bg nApt32c4ps = "images/ep5/nApt32c4ps.png"
    image bg nApt33_c8ps = "images/ep5/nApt33_c8ps.png"
    image bg nApt33c7ps = "images/ep5/nApt33c7ps.png"
    image bg nApt34_c9ps = "images/ep5/nApt34_c9ps.png"
    image bg nApt34c9ps = "images/ep5/nApt34c9ps.png"

    image bg bank1c1ps = "images/ep5/bank1c1ps.png"
    image bg bank2c2ps = "images/ep5/bank2c2ps.png"
    image bg bank3c2ps = "images/ep5/bank3c2ps.png"
    image bg bank4c4ps = "images/ep5/bank4c4ps.png"
    image bg bank5c4ps = "images/ep5/bank5c4ps.png"
    image bg bank6c5ps = "images/ep5/bank6c5ps.png"
    image bg bank7_c6ps = "images/ep5/bank7_c6ps.png"
    image bg bank7c7ps = "images/ep5/bank7c7ps.png"
    image bg bank8_c7_ps = "images/ep5/bank8_c7_ps.png"
    image bg bank8_c7ps = "images/ep5/bank8_c7ps.png"
    image bg bank8c7ps = "images/ep5/bank8c7ps.png"
    image bg bank9c6ps = "images/ep5/bank9c6ps.png"
    image bg bank10c8ps = "images/ep5/bank10c8ps.png"
    image bg bank11c9ps = "images/ep5/bank11c9ps.png"
    image bg bank12_c2ps = "images/ep5/bank12_c2ps.png"
    image bg bank12c2ps = "images/ep5/bank12c2ps.png"
    image bg bank13_c2ps = "images/ep5/bank13_c2ps.png"
    image bg bank13c2ps = "images/ep5/bank13c2ps.png"
    image bg bank14c3ps = "images/ep5/bank14c3ps.png"
    image bg bank15c4ps = "images/ep5/bank15c4ps.png"
    image bg bank16c4ps = "images/ep5/bank16c4ps.png"
    image bg bank17_c7ps = "images/ep5/bank17_c7ps.png"
    image bg bank17c5ps = "images/ep5/bank17c5ps.png"
    image bg bank17c6ps = "images/ep5/bank17c6ps.png"
    image bg bank17c7ps = "images/ep5/bank17c7ps.png"
    image bg bank18c1ps = "images/ep5/bank18c1ps.png"
    image bg bank19c2ps = "images/ep5/bank19c2ps.png"
    image bg bank20_c9ps = "images/ep5/bank20_c9ps.png"
    image bg bank20c8ps = "images/ep5/bank20c8ps.png"
    image bg bank21c10ps = "images/ep5/bank21c10ps.png"
    image bg bank22_c10ps = "images/ep5/bank22_c10ps.png"
    image bg bank22c10ps = "images/ep5/bank22c10ps.png"
    image bg bank23_c12ps = "images/ep5/bank23_c12ps.png"
    image bg bank23_c13ps = "images/ep5/bank23_c13ps.png"
    image bg bank23c11ps = "images/ep5/bank23c11ps.png"
    image bg bank23c12ps = "images/ep5/bank23c12ps.png"

    image bg nApt35c1ps = "images/ep5/nApt35c1ps.png"
    image bg nApt36_c2ps = "images/ep5/nApt36_c2ps.png"
    image bg nApt36c2ps = "images/ep5/nApt36c2ps.png"
    image bg nApt37c3ps = "images/ep5/nApt37c3ps.png"
    image bg nApt38_c4ps = "images/ep5/nApt38_c4ps.png"
    image bg nApt38c4ps = "images/ep5/nApt38c4ps.png"
    image bg nApt39_c6ps = "images/ep5/nApt39_c6ps.png"
    image bg nApt39c5ps = "images/ep5/nApt39c5ps.png"
    image bg nApt40_c8ps = "images/ep5/nApt40_c8ps.png"
    image bg nApt40_c9ps = "images/ep5/nApt40_c9ps.png"
    image bg nApt40c7ps = "images/ep5/nApt40c7ps.png"
    image bg nApt41c10ps = "images/ep5/nApt41c10ps.png"
    image bg nApt42_c11ps = "images/ep5/nApt42_c11ps.png"
    image bg nApt42c11ps = "images/ep5/nApt42c11ps.png"
    image bg nApt43_c12ps = "images/ep5/nApt43_c12ps.png"
    image bg nApt43c12ps = "images/ep5/nApt43c12ps.png"
    image bg nApt43c13ps = "images/ep5/nApt43c13ps.png"
    image bg nApt44c12ps = "images/ep5/nApt44c12ps.png"
    image bg nApt45_c15ps = "images/ep5/nApt45_c15ps.png"
    image bg nApt45c14ps = "images/ep5/nApt45c14ps.png"
    image bg nApt46_c16ps = "images/ep5/nApt46_c16ps.png"
    image bg nApt46c16ps = "images/ep5/nApt46c16ps.png"
    image bg nApt47_c17ps = "images/ep5/nApt47_c17ps.png"
    image bg nApt47c17ps = "images/ep5/nApt47c17ps.png"

    label episode5:

        c "Impressive, huh ? It's {b}AMCG{/b}, [bro]..."
        scene bg atHome98c4ps with fade
        b "AMCG ?!"
        c "Advanced Military Combat Gear for the army and special forces, at least it was ment to be. These are only prototypes, none in mass production. We hope that this stuff will give as an advantage against the other guys during the conflict"
        $ ep5suitcaseGun = 0
        $ ep5suitcaseTube = 0
        menu ep5suitcase:
            "Take the Gun" if ep5suitcaseGun == 0:
                $ ep5suitcaseGun += 1
                scene bg atHome99c4ps with Dissolve(1.0)
                b "What is so advanced about this gun ?"
                c "The gun is a prototype of a new generation fire weapon. It equipped with Artificial Neural Network or {b}ANN{/b}, built in fingerprint scanner for security reasons, and bunch of other sensors that will drastically increase your accuracy."
                c "Of course it is switchable if you decide to shot into the air for some reason."
                scene bg atHome100c4ps with dissolve
                b "No shit.."
                c "ANN tracks current barrel position and processes given thermal image, then compares it with human body shape patterns. All combined it allows to compute whether the shot will be successful or not."
                c "In other words it's 'One shot - One hit' toy.."
                play sound ('music/sounds/click.mp3')
                scene bg atHome101c4ps with dissolve
                b "Sounds interesting.."
                b "If this gun is so advanced, why didn't they put into production.. It would be huge advantage for the soldiers during combat, wouldn't it ?"
                c "This gun is an expensive one. 'Bean counters' in the government didn't think that a soldier's life was worth this much."
                play sound ('music/sounds/click.mp3')
                scene bg atHome99c4ps with dissolve
                b "Damn.."
                c "We wanted to perform reverse engineering in order to run mass production or at least make few more toys like this for our 'company'. Unfortunately our tech-guy stopped answering phone calls few hours ago"
                b "Doesn't look like a coincidence"
                c "Indeed"
                jump ep5suitcase
            "Take the Tube" if ep5suitcaseTube == 0:
                $ ep5suitcaseTube += 1
                scene bg atHome102c4ps with Dissolve (1.0)
                b "What are these glowing tubes..?"
                c "Those are {b}ECEN{/b} which is basically: experimental cognitive enhancers and neurostimulators."
                b "Did you just speak English ? Cause I don't understand anything."
                c "Listen [bro], these chemical compounds are incredibly dangerous and harmful drugs with a whole lot of side effects that will inevitably damage your central nervous system."
                b "But they are in the suitcase which means that this stuff is meant for something more than just a headache, depression or diarrhea right ?"
                c "Absolutely, all these three tubes serve their own purpose. But the effect and side-effect are most likely to be permanent so you should ask yourself: are you willing to lose the part of who you are and become something another..? There is no way back after injection."
                b "I guess not.."
                c "These three tubes are all we have right now, [bro]. I would rather you didn't use it on you, unless the situation is hopeless. We need to find a high qualified chemist who can analyze the substance and a laboratory in order to reproduce this stuff."
                b "I see.."
                jump ep5suitcase

        scene bg atHome98c4ps with Dissolve (1.0)
        c "Anyway, the gun is yours. Feel free to use it from now on. But I'm asking you to leave the stimulators as is."
        b "Understood. What about the overall situation ? Any news from the boss ?"
        c "Unfortunately no. I would tell you if I knew anything myself. As you know the boss left me in charge and for now the situation looks quite shitty. We are losing more and more loyal people. It's hard to determine who can be trusted and who is compromised, so watch out."
        c "By the way, I've announced that Antonio is the traitor, so as soon as our guys find him I'll contact with you. For now wait for further instructions and get yourself some rest, [bro]."
        b "Got it.."
        "{b}{i}END OF CALL{/b}{/i}"
        b "{i}Damn..{/i}"
        b "{i}I'm too tired to analyze all this information right now. I'd better lock the suitcase and hide it. I need to get myself some sleep, I'm exhausted..."
        menu:
            "Go to sleep":
                jump ep5morning
        return

    label ep5morning:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Sonraki sabah...")
        $ renpy.pause()
        scene bg atHome103c6ps with Dissolve (1.0)
        $ renpy.pause()
        j "[bro].. are you sleeping ?"
        b "Z-z-z.."
        scene bg atHome103c1ps with fade
        j "Wake up, sleeping secret spy, ha-ha.. It's already noon !"
        scene bg atHome103c1ps with vpunch
        scene bg atHome103c1ps with vpunch
        scene bg atHome103c1ps with vpunch
        scene bg atHome104c5ps with fade
        b "Z-z.. Huh ?! What, who..me.. I'm not sleeping.. {i}Yawn.."
        j "Ha-ha..Tough night, huh ? Probably been busy saving the world ?"
        b "{i}Yawn..{/i} Yeah, you could say so.."
        menu:
            "Get up":
                scene bg atHome105c7ps with fade
        j "Considering how heavy you were asleep, the world most likely was saved this night at least few times, ha-ha.."
        b "You know, it's a boring job, but someone has to do it.."
        scene bg atHome105c8ps with fade
        j "Sure, ha-ha. Sorry that I had to wake you up though, but you do remember that today is a very intense day with a bunch things we need to do, right ?"
        b "Really ? Why me sleeping few more hours just couldn't be one of those things, huh.."
        j "Come on, [bro]. We need to visit the bank, do the workout at the gym, also I wanted to go shopping with you, I want to buy some new clothing before meeting Scarlett. I can't wait to introduce you to each other..."
        b "That's not how I imagined my day-off.."
        scene bg atHome106c7ps with fade
        j "Well, sorry for altering your top-secret schedule, ha-ha. But first of all you need to have your breakfast. I made it while you were sleeping so you'd better start eating unless you like it cold.."
        b "Thank you, Julie. It's so sweet of you"
        $ ep5JulieLipsKissed = 0
        menu:
            "Kiss her forehead":
                play sound ("music/sounds/kiss.mp3")
                scene bg atHome107c9ps with kissFlash
                b "{i}mwah.."
                j "Ha-ha, it tickles, [bro]"
                scene bg atHome109c8ps with fade
                b "I'm so glad that you are here, Julie. Now I know what I've been missing all this time."
                j "Me too [bro], I'm so happy that we are finally together.."
            "Kiss her lips":
                play sound ("music/sounds/kiss.mp3")
                scene bg atHome108c9ps with kissFlash
                $ ep5JulieLipsKissed += 1
                b "{i}mwah.."
                j "{i}Mmah.."
                if ep4JulieShirtTold == 1:
                    scene bg atHome109c8ps with fade
                    b "You are an amazing girl, Julie. Incredibly beautiful, smart, funny and caring. You're the best [sis] I could ever ask for..."
                    j "I love you too [bro], you are a lot more than just a [brother] to me.."
                else:
                    scene bg atHome109_c8ps with fade
                    j "Wow.. That was quite unexpected, [bro].."
                    b "Why.. You didn't like it, Julie ?"
                    j "I.. I don't know.. Do you think it's okay to kiss each other like this ? I mean we are [brother] and [sis], it's not the same like when we were kids, we are adults now.."
                    b "I think you are over complicating things, Julie. I'm just showing you my gratitude and love. I'm totally okay with it, but if you don't like it.."
                    scene bg atHome109c8ps with dissolve
                    j "I'm okay with it too, [bro]. Nevermind, I don't know why I was even thinking about this.."
                    b "I'm glad to hear it"
        scene bg atHome110c10ps with fade
        j "But hey, you'd better hurry up, we don't have all day for kisses and cuddles. I already had my breakfast so now I'm going to take a shower, hope you'll finish by the time I go out."
        b "Do you remember where the towels are or I should guide you again ?"
        scene bg atHome110c9ps with fade
        j "Ha-ha, no [bro]. I think this time I'll be able to find them myself, unless you deliberately have hidden them in order to see me wet and all naked, ha-ha."
        b "Hm, I wouldn't mind.. That is a really good idea, thanks for the advice, Julie."
        scene bg atHome110c11ps with fade
        j "Ha-ha, shame on you !"
        b "What ?! It's you who said that, not me. Anyway, it's not like there is something I haven't seen before."
        j "Yeah, keep saying yourself that, [bro], ha-ha."
        $ renpy.pause()
        scene bg atHome111c12ps with fade
        b "You just don't remember it but we used to take a bath together. I always had to wash your back cause you were so dirty.."
        j "Actually I still am, even more than before.. But now the situation is quite different as you may noticed."
        $ renpy.pause()
        scene bg atHome111c15ps with fade
        b "Oh I did, Julie. It's really hard not to notice..some things.."
        j "Thanks.. I'll take it as a compliment, [bro]."
        scene bg atHome111c13ps with fade
        b "I'm starting to get ha..hungry. Seems like my appetite has awaken. Anyway, if you need anything, just call me, okay ?"
        j "Oh yeah ? Enjoy your meal then, but don't need to rush, better take it slow. It may still be hot.."
        b "Thanks, Julie."
        j "No peeking, [bro].."
        b "Well, if you insist.."
        j "Not really, ha-ha.."
        b "You such a bad girl, Julie.."
        j "I know.. See you soon, [brother].."
        scene black with Dissolve (2.0)
        $ renpy.notify ("15 dakika sonra...")
        $ renpy.pause()
        scene bg atHome112c1ps with dissolve
        b "{i}The breakfast was delicious. I have to admit that Julie definitely knows how to cook. Probably [mom] shared few her secrets with Julie. By the way, I should probably call her and tell that everything is alright. We haven't talked to each other for a long time."
        b "{i}I wonder what this 'little talk' right before Julie went to the bathroom was all about. I know that she likes fooling around but, this time it seemed more like flirting or something."
        b "{i}Damn, [bro]. Do you really think she might be sexually attracted to her older [brother] ?! She clearly let me know about her sexual orientation, and she has a girlfriend so that is already two reasons to throw this shit out of your head and focus on a more serious problems."
        b "{i}Like how not to catch a bullet in your head during upcoming war between gangs or how can I protect Julie if something goes wrong."
        b "{i}Fuck, why all this shit is happening right now.."
        $ renpy.pause()
        scene bg atHome113c1ps with dissolve
        j "Hi there.."
        b "Julie.."
        j "Did you like the breakfast, [bro] ?"
        b "Yes, it was incredibly tasty, Julie. I would never cook myself something like that. What is your secret ?"
        j "Okay, I will tell you one big secret, but only because you're my [brother] and if you promise me not sharing it with others, deal ?"
        b "You have my word.."
        j "You must never use overdue products !"
        b "Damn, I was so close to figuring it out myself. That is basically one of the drawbacks of being a spy. After saving the world the grocery stores are already closed so you have to eat whatever is left in the fridge, you know..."
        scene bg atHome114c3ps with fade
        j "Ha-ha, don't worry. From now on I'll take care about your nutrition, [bro]."
        b "Thanks Julie, you are a life savior. So how much time do you need before we can go ?"
        j "I'm almost ready I just need to get dry and get dressed, 15 minutes will be enough, I think."
        b "Okay then, I'm getting dressed too.."
        play sound ("music/sounds/doorKnock.mp3")
        "{i}knock-knock"
        scene bg atHome115c3ps with dissolve
        j "Huh..?"
        b "Julie, go to your room, now !"
        b "... Who is there ?"
        n "It's Nicole, your neighbour... May I come in ?"
        scene bg atHome115_c3ps with dissolve
        j "Nicole ? Is she hot ?"
        b "Julie, stop it ! Please go to your room, you are almost naked... \nOne minute Nicole, I'm coming."
        j "Come in, it's opened !"
        scene bg atHome115_c3ps with hpunch
        b "What ?!"
        j "I went for the groceries in the morning and didn't lock the door after that, so what.."
        b "Argh.. Next time make sure you lock it, okay ? Come in, Nicole.."
        play sound ("music/sounds/openDoor.mp3")
        scene bg atHome116c2ps with fade
        n "Hello, [bro]. Thanks god you are at home."
        $ renpy.pause()
        scene bg atHome117c4ps with fade
        b "Julie, meet Nicole. Nicole, this is my little [sis] Julie."
        scene bg atHome116_c2ps with fade
        n "Nice to meet you, Julie. [bro] told me a lot about you."
        j "Wow, you are adorable Nicole. [bro] didn't tell me that he has such a hot neighbour."
        scene bg atHome117_c4ps with fade
        b "Julie!"
        n "Wow, quite straightforward but thanks, ha-ha. You are very cute and pretty as well, baby."
        scene bg atHome118_c5ps with fade
        j "{b}Whispering:{/b}\nSo are you dating [bro] already or you two just not get to that yet ?"
        n "{b}Whispering:{/b}\nYes, we just started, but I think I'm falling for him already"
        j "{b}Whispering:{/b}\nI knew it as soon as you came in. The way you look at each other told me everything. It's hard not to feel this sexual tension and chemistry between two of you."
        scene bg atHome118c6ps with fade
        n "{b}Whispering:{/b}\nReally ? I didn't think that it is so noticeable, ha-ha.. You are very observant for a little girl, Julie.."
        j "{b}Whispering:{/b}\nYeah, it seems like you want him really bad.. He feels the same towards you, believe me"
        n "{b}Whispering:{/b}\nOh my god Julie, I'm embarrassed.. I mean I didn't think that you are so frank and discerning.."
        scene bg atHome118_c6ps with dissolve
        n "{b}Whispering:{/b}\nBy the way, your towel slipped off, Julie. You should probably cover your..you know.."
        j "Huh ?"
        scene bg atHome119c5ps with fade
        $ renpy.pause()
        j "{b}Whispering:{/b}\nWow that is awkward.. I can't believe I was standing and talking in front of you all this time like this."
        n "{b}Whispering:{/b}\nIt's okay Julie, there is nothing to worry about..I've seen plenty of these in the female dormitory back then when I was at your age."
        scene bg atHome120c8ps with fade
        b "Girls, what are you whispering about ?"
        n "You know, just a girls talk [bro]."
        scene bg atHome121_c8ps with dissolve
        j "Yeah, men not allowed to hear it, that is why we were whispering, ha-ha"
        n "Exactly"
        b "I see"
        scene bg atHome121c8ps with dissolve
        j "Okay guys, I'll leave you alone so you can chit-chat a bit. But I still will be able to hear you through the door, so no funny business, ha-ha. It was nice to meet you Nicole, see you later."
        n "Likewise Julie, bye."
        play sound ("music/sounds/doorClose.mp3")
        scene bg atHome122c6ps with fade
        n "She is a good girl, [bro]."
        b "Yeah, I know.. I'm happy to see you Nicole, you are looking adorable. Last evening was amazing.."
        n "I'm glad to see you too, [bro].. I hope you enjoyed everything as much as I did.."
        b "Sure thing, it was incredible, I can't wait to do it again.."
        n "Really ?"
        b "I would so pinned you towards the wall and have my way with you right now.."
        scene bg atHome124c6ps with dissolve
        n "Oh, [bro].. You are making me blush.."
        j "{b}Voice from another room:{/b}\nWow, that was pretty hot line, good job [bro] !"
        scene bg atHome123c6ps with dissolve
        b "..."
        n "Ha-ha, right."
        scene bg atHome122c6ps with dissolve
        n "I almost forgot, I feel uncomfortable asking you again, but.. Could you help me to bring into my apartment some of my stuff ?"
        b "Actually we are kind of in a hurry, Nicole."
        n "It won't take long, there are just few boxes, I would do it myself but they are too heavy for me. I don't know how it happened, probably the freight company messed up order details or something. I asked them to deliver my stuff directly into the apartment but instead they left it all outside, in front of the building."
        b "Oh, I see.. Julie, meet me outside in 10 minutes, I will be waiting for you at the street after I finish helping Nicole."
        j "{b}Voice from another room:{/b}\nOkay!"
        scene bg atHome125c7ps with fade
        n "Thank you, [bro]. I don't even know what would I do without you.."
        b "Don't mention it, Nicole. It's a piece of cake."
        n "Sure, for a young handsome with the body like this, lifting couple of heavy boxes is not a problem at all."
        b "Yeah, sometimes it happens to the guys who are regularly visiting the gym."
        n "I didn't know that you are that fit.. I can actually offer you something.."
        b "Let's talk about this in the meanwhile, I need to get dressed."
        scene bg atHome124_c6ps with fade
        n "Right, I will be waiting for you outside, [bro]."
        b "Okay.. Julie, I hope you don't forget to take all your documents that will be needed at the bank."
        scene bg atHome126c5ps with fade
        j "{b}Voice from another room:{/b}\nI will, [bro]! I mean I won't forget them, thanks for the reminding."
        b "I will be outside in few minutes, Nicole"
        scene bg atHome126c9ps with fade
        n "Okay.."
        j "{b}Voice from another room:{/b}\nGood bye, Nicole ! We definitely should hang out together sometime !"
        b "..."
        n "Ha-ha, sure thing, Julie"
        $ renpy.pause()
        jump ep5Julie
        return

    label ep5Julie:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Bir an sonra...")
        $ renpy.pause()
        $ renpy.music.set_volume(0.25, delay=0, channel=1)
        $ renpy.music.play("music/sexyTheme.mp3", channel=1, loop=True, fadein=15)
        scene bg atHome127c2ps with Dissolve (2.5)
        j "{i}Finally.. [bro] has gone and I can play with myself in this room. I can still smell Nicole's perfume and this scent of sexual tension between two of them.."
        $ renpy.pause()
        scene bg atHome127c4ps with fade
        j "{i}I'm so horny right now.. I haven't had sex with Scarlett for few months by now. But I have needs too, my little pussy is dripping wet, damn.."
        $ renpy.pause()
        scene bg atHome128c3ps with fade
        j "{i}I don't know what is so special about this couch but I have the most intense orgasm only when I'm masturbating on it. Maybe it's all because of [bro].. The fact that he sleeps here without even knowing that I masturbate on the couch turns me on so bad. I'm such a naughty girl.."
        $ renpy.pause()
        scene bg atHome129c5ps with fade
        j "{i}I wonder how it would feel when I masturbate on this couch directly in front of [bro] while he will be sleeping.. I should definitely try it sometime, I guess I will orgasm like a little slut.."
        $ renpy.pause()
        scene bg atHome130c6ps with fade
        j "{i}My titties are so lonely without Scarlett's sweet kisses and warm tongue.. The way she caresses my breasts and sucks on my nipples drives me crazy.."
        $ renpy.pause()
        scene bg atHome130_c6ps with dissolve
        j "{i}Mmm.. I'm missing her soft tiny fingers inside my wet little pussy.. God, I want her to finger me so bad while she will be eating me out down there.."
        $ renpy.pause()
        scene bg atHome132_c7ps with fade
        j "{i}I can't hold it any longer, I'm all wet right now.. Oh, yes.. Here is my tiny little clit.."
        scene bg atHome132c7ps with Dissolve (1.0)
        scene bg atHome132_c7ps with Dissolve (1.0)
        scene bg atHome132c7ps with Dissolve (1.0)
        scene bg atHome132_c7ps with Dissolve (1.0)
        j "{i}Ah, yes.. "
        scene bg atHome132c6ps with fade
        j "{i}I wonder how a real cock would fell inside of my tight little pussy.. My legs are tremble each time I think about something big and hard goes inside of me.."
        scene bg atHome131c7_ps with fade
        j "{i}Sometimes I feel like I'm really missing something warm and throbbing inside my pussy.."
        scene bg atHome131c7ps with dissolve
        j "{i}I like eating pussy but I want to know how a cock tastes like.. I want to suck it really bad.."
        scene bg atHome131c7_ps with dissolve
        j "{i}I would start from the balls, licking my way along the shaft straight towards the glans.."
        scene bg atHome131c7ps with dissolve
        j "{i}Then I would take it all in my deep warm little mouth.."
        scene bg atHome131c7_ps with dissolve
        j "{i}Twirling my tongue all over the glans, while my lips are tightly wrapped around it.."
        scene bg atHome131c7ps with dissolve
        j "{i}I would gag on the cock and take it like a good girl as deep as I can.."
        scene bg atHome131c7_ps with dissolve
        j "{i}Oh yes.. I'm about to cum.."
        scene bg atHome131c7ps with Dissolve (0.75)
        scene bg atHome131c7_ps with Dissolve (0.75)
        scene bg atHome131c7ps with Dissolve (0.75)
        scene bg atHome131c7_ps with Dissolve (0.75)
        scene bg atHome131c7ps with Dissolve (0.75)
        scene bg atHome131c7_ps with Dissolve (0.75)
        j "{i}But most of all I crave that someone bend me over, tie my hands together and spread my legs so can't even move, while fucking me from behind really hard and balls-deep like a fucking whore until I lose my consciousness.."
        scene bg atHome132_c7ps with Dissolve (0.75)
        j "{i}Oh yes, I'm comming.."
        scene bg atHome132c7ps with kissFlash
        scene bg atHome132_c7ps with kissFlash
        scene bg atHome132c7ps with kissFlash
        j "{i}Aaaaah..."
        scene bg atHome133_c8ps with kissFlashLong
        j "{i}Oh my god !!!"
        scene bg atHome133_c8ps with vpunch
        scene bg atHome133_c8ps with vpunch
        scene bg atHome133_c8ps with vpunch
        scene bg atHome133c6ps with kissFlashLong
        j "{i}Mmm.. Yes.. That's it.. My orgasms are getting stronger each time I dream about a cock.. I need to talk with Scarlett about these fantasies.."
        $ renpy.music.stop(channel=1, fadeout=5.0)
        $ renpy.pause()
        jump ep5NicoleDay
        return

    label ep5NicoleDay:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Bu arada...")
        $ renpy.pause()
        scene bg nApt24c5ps with Dissolve (2.0)
        n "That was the last one, thanks [bro]. Looks like I owe you one again."
        b "Don't mention it, Nicole. I know it's not my business but I wonder what's inside of these boxes ?"
        n "Actually it is your business, at least it can be."
        b "I don't understand.."
        scene bg nApt26c6ps with fade
        n "Well, as you might remember I'm a beginner photographer and all this stuff is basically equipment for my work. Photography screen, the tripod, spotlights, reflectors and camera lenses."
        b "I see, but I still don't understand how it is my business anyway."
        n "I want to offer you a job, [bro].."
        b "A job for me ? I know nothing about the photography, Nicole.."
        scene bg nApt27c1ps with fade
        n "Not as a photographer, but as a model. Are you interested ?"
        b "What do you mean.."
        n "Well, now I'm in the middle of an interview that is conducted by a very prestigious online magazine for men. They really like my style and work, however they've given me a test task because I don't have any photos in my portfolio that correspond to the subject of the magazine.."
        n "So I need to send them some photos of a good looking man that is almost naked.. You are ideally fit into the description so that is why I decided to offer you this.. I was wondering maybe.. "
        b "You were wondering if I'm ready to pose for you naked and become famous by showing off my body on the cover of the magazine.."
        scene bg nApt28c1ps with dissolve
        n "Not exactly, but it's not far away from the truth.. Those photos won't be on the cover of the magazine, they are just for the interview purposes.."
        b "I'm in, of course if that means that I still have to be naked in front of you, Nicole.."
        scene bg nApt29c1ps with dissolve
        n "[bro].. It doesn't mean that you have take off all of your clothes.. You don't have to get yourself all naked if you don't want to.."
        b "What about you, Nicole.. What would you want..?"
        scene bg nApt28c1ps with dissolve
        n "[bro].. I.."
        menu:
            "Kiss her":
                b "Come here.."
                play sound ("music/sounds/kiss.mp3")
        scene bg nApt30c2ps with kissFlash
        n "{i}Mwah.."
        $ renpy.pause()

        $ ep5NicoleTongue = 0
        $ ep5NicoleAss = 0
        $ ep5NicoleBreasts = 0
        $ ep5NicolePussy = 0
        menu ep5NicoleMenu:
            "Grope her ass" if ep5NicoleAss == 0:
                $ ep5NicoleAss += 1
                if ep5NicoleTongue == 0:
                    jump ep5NicoleDayEnd
                else:
                    scene bg nApt31c3ps with fade
                    n "{i}Oh, [bro].. Mwah.."
                    b "{i}It' time to give that sexy little buttock a firm squeeze.."
                    menu:
                        "Squeeze":
                            play sound ("music/sounds/sigh.mp3")
                    scene bg nApt31_c3ps with dissolve
                    n "{i}Huh.. Ah.. Mwaa.."
                    n "[bro].. Please don't.. {i}Mwah..{/i} Let's wait till the evening.. Oh.."
                    b "{i}That's right, baby.. I know you like it.."
                    jump ep5NicoleMenu
            "Use your tongue" if ep5NicoleTongue == 0:
                $ ep5NicoleTongue += 1
                $ renpy.music.play("music/sounds/wetKiss_long.mp3", channel=1, loop=True, fadein=0)
                play sound ("music/sounds/kiss.mp3")
                scene bg nApt30_c2ps with kissFlash
                n "{i}Mwah.."
                b "{i}Yes, baby.. Give me that sweet tongue of yours.."
                n "{i}Oh.. [bro].. Mwah.."
                jump ep5NicoleMenu
            "Caress her breasts" if ep5NicoleBreasts == 0:
                $ ep5NicoleBreasts += 1
                if ep5NicoleTongue + ep5NicoleAss == 2:
                    play sound ("music/sounds/sighLoud.mp3")
                    scene bg nApt32c4ps with fade
                    n "N-no.. st.. stop.. [bro].."
                    n "{i}Aah.. Mwah.."
                    b "{i}Good girl.. Playing hard to get.."
                    b "{i}She is not wearing a bra, that's exactly what I like.."
                    b "{i}I bet she is already wet down there.."
                    scene bg nApt30c2ps with fade
                    scene bg nApt30_c2ps with Dissolve (1.0)
                    scene bg nApt30c2ps with Dissolve (1.0)
                    scene bg nApt30_c2ps with Dissolve (1.0)
                    scene bg nApt30c2ps with Dissolve (1.0)
                    jump ep5NicoleMenu
                else:
                    jump ep5NicoleDayEnd
            "Finger her pussy" if ep5NicoleTongue + ep5NicoleAss + ep5NicoleBreasts == 3:
                b "{i}It's one more thing left before she asks me pin her to the wall and fuck her really good.."
                n "Oh.. [bro].. {i}Mwah..{/i} I'm.."
                play sound ("music/sounds/squish.mp3")
                scene bg nApt33c7ps with kissFlash
                play sound ("music/sounds/sighLoud.mp3")
                n "Aaah..!"
                $ renpy.pause()
                b "Wow, no panties.. Such a bad girl.."
                n "P-please, [bro].. D-don't.."
                b "Hm, you may say 'No' but your pussy says 'Yes'.. Just look at my hand.. It's all wet, Nicole.."
                n "Oooh..! {i}Mwah..{/i}"
                b "Now.. Get down on your knees and be a good girl, Nicole.."
                n "As you say.."
                jump ep5NicoleDayEnd
        $ renpy.pause()
        return

    label ep5NicoleDayEnd:
        $ renpy.music.stop(channel=1, fadeout=3.0)
        play sound ("music/sounds/doorKnock.mp3")
        scene bg nApt33_c8ps with fade
        n "Mwah ?"
        b "..."
        j "[bro].. Are you here..?"
        scene bg nApt34_c9ps with fade
        n "Looks like you need to go, [bro].. See you at the evening then ?"
        b "Of course, Nicole. Get ready for me.. You will remember this photo shoot for a long time.."
        n "I can't wait.."
        j "[bro], we really don't have that much time.."
        scene bg nApt34c9ps with dissolve
        n "He is coming, Julie.. I'm returning [bro] to you.."
        b "I want you so bad Nicole.. You are driving me mad.."
        scene bg nApt34_c9ps with dissolve
        n "Not now, handsome.. You will have me at the evening.."
        b "I'm coming, Julie.."
        n "That's right.. I'll be waiting for you, [bro].."
        $ renpy.pause()
        jump ep5Bank
        return

    label ep5Bank:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra Bankada...")
        $ renpy.pause()
        scene bg bank1c1ps with Dissolve (2.0)
        b "Here we are, Julie. You can take a sit over there I just need to talk with few people to skip the queues and make sure that the procedure will be finished as quick as possible."
        j "Aha.."
        b "Julie.. Are you even listening ?"
        j "Yeah-yeah, just a second.."
        scene bg bank2c2ps with fade
        "{b}{i}Guard:{/b}{/i}\nGood afternoon, [bro]. We are always glad to welcome you in our humble refuge. May I be of some help to you ?"
        b "Hi, Stephen. I'm glad to see you too. Where did you learn to talk like that ?"
        "{b}{i}Stephen:{/b}{/i}\nAt the service of the queen of England of course, ha-ha"
        b "At ease, soldier ! Have you seen Markus by any chance ?"
        "{b}{i}Stephen:{/b}{/i}\nHe is at his office as always. By the way.."
        scene bg bank3c2ps with dissolve
        "{b}{i}Stephen:{/b}{/i}\nWho is this pretty gorgeous young little lady with you.."
        j "At ease Stephen, I'm a lesbian."
        "{b}{i}Stephen:{/b}{/i}\nWow.."
        b "Well, better luck next time, friend.."
        j "Hey, [bro] it is Scarlett texting me right now. She says that she will be in the city in a few hours, I'm so excited !"
        b "Good for you, Julie."
        scene bg bank2c2ps with dissolve
        b "Anyway, it was nice to see you Stephen. Say hello to your wife and children from me."
        "{b}{i}Stephen:{/b}{/i}\nSure thing, as soon as I will have them, ha-ha"
        b "Can't live alone forever, pal."
        "{b}{i}Stephen:{/b}{/i}\nDid your wife tell you that ?"
        b "Ha-ha.. Take care, buddy"
        "{b}{i}Stephen:{/b}{/i}\nSee you around, [bro].."
        scene bg bank4c4ps with fade
        b "Listen Julie, I need to talk to the manager of this bank in order to make all this process as quick as possible. I suggest you take a sit in the meanwhile and wait for me until I call you, okay ?"
        j "Okay, [bro]. As you say, I will be waiting for you right here."
        b "Do not get bored here without me, promise ?"
        scene bg bank5c4ps with dissolve
        j "Oh don't worry about it. Scarlett just started sending me her nude photos, so I won't get bored."
        b "Wow, that is interesting.."
        j "Yup ! Do you want to take a look..?"
        b "Ahm.. Thanks, but probably later, now is not the best time you know.."
        j "As you wish.."
        b "I'll be right back, Julie"
        scene black with Dissolve (2.0)
        $ renpy.notify ("Birkaç dakika sonra...")
        $ renpy.pause()
        scene bg bank6c5ps with Dissolve (2.0)
        v "..."
        v "God dammit I hate these queues! What is the current number ? Argh, 10 more people before me.."
        v "Huh..? Is that Julie..?"
        scene bg bank7c7ps with fade
        v "Hi, kiddo.."
        j "Vicky ? What a surprise ! I'm happy to see you. You're looking hot as hell, just as always.."
        scene bg bank7_c6ps with fade
        v "Thanks, Julie. You are looking fantastic too. What are you doing here alone ?"
        j "Oh, I'm not alone here, [bro] is with me"
        $ renpy.pause()
        scene bg bank8_c7_ps with fade
        j "He is talking to the manager right now. We came here to open a bank account for me. He said that it won't take long, but I literally feel how I'm getting old while I'm waiting for him, ha-ha"
        v "I see.."
        scene bg bank8_c7ps with dissolve
        j "Anyway.. What are you doing here besides breaking the hearts of all these poor males ?"
        scene bg bank9c6ps with fade
        j "Wait.. Is something happened..? Your amazing smile just suddenly gone from your face.."
        v "Ahm.. Nevermind, Julie, I'm okay.. I just hate such things as queues, you know.."
        j "Really..? For a moment I started to think that it's something between you and [bro].."
        v "You are right Julie, it is.. I don't want to be rude but this is our problems. I would rather keep it between me and him alone, hope you will understand.."
        j "Okay Vicky.. But I want you to know that if you ever need to talk about it I'm always here for you.."
        v "Thanks, Julie.."
        j "Wait a second.."
        scene bg bank8c7ps with fade
        j "Who are these guys..?! Is this some kind of prank or something..?!"
        v "Huh..?"
        $ renpy.music.play("music/enemyTheme.mp3", channel=1, loop=True, fadein=10)
        scene bg bank11c9ps with fade
        $ renpy.pause()
        "{b}{i}Robber:{/b}{/i}\nLadies and Gentlemen, may I have your attention please. Today you are lucky to witness the most daring robbery, but do not forget to lie on the floor and keep your hands in sight, unless you are really tired of living your fucking lives !"
        scene bg bank11c9ps with vpunch
        "{b}{i}Robber:{/b}{/i}\nPlease keep in mind that the last one who will be standing on their feet will get a bullet from me, so hurry up ! {i}Working fast, guys, we have only 5 minutes to clean the vault.."
        scene bg bank12c2ps with fade
        "{b}{i}Stephen:{/b}{/i}\nHey, are you out of your mind guys ? Do you even know whose bank you are trying to rob ?! You are all dead men !"
        "{b}{i}Robber:{/b}{/i}\nLooks like we have a winner !"
        play sound ("music/sounds/shotgun.mp3")
        scene bg bank12_c2ps with killFlash
        "{b}{i}Stephen:{/b}{/i}\nAagh..."
        play sound ("music/sounds/bodyFall.mp3")
        scene bg bank13c2ps with dissolve
        "{b}{i}Robber:{/b}{/i}\nThat's a shame. He probably wanted to say something important.."
        scene bg bank13_c2ps with dissolve
        "{b}{i}Robber:{/b}{/i}\nAnyone else has something to say ?"
        $ renpy.pause()
        scene bg bank10c8ps with fade
        "{b}{i}Markus:{/b}{/i}\nWhat the hell ?! It was a gunshot, wasn't it ?"
        b "Shit.. It's a robbery, turn on the alarm right now !"
        "{b}{i}Markus:{/b}{/i}\nAlready did.. Hope our guys will arrive quick enough.. What kind of psychos decided to rob our vault ?!"
        b "They don't look like an amateurs, Markus.. They've killed Stephen.. If I were you I would call the police as well. As you understand the situation is far more serious than just a bunch of psychos in the masks picked wrong bank to rob.."
        "{b}{i}Markus:{/b}{/i}\nDamn.. What are you going to do about it, [bro]..?"
        b "I'll wait until they split up, they have those money bags for a purpose.."
        "{b}{i}Markus:{/b}{/i}\nWhat the hell ?! The indicator shows that the vault is opened.. How did they crack it that fast.."
        b "They know the code, it's obvious.. Someone sold us out.."
        "{b}{i}Markus:{/b}{/i}\nFuck!"
        scene bg bank15c4ps with fade
        "{b}{i}Robber:{/b}{/i}\nKeep an eye on things over here, we will be back in 3 minutes. If you feel like someone decided to play a fucking hero, do not hesitate and shoot the motherfucker."
        "{b}{i}Scum:{/b}{/i}\nGot it boss !"
        scene bg bank14c3ps with fade
        j "Vicky, did they just kill that guy ?! I'm scared.. {i}sob-sob..{/i} Thanks god you are here.. I don't know what would I do if I were here alone.. [bro]! Oh my god, I hope he is okay..{i}sob-sob..{/i}"
        v "Hush Julie, you need to calm down.. We don't want to draw their attention.. They just take what they came for and will go away.. Keep quiet and try to avoid the eye contact.."
        $ renpy.pause()
        scene bg bank16c4ps with fade
        "{b}{i}Scum:{/b}{/i}\nOkay dear visitors, I have only two rules for you, so if you want to survive this little madness, I highly recommend you to follow them"
        "{b}{i}Scum:{/b}{/i}\nThe rules are simple: Stay the fuck down and Shut the fuck up ! It's that easy.."
        $ renpy.pause()
        scene bg bank14c3ps with fade
        j "Oh no, Vicky.. He is coming to us.. What does he need here.. Please don't let him hurt us.. {i}sob-sob..{/i}"
        v "Calm down, Julie.. He won't hurt you.. I promise.."
        scene bg bank17c5ps with fade
        "{b}{i}Scum:{/b}{/i}\nWell-well-well, look who is here.. Two sexy bitches.. My prayers are finally answered.."
        j "Oh my god Vicky, no.. I'm so scared..{i}sob-sob.."
        "{b}{i}Scum:{/b}{/i}\nHm, I don't even know what to chose, sweet little bum of the blondy or luscious huge tits of the brunette. I guess we will take both of you to our shelter. You are good girls and will help us to celebrate, am I right ?"
        j "No.. I don't want it Vicky, please..{i}sob-sob..{/i}"
        scene bg bank17c7ps with fade
        v "She is just the kid.. How about you have only me and this will be enough for you.."
        "{b}{i}Scum:{/b}{/i}\nNo, sexy.. We have one more guy with us, so we need at least four sweet little holes to fuck, he-he.."
        j "No.. please don't hurt us..{i}sob-sob..{/i}"
        scene bg bank17_c7ps with dissolve
        "{b}{i}Scum:{/b}{/i}\nHey, this little bitch starts to annoy me with this sobbing shit.."
        v "..."
        j "{i}Sob-sob..{/i}"
        scene bg bank17c6ps with fade
        "{b}{i}Scum:{/b}{/i}\nI'm serious, tell her to shut the fuck up or I will calm her down forever"
        b "You will pay for that, bastard. Damn.. It's too risky to shot him from here, he is holding the gun right in front of girls.. I need to get closer.."
        "{b}{i}Scum:{/b}{/i}\nOkay sluts, did I make it clear that you are going with us when we are finished here ?"
        scene bg bank18c1ps with fade
        j "Yes..{i}sob..{/i}"
        v "Yes, Sir.. As you wish.."
        "{b}{i}Scum:{/b}{/i}\nThat's a good girls.."
        v "{b}{i}Whispering:{/i}{/b}\nJulie, everything is okay.. [bro] is right behind him, we just need to distract this scum so [bro] could neutralize him.. Will you help me with that ?"
        j "{b}{i}Whispering:{/i}{/b}\nWhat's on your mind, Vicky ?"
        v "Come here, baby.."
        play sound ("music/sounds/kiss.mp3")
        scene bg bank20_c9ps with kissFlash
        v "{i}Mwah.."
        j "{i}Oh..? mwah.."
        "{b}{i}Scum:{/b}{/i}\nWhat the fuck..?"
        play sound ("music/sounds/kiss.mp3")
        scene bg bank20c8ps with kissFlash
        j "{i}Mwah..{/i} Vicky your lips are so soft and sweet.."
        v "{i}Mma..wah..{/i} You are an amazing kisser, Julie.."
        play sound ("music/sounds/kiss.mp3")
        scene bg bank19c2ps with kissFlash
        "{b}{i}Scum:{/b}{/i}\nDamn, bitches.. You just can't wait any longer, huh ? The idea of two hard cocks inside of you turned you on, he-he..?"
        v "Oh yes.. I'm starting to get wet down there.. {i}mwah.."
        j "Ah, baby.. I feel a pleasant tingle betweetn my legs.. {i}mwah.."
        "{b}{i}Scum:{/b}{/i}\nFuck.. You are so bad, bitches.. I can't wait to shove my cock right up inside each of your asses ! I think the blondy will be the first, it seems that her ass is much tighter, no offence he-he.."
        $ renpy.pause()
        scene bg bank21c10ps with fade
        "{b}{i}Scum:{/b}{/i}\nShit.. I imagine how it would feel when I thrust my cock balls deep inside your asses, sluts !"
        $ ep5killCounter = 0
        menu:
            "Kill":
                $ ep5killCounter += 1
                b "Imagine this you piece of shit."
                play sound ("music/sounds/gunSilencer.mp3")
                scene bg bank22c10ps with killFlash
                "{b}{i}Scum:{/b}{/i}\nAhg............."
                scene black with dissolve
                play sound ("music/sounds/bodyFall.mp3")
                $ renpy.pause()
                scene bg bank23c11ps with Dissolve(1.5)
                j "Oh my god [bro] I'm so glad that you are finally here.."
                b "There-there baby.. There is nothing to worry about anymore.."
                b "Hey.."
                v "[bro].."
                b "Nice move with the distraction, thank you.. And thanks for being with Julie, I appreciate it, Vicky.."
                scene bg bank23c12ps with fade
                v "You didn't have to kill him, [bro]. The police will now have a lot of questions.. Anyway it's not the best time to think about this right now. We need to help evacuate the people from the building and do something about those two robbers."
                "{b}{i}Markus:{/b}{/i}\nThe police is coming, I already called them.."
                scene bg bank23_c12ps with dissolve
                v "Good, we just need to take care of those two.."
                b "Vicky, help people to leave the bank and take Julie away from here.. I'm going to kill those bastards !"
                scene bg bank23c12ps with dissolve
                j "No please, [bro].. Don't go there, don't leave me alone here.."
                b "It's okay, Julie.. I'll be right back.."
                v "I doubt it, [bro]. You won't have the surprise effect like you just had with this guy, and besides there are two of them. We need to come up with something better that just assaulting the vault, you don't want to die in vain, do you ?"
                j "Please don't go there, [bro].."
                b "..."
                scene bg bank23_c12ps with dissolve
                "{b}{i}Markus:{/b}{/i}\nI have an idea. The door that  leads to to corridor with the vault is highly armored and is locked with an electronic lock."
                "{b}{i}Markus:{/b}{/i}\nI could change the code from the central panel at my office thus leaving them trapped inside. There is no other exit except this one."
                v "This might work, good point.."
                b "Yeah, we will keep them like this until the police arrives.."
                "{b}{i}Markus:{/b}{/i}\nOkay, give me 15 seconds.."
                b "Hurry up, Markus.."
                scene bg bank23_c13ps with fade
                "{b}{i}Markus:{/b}{/i}\nJust a moment.. Almost there.."
                play sound ("music/sounds/lockSound.mp3")
                "{b}{i}Markus:{/b}{/i}\nDone ! Ha-ha, they are trapped inside.. How would you like this, bastards ?!"
                $ renpy.music.stop(channel=1, fadeout=5.0)
                b "Whew.. What a day.."
                v "Tell me about it.."
                j "Is it all over..?"
                b "Yes, baby.."
                v "Not exactly.. We still need to wait for the police to testify and tell them what exactly happened here.."
                b "We don't have all day for this, we are leaving, come on Julie.."
                $ renpy.music.play("music/sounds/policeSiren.mp3", channel=3, loop=True, fadein=3)
                v "They are already here.. I suggest you to cooperate and play it cool. You are a witness, not a criminal after all.. It won't take more than few hours.."
                b "Fine.. But I don't want Julie to be involved into this.. Here is some cash, little one, take the cab and go home.. I'll see you later"
                j "Okay.."
                v "Damn.. The reporters are already here.. I wonder how do they always arrive at the same time as police does.."
                jump ep5NicolePhotoshoot
            "Neutralize":
                play sound ("music/sounds/punchFace2.mp3")
                scene bg bank22_c10ps with hpunch
                b "Stay the fuck down!"
                "{b}{i}Scum:{/b}{/i}\nHu-uugckk..."
                scene black with dissolve
                play sound ("music/sounds/bodyFall.mp3")
                $ renpy.pause()
                scene bg bank23c11ps with Dissolve(1.5)
                j "Oh my god [bro] I'm so glad that you are finally here.."
                b "There-there baby.. There is nothing to worry about anymore.."
                b "Hey.."
                v "[bro].."
                b "Nice move with the distraction, thank you.. And thanks for being with Julie, I appreciate it, Vicky.."
                scene bg bank23c12ps with fade
                "{b}{i}Scum:{/b}{/i}\nOh..What the hell ?!"
                play sound ("music/sounds/kneeKick.mp3")
                scene bg bank23c12ps with vpunch
                b "Shut the fuck up! "
                "{b}{i}Scum:{/b}{/i}\n*{i}Knocked out{/i}*"
                v "[bro], we need to help evacuate the people from the building and do something about those two robbers."
                "{b}{i}Markus:{/b}{/i}\nThe police is coming, I already called them.."
                scene bg bank23_c12ps with dissolve
                v "Good, we just need to take care of those two.."
                b "Vicky, help people to leave the bank and take Julie away from here.. I'm going to kill those bastards !"
                scene bg bank23c12ps with dissolve
                j "No please, [bro].. Don't go there, don't leave me alone here.."
                b "It's okay, Julie.. I'll be right back.."
                v "I doubt it, [bro]. You won't have the surprise effect like you just had with this guy, and besides there are two of them. We need to come up with something better that just assaulting the vault, you don't want to die in vain, do you ?"
                j "Please don't go there, [bro].."
                b "..."
                scene bg bank23_c12ps with dissolve
                "{b}{i}Markus:{/b}{/i}\nI have an idea. The door that  leads to to corridor with the vault is highly armored and is locked with an electronic lock."
                "{b}{i}Markus:{/b}{/i}\nI could change the code from the central panel at my office thus leaving them trapped inside. There is no other exit except this one."
                v "This might work, good point.."
                b "Yeah, we will keep them like this until the police arrives.."
                "{b}{i}Markus:{/b}{/i}\nOkay, give me 15 seconds.."
                b "Hurry up, Markus.."
                scene bg bank23_c13ps with fade
                "{b}{i}Markus:{/b}{/i}\nJust a moment.. Almost there.."
                play sound ("music/sounds/lockSound.mp3")
                "{b}{i}Markus:{/b}{/i}\nDone ! Ha-ha, they are trapped inside.. How would you like this, bastards ?!"
                $ renpy.music.stop(channel=1, fadeout=5.0)
                b "Whew.. What a day.."
                v "Tell me about it.."
                j "Is it all over..?"
                b "Yes, baby.."
                v "Not exactly.. We still need to wait for the police to testify and tell them what exactly happened here.."
                b "We don't have all day for this, we are leaving, come on Julie.."
                $ renpy.music.play("music/sounds/policeSiren.mp3", channel=3, loop=True, fadein=3)
                v "They are already here.. I suggest you to cooperate and play it cool. You are a witness, not a criminal after all.. It won't take more than few hours.."
                b "Fine.. But I don't want Julie to be involved into this.. Here is some cash, little one, take the cab and go home.. I'll see you later"
                j "Okay.."
                v "Damn.. The reporters are already here.. I wonder how do they always arrive at the same time as police does.."
                jump ep5NicolePhotoshoot
        return

    label ep5NicolePhotoshoot:
        $ renpy.music.stop(channel=3, fadeout=3.0)
        scene black with Dissolve (2.0)
        $ renpy.notify ("Akşamın ilerleyen saatlerinde..")
        $ renpy.pause()
        b "{i}Damn, this whole interrogation process made me exhausted. Now I'm under the police supervision which kind of ties my hands together. I'm not allowed to leave the city until the end of investigation. But at least I managed to keep my new 'toy' with me."
        b "{i}Julie is already meeting with Scarlett at the cafe, I have to join them too as I promised. But I just don't feel like it right now. I need something else, something that will help me to release the tension.."
        b "{i}I guess I'll go to Nicole, she is waiting for me all day long.."
        $ renpy.pause()
        $ renpy.notify ("Bir süre sonra..")
        $ renpy.pause()
        play sound ("music/sounds/doorKnock.mp3")
        "{i}Knock-knock"
        n "Yes, come in, please.."
        play sound ("music/sounds/openDoor.mp3")
        scene bg nApt35c1ps with Dissolve (2.0)
        b "Evening, Nicole.."
        n "Hello again, [bro]. Thank you for finding the time for me, I appreciate it. I've been expecting you.."
        b "I can see that, wow. I don't recognize your apartment, it's more like a photo studio right now."
        scene bg nApt36c2ps with fade
        n "Yep, I've prepared everything beforehand, so we can go straight to business without wasting any time."
        b "I like your eagerness, Nicole."
        n "Well, I can be wild like that sometimes, ha-ha.."
        scene bg nApt36_c2ps with dissolve
        n "I'd like you to take off your clothes and take a sit over there, I just need to make final preparations.. I'll be right back.."
        b "Okay Nicole, just make it quick.."
        scene black with Dissolve (1.0)
        $ renpy.notify ("Bir an sonra..")
        $ renpy.pause()
        scene bg nApt37c3ps with Dissolve (1.5)
        $ renpy.pause()
        n "Wow.. Looking good. You are natural, [bro]! Are you sure that you didn't pose in front of the camera before ?"
        b "I'm sure.. I guess it is because a talented person is talented in a lot of things."
        n "Can't argue with that.. I like your confidence, [bro].."
        scene bg nApt38c4ps with fade
        b "Are we ready to go ?"
        n "Yes, I just can't find my camera.. Oh god what is happening to me. I always get like this when I'm nervous and.."
        b "Aroused..? Here it is, on your right on top of the table.."
        scene bg nApt38_c4ps with dissolve
        n "Right, it's exactly where I left it, silly me.."
        b "Relax, Nicole. There is nothing to worry about it, focus on your task.. By the way you are looking incredibly sexy in this light, it emphasizes your body curves and your gorgeous blue eyes.."
        scene bg nApt38c4ps with dissolve
        n "Thanks, [bro].. You are making me blush right now.."
        scene bg nApt39c5ps with fade
        n "Okay, here we go. Sit like this, don't move a muscle. I want you to give me the most sexy and masculine gaze"
        b "Fine, here.."
        n "That's perfect !"
        play sound ("music/sounds/cameraShot.mp3")
        scene bg nApt39_c6ps with cumFlash
        n "Wow.. The way you look at me right now turns me on so bad.."
        b "I'm imagining what I will do with you after we finish the photoshoot.."
        n "Mmm.. Am I standing on my knees in your imagination.. ?"
        b "Of course, like any other good girl.."
        scene bg nApt40_c8ps with fade
        n "Well, I'm willing to bring those fantasies into reality then.."
        n "Damn.. You look so masculine right now, [bro].. I'm getting turned on from your look alone.."
        play sound ("music/sounds/cameraShot.mp3")
        scene bg nApt40c7ps with cumFlash
        b "Imagine how good it would feel when I.."
        n "When you start to have your way with me.."
        b "Exactly.."
        play sound ("music/sounds/cameraShot.mp3")
        scene bg nApt40_c9ps with cumFlash
        n "I porbably couldn't take that much pleasure and orgasms.."
        b "You will have to take it like a good girl, Nicole.."
        play sound ("music/sounds/cameraShot.mp3")
        scene bg nApt41c10ps with cumFlash
        n "Oh my, it so hot.. I'm all wet down there, [bro].. I guess these photos should be enough.."
        b "Show them to me.."
        $ renpy.music.set_volume(0.25, delay=0, channel=1)
        $ renpy.music.play("music/sexyTheme.mp3", channel=1, loop=True, fadein=10)
        scene bg nApt42c11ps with fade
        n "Here, take a look.. Each one is a masterpiece.."
        b "Not bad.. I didn't know that I look that good in the photos.."
        n "That's true.. But.."
        scene bg nApt42_c11ps with Dissolve (1.0)
        n "I like it much more how you look in reality.."
        b "Show me how much you like it.."
        menu:
            "Take off the pants":
                play sound ("music/sounds/femaleGiggle.mp3")
        scene bg nApt43c12ps with fade
        n "Oh my.. I think I will never get used to the size of your cock.."
        $ renpy.pause()
        scene bg nApt43c13ps with fade
        n "It's so huge and thick.. It's definitely the biggest one I've ever seen.."
        b "Want to take a closer look?"
        menu:
            "Pull her head":
                play sound ("music/sounds/squish.mp3")
        scene bg nApt44c12ps with kissFlash
        n "{i}Mmff cough !"
        $ renpy.pause()
        b "Yeees.. Right inside your warm little mouth, baby.. That's a good girl.."
        scene bg nApt43_c12ps with Dissolve (1.0)
        n "{i}Mmm..suck-suck"
        scene bg nApt44c12ps with Dissolve (1.0)
        scene bg nApt43_c12ps with Dissolve (1.0)
        scene bg nApt44c12ps with Dissolve (1.0)
        scene bg nApt43_c12ps with Dissolve (1.0)
        b "I know you've been wanting to suck my cock all day long.. Show me how bad you want it.."
        scene bg nApt44c12ps with Dissolve (1.0)
        scene bg nApt43_c12ps with Dissolve (1.0)
        scene bg nApt44c12ps with Dissolve (1.0)
        scene bg nApt43_c12ps with Dissolve (1.0)
        n "{i}Suck-suck...Mmm...Aah.."
        b "You are sucking my dick so greedily, Nicole.. It seems like you haven't sucked one for a long time.. Come here, let me remind you what this is really like.."
        b "Take off your top and open your mouth wide.."
        scene bg nApt45_c15ps with fade
        n "{i}Mwa..gag..suck-suck.."
        $ renpy.pause()
        b "Look at me while I'm fucking your mouth with my cock, do you understand..?"
        n "{i}Muhu..Yef..suck-suck.."
        b "Good girl.."
        b "Now I'm going to shove it as deep as I can right down your throat.."
        menu:
            "Shove":
                play sound ("music/sounds/squish.mp3")
        scene bg nApt45c14ps with kissFlash
        scene bg nApt45c14ps with hpunch
        n "{i}Uek..gag-gag..cough-coguh.."
        n "{i}whi kuant..gag-gag.."
        b "Don't worry, baby.. No girl could ever take my cock all the way in her throat.."
        b "I know something that you would like, Nicole..Stick out your tongue.."
        scene bg nApt46c16ps with fade
        n "{i}Mwee..slurp-slurp.."
        scene bg nApt46_c16ps with Dissolve (1.0)
        b "Yees, baby.. Show me what you can do with your tongue.."
        scene bg nApt46c16ps with Dissolve (1.0)
        scene bg nApt46_c16ps with Dissolve (1.0)
        scene bg nApt46c16ps with Dissolve (1.0)
        scene bg nApt46_c16ps with Dissolve (1.0)
        scene bg nApt46c16ps with Dissolve (1.0)
        scene bg nApt46_c16ps with Dissolve (1.0)
        n "{i}gag-gag..slurp..suck-suck.."
        b "I know you love it.. Such a bad girl.. I'm about to cum, shit.."
        scene bg nApt46c16ps with Dissolve (1.0)
        scene bg nApt46_c16ps with Dissolve (1.0)
        scene bg nApt46c16ps with Dissolve (1.0)
        scene bg nApt46_c16ps with Dissolve (1.0)
        b "Would you like me to cum on your pretty face or inside your slutty little mouth ?"
        n "{i}suck-suck.. yo kwan do whatefer yo want fith mwe.. gag-gag..slurp"
        b "That's a right answer.. Good girl.. Oh shit I'm comming !"
        scene bg nApt46c16ps with dissolve
        scene bg nApt46_c16ps with dissolve
        scene bg nApt46c16ps with dissolve
        scene bg nApt46_c16ps with dissolve
        scene bg nApt46c16ps with dissolve
        scene bg nApt46_c16ps with dissolve
        scene bg nApt46c16ps with dissolve
        scene bg nApt46_c16ps with dissolve
        menu:
            "Cum inside":
                scene bg nApt46c16ps with cumFlash
                scene bg nApt46_c16ps with cumFlash
                scene bg nApt46c16ps with cumFlash
                b "AAAAAAAAAAAAARGH FUUUUUUUUUUUUCK"
                scene bg nApt46_c16ps with vpunch
                scene bg nApt46_c16ps with vpunch
                scene bg nApt46_c16ps with vpunch
                scene bg nApt47_c17ps with cumFlashLong
                b "Fuck, baby.."
                n "{i}{b}Heavy breathing{/b}{/i}\nAha, hah, hu.. yummy, [bro].. Every single drop is inside of me.."
                b "That's my girl.."
                $ renpy.pause()
                $ renpy.music.stop(channel=1, fadeout=3.0)
                jump episode6
                #jump supportMe
            "Cum on her face":
                scene bg nApt46c16ps with cumFlash
                scene bg nApt46_c16ps with cumFlash
                scene bg nApt46c16ps with cumFlash
                b "AAAAAAAAAAAAARGH FUUUUUUUUUUUUCK"
                scene bg nApt46_c16ps with vpunch
                scene bg nApt46_c16ps with vpunch
                scene bg nApt46_c16ps with vpunch
                scene bg nApt47c17ps with cumFlashLong
                b "Shit, baby.."
                n "Mweeh, ha-ha.. It's feels so good on my face, it is so hot.. You should cum on my face more often, [bro]..."
                b "I will, baby.."
                $ renpy.pause()
                $ renpy.music.stop(channel=1, fadeout=3.0)
                jump episode6
                #jump supportMe
        return

####################################################EPISODE_6##################################################

    image bg atHome134c1ps = "images/ep6/atHome134c1ps.png"
    image bg atHome135c4ps = "images/ep6/atHome135c4ps.png"
    image bg atHome135c5ps = "images/ep6/atHome135c5ps.png"
    image bg atHome136_c12ps = "images/ep6/atHome136_c12ps.png"
    image bg atHome136c6ps = "images/ep6/atHome136c6ps.png"
    image bg atHome136c8ps = "images/ep6/atHome136c8ps.png"
    image bg atHome136c9ps = "images/ep6/atHome136c9ps.png"
    image bg atHome136c11ps = "images/ep6/atHome136c11ps.png"
    image bg atHome136c12ps = "images/ep6/atHome136c12ps.png"
    image bg atHome137___c18ps = "images/ep6/atHome137___c18ps.png"
    image bg atHome137__c14ps = "images/ep6/atHome137__c14ps.png"
    image bg atHome137_c14ps = "images/ep6/atHome137_c14ps.png"
    image bg atHome137_c12ps = "images/ep6/atHome137_c12ps.png"
    image bg atHome137c13ps = "images/ep6/atHome137c13ps.png"
    image bg atHome138_1c16ps = "images/ep6/atHome138_1c16ps.png"
    image bg atHome138_c15ps = "images/ep6/atHome138_c15ps.png"
    image bg atHome138c15ps = "images/ep6/atHome138c15ps.png"
    image bg atHome138c16ps = "images/ep6/atHome138c16ps.png"
    image bg atHome139c18ps = "images/ep6/atHome139c18ps.png"
    image bg atHome140c19ps = "images/ep6/atHome140c19ps.png"
    image bg atHome140_c19ps = "images/ep6/atHome140_c19ps.png"
    image bg atHome140_1c19ps = "images/ep6/atHome140_1c19ps.png"
    image bg atHome140_2c19ps = "images/ep6/atHome140_2c19ps.png"
    image bg atHome141c3ps = "images/ep6/atHome141c3ps.png"

    image bg badGuys1c3_1ps = "images/ep6/badGuys1c3_1ps.png"
    image bg badGuys1c3_ps = "images/ep6/badGuys1c3_ps.png"
    image bg badGuys1c3ps = "images/ep6/badGuys1c3ps.png"
    image bg badGuys2c3_ps = "images/ep6/badGuys2c3_ps.png"
    image bg badGuys2c3ps = "images/ep6/badGuys2c3ps.png"

    image bg cafe8c1ps = "images/ep6/cafe8c1ps.png"
    image bg cafe9c3ps = "images/ep6/cafe9c3ps.png"
    image bg cafe10c2ps = "images/ep6/cafe10c2ps.png"
    image bg cafe11c3ps = "images/ep6/cafe11c3ps.png"
    image bg cafe12c4ps = "images/ep6/cafe12c4ps.png"
    image bg cafe13c5ps = "images/ep6/cafe13c5ps.png"
    image bg cafe14c6__ps = "images/ep6/cafe14c6__ps.png"
    image bg cafe14c6_ps = "images/ep6/cafe14c6_ps.png"
    image bg cafe14c6ps = "images/ep6/cafe14c6ps.png"
    image bg cafe15c6__ps = "images/ep6/cafe15c6__ps.png"
    image bg cafe15c6_ps = "images/ep6/cafe15c6_ps.png"
    image bg cafe15c6ps = "images/ep6/cafe15c6ps.png"
    image bg cafe16c7ps = "images/ep6/cafe16c7ps.png"
    image bg cafe17c6ps = "images/ep6/cafe17c6ps.png"
    image bg cafe18c7ps = "images/ep6/cafe18c7ps.png"
    image bg cafe19c7ps = "images/ep6/cafe19c7ps.png"
    image bg cafe20c7ps = "images/ep6/cafe20c7ps.png"
    image bg cafe21_c7ps = "images/ep6/cafe21_c7ps.png"
    image bg cafe21c7ps = "images/ep6/cafe21c7ps.png"
    image bg cafe22c7ps = "images/ep6/cafe22c7ps.png"
    image bg cafe23c7ps = "images/ep6/cafe23c7ps.png"
    image bg cafe24_c8ps = "images/ep6/cafe24_c8ps.png"
    image bg cafe24c7ps = "images/ep6/cafe24c7ps.png"
    image bg cafe25c8ps = "images/ep6/cafe25c8ps.png"
    image bg cafe26c9ps = "images/ep6/cafe26c9ps.png"

    image bg cafer1_c24ps = "images/ep6/cafer1_c24ps.png"
    image bg cafer1c24ps = "images/ep6/cafer1c24ps.png"
    image bg cafer2c25ps = "images/ep6/cafer2c25ps.png"
    image bg cafer3c27ps = "images/ep6/cafer3c27ps.png"
    image bg cafer3c28ps = "images/ep6/cafer3c28ps.png"
    image bg cafer4_c13ps = "images/ep6/cafer4_c13ps.png"
    image bg cafer4c12ps = "images/ep6/cafer4c12ps.png"
    image bg cafer5c13ps = "images/ep6/cafer5c13ps.png"
    image bg cafer6_c17ps = "images/ep6/cafer6_c17ps.png"
    image bg cafer6c15ps = "images/ep6/cafer6c15ps.png"
    image bg cafer7c15ps = "images/ep6/cafer7c15ps.png"
    image bg cafer8_c17_ps = "images/ep6/cafer8_c17_ps.png"
    image bg cafer8_c17ps = "images/ep6/cafer8_c17ps.png"
    image bg cafer8c17_ps = "images/ep6/cafer8c17_ps.png"
    image bg cafer8c17ps = "images/ep6/cafer8c17ps.png"
    image bg cafer9c17_ps = "images/ep6/cafer9c17_ps.png"
    image bg cafer9c17ps = "images/ep6/cafer9c17ps.png"
    image bg cafer10_c19ps = "images/ep6/cafer10_c19ps.png"
    image bg cafer10c18ps = "images/ep6/cafer10c18ps.png"

    image bg pstation1c12ps = "images/ep6/pstation1c12ps.png"
    image bg pstation2c1ps = "images/ep6/pstation2c1ps.png"
    image bg pstation2c2ps = "images/ep6/pstation2c2ps.png"
    image bg pstation3_c3_ps = "images/ep6/pstation3_c3_ps.png"
    image bg pstation3_c3ps = "images/ep6/pstation3_c3ps.png"
    image bg pstation3c3_ps = "images/ep6/pstation3c3_ps.png"
    image bg pstation3c3ps = "images/ep6/pstation3c3ps.png"
    image bg pstation4_c3ps = "images/ep6/pstation4_c3ps.png"
    image bg pstation4c3ps = "images/ep6/pstation4c3ps.png"
    image bg pstation5_c3ps = "images/ep6/pstation5_c3ps.png"
    image bg pstation5c3ps = "images/ep6/pstation5c3ps.png"
    image bg pstation6_c3ps = "images/ep6/pstation6_c3ps.png"
    image bg pstation6c3ps = "images/ep6/pstation6c3ps.png"
    image bg pstation7c4ps = "images/ep6/pstation7c4ps.png"
    image bg pstation8c3ps = "images/ep6/pstation8c3ps.png"
    image bg pstation8_c4ps = "images/ep6/pstation8_c4ps.png"
    image bg pstation8c2ps = "images/ep6/pstation8c2ps.png"
    image bg pstation9_c2ps = "images/ep6/pstation9_c2ps.png"
    image bg pstation9_c5ps = "images/ep6/pstation9_c5ps.png"
    image bg pstation9c5ps = "images/ep6/pstation9c5ps.png"

    image bg vApt1c3ps = "images/ep6/vApt1c3ps.png"
    image bg vApt2_c_1ps = "images/ep6/vApt2_c_1ps.png"
    image bg vApt2_c1ps = "images/ep6/vApt2_c1ps.png"
    image bg vApt2c1ps = "images/ep6/vApt2c1ps.png"
    image bg vApt3_c1ps = "images/ep6/vApt3_c1ps.png"
    image bg vApt3c1ps = "images/ep6/vApt3c1ps.png"
    image bg vApt4c2ps = "images/ep6/vApt4c2ps.png"
    image bg vApt5_a_c4ps = "images/ep6/vApt5_a_c4ps.png"
    image bg vApt5_ac4ps = "images/ep6/vApt5_ac4ps.png"
    image bg vApt5_c4ps = "images/ep6/vApt5_c4ps.png"
    image bg vApt5c2ps = "images/ep6/vApt5c2ps.png"
    image bg vApt6c6ps = "images/ep6/vApt6c6ps.png"
    image bg vApt7c7ps = "images/ep6/vApt7c7ps.png"
    image bg vApt8_c8ps = "images/ep6/vApt8_c8ps.png"
    image bg vApt8_c10ps = "images/ep6/vApt8_c10ps.png"
    image bg vApt8c8ps = "images/ep6/vApt8c8ps.png"
    image bg vApt8c10ps = "images/ep6/vApt8c10ps.png"
    image bg vApt8f_c9ps = "images/ep6/vApt8f_c9ps.png"
    image bg vApt8fc9ps = "images/ep6/vApt8fc9ps.png"
    image bg vApt9_a_c7ps = "images/ep6/vApt9_a_c7ps.png"
    image bg vApt9_ac7_ps = "images/ep6/vApt9_ac7_ps.png"
    image bg vApt9_ac7ps = "images/ep6/vApt9_ac7ps.png"
    image bg vApt9_c7ps = "images/ep6/vApt9_c7ps.png"
    image bg vApt9_c10ps = "images/ep6/vApt9_c10ps.png"
    image bg vApt9c10ps = "images/ep6/vApt9c10ps.png"
    image bg vApt9fc9ps = "images/ep6/vApt9fc9ps.png"
    image bg vApt10_c10ps = "images/ep6/vApt10_c10ps.png"
    image bg vApt10c10ps = "images/ep6/vApt10c10ps.png"
    image bg vApt11_c8ps = "images/ep6/vApt11_c8ps.png"
    image bg vApt11c7ps = "images/ep6/vApt11c7ps.png"
    image bg vApt11c8ps = "images/ep6/vApt11c8ps.png"
    image bg vApt11c10ps = "images/ep6/vApt11c10ps.png"
    image bg vApt11fc9ps = "images/ep6/vApt11fc9ps.png"
    image bg vApt12c7ps = "images/ep6/vApt12c7ps.png"
    image bg vApt13c1ps = "images/ep6/vApt13c1ps.png"
    image bg vApt13c2ps = "images/ep6/vApt13c2ps.png"
    image bg vApt14c2ps = "images/ep6/vApt14c2ps.png"
    image bg vApt15c7ps = "images/ep6/vApt15c7ps.png"

    label episode6:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Şehirde bir yerde..")
        $ renpy.pause()
        $ renpy.music.set_volume(1, delay=0, channel=3)
        $ renpy.music.play("music/nightmareTheme.mp3", channel=3, loop=True, fadein=3)
        scene bg badGuys1c3ps with Dissolve (3.0)
        "{b}TV:{/b}\n{i}Today's robbery in broad daylight became the most resonant event in our city for the last few years"
        nacho "Check this out, it's about our guys"
        rocco "..."
        "{b}TV:{/b}\n{i}Our correspondents were the first at the place and had a chance to talk to the man who played a main role in preventing the crime. Here is the short video of what happened just few hours ago."
        "{b}Reporter:{/b}\n{i}Sir, please say a few words to our audience ! How does it feel to be a 'savior' ? What made you do that ?"
        b "{i}No comments or interviews, sorry"
        scene bg badGuys1c3_ps with dissolve
        nacho "Wait a second.."
        "{b}Reporter:{/b}\n{i}But people should know their hero by sight, don't turn your back on them !"
        "{b}Police officer:{/b}\n{i}Hey, leave him alone ! It's police business now."
        scene bg badGuys1c3ps with dissolve
        nacho "His face looks familiar.."
        "{b}TV:{/b}\n{i}Unfortunately that's all the information that we are allowed to disclose for now due to the police investigation."
        "{b}TV:{/b}\n{i}We are reminding you that today group of four people tried to rob the commercial bank that belongs to the infamous businessman and entrepreneur..."
        scene bg badGuys1c3_ps with dissolve
        nacho "Yes that is him, I remembered !"
        scene bg badGuys2c3_ps with dissolve
        nacho "I know this punk !"
        rocco "Tell me everything you know about him"
        nacho "Well.. It's not like I fucking know him, I just saw this punk the other day.."
        "{b}TV:{/b}\n{i}...reportedly of $500 million total in the vault..."
        scene bg badGuys1c3_1ps with dissolve
        nacho "What was his name.. Shit.. "
        "{b}TV:{/b}\n{i}...good to know that the world is full of good people like ours hero of the day. My name is Marie, 216 channel. Thanks for watching."
        scene bg badGuys2c3_ps with dissolve
        nacho "[bro]! That's it, one bitch said his name when I was going to buy some stuff for myself at the store"
        if ep3NachoBeaten == 1:
            nacho "This motherfucker actually kicked the shit out of me, I have to admit. He used the element of surprise and I wasn't ready at that moment, but it wouldn't have happened if you had given me that thing.."
            rocco "I'm not authorized to help you with this. Talk to the Boss about the procedure."
        else:
            nacho "I was going to bang some hot chick but this whiny little bitch showed up and started crying out this 'I'll call the police' shit.."
            rocco "It's not the first time you got distracted during the assignment. Boss would be displeased with it."
        nacho "I don't recognize you pal, you became completely other man after you.."
        rocco "I want you to find out who exactly this man is. I suggest you to use the store as a start point of searching, there is a chance that this man lives nearby that area."
        scene bg badGuys2c3ps with dissolve
        nacho "Okay but how am I supposed to.."
        rocco "Contact with our man from the bank"
        scene bg badGuys2c3_ps with dissolve
        nacho "..."
        rocco "He might be able to provide us other useful information apart from bank's alarm system. Ask him to check the database of all clients with name [bro] whose residental adress corresponds to the store neighborhood."
        nacho "Hm, this might work I guess.. I hope this punk has an account at the bank and our guy knows who that bitch is, it would be so much easier for us.."
        rocco "Most likely our target has some values at the bank, otherwise it would be unreasonable for him to risk the life and interfere the robbery. Unless he had some other reasons to act."
        rocco "Police probably retrieved the video data of the robbery for the investigation, but you must get the copy of it as soon as possilbe, boss demands full report."
        nacho "Alright, alright.. Damn.. Although it's not our fault, I have a feeling that boss is fucking mad right now. Hey, what about our so-called 'secret agent' ? If it was up to me, I would already use this option. Maybe now is the best time to make a move ?"
        rocco "Later. Everything needs to look believable in order to work as planned. Now get back to work."
        $ renpy.music.stop(channel=3, fadeout=3)
        $ renpy.pause()
        jump ep6cafe
        return

    label ep6cafe:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra Kafe'de..")
        $ renpy.pause()
        scene bg cafe8c1ps with Dissolve (2.0)
        j "Babe, your coffee is getting cold.. What took you so long ?"
        s "Relax honey, I was checking out the restroom. They are comfy enough, if you know what I mean."
        scene bg cafe9c3ps with fade
        j "Ooh, that sounds interesting.. You do know how I am gettig turned on about this idea.."
        s "You are so naughty, babe.. How many times have you been thinking about being fucked in a public place ?"
        j "Too many, I'm afraid I lost the count.."
        s "Good girl.. You don't have to dream about it any longer, because I'm here.. Let's go, honey"
        j "Come on, babe. You know we can't do this right now, [bro] is about to come."
        s "You're breaking my heart, sweetie.."
        scene bg cafe11c3ps with dissolve
        j "There he is. {b}Over here, [bro].{/b} Please Scarlett, be nice to him. I want you two to get along well together"
        scene bg cafe10c2ps with fade
        s "Don't worry Julie, I won't torture your [brother]. I want to be a part of your lovely family... \nHowever I have to admit, that I can't wait to see how {i}big{/i} your [brother] really is.."
        j "Stop it Scarlett ! You such a minx, you know that ?"
        $ renpy.music.set_volume(1, delay=0, channel=3)
        $ renpy.music.play("music/scarlettTheme.mp3", channel=3, loop=True, fadein=0)
        scene bg cafe12c4ps with Fade(0.25, 0.5, 3.0)
        s "Hi there.."
        b "Hello girls, hope you did not miss me too much"
        j "Ha-ha, no [bro], not too much, just a bit."
        s "Now I know what we've been missing all this time.."
        j "[bro], meet my girlfirend Scarlett, babe - this is my [brother] [bro]"
        b "Nice to meet you Scarlett. Julie's told me a lot about you. "
        scene bg cafe13c5ps with fade
        s "Oh, [bro].. A pleasure is all mine. I don't know why but Julie never mentioned that she has such a handsome [brother].."
        b "Thank you, Scarlett.. I have a strange feeling that I know you. Have we met somewhere before ?"
        $ renpy.pause()
        s "Hm.. Maybe it was in another life where I was a little princess and you.. were a king..? But I would definitely remember your face so that is impossible."
        j "Hey guys, are you going to stand there all night long or you will finally take a seat ?"
        b "Good idea, please, after you Scarlett.."
        scene bg cafe14c6_ps with fade
        b "Is it just me or you girls have the exact same haircut ?"
        j "Yes, you are right [bro]. I've made the same haircut as Scarlett has 'cause I wanted us to look more like sisters.."
        scene bg cafe14c6__ps with dissolve
        j "Isn't that cute, [bro] ? Me and Scarlett almost look like twins, right ?"
        b "Sure, you two are pretty good looking girls"
        s "Or I would say two sexy hot as hell heartbreakers.."
        scene bg cafe15c6__ps with dissolve
        b "Agree"
        s "I wouldn't mind be your little sl..sister, [bro].."
        scene bg cafe14c6ps with dissolve
        j "Scarlett !"
        scene bg cafe15c6_ps with dissolve
        s "What ?! I think it would be awesome, I would be your older sister and [bro] would be our brother or maybe even our daddy.. We would all live together and..would take care of each other"
        s "Just imagine how fun it would be.. [bro] would protect us just like he did today at the bank, and we would do our best to make him happy.."
        b "{i}Huh ?! Where is it coming from ?!"
        scene bg cafe15c6ps with dissolve
        j "Speaking about bank situation, I'm still a bit scared of that nightmare.. What happened there after I leaved the bank ? Did police catch two other guys ?"
        scene bg cafe14c6_ps with dissolve
        b "Actually there was one more guy outside, their driver, but cops got all of them eventually."
        j "That's good to know. I hope those bastards will get what they deserve.. By the way what happened with Vicky, is she okay ?"
        scene bg cafe15c6_ps with dissolve
        s "Who is Vicky ?"
        j "She's [bro]'s girlfriend and my friend"
        b "No, she is not.."
        scene bg cafe16c7ps with fade
        s "Wait a second, I'm a bit confused, she is not the girlfriend or she is not the friend ?"
        b "She is neither"
        j "She is my friend and it's not my fault that you two can't get along together, I like her !"
        s "So whose girlfriend that Vicky is ?"
        b "You don't know her at all, Julie. Vicky is completely other person than you think she is."
        scene bg cafe17c6ps with fade
        j "Come on [bro], you are making things up right now. I love you and know that it's not my business, but please don't make me lose my friend only because you and Nicole suddenly fell in love with each other."
        s "Who is Nicole..?"
        scene bg cafe15c6_ps with dissolve
        j "Looks like she is [bro]'s new girlfriend"
        scene bg cafe18c7ps with fade
        $ renpy.pause()
        s "Wow it looks like [bro] is quite in demand among the women, aren't you ?"
        b "It's complicated.. Anyway me and Vicky testified about what happened at the bank also police asked other witnesses of the robbery. But it took us way longer than others because we had to explain the police why we had the weapon."
        j "Well, Vicky had to get armed with one of the scum's weapon, but where you found a gun for yourself is still a mystery to me.."
        scene bg cafe23c7ps with fade
        s "Really ? So you have a personal gun [bro] ?"
        b "Well.. I do"
        scene bg cafe24c7ps with dissolve
        b "{i}What the..?!"
        s "I bet it's a big gun that you have.. Would you show it to me ?"
        j "Oh yeah, it seemed really huge to me.."
        s "So, you've already shown your big gun to your little [sis], that's interesting.."
        if ep5killCounter == 1:
            j "Unfortunatelly [bro] had to use it, 'cause the scums were going to take me and Vicky with them and rape us.."
            s "Oh, I'm so sorry sweetie.. Good thing that didn't happen thanks to [bro].."
        else:
            j "Actually [bro] didn't even had to use it, he kicked the shit out of the scum with his bare hands.."
            s "That is a right decision, because one needs to use big gun wisely. It doesn't make sense just swinging it around mindlessly and point it at everybody.."
        scene bg cafe19c7ps with fade
        j "Right, I'm just happy that it all eventually ended up good for us. You are my hero, [bro].."
        b "Don't mention it [sis], I would.."
        scene bg cafe25c8ps with vpunch
        b "Ghrm.. I would do anything to protect you..{i}What the hek..?!"
        j "I know [bro].. Ah.. Mm.. Love you.."
        s "Oh, that is so sweet.. You know what ? I would really want to take your gun in my hands right now [bro].. I've never held the gun in my entire life, especially huge one.. Give it to me, [bro].."
        b "{i}Damn, she is talking about my dick so explicitly.. What a naughty girl.."
        s "I can feel it in your pants.."
        j "Ahm, guys.. Let's change the subject, shall we.. ? Oh.."
        scene bg cafe20c7ps with fade
        $ renpy.pause()
        j "I.. I think that whatever happened in the past should remain there, especially if it's.."
        s "As you say Julie, we won't {i}stir up{/i} the past from now on.."
        scene bg cafe26c9ps with fade
        j "Mhm-am.. Thanks.."
        b "{i}I wonder if Julie noticed that her girlfriend is touching my dick with her foot right now.."
        s "So [bro], what are you doing in the life besides taking care of our little Julie..?"
        b "Can't tell you that Scarlett, because I will have to deal with you after that"
        scene bg cafe20c7ps with fade
        s "Oh, I would mind actually.."
        j "Oh, ha-ha.. Right, [bro] is a top secret spy, I told you that.. He never talks about his job.."
        s "I know few tricks that will help me to persuade him and share this information.."
        $ renpy.pause()
        "{i}{b}PHONE RINGING"
        $ renpy.music.stop(channel=3, fadeout=5)
        scene bg cafe24_c8ps with vpunch
        b "{i}Huh, hidden number ? Who is this ?"
        s "Is everything okay, [bro] ?"
        scene bg cafe20c7ps with fade
        b "Yes, absolutely, I just need to answer the call, excuse me."
        j "Come.. back soon, okay ?"
        b "Sure, honey. I'll be right back. {i}My phone's number is known to a very few people, so it's definitely not a robocall or some telemarketing shit that tries to sell me 'magic pills'"
        jump ep6cafer
        return

    label ep6cafer:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Bir an sonra..")
        $ renpy.pause()
        scene bg cafer2c25ps with dissolve
        b "Yes, who is this ?"
        "{b}{i}Phone call:{/b}{/i}\nEvening, [bro]. This is detective White, from metropolitan police department. I'm calling you due to the investigation of today's incident at the bank. I would like to ask you a few questions."
        b "Ahm, actually I don't know what else I can tell about the robbery. I mean I already testified to the one of police officers."
        scene bg cafer3c28ps with fade
        "{b}{i}Det. White:{/b}{/i}\nWe appreciate your help and cooperation, however now the circumstances have changed and our investigation needs additional information that you can provide, of course if you do not refuse to."
        b "Of course not, I'm not refusing to help you detective."
        scene bg cafer3c27ps with fade
        b "How can I help you, what exactly you would like to know ?"
        "{b}{i}Det. White:{/b}{/i}\nActually it's not something that we will discuss on a phone as you might guess, [bro]. I want you to come to the police station as soon as possible."
        b "What ?"
        $ renpy.music.play("music/scarlettTheme.mp3", channel=3, loop=True, fadein=0)
        scene bg cafer4_c13ps with hpunch
        $ renpy.pause()
        s "Hush.."
        b "No, detective I can't.. Not right now, please.. Is it really necessary ?"
        scene bg cafer5c13ps with fade
        s "Relax, handsome.. You are so stressed out.. I'm gonna help you with that, [bro].."
        "{b}{i}Det. White:{/b}{/i}\nI can assure you, it won't take much time. The only reason I need your direct presence is because the procedure requires the video record for the interrogation protocol."
        b "I understand but why this whole procedure can't be done later, tomorrow at the morning for example ?"
        scene bg cafer4c12ps with fade
        s "Nah.. Tomorrow at this time I will be helping you with your 'morning wood', honey.."
        b "Oh, shit.."
        "{b}{i}Det. White:{/b}{/i}\nTomorrow is too late, because during the analysis of the video record from the bank.."
        scene bg cafer6_c17ps with fade
        $ renpy.pause()
        s "[bro] I can feel it's getting harder, oh my.."
        b "Damn.. So, detective, you've found something important on that records, right ?"
        "{b}{i}Det. White:{/b}{/i}\nAre you here ? I have a feeling that you're not listening to me, [bro]."
        b "Ahm, sorry, there is probably something wrong with the connection, could you repeat your last few words please ?"
        play sound "music/sounds/jeansZipper.mp3"
        scene bg cafer7c15ps with fade
        play sound "music/sounds/femaleGasps.mp3"
        s "Oh my god, [bro].. It's huge, I've never seen one that big.."
        scene bg cafer6c15ps with dissolve
        $ renpy.pause()
        "{b}{i}Det. White:{/b}{/i}\nIt's not a joke, [bro]. The situation is far more serious than it seems, the security cameras captured interesting details that you decided to omit for some reason in your testifications.."
        b "I don't know what you're talking about, detective.."
        s "Actually I'm a bit jealous right now.. Julie is so lucky with you.. "
        scene bg cafer1c24ps with fade
        s "I wish you were my [brother], [bro].."
        scene bg cafer1_c24ps with dissolve
        s "I would be fucking with you every single minute.."
        "{i}Scarlett tightens the grip.."
        scene bg cafer1_c24ps with hpunch
        b "Oh, fuck, babe.."
        scene bg cafer1c24ps with dissolve
        scene bg cafer1_c24ps with dissolve
        scene bg cafer1c24ps with dissolve
        scene bg cafer1_c24ps with dissolve
        b "Just like that, Scarlett.."
        scene bg cafer1c24ps with dissolve
        scene bg cafer1_c24ps with dissolve
        scene bg cafer1c24ps with dissolve
        scene bg cafer1_c24ps with dissolve
        scene bg cafer8c17ps with fade
        "{b}{i}Det. White:{/b}{/i}\n...so this newly discovered circumstance allows me to change your current status in this case from 'witness' to something different. That is why I highly recommend you.."
        scene bg cafer8c17_ps with dissolve
        b "You are trying to tell me that now I'm a criminal ?"
        scene bg cafer8c17ps with dissolve
        scene bg cafer8c17_ps with dissolve
        scene bg cafer8c17ps with dissolve
        scene bg cafer8_c17_ps with dissolve
        s "Oh, that is so hot.. I'm stroking the bad guy's cock in the public place right now.."
        scene bg cafer8c17_ps with dissolve
        scene bg cafer8c17ps with dissolve
        s "It turns me on so bad.. This cock is even more desirable for me now.. I want to wrap my soft lips around it"
        "{b}{i}Det. White:{/b}{/i}\n'Suspect' is more correct word to use. Until your guilt is proven in the court.."
        scene bg cafer8_c17_ps with dissolve
        s "I wonder how your hot sperm would taste like.."
        b "Oh, yes, babe.. Ahm.. Wait, what ?"
        scene bg cafer8_c17ps with dissolve
        scene bg cafer8_c17_ps with dissolve
        scene bg cafer8_c17ps with dissolve
        scene bg cafer8_c17_ps with dissolve
        scene bg cafer8_c17ps with dissolve
        "{b}{i}Det. White:{/b}{/i}\nYour current status in this case will be changed to 'suspect' if you are not at the police station in 30 minutes.."
        s "Does the fact that somebody may come in right now exites you ? They would see how greedily I'm stroking your massive pulsating cock.. What do you think they would say to us..?"
        scene bg cafer8_c17_ps with dissolve
        scene bg cafer8_c17ps with dissolve
        scene bg cafer8_c17_ps with dissolve
        scene bg cafer8_c17ps with dissolve
        b "Holy fuck.."
        "{b}{i}Det. White:{/b}{/i}\nYou can be sure that it won't take me too much time to convince the attorney in giving me the order for your detention in case your refusal of cooperation."
        scene bg cafer1c24ps with fade
        scene bg cafer1_c24ps with dissolve
        scene bg cafer1c24ps with dissolve
        scene bg cafer1_c24ps with dissolve
        scene bg cafer1c24ps with dissolve
        scene bg cafer1_c24ps with dissolve
        scene bg cafer1c24ps with dissolve
        scene bg cafer1_c24ps with dissolve
        scene bg cafer8c17ps with fade
        s "I don't even know if I will be able to put this huge and thick cock in my warm slutty mouth.."
        b "Shit.. Wait detective, I'm not refusing I'll be at the station shortly. How can I find you there ?"
        scene bg cafer8_c17_ps with dissolve
        scene bg cafer8_c17ps with dissolve
        scene bg cafer8_c17_ps with dissolve
        scene bg cafer8_c17ps with dissolve
        scene bg cafer8_c17_ps with dissolve
        scene bg cafer8_c17ps with dissolve
        scene bg cafer8_c17_ps with dissolve
        scene bg cafer8_c17ps with dissolve
        s "My tight little butthole probably won't take your cock from the begining either.. You will have to stretch it out really good.. I know it will be painfull but I promise that I'll take it like a good girl, [bro]"
        b "Oh, shit, I think I'm about to come right now !"
        "{b}{i}Det. White:{/b}{/i}\nThat's good to know. You could ask any officer in the building to guide you to detective White so it shouldn't be a problem for you to find me."
        scene bg cafer8_c17_ps with dissolve
        scene bg cafer8_c17ps with dissolve
        scene bg cafer8_c17_ps with dissolve
        scene bg cafer8_c17ps with dissolve
        s "After you stretch out my tight little asshole I want you to shove your big cock balls deep and cum right inside my sweet and wet little pussy !"
        b "Oh fuck, Scarlett !"
        "{b}{i}Det. White:{/b}{/i}\nI beg you a pardon ?"
        scene bg cafer1c24ps with fade
        scene bg cafer1_c24ps with dissolve
        scene bg cafer1c24ps with dissolve
        scene bg cafer1_c24ps with dissolve
        scene bg cafer1c24ps with dissolve
        scene bg cafer1_c24ps with dissolve
        b "I'm comming, almost there !"
        scene bg cafer9c17ps with fade
        s "Oops.. This is a men's restroom, isn't it ?"
        scene bg cafer9c17_ps with hpunch
        b "What ?! Why did you stop ?!"
        s "Oh, silly me, I always take a wrong door.."
        b "Are you fucking serious ?!"
        "{b}{i}Det. White:{/b}{/i}\nHey, watch your language !"
        scene bg cafer10_c19ps with fade
        b "I'm sorry, detective, I wasn't talking to you.."
        "{b}{i}Det. White:{/b}{/i}\nI'm waiting for you at the station for one more hour, after that your status will be changed wich means no good for you. {b}{i}\nEnd of the call"
        b "What the fuck was that, Scarlett ?"
        s "It was a little greeting handshake, [bro]. Looks like you have to be somewhere else so, see you later, big guy.."
        scene bg cafer10c18ps with fade
        s "Well, now I need to find a women's restroom, excuse me.."
        s "Oh, and of course.. It was really nice to meet you.. \nBoth of you.. Can't wait to see you again.."
        b "Un-fucking-believable..."
        $ renpy.music.stop(channel=3, fadeout=5)
        $ renpy.pause()
        scene black with Dissolve (2.0)
        $ renpy.notify ("Bir an sonra..")
        $ renpy.pause()
        scene bg cafe21_c7ps with dissolve
        $ renpy.pause()
        j "What's up, [bro] ? Is everything okay ?"
        b "Yeah, Julie.. It was the call from detective, I need to go to the police station right now to clarify some details for the investigation. I'm afraid I can't give you and Scarlett a ride to home because I don't know how long it will take, here is some cash for the taxi."
        scene bg cafe21c7ps with dissolve
        j "Oh, that is bad.. I hope it's nothing serious.."
        if ep5killCounter == 1:
            j "Maybe they want to talk because you killed one of those scums.."
        b "I'll find this out soon anyway. It's already late outside, I don't want you girls to stay here too long, promise that you won't sit here all night long"
        scene bg cafe21_c7ps with dissolve
        j "Sure we won't, [bro]. I'll call a cab as soon as Scarlett comes back."
        scene bg cafe22c7ps with dissolve
        j "She went to the restroom shortly after you did.. Have you seen her by any chance ?"
        b "Ahm.. I saw her looking for the women's toilet"
        scene bg cafe21_c7ps with dissolve
        j "That is really strange, she already used a restroom few times while we are sitting at this cafe.."
        b "There is nothing strange about it, Julie.. I mean, maybe she drinks a lot of water, who knows ?!"
        j "Ha-ha, right, that can be the case"
        b "Anyway, tell Scarlett that it was really nice to meet her. Sorry again that I have to go so quickly, I would definitely spend more time with two of you, girls."
        j "It's okay, [bro] I understand everything. I'm sure that Scarlett liked you too, usually she is very hostile to my friends, especially to the boys but looks like you are lucky, ha-ha"
        b "Oh yeah, I noticed.. Have a nice rest of the day, [sis]. See you later"
        j "Bye, [bro]."
        j "Oh, almost forgot, I wanted to ask if it's okay for Scarlett to stay at our place for the night ?"
        b "What a [brother] I would be if I said 'no' ?! Of course she can stay, Julie.."
        j "Yay, you are the best, [bro]. Love you !"
        b "Love you too, Julie.. Bye"
        jump ep6pstation
        return

    label ep6pstation:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra Karakolda..")
        $ renpy.pause()
        scene bg pstation1c12ps with Dissolve (2.0)
        b "{i}I'd never have thought that I will have to cooperate with the police. What if coordinator or someone from the gang will know about me working with the police ?! I've always tried working carefully and clean leaving no traces."
        b "{i}Today was an exceptional case, it's all because of Julie. I couldn't let that bastard hurt her, I just won't forgive myself if something bad happens to her especially because of me."
        b "{i}I don't think that police really found something solid against me, they are probably just bluffing. Otherwise I'd already be behind the bars. Damn, this whole situation is getting worse and worse with each day. First this conflict between the gangs, then the traitors factor. Now the police gets involved."
        b "{i}Being shot, betrayed or arrested doesn't sound good at all, yet everything comes down to it more and more with each day. I don't know how I'm going to handle all this madness alone. If I only have something that can help me with it...or someone..."
        $ renpy.pause()
        menu:
            "Enter the building":
                b "{i}Let's see what they found out about me..."
        scene black with Dissolve (2.0)
        $ renpy.notify ("Bir an sonra..")
        $ renpy.pause()
        scene bg pstation2c1ps with Dissolve (2.0)
        "{b}{i}Det. White:{/b}{/i}\nAt last, the second witness decided to honor us with his presence."
        b "Greetings detective, it's nice to meet.."
        "{b}{i}Det. White:{/b}{/i}\nYeah-yeah, leave that all formal bullshit behind the doors and come inside"
        "{b}{i}Det. White:{/b}{/i}\nOf course you are welcome to make yourself at home, [bro]."
        b "Thanks god we won't be playing the 'Good cop, Bad cop' routine right now. Just the 'Bad cop' will be enough I believe."
        "{b}{i}Det. White:{/b}{/i}\n[bro], iyi bir ruh halinde olmana sevindim. Bunu görüşmemizin sonuna kadar saklayabilecek misin göreceğiz ama şimdilik senden 'saçmalamayı kesmeni' ve yerine oturmanı öneriyorum."
        b "Okay detective, you are the boss here.."
        scene bg pstation2c2ps with fade
        v "Hi [bro]..."
        $ renpy.pause()
        b "Vicky..? What are you doing here ?"
        v "I.."
        "{b}{i}Det. White:{/b}{/i}\nI already tired to repeat telling this to everyone, but it's {b}ME{/b} who asks the questions here."
        scene bg pstation3_c3_ps with fade
        "{b}{i}Det. White:{/b}{/i}\nThis is not a date or 'How are you doing' interests club. It's witnesses confrontation because your testifications regarding the case are quite contradictory. That's why I want to understand which one of you two is lying and where the truth is."
        "{b}{i}Det. White:{/b}{/i}\nDon't get me wrong, I'm impressed by your courage and civil liability. But over the years of my service at the police I've never faced with such people who had the guts to did what you two have done against armed robbers at the bank."
        "{b}{i}Det. White:{/b}{/i}\nAfter studying the video record from the bank I noticed that you two didn't share with the police few important details of the robbery for some reason."
        scene bg pstation3_c3ps with dissolve
        "{b}{i}Det. White:{/b}{/i}\nThe lady kindly shared with me her version of event already. Now I'd like to hear your story, [bro]. Oh and I highly recommend you to tell me the truth this time, becuase if your stories won't match you both will become suspects in this case."
        v "..."
        scene bg pstation3c3ps with dissolve
        b "I still don't understand what exactly do you want from us. We already told everything to the one of your colleagues. What else do you want to know ?"
        if ep5killCounter == 0:
            "{b}{i}Det. White:{/b}{/i}\nI want to know why you didn't say anything about the gun that you have. Security cameras clearly show you holding a gun that doesn't belong to the robbers or to bank's security personnel."
            scene bg pstation3c3_ps with dissolve
            "{b}{i}Det. White:{/b}{/i}\nNeither you nor Vicky mentioned about this little detail that helped you equalize the odds against the criminals. Now I understand how you two managed to disarm and neutralize the scum."
            v "..."
            "{b}{i}Det. White:{/b}{/i}\nBut the most interesting detail about all this is"
            scene bg pstation3c3ps with dissolve
            "{b}{i}Det. White:{/b}{/i}\nThat none of you taken the gun away from the bank 'cause you haven't had it on you during the inspection. Also I know that you don't have a permission for carrying a fire weapon, our database clearly shows that. So my reasonable question is.."
            "{b}{i}Det. White:{/b}{/i}\nWhere is the gun now, [bro] ? Where and how did you get it ?"
            b "I don't know what you've seen on the videorecord and what makes you think that this was a gun. There were no gunshots or other evidances apart from your guesses that the thing was a real gun."
            b "Your assumptions won't be enough to accuse me so don't try to scare me with this bullshit, I know my rights."
        else:
            "{b}{i}Det. White:{/b}{/i}\nYou do realize that you killed a man, [bro] ? No matter who he was or what he did, no one has the right to take another’s life."
            "{b}{i}Det. White:{/b}{/i}\nAfter analyzing the video record I've come to the conclusion that there was no need to kill him."
            scene bg pstation3c3_ps with dissolve
            v "There was..."
            scene bg pstation3_c3ps with dissolve
            "{b}{i}Det. White:{/b}{/i}\nWell thanks a lot for your professional assessment of the situation, I hope the commission of inquiry will take it under the consideration."
            scene bg pstation3c3ps with dissolve
            b "Hey, you were not there, detective. It was 50 by 50 chance for them becuse the scum was pointing the gun right at..Vicky. It's always easier to evaluate the situation when you are sitting on a chair and look at it through the screen."
            scene bg pstation3_c3_ps with dissolve
            b "I couldn't take that risk so I decided to act..."
            "{b}{i}Det. White:{/b}{/i}\nI hope this will serve you as an excuse because my report to the commission will remain with the note of 'Unreasonable use of the weapon'. However the most suspicious detail about all this is.."
            scene bg pstation3_c3ps with dissolve
            "{b}{i}Det. White:{/b}{/i}\nthat both of you lied about the weapon the robber was killed with. The video record shows the gun that you both decided not to mention during testification. "
            scene bg pstation3c3ps with dissolve
            "{b}{i}Det. White:{/b}{/i}\nCaliber analysis of the bullet now does not make much sense, because it was another gun. So I'll ask you only one time [bro], where did you get that weapon and where is it now ?"
            $ renpy.pause()
            b "I'm not carrying any illegal weapon on me, I didn't have it when your men were conducting the search either. So you'd better deal with bad guys, detective. That's all I can tell you..."
        scene bg pstation4c3ps with vpunch
        "{b}{i}Det. White:{/b}{/i}\nYou are playing a very dangerous game right now, [bro]. I know that this gun is still somewhere in the bank. You can be pretty sure that I'll turn whole bank upside down to find it with your fingerprints and then we will continue this talk differently."
        b "Good luck with that, detective. Is there anything else I can help you with ?"
        scene bg pstation4_c3ps with dissolve
        "{b}{i}Det. White:{/b}{/i}\nBirbirinizi nasıl tanıyorsunuz? Bu 'bankada tanıştık' saçmalığına inanmıyorum."
        $ ep6vickyGirlfriend = 0
        menu:
            "She is my girlfriend":
                $ ep6vickyGirlfriend += 1
                b "She is my girlfriend and yes, we've met at the bank earlier this month. I think it's not prohibited by the law, is it detective ?"
                scene bg pstation5c3ps with vpunch
            "She is just a whore":
                scene bg pstation7c4ps with fade
                $ renpy.pause()
                b "Oh, she is just an escort babe that I used to fuck from time to time. I have to confess that she is a real hurricane in the bed, detective. A royal-class elite slut, I highly recommend you to try her sometime, but keep in mind that her time costs whole a lot of money."
                scene bg pstation4c3ps with fade
        "{b}{i}Det. White:{/b}{/i}\nDo you think this is funny ? You are unemployed armed man who drives premium-class car one step away from becoming a suspect or maybe even an accomplice of the robbery. I would not be surprised if you have a large amount of money in that bank."
        b "Yeah, the unemployment benefits from the government are pretty solid nowadays."
        "{b}{i}Det. White:{/b}{/i}\nYou do understand the consequences of such 'cooperation', right ? You didn't give direct answer on any of my questions."
        b "I guess you are just asking them wrongly, detective. They say 'Correctly asked question is already the half of the answer'."
        "{b}{i}Det. White:{/b}{/i}\nWhat do you know about two dead bodies that were found at the warehouse the night you were stopped for speeding ?"
        b "I know nothing about this, the city is big and bad things happen all the time. As for my case it was a pure coincidence, detective."
        "{b}{i}Det. White:{/b}{/i}\nOf course it was.. By the way, how is your wife doing ? Hope you made it to the hospital in time that night."
        b "She is okay, thanks for asking..."
        "{b}{i}Det. White:{/b}{/i}\nYou probably think of me as an idiot and you are sure that your impunity will last forever. I'll have to disappoint you [bro], I know you are a criminal, I just can't prove it yet."
        "{b}{i}Det. White:{/b}{/i}\nI only need this much, a very little disturbance and I will put you in a cell. So please, do me a favour and make some violation..."
        "{b}{i}Det. White:{/b}{/i}\nParking your car in the wrong place or running through the red light will bring you to me again, and then you and I will have.."
        play sound ("music/sounds/phoneRing.mp3")
        scene bg pstation5_c3ps with dissolve
        "{i}{b}PHONE RINGING"
        "{b}{i}Det. White:{/b}{/i}\nExcuse me, I need to answer the call"
        b "Sure"
        scene bg pstation6c3ps with Dissolve(1.0)
        "{b}{i}Det. White:{/b}{/i}\nYes sir..."
        v "What a lovely day, huh ?!"
        b "You don't say, best day ever."
        "{b}{i}Det. White:{/b}{/i}\nNo sir, I didn't..."
        "{b}{i}Det. White:{/b}{/i}\nBut sir... Understood..."
        "{b}{i}Det. White:{/b}{/i}\nMay I know who has authorized... \nYes sir, that is clear. Good night."
        scene bg pstation6_c3ps with dissolve
        "{b}{i}Det. White:{/b}{/i}\nYou two can be free, I don't have all night for you. That is all for now..."
        v "Huh, really ?"
        b "Great, let's go Vicky"
        "{b}{i}Det. White:{/b}{/i}\nShould I remind you two that it would be better for you to not leave the city while the investigation is not finished ?"
        b "Yes please. I would like to get a daily reminder from you, preferably at the morning, something like 'Have a nice day honey, you are the best, don't leave the city or I will be upset...'"
        "{b}{i}Det. White:{/b}{/i}\nHe who laughs last, laughs best, [bro]... Your ass is in my hands from now on.."
        b "Thanks, it's good to know that now it's in your safe hands. It was nice to meet you detective White, sincerely hope we don't meet again."
        v "..."
        scene black with Dissolve (2.0)
        $ renpy.notify ("Birkaç dakika sonra..")
        $ renpy.pause()
        $ renpy.music.set_volume(1, delay=0, channel=3)
        $ renpy.music.play("music/sounds/engineWorking.mp3", channel=3, loop=True, fadein=0)
        scene bg pstation8c3ps with Dissolve (2.0)
        $ renpy.pause()
        v "Any plans for the rest of the night, [bro] ?"
        b "No, not really.. Believe it or not but I'm extremely exhausted, this day was a real challenge. I feel like going home and falling asleep right now."
        v "That's exactly what I was going to do before the interrogation.."
        scene bg pstation8_c4ps with fade
        b "So how did you get here ?"
        v "Oh, I was taking a shower right after I finished working with the client, then detective White called me and demanded to come here. He said it was extremely important so I called a cab and came here right away."
        menu:
            "What did he tell you ?":
                v "Ahm, I don't really remember. It was something about our current status and the investigation."
            "Working with the client ?":
                v "Yes, I still need the money. Oh wait a second, you didn't think you are my only client, did you ?"
            "He tried to intimidate us":
                v "He actually succeed at it. At least he managed to scare the shit out of me. I don't want to go to the jail..."
        scene bg pstation9_c2ps with fade
        $ renpy.pause()
        v "By the way [bro], if I were you I wouldn't be talking like that to the police officer, especially detective. Once I had a bad experience with the police and I almost got behind the bars. It's better play it cool and cooperate..."
        b "I would already been in jail if they really had something on me, so instead of burying a head in the sand it's better to show who you are right from the start."
        scene bg pstation9c5ps with fade
        v "[bro], can I ask you something ? \nDid you really mean everything that you said about us or it all was told only for the detective ?"
        menu:
            "Yes":
                if ep6vickyGirlfriend == 1:
                    $ ep6vickyGirlfriend += 1
                    b "Yes I was absolutely serious about it. I'd really want you to be my girlfriend, Vicky..."
                    scene bg pstation9_c5ps with dissolve
                    v "Oh [bro], it is so cute... I don't even know what to say..."
                    if ep4VickyWarned == 0:
                        v "To be honest I'm still mad at you after what happened at the alley the other night..."
                        b "Come on, it's not a big deal"
                        v "It is a big deal for me [bro]..."
                    else:
                        b "How about \n{i}I always wanted you to be more than just a client to me{/i} \nor if it sounds too cheesy \n{i}I've always wanted to be your little naughty girl{/i}"
                        v "Ha-ha, I will think about it [bro].."
                else:
                    $ ep6vickyGirlfriend = 0
                    b "Yes I was completely honest about it. You are fucking hot and sexy girl, Vicky. You are worth every single dollar, babe"
                    scene bg pstation9_c5ps with dissolve
                    v "Huh, thanks [bro]. I'll take it as a compliment..."
            "No":
                if ep6vickyGirlfriend == 1:
                    $ ep6vickyGirlfriend = 0
                    b "Of course not, Vicky. I mean you are beautiful and smart but now I understand that I couldn't date a girl from escort service, sorry."
                    scene bg pstation9_c5ps with dissolve
                    v "Oh, don't be sorry. I couldn't date someone like you either so we are even, [bro]"
                else:
                    $ ep6vickyGirlfriend += 1
                    b "Of course I didn't mean that Vicky. I just wanted detective left you alone, because to be honest you did nothing wrong at the bank, you just tried to help me. Sorry that I drawed you into this..."
                    scene bg pstation9_c5ps with dissolve
                    v "It's okay, [bro]. I regret of nothing, you and Julie are not indifferent to me..."
                    if ep4VickyWarned == 0:
                        v "Fine, to be honest I'm still mad at you after what you did to me at the alley the other night..."
                        b "Couldn't help myself, you are so damn hot Vicky"
                        v "That's not what I wanted to hear, [bro]..."
                    else:
                        v "Actually, no one treated me as well as you do and I appreciate it [bro]..."
                        $ renpy.pause()
        b "Hey, it's already late, get in the car I'll give you a ride."
        v "Thanks for the offer [bro]. Just letting you know that you won't get a blowjob in the car from me. I want to clarify this in case it was your big plan by offering me a ride."
        b "Oh no, that won't work. See you later then Vicky"
        scene bg pstation9c5ps with dissolve
        v "Hey..."
        b "Just kidding, come on, hop in already"
        $ renpy.pause()
        jump ep6vapt
        return

    label ep6vapt:
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra Vicky'nin yerinde..")
        $ renpy.pause()
        $ ep6VickyMad = 0
        scene bg vApt1c3ps with Dissolve (2.5)
        v "Well here we are, my apartment is over there. Thanks for the ride [bro]... It's time say goodbye, I guess..."
        scene bg vApt2c1ps with fade
        b "Wait, are you saying that I won't even get an invitation for a cup of coffee ?"
        scene bg vApt3_c1ps with dissolve
        v "I'm sorry [bro], I can't invite you inside now. I have an appointment with the next client..."
        b "What ?"
        scene bg vApt2_c_1ps with dissolve
        v "You'd better go home, really. Take some rest, it's been a tough day for you."
        b "Did I get you right ? You are now serving the clients at your place ? You never did that when we were.."
        scene bg vApt3c1ps with dissolve
        v "Well, what can I do you were my favourite client but you decided to stop seeing each other and I still need the money. Besides not every client is ready to let me in their place or rent a room in a hotel."
        v "Almost all of them are famous people who don't want that kind of publicity, that is why my apartment is a good option."
        scene bg vApt3_c1ps with dissolve
        menu:
            "Offer her money":
                b "How about I'll pay you twice more than this next client of yours ? I want you to cancel the meeting and you will hang out with me instead."
                scene bg vApt2_c1ps with dissolve
                v "Don't ask me to do such thing [bro].. You know it's against my principles, who would I be without them ?"
                b "I thought you need the money Vicky, I can give it to you just stay with me"
            "Offer her quit":
                $ ep4VickyWarned = 1
                b "Vicky.. I've been thinking about this a lot lately, I want you to quit the escort and I want you to be with me."
                scene bg vApt2_c1ps with dissolve
                v "[bro]..."
                b "Yes, I know that I may not be perfect, I'm sory for that, also I'm sorry for everything bad that I've done to you. I feel that I'm getting better with you, feel this connection between us, don't you feel it too ?"
        if (ep4VickyWarned == 1 and ep6vickyGirlfriend != 0):
            v "[bro] I am a prostitute and you a criminal... What future do we have ?"
            b "Come here, baby..."
            scene bg vApt5c2ps with fade
            v "Oh..?"
            b "I don't care what future is waiting for us, but I promise that I'll do everything I can to make it good for us.."
            b "I need you Vicky..."
            $ renpy.pause()
            scene bg vApt5_c4ps with fade
            v "[bro] this is so unexpected, I don't even know what to say, I mean I do have a feelings to you, but..."
            b "Hush, no words are necessary... Just kiss me like you did that night..."
            $ renpy.pause()
            scene bg vApt6c6ps with fade
            v "Come on [bro], you know it's against my principles, that kiss was an exception because you were.. you are my favourite client and I wanted to make you feel good.. But now I need to go, let's talk about it later, ok..?"
            b "I want to be the only one, not your favourite one, Vicky... I also want to make you feel good, come here"
            scene bg vApt7c7ps with fade
            v "Huh ?"
            b "Oh babe, you smell so incredibly good.. I'm getting hard only from your scent alone.."
            scene bg vApt8c8ps with fade
            $ renpy.music.set_volume(0.35, delay=0, channel=1)
            $ renpy.music.play("music/sexyTheme.mp3", channel=1, loop=True, fadein=5)
            $ renpy.pause()
            v "Oh, I'm flattered, [bro]..."
            b "Here, touch and check it for yourself... I want you to feel it..."
            menu:
                "Move her hand":
                    scene bg vApt8_c8ps with dissolve
            v "Yes... It's hard as rock..."
            b "It's only for you, Vicky..."
            scene bg vApt8_c10ps with fade
            $ renpy.pause()
            b "I miss your amazing body so much, babe.. Your incredibly soft and silky skin, slender legs and curvy thighs.."
            v "[bro]..."
            menu:
                "Touch her breasts":
                    scene bg vApt9_c10ps with dissolve
            b "These gorgeous and tender breasts..."
            v "Ah.."
            b "I would so want to take off your cloth and have my way with you from behind, pinning you against the trunk of my car.."
            scene bg vApt8fc9ps with fade
            v "[bro]... You now we can't do that... I need to..."
            menu:
                "Squeeze":
                    scene bg vApt9fc9ps with dissolve
            play sound ("music/sounds/sighLoud.mp3")
            v "Oh..."
            b "Your breasts should be worshiped, Vicky... "
            scene bg vApt9_c7ps with fade
            b "I've never seen anything more perfect and alluring..."
            $ renpy.pause()
            scene bg vApt9_c10ps with fade
            b "I would caress them all night long tirelessly..."
            menu:
                "Bare":
                    play sound ("music/sounds/sigh.mp3")
            scene bg vApt10c10ps with dissolve
            v "Huh-ah..."
            b "Here they are... So soft and firm... Come to daddy"
            v "Mmm.."
            scene bg vApt10_c10ps with Dissolve(0.75)
            scene bg vApt10c10ps with Dissolve(0.75)
            scene bg vApt10_c10ps with Dissolve(0.75)
            scene bg vApt10c10ps with Dissolve(0.75)
            scene bg vApt10_c10ps with Dissolve(0.75)
            scene bg vApt10c10ps with Dissolve(0.75)
            v "Oh, [bro].. That feels so good.."
            b "The only thing I miss more than your breasts is your sweet luscious wet little pussy. I know you wouldn't like it but I would be doing it with you without a condom this time Vicky and you exactly now why.."
            scene bg vApt10_c10ps with Dissolve(0.75)
            scene bg vApt10c10ps with Dissolve(0.75)
            scene bg vApt10_c10ps with Dissolve(0.75)
            scene bg vApt10c10ps with Dissolve(0.75)
            v "Oh.. Do I..?"
            b "Yes, baby.."
            scene bg vApt9fc9ps with fade
            v "Why.."
            b "Because you are the bad girl, Vicky.."
            v "Oh, [bro]..."
            b "Who is the bad girl, huh ?"
            v "Ahm.."
            b "Say it !"
            scene bg vApt8f_c9ps with dissolve
            v "I'm the bad girl..."
            b "Exactly..."
            $ renpy.pause()
            scene bg vApt10c10ps with fade
            b "One thing I love the most about the bad girls is that they're always wet..."
            menu:
                "Finger her":
                    scene bg vApt11c10ps with dissolve
            play sound ("music/sounds/sighLoud.mp3")
            v "Ah..."
            b "Wow you have quite of a flood down here, Vicky.. Your pussy is so wet.."
            scene bg vApt11_c8ps with fade
            v "Oh yes.."
            b "I would start filling your sweet and tight little pussy slowly and gently... Carefully plunging it deep inside of you inch by inch until you take it all fully like a good girl.."
            b "You would feel pleasant hardness and pulsation of my cock in your stretched and warm little pussy..."
            menu:
                "Rub the clit":
                    scene bg vApt11c8ps with dissolve
            b "That's a good girl.. Stroke my cock meanwhile.."
            v "Oh [bro]..."
            scene bg vApt11_c8ps with dissolve
            scene bg vApt11c8ps with dissolve
            v "Just like that... Ah..."
            scene bg vApt11_c8ps with dissolve
            scene bg vApt11c8ps with dissolve
            scene bg vApt11_c8ps with dissolve
            scene bg vApt11c8ps with dissolve
            scene bg vApt11_c8ps with dissolve
            scene bg vApt11c8ps with dissolve
            scene bg vApt11_c8ps with dissolve
            scene bg vApt11c8ps with dissolve
            b "Then I would pull your hair and would intensify the thrusts and speed up the frictions, thus shoving it balls-deep inside of you each time.."
            v "Oh my god, [bro]... Please don't stop..."
            menu:
                "Speed up":
                    scene bg vApt11_c8ps with Dissolve(0.35)
            scene bg vApt11c8ps with Dissolve(0.35)
            scene bg vApt11_c8ps with Dissolve(0.35)
            scene bg vApt11c8ps with Dissolve(0.35)
            scene bg vApt11_c8ps with Dissolve(0.35)
            scene bg vApt11c8ps with Dissolve(0.35)
            scene bg vApt11_c8ps with Dissolve(0.35)
            scene bg vApt11c8ps with Dissolve(0.35)
            scene bg vApt11_c8ps with Dissolve(0.35)
            scene bg vApt11c8ps with Dissolve(0.35)
            b "I would start fucking and spanking you as hard as I can because I know you crave it... "
            v "Just like that, oh my god.. Almost there.."
            b "Bad girl.."
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            b "After this rough fucking I would so blow my big load deeply inside your tight and sweet little pussy because I know that you love the feeling of a flowing hot cum inside you"
            v "Oh yes [bro], I'm comming !"
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            b "Cum for me Vicky, cum like a good girl !"
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            scene bg vApt11_c8ps with Dissolve(0.25)
            scene bg vApt11c8ps with Dissolve(0.25)
            v "Aaaaaah !"
            scene bg vApt11_c8ps with kissFlash
            scene bg vApt11c8ps with kissFlash
            scene bg vApt11c10ps with kissFlash
            scene bg vApt11c7ps with kissFlash
            menu:
                "Put fingers inside":
                    play sound ("music/sounds/squish.mp3")
            scene bg vApt9fc9ps with kissFlashLong
            play sound ("music/sounds/sighLoud.mp3")
            scene bg vApt11fc9ps with Dissolve (1.0)
            v "Oh my god, [bro] !!!"
            b "Good girl... I can feel how your pussy contracts and pulsates right now..."
            v "{i}Breathing heavily{/i}\nI.. I'm.."
            b "Hope I'm still your favourite client Vicky.."
            v "That's for sure [bro], it was fantastic... Now I have a feeling that it's my turn to pay you..."
            $ renpy.pause()
            jump ep6AtHome
        elif (ep4VickyWarned == 0 and ep6vickyGirlfriend == 0):
            $ ep6VickyMad += 1
            scene bg vApt4c2ps with fade
            v "Of course you want it, It would be so convenient for you. You just need a dirty whore to fuck, you already said and proved that with your actions."
            b "It's not like that, girl. Come here, I'll show you what I want..."
            $ renpy.pause()
            scene bg vApt9_ac7_ps with fade
            v "Hey, what are you..?"
            b "Relax, baby... Why are you so stressed out...?"
            v "[bro]... Seriously, didn't you hear what I just said ?"
            b "I know a cure that will help you to calm down Vicky..."
            menu:
                "Touch her breasts":
                    scene bg vApt9_c10ps with fade
            v "What ? Are you serious ? Groping my breasts on the street in the middle of the night seems funny to you ?"
            scene bg vApt9_ac7ps with fade
            b "It's just the beginning, babe... I would so pin you against the car and have my way with you from behind right now..."
            scene bg vApt9_a_c7ps with dissolve
            v "Hey, take your hands away from me !"
            b "Relax, sexy... You'll miss all the fun if you continue to be so nervous..."
            v "[bro] ! I'm serious, leave me alone it's not funny at all !"
            b "Hm... I don't get it... Do you want me to fuck you as if it were a rape or you're just playing hard to get...? To be honest either way sounds good to me, it turns me on even more Vicky... Yeah, do you feel how hard my cock is, babe ?"
            scene bg vApt9_a_c7ps with vpunch
            v "I'm not kidding [bro] ! Last warning, let me go or I promise you'll regret it !"
            b "Damn, you're saying it so believable and genuinely that I would even buy it, but I know that you're just a dirty slut who extremely likes teasing..."
            b "Let's find out who is right, I bet your pussy is alredy completely wet and is waiting for my hard cock..."
            menu:
                "Finger her":
                    scene bg vApt15c7ps with dissolve
            b "Well well well, what do we have here ? Come to daddy..."
            v "That's it, I'm done with this shit !"
            play sound ("music/sounds/punchFace.mp3")
            scene bg vApt12c7ps with hpunch
            scene bg vApt12c7ps with cumFlash
            v "Get your fucking hands off me !"
            b "{i}Agh.. What-the.."
            scene bg vApt5_a_c4ps with fade
            v "If you ever do something like this to me again, I swear to god, I'll kick the shit out of you [bro]. Did I make myself clear ?"
            $ renpy.pause()
            scene bg vApt13c1ps with fade
            v "But why should I bother, we won't see each other again you can be damn sure about it. Too bad Julie has to live with such an asshole [brother]..."
            $ renpy.pause()
            scene bg vApt13c2ps with fade
            b "Vicky wait ! Why did you do that ?!"
            v "Tell Julie about what happened here, I'm sure she will gladly explain you how to treat a woman... I don't want to talk to you anymore..."
            b "Hey..."
            $ renpy.pause()
            scene bg vApt14c2ps with fade
            b "{i}Shit... What the fuck is wrong with that bitch. Do all whores behave like this nowadays. Too bad I haven't had a chance to fuck her in the ass. Looks like this option is lost, I have to find someone else..."
            $ renpy.pause()
            jump ep6AtHome
        else:
            scene bg vApt3c1ps with dissolve
            v "Do you think that the way you treat me is normal ? You tend to say one things and do completely opposite ones."
            scene bg vApt3_c1ps with dissolve
            v "I don't even know how real [bro] looks like and who he is."
            b "Come here, babe. I'll show you who I really am..."
            scene bg vApt7c7ps with fade
            v "Wow, I don't know what you are going to do, but keep in mind that you don't have much time and I need to go"
            b "Don't worry Vicky, when I finish you might actually cancel the date with whoever that jerk is and will ask me for more..."
            scene bg vApt8c8ps with fade
            v "Really ? Sounds intriguing... "
            b "You know, I barely started touching you but my dick is already rock-hard for you... Here, check it for yourself..."
            menu:
                "Move her hand":
                    scene bg vApt8_c8ps with dissolve
            v "Well, I have to admit that it's really hard... But don't worry, nothing lethal in this, it tends to happen to all men who know me close enough, [bro]..."
            b "Do you feel how hard and ready for you it is ? Stroke it for me, Vicky..."
            scene bg vApt8_c10ps with fade
            v "Sorry [bro], I'd rather not to..."
            b "What ? Why ?"
            scene bg vApt8c10ps with dissolve
            v "I just don't want you to get too excited, you know. I have a feeling that you don't have an extra pair of pants in the trunk of your car and I don't want to wash them in the middle of the night either..."
            b "You probably confused me with someone else..."
            v "Maybe... To which [bro] am I talking to right now ?"
            b "To one who doesn't cum inside his own pants. This one cums only inside good girls sweet mouths..."
            b "Speaking about the trunk... I would so pin you against it and have my way with you from behind right now..."
            scene bg vApt8fc9ps with fade
            v "Really ? I would never have thought... Do you tell it to all girls ?"
            b "No... Only to good ones... And you are a good girl, aren't you Vicky...?"
            scene bg vApt8c10ps with fade
            v "Ahm... I don't even know... Let me think about it..."
            v "Hm... Oh, I don't swallow, that is the sad truth... I bet that good girls do that, unfortunately that's not about me so, I guess it makes me 'bad girl' doesn't it...?"
            b "That's not a problem, baby... I know a guy who will gladly donate you his hot and yummy sperm... You just have to try it, then you'll get used to cum, that's the whole trick..."
            scene bg vApt8fc9ps with fade
            v "I don't even want to know how you found out about it..."
            scene bg vApt8fc9ps with vpunch
            b "Are you fucking with me right now ?!"
            scene bg vApt8f_c9ps with dissolve
            v "Of course not [bro]... I'm just amazed with your deep knowledge of swallowing..."
            b "{i}Damn... She's not showing any interest at all..."
            scene bg vApt8c10ps with fade
            b "Do you want to know what I am amazed with...?"
            v "I have {b}absolutely{/b} no idea [bro]... God, I hope it doesn't related to excessive nature caring, something like washing the toilet paper and using it again..."
            scene bg vApt8c10ps with hpunch
            b "I'm amazed with this !"
            menu:
                "Touch her breasts":
                    scene bg vApt9c10ps with dissolve
            b "So soft and tender... I am so lucky to have you Vicky... Other guys will never..."
            v "Speaking about other guys..."
            scene bg vApt5_ac4ps with fade
            b "Huh ? What's wrong ?"
            v "I'm afraid our time is up [bro]. I need to go now. Thanks again for the ride, have a good rest of the night. Drive safely and responsibly, always wear the seatbelt. Oh and please say hello to Julie, poor girl probably still scared, hope she's okay."
            b "What ?! Are you serious ?"
            v "Yup, goodbye !"
            $ renpy.pause()
            scene bg vApt14c2ps with fade
            b "{i}What the fuck was that ?! I guess I'll never understand women's logic... Damn, I'd better go home now, this shitty day must come to an end..."
            $ renpy.pause()
            jump ep6AtHome
        return

    label ep6AtHome:
        $ renpy.music.stop(channel=1, fadeout=3)
        $ renpy.music.stop(channel=3, fadeout=3)
        scene black with Dissolve (2.0)
        $ renpy.notify ("Bu arada evde..")
        $ renpy.pause()
        $ renpy.music.set_volume(0.5, delay=0, channel=1)
        $ renpy.music.play("music/scarlettTheme.mp3", channel=1, loop=True, fadein=3)
        scene bg atHome134c1ps with Dissolve (2.5)
        j "You can't even imagine how long I've been waiting for this Scarlett..."
        s "Me too Julie, I missed you so much"
        scene bg atHome135c4ps with fade
        j "Honestly I don't how you managed to stand that long without having a sex... I literally masturbated like 5 times a day, that's how badly I want you girl... Let's not part for such a long period of time again..."
        scene bg atHome135c5ps with fade
        s "Deal, I won't let you go this time I promise. Tell me what you've been thinking about when you're playing with yourself without me, baby. Maybe there is something you'd like to tell me about, don't be shy."
        $ renpy.pause()
        j "Ahm... It's you Scarlett, I'm always thinking about you... and..."
        play sound ("music/sounds/kiss.mp3")
        scene bg atHome136c8ps with kissFlash
        s "Yes ?"
        j "Lately I've started to think about..."
        s "About what ?"
        j "I've started to think about a cock... I'm sorry baby..."
        scene bg atHome136c9ps with fade
        s "Oh Julie, stop it. You shouldn't be sorry, it's completely normal to think about big thick cock. Tell me more, I want the details."
        j "Ah... Well... "
        $ renpy.pause()
        scene bg atHome136c11ps with fade
        j "Oh... Firstly I'm imagining how greedily I suck on it, trying to swallow the glance as deep as I can... But the dick I'm dreaming about is so huge that it barely fits inside my throat, I can't breath so I start gagging..."
        scene bg atHome136c12ps with fade
        s "That is totally okay Julie, you need to get use to gagging at first. Then you will be taking it inside your sweet little mouth like a good girl. What happens next ?"
        scene bg atHome136_c12ps with dissolve
        j "Ah... Then I imagine how this cock is starting to fuck me... But since I'm still a virgin I'm too scared to let it inside of me, so I take just the tip of it in my pussy... That's basically it, by this time I usually come few times and can't continue any longer, you do know that I'm very sensitive and come fast..."
        scene bg atHome136c6ps with fade
        s "I know Julie... Tell me who the cock you're imagining during the masturbation belongs to... Is it someone special, is it someone you know, who is it ?"
        $ renpy.pause()
        scene bg atHome136c12ps with fade
        j "Ah, no not really..."
        play sound ("music/sounds/kiss.mp3")
        scene bg atHome136_c12ps with kissFlash
        s "It has to be someone..."
        j "I... I really don't know... I almost don't have friends or guys, especially in this city... I'm just imagining the general elements such as strong arms, v-shaped body and wide shoulders..."
        scene bg atHome136c11ps with fade
        s "Hm...That reminds me of someone..."
        $ renpy.pause()
        scene bg atHome136c8ps with fade
        j "What... Who ?!?!?!"
        $ renpy.pause()
        scene bg atHome136c12ps with fade
        s "It's your brother isn't it...?"
        scene bg atHome136_c12ps with dissolve
        j "Whaaat...?!"
        play sound ("music/sounds/kiss.mp3")
        scene bg atHome136_c12ps with kissFlash
        s "I have to confess Julie... Hope you won't get jealous and you will understand me..."
        scene bg atHome136c9ps with fade
        s "This whole summer I've been having a sex with my [father]..."
        play sound ("music/sounds/kiss.mp3")
        scene bg atHome136c6ps with kissFlash
        j "Seriously ?! How could you do that Scarlett..."
        $ renpy.pause()
        s "I wanted to expand our sex life Julie... But I was afraid of suggesting you something new like that, I didn't want to lose you babe..."
        scene bg atHome136c12ps with fade
        s "I started to dream about the dick, I got obsessed with it so I decided to act... I didn't want to fuck some jerk who would dump me right after the sex, so I choosed my [father] as my first lover... He was the one who took my virginity and I have no regrets about it..."
        s "In fact I'm very happy about it, because these men are the best ! Think for yourself, they'll never hurt you or make you feel bad, they will always treat you well because you are the [family]"
        play sound ("music/sounds/kiss.mp3")
        scene bg atHome136_c12ps with kissFlash
        j "Scarlett... I don't even know what to say..."
        s "Let's be honest Julie... Your [brother] is so fucking hot, don't you ever think of him like that...?"
        j "...how...how were the feelings from the dick...?"
        s "Come here, I'll show you..."
        play sound ("music/sounds/sighLoud.mp3")
        scene bg atHome137c13ps with fade
        j "Oh..."
        $ renpy.pause()
        s "Here, these are my fingers... Believe it or not but a dick feels like 100 times better..."
        j "No way... Ah.. I come almost instantly from the fingers alone, I wonder how would it feel like with dick...?"
        scene bg atHome138_1c16ps with fade
        s "It will be so fucking amazing, that you will lose your consciousness during the orgasm, Julie.... Like I did..."
        scene bg atHome137_c14ps with fade
        scene bg atHome137__c14ps with dissolve
        scene bg atHome137_c14ps with dissolve
        scene bg atHome137__c14ps with dissolve
        scene bg atHome137_c14ps with dissolve
        scene bg atHome137__c14ps with dissolve
        j "Oh my god, yes... Just like that Scarlett..."
        scene bg atHome137_c12ps with fade
        s "Me and my [father] tried everything we wanted in sex... Except anal... For some reason [father] didn't want to fuck me in the ass, so I had to buy a butt-plug for myself"
        $ renpy.pause()
        scene bg atHome138_1c16ps with fade
        s "But frankly speaking, the most fantastic feelings that I get come from stimulation of my tight little asshole..."
        scene bg atHome138c16ps with dissolve
        s "I always came like a crazy bitch when [father] was fucking my pussy and played with the butt-plug at the same time..."
        j "Oh, yes, that feels so good..."
        scene bg atHome137_c14ps with fade
        scene bg atHome137__c14ps with dissolve
        scene bg atHome137_c14ps with dissolve
        scene bg atHome137__c14ps with dissolve
        scene bg atHome137_c14ps with dissolve
        scene bg atHome137__c14ps with dissolve
        s "So if I were you Julie, I would be definitely starting to think about doing it with [bro], to me it's the perfect option..."
        scene bg atHome137_c14ps with dissolve
        scene bg atHome137__c14ps with dissolve
        scene bg atHome137_c14ps with dissolve
        scene bg atHome137__c14ps with dissolve
        scene bg atHome138_1c16ps with fade
        s "I wouldn't mind fucking him myself, but I have a feeling that you'd be against it, wouldn't you...?"
        scene bg atHome137_c12ps with fade
        j "Scarlett... Stop it... He is not like that, he will decide that I'm crazy or perverted... What would he think about me after this...?"
        scene bg atHome138c16ps with fade
        s "You'd better be thinking about his big hard cock in your little mouth Julie..."
        scene bg atHome138c15ps with fade
        j "Ah... Scarlett..."
        $ renpy.pause()
        s "Yes baby... I love sucking a dick, you will love it too... There is some kind of its own pleasure in it, the element of submission or just female primal instinct to surrender, can't really tell... But one thing I know for sure, the blowjob turns me on like nothing else does, I instantly become wet down there..."
        j "Oh... I want it... I want to experience those feelings, I want to suck a dick..."
        play sound ("music/sounds/squish.mp3")
        scene bg atHome138_c15ps with kissFlash
        j "{i}Ah... Ghah..."
        s "Good girl... Here is something for you..."
        j "{i}Mmm...suck-suck..."
        scene bg atHome137_c12ps with fade
        j "I'm almost there Scarlett... I'm close to comming..."
        scene bg atHome138_1c16ps with fade
        s "One of my favourite things is when I'm being fucked really hard from behind with my legs wide opened the way I can't bring them together... This gives me indescribable feeling of helplessness so I come more intense..."
        j "I'm comming Scarlett... Aaaah..."
        scene bg atHome137_c14ps with fade
        scene bg atHome137__c14ps with Dissolve(0.25)
        scene bg atHome137_c14ps with Dissolve(0.25)
        scene bg atHome137__c14ps with Dissolve(0.25)
        scene bg atHome137_c14ps with Dissolve(0.25)
        scene bg atHome137__c14ps with Dissolve(0.25)
        scene bg atHome137_c14ps with Dissolve(0.25)
        scene bg atHome137__c14ps with Dissolve(0.25)
        scene bg atHome137_c14ps with Dissolve(0.25)
        scene bg atHome137__c14ps with Dissolve(0.25)
        s "Do it baby, come for me ! Imagine that it's the big cock of your [brother] fucking you like a little bitch right now !"
        scene bg atHome137_c14ps with Dissolve(0.25)
        scene bg atHome137__c14ps with Dissolve(0.25)
        scene bg atHome137_c14ps with Dissolve(0.25)
        scene bg atHome137__c14ps with Dissolve(0.25)
        scene bg atHome137_c14ps with Dissolve(0.25)
        scene bg atHome137__c14ps with Dissolve(0.25)
        scene bg atHome137_c14ps with Dissolve(0.25)
        scene bg atHome137__c14ps with Dissolve(0.25)
        s "Imagine like he comes deep inside in you and his cum spreads all over your pussy !"
        scene bg atHome137_c14ps with kissFlash
        scene bg atHome137__c14ps with kissFlash
        play sound ("music/sounds/squish.mp3")
        scene bg atHome137___c18ps with kissFlashLong
        scene bg atHome137___c18ps with vpunch
        scene bg atHome137___c18ps with vpunch
        scene bg atHome137___c18ps with vpunch
        j "Aaaah... That was incredible Scarlett... I've never came so hard before..."
        s "Good girl..."
        $ renpy.pause()
        j "Hug me please, Scarlett... You know how much I love cuddling after sex..."
        s "Of course I do, Julie... Come to me..."
        scene bg atHome139c18ps with fade
        s "I love you baby... I'm glad that we both don't mind our little experiments in the bed..."
        scene bg atHome140c19ps with fade
        j "I love you too darling... I'm just not quite sure that I can make it, to be honest... I mean fantasies is one thing but reality is absolutely another..."
        s "Don't worry Julie, I will help you..."
        j "And I'm still worrying about [bro]... What if he is just not into it and will throw me outside...?"
        s "Don't be... No man will say 'No' to you, and your [brother] is not an exception... You are incredibly beautiful Julie..."
        j "Thank you Scarlett, you are so sweet and adorable... What do you suggest me then ? How should I draw [bro]'s attention to me for further seduction ? What did you do to make it happen with your [father]...?"
        play sound ("music/sounds/doorClose.mp3")
        scene bg atHome140_1c19ps with dissolve
        "{i}{b}DOOR CLOSES"
        j "Huh ?! Looks like [bro] came home..."
        $ renpy.pause()
        scene bg atHome141c3ps with fade
        b "{i}Ah shit, that was probably a bit loud..."
        play sound ("music/sounds/lockSound.mp3")
        b "{i}I feel like falling asleep right here... But I need to take a shower first, hope I won't wake up Julie... Huh what is this, an extra pair of shoes ? Of course, Julie told me that Scarlett stays here for the night..."
        scene bg atHome140_c19ps with fade
        s "As for your question, it's better to go straight to the business, that's what I've done with my [father] and it worked, so..."
        scene bg atHome140_2c19ps with dissolve
        j "Wait Scarlett !"
        scene bg atHome140_c19ps with hpunch
        s "[bro] ! IS THAT YOU ?! COME INSIDE FOR A SECOND PLEASE WE NEED YOUR HELP !"
        $ renpy.pause()
        scene bg atHome140_2c19ps with dissolve
        j "Are you nuts ?! What do you think you're doing ?!"
        scene bg atHome140_1c19ps with dissolve
        s "Trying to get us both some fun, don't you see ?! And besides unlike you I haven't had an orgasm today yet..."
        scene bg atHome140_c19ps with dissolve
        j "Oh my god... What will happen now...?"
        s "Relax Julie, everything will be just right... You and I will remember this night for the rest of our lives..."
        $ renpy.music.stop(channel=1, fadeout=15)
        jump episode7
        #jump supportMe
        return

####################################################EPISODE_7##################################################

    image bg atHome141c3_ps = "images/ep7/atHome141c3_ps.png"
    image bg atHome142__c4ps = "images/ep7/atHome142__c4ps.png"
    image bg atHome142_c4ps = "images/ep7/atHome142_c4ps.png"
    image bg atHome142c4ps = "images/ep7/atHome142c4ps.png"
    image bg atHome143c20ps = "images/ep7/atHome143c20ps.png"
    image bg atHome144c1ps = "images/ep7/atHome144c1ps.png"
    image bg atHome144c20ps = "images/ep7/atHome144c20ps.png"
    image bg atHome144c2ps = "images/ep7/atHome144c2ps.png"
    image bg atHome145c1ps = "images/ep7/atHome145c1ps.png"
    image bg atHome145c2ps = "images/ep7/atHome145c2ps.png"
    image bg atHome146_c2ps = "images/ep7/atHome146_c2ps.png"
    image bg atHome146c1ps = "images/ep7/atHome146c1ps.png"
    image bg atHome146c2ps = "images/ep7/atHome146c2ps.png"
    image bg atHome147_c7ps = "images/ep7/atHome147_c7ps.png"
    image bg atHome147c4ps = "images/ep7/atHome147c4ps.png"
    image bg atHome147c5ps = "images/ep7/atHome147c5ps.png"
    image bg atHome147c6ps = "images/ep7/atHome147c6ps.png"
    image bg atHome147c7ps = "images/ep7/atHome147c7ps.png"
    image bg atHome148c5ps = "images/ep7/atHome148c5ps.png"

    image bg Trap1c1ps = "images/ep7/Trap1c1ps.png"
    image bg Trap2c3ps = "images/ep7/Trap2c3ps.png"
    image bg Trap3__c2ps = "images/ep7/Trap3__c2ps.png"
    image bg Trap3_c2ps = "images/ep7/Trap3_c2ps.png"
    image bg Trap3c2ps = "images/ep7/Trap3c2ps.png"
    image bg Trap4__c4ps = "images/ep7/Trap4__c4ps.png"
    image bg Trap4_c4ps = "images/ep7/Trap4_c4ps.png"
    image bg Trap4c4ps = "images/ep7/Trap4c4ps.png"
    image bg Trap5c4ps = "images/ep7/Trap5c4ps.png"
    image bg Trap6c5ps = "images/ep7/Trap6c5ps.png"
    image bg Trap6c6ps = "images/ep7/Trap6c6ps.png"
    image bg Trap7__c8ps = "images/ep7/Trap7__c8ps.png"
    image bg Trap7_c8ps = "images/ep7/Trap7_c8ps.png"
    image bg Trap7c7ps = "images/ep7/Trap7c7ps.png"
    image bg Trap7c8ps = "images/ep7/Trap7c8ps.png"
    image bg Trap8__c11ps = "images/ep7/Trap8__c11ps.png"
    image bg Trap8_c10ps = "images/ep7/Trap8_c10ps.png"
    image bg Trap8c9ps = "images/ep7/Trap8c9ps.png"
    image bg Trap9_c13ps = "images/ep7/Trap9_c13ps.png"
    image bg Trap9c12ps = "images/ep7/Trap9c12ps.png"
    image bg Trap10__c12ps = "images/ep7/Trap10__c12ps.png"
    image bg Trap10_c12ps = "images/ep7/Trap10_c12ps.png"
    image bg Trap10c9_ps = "images/ep7/Trap10c9_ps.png"
    image bg Trap10c9ps = "images/ep7/Trap10c9ps.png"
    image bg Trap11__c10ps = "images/ep7/Trap11__c10ps.png"
    image bg Trap11_c10ps = "images/ep7/Trap11_c10ps.png"
    image bg Trap11_c14ps = "images/ep7/Trap11_c14ps.png"
    image bg Trap11c13ps = "images/ep7/Trap11c13ps.png"

    image bg atHome149__c2__ps = "images/ep7/atHome149__c2__ps.png"
    image bg atHome149_c2__ps = "images/ep7/atHome149_c2__ps.png"
    image bg atHome149_c2_ps = "images/ep7/atHome149_c2_ps.png"
    image bg atHome149_c5ps = "images/ep7/atHome149_c5ps.png"
    image bg atHome149c5ps = "images/ep7/atHome149c5ps.png"
    image bg atHome150__c2ps = "images/ep7/atHome150__c2ps.png"
    image bg atHome150_c2ps = "images/ep7/atHome150_c2ps.png"
    image bg atHome150c2ps = "images/ep7/atHome150c2ps.png"
    image bg atHome151c2ps = "images/ep7/atHome151c2ps.png"
    image bg atHome152c_1ps = "images/ep7/atHome152c_1ps.png"
    image bg atHome152c1ps = "images/ep7/atHome152c1ps.png"
    image bg atHome153c1ps = "images/ep7/atHome153c1ps.png"
    image bg atHome154_c1_ps = "images/ep7/atHome154_c1_ps.png"
    image bg atHome154_c1ps = "images/ep7/atHome154_c1ps.png"
    image bg atHome154c1ps = "images/ep7/atHome154c1ps.png"
    image bg atHome154c2ps = "images/ep7/atHome154c2ps.png"
    image bg atHome155__c3ps = "images/ep7/atHome155__c3ps.png"
    image bg atHome155_c4ps = "images/ep7/atHome155_c4ps.png"
    image bg atHome155c1ps = "images/ep7/atHome155c1ps.png"
    image bg atHome155c3ps = "images/ep7/atHome155c3ps.png"
    image bg atHome156c4ps = "images/ep7/atHome156c4ps.png"
    image bg atHome157c1_ps = "images/ep7/atHome157c1_ps.png"
    image bg atHome157c1ps = "images/ep7/atHome157c1ps.png"

    image bg Trap12_c16ps = "images/ep7/Trap12_c16ps.png"
    image bg Trap12_c17ps = "images/ep7/Trap12_c17ps.png"
    image bg Trap12_c9ps = "images/ep7/Trap12_c9ps.png"
    image bg Trap12c15ps = "images/ep7/Trap12c15ps.png"
    image bg Trap12c16ps = "images/ep7/Trap12c16ps.png"
    image bg Trap12c9ps = "images/ep7/Trap12c9ps.png"
    image bg Trap13_c19ps = "images/ep7/Trap13_c19ps.png"
    image bg Trap13c18ps = "images/ep7/Trap13c18ps.png"
    image bg Trap13c19ps = "images/ep7/Trap13c19ps.png"
    image bg Trap14__c20ps = "images/ep7/Trap14__c20ps.png"
    image bg Trap14_c20ps = "images/ep7/Trap14_c20ps.png"
    image bg Trap14c19ps = "images/ep7/Trap14c19ps.png"
    image bg Trap15_c21ps = "images/ep7/Trap15_c21ps.png"
    image bg Trap15c21ps = "images/ep7/Trap15c21ps.png"

    image bg atHome158c4ps = "images/ep7/atHome158c4ps.png"
    image bg atHome158c5ps = "images/ep7/atHome158c5ps.png"
    image bg atHome158c6ps = "images/ep7/158c6ps.png"
    image bg atHome159c5ps = "images/ep7/atHome159c5ps.png"
    image bg atHome160_c4ps = "images/ep7/atHome160_c4ps.png"
    image bg atHome160c4ps = "images/ep7/atHome160c4ps.png"
    image bg atHome161_c4_ps = "images/ep7/atHome161_c4_ps.png"
    image bg atHome161_c4_ps_ = "images/ep7/atHome161_c4_ps_.png"
    image bg atHome161_c4ps = "images/ep7/atHome161_c4ps.png"
    image bg atHome161c4ps = "images/ep7/atHome161c4ps.png"
    image bg atHome162_c4ps = "images/ep7/atHome162_c4ps.png"
    image bg atHome162c4ps = "images/ep7/atHome162c4ps.png"
    image bg atHome163_c4ps = "images/ep7/atHome163_c4ps.png"
    image bg atHome163c4ps = "images/ep7/atHome163c4ps.png"
    image bg atHome164_c4ps = "images/ep7/atHome164_c4ps.png"
    image bg atHome164c4ps = "images/ep7/atHome164c4ps.png"
    image bg atHome165_c4ps = "images/ep7/atHome165_c4ps.png"
    image bg atHome165c4ps = "images/ep7/atHome165c4ps.png"

    image bg dream17_c2ps = "images/ep7/dream17_c2ps.png"
    image bg dream17c1ps = "images/ep7/dream17c1ps.png"
    image bg dream18_c4ps = "images/ep7/dream18_c4ps.png"
    image bg dream18c1_ps = "images/ep7/dream18c1_ps.png"
    image bg dream18c1ps = "images/ep7/dream18c1ps.png"
    image bg dream19c1_ps = "images/ep7/dream19c1_ps.png"
    image bg dream19c1ps = "images/ep7/dream19c1ps.png"
    image bg dream19c1ps_ = "images/ep7/dream19c1ps_.png"

    image bg atHome166_c5ps = "images/ep7/atHome166_c5ps.png"
    image bg atHome166c5ps = "images/ep7/atHome166c5ps.png"
    image bg atHome167c2ps = "images/ep7/atHome167c2ps.png"
    image bg atHome168__c4ps = "images/ep7/atHome168__c4ps.png"
    image bg atHome168_c1ps = "images/ep7/atHome168_c1ps.png"
    image bg atHome168_c5ps = "images/ep7/atHome168_c5ps.png"
    image bg atHome168c4ps = "images/ep7/atHome168c4ps.png"
    image bg atHome169_c5_ps = "images/ep7/atHome169_c5_ps.png"
    image bg atHome169_c5ps = "images/ep7/atHome169_c5ps.png"
    image bg atHome169c5__ps = "images/ep7/atHome169c5__ps.png"
    image bg atHome169c5_ps = "images/ep7/atHome169c5_ps.png"
    image bg atHome169c5ps = "images/ep7/atHome169c5ps.png"
    image bg atHome170c6ps = "images/ep7/atHome170c6ps.png"
    image bg atHome170c7ps = "images/ep7/atHome170c7ps.png"
    image bg atHome171__c5ps21 = "images/ep7/atHome171__c5ps21.png"
    image bg atHome171_c5_ps11 = "images/ep7/atHome171_c5_ps11.png"
    image bg atHome171_c5ps = "images/ep7/atHome171_c5ps.png"
    image bg atHome171c2ps = "images/ep7/atHome171c2ps.png"
    image bg atHome171c4ps = "images/ep7/atHome171c4ps.png"
    image bg atHome171c4ps_ = "images/ep7/atHome171c4ps_.png"
    image bg atHome171c5__ps = "images/ep7/atHome171c5__ps.png"
    image bg atHome171c5_ps22 = "images/ep7/atHome171c5_ps22.png"
    image bg atHome171c5ps_ = "images/ep7/atHome171c5ps_.png"
    image bg atHome171c5ps12 = "images/ep7/atHome171c5ps12.png"
    image bg atHome172c3ps = "images/ep7/atHome172c3ps.png"
    image bg atHome172c4ps = "images/ep7/atHome172c4ps.png"
    image bg ep7carlos = "images/ep7/carlos_ps.png"

    label episode7:
        scene black with Dissolve (1.0)
        scene bg atHome142c4ps with dissolve
        b "{i}I wonder what Scarlett has on her mind, her behavior is completely unpredictable. I don't know what I should do in this situatuon, I'd gladly fuck all the brains out of her after that little performance at the cafe, I mean what can be more obvious sign that she wants me ?!"
        b "{i}But she is Julie's girlfriend and I don't want to ruin these lesbian relations. I guess semi-lesbian sounds more correct considering all the facts.."
        b "{i}Redheads.."
        b "Ok girls, I'm comming !"
        s "Yes [bro] come inside us.."
        j "Scarlett !"
        s "I mean inside the room.."
        menu:
            "Open the door":
                play sound ("music/sounds/phoneRing.mp3")
        "{i}{b}PHONE RINGING"
        scene bg atHome142_c4ps with dissolve
        b "{i}Coordinator is calling. I have to answer the call, he probably has some new and importaint information about currnet situation. Last time we talked about that fancy suitcase with a bunch of stuff in it and..we also talked about Antonio the betrayer.. I wonder how many more traitors still out there, whom can I trust..{/i}"
        menu:
            "Answer the call":
                scene bg atHome142__c4ps with dissolve
        b "hello.."
        $ renpy.music.play("music/suspenseTheme.mp3", channel=1, loop=True, fadein=3)
        c "{i}..."
        extend "..."
        b "hello..??"
        c "{i}[bro] is that you ? I hardly recognize your voice, why are you whispering ?"
        b "ahm..it's not quite convenient for me to talk right now.."
        c "{i}Why, what happened ? Is everything ok, where are you ?"
        b "{i}*Strange, he usually don't ask that many questions.. I wonder why he is being so curious. Considering current circumstances it all seems suspicious..*"
        c "{i}[bro], are you still on the phone ?! I need to know where are you and what is going on.."
        menu:
            "Tell the truth":
                b "yes, everything is fine, i'm at my safe house it's just two girls at my bedroom and.."
            "Lie":
                b "yes, i'm at my girlfriend's apartment.."
                c "{i}Didn't know you have one. Where does she live ?"
                b "why..?"
                c "{i}I'm asking because tracker shows that current location of suitcase is somewhere around your safe house area. So it's either you left the case at your place and went to your GF, which would be completely irresponsible from you or she lives next door to you."
                b "{i}*they know..they've been tracking me all this time since I got the case..*"
                c "{i}Probably I had to tell you this earlier, the case has a transmitter and we could track it if it got to the wrong hands. Unfortunatelly it's not that accurate as we would want to, it shows approximate area of 50 meters about its location, but anyway it's better than nothing."
                b "ahm yeah, we are actually neighbours  but anyway I didn't forget about the importance of keeping the case safe, so I took it with me and put some stuff from sex shop inside for.."
        c "{b}Interrupts:{/b}{i}\nI don't need any details about how you spend your free time. All I am interested in is whether or not you keep the case and its contents at the safe place"
        b "oh, don't worry about that, I always keep an eye on it.. suitcase and the contents are completely safe..totally..almost.."
        c "{i}What ?!"
        b "ok..I had to leave the gun at the bank in order to safely pass police inspection, otherwise they would have taken it from me. So asked the manager to hide it. I'll take it back tomorrow at the morning"
        c "{i}Well, that is bad, because now you'll have to go on the mission without your 'toy'. No shootout is expected but anyway it would be more rational for you to have it just in case"
        b "{i}*shit..looks like I got myself into inconvenient situation. I hope it will be easy one..*"
        b "what are my objectives ?"
        c "{i}We caught Antonio, the guy who sold out information about recent meeting at the warehouse. I don't think that I should remind you what price it cost us"
        b "no need in this, unfortunately I remember that day even better that I would want to.."
        scene bg m6c9psN with cumFlashLong
        b "{i}I still remember their faces..."
        scene bg atHome142__c4ps with fade
        c "{i}I want you to go to our 'Meetings Center' so you and traitor could have a productive conversation regarding his new friends"
        b "why me ? I'm not that good at interrogations so if he didn't say anything yet I doubt that.."
        c "{i}Our man Carlos has already started 'warming up' Antonio, but it turned out that he is stubborn one. We decided to draw you into this for so called 'good cop bad cop' routine, and besides you're the last person he talked to before he betrayed us"
        b "you don't think I'm involved into this do you ?"
        c "{i}..."
        c "{i}Make him talk, I'll send you the address and password for Carlos via text message. I believe you three will have a productive conversation. Time waits for no one so hurry up.. And..Be careful {i}{b}\nEND OF CALL"
        scene bg atHome142_c4ps with dissolve
        b "{i}Why do I have a bad feeling about all this..."
        $ renpy.music.stop(channel=1, fadeout=5)
        scene bg atHome143c20ps with fade
        j "What takes him so long ?! I mean.. Wait, what am I saying ?!.. I'm completely naked waiting for my [brother] to come in and see me like this..Oh my god, my heart is racing right now !"
        s "Relax Julie, he is not going to punish us, we haven't done anything bad yet.. Actually I wouldn't mind some spanking, it turns me on so bad, my pussy gets wet in a few seconds.."
        j "Oh no.. I can't do that Scarlett, it all does seem like a bad idea !"
        b "Girls I have to go, work is calling. See you later.."
        play sound ("music/sounds/doorClose.mp3")
        scene bg atHome141c3_ps with fade
        "{i}{b}DOOR CLOSES"
        $ renpy.pause()
        scene bg atHome144c2ps with fade
        $ renpy.music.set_volume(0.5, delay=0, channel=1)
        $ renpy.music.play("music/scarlettTheme.mp3", channel=1, loop=True, fadein=0)
        j "Are you out of your mind Scarlett ?! Thanks god [bro] had to left"
        s "Didn't you like it Julie ?! I thought you are sexually open-minded and willing to experiment in bed"
        scene bg atHome144c20ps with fade
        j "Of course I liked it and I'm into such new things regarding sex but he is my [brother] Scarlett ! You can't go straight to the business and drag him into bed like this !"
        $ renpy.pause()
        scene bg atHome144c1ps with fade
        s "Hm, you probably right.. Next time I'll send him an invitation to join us via e-mail"
        j "It's not what I meant !"
        s "Why not, at least he'll be able to fit our tight pussies into his tight schedule.."
        $ renpy.pause()
        scene bg atHome145c2ps with fade
        j "Stop it Scarlett, it's an important conversation and I want you to be a little more serious"
        s "And I want you to be a little more fun and relaxed Julie.."
        scene bg atHome146c1ps with fade
        s "Babe, I know your temper and how you like to control anything in your life, but let me tell you something I learned about sex - it's better lose control and go wild while you're having it"
        scene bg atHome145c1ps with dissolve
        s "There is no perfect time or correct formula for this - you have to unleash your emotions and enjoy the feelings. Stop nervouse and thinking thousand thoughts, throw everything out of your head, and just give it a try - nothing bad will happen I promise you."
        j "You're so confident about it, what makes you think that he won't kick us both out ?"
        scene bg atHome145c2ps with fade
        s "Please, Julie you are underestimating yourself. Look at you, you are as hot as hell, girl - the worst case that might be is your [brother] simply be acting like nothing happened."
        s "The situation will indeed be awkward but you have to start with something if you decide to get what you want. By the way, I suspect that he already started to show his interest towards you, didn't he ?"
        scene bg atHome146c2ps with dissolve
        j "Hm let me think, I guess there was something I'd call unusual and almost inappropriate in [bro]'s behavior.. Well.."
        if bathroom_naked != 0:
            j "The day I first came in this apartment he entered the bathroom when I was asking for a towel after the shower, so he literally saw me naked"
            scene bg atHome146_c2ps with dissolve
            s "Good start, you shouldn't be shy next time when you will be naked in front of him"
            j "Do you really think this will be a good idea ?"
            s "Totally, girl. Let him get used to your naked, curvy and sexy body. I would recommend you stop wearing any tops, t-shirts and bras while you two are alone at home. Let him enjoy your sweet bobbies"
            j "Okay, ahm.."
            scene bg atHome146c2ps with dissolve
        if ep2kissLips != 0:
            j "One night [bro] kissed me on the lips, but it was more likely a caring kiss, no tongue involved"
            scene bg atHome146_c2ps with dissolve
            s "A kiss is a kiss, Julie - congratulations first base successfully passed"
            j "I doubt it Scarlett, he probably wanted it to be like a 'good night, sweet dreams' thing, nothing perverted"
            s "Or he would want you to think like that. You are an adult now Julie every kiss that is not on the forehead or cheek could mean something.."
            scene bg atHome146c2ps with dissolve
            j "Maybe you are right.."
        if ep3checkingOut != 0:
            j "The day me and him went to the gym, he was staring at my butt and he said that it looks alluring, can you believe this ?"
            scene bg atHome146_c2ps with dissolve
            s "Girl, your ass is a masterpice ! If I were a guy I would be fucking you right inside it all the time"
            j "Come on Scarlett, you know that your butt is as good as mine"
            s "Aw, baby that is so sweet of you.."
            scene bg atHome146c2ps with dissolve
            j "So, what else.."
        if ep3pussyTouched != 0:
            j "I think that he touched my pussy as well.."
            scene bg atHome146_c2ps with dissolve
            s "No way ! Give me the details, please !"
            scene bg atHome146c2ps with dissolve
            j "Well it may sound like he did it on purpose but I think he just was trying to help me deal with a spasm in my thigh"
            scene bg atHome146_c2ps with dissolve
            s "Yeah-yeah, and my [father] was helping to warm up my pussy from the inside with his huge dick, ha-ha. We girls always can tell if such things were done on purpose or accidently, otherwise you wouldn't notice this little accident, would you ?"
            scene bg atHome146c2ps with dissolve
            j "I guess you're right.."
        scene bg atHome147c7ps with fade
        if bathroom_naked + ep2kissLips + ep3checkingOut + ep3pussyTouched == 0:
            j "I guess [bro] showed no signs of interest in me"
            s "Don't worry Julie, I had to start from the beginning with my [father] as well. You already know how to seduce, so use your charm and make him think of you as a woman"
        else:
            j "Ahm.. Looks like that is it"
            s "Well so far so good baby"
        s "Keep in mind that if he didn't have sex with you yet it doesn't mean he is not thinking about it, girl. You two just need to start having a little fun together it's just a matter of who is going to do the first step."
        scene bg atHome147c4ps with fade
        j "I don't know Scarlett.. I'm still not sure that this is a good idea, it all seems wrong"
        s "You can't go against the nature Julie, if you really have some feelings towards [bro] you should surrender to them. After all we are all just males and females"
        s "To be honest I envy you a little. Those feelings and emotions, the first time when you are being taken from behind like a little innocent girl are indescribable.."
        scene bg atHome147c6ps with fade
        j "You describe this so persuasively Scarlett.. Actually I'm really starting to get turned on about this whole idea, and you know that when I'm turned on I'm losing control over my body. I guess I'm ok to have a threesome with you and [bro] next time, my pussy gets incredibly wet only from that idea alone"
        scene bg atHome147c7ps with fade
        s "I know Julie, however I think there is no need to rush, I mean your first time with your [brother] should be more intimate, it's only about you two.."
        scene bg atHome148c5ps with fade
        j "Honestly I would love to share this momet with you.. Besides I didn't have any experience with men so I was hoping you will be able to guide me if I'll do something wrong.."
        s "I understand baby, everything will be ok. I just remembered how tender and sensual was my first time with my [father], we enjoyed each other like there are only two of us in the whole world.. He was so deep inside of me and all that I could think of at that moment was his huge throbbing dick in my tight virgin pussy."
        scene bg atHome147c7ps with fade
        s "I just don't want to be a 'third wheel' during your first time.."
        scene bg atHome147_c7ps with dissolve
        s "But after this.. I have a feeling that [bro] will be fucking us like we are his personal little whores. I bet we will greedily compete for whose mouth he should cum in or whose pussy will get fucked first.."
        scene bg atHome148c5ps with fade
        j "You are so bad Scarlett you know that ?! You can almost make me cum only using the words that come out from your mouth.."
        s "You know what else I can do with my mouth, don't you.."
        scene bg atHome147c5ps with dissolve
        j "Oh yes, baby eat that pussy out.. Come to me.."
        $ renpy.music.stop(channel=1, fadeout=5)
        scene black with Dissolve (2.0)
        jump ep7Trap
        return

    label ep7Trap:
        $ renpy.notify ("O gecenin ilerleyen saatlerinde..")
        $ renpy.pause()
        $ renpy.music.set_volume(1.5, delay=0, channel=3)
        $ renpy.music.play("music/sounds/engineWorking.mp3", channel=3, loop=True, fadein=0)
        $ renpy.music.play("music/trapTheme.mp3", channel=1, loop=True, fadein=0)
        scene bg Trap1c1ps with Dissolve (2.0)
        b "{i}Looks like this is the right address.. I have to admit that the place doesn't seem abandoned, it's cozy enough for tet-a-tet conversations that include tortures. No wonder that it's located far away from residential buildings, last sign of civilization was few miles away. No neighbours and no witnesses.. Smart.."
        b "{i}Okay, I have to find Carlos first, he must be somewhere around here."
        menu:
            "Look for Carlos":
                $ renpy.music.stop(channel=3, fadeout=3)
                play sound ("music/sounds/carDoorClose.mp3")
        scene bg Trap2c3ps with fade
        $ renpy.pause()
        b "{i}Nice car, I remember those days when I just joined the gang and had to use public transport to move around the city. Me and other new members of the gang were always jealous of those who already proved their loyalty and were given the exact such cars."
        b "{i}Now I have completely different car, most of those guys I started working with are either dead, behind the bars or forgot the word 'loyalty'. Times change indeed.. "
        b "{i}Hope Antonio will give me an explanation why he betrayed us. For his own good, maybe the truth will help to save his life."
        menu:
            "Knock":
                play sound ("music/sounds/garageDoorKnock.mp3")
        scene bg Trap3c2ps with fade
        "{i}{b}KNOCK-KNOCK-KNOCK-KNOCK-KNOCK"
        b "{i}..."
        $ renpy.pause()
        menu:
            "Knock again":
                play sound ("music/sounds/garageDoorKnock.mp3")
        "{i}{b}KNOCK-KNOCK-KNOCK-KNOCK-KNOCK"
        "{b}??????{/b}\nWho is there ?"
        b "{i}Let's see..The password was 'silence is golden..not'"
        b "Silence is golden..Not.."
        "{b}??????{/b}\n..."
        play sound ("music/sounds/garageDoorOpen.mp3")
        scene bg Trap3_c2ps with Dissolve(1.75)
        scene bg Trap3__c2ps with Dissolve(1.75)
        $ renpy.pause()
        b "You must be Carlos, hi.."
        "{b}Carlos{/b}\n..."
        b "I'm [bro]. I'm here to talk to Antonio, could you please take me to him ?"
        scene bg Trap4c4ps with fade
        "{b}Carlos{/b}\nDid you come alone ?"
        scene bg Trap4_c4ps with dissolve
        b "Yeah, why ?"
        scene bg Trap4c4ps with dissolve
        "{b}Carlos{/b}\nIt's me who usually asks questions here.."
        scene bg Trap4_c4ps with dissolve
        b "Glad to hear that, but looks like today I'm going to do your job, pal"
        scene bg Trap4c4ps with dissolve
        "{b}Carlos{/b}\nAre you telling me that there is no one else in the car ?"
        scene bg Trap4_c4ps with dissolve
        b "Do I look like Antonio ?! Why are you asking these questions, I already told you the password, it should be more than enough."
        scene bg Trap5c4ps with Dissolve(.75)
        "{b}Carlos{/b}\nOf course you did, it's just my professional curiosity, don't take it personal. Also I think that this fucking situation with those shitty traitors makes me paranoid. Probably I'll take the vacation when we deal with those rats.."
        scene bg Trap4c4ps with dissolve
        "{b}Carlos{/b}\nThere are only few of them left, right ?"
        menu:
            "It's not that easy":
                b "Rats are only half of the problem, we also need to win a war against 'uninvited guests'.. Anyway, take me to Antonio, I want to deal with it fast.."
            "I wouldn't mind too":
                b "I don't remember what the 'vacation' word means, but I wouldn't mind at least one day off.. Anyway, take me to Antonio, I want to deal with it fast.."
        scene bg Trap4__c4ps with dissolve
        "{b}Carlos{/b}\nSure thing [bro], be my guest. Welcome to the house of 'truth', ha-ha.. We've been waiting for you.."
        $ renpy.music.stop(channel=1, fadeout=2)
        scene black with Dissolve(1.5)
        play sound ("music/sounds/garageDoorOpen.mp3")
        $ renpy.pause()
        scene bg Trap6c6ps with Dissolve(1.5)
        $ renpy.music.play("music/trapTheme2.mp3", channel=1, loop=True, fadein=2)
        "{b}Carlos{/b}\nFollow me, this place is a mess. One wrong move and you will break your neck so watch out and look under your feet.."
        b "Okay thanks.."
        $ ep7carlos = 0
        menu:
            "Ask about him":
                $ ep7carlos += 1
                b "How long have you been working in our business ? Even though I already work here about 5 years, I don't think we've met before on the general meetings"
                "{b}Carlos{/b}\nAhm.. Long enough, pal.. Can't tell you the exact date, probably more than a year that's for sure.."
                b "I see.. By the way the car is awesome, I remember the time when I just started working here, I couldn't even think that I will get one in 'more than a year'... I got mine just few month ago"
                scene bg Trap6c5ps with fade
                "{b}Carlos{/b}\nHuh, hell yeah your car is badass but don't show off that explicitly next time okay ? I've always envied you guys: new cars, big guns, hot chicks - what can I say I studied the wrong profession.."
                b "What are you talking about ?"
                scene bg Trap7c7ps with fade
                "{b}Carlos{/b}\nI'm saying that I still didn't get at least shitty motorbike for my service.. I always have to take a cab or walk in order to get to this fucking place.."
                b "Actually I was talking about the car parked outside the building, isn't it yours ?"
                scene bg Trap7__c8ps with fade
                "{b}Carlos{/b}\nWhat car..?{nw}{w=1.0}"
                b "...{nw}{w=1.0}"
                scene bg Trap7_c8ps with dissolve
                "{b}Carlos{/b}\nOh, do you mean that piece of shit.. That junk can't be called a car, pal.. The shit doesn't even start for months, probably the engine is fucking dead, the only way it may move - is if someone decides to tow it on a rope right to the dump.."
                b "Is it ? I'd never have thought, the car looks completely ok to me"
                scene bg Trap7c8ps with dissolve
                "{b}Carlos{/b}\nAppearances are deceptive [bro], believe me, that garbage already rusts here for a long time.. I bet I'll cut off my balls and eat them if that car will ever move again without proper repair.."
                b "You know how to convince people...{nw}{w=1.5}"
                scene bg Trap7__c8ps with dissolve
                "{b}Carlos{/b}\nLet's go, it's time for you to say 'hi' to Antonio..."
            "Ask about Antonio":
                b "Where did you find him, I heard nothing about those who decide to 'change the side' they just disappear. I was wondering how you managed to caught him"
                "{b}Carlos{/b}\nWell, ahm.. That's a fucking mystery to me as well. By the time I arrived he has already been here so I have nothing to do with his capturing.. Probably 'hunters' delivered him here to me as always.."
                scene bg Trap7c7ps with fade
                "{b}Carlos{/b}\nActually I wouldn't mind to have a car and deliver clients personally, to be honest..."
                "{b}Carlos{/b}\nBut I'm not a 'hunter' or 'fighter' like you - I'm an interrogator.. We are not supposed to have a car in order to do our job.."
                b "You don't have one..? Strange.. It seems unfair to me"
                "{b}Carlos{/b}\nThat's what I'm talking about, it's a fucking disgrace that I'm still not given at least shitty car after all these years of service. I can't even afford to buy one for myself because the 'coordinator' pays me too fucking little"
                b "I see..{nw}{w=1.0}"
                scene bg Trap7_c8ps with fade
                menu:
                    "Ask about the car":
                        $ ep7carlos += 1
                        b "Do you know whose car is parked outside the building, I have a feeling that I've already seen it somewhere.."
                        scene bg Trap7__c8ps with dissolve
                        "{b}Carlos{/b}\nThe car?... Ehm, I think that this is the car.. Ahm that Antonio was delivered on"
                        b "The 'hunters' left it here and just walked away..?"
                        scene bg Trap7_c8ps with dissolve
                        "{b}Carlos{/b}\nYes, right - they left the car here, it probably belongs to Antonio. Or should I say belonged to him.."
                        b "Why is that ?"
                        scene bg Trap7c8ps with dissolve
                        "{b}Carlos{/b}\nWell after I 'talked' with him a little I doubt that he will ever be able to walk again and use his legs to control a car.."
                        scene bg Trap7__c8ps with dissolve
                        b "As you say..{nw}{w=1.0}"
                        "{b}Carlos{/b}\nCome on, he's right behind that door.. It's time for you to join Antonio"
                    "Ask about Antonio":
                        scene bg Trap7__c8ps with dissolve
                        b "Speaking about Antonio, did he tell you at least something useful ? Like why did he do that or who are those people he decided to work with ?"
                        scene bg Trap7_c8ps with dissolve
                        "{b}Carlos{/b}\nNah, the punk turned up a tough one."
                        scene bg Trap10c9ps with fade
                        b "I hope I will be able to get at least something from him"
                        "{b}Carlos{/b}\nThe way I see it, it'd be better if you wouldn't show up here at all. You see, the moment I barely started to have fun with Antonio I got a call and was told to take it easy on him. Otherwise he'd already be begging to stop and I would knew everything we need"
                        "{b}Carlos{/b}\nBut coordinator clearly told me that I have to make sure that the rat will be able to recognize you when you show up."
                        b "Recognize..?{nw}{w=1.0}"
                        scene bg Trap10c9_ps with fade
                        "{b}Carlos{/b}\nMy methods are truly effective and never failed me. But this time I couldn't use them... I usually gouge out the eyes of my clients right from the begining. After they finish yelling in pain they tell me everything"
                        "{b}Carlos{/b}\nWhen they can't see nothing but darkness - my voice becomes for them this tiny bridge between life and death, that is how I like to think about it.. Not everyone knows that the Truth is blind as much as the Justice..."
                        b "...{nw}{w=1.0}"
                        scene bg Trap10_c12ps with fade
                        "{b}Carlos{/b}\nBut unfortunately with Antonio I had to use that old primitive tools: smashing bones with a sledgehammer and cutting off the limbs using a chainsaw.."
                        b "Is he.. Still able to talk after what you did to him..?"
                        "{b}Carlos{/b}\nSure he is, I only broke his knees and cut off his ankles, had to make sure that even he will manage to untie himself he won't run too far.."
                        scene bg Trap10__c12ps with dissolve
                        "{b}Carlos{/b}\nDon't be shy, he is waiting for you right behind the door. I'm sure he will be glad to see your face."
                        extend " For the last time..."
                        b "What will you do ?{nw}{w=1.0}"
                        scene bg Trap10_c12ps with dissolve
                        "{b}Carlos{/b}\nI'll be waiting right here, don't hesitate to call me if you need some help. Good luck with your first interrogation, pal..."
                        scene bg Trap11c13ps with fade
                        b "{i}This guy is completely nuts - he is talking about tortures like this is some kind of entertainment.. On the other hand I don't know what would happen to me if I had to do this job every day. As the saying goes 'if you gaze long into an abyss, the abyss also gazes into you...'"
                        b "Ok, I'll be right back{nw}{w=1.0}"
                        "{b}Carlos{/b}\nTake your time, who knows maybe you will enjoy it as much as I do..."
                        b "I doubt it {nw}{w=1.0}"
                        menu:
                            "Open the door":
                                play sound ("music/sounds/metalDoorOpens.mp3")
                        jump ep7TrapEnd
        menu:
            "Continue":
                scene bg Trap7__c8ps with dissolve
                b "Speaking about Antonio, did he tell you at least something useful ? Like why did he do that or who are those people he decided to work with ?"
                scene bg Trap7_c8ps with dissolve
                "{b}Carlos{/b}\nNah, the punk turned up a tough one."
                scene bg Trap10c9ps with fade
                b "I hope I will be able to get at least something from him"
                "{b}Carlos{/b}\nThe way I see it, it'd be better if you wouldn't show up here at all. You see, the moment I barely started to have fun with Antonio I got a call and was told to take it easy on him. Otherwise he'd already be begging to stop and I would knew everything we need"
                "{b}Carlos{/b}\nBut coordinator clearly told me that I have to make sure that the rat will be able to recognize you when you show up."
                b "Recognize..?{nw}{w=1.0}"
                scene bg Trap10c9_ps with fade
                "{b}Carlos{/b}\nMy methods are truly effective and never failed me. But this time I couldn't use them... I usually gouge out the eyes of my clients right from the begining. After they finish yelling in pain they tell me everything"
                "{b}Carlos{/b}\nWhen they can't see nothing but darkness - my voice becomes for them this tiny bridge between life and death, that is how I like to think about it.. Not everyone knows that the Truth is as blind as the Justice..."
                b "...{nw}{w=1.0}"
                scene bg Trap10_c12ps with fade
                "{b}Carlos{/b}\nBut unfortunately with Antonio I had to use that old primitive tools: smashing bones with a sledgehammer and cutting off the limbs using a chainsaw.."
                b "Is he.. Still able to talk after what you did to him..?"
                "{b}Carlos{/b}\nSure he is, I only broke his knees and cut off his ankles, had to make sure that even if he will manage to untie himself he won't run too far.."
                scene bg Trap10__c12ps with dissolve
                "{b}Carlos{/b}\nDon't be shy, he is waiting for you right behind the door. I'm sure he will be glad to see your face."
                extend " For the last time..."
                b "What will you do ?{nw}{w=1.0}"
                scene bg Trap10_c12ps with dissolve
                "{b}Carlos{/b}\nI'll be waiting right here, don't hesitate to call me if you need some help. Good luck with your first interrogation, pal..."
                scene bg Trap11c13ps with fade
                b "{i}This guy is completely nuts - he is talking about tortures like this is some kind of entertainment.. On the other hand I don't know what would happen to me if I had to do this job every day. As the saying goes 'if you gaze long into an abyss, the abyss also gazes into you...'"
                b "Ok, I'll be right back{nw}{w=1.0}"
                "{b}Carlos{/b}\nTake your time, who knows maybe you will enjoy it as much as I do..."
                b "I doubt it {nw}{w=1.0}"
                menu:
                    "Open the door":
                        play sound ("music/sounds/metalDoorOpens.mp3")
                jump ep7TrapEnd
            "Stop" if ep7carlos != 0:
                b "{i}It all seems way to suspicious. Most likely Carlos is a traitor and looks like he is luring me into trap. I don't know what he has on his mind but he asked the questions I would ask myself before leading someone into trap. "
                b "{i}He knows that I'm physically superior and he doesn't know whether I have a gun or not, probably that's why he hesitates to attack. I guess he waits for the right moment to stab my back with a knife.{/i}"
                menu:
                    "Attack":
                        b "{b}Not today you piece of shit ! Take this ! {nw}{w=1.0}"
                $ renpy.music.play("music/enemyThemeShort.mp3", channel=1, loop=True, fadein=0)
                play sound ("music/sounds/punchFace.mp3")
                scene bg Trap8c9ps with Fade(0.1, 0.1, 0.35, color="#fff")
                scene bg Trap8c9ps with vpunch
                b "You fucking liar !{nw}{w=0.75}"
                "{b}Carlos{/b}\nArgh !!! Help, Jose !!!{nw}{w=0.75}"
                play sound ("music/sounds/kneeKick.mp3")
                scene bg Trap8_c10ps with Fade(0.1, 0.1, 0.35, color="#fff")
                scene bg Trap8_c10ps with hpunch
                "{b}Carlos{/b}\nOugh..{i}*cough-cough*{nw}{w=0.75}"
                b "Take it, traitor !{nw}{w=0.75}"
                play sound ("music/sounds/punchFace2.mp3")
                scene bg Trap8__c11ps with Fade(0.1, 0.1, 0.35, color="#fff")
                scene bg Trap8__c11ps with vpunch
                b "Get over here punk !{nw}{w=0.75}"
                "{b}Carlos{/b}\nArgh, ouch {i}*cough-cough-cough...*{nw}{w=0.75}"
                play sound ("music/sounds/kneeKick.mp3")
                scene bg Trap9c12ps with Fade(0.1, 0.1, 0.35, color="#fff")
                scene bg Trap9c12ps with hpunch
                "{b}Carlos{/b}\nAaaarh !!!{nw}{w=0.75}"
                b "Die motherfucker !{nw}{w=0.75}"
                play sound ("music/sounds/bodyFall.mp3")
                scene bg Trap9_c13ps with Fade(0.1, 1.5, 1.25, color="#fff")
                "{b}Carlos{/b}\n{i}*Unconscious*\nZzz..{nw}{w=1.0}"
                b "{i}I'd better get out of here, who knows how many more of them are out here..."
                $ renpy.pause(1.0)
                jump episode7home
        return

    label ep7TrapEnd:
        $ renpy.music.stop(channel=1, fadeout=1)
        scene black with Dissolve (2.0)
        $ renpy.music.play("music/warehouseTheme.mp3", channel=1, loop=True, fadein=2)
        $ renpy.music.play("music/sounds/heartBeat.mp3", channel=3, loop=True, fadein=2)
        scene bg Trap11_c14ps with dissolve
        b "What the.. Carlos where are the lights I can't see anything ?!"
        "{b}Carlos{/b}\nOh I'm sorry [bro], forget to tell you.. There are no lights in that room.. and"
        scene bg Trap11_c10ps with fade
        "{b}Carlos{/b}\nthere is no Antonio either, ha-ha...{nw}{w=1.5}"
        b "Is this some kind of stupid joke ?!"
        "{b}Carlos{/b}\nThe only stupid thing here is you, bitch{nw}{w=1.5}"
        scene bg Trap11__c10ps with dissolve
        play sound ("music/sounds/click.mp3")
        b "Huh..?{nw}{w=1.0}"
        "{b}????{/b}\nYou picked the wrong side, punk... Don't you fucking move or I'll shoot you right in the face."
        scene bg ep7carlos with dissolve
        "{b}Carlos{/b}\nEasy Jose, we don't want to kill him, remember ? Nacho asked us to keep him alive until he arrives."
        "{b}Jose{/b}\nThe punk will try to escape, I don't want to point the gun at him all night long"
        "{b}Carlos{/b}\nI'll make sure he won't run away, look after him I'll go get the chainsaw..."
        "{b}Jose{/b}\nYeah, that's a good idea... Lay on the floor with your hands behind the back, bitch ! You may don't know it but you are already dead..."
        $ renpy.music.stop(channel=1, fadeout=2)
        $ renpy.music.stop(channel=3, fadeout=2)
        $ renpy.pause(2.0)
        jump gameOver
        return

    label episode7home:
        $ renpy.music.stop(channel=1, fadeout=2)
        scene black with Dissolve (2.0)
        $ renpy.notify ("Daha sonra evde..")
        $ renpy.pause()
        scene bg atHome149_c2__ps with Dissolve(1.5)
        $ renpy.music.play("music/suspenseTheme.mp3", channel=1, loop=True, fadein=0)
        b "{i}This is madness.. Is anyone left in this city who can still be trusted ? Shit.."
        b "{i}Coordinator said that the suitcase has a transmitter which means that they could find me dozen times already if they wanted to.. At the same time it's already second occasion when he sends me right into the fucking mess."
        b "{i}How do I know that he is still on my side...?! Even if he is, I have no guarantee that they didn't kill him and now are just using his phone.. They also could have taken him as hostage and order him what to do and what to tell me and other guys.. Damn.."
        $ renpy.pause(1.0)
        b "{i}Looks like I'll have to take a chance..."
        menu:
            "Make a call":
                play sound ("music/sounds/dialPhone.mp3")
        scene bg atHome149c5ps with dissolve
        b "...{nw}{w=2.5}"
        c "{i}Report"
        scene bg atHome149_c2_ps with dissolve
        b "It was a trap, it was a fucking trap.. I was lucky that I managed to get out of there alive. Not exactly the kind of report you've been expecting I guess, sorry to disappoint.. Going on a missions is a one thing, but going into traps - I'm done with this.."
        c "{i}Calm down, [bro]. I've been tracking your movement and been waiting for your call. Is the contents of the case still intact ?"
        scene bg atHome149_c5ps with dissolve
        b "Are you kidding me ? I thought you would ask whether I am okay or not. What if I got shot ?!"
        c "{i}I hope that you're okay and intact. Since you decided to call me from your safe place I suspect that you have something important to tell but unfortuntaelly it all won't matter if the contents of the case isn't safe."
        scene bg atHome149c5ps with dissolve
        b "Yes, it's safe. I didn't open it anymore... Shit I nearly died again, so what's the difference, maybe I should have open it and use one of those things ?! Damn.. I don't understand what is going on anymore. No one can be trusted, looks like it is a dead end.."
        c "{i}Take it easy, first things first. Why did you decide that it was a trap ?"
        scene bg atHome149_c2_ps with dissolve
        b "Why did I decide that ?! Because it was so damn obvious, the whole place looked like a fucking trap ! Of course there was no billboard with inscription 'Welcome [bro] it's a Trap !'. To be honest the place looked very incomplete without it, but somehow I managed to figure that out anyway."
        c "{i}Any details ?"
        b "You can call it premonition or intuition, doesn't really matter. Carlos was nervous and something was definitely wrong about him..."
        c "{i}You can't make conclusions whether or not that was a trap based on your intuition alone, the meeting was incredibly important and.."
        scene bg atHome149_c5ps with dissolve
        b "{b}Interrupts:{/b}\nFine if you don't belive me, try to call and talk to Carlos - let him tell you his story.. But honestly I doubt that he will pick up the phone again"
        c "{i}Did you kill him ?"
        scene bg atHome149_c2_ps with dissolve
        b "No I just helped him to lose his consciousness.."
        c "{i}If he wanted to kill you he would have done it before you entered the building."
        scene bg atHome149c5ps with dissolve
        b "Listen, I don't really know how to explain you this but consider the facts and just 'do the math'"
        b "Yes, he could have killed me right from the begining, but he didn't know whether I have a gun or did I came there alone. Plus I'm sure that they didn't want to kill me right away because they wanted to get at least some information from me, that is why he tried to lure me into the building."
        c "{i}That's not a solid proof"
        scene bg atHome149_c2_ps with dissolve
        b "Agreed, these facts are just parts of a whole picture.. The most suspicious detail among all this was the car parked nearby"
        c "{i}...{nw}{w=0.5}"
        b "It was one of those cars that were given to the best of us few years ago. Carlos made a mistake by saying that the car doesn't belong to him"
        c "{i}As far as I know he really didn't get one, he joined our 'team' not so long ago."
        scene bg atHome149_c5ps with dissolve
        b "You told that only three of us would be at the place: me, Carlos and Antonio, right ?"
        c "{i}That is correct"
        scene bg atHome149_c2_ps with dissolve
        b "So why the hell that car was doing there ?! Far away from the city, in the middle of the night. I doubt that Antonio himself decided to drive there, surrender and start torturing himself in front of Carlos."
        b "I bet that those bastards just didn't think that I could notice and start asking the questions about the car. Carlos told the truth, the car isn't his, but by that he 'buried' himself."
        scene bg atHome149_c5ps with dissolve
        b "Probably someone else who worked with us before was there.. I'm sorry, I didn't want to stay there waiting for the bullet to meet with my head, so I decided to get out of there as soon as possible."
        c "{i}...{nw}{w=1.0}"
        scene bg atHome149c5ps with dissolve
        c "{i}Now your words start to have sense.. Someone named Jose, one of our oldest and loyal 'employees' stopped communicating day ago.. Shit, that was our last chance.."
        scene bg atHome149_c2_ps with dissolve
        b "I doubt that it really was a chance. I don't think that Antonio really was in that building and could tell me something. Most likely he's already dead."
        c "{i}If that is true..{nw}{w=1.0}"
        scene bg atHome149c5ps with dissolve
        c "{i}If he really is dead that means that we.. that I.. don't know what I'm going to do..."
        b "...{nw}{w=0.5}"
        c "{i}I had that last bit of hope that information from Antonio will lead us to something, something that we could use as an advantage.. But now, looks like only few of us left - I don't think there are at least five loyal people left.."
        scene bg atHome149_c2_ps with dissolve
        b "What ?!"
        c "{i}I didn't want to tell you this, but each and every guy I've sent to a misson stopped answering the calls. They either 'switched the side' or are already dead..."
        b "No.. I can't belive this.. What about the boss ?! What about other guys ?! Are you saying that {b}all{/b} of them are..."
        c "{i}I didn't get any news from boss since he went to that fucking meeting, which meens that.. Most likely he is already dead.. I don't have further instructions, don't have the resources.. I don't have any loyal people to coordinate, except you.. Looks like this is it.. "
        scene bg atHome149_c5ps with dissolve
        b "This can't be true.. Is it really no one left ?!"
        c "{i}I have to apologize, I shouldn't have said that.. I need some time to think about this whole mess..."
        scene bg atHome149_c2_ps with dissolve
        b "What are you talking about ?! Think about what ?!"
        c "{i}Think about the way we both can make it out of here alive, considering given circumstances... Here is some free advice for you - take back your weapon and never lose it again. Keep the 'case' with you for now, who knows maybe I'll find a safe way for us to use it."
        c "{i}We have no chances to win this war, but maybe we will manage to at least save our lives... Be careful, I'll call you later"
        scene bg atHome149_c5ps with dissolve
        b "Wait !"
        "{i}{b}END OF CALL"
        scene bg atHome149c5ps with dissolve
        b "{i}Shit there are to many question without an answer in my head right now.."
        scene bg atHome149_c2__ps with dissolve
        b "...{nw}{w=0.5}"
        scene bg atHome149__c2__ps with dissolve
        b "{i}They won't answer themself magically and I'm to tired to think clearly.. I guess I'll take a shower and will go to sleep.. Fuck, one of the worst days in my life.."
        $ renpy.pause(1.0)
        $ renpy.music.stop(channel=1, fadeout=3)
        scene black with Dissolve (2.0)
        $ renpy.notify ("Bir süre sonra..")
        $ renpy.pause(2.0)
        $ renpy.music.set_volume(1.0, delay=0, channel=1)
        $ renpy.music.play("music/rainTheme.mp3", channel=1, loop=True, fadein=0)
        $ renpy.music.set_volume(0.5, delay=0, channel=3)
        $ renpy.music.play("music/mainTheme2.mp3", channel=3, loop=True, fadein=0)
        scene bg atHome150c2ps with Dissolve(2.0)
        $ renpy.pause(1.0)
        b "{i}Now it's better... I love that feeling of a freshness after shower, the head starts to fill up with right thoughts. Anxiety and fear fade away, whole body starts relaxing and it no longer seems that there is some danger, which not so long ago was one step away from you, right behind your back..."
        b "{i}Coordinator's words made me think of something, I've never thought before... I have a mixed feelings about this... For the one hand it's inevitability of our defeat causes that desperate feeling of loss, especially knowing that the truth is on our side... But the truth is 'everyone has his own truth'..."
        b "{i}For the other hand I can't really tell that those things what I've been doing all these years can be called righteous and are worth fighting for... Even after all this time, I still have a feeling that I don't belong here, like there is something else awaiting for me... I should finally stop running from myself... "
        b "{i}I have to admit that I'm fed up with all this criminal life... Life on the edge looks tempting and interesting: being above the system and experiencing all the benefits of a lawless life sounds amazing... Until you realise that this life can come to an end any moment..."
        b "{i}The saying goes 'The brighter the fire, the faster it ends'... Sometimes it's so fast that you don't have enough time to enjoy it and warm up - in my case it's a spark, not a fire and I guess no matter how bright the flash from a spark is - it won't warm up nobody even those who you love..."
        b "{i}So I should ask myself to what end all this ?!"
        $ renpy.pause()
        b "{i}I hope that it's not too late for me to start over and begin to live a normal life. For the first time in a while I have a real chance to stop endangering my [family] and finally be together with them..."
        if ep5killCounter != 0:
            b "{i}I have the 'blood on my hands', had to kill that son of a bitch in the bank... But I'm ready to take responsibility for my actions, especially when it comes to my [family]..."
        else:
            b "{i}I don't have the 'blood on my hands', there is always a way to avoid killing... I don't want my [family] to pay for my sins, they must not suffer because of me..."
        play sound ("music/sounds/thunder2.mp3")
        scene bg atHome150_c2ps with dissolve
        "{i}{b}THUNDER BLASTS{nw}{w=0.75}"
        $ renpy.pause(1.0)
        b "{i}Damn... It will be hard to fall asleep 'in such silence'... I hope that I'm exhausted enough to doze off in between thunderclaps..."
        $ renpy.pause(1.0)
        play sound ("music/sounds/thunder1.mp3")
        "{i}{b}THUNDER BLASTS{nw}{w=0.75}"
        j "{b}[bro]...{nw}{w=1.0}"
        scene bg atHome150__c2ps with dissolve
        b "{i}...{nw}{w=1.0}"
        j "{b}[bro] are you home..?"
        $ ep7JulieMutual = 0
        menu:
            "Answer Julie":
                b "Yes Julie, I'm here..."
        j "{b}Can you please come inside for a minute..?"
        menu:
            "Yes":
                $ ep7JulieMutual += 1
                b "Sure thing little one, I'm coming to you"
            "No":
                b "I was trying to sleep, you should be sleeping too. It's 3 AM..."
                play sound ("music/sounds/thunder1.mp3")
                j "{b}Please..."
                scene bg atHome150_c2ps with dissolve
                b "Okay [sis], on my way"
        $ renpy.pause(0.5)
        scene black with Dissolve (2.0)
        jump ep7Julie
        return

    label ep7Julie:
        play sound ("music/sounds/openDoor.mp3")
        $ renpy.pause(1.0)
        $ renpy.music.set_volume(0.65, delay=0, channel=3)
        $ renpy.music.play("music/afterDarkShortTheme.mp3", channel=3, loop=True, fadein=2)
        scene bg atHome151c2ps with Dissolve (2.0)
        $ renpy.pause()
        j "Hey..."
        b "Hi Julie... {nw}{w=0.75}"
        scene black with fade
        b "Oops"
        b "I'm sorry... I probably came in too early, you I did not have time to put on all of your cloth..."
        j "It's okay [bro].. You can open your eyes"
        b "Are you sure..?!"
        j "Yes.."
        scene bg atHome152c1ps with Dissolve (2.0)
        j "I just didn't feel like putting it on, sleeping half-naked feels more comfortable also it's dark in the room and one can barely see something here. Besides you've already seen me like this plenty of times, so why bother.."
        $ renpy.pause(1.0)
        b "Well.. It was long time ago when you were a kid.. But if you are okay with it.."
        scene bg atHome152c_1ps with dissolve
        j "I'm totally okay with it.."
        b "Fine.. Ahm, you called me.. Do you need something, any help ?"
        j "Yes, I was wondering.. If you could stay with me for a while until the storm passes by.."
        play sound ("music/sounds/thunder2.mp3")
        scene bg atHome153c1ps with dissolve
        j "You do know that I always been afraid of it, since the childhood.."
        scene bg atHome152c1ps with dissolve
        b "I do remember that you've been afraid of the storm, but I thought that since I left.. Since you grew up - you no longer afraid of it.."
        scene bg atHome153c1ps with dissolve
        j "Yeah, I know that it's silly to be afraid of such things at my age.. Probably it's not only because of storm.. I'm still scared after what happened at the bank.. I can't forget the words that scum said after he pointed the weapon on us.. He started to describe what they are going to do with me and Vicky.."
        j "I just imagined what could happen if you weren't there at that moment.. {i}\n*sob-sob...*"
        b "There there little one, come here, let me hug you.."
        scene bg atHome152c_1ps with dissolve
        j "Gladly.."
        scene black with Dissolve (1.5)
        scene bg atHome154_c1_ps with Dissolve (1.5)
        $ renpy.pause()
        b "Never think of such things again, okay ?! I'm here with you, I won't let anyone hurt you, I promise."
        j "I know.. It's such a pleasure to feel safe and secure, knowing that you are always here and will protect me. I fear nothing when you cuddle me like this..."
        b "Don't get used to it too much, there is still no cure from the 'Cuddling Addiction'"
        scene bg atHome154_c1ps with dissolve
        j "Ha-ha, I know. I've already been searching for it at the local pharmacy"
        $ renpy.pause(1.0)
        b "I won't ever let you go Julie.."
        play sound ("music/sounds/thunder2.mp3")
        j "I know, [bro].. I won't either.."
        scene bg atHome154c1ps with dissolve
        $ renpy.pause(1.0)
        j "I can feel the warmth of your body.."
        scene bg atHome154c2ps with fade
        $ renpy.pause(1.0)
        j "Your arms are so big and strong.."
        scene bg atHome155_c4ps with fade
        j "I can hear your heart beating and deep breathing.."
        $ renpy.pause()
        scene bg atHome154c1ps with fade
        j "[bro]... Can I ask you something..?"
        b "Sure, you can ask me anything you want, Julie.."
        scene bg atHome154_c1_ps with dissolve
        j "Do you think I'm pretty..?"
        scene bg atHome155c1ps with dissolve
        j "I mean do you find me really attractive girl..?"
        b "Of course, You are gorgeous and stunning.. I bet that any guy would give everything for a chance to be with you. Looks like bunch of girls wouldn't mind either as far as I can tell.."
        j "Thanks.. But what about you..?"
        b "..."
        scene bg atHome155c3ps with fade
        j "Would you date a girl like me ..?"
        menu:
            "Yes":
                $ ep7JulieMutual += 1
                b "Sure I would date you, Julie.. I would even have married an amazing girl like you without thinking any single minute..."
            "No":
                b "I don't think so.. You are my [sis] and you are not exactly my type of girl..."
        play sound ("music/sounds/thunder1.mp3")
        scene bg atHome155__c3ps with dissolve
        j "Oh..."
        j "You know.. I just remembered the time when we were kids, sometimes we had to stay alone at the house because [mom] was working late hours.. You knew the way how to calm me down during the storm.."
        j "We were hiding inside the 'shelter' you had built using pillows and blanket, it worked every time... You always took a flashlight with you so you could read me fairy tales until I fall asleep.."
        scene bg atHome155c3ps with dissolve
        b "Yeah.. I almost forgot, those were a good times.. It's just so many things happened since I moved to this city: new work, new place, new people.. I started to forget some of my old memories, thank you for reminding me this one.."
        scene bg atHome155c1ps with fade
        j "By the way how is your work going on ? I know that you don't like to talk about it but you left so quick in a hurry today.. I noticed that it doesn't really matter whether it's the middle of the night or not  - probably your work is really urgent and important.."
        j "I just wanted to ask.. Will it always be like this with your work ? "
        scene bg atHome155__c3ps with fade
        j "I mean.. I would want me and you to spend more time together.. We didn't have any chance to see each other until I moved here, but even now, when we are living together we barely see each other.."
        scene black with Dissolve (1.5)
        scene bg atHome154c1ps with Dissolve (1.5)
        j "When the study starts I will move living at the university's dormitory and we won't have that much time to spend together.."
        j "Your work literally taking you away from us.."
        scene bg atHome154_c1_ps with dissolve
        j "Sometimes a have a bad dreams.. In those dreams we, your [family], bother and disturb you from the work.. Me and [mom] are just a burden that pulls you down and doesn't let you live the life you really want.. So you eventually decide to leave us and start acting like a complete stranger.."
        $ renpy.pause()
        b "Those just a nightmares Julie.."
        play sound ("music/sounds/thunder1.mp3")
        scene bg atHome155c1ps with Dissolve(0.75)
        j "You won't leave us like our [father] did, will you ?"
        b "Of course I won't, little one.. You and [mom] is everything that I have in my life. I'm willing to do everything possible and impossible only to make sure that you two are happy and safe.."
        scene bg atHome154_c1_ps with Dissolve(0.75)
        j "But what about your work.. What if you happen to chose between us and the work again.. What will be your choice..?"
        b "I won't make this mistake second time, Julie.. That's why today I decided to quit that job, I don't work there anymore.. From now on everything is going to be good. We will live a happy life like any other [family] does.. I will find a normal job with a common schedule 9 to 5 and I promise that we will catch up the lost time.."
        scene bg atHome157c1ps with Dissolve(0.75)
        j "Really ? That is so awesome [bro] ! I can't wait for that day to come ! When it all will start ?"
        b "Starting today.. I mean we will have to get some sleep at first, but straight from the morning.."
        j "Sweet ! I love you [bro].. You are the best [brother] and.. the best man in my whole life.."
        b "I love you too Julie, but don't praise me too much or I'm afraid I'll become too arrogant.."
        scene bg atHome155c3ps with fade
        j "You won't [bro].. You are too kind, and there is no place for such bad things in your heart.."
        b "You are the cutest girl I ever met.."
        $ renpy.pause(1.0)
        scene bg atHome155__c3ps with dissolve
        j "Uhm.. I just realised that I should call [mom] again and tell her the good news.. She would love to hear that you left the job and will be more available from now on.."
        scene bg atHome155c3ps with dissolve
        b "Did you talk to [mom] recently ? I was just about to call her myself. How is she ?"
        scene bg atHome155__c3ps with dissolve
        j "She is fine, we talked few hours ago. I told her about today, the bank and how heroically you saved everyone. By the way she is planning to visit us soon"
        $ ep7bank = 0
        $ ep7visit = 0
        menu ep7talking:
            "Bank" if ep7bank == 0:
                play sound ("music/sounds/thunder1.mp3")
                $ ep7bank += 1
                b "Julie, you shouldn't have told her about the accident at the bank.. There is no need for her to know and worry about that.."
                scene bg atHome155c3ps with dissolve
                j "I know, that is why I described her the situation in general, without any detals. But anyway, by the time I called her, she's already seen the TV report from the daily news"
                b "Well, I guess in that case hearing the 'truth' from you is way better"
                jump ep7talking
            "Visit" if ep7visit == 0 :
                play sound ("music/sounds/thunder1.mp3")
                $ ep7visit += 1
                b "Did [mom] really tell you about her plans to visit us ? "
                scene bg atHome155c3ps with dissolve
                j "Sure, she is missing you and finally wants to see you already after all these years. Just imagine how lonely she is there since I left.."
                b "I guess.. I miss her as well.. I just realised how much I missed you two.."
                jump ep7talking
        $ renpy.pause(1.0)
        j "[bro].. I'm sorry for being too nosy but I was wondering what is going on between you and Vicky.."
        b "Why ?"
        scene bg atHome155__c3ps with dissolve
        j "Well, at first I thought that you two are dating.. I like her and wouldn't mind to date her myself to be honest, huh.. But today at the bank before those scums showed up, she told me that there are some problems between you two.."
        j "Furthermore, I didn't figure out what that hot and mature blond Nicole has to do with you anyway.."
        scene bg atHome155c3ps with dissolve
        j "Did you broke up with Vicky because of Nicole..?"
        b "It's complicated Julie.. I don't know how to explain you this.. It doesn't really matter whether I want it or not but me and Vicky can't be together anymore.. Sometimes there are certain things in your life that you can't change, so you just have to accept the reality and move on.."
        b "Now we two have kind of a business relations, you could say that we are the partners in some sense.."
        scene bg atHome155__c3ps with dissolve
        j "She is an escort girl, isn't she ?"
        b "Huh, you are insightful Julie, you know that..? Did you know everything from the very first day ?"
        scene bg atHome155c3ps with dissolve
        j "Well, I have to admit that your story was persuasive, I almost belived it.."
        b "Almost ?"
        scene bg atHome155__c3ps with dissolve
        j "I mean of course it was too obvious that she is not a regular girlfriend, her appearance and outfit spoke for herself.. But.."
        j "The thing is, I noticed the way she looks at you, something in her eyes was indicating that she really feels something towards you, I saw that you were not indifferent to her.."
        j "She tried to hide it as much as she could but I noticed it anyway.. Her emotions were sincere, I doubt that she is acting like this with any other client.."
        j "Too bad you two broke up.. You looked so good together, such a good couple.."
        scene bg atHome155c3ps with dissolve
        b "Well, technically me and Vicky never were a 'couple' so I don't think that saying 'we broke up' is appropriate here.."
        j "Do you still have feelings towards her ..?"
        $ ep7VickyMatters = 0
        menu:
            "Yes":
                $ ep7VickyMatters += 1
                b "I feel quite awkward by telling you this.. You see, the thing is that Vicky was my first woman and I can't describe by words how incredible I feel about it.. I sense some special bonding with her, me and Vicky are kind of a soul mates, like she completes me.."
                b "Maybe this is the true love, I don't know.. I've never experienced and felt something like this before.. I don't know how strong or what kind of feeligs you're talking about she had towards me, but the one thing I know for sure.. I was always happy being with her.."
            "No":
                b "Actually, there is not much to tell, she is just a pretty girl who I paid for the sex, that is all. Of course she is smart, beautiful and gorgeous - I would lie if I tell that I don't like her - why would I pay her otherwise ?!"
                b "But at the same time I can't tell that she is special or I felt something incredible towards her.. It was pleasant for me to 'cover physiological needs' with her and I doubt that the look you've seen in her eyes is any different from the way she is looking at any other man who pays her for sex.."
        scene bg atHome155__c3ps with dissolve
        j "Oh, I see.."
        b "Anyway, none of this matters anymore - she has her own path and I have mine, I guess we won't ever see each other again.."
        j "It's a pitty, I really liked her.. Is there nothing you can do to change the situation ?"
        b "It doesn't matter whether it's your or someone's else - 'the heart wants what it wants' Julie.."
        scene bg atHome155c3ps with dissolve
        j "Well, I hope you will eventually find the woman of your life and will know what the true love is.. I want you to finally be happy.."
        $ renpy.music.stop(channel=1, fadeout=5.0)
        b "The time will show, little one.. Hey.. Looks like the storm passed by.."
        scene bg atHome155_c4ps with fade
        menu:
            "Hug her gently":
                $ ep7JulieMutual += 1
                scene bg atHome156c4ps with Dissolve(0.75)
                $ renpy.pause(1.0)
                b "Let's go to sleep Julie, I would love to talk with you more but unfortunately I'm completely exhausted.."
            "Don't hug her":
                b "Let's go to sleep Julie, I would love to talk with you more but unfortunately I'm completely exhausted.."
        j "Oh, I'm sorry.. I almost forgot how rough day you had today.. Silly me.."
        scene bg atHome157c1_ps with fade
        b "That is okay, baby.. Sweet dreams.."
        j "Good night, [bro]... I love you..."
        b "Love you too.. Julie.. {i}\nZ-z-z.."
        $ renpy.pause()
        jump ep7badGuys
        return

        define roc = Character("Rocco", color="#201345")
        define nac = Character("Nacho", color="#ff6e00")

    label ep7badGuys:
        $ renpy.music.stop(channel=3, fadeout=3)
        scene black with Dissolve (3.0)
        $ renpy.notify ("Bu gece daha sonra...")
        $ renpy.pause()
        $ renpy.music.play("music/nightmareTheme.mp3", channel=1, loop=True, fadein = 3)
        scene bg Trap12c15ps with Dissolve (3.0)
        $ renpy.pause()
        rocco "So he was alone and yet you missed him..."
        "{b}Carlos{/b}\nCome on, Rocco.. This was the guy from the bank, he alone managed to kick asses of your guys at the bank. How many of them was there ?! Three !? I bet they were well armed and I didn't have at least shitty gun.."
        "{b}Carlos{/b}\nIf I had one - that punk would already be at the bottom of the river"
        scene bg Trap12c9ps with fade
        roc "You didn't have an objective to kill him, your task was to guide him from the front door to the door behind you..."
        "{b}Carlos{/b}\nYeah I know but.."
        scene bg Trap12_c17ps with fade
        nacho "Looks like it was too difficult for you, wasn't it Carlos ? You had an unique opportunity to catch that son of a bitch, but instead you just fucked everything up"
        "{b}Carlos{/b}\nI'm sorry Nacho.. I'll fix this I promise, I just want to prove you my loyalty that's all.. I don't know why it didn't work, I did everything right..."
        scene bg Trap12c9ps with fade
        roc "It's obvious that you exposed yourself by your speech and behavior, he felt your nervousness and heard the trembling in your voice. As soon as he realised that it's a trap you've been neutralized, that's why it didn't work"
        scene bg Trap12_c9ps with dissolve
        "{b}Carlos{/b}\nIt wasn't like that, somehow he knew that it's a trap - he just started to beat me without any reason"
        if ep3NachoBeaten == 1:
            nac "Can't argue with that, the motherfucker can fight only surreptitiously"
        else:
            nac "Strange, usually the punk only threatens to call the police, fighting isn't his style"
        nac "Anyway pal, you literally hold that bastards's balls in your hand yet you couldn't squeeze them and complete that simple job"
        scene bg Trap12c16ps with fade
        "{b}Carlos{/b}\nPlease give me one more chance and I will prove you that I can do this job, I want to show you my loyalty"
        roc "What you and him were talking about right before the fight ?"
        "{b}Carlos{/b}\nNothing special, I asked him if he arrived alone and then we had a shitty chit-chat about the job and the car"
        scene bg Trap12_c16ps with dissolve
        roc "What car ?"
        "{b}Carlos{/b}\nJose's car, he came on it here, but I.."
        nac "Great.. He was stupid enough to leave it outside, right in front of the entrance ?! You guys are just fucking 'Dream Team'"
        "{b}Carlos{/b}\nIt's none of my business where Jose left his car, I have nothing to do with it anyway, it's not my car I just.."
        scene bg Trap12_c17ps with fade
        nac "You two are really dumb fuckheads, you know that ?! You told that the car isn't yours and the punk kicked your ass, right ?"
        "{b}Carlos{/b}\nProbably.."
        nac "I thought you are an interrogator, not a stupid bitch.."
        scene bg Trap13c18ps with fade
        "{b}Carlos{/b}\nListen.. Ok, I know, I panicked for a second or two when I realised that the car can expose us but I really tried to fix the situation.. I just.."
        scene bg Trap13c19ps with fade
        roc "What you can tell me about the man who gives you orders ?"
        "{b}Carlos{/b}\nTh-the coordinator .. ?! I.. I don't know him, I've never met him before - since I started working here, I only got phone calls from him."
        "{b}Carlos{/b}\nH-he just tells what to do and where I can pick up the reward after I finish the job, they always hide the money at different places around the city.."
        roc "Do you ever tried to contact with him first ?"
        "{b}Carlos{/b}\nYes.. Ahm, as soon as I woke up I tried to call coordinator and tell that [bro] is a traitor, was hoping that I could put the blame on that motherfucker, but the number was out of service.."
        nac "Fucking genius ! I think that next time you should call directly [bro] and tell him who he really is."
        scene bg Trap13_c19ps with dissolve
        roc "Is there anything else you can tell me about the coordinator ?"
        "{b}Carlos{/b}\nMe ?! No.. I, I mean.. I just told you everything I know.. What else do you want from me ?"
        nac "Too bad, Carlos.. Looks like you did everything you could in order to fix the situation, but it didn't really help you."
        "{b}Carlos{/b}\nW-what are-e you talking about, Nacho..?"
        nac "Jose turned up to be a bit smarter than you, that is why he didn't try to help you and escaped as quick as possible. He realised that you both failed and therefore you two are no use for us any longer"
        "{b}Carlos{/b}\nNo, that's not true ! I'll fix this Nacho, I promise ! Just give me another chance and some weapon - I swear to god I'll find and will kill that son of a bitch. I beg you guys, let me prove you my loyalty !"
        nac "..."
        roc "..."
        "{b}Carlos{/b}\nRocco, please tell him !"
        roc "You know the common problem of all betrayers ? They all know word 'loayalty'"
        scene bg Trap13c19ps with dissolve
        roc "But none of them knows what this word means {nw}{w=1.5}"
        play sound ("music/sounds/kneeKick.mp3")
        scene bg Trap14__c20ps with Fade(0.05, 0.05, 0.05, color="#8a0303")
        scene bg Trap14_c20ps with Dissolve(0.025)
        play sound ("music/sounds/kneeKick.mp3")
        scene bg Trap14__c20ps with Fade(0.05, 0.05, 0.05, color="#8a0303")
        scene bg Trap14_c20ps with Dissolve(0.025)
        play sound ("music/sounds/kneeKick.mp3")
        scene bg Trap14__c20ps with Fade(0.05, 0.05, 0.05, color="#8a0303")
        scene bg Trap14_c20ps with Dissolve(0.25)
        play sound ("music/sounds/kneeKick.mp3")
        scene bg Trap14__c20ps with Fade(0.05, 0.05, 0.05, color="#8a0303")
        scene bg Trap14c19ps with Fade(0.05, 1, 2, color="#8a0303")
        roc "...{nw}{w=1.25}"
        "{b}Carlos{/b}\n{i}Dead.........."
        scene bg Trap12_c17ps with fade
        play sound ("music/sounds/bodyFall.mp3")
        nac "Holy shit.. Rocco, sometimes you're scaring me.. You've become a hellish beast after those enhancers, do you know that ?! I heard his neck break even after first hit"
        scene bg Trap15c21ps with fade
        roc "Traitors.. It's just the matter of time when they will decide to change the side and betray again.."
        nac "Actually I was hoping you will leave him to me. Unlike you I still need to practice. But I guess this time I will have to find someone else for myself"
        scene bg Trap15_c21ps with dissolve
        nac "I wonder what Jose is going to do now.. Probably the best option for him is to surrender to the police, what do you think about him ?"
        roc "Nothing. We have more important things to do rather than worrying about Jose"
        nac "What are you talking about ? I think we can call it a win and we deserved some rest. I mean the rats played their roles: they snitched and gave us all the information about the hideouts, banks and weapon bases."
        nac "Their whole infrastructure is in our hands and thanks to you, their so-called 'resistance' is completely fucked out. We've never won a city so quick before, those guys were fucking amateurs. I think there only few of their people left - there is nothing to worry about."
        roc "These 'few people' may be the most important and dangerous. Coordinator and that guy combined could cause us a lot of problems"
        nac "I didn' get it: you killed like a fucking hundred of those punks and you still bother about shitty coordinator and that bastard from the bank ?! Antonio told us that they don't have any enhancers but even if they had them - the body has to be compatible - so why bother ?"
        roc "Antonio was saying exactly what we wanted to hear from him, his words may be lie. He was hoping that he can finally reunite with his family again. "
        nac "Indeed, motherfucker could be lying.. Well, at least I kept my word and made sure that Antonio and his kids eventually reunite as I promised.. I wasn't saying that they reunite alive though, ha-ha.. As for the guy.."
        nac "Don't worry, pal. I promise that the next time I'll meet this piece of shit I will cut his fucking head off"
        roc "We should find him as soon as possible. The boss still waits for our report on this case"
        nac "My 'pawns' already started searching him as you suggested, or if he is dumb enough to show up at the bank again - we will catch him. Anyway the motherfucker has less than a week to live.."
        roc "Tell your guys to deliver him alive, whenever possible. Before the killing I want to talk to him and get the information regarding coordinator and the rest of the money"
        nac "As you say, pal.."
        $ renpy.music.stop(channel=1, fadeout=3)
        jump ep7HomeDream
        return

    label ep7HomeDream:
        scene black with Dissolve (2.5)
        $ renpy.notify ("Bu arada evde...")
        $ renpy.pause()
        $ renpy.music.play("music/afterDarkTheme2.mp3", channel=3, loop=True, fadein = 3)
        scene bg atHome158c5ps with Dissolve (2.5)
        $ renpy.pause()
        j "{i}Z-z-z..."
        $ renpy.pause()
        b "{i}Z-z-z..."
        scene black with Dissolve (1.5)
        scene bg atHome158c6ps with Dissolve (1.5)
        j "{i}Z-z-z... Z-z-z..."
        $ renpy.pause()
        b "{i}Z-z-z... Z-z-z.."
        scene black with Dissolve (1.5)
        scene bg atHome158c4ps with Dissolve (1.5)
        $ renpy.pause()
        j "{i}Z-z-z... Z-z-z..."
        $ renpy.pause()
        b "{i}Z-z-z...Z-z-z.."
        scene black with Dissolve (1.5)
        scene bg atHome158c5ps with Dissolve (1.5)
        j "{i}Z-z-z... Z-z-z..."
        $ renpy.pause()
        scene bg atHome159c5ps with Dissolve (0.75)
        $ renpy.pause(0.5)
        b "Uhm... Mhmm...{i}Z-z-z..."
        j "{i}Z-z-z... Z-z"
        b "Oh... Uhmm {i}Z-z..."
        j "Huh..? {i}Z-z.."
        b "Yes..like that.. {i}Z-z-z.."
        j "[bro]..? {i}Z-z.."
        $ renpy.pause()
        $ renpy.music.set_volume(0.25, delay=0, channel=1)
        $ renpy.music.set_volume(0.65, delay=0, channel=3)
        scene black with Dissolve (1.5)
        scene bg atHome160c4ps with Dissolve (1.5)
        menu:
            "View Dream":
                $ renpy.music.stop(channel=3, fadeout = 5)
                scene black with Dissolve (3.0)
                $ renpy.pause()
                $ renpy.music.play("music/sexyTheme.mp3", channel=1, loop=True, fadein = 5)
                scene bg dream17c1ps with Dissolve (3.0)
                $ renpy.pause()
                v "That's what I call 'riding the dick' girls, just look at his face - I bet he never came that hard before. So, who wants to be the next ?"
                s "I wouldn't mind to ride this stud.. I hope I will be able to take this huge dick right inside my tight little pussy.."
                j "Come on Scarlett, don't be so selfish - let him take a breath for few minutes. Vicky has taken all his hot and sticky cum"
                v "Julie is right, [bro] needs a little break to restore the deposits of his sweet and delicious semen"
                s "I can't wait for you to cum in my mouth, [bro]. I want to know how good it tastes"
                j "I bet it tastes amazing Scarlett. You just need to be patient little girl and [bro] will reward you."
                v "Yes Scarlett, Julie is right - just be a good girl"
                s "Being patient good girl is not my style - I more like to think of me as a naughty little whore who always craves for a dick"
                j "Your [father] just didn't give you proper spanking, otherwise you would know how to behave. But it's okay, [bro] will fix that."
                $ renpy.pause()
                scene black with Dissolve (2.0)
                scene bg dream17_c2ps with Dissolve (2.0)
                v "Okay girls, I had my fun with him - now it's your turn. I'm sure that you know what to do with that huge throbbing cock.."
                v "By the way Scarlett, considering that you are more experienced with men - don't forget to guide and help Julie when she needs it.."
                s "I know, she never touched a dick before but that is a plus in our case - deep inside every man wants to be girl's first.."
                j "I'm fast learner.. Thanks to Vicky now I know how to give a blowjob.. Theoretically of course.."
                v "Remember Julie, only the woman who mastered the 'Royal Blowjob' can be called a blowjob queen"
                s "And a filthy whore.."
                v "Exactly.. Anyway, always share his cock between you two and don't be greedy.. See you later, girls.."
                j "Bye Vicky.."
                s "Bye-bye.."
                v "Can't wait to see you again, [bro].."
                scene black with Dissolve (2.0)
                scene bg dream18c1ps with Dissolve (2.0)
                $ renpy.pause(0.75)
                s "So.. Tell me Julie, what whould you like to start doing with your [brother]..?"
                scene bg dream18c1_ps with Dissolve (1.0)
                $ renpy.pause(0.75)
                j "I don't know.. I have so many dirty sexual fantasies in my head right now.. I want to try all that is possible and I want it at once. I don't have any experience with men, but I desperately want to become his personal little slut.. Scarlett, what would you suggest to start with ?"
                scene bg dream18c1ps with Dissolve (1.0)
                $ renpy.pause(0.35)
                s "That's my girl.."
                scene bg dream19c1_ps with Dissolve (0.5)
                s "Well, I would recommend you to start with anal sex"
                scene bg dream19c1ps with Dissolve (0.75)
                $ renpy.pause(0.25)
                j "Just like that..?"
                scene bg dream19c1ps_ with Dissolve (0.75)
                s "Yes, just like that.. You see, a lot of people decide to postpone this most pleasurable and sensual kind of sex for some reason.."
                scene dream18c1ps with Dissolve(0.75)
                j "Oh.. I can't help it - I want to touch myself down there.."
                scene bg dream18c1_ps with Dissolve (0.75)
                s "Afterwards they always regret they didn't start doing it earlier.."
                scene bg dream19c1ps_ with Dissolve (0.75)
                j "Is it that pleasant..?"
                scene bg dream19c1ps with Dissolve (0.75)
                s "It's amazing Julie.. Me personally love it the most.. The feeling when you're being fucked from behind, right inside your tight and defenseless little asshole, it's incredible.."
                scene dream18c1ps with Dissolve(0.75)
                j "I don't even know.. I mean look at the size of this dick - we barelly can wrap it with both our hands, I don't know how I can take it inside my little ass.."
                scene bg dream18c1_ps with Dissolve (0.75)
                s "Yes it's big, but it will fit - trust me.. Everything just needs to be done step by step - no need to rush.."
                scene dream18c1ps with Dissolve(0.75)
                s "I like to start it with very slow and smooth insertion of the dick. At first I need some time to adopt when a huge throbbing cock fully enters inside my tiny little butthole.."
                scene bg dream18c1_ps with Dissolve (0.75)
                j "Sounds good.."
                s "I adore the feeling from understanding that pulsating big cock filled my ass up completely.."
                scene bg dream19c1ps_ with Dissolve (0.75)
                j "Oh my god Scarlett.. I'm so wet already.."
                s "Then I love deep and strong thrusts with a low amplitude of the frictions.. I like to spread my legs wide open thus letting the cock to be as deep as possible inside of me.."
                scene bg dream18c1_ps with Dissolve (0.75)
                j "Umm, just like I imagined it.."
                s "After few such thrusts I usually get incredibly horny so I start to slowly move my ass towards the dick - I love to smoothly and fully take in and take out the cock by myself.."
                scene bg dream19c1ps with Dissolve (0.75)
                j "Are you saying that your ass starts to glide along the dick on a full length..?"
                s "Aha.. My tight little butthole becomes loose enough for the glans to easily come in and out.. By that time I usually already beg about being fucked like a true slut as hardly and quickly as possible.."
                scene bg dream19c1ps_ with Dissolve (0.75)
                s "You can't even imagine how good is the feeling when a man deeply cums right inside your no longer sealed and already fucked ass."
                scene bg dream18c1_ps with Dissolve (0.75)
                j "I want to know how does it feel to climax when the dick is deeply fucking me right up in the ass.."
                scene dream18c1ps with Dissolve(0.75)
                s "It's amazing Julie.. You will know how good it feels, especially with [bro]'s size.."
                scene bg dream18c1_ps with Dissolve (0.75)
                j "It's okay that he is that big..?"
                scene dream18c1ps with Dissolve(0.75)
                s "Sure, that's the point. If the cock is huge I came that hard that the tears start come out of my eyes.."
                scene bg dream19c1ps_ with Dissolve (0.75)
                j "Maybe it's because of pain..?"
                scene bg dream19c1ps with Dissolve (0.75)
                s "Well, at the beginning it will hurt a little bit, but this pain eventually will wake up your primal instincts and you will get horny like never before.."
                j "Really ? I don't quite understand how the pain can be pleasant.."
                scene dream18c1ps with Dissolve(0.75)
                s "Keep in mind that anal sex is also about psychological delight.. Realising that you are being roughly fucked like a dirty little whore by brutal and strong male right inside your ass brings that many pleasure - that the pain fades away, trust me.."
                j "I guess.. I just never thought about it.."
                scene bg dream19c1ps_ with Dissolve (0.75)
                j "You are right, after all it's our nature - women meant to be submissive and deep inside we crave to obey and surrender to a dominant man.."
                scene bg dream19c1ps with Dissolve (0.75)
                s "Exactly Julie, you are indeed fast learner.. Let's start to practice, shall we ?"
                scene dream18c1ps with Dissolve(0.75)
                menu:
                    "Continue":
                        scene bg dream19c1ps_ with Dissolve (0.75)
                        j "To be honest I'm still a bit scared because of pain.. But for the other hand I got so horny and wet - there is literally a flood between my legs. I think I won't need any extra lube for my little butthole - the pussy juice is more than enough.."
                        scene bg dream19c1ps with Dissolve (0.75)
                        s "Relax, I'm with you and will take care of everything. Besides, [bro] will do his best in order to not hurt you. After all, who else would you let to fuck your tiny virgin ass except [bro] ?"
                        j "No one.. Ever.."
                        scene dream18c1ps with Dissolve(0.75)
                        s "That's a good girl.. Believe me, considering the size of your [brother]'s cock - you will come quick and hard enough that your legs will stop listen to you and the head will become dizzy"
                        s "You'll need some time to take a break and at the meanwhile I hope that [bro] will do the same with me.."
                        scene bg dream19c1ps_ with Dissolve (0.75)
                        j "Scarlett.. I just realised that I want to taste [bro]'s cock while he is fucking your ass.. I got turned on only from the thinking about it"
                        scene bg dream19c1ps with Dissolve (0.75)
                        s "Yeah, I just thought of it myself it's so hot.."
                        scene bg dream19c1ps_ with Dissolve (0.75)
                        s "[bro] please don't forget to take out your cock and let us suck on it while you will be fucking our tiny buttholes, okay..?"
                        scene bg dream18c1_ps with Dissolve (0.75)
                        j "Yeah, and one more thing I just wanted to ask - [bro] please don't leave all of your cum inside our asses - save some of your sweet semen for my mouth I've been wanting to swallow it for a long time.."
                        scene bg dream19c1_ps with Dissolve (0.75)
                        s "Hope you will share some of his hot juice with me Julie.. I promise I won't spill any single drop.."
                        scene bg dream19c1ps with Dissolve (0.75)
                        j "Of course baby, I can't refuse you.."
                        s "Thanks, babe.."
                        scene bg dream18c1ps with Dissolve(0.75)
                        j "So [bro].. Would you like to fuck me in my ass like a dirty little whore..?"
                        scene bg dream18c1_ps with cumFlash
                        scene bg dream18c1ps with cumFlash
                        scene bg dream18c1_ps with cumFlash
                        scene bg dream18_c4ps with cumFlashLong
                        $ renpy.pause()
                        $ renpy.music.stop(channel=1, fadeout = 5)
                        scene black with Dissolve (3.0)
                        $ renpy.pause()
                        $ renpy.music.play("music/afterDarkTheme2.mp3", channel=3, loop=True, fadein = 3)
                        scene bg atHome165c4ps with Dissolve (3.0)
                        $ renpy.pause()
                        b "{i}Huh..?! What the hell..?! Oh my god.. That was one of those dreams about me having sex with Julie.."
                        j "{i}Z-z.."
                        if ep7JulieMutual >= 2:
                            b "{i}Holy fuck I wish I didn't wake up and watch it to the end.."
                        else:
                            b "Why do I have such dreams about my little [sis] ?! It's wrong.."
                        j "{i}Z-z.."
                        b "{i}Thinking about anal sex with my little [sis] made my cock hard as rock.. I've never experienced such strong boner, damn.."
                        j "{i}Z-z.."
                        b "{i}Anyway, I should cover it with something.. I don't know what is going to happen if Julie wakes up and sees me like this.."
                        menu:
                            "Cover the cock":
                                b "{i}Okay.. Carefully.. Please don't wake up, little one.."
                                scene bg atHome165_c4ps with Dissolve (0.75)
                        j "{i}Z-.."
                        j "..."
                        $ renpy.pause()
                        j "{i}Z-z.."
                        b "{i}Wow.. That was close.."
                        b "{i}I guess I'll go back to sleep, I still feel tiredness after yesterday.."
                        b "sleep tight Julie.. have a sweet dreams.."
                        j "you to..{i}z-z.."
                        b "{i}Huh ?! She wasn't sleeping ?! "
                        $ renpy.pause()
                        b "are you sleeping..?"
                        j "..."
                        $ renpy.pause()
                        j "{i}Z-z.."
                        b "{i}Phew.. I think I should call it a day, that's enough for one night.."
                        $ renpy.pause()
                        jump ep7Morning
            "Stay As Is":
                b "Oh yes.. So good.. {i}Z-z-z.."
                j "[bro].. Are you talking to me..? I thought you wanted to sleep.."
                j "Wait a second.. What is this so hot.. It's poking at my elbow.."
                b "Yes, baby.. {i}Z-z-z.."
                scene bg atHome160_c4ps with Dissolve(0.75)
                $ renpy.pause(0.5)
                j "Oh my.. Is this.. Your.."
                b "Oh, yes..{i}Z-z-z"
                scene bg atHome161_c4ps with Dissolve (1.25)
                j "[bro] are you okay !?"
                $ renpy.pause()
                b "Mh...{i}Z-z-z.."
                j "{i}Looks like he is sleeping.. I wonder what he is dreaming about.."
                scene bg atHome161_c4_ps_ with Dissolve (0.75)
                j "{i}Oh my.. So that is how a real cock looks like.. I didn't know it's that thick.."
                b "Oh, Julie.. {i}Z-z-z.."
                scene bg atHome161_c4ps with dissolve
                j "{i}Huh ? Is he.. Is my [brother] dreaming about me..?! "
                b "{i}Z-z-z..."
                j "{i}I can't believe this, [bro] is having sexual dream about me.. That is unusuall.. I mean is this okay to have such dreams ?!"
                scene bg atHome161c4ps with dissolve
                j "{i}For the other hand I thought about having sex with my [brother] and talked about it with Scarlett, so how is this any different ?! I mean of course I was aroused after the orgasm and sex with Scarlett, but.. wait.. That strange feeling in my belly.."
                j "{i}Oh my good, it is so warm and.. Hard.. I've never touched a dick in my life.. Do they all like this ?"
                scene bg atHome161_c4_ps_ with Dissolve (0.75)
                j "{i}Interesting.. I wonder how big it is.. I'll just take a little glimpse, nothing bad will happen if I just take a better look at it.."
                j "{i}Okay Julie.. Slowly pull down the underpants.."
                scene bg atHome162c4ps with dissolve
                b "Mhh.. Yes.. {i}Z-z-z.."
                j "{i}Oh my god.. It's enormous I didn't expect [bro]'s dick will be that huge.. It's like my forearm, how can this one fit inside a pussy ?"
                b "{i}Z-z-z.."
                scene bg atHome161_c4_ps with Dissolve (0.75)
                $ renpy.pause()
                j "{i}Wait.. What am I doing.. What if my [brother] wakes up and sees me holding his dick.. He'll probably decide that I'm some kind of pervert and will get mad at me.."
                j "{i}But what if.."
                scene bg atHome163_c4ps with Dissolve (0.75)
                j "{i}What if Scarlett is right.. I think I'll just give it a try and will see where it goes.. After all who is a better candidate among all the men - he loves me and cares about me - that is more than enough.."
                b "Ahm..Mhhh.. {i}Z-z-z.."
                j "{i}Actually that sense of uncertainty kind a excites me.. Didn't expect from myself that I can get really horny from touching my [brother]'s huge cock alone.."
                scene bg atHome163c4ps with Dissolve (0.75)
                j "{i}To be honest this is the kind of cock I've been recently dreaming about during the masturbation.. The shape and size even better than I imagined.."
                j "{i}Oh my.. I'm starting to get really wet down there.."
                scene bg atHome163_c4ps with Dissolve (0.75)
                scene bg atHome163c4ps with Dissolve (0.75)
                scene bg atHome163_c4ps with Dissolve (0.75)
                j "{i}Why do I have that feeling.. Why I want to take it in my mouth so bad.."
                scene bg atHome164_c4ps with Dissolve (0.75)
                j "{i}It's probably the same feeling when a man sees a naked woman and instantly wants to fuck her right away.."
                j "{i}I feel myself such a bad girl right now.."
                scene bg atHome164c4ps with Dissolve (0.75)
                j "{i}Stroking my [brother]'s huge cock while he's asleep.. It's really perverted and a bit creepy, but for the other hand how is that any different from a regular massage..?! I'm just helping him release the tension that is it.."
                scene bg atHome164_c4ps with Dissolve (0.75)
                b "Oh yes..{i} Z-z-z.."
                scene bg atHome163c4ps with Dissolve (0.75)
                j "{i}There are so many thoughts running through my mind.. Maybe I should stop doing this before it's too late.. I can't think about anything else since Scarlett sowed in my head the idea of having sex with [bro].."
                j "{i}But if it all is bad.."
                scene bg atHome164c4ps with Dissolve(0.75)
                j "{i}Why does it feel so good..?!"
                j "{i}I think I just need to decide how I'm going to seduce my own [brother].. Scarlett told that she went straight to the point with her [father], but I'm not that confident.."
                b "Scarlett.. Mhh.. {i}Z-z-z..."
                scene bg atHome164_c4ps with Dissolve(0.75)
                j "{i}Huh, looks like [bro] is having a good time with me and my girlfriend.."
                b "Oh yes.. {i}Z-z-z.."
                scene bg atHome162_c4ps with Dissolve (0.75)
                j "{i}Wow.. It starts pulsating in my hand.. Probably [bro] is about to cum.. I wonder will he wake up or I should stop to avoid awkward situation.."
                b "Mhmh..Oh yes..{i}Z-z-z.."
                scene bg atHome164_c4ps with Dissolve (0.75)
                j "{i}So be it.. I think I should tell Scarlett about my decision - I want to seduve my old [brother]. I need to take some advices about what to do.."
                scene bg atHome164c4ps with Dissolve (0.75)
                scene bg atHome164_c4ps with Dissolve (0.75)
                scene bg atHome164c4ps with Dissolve (0.75)
                scene bg atHome164_c4ps with Dissolve (0.75)
                b "{i}Oh..?? {i}Z-z..{/i} Julie... What are you..{i}Z.."
                scene bg atHome161_c4_ps with dissolve
                j "{i}Oh gosh, looks like [bro] is about to wake up.. I got to excited again.. What I was thinking of ?! I'll pretend that I'm sleeping.."
                scene bg atHome165c4ps with dissolve
                b "Huh..?  What the.. {i}Did Julie really just hold my cock or it all was a dream ?!"
                b "{i}Shit I have to hide that boner.."
                scene bg atHome165_c4ps with Dissolve(0.75)
                b "{i}I could swear that I felt the warmth from the hand on my cock right before I woke up.. Is Julie really just.."
                j "Sweet dreams [bro]..{i}Z-z.."
                scene bg atHome165_c4ps with hpunch
                b "{i}She really did that.."
                b "{i}Well.. I guess I need to talk about this with her at the morning.."
                b "Good night little one.."
        $ renpy.pause()
        jump ep7Morning
        return

    label ep7Morning:
        $ renpy.music.stop(channel=1, fadeout = 5)
        $ renpy.music.stop(channel=3, fadeout = 5)
        scene black with Dissolve (2.5)
        $ renpy.notify ("Sonraki sabah...")
        $ renpy.pause()
        scene bg atHome166c5ps with Dissolve (2.5)
        $ renpy.pause()
        b "{i}Z-z-z..."
        play sound ("music/sounds/doorBell.mp3")
        "{b}{i}DOOR BELL"
        b "{i}Z-z.."
        play sound ("music/sounds/doorBell.mp3")
        "{b}{i}DOOR BELL"
        b "Huh.. ?!"
        scene bg atHome166_c5ps with dissolve
        j "{b}[bro], please open the door - I'm at the bathroom"
        b "{i}I wonder who can it be..?"
        play sound ("music/sounds/doorBell.mp3")
        "{b}{i}DOOR BELL"
        b "{i}Shit.. Persistent one, I hope this is not the police.."
        b "I'm comming.."
        menu:
            "Get up":
                scene black with dissolve
                play sound ("music/sounds/openDoor.mp3")
        $ renpy.pause(1.25)
        play sound ("music/sounds/doorClose.mp3")
        $ renpy.pause()
        $ renpy.music.set_volume(0.15, delay=0, channel=1)
        $ renpy.music.play("music/sounds/shower.mp3", channel=1, loop=True, fadein = 3)
        scene bg atHome167c2ps with Dissolve(1.5)
        b "{i}Maybe it's Nicole.. I miss her already, can't forget the amazing blowjob she gave me the other night.."
        play sound ("music/sounds/doorBell.mp3")
        "{b}{i}DOOR BELL"
        j "{b}[bro]..?"
        b "On my way !"
        menu:
            "Open the door":
                scene black with Dissolve(1.5)
                play sound ("music/sounds/openDoor.mp3")
                $ renpy.pause(0.5)
                $ renpy.music.set_volume(1.0, delay=0, channel=3)
                $ renpy.music.play("music/scarlettTheme.mp3", channel=3, loop=True, fadein = 3)
                scene bg atHome168c4ps with Dissolve (3.0)
        $ renpy.pause()
        b "Oh.. Scarlett, hi.. What a surprise.. Come in, make yourself at home.."
        s "Morning [bro], long time no see.."
        scene bg atHome168_c1ps with fade
        s "Did you miss me..? Because I've been missing you very much.. "
        $ renpy.pause()
        scene bg atHome168_c5ps with fade
        b "Yeah, I missed you to.. So what's up, how are the things going ?"
        s "Fine and going to become even better really soon - thanks for asking.. You are doing well too as far as I can tell. Didn't know you have such an amazing body.."
        b "Uhm thanks, I do the workout from time to time.. Can I get you something..?"
        scene bg atHome169_c5_ps with dissolve
        b "Julie is taking the shower.. So I thought.."
        scene bg atHome169_c5ps with dissolve
        b "Maybe at the meanwhile you would like something to drink.."
        scene bg atHome168_c5ps with dissolve
        s "Oh [bro], it's so kind of you - but I already had a breakfast.."
        b "Oh.. I see.. So come over and take a seat then, my [sis] will be in a few minutes.."
        $ renpy.pause()
        s "You know.. Actually there is something I want since yesterday.."
        scene bg atHome169c5__ps with dissolve
        s "That I would love to drink.."
        s "Or eat.."
        scene bg atHome169c5_ps with dissolve
        s "I guess it depends on you handsome.."
        scene bg atHome168__c4ps with fade
        s "That's good to know that you already prepared it for me.. I just don't know if I will be able to swallow it all entirelly.."
        $ renpy.pause()
        b "Scarlett, I don't think this is a good idea.. Now is not the best time considering that Julie is taking a shower right behind the door.."
        $ renpy.pause(0.25)
        scene bg atHome170c6ps with hpunch
        s "Gotcha !"
        b "Scarlett.. What are you doing ?! Julie can come out any second.."
        s "It turns me on even more, don't you feel the same about it ? The excitement of being caught turns me on like a crazy one and my pussy starts dripping wet.. Besides.."
        scene bg atHome170c7ps with fade
        s "I already told you - you won't go anywhere at the morning until I deal with your 'morning wood', remember..?"
        b "She is your girlfriend - if she sees us she will definitely get upset. Do you really want this ? It's not cool for you to cheat on her with me.."
        s "Oh [bro].. Looks like you know nothing about Julie, don't you ?"
        b "What do you mean..?"
        s "She didn't tell you, right ? Well, looks like I have plenty of good news for you handsome.. Let me show you what exactly I mean.."
        scene black with Dissolve (1.5)
        scene bg atHome171c2ps with Dissolve (1.5)
        b "Holy shit, babe.. If only you would knew how sexy you look standing on your knees with my cock in your hand.."
        s "I bet I would look sexier if it was in my mouth.."
        b "Oh yes.. Shit.."
        $ renpy.pause()
        scene black with Dissolve (1.5)
        scene bg atHome171c5ps_ with Dissolve (1.5)
        s "Oh my gosh.. What a perfect dick you have [bro].. It looks even bigger than yesterday.."
        scene bg atHome171_c5_ps11 with Dissolve (0.5)
        b "What about those good news you were talking a moment ago ?"
        scene bg atHome171c5ps12 with Dissolve (0.75)
        s "You know.. I thought that I shouldn't spoil the surprise.."
        scene bg atHome171_c5_ps11 with Dissolve (0.75)
        s "After all, why do I have to take all the fun with me..?! Julie will tell you everything herself.. But here is a little hint for now.."
        scene bg atHome171c5ps12 with Dissolve (0.75)
        scene bg atHome171_c5_ps11 with Dissolve (0.75)
        scene bg atHome171c5ps12 with Dissolve (0.75)
        scene bg atHome171_c5_ps11 with Dissolve (0.75)
        s "I would suggest you to imagine how me and Julie will be greedily sucking your big hard cock.."
        b "Oh fuck.."
        scene bg atHome171__c5ps21 with dissolve
        s "How do you like that idea, huh..?"
        b "I.. I like the idea of you sucking on my dick.. I can't wait until you put it in your mouth.."
        s "I knew you would like it.."
        scene bg atHome171_c5ps with dissolve
        $ renpy.pause()
        s "Gosh.. I envy Julie so much.. She can be sucking and riding on your cock whenever she wants, any time and everywhere.."
        scene bg atHome171c5_ps22 with dissolve
        b "Julie is not like that.."
        s "At least I would be doing so if I were your little [sis], [bro].."
        b "Fuck, babe.. Didn't know that incest fantasies turn you on.. You are so bad you know that ?"
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        play sound ("music/sounds/femaleGiggle.mp3")
        s "It's not only the fantasies.. Did I ever tell you how I loved to fuck with my [father]?"
        b "What..?"
        $ renpy.music.stop(channel=1, fadeout = 5)
        scene bg atHome171_c5ps with dissolve
        s "You see, I've always been a bad girl.. Probably it's because I love being spanked. When I was little I tried to be as naughty as possible to get myself some spanks over and over again.."
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        s "I literally was counting the hours until my [father] decides that I deserved some new spanks again.."
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        b "Ah shit, such a bad girl - did he really fuck his naughty little girl ?"
        scene bg atHome171_c5ps with dissolve
        s "Of course he did, you see - I've always been sexually attracted to my [father], I wanted him to be my first man the man who would take my virginity and make me real woman.. I always get what I want that is why I eventullay lost my virginity to him"
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        b "Yeah ? I bet you liked it, tell me how he fucked you"
        scene bg atHome171_c5ps with dissolve
        s "Gladly.. At first I sucked his thick pulsating dick like a good girl. I've never sucked a dick before, but he came very quick and hard - looks like I am natural and have a talent at giving blowjobs.."
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        s "Of course his dick was smaller than yours.."
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        b "Good girl, continue.."
        scene bg atHome171_c5ps with Dissolve (0.75)
        s "After I finished swallowing big load of semen that he injected in my mouth he started to warming me up with his tongue"
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        s "He went down on me and ate out my pussy that good, that I nearly lost my consciousness during the orgasm.."
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        b "You can be damn sure that you will lose it, when I'll be fucking you, I promise.."
        scene bg atHome171_c5ps with Dissolve (0.75)
        s "I know [bro]... At the end he turned me on my belly, spread my legs that were trembling after previous orgasm - he made it clear that I couldn't move and escape from him even if I would want it"
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171_c5ps with dissolve
        s "So having me caught and helpless like that, he started fucking me from behind as deep and as rough as he could. It was that pleasant, that I was crying during the orgasm that my [father] gave me.."
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        b "That's exactly how I like and will be fucking you Scarlett.."
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        s "I'm ready for that [bro]... Promise that you will be fucking me like a last filthy whore.."
        scene bg atHome171c5_ps22 with Dissolve (0.75)
        scene bg atHome171__c5ps21 with Dissolve (0.75)
        b "You will see no mercy from me Scarlett, I will be fucking you the way your [father] never could.."
        scene bg atHome171c5_ps22 with Dissolve (0.5)
        scene bg atHome171__c5ps21 with Dissolve (0.5)
        s "Oh, yes.."
        scene bg atHome171c5_ps22 with Dissolve (0.5)
        scene bg atHome171__c5ps21 with Dissolve (0.5)
        scene bg atHome171c5_ps22 with Dissolve (0.5)
        scene bg atHome171__c5ps21 with Dissolve (0.5)
        scene bg atHome171c5_ps22 with Dissolve (0.5)
        scene bg atHome171__c5ps21 with Dissolve (0.5)
        scene bg atHome171_c5ps with dissolve
        s "You know, I'm so happy for Julie, she still has to go through it with you and experience those emotions.. Although she still has some doubts about it, but eventually she will be thankful to me.."
        scene bg atHome171c5_ps22 with Dissolve (0.5)
        scene bg atHome171__c5ps21 with Dissolve (0.5)
        scene bg atHome171c5_ps22 with Dissolve (0.5)
        scene bg atHome171__c5ps21 with Dissolve (0.5)
        b "Thankful for what ?!"
        scene bg atHome171c5_ps22 with Dissolve (0.5)
        scene bg atHome171__c5ps21 with Dissolve (0.5)
        scene bg atHome171c5_ps22 with Dissolve (0.5)
        scene bg atHome171__c5ps21 with Dissolve (0.5)
        play sound ("music/sounds/lockSound.mp3")
        "{i}{b}Door Lock Opened"
        scene bg atHome171c5__ps with Dissolve (0.75)
        s "Huh..?"
        scene bg atHome171c4ps with fade
        scene bg atHome171c4ps with vpunch
        b "Oh Fuck, that's the Julie coming out of the bathroom, we should stop or she will see us"
        scene bg atHome171c4ps_ with dissolve
        s "She is still closing bathroom door on the lock ? I thought you guys already passed that base.. Looks like she is really doubting about that kind of relations.."
        b "Get up, now !"
        play sound ("music/sounds/openDoor.mp3")
        scene bg atHome172c4ps with Dissolve (1.25)
        s "Hello Julie, how is the feeling after the shower ?"
        j "Scarlett.."
        scene bg atHome172c3ps with fade
        $ renpy.pause()
        b "Morning, little one.."
        j "[bro], what is going on with.."
        b "{i}Oh shit.."
        j "[bro] I just don't understand what.."
        s "It's not what it looks like.. It's way better - trust me"
        b "Okay Julie, I know there is no excuse for that.."
        j "What are you two..."
        extend "talking about..?!"
        scene bg atHome173_c7__ps with fade
        $ renpy.music.stop(channel=3, fadeout = 5)
        s "Wait, babe what happened ?"
        b "Are you okay Julie ?"
        #jump supportMe
        jump episode8
        return

####################################################EPISODE_8##################################################

    image bg atHome173c6ps = "images/ep8/atHome173c6ps.png"
    image bg atHome173c6_1ps = "images/ep8/atHome173c6_1ps.png"
    image bg atHome173_c7ps = "images/ep8/atHome173_c7ps.png"
    image bg atHome173_c7_ps = "images/ep8/atHome173_c7_ps.png"
    image bg atHome173_c7__ps = "images/ep8/atHome173_c7__ps.png"
    image bg atHome173__c7ps = "images/ep8/atHome173__c7ps.png"
    image bg atHome174c6ps = "images/ep8/atHome174c6ps.png"
    image bg atHome174_c7ps = "images/ep8/atHome174_c7ps.png"
    image bg atHome175c8ps = "images/ep8/atHome175c8ps.png"
    image bg atHome175c9ps = "images/ep8/atHome175c9ps.png"
    image bg atHome175_c10ps = "images/ep8/atHome175_c10ps.png"
    image bg atHome176c7ps = "images/ep8/atHome176c7ps.png"
    image bg atHome177c1ps = "images/ep8/atHome177c1ps.png"
    image bg atHome177c4ps = "images/ep8/atHome177c4ps.png"
    image bg atHome177c5ps = "images/ep8/atHome177c5ps.png"
    image bg atHome177_c1ps = "images/ep8/atHome177_c1ps.png"
    image bg atHome177_c8ps = "images/ep8/atHome177_c8ps.png"
    image bg atHome178c3ps = "images/ep8/atHome178c3ps.png"
    image bg atHome178c5ps = "images/ep8/atHome178c5ps.png"
    image bg atHome178_c3ps = "images/ep8/atHome178_c3ps.png"
    image bg atHome178_c5ps = "images/ep8/atHome178_c5ps.png"
    image bg atHome179c1ps = "images/ep8/atHome179c1ps.png"
    image bg atHome179c4ps = "images/ep8/atHome179c4ps.png"

    image bg bank24c1ps = "images/ep8/bank24c1ps.png"
    image bg bank24_c1ps = "images/ep8/bank24_c1ps.png"
    image bg bank24__c1ps = "images/ep8/bank24__c1ps.png"
    image bg bank25c8ps = "images/ep8/bank25c8ps.png"
    image bg bank25_c2ps = "images/ep8/bank25_c2ps.png"
    image bg bank25_c8ps = "images/ep8/bank25_c8ps.png"
    image bg bank25__c1ps = "images/ep8/bank25__c1ps.png"
    image bg bank25__c3ps = "images/ep8/bank25__c3ps.png"
    image bg bank25__c8ps = "images/ep8/bank25__c8ps.png"
    image bg bank26c1ps = "images/ep8/bank26c1ps.png"
    image bg bank26_c1ps = "images/ep8/bank26_c1ps.png"
    image bg bank26_c3ps = "images/ep8/bank26_c3ps.png"
    image bg bank27c1ps = "images/ep8/bank27c1ps.png"
    image bg bank27_c3ps = "images/ep8/bank27_c3ps.png"
    image bg bank27__c3ps = "images/ep8/bank27__c3ps.png"
    image bg bank28c3ps = "images/ep8/bank28c3ps.png"
    image bg bank28_c1ps = "images/ep8/bank28_c1ps.png"
    image bg bank28_c3ps = "images/ep8/bank28_c3ps.png"
    image bg bank29c2ps = "images/ep8/bank29c2ps.png"
    image bg bank29c3ps = "images/ep8/bank29c3ps.png"
    image bg bank29_c2ps = "images/ep8/bank29_c2ps.png"
    image bg bank30_c8ps = "images/ep8/bank30_c8ps.png"
    image bg bank30c8ps = "images/ep8/bank30c8ps.png"
    image bg bank31c8ps = "images/ep8/bank31c8ps.png"

    image bg fr12c2ps = "images/ep8/fr12c2ps.png"
    image bg fr12_c1ps = "images/ep8/fr12_c1ps.png"
    image bg fr13c2ps = "images/ep8/fr13c2ps.png"
    image bg fr13c3ps = "images/ep8/fr13c3ps.png"
    image bg fr13_c4ps = "images/ep8/fr13_c4ps.png"
    image bg fr13_c5ps = "images/ep8/fr13_c5ps.png"
    image bg fr13_c6ps = "images/ep8/fr13_c6ps.png"
    image bg fr13_c7ps = "images/ep8/fr13_c7ps.png"
    image bg fr13_c8ps = "images/ep8/fr13_c8ps.png"
    image bg fr14c2ps = "images/ep8/fr14c2ps.png"
    image bg fr14c3ps = "images/ep8/fr14c3ps.png"
    image bg fr15c2ps = "images/ep8/fr15c2ps.png"
    image bg fr15c4ps = "images/ep8/fr15c4ps.png"
    image bg fr15_c4ps = "images/ep8/fr15_c4ps.png"
    image bg fr16c1ps = "images/ep8/fr16c1ps.png"
    image bg fr16c3ps = "images/ep8/fr16c3ps.png"
    image bg fr16c4ps = "images/ep8/fr16c4ps.png"
    image bg fr16_c2ps = "images/ep8/fr16_c2ps.png"
    image bg fr16_c2_ps = "images/ep8/fr16_c2_ps.png"
    image bg fr16_c3ps = "images/ep8/fr16_c3ps.png"
    image bg fr16__c2ps = "images/ep8/fr16__c2ps.png"
    image bg fr16__c2ps1 = "images/ep8/fr16__c2ps1.png"
    image bg fr16__c2_ps = "images/ep8/fr16__c2_ps.png"
    image bg fr17c1ps = "images/ep8/fr17c1ps.png"
    image bg fr17_c2ps = "images/ep8/fr17_c2ps.png"
    image bg fr17_c6ps = "images/ep8/fr17_c6ps.png"
    image bg fr17__c2ps = "images/ep8/fr17__c2ps.png"
    image bg fr17__c2_ps = "images/ep8/fr17__c2_ps.png"
    image bg fr18c6ps = "images/ep8/fr18c6ps.png"
    image bg fr18_c6ps = "images/ep8/fr18_c6ps.png"
    image bg fr19c6ps = "images/ep8/fr19c6ps.png"
    image bg fr19_c1ps = "images/ep8/fr19_c1ps.png"
    image bg fr19__c1ps = "images/ep8/fr19__c1ps.png"
    image bg fr20c1ps = "images/ep8/fr20c1ps.png"
    image bg fr20c2ps = "images/ep8/fr20c2ps.png"
    image bg fr20_c1ps = "images/ep8/fr20_c1ps.png"
    image bg fr21c1ps = "images/ep8/fr21c1ps.png"
    image bg fr21_c1ps = "images/ep8/fr21_c1ps.png"

    image bg nApt48c2ps = "images/ep8/nApt48c2ps.png"
    image bg nApt48_c2ps = "images/ep8/nApt48_c2ps.png"
    image bg nApt48__c1ps = "images/ep8/nApt48__c1ps.png"
    image bg nApt48__c2ps = "images/ep8/nApt48__c2ps.png"
    image bg nApt48__c3ps = "images/ep8/nApt48__c3ps.png"
    image bg nApt49c1ps = "images/ep8/nApt49c1ps.png"
    image bg nApt50c11ps = "images/ep8/nApt50c11ps.png"
    image bg nApt50c11ps_ = "images/ep8/nApt50c11ps_.png"
    image bg nApt50c7ps = "images/ep8/nApt50c7ps.png"
    image bg nApt50c9ps = "images/ep8/nApt50c9ps.png"
    image bg nApt50c9ps_ = "images/ep8/nApt50c9ps_.png"
    image bg nApt50_c3ps = "images/ep8/nApt50_c3ps.png"
    image bg nApt50_c4ps = "images/ep8/nApt50_c4ps.png"
    image bg nApt51c11ps = "images/ep8/nApt51c11ps.png"
    image bg nApt51_c11ps = "images/ep8/nApt51_c11ps.png"
    image bg nApt51c7ps = "images/ep8/nApt51c7ps.png"
    image bg nApt51_c9ps = "images/ep8/nApt51_c9ps.png"
    image bg nApt51_c9ps_ = "images/ep8/nApt51_c9ps_.png"
    image bg nApt51_c9ps__ = "images/ep8/nApt51_c9ps__.png"
    image bg nApt52_c9ps = "images/ep8/nApt52_c9ps.png"
    image bg nApt52_c9ps_ = "images/ep8/nApt52_c9ps_.png"
    image bg nApt52c9ps = "images/ep8/nApt52c9ps.png"
    image bg nApt52c9ps_ = "images/ep8/nApt52c9ps_.png"
    image bg nApt53_c10ps = "images/ep8/nApt53_c10ps.png"
    image bg nApt53_c9ps = "images/ep8/nApt53_c9ps.png"
    image bg nApt53c8ps = "images/ep8/nApt53c8ps.png"
    image bg nApt53c8ps_ = "images/ep8/nApt53c8ps_.png"
    image bg nApt54c10ps = "images/ep8/nApt54c10ps.png"
    image bg nApt54c10ps_ = "images/ep8/nApt54c10ps_.png"
    image bg nApt54c10__ps = "images/ep8/nApt54c10__ps.png"
    image bg nApt54c10__ps_ = "images/ep8/nApt54c10__ps_.png"
    image bg nApt54_c8ps = "images/ep8/nApt54_c8ps.png"
    image bg nApt54_c8ps_ = "images/ep8/nApt54_c8ps_.png"
    image bg nApt55c12ps = "images/ep8/nApt55c12ps.png"
    image bg nApt55c12ps_ = "images/ep8/nApt55c12ps_.png"
    image bg nApt55c8ps = "images/ep8/nApt55c8ps.png"
    image bg nApt55c8ps_ = "images/ep8/nApt55c8ps_.png"
    image bg nApt55c9ps = "images/ep8/nApt55c9ps.png"
    image bg nApt55c9ps_ = "images/ep8/nApt55c9ps_.png"
    image bg nApt55_c8ps = "images/ep8/nApt55_c8ps.png"
    image bg nApt55_c8ps_ = "images/ep8/nApt55_c8ps_.png"

    image bg streets30c1ps = "images/ep8/streets30c1ps.png"
    image bg streets30_c2ps = "images/ep8/streets30_c2ps.png"
    image bg streets31c7ps = "images/ep8/streets31c7ps.png"
    image bg streets31_c6ps = "images/ep8/streets31_c6ps.png"
    image bg streets31_fps = "images/ep8/streets31_fps.png"
    image bg streets31_fps_j = "images/ep8/streets31_fps_j.png"
    image bg streets32c6ps = "images/ep8/streets32c6ps.png"
    image bg streets33c1ps = "images/ep8/streets33c1ps.png"
    image bg streets33_c1ps = "images/ep8/streets33_c1ps.png"
    image bg streets33_c2ps = "images/ep8/streets33_c2ps.png"
    image bg streets34c4ps = "images/ep8/streets34c4ps.png"
    image bg streets34_c2ps = "images/ep8/streets34_c2ps.png"
    image bg streets35c3ps = "images/ep8/streets35c3ps.png"
    image bg streets35c4ps = "images/ep8/streets35c4ps.png"
    image bg streets35_c4ps = "images/ep8/streets35_c4ps.png"
    image bg streets35_fc3ps = "images/ep8/streets35_fc3ps.png"
    image bg streets35_f_c3ps = "images/ep8/streets35_f_c3ps.png"
    image bg streets36c1ps = "images/ep8/streets36c1ps.png"
    image bg streets36c5ps = "images/ep8/streets36c5ps.png"
    image bg streets36c6ps = "images/ep8/streets36c6ps.png"
    image bg streets36_c1ps = "images/ep8/streets36_c1ps.png"
    image bg streets36_c4ps = "images/ep8/streets36_c4ps.png"
    image bg streets37c5ps = "images/ep8/streets37c5ps.png"
    image bg streets37c6_ps = "images/ep8/streets37c6_ps.png"
    image bg streets38c2ps = "images/ep8/streets38c2ps.png"
    image bg streets38_c1ps = "images/ep8/streets38_c1ps.png"
    image bg streets38__c1ps = "images/ep8/streets38__c1ps.png"
    image bg streets39c8ps = "images/ep8/streets39c8ps.png"
    image bg streets39_g1c5ps = "images/ep8/streets39_g1c5ps.png"
    image bg streets39_g2c5ps = "images/ep8/streets39_g2c5ps.png"
    image bg streets39_g3c5ps = "images/ep8/streets39_g3c5ps.png"
    image bg streets39_gc5ps = "images/ep8/streets39_gc5ps.png"
    image bg streets39_v1c7ps = "images/ep8/streets39_v1c7ps.png"
    image bg streets39_v2c7ps = "images/ep8/streets39_v2c7ps.png"
    image bg streets39_v3c5ps = "images/ep8/streets39_v3c5ps.png"
    image bg streets39_v3c7ps = "images/ep8/streets39_v3c7ps.png"
    image bg streets39_vc7ps = "images/ep8/streets39_vc7ps.png"

    label episode8:
        scene bg atHome173_c7ps with vpunch
        $ renpy.music.set_volume(0.5, delay=0, channel=3)
        $ renpy.music.play("music/julieMascaraTheme.mp3", channel=3, loop=True, fadein = 3)
        j "No I'm not!"
        j "It burns so bad - I can't open my eyes!"
        scene bg atHome173_c7_ps with dissolve
        j "Damn water stopped flowing just after I started to apply the makeup but I clearly did something wrong so the mascara got right into my eyes! At least I had enough time to properly take a shower!"
        scene bg atHome173_c7ps with vpunch
        j "Argh!"
        b "I'm so sorry Julie. Scarlett, is there something you can do to fix the situation ?"
        s "Just a second babe, let me help you"
        scene bg atHome173_c7__ps with Dissolve(1.0)
        play sound ("music/sounds/sigh.mp3")
        j "*{i}Takes a deep breath{/i}*\nPhew.. I didn't expect that applying a makeup is so difficult. It seems much easier on the video from the internet.."
        j "I tried to clean it with the towel but it only worsen everything and now it is smeared all over my face.."
        scene bg atHome173__c7ps with dissolve
        j "Also I couldn't find any wet wipes at the bathroom, with closed eyes it's quite difficult by the way, so.."
        scene bg atHome173_c7__ps with dissolve
        scene bg atHome174c6ps with fade
        b "They ended just few days ago, I forgot to buy new ones, sorry"
        j "Oh it's okay, [bro].. It wouldn't have happened if I weren't so clumsy.."
        s "Fortunately I have a pair of alcohol free cleansing wipes. Come on Julie, open your eyes - let me take a look."
        j "I'll try babe, but it burns really bad"
        b "{i}Looks like Julie didn't see anything me and Scarlett were doing right before she opened the door.."
        s "By the way [bro], I suggest you to buy some of these wet wipes. They are multifunctional and may come in handy so to say..."
        j "..."
        b "Yeah right.."
        s "You know, it's good to have some of them at home just in case.."
        play sound ("music/sounds/doorBell.mp3")
        "{b}{i}DOOR BELL"
        b "Huh ?"
        j "Are you expecting someone [bro] ?"
        scene bg atHome174_c7ps with fade
        scene bg atHome174_c7ps with vpunch
        j "Ouch!"
        s "Come on Julie, hold still - let me clean it from your eyes. I'm trying as carefully as possible but it will be hard to do if you won't stop moving your head."
        b "I don't have any plans for today except going to the city, have to visit the bank and grab.. some of my stuff from the friend of mine"
        s "Nice, we are just going to the midtown as well. Do you want to join us ?"
        j "Forget it Scarlett, I don't want to go shopping anymore! My mood is gone - I mean just look at me, I'm such a mess!"
        s "Calm down babe, I'll fix it in a minute and will help you to apply the makeup properly this time. Since you don't have the vanity table - let's go to the bathroom because the light in this room is terrible"
        scene bg atHome174_c7ps with hpunch
        j "Ouch!"
        s "I'm so so sorry babe, but there is no other way to clean it"
        b "Good point Scarlett, help Julie and in the meantime I'll take a look who is out there"
        s "So [bro], are you in ?"
        b "Sure, can you girls give me 15 minutes ? Then I'll give you a ride"
        s "Take your time, we are not in a hurry"
        $ renpy.music.stop(channel=3, fadeout = 5)
        b "Okay"
        j "Thank you [bro].."
        b "No problem"
        play sound ("music/sounds/doorBell.mp3")
        "{b}{i}DOOR BELL"
        scene black with Dissolve(1.0)
        play sound ("music/sounds/doorClose.mp3")
        "{b}{i}BATHROOM DOOR CLOSES"
        menu:
            "Open the door":
                play sound ("music/sounds/openDoor.mp3")
        $ renpy.music.play("music/nicoleTheme.mp3", channel=3, loop=True, fadein = 3)
        scene bg atHome175c8ps with Dissolve(2.5)
        $ renpy.pause(0.5)
        n "Hi [bro]..."
        b "Nicole, what a surprise. It's good to see you again, you look amazing "
        n "Thanks, long time no see.. I missed you quite a bit to be honest. Hope I'm not distracting you from something urgent, am I ?"
        menu:
            "I missed you too":
                b "It's okay Nicole, you know that I will always find some time for you no matter what."
                scene bg atHome175c9ps with fade
                n "It's good to hear that [bro], because to be honest I started to think that you're ignoring me, especially after you didn't respond any of my text messages"
                b "Yeah I know, I've seen them but I lost the count of time lately because of work - it's such a madness going on last few days. Sorry if it all seemed like I want to dump you Nicole, I will make it up to you somehow"
                n "It's okay [bro].. I guess you know exaclty 'how' I would like you to make it up to me.. By the way.."
            "I have some plans":
                b "I'm sorry to say that but I'm afraid I don't know when I will be available to set up our next date. There is so much going on right now at work, but I promise that I will find the time for us to meet."
                scene bg atHome175c9ps with fade
                n "It's okay [bro], I totally understand that you have plenty of other things to do. I just wanted to know how you're doing and share with you some good news, I tried to contact with you on the phone but didn't get any response."
                b "Yeah, probably the battery died and the phone run out of juice. So what's the news you wanted to share with me ?"
        scene bg atHome175_c10ps with fade
        n "Do you remember the photoshoot I asked you to participate in ?"
        b "Sure thing, Nicole.. Such things can't be forgotten.."
        play sound ("music/sounds/cameraShot.mp3")
        scene bg nApt43c12ps with cumFlash
        $ renpy.pause()
        play sound ("music/sounds/cameraShot.mp3")
        scene bg nApt46c16ps with cumFlash
        $ renpy.pause()
        play sound ("music/sounds/cameraShot.mp3")
        scene bg nApt45_c15ps with cumFlash
        $ renpy.pause()
        scene bg atHome175_c10ps with cumFlashLong
        n "Well you can congratulate me, I've just returned from the job interview. The agency liked the photos we've made so my test task is completed and now I'm officially a photographer. Thank you again for helping me with this, [bro]"
        b "Don't mention it, Nicole it's least I can do for you. In fact, if you'd like to 'expand' your portfolio with some new photos I don't mind helping you with it again and make new photoshoots with you"
        play sound ("music/sounds/femaleGiggle.mp3")
        n "*{i}Giggles*{/i}\nWell, I'll keep that in mind.. Maybe for the next work session we will come up with something more hot & kinky.."
        b "I wouldn't mind that at all"
        n "By the way, since I finished working for today, I was wondering if you are free at the evening - I'd like to invite you celebrate with me my new job"
        b "I would love to Nicole, however I don't want to make promises that I can't keep, so I'll call you later today and we will agree on the occasion"
        n "Okay [bro], I understand.. There is actually one more thing I wanted to tell you, but it would be much better if you could come over in my apartment so you could take a look at it for yourself"
        b "I don't think I have enough time for this. I promised Julie to drive her at the city."
        n "Don't worry, it won't take long. It's just a little present that I prepared for you.."
        b "Oh, that's intriguing. At least your PC is doing okay, because for a moment I thought that the laptop stopped working again"
        n "No, but the present still deserves more {b}personal touch{/b}.. Your {b}touch{/b} to be specific.."
        b "Okay, give me few minutes, I need to put some clothes on"
        n "Me too [bro].. Anyway, the door will be opened, feel free to come in without knocking - I will be waiting for you.."
        $ renpy.music.stop(channel=3, fadeout = 5)
        scene black with Dissolve(3.0)
        play sound ("music/sounds/openDoor.mp3")
        b "{i}Wow.."
        play sound ("music/sounds/doorClose.mp3")
        b "{i}I have to check how Julie and Scarlett are doing over there"
        menu:
            "Check":
                play sound ("music/sounds/doorKnock.mp3")
        b "*{b}Knock-Knock{/b}*\nIs everything okay, girls ?"
        j "{i}Yeah we are good, Scarlett almost finished"
        s "{i}Don't forget that I still have to apply the new makeup Julie. I don't want those beautiful eyes of yours to get hurt again, so no rush this time"
        j "{i}Well, I guess you'll have to wait for us [bro].. Sorry.."
        b "Okay, I just wanted to let you know that I will be ready in 10 minutes.."
        s "{i}That will be more than enough"
        b "Let's meet at the street and if I'm not there by the time you are ready - get in the car it will be opened"
        j "{i}Okay"
        menu:
            "Get dressed":
                play sound ("music/sounds/clothSounds.mp3")
                b "{i}I wonder what the surprise Nicole prepared for me.."
        jump ep8Nicole
        return

    label ep8Nicole:
        $ renpy.notify ("Bir an sonra..")
        $ renpy.pause()
        play sound ("music/sounds/openDoor.mp3")
        $ renpy.pause()
        play sound ("music/sounds/doorClose.mp3")
        scene bg nApt48_c2ps with Dissolve (2.5)
        b "Uhm, Nicole.. It's me.."
        n "Just a second [bro], I'm almost ready.."
        b "Sure take your time.. You know, actually I feel quite uncomfortable about this 'present' idea. I mean you did everything yourself and considering all that, I don't really understand why I deserved the.."
        $ renpy.music.play("music/nicoleSpankingTheme.mp3", channel=3, loop=True, fadein = 3)
        scene bg nApt48c2ps with Dissolve (1.0)
        n "Were you just saying something [bro]..?"
        $ renpy.pause()
        b "Oh my.."
        n "I didn't know what exactly turns you on so I decided to go for the classic.. Do you like it ?"
        menu:
            "Absolutely":
                b "It's exactly the type of lingerie I love to see on a woman. Black lace bra & panties combined with those sexy stockings just driving me crazy"
                scene bg nApt49c1ps with fade
                n "Wow, looks like my guesses about you were right, I'm glad you like it.."
                b "What guesses..?"
                n "You know, some say that the ones who prefer black colors are actually more passionate and kinky persons.. It's funny but the lingerie often can show you more about the woman than her naked body.."
                b "Is that so"
                $ renpy.pause()
                scene bg nApt48__c2ps with fade
                b "{i}Oh my.. What a view"
                n "Yeah.. It's the black color that conceals their secret desires and true identity at the same exposes their nature.."
                $ renpy.pause()
                scene bg nApt48__c3ps with fade
                b "I would love to know what your secret desires really are, Nicole."
                n "Come on [bro], don't you know that it's inappropriate to ask women that kind of questions.."
                b "Well, how about this time I'll try to guess them, let's play 'Cold & Warm' game."
                $ renpy.pause()
                scene bg nApt48__c1ps with fade
                n "Sounds like a game that might turn me on, what are the rules..?"
                b "Quite simple actually. You are guiding me by saying 'warm' if I'm doing right things or you say 'cold' if the situation moves in a wrong direction"
                n "Okay, I'm in.."
                menu:
                    "Come closer":
                        play sound ("music/sounds/footsteps.mp3")
                scene black with dissolve
                scene bg nApt50_c4ps with fade
                n "Wow that is definitelly a 'warm' one, I like it.."
                $ renpy.pause()
                b "So speaking about Ms. Nicole's secret desires."
                n "Cold.. It's just Nicole, how many times do I.."
                play sound ("music/sounds/assSlap.mp3")
                scene bg nApt50_c3ps with hpunch
                play sound ("music/sounds/sigh.mp3")
                n "Wow.. Getting warmer [bro].."
                b "Who would have thought. So that's what you like."
                n "Kind of.."
                menu:
                    "Bend":
                        play sound ("music/sounds/tableSlide.mp3")
                scene bg nApt50c7ps with fade
                play sound ("music/sounds/femaleGasps.mp3")
                n "Ooh..?!"
                b "Looks like I've got a bad girl over here. Am I right ?"
                scene bg nApt50c11ps with fade
                n "..."
                b "I mean just look at those sweet buttocks - I think they will definitely look better after some spanking."
                n "Oh yeah, it's much warmer now.."
            "Close enough":
                scene bg nApt49c1ps with fade
                b "Nicole you get a 10 points for an attempt, however I prefer more revealing lingerie.."
                n "Oh, I see.. Well, maybe next time we will pick something you like together. Since we didn't know much about each other, it is really difficult to guess what your tastes are.."
                b "Don't worry babe, I'll show you {b}exactly{/b} what I like. Now turn around for me, I want to see that sexy ass of yours"
                scene bg nApt48__c2ps with fade
                n "Like that..?"
                $ renpy.pause()
                b "Yeah, that's a good girl. Damn that sexy ass deserves some attention."
                scene bg nApt48__c1ps with fade
                n "That's why I was talking about your '{b}personal touch{/b}'.."
                b "And now it will get it"
                play sound ("music/sounds/footsteps.mp3")
                scene black with dissolve
                scene bg nApt50_c4ps with fade
                b "You are just fucking amazing Nicole, you know that"
                n "Yeah, I guess I've heard that somewhere two or three times.."
                $ renpy.pause()
                b "Too bad I'm in a hurry right now"
                scene bg nApt50_c3ps with fade
                n "I know.. That's why I told you that it won't take much time - I just wanted to give you a small glimpse at what will be waiting for you at the evening.."
                b "It's not the only thing you give me Nicole. Can you feel it ?"
                play sound ("music/sounds/femaleGiggle.mp3")
                n "Well I guess that's just someone missed me a lot and now is glad to meet.."
                b "Of course, but I'm talking about you deliberately decided to tease me and left me 'blue-balled' with the boner till the evening. Am I right ?"
                n "Maybe.."
                b "Such a bad girl, I knew it."
                $ renpy.pause()
                b "Now.. Bend over that table, I'm gonna give you something you deserved"
                n "As you say.."
                play sound ("music/sounds/tableSlide.mp3")
                scene bg nApt50c7ps with fade
                n "..."
                b "Now we are talking. I like how eagerly you obey to my commands"
                scene bg nApt50c11ps with fade
                n "I've realized how much of a bad girl I really am.. I don't want to worsen the situation further so I'll obey to any of your command.."
                b "Relax, nothing that I couldn't fix happened. You just been behaving naughty and deserved some punishment.."
                b "I'll make you a good girl"
        menu:
            "Spank":
                play sound ("music/sounds/Slap.mp3")
        scene bg nApt50c11ps_ with hpunch
        n "Oh.."
        scene bg nApt50c11ps with Dissolve(0.75)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt50c11ps_ with hpunch
        b "It's such a firm and curvy - I've been waiting it for so long"
        scene bg nApt50c9ps_ with fade
        n "Yes, don't stop.."
        scene bg nApt50c9ps with Dissolve(0.75)
        menu:
            "Spank":
                play sound ("music/sounds/Slap.mp3")
        scene bg nApt51_c9ps_ with hpunch
        n "Oh yeah, that's hot.."
        scene bg nApt51c7ps with fade
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt51c7ps with hpunch
        b "You are so bad Nicole, you know that ?"
        scene bg nApt50c11ps with fade
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt50c11ps_ with hpunch
        n "Yes.."
        scene bg nApt50c11ps with Dissolve(0.75)
        menu:
            "Spank harder":
                play sound ("music/sounds/Slap.mp3")
        scene bg nApt50c11ps_ with hpunch
        n "Oh.. Just like that.."
        play sound ("music/sounds/sighLoud.mp3")
        scene bg nApt51c11ps with Dissolve(0.75)
        b "Well-well, looks like someone starts really enjoying it"
        n "Please don't stop.."
        scene black with dissolve
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt51_c9ps with hpunch
        b "It's up to me to decide when to stop, do you understand ?!"
        n "Yes.."
        scene bg nApt51_c9ps__ with Dissolve(0.75)
        b "That's a good girl"
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt52c9ps with hpunch
        n "Oh yes.."
        scene bg nApt52c9ps_ with Dissolve(0.75)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt52c9ps with hpunch
        n "Ah.."
        b "Do you like it ? Do you like being spanked like a naughty little girl ?"
        scene bg nApt52_c9ps_ with Dissolve(0.75)
        n "..harder.."
        b "What was that ?"
        scene bg nApt52_c9ps with Dissolve(0.75)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt52c9ps with hpunch
        n "Harder !"
        b "Oh, so that's how you want it.."
        scene bg nApt51c11ps with fade
        b "You forgot something"
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt51_c11ps with hpunch
        n "Ah.. please.."
        scene bg nApt51c11ps with Dissolve(0.75)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt51_c11ps with hpunch
        b "Sorry, can't hear you"
        scene bg nApt51c11ps with Dissolve(0.75)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt51_c11ps with hpunch
        n "Spank harder please.."
        b "Say it like you mean it, girl"
        scene bg nApt51c11ps with Dissolve(0.75)
        n "SPANK ME HARDER PLEASE!!!"
        b "Now we are talking"
        menu:
            "Spank Harder":
                scene black with dissolve
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt53_c9ps with hpunch
        scene bg nApt53_c9ps with hpunch
        play sound ("music/sounds/sighLoud.mp3")
        n "Ah.. That feels good"
        b "Look at you Nicole, you're asking for being spanked"
        n "I'm not asking.. I'm {b}begging{/b} you to spank my little ass, I've deserved it.. I'm such a bad girl.."
        scene bg nApt53_c10ps with fade
        b "I want to know what's on your mind Nicole."
        n "..."
        menu:
            "Squeeze":
                play sound ("music/sounds/sighLoud.mp3")
        scene bg nApt54c10__ps with vpunch
        b "Tell me what you are thinking of right now"
        scene bg nApt54c10__ps_ with Dissolve(0.75)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt54c10ps_ with hpunch
        scene bg nApt54c10ps_ with hpunch
        n "Oh..."
        b "While I'm spanking you like a horny slut"
        scene bg nApt54c10__ps_ with Dissolve(0.75)
        n "I am.. I'm thinking about your huge throbbing cock [bro]"
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt54c10ps_ with hpunch
        scene bg nApt54c10ps_ with hpunch
        n "Yes.. I want to suck on it.. I want to feel it inside of me.."
        scene bg nApt54c10ps with Dissolve(0.75)
        b "Yeah ? You want me to fuck you from behind like a dirty whore ?"
        scene black with dissolve
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt54_c8ps_ with vpunch
        scene bg nApt54_c8ps_ with vpunch
        play sound ("music/sounds/sighLoud.mp3")
        n "Yes.. I want it rough.. I.."
        scene bg nApt53c8ps with Dissolve(0.75)
        b "I will have it my way with you Nicole, I promise"
        n "Oh yes, please continue, I'm about to cum.."
        scene bg nApt53c8ps_ with Dissolve(0.75)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt54_c8ps_ with vpunch
        scene bg nApt54_c8ps_ with vpunch
        play sound ("music/sounds/sighLoud.mp3")
        n "Ah.."
        scene bg nApt53c8ps with Dissolve(1.25)
        scene bg nApt53_c9ps with fade
        n "But most of all I want you to keep spanking me like that while you will be fucking me balls-deep.."
        b "Argh, you know exactly what to say - such a good girl"
        scene bg nApt55c9ps_ with Dissolve(0.25)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c9ps with hpunch
        scene bg nApt55c9ps with hpunch
        $ renpy.music.set_volume(1.0, delay=0, channel=1)
        $ renpy.music.play("music/sounds/sighLoud.mp3", channel=1, loop=False, fadein=0)
        b "Take it !{nw}{w=0.75}"
        scene bg nApt55c9ps_ with Dissolve(0.25)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c9ps with hpunch
        scene bg nApt55c9ps with hpunch
        play sound ("music/sounds/sighLoud.mp3")
        n "Oh yes, just like that !{nw}{w=1.0}"
        scene bg nApt55c9ps_ with Dissolve(0.25)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c9ps with hpunch
        scene bg nApt55c9ps with hpunch
        $ renpy.music.play("music/sounds/sighLoud.mp3", channel=1, loop=False, fadein=0)
        n "I'm about to cum ! Don't stop{nw}{w=1.0}"
        scene bg nApt55c9ps_ with Dissolve(0.25)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c9ps with hpunch
        scene bg nApt55c9ps with hpunch
        $ renpy.music.play("music/sounds/sighLoud.mp3", channel=1, loop=False, fadein=0)
        b "Who is the bad girl, huh ?{nw}{w=1.0}"
        scene bg nApt55c9ps_ with Dissolve(0.25)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c9ps with hpunch
        scene bg nApt55c9ps with hpunch
        $ renpy.music.play("music/sounds/sighLoud.mp3", channel=1, loop=False, fadein=0)
        n "I am.. I am the bad girl..{nw}{w=1.0}"
        scene bg nApt55c12ps_ with fade
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c12ps with hpunch
        scene bg nApt55c12ps with hpunch
        $ renpy.music.play("music/sounds/sighLoud.mp3", channel=1, loop=False, fadein=0)
        b "This ass belongs to me now, and I will do whatever I want with it, is that clear bitch ?{nw}{w=3.0}"
        scene bg nApt55c12ps_ with dissolve
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c12ps with hpunch
        scene bg nApt55c12ps with hpunch
        play sound ("music/sounds/sighLoud.mp3")
        n "Ah.. Yes.. Almost there !{nw}{w=1.0}"
        scene bg nApt55c8ps_ with fade
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c8ps with hpunch
        scene bg nApt55c8ps with hpunch
        play sound ("music/sounds/sighLoud.mp3")
        b "Whose ass is that, huh ?{nw}{w=1.0}"
        scene bg nApt55c8ps_ with dissolve
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c8ps with hpunch
        scene bg nApt55c8ps with hpunch
        play sound ("music/sounds/sighLoud.mp3")
        n "I'm coming !{nw}{w=1.0}"
        b "Tell me whose ass is that, slut !{nw}{w=1.0}"
        scene bg nApt55c8ps_ with Dissolve(0.15)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c8ps with hpunch
        scene bg nApt55c8ps_ with Dissolve(0.15)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c8ps with hpunch
        scene bg nApt55c8ps_ with Dissolve(0.15)
        play sound ("music/sounds/Slap.mp3")
        scene bg nApt55c8ps with hpunch
        scene bg nApt55c8ps_ with Dissolve(0.15)
        play sound ("music/sounds/Slap.mp3")
        $ renpy.music.play("music/sounds/sighLoud.mp3", channel=1, loop=False, fadein=0)
        scene bg nApt55c8ps with hpunch
        scene bg nApt55_c8ps with cumFlash
        play sound ("music/sounds/Slap.mp3")
        $ renpy.music.play("music/sounds/sighLoud.mp3", channel=1, loop=False, fadein=0)
        scene bg nApt55_c8ps_ with cumFlash
        scene bg nApt55_c8ps with cumFlash
        play sound ("music/sounds/Slap.mp3")
        $ renpy.music.play ("music/sounds/climax.mp3", channel=1, loop=False, fadein=0)
        scene bg nApt55_c8ps_ with cumFlashLong
        $ renpy.music.set_volume(0.5, delay=0, channel=1)
        $ renpy.music.play ("music/sounds/breathAfterClimax.mp3", channel=1, loop=True, fadein=0)
        scene bg nApt55_c8ps_ with vpunch
        scene bg nApt55_c8ps_ with vpunch
        scene bg nApt55_c8ps_ with vpunch
        scene bg nApt55_c8ps_ with vpunch
        scene bg nApt55_c8ps_ with vpunch
        n "It's yours it's yours ! Aaahhh..."
        n "{i}*Panting*"
        b "Wow, I wouldn't believe that you can cum from being spanked.. Didn't know that you're so much into it.."
        $ renpy.music.stop(channel=1, fadeout = 3)
        n "{i}*Panting*{/i}\nThere is a lot of things you don't know about me.."
        b "I can't wait to get to know them all Nicole.."
        $ renpy.music.stop(channel=3, fadeout = 5)
        n "Evening.. Today.. I'll be waiting for you [bro]"
        b "You are the best.."
        scene black with Dissolve (3.0)
        jump ep8girls
        return

    label ep8girls:
        $ renpy.notify ("O esnada..")
        $ renpy.pause()
        scene bg atHome176c7ps with Dissolve(2.5)
        $ renpy.music.set_volume(0.5, delay=0, channel=3)
        $ renpy.music.play ("music/girlsChillTheme.mp3", channel=3, loop=True, fadein=3)
        s "See ?! What did I tell you - it's looking much better now. With this makeup you look sexy as hell, Julie. Why are you still so sad ?"
        j "Well, I guess. Nevermind - I probably just didn't calm down entirely after the morning failure"
        scene bg atHome173c6ps with fade
        s "You know as the saying goes 'Practice makes perfect', and this applies not only to makeup. By the way how are the things with [bro] going on ?"
        scene bg atHome173c6_1ps with dissolve
        j "Right, he's waiting for us outside and I still stand here without pants. I need to quickly get dressed."
        play sound ("music/sounds/couchSqueak.mp3")
        scene bg atHome177_c1ps with fade
        s "No need to rush, we still have some time. So, what is going on between you two ?"
        play sound ("music/sounds/clothSounds.mp3")
        j "Well.. It's quite complicated.."
        j "Even considering the situation.. I mean, I'm still not sure that this whole idea will lead to something good.."
        scene bg atHome177c1ps with dissolve
        s "Trust me - everything will be amazing. You just need to get rid of all those anxious thoughts and stop thinking of what could happen or might go not exactly as you planned"
        j "I know and understant this, I mean it's just.. Knowing what to do and actually do it are not the same things.."
        scene bg atHome179c1ps with dissolve
        s "Wow, those are really sexy pants Julie, I haven't seen them before - black color suits you"
        j "Thank you babe"
        scene bg atHome177_c8ps with fade
        s "So, speaking about you and [bro].."
        j "Yeah.. Ahm.. Last night I decided to step up a little.."
        s "Oh, that is interesting. Give me the details"
        scene bg atHome178c5ps with fade
        j "Well, I happened to see and touch his cock.. It's so huge by the way.."
        s "Way to go girl, although I was thinking that you two are already got to the oral sex, but hey - you have to start with something anyway. So what did he say ?"
        scene bg atHome177c4ps with fade
        j "What do you mean ?"
        scene bg atHome179c4ps with Dissolve(0.75)
        s "What were his words and reaction while you were wrapping your hand around his amazing cock ?"
        j "I don't know.. [bro] was sleeping, maybe he woke up at some point but it wasn't for too long - I decided to stop at some point.."
        scene bg atHome178c5ps with fade
        s "What ?!"
        j "I mean, I guess he liked it.. That thing was hard as rock.."
        scene bg atHome178c5ps with hpunch
        s "No-no-no, that's not how a dick works Julie. You don't want to do that again. You stopped giving him a hand right before he was about to cum - that's not cool and called 'blue-balls'"
        s "I mean sometimes it serves a specific purpose... But generally you must not leave a guy blue balled, it's actually harmful for the health"
        scene bg atHome178_c5ps with dissolve
        j "Oh, my bad.. I just got scared thinking of what [bro] would say, seeing me jerking him in the middle of the night.."
        s "Really ? That's strange, 'cause I thought you are taking it more eagerly"
        j "I wish so.. The thing is, I'm  that lustful and naughty only with you. He is my [brother] after all, I can't just ignore that fact and I still have doubts about this whole idea.. I'm afraid that I will not succeed.."
        scene bg atHome178_c3ps with fade
        s "Come on girl, we are women - the ones who own the most powerfull and elegant 'weapon' - which is the beauty and sexuallity"
        s "It's our nature to attract and we all know how to seduce a man, even subconsciously - it's just a matter of mastering this 'Art' that's all"
        scene bg atHome178_c5ps with fade
        j "I don't know, it all sounds so difficult and unfamiliar to me.."
        s "Remember what I told you ? You just need to relax, don't try to plan everything ahead. Just trust your instincts and let your female nature out"
        j "You know, it was much simplier back when I was just angry at [bro]. I had clear thoughts about what I want and what needs to be done.. But now it's such a mess, everytime I talk to him I always feel the goosebumps on my back and a tickling feeling down my belly.."
        s "It's a good sign actually - that's what I'm talking about - those are true feelings. You are in love with your [brother] Julie, that is awesome"
        scene bg atHome178c5ps with dissolve
        j "Is it ? I thought you would be jealous"
        play sound ("music/sounds/femaleGiggle.mp3")
        s "*{i}Giggles{/i}*\nWhy would I ?! You are the [family] after all.."
        scene bg atHome178_c5ps with dissolve
        j "That's not funny Scarlett..."
        scene bg atHome178_c3ps with fade
        s "I'm serious babe.. Look, if you are okay with it then I'm okay too. I'll help you as much as I can with it, I only want the best for you Julie. If you ever need something just ask."
        s "The only thing that really disturbs me about you and [bro] is.."
        scene bg atHome177c1ps with fade
        s "If it will continue to go on like this, I'm afraid that I will eventually fuck him faster than you.."
        j "What ?!"
        scene bg atHome179c4ps with fade
        s "Come on Julie, he is a handsome, and as far as I remember you told that you wouldn't mind me and [bro] have some fun together"
        j "Well, yes.. But I didn't think that you and [bro] will hookup that quickly.."
        s "I would say more than quickly: I was giving your [brother] a hand and almost had his cock in my mouth right before you came out of the bathroom."
        scene bg atHome179c4ps with hpunch
        scene bg atHome179c4ps with hpunch
        j "WHAT ?!"
        scene bg atHome178c3ps with fade
        s "Yeah, I was hoping that you would join us - I had no idea that you and [bro] stuck on a 'Second Base', or should I say 'First Base plus' considering that he was sleeping.."
        j "I can't belive that.."
        s "Yeah, me too - I expected he would cum in my mouth or in yours. Damn, thinking about giving [bro] a blowjob turns me on so bad"
        scene bg atHome177c5ps with fade
        j "You such a slut Scarlett, you know that ?!"
        s "Sure.. That's why you love me babe. "
        scene bg atHome178c3ps with fade
        s "Hey I have an idea, how about you and me make a deal - the first of us who gets fucked by [bro] wins"
        scene bg atHome179c4ps with fade
        j "Ha-ha, that's not fair Scarlett, you've already started working in that direction"
        scene bg atHome177c4ps with dissolve
        s "Well, how about that - I can equalize our chances by leaving [bro] alone for few days"
        j "Sounds fun but it's not a competition Scarlett.. Maybe we will talk about it later when I'll be ready"
        scene bg atHome178_c3ps with fade
        s "Okay babe, as you say. Sorry if it all was a bit too much - I just wanted to cheer you up a bit by bringing competitive spirit. I'm worrying about you"
        scene bg atHome178_c5ps with fade
        j "Nevermind, everything is great, it's just.. I mean there is so much things on my mind right now"
        s "Oh I see, uhm.. How about a joke ? If this is the sexiest lingerie you have - no wonder that [bro] still didn't make you his little slut. These granny drawers are only capable of invoking an anti-boner"
        scene bg atHome177c5ps with dissolve
        j "Ha-ha, shut up ! Just for the record I already have incredibly sexy panties - Vicky bought it to me."
        s "One pair of panties is not enough Julie - your wardrobe definitely needs to be renewed. No worries I'll help you with that."
        $ renpy.music.stop(channel=3, fadeout = 5)
        j "Okay. Let's go, [bro] probably already tired waiting for us"
        $ renpy.pause()
        scene black with Dissolve(2.5)
        jump ep8streets
        return

    label ep8streets:
        $ renpy.notify ("Bu günün ilerleyen saatlerinde..")
        $ renpy.pause()
        $ renpy.music.set_volume(0.75, delay=0, channel=3)
        $ renpy.music.set_volume(0.25, delay=0, channel=1)
        $ renpy.music.play ("music/streetAmbient.mp3", channel=3, loop=True, fadein=3)
        $ renpy.music.play ("music/sounds/engineWorking.mp3", channel=1, loop=True, fadein=3)
        scene bg streets30c1ps with Dissolve(2.5)
        b "Here we are girls, the midtown. Sorry, I can't get you closer to the clothing store - that street is pedestrian only at this time."
        j "That's okay [bro], thanks. Me and Scarlett will take a walk from here.."
        s "Wow, didn't know you're so good at driving [bro]. Are you sure you're not some kind of undercover {i}Uver's{/i} driver ?!"
        b "Unfortunatelly not - I'm just a regular wanted thug who doesn't mind shoot at people from time to time."
        j "..."
        b "But hey, I would consider working a taxi driver if all my clients were as pretty as you girls."
        s "Ha-ha, that's a good one [bro]"
        menu:
            "Exit":
                scene black with dissolve
        play sound ("music/sounds/carDoorClose.mp3")
        $ renpy.music.set_volume(1.0, delay=0, channel=3)
        $ renpy.music.set_volume(0.5, delay=0, channel=1)
        scene bg streets30_c2ps with fade
        $ renpy.pause()
        b "Here is the bank I was talking about. I need to close my account and grab some stuff from the manager - I don't think it will take much time"
        j "I'm still scared of this place.."
        scene bg streets31_c6ps with fade
        s "I'm sorry babe - can't imagine what you've been through."
        b "Sorry Julie, I should have thought about it before driving you here."
        j "Nevermind - I'm okay.. Looks like there are no people at the building - are you sure it's working today ?"
        b "There has to be someone. Anyway, I don't think that you girls should be waiting for me here - that will be just a waste of time. So you'd better go to the clothing store and I will meet you there."
        play sound ("music/sounds/carDrive2.mp3")
        scene bg streets31c7ps with fade
        s "Sounds cool. The store is about 300 yards down the street, you won't miss it. It's called 'Queen of the Night'..."
        scene bg streets31_fps_j with Dissolve(0.25)
        j "Really ? What a coincidence - I've already been there with Vicky. The store has the best choice of lingerie in the city, at least that's what she said."
        scene bg streets31_fps with Dissolve(0.25)
        s "She is right - looks like me and her have the good taste in common. Now I'm even more thrilled to meet Vicky"
        j "Well, I hope we will meet soon and I will introduce you to each other.."
        b "Uhm..{nw}{w=0.75}"
        scene bg streets31c7ps with dissolve
        b "Are you girls still sure that my presence at the store is really necessary ? I mean you have each other for honest opinion on whether the lingerie fits you or not."
        play sound ("music/sounds/carDrive3.mp3")
        s "Of course - me and Julie just suddenly felt that we lack a male's opinion, right babe ?"
        scene bg streets31_c6ps with fade
        j "Yeah, we would like you to tell us from the men's perspective which lingerie looks better and more sexier on Scarlett.."
        play sound ("music/sounds/hawking.mp3")
        scene bg streets31_c6ps with hpunch
        s "{i}*Clearing throat*{/i}\nUghm-grhm!"
        j "..and on me too.. Of course if I find some lingerie that I might like and can afford, huh.."
        scene bg streets31c7ps with fade
        b "Oh, I thought since you're into girls - you don't bother what men think of you."
        s "Some things never change [bro], but some things do.."
        play sound ("music/sounds/carDrive2.mp3")
        scene bg streets32c6ps with fade
        b "Ok I'll be there"
        j "Bye [bro], see you soon"
        s "We will be waiting for you.."
        b "Take care, girls"
        $ renpy.music.stop(channel=1, fadeout = 3)
        menu:
            "Lock the car":
                play sound ("music/sounds/carLock.mp3")
        $ renpy.music.stop(channel=3, fadeout = 5)
        $ renpy.pause(1.0)
        scene black with Dissolve (2.5)
        jump ep8bank
        return

    label ep8bank:
        $ renpy.notify ("Bir an sonra..")
        $ renpy.pause()
        $ renpy.music.set_volume(1.0, delay=0, channel=3)
        $ renpy.music.play ("music/bankTheme0.mp3", channel=3, loop=True, fadein=2)
        scene bg bank24c1ps with Dissolve(2.5)
        define mrk = Character("Markus", color="#42ddf5")
        mrk "... I never actually understood our coordinator's policy regarding sharing cellphone numbers either - it would be so much simpler, right ? To be honest I didn't expect you to show up here that soon, but anyway - I'm glad to see you, pal"
        b "Yeah, sorry for this sudden visit - there is nothing personal Markus, but I'd like to 'play this one pretty close to the chest'. Anyway it's good that my guesses were correct and you are here. I didn't know whether the bank will be open or closed."
        mrk "Even though we are officially closed but someone has to sit here and provide cops the access to evidences or whatever they might need."
        b "The investigation still not finished ?"
        mrk "Nah.. They told it will be done in few days or so. Though nothing was stolen - it takes the eternity for those government freeloaders to close the case. Imagine if some money were really stolen ?! You can be damn sure those dumbasses won't return anything."
        scene bg bank24__c1ps with Dissolve(0.25)
        mrk "But why I have to suffer from their incompetence ?! I mean I feel myself like a fucking 'Hachiko' waiting here until they will need something. I'm literally dying of boredom here - I was even thinking about ordering myself a hooker from the escort right at this place."
        scene bg bank24c1ps with Dissolve(0.25)
        play sound ("music/sounds/phoneMessage.mp3")
        "{b}{i}PHONE MESSAGE"
        b "Is it yours ? The phone.."
        scene bg bank24_c1ps with Dissolve(0.25)
        mrk "Huh..."
        extend " Speaking about the devil - looks like the feds finally woke up - excuse me, I need to send some information to the... 'Robbery Investigation Department'. Damn, what a name huh.."
        $ renpy.music.play ("music/sounds/phoneTyping.mp3", channel=1, loop=True, fadein=0)
        "{b}{i}Markus is typing..."
        b "Actually I came here on business - I would like to take something I left and asked you to keep an eye on. Sorry for hurrying you up - I'm afraid I don't have much time"
        play sound ("music/sounds/phoneMessage.mp3")
        "{b}{i}PHONE MESSAGE"
        mrk "Just a second..."
        $ renpy.music.stop(channel=1, fadeout = 0)
        play sound ("music/sounds/messageSent.mp3")
        mrk "Done.."
        scene bg bank24c1ps with Dissolve(0.25)
        mrk "Sure thing [bro], it's here and safely hidden in my stash. Cops turned everything upside down here but that didn't help them to find your weapon."
        scene bg bank24__c1ps with Dissolve(0.25)
        mrk "Let me know if you will need it back"
        scene bg bank24c1ps with Dissolve(0.25)
        b "The circumstances require me to take it back right now, also I would like to withdraw all my money and close the bank account - I have a feeling that all this stuff will come in handy very soon..."
        play sound ("music/sounds/phoneMessage.mp3")
        "{b}{i}PHONE MESSAGE"
        scene bg bank24_c1ps with Dissolve(0.25)
        $ renpy.music.play ("music/sounds/phoneTyping.mp3", channel=1, loop=True, fadein=0)
        mrk "Excuse me.. I don't mean to be rude but I have to answer this one"
        b "..."
        mrk "Looks like they even more stupid than I thought.."
        b "So what about my request ?"
        $ renpy.music.stop(channel=1, fadeout = 0)
        play sound ("music/sounds/messageSent.mp3")
        scene bg bank24c1ps with Dissolve(0.35)
        mrk "Sorry.. Right, closing your account.. Uhm.."
        $ renpy.music.set_volume(1.0, delay=0, channel=4)
        $ renpy.music.play ("music/bankTheme1.mp3", channel=4, loop=True, fadein=2)
        $ renpy.music.stop(channel=3, fadeout = 2)
        mrk "I need your actual living address in order to close account properly. Hope you understand - currently feds are 'sniffing around' so I have to leave no trails"
        b "Why not just use the fake one - the same that is currenlty used ?"
        scene bg bank24__c1ps with Dissolve(0.5)
        mrk "You know.. Those damn cops are paying a lot of attention to operations with the bank accounts, especially after the robbery.. They are not interested in old accounts but they very carefully analyze all new operations. It will be suspicios if I specify the non-existing address. What if they would want to check it ?"
        if ep5killCounter > 0:
            mrk "Besides you killed one of those guys - so I'm sure cops are watching you closely"
        scene bg bank24c1ps with Dissolve(0.35)
        mrk "So I don't want more problems than I already have - I hope you understand"
        play sound ("music/sounds/phoneMessage.mp3")
        "{b}{i}PHONE MESSAGE"
        scene bg bank24_c1ps with Dissolve(0.25)
        $ renpy.music.play ("music/sounds/phoneTyping.mp3", channel=1, loop=True, fadein=0)
        b "Sorry Markus but I don't want to expose myself either - I just want to take what belongs to me, that's it. I mean are we still in the 'same boat' ?"
        $ renpy.music.play ("music/sounds/phoneTyping.mp3", channel=1, loop=True, fadein=0)
        mrk "Uhm.. One second please.."
        b "Isn't all the money here dirty and the most of clients our guys - cause I have a feeling that I've came to the wrong bank. There are tons of cash in the safe, what's the problem of giving me my deposit like any other one ?!"
        mrk "..."
        b "Markus ?"
        mrk "Yeah, sorry"
        $ renpy.music.stop(channel=1, fadeout = 0)
        play sound ("music/sounds/messageSent.mp3")
        scene bg bank24c1ps with Dissolve(0.25)
        mrk "The thing is those money is 'sealed' until the investigation is complete"
        b "Damn I really need those 100 grands.. Is there something you can do ?"
        scene bg bank24__c1ps with Dissolve(0.25)
        mrk "Well.. Let me think... Uhm... How about.. Oh, I know - I can suggest you this: I have some money at this bank, but I prefer to keep them in a bank-cells."
        mrk "If you could give me 10 minutes - I can go to the safe and grab the cell - thus giving you my money. When your money will be 'unsealed' I'll just put them in my cell instead. Sounds good ?"
        menu:
            "Yes":
                scene bg bank24c1ps with Dissolve(0.25)
                mrk "Cool, you can wait for me here I'll return quickly. Sorry the coffee machine isn't working but as for other things - feel yourself at home, I'll be right back."
                b "Okay"
                $ renpy.music.stop(channel=4, fadeout = 10)
                scene black with Dissolve(3.0)
                $ renpy.notify ("15 dakika sonra..")
                $ renpy.pause(2.0)
                scene bg bank30c8ps with Dissolve(2.5)
                b "{i}Damn, why is it taking so long.. I should go and check if everything is ok over there"
                menu:
                    "Check":
                        play sound ("music/sounds/openDoor.mp3")
                scene bg bank30_c8ps with dissolve
                $ renpy.music.set_volume(0.5, delay=0, channel=1)
                $ renpy.music.set_volume(0.5, delay=0, channel=3)
                $ renpy.music.play ("music/sounds/doorClose.mp3", channel=1, loop=False, fadein=0)
                mrk "That's me"
                b "Finally ! I started to worry about you Markus - thought you are lost in the maze of gold or got yourself under one of those heavy pallets with money"
                mrk "Huh, I'm okay.. It's a shame that I can't say the same about you and your money"
                b "Why is that ?"
                mrk "You won't need them - dead men need no money"
                $ renpy.music.play("music/warehouseTheme.mp3", channel=1, loop=True, fadein=2)
                $ renpy.music.play("music/sounds/heartBeat.mp3", channel=3, loop=True, fadein=2)
                b "What is that supposed to..{nw}{w=1.0}"
                play sound ("music/sounds/openDoor.mp3")
                scene bg bank31c8ps with dissolve
                scene bg bank31c8ps with vpunch
                b "WHAT THE FUCK ?!"
                nac "Well well well... Look who we got here - long time no see punk"
                mrk "Here you go gentlemen - just as I promised"
                scene bg bank31c8ps with vpunch
                b "You fucking traitor Markus - I trusted you !"
                nac "Shut the fuck up bitch - your ass is in my hands now !"
                roc "He is right - kill the traitor"
                mrk "What?!{nw}{w=0.75}"
                play sound ("music/sounds/pistolShot.mp3")
                $ renpy.music.set_volume(2.5, delay=0, channel=5)
                $ renpy.music.play("music/sounds/noise.mp3", channel=5, loop=False, fadein=0)
                scene black with cumFlashLong
                b "FUCKING HELL !"
                roc "Now you gonna tell me everything I want to know, then I will kill you"
                $ renpy.music.stop(channel=1, fadeout=2)
                $ renpy.music.stop(channel=3, fadeout=2)
                $ renpy.pause(2.0)
                jump gameOver
            "No":
                b "I don't have time for this - I guess I'll just take the gun and will come back for the money some other day."
                scene bg bank24c1ps with dissolve
                mrk "Suit yourself [bro], to me 10 min is not a big deal - but if you're in a rush let's stop wasting your precious time."
                scene black with Dissolve(1.0)
                play sound ("music/sounds/footsteps.mp3")
                $ renpy.music.play ("music/bankTheme2.mp3", channel=3, loop=True, fadein=2)
                $ renpy.music.stop(channel=4, fadeout = 2)
                $ renpy.pause(1.0)
                scene bg bank25c8ps with Dissolve(2.0)
                mrk "Can I ask you something ? What is it so special about this gun ? I mean it definitely looks futuristic but I'm sure that it's not the only weapon you have in your gear, right ?"
                menu:
                    "Yes":
                        b "Of course I have plenty of other weapon - but this one is something I wouldn't believe if I didn't hold it in my hands."
                    "No":
                        b "Unfortunately this is the only gun I have right now, at least the one which is that advanced."
                mrk "That's interesting.. I mean you can still shot someone from this gun just by pulling the trigger, right ?"
                scene bank25_c2ps with fade
                b "Yeah, no two step authentication is needed - just aim and shoot the motherfucker. By the way this thing even helps you to aim so all you really have to do is kill."
                mrk "Wow that sounds really 'dope'. I guess none of our guys have such hi-tech equipment. I wonder where did you get it ?"
                scene bank25_c8ps with fade
                b "Well, actually I didn't expect to get something advanced and futuristic like this but.."
                $ renpy.music.stop(channel=3, fadeout = 5)
                $ renpy.music.play ("music/warehouseTheme.mp3", channel=4, loop=True, fadein=5)
                mrk "Forget about it - actually I'm not interested at all. I mean who cares how did you get it, if now this gun belongs to me !"
                scene bank25__c8ps with Dissolve(0.25)
                scene bank25__c8ps with hpunch
                b "What the heck ?!"
                mrk "Hope you won't mind if I keep it to myself. Also thanks a lot for your money - I'll find a good use for it as well."
                b "Put the gun down Markus, don't do stupid things"
                scene bg bank25__c3ps with fade
                mrk "Let's clarify the situation [bro] - I don't want to shoot you, but if you won't listen to me and make the attempt to escape you will leave me no choice so I will have to kill you."
                scene bg bank25__c1ps with fade
                mrk "Sit still in that chair until they will show up"
                b "So that's how it will end huh.. You've been lying to me all this time - there is no the 'Robbery Investigation Department' - you've been messaging with those bustards, trying to hold me up as long as possilbe. It was you who sold them the security codes from the safe"
                scene bg bank26c1ps with dissolve
                mrk "Not exactly - my assistant Jose did that, he was their man at the bank. I decided to join them later"
                b "But why Markus..?"
                scene bg bank25__c1ps with dissolve
                mrk "It's quite simple - I want to live and want to have a lot of money. Me and Jose talked to the new guys, made a deal and came up with an agreement: we sell out everyone we know - instead taking their money share at the bank"
                mrk "Unfortunately while I was helping you to stop the robbery I still was on a wrong side and didn't know the whole benefits that I could get. So now I have to 'pay a damage' and provide them some compensation by giving you away"
                b "So all this only because of money..?"
                scene bg bank26c1ps with dissolve
                mrk "Nothing personal [bro], it's just my life or yours - I assume you'd have the same preference as I do"
                b "What's next Markus..? Aren't you going at least try to do something right, try to stop them ?! They won't expect such scenario, so you and I will have an advantage.."
                mrk "Don't be ridiculous [bro], you probably know nothing about those guys. They can't be stopped - they are everywhere and every criminal in this city works for them. They even have few people at the local police department - can you imagine the level of influence they have in this city ?"
                scene bg bank25__c1ps with dissolve
                mrk "It's a suicide to fight against them alone."
                b "I'm not alone, so are you.."
                scene bg bank26c1ps with dissolve
                mrk "When was the last time you talked to any of our guys, huh ?! After the general meeting everything completely fucked up - the smartest of us switched over from the very beginning, the most stupid are already dead - even the coordinator went silent, which means that it's over.."
                mrk "Too bad it's me who happened to sell you out, but I'm telling you this again - there is nothing personal just business."
                b "So you've made your decision - very well then.."
                menu:
                    "Get up":
                        scene bg bank26_c1ps with dissolve
                mrk "What the hell do you think you are doing - sit the fuck down or I'll kill you !"
                b "You wouldn't Markus.."
                scene  bg bank26_c3ps with fade
                mrk "I wouldn't ?! Why the fuck is that ?! You don't think I will ???"
                b "No..."
                mrk "You probably think I won't shoot cause they need you alive - they don't care about that shit ! So sit in that fucking chair - last warning !"
                b "I know.. There is another reason why.."
                $ renpy.music.stop(channel=4, fadeout = 3)
                scene  bg bank26_c3ps with hpunch
                mrk "Do you think I am bullshitting you, do you think I am lying? Fuck You !"
                $ renpy.music.play ("music/sounds/click.mp3", channel=5, loop=False, fadein=0)
                $ renpy.music.play ("music/sounds/errorSound.mp3", channel=6, loop=False, fadein=0)
                $ renpy.music.play ("music/sounds/click.mp3", channel=5, loop=False, fadein=0)
                $ renpy.music.play ("music/sounds/errorSound.mp3", channel=6, loop=False, fadein=0)
                scene  bg bank26_c3ps with hpunch
                "{i}{b}Trigger click"
                scene bg bank27_c3ps with dissolve
                mrk "Huh..?!"
                $ renpy.music.play ("music/sounds/click.mp3", channel=5, loop=False, fadein=0)
                $ renpy.music.play ("music/sounds/errorSound.mp3", channel=6, loop=False, fadein=0)
                "{i}{b}Trigger click"
                scene bg bank27_c3ps with vpunch
                mrk "What the fuck.."
                b "You literally can't shoot me from this gun - my fingerprint is required on a trigger - simple security feature yet quite futuristic, right ?"
                scene bg bank27c1ps with fade
                mrk "No.. That's impossible ?!"
                $ renpy.music.play ("music/sounds/click.mp3", channel=5, loop=False, fadein=0)
                $ renpy.music.play ("music/sounds/errorSound.mp3", channel=6, loop=False, fadein=0)
                "{i}{b}Trigger click"
                scene bg bank27__c3ps with fade
                $ renpy.music.play ("music/sounds/errorSound.mp3", channel=6, loop=True, fadein=0)
                mrk "No-no-no{nw}{w=1.0}"
                $ renpy.music.stop(channel=6, fadeout = 1)
                b "Looks like you've picked the wrong side Markus - they even didn't give you own gun"
                menu:
                    "Attack":
                        b "Get over here !"
                        $ renpy.music.play ("music/sounds/furnitureFalls.mp3", channel=6, loop=False, fadein=0)
                $ renpy.music.play ("music/sounds/kneeKick.mp3", channel=5, loop=False, fadein=0)
                scene bg bank28c3ps with Fade(0.075, 0.15, 0.5, color="#ffffff")
                scene bg bank28_c1ps with cumFlash
                scene bg bank28_c1ps with vpunch
                scene bg bank28_c1ps with vpunch
                mrk "Argh.. Shit.. You broke my leg !"
                $ renpy.music.play ("music/nightmareTheme.mp3", channel=3, loop=True, fadein=3)
                scene bg bank28_c3ps with fade
                $ renpy.pause()
                mrk "..."
                mrk "What are you waiting for [bro].. Just do it already.."
                menu:
                    "Kill":
                        $ ep5killCounter += 1
                        scene bg bank29c3ps with Dissolve(0.5)
                        b "Any last words Markus ?"
                        mrk "If I were you.. I would run from this city without looking back.. otherwise they will find you.. and they will kill you.. I didn't tell them about your [sis].. You're a good man [bro].. "
                        extend "\nNever understood why you joined such business..{nw}{w=1.5}"
                        $ renpy.music.play ("music/sounds/gunSilencer.mp3", channel=5, loop=False, fadein=0)
                        $ renpy.music.play ("music/sounds/bodyFall.mp3", channel=4, loop=False, fadein=0)
                        scene bg bank29_c2ps with killFlash
                        $ renpy.pause()
                        b "{i}I need to get out of here quick, who knows how many of them are coming - if I decide to stay I don't think my chances to make it out of here alive are that high.."
                        menu:
                            "Leave":
                                scene black with Dissolve(2.0)
                                play sound ("music/sounds/footsteps.mp3")
                                $ renpy.pause(0.75)
                                $ renpy.music.stop(channel=3, fadeout = 3)
                                $ renpy.music.play ("music/sounds/openDoor.mp3", channel=4, loop=False, fadein=0)
                    "Spare":
                        b "I won't kill you, but I don't have to save you. Your new friends will decide what to do with you. If you ever stand on my way again I won't be that merciful next time"
                        scene bg bank29c2ps with fade
                        mrk "They will kill me don't you understand ?!"
                        b "You brought it to yourself Markus.. Now it's time to face the consequences.."
                        scene bg bank29c2ps with hpunch
                        mrk "Don't try to redeem yourself - you are a criminal and always will be !"
                        b "At least I know what I'm fighting for.."
                        menu:
                            "Leave":
                                scene black with Dissolve(2.0)
                        play sound ("music/sounds/footsteps.mp3")
                        $ renpy.pause(0.75)
                        $ renpy.music.stop(channel=3, fadeout = 3)
                        $ renpy.music.play ("music/sounds/openDoor.mp3", channel=4, loop=False, fadein=0)
        $ renpy.pause()
        jump ep8streetsGirls
        return

    label ep8streetsGirls:
        $ renpy.notify ("O esnada..")
        $ renpy.pause()
        $ renpy.music.set_volume(0.5, delay=0, channel=1)
        $ renpy.music.set_volume(0.75, delay=0, channel=3)
        $ renpy.music.play ("music/streetAmbient.mp3", channel=1, loop=True, fadein=3)
        $ renpy.music.play ("music/girlsWalkingTheme.mp3", channel=3, loop=True, fadein=3)
        scene bg streets33c1ps with Dissolve(2.5)
        j "... I don't care about my wardrobe Scarlett, I won't be pumping the money out of [bro] - I'm not a freaking gold digger.."
        s "Of course you're not, think of it as a little compensation for his absence all this time. Think of all your birthdays he has missed, I suspect he didn't give you any gifts as well."
        j "Yeah, but [bro] has been helping as much as he could - thanks to him I'm here, he pays for the college and stuff.."
        s "I totally understand you babe - but aren't you tired of being good girl, aren't you feel yourself like a bird in a cage ? I mean don't you want to spread the 'wings' wide before college starts ?"
        j "What do you mean by that ?"
        scene bg streets33_c1ps with fade
        s "When was the last time you hang out and went really wild ?"
        j "I don't know, I'm only hanging out when I'm with you babe"
        s "That's exactly what I'm talking about Julie. Look there is no easy way to say it so let me be honest with you. I'd really like to go with you in one of the local nightclubs, but I'm afraid that you don't have the outfit that is appropriate for such places."
        j "Oh, I see.. Well it's just I'm not that sexy, good looking and confident as you babe - but I'm working on it and looking forward to become someday just like you.."
        scene bg streets34c4ps with fade
        s "Babe, don't say such things, there is nothing wrong with you - I'm just talking about your untapped potential. The only difference between me and you is an outfit. You can't imagine how drastically it boosts your feminine game."
        s "Of course I also happened to fuck with my [father] unlike you but this is different"
        $ renpy.pause()
        scene bg streets33_c2ps with fade
        j "Yeah, a minor difference not worth mentioning, huh"
        s "Believe me Julie, I went through this not so long ago - it's literally a game-changer. You can see for yourself how it affected me, so I can't wait to see how it will change you - then the whole world around you starts to do the same."
        j "Who would have thought that the outfit means so much - I thought what's inside values more.. Whatever, will you help me with this ?"
        s "Gladly babe - I promise we will find some hot outfit for your sexy and curvy body. I personally get a lot of joy by accepting a lot of attention from boys. Can't wait to see the faces of all those poor males at the nightclub - dance floor will be ours, girl!"
        j "Isn't it a bit cruel and vanity babe ? Playing with their feelings, flirting but leaving them no chance to get you - didn't know you are so into it. You are so sexy and hot babe - you literally can tease someone to the.."
        $ renpy.music.stop(channel=3, fadeout = 5)
        nac "Death"
        scene bg streets34_c2ps with dissolve
        j "Huh..?!"
        $ renpy.music.play ("music/luringTheme.mp3", channel=4, loop=True, fadein=2)
        scene bg streets35c4ps with fade
        s "Excuse me ?!"
        nac "I know this is totally random, but I just saw you two over here and I thought you girls were absoulutely stunning"
        scene bg streets35_c4ps with dissolve
        s "Wow thank you, nowadays almost no one meets on the street - that's a 'bold move'.."
        nac "I don't think we've met yet. I'm Nacho"
        s "I'm Scarlett and this is my girlfriend.."
        j "..."
        s ".. Julie"
        scene bg streets35c4ps with dissolve
        nac "What a beautiful name - Julie"
        s "..."
        scene bg streets35c3ps with fade
        $ renpy.pause()
        nac "Tell me something interesting about yourselves girls, besides your looks"
        j "Excuse us, we are in a hurry - it was nice to meet you.."
        s "Come on Julie don't be rude.."
        scene bg streets35_f_c3ps with dissolve
        $ renpy.pause()
        nac "Oh it's okay Scarlett, I'm sure that Julie didn't mean it, she is a good girl just like you. There is one great thing about good girls"
        s "Really ?"
        j ".."
        scene bg streets35_fc3ps with dissolve
        $ renpy.pause(0.75)
        nac "They usually get good opportunities and a lot of privileges if they meet the right people"
        scene bg streets35c3ps with dissolve
        $ renpy.pause(0.75)
        s "I assume you are one of those right people Nacho.."
        scene bg streets35_f_c3ps with dissolve
        nac "Smart and gorgeous - exactly what I like"
        s "You were saying about those opportunities.."
        scene bg streets35c3ps with dissolve
        j "Scarlett shall we go already ? We will be late.."
        scene bg streets36c1ps with fade
        nac "What's the matter Julie ? Don't you want to hear an interesting proposal like Scarlett does ?"
        j "Not really..."
        scene bg streets36c6ps with fade
        s "Babe, nothing bad will happen if we give this handsome gentleman two more minutes of ours precious time"
        nac "I can tell you both are really deep persons, I bet you girls have some pretty big ambitions - at the same time I'm sure you love to hang out and have some fun from time to time"
        scene bg streets36c5ps with fade
        s "Are you reading my mind ?! We were just talking about it.."
        nac "In this city there is no better place to relax and have some good time for the girls like you than my brand new night club which is few blocks from here."
        nac "It's called 'Mint Rhinoceros' - just tell the guard that you are from Nacho and they will let you through freely. As for the other privileges for such a good girls - we will discuss them when you come to visit me at the club"
        play sound ("music/sounds/phoneMessage.mp3")
        "{i}{b}PHONE MESSAGE"
        scene bg streets36_c4ps with fade
        j "Where such generosity comes from ?!"
        nac "..."
        scene bg streets37c5ps with fade
        j "He thinks we are stupid and don't know what it all means ?!"
        s "Julie, what got on you..???"
        nac "Hush, baby girl.. This one is really important.."
        scene bg streets36_c1ps with fade
        j "Scarlett don't you see what he is trying to say ?! His proposal makes me feel like I'm some sort of a thing anyone could buy !"
        scene bg streets36_c1ps with hpunch
        s "Julie ?!"
        j "We are not interested in your good opportunities and unique privileges Mr. Nacho - keep it for those who need it."
        j "I'm not going to stay here any longer Scarlett - let's go"
        nac "I'm afraid I'll have to leave you girls.."
        scene bg streets37c6_ps with fade
        s "Julie where are your manners ?!"
        v "What is going on here ? Is everything ok girls ?"
        j "Huh..?!"
        play sound ("music/sounds/footsteps.mp3")
        scene bg streets38c2ps with fade
        nac "{i}Hey Rocco, that's me. I just got a message from the snitch - that punk came into the bank. I'm only few blocks away but I need to grab my gun - our guy tries to play for time and hold up the bitch as much as possible... 15 minutes..? Right I got you, let's meet there.."
        j "Vicky ?!"
        scene bg streets38_c1ps with fade
        v "..."
        s "Is this Vicky ?"
        j "Vicky !"
        $ renpy.music.stop(channel=4, fadeout = 5)
        $ renpy.music.play ("music/girlsWalkingTheme.mp3", channel=3, loop=True, fadein=5)
        scene bg streets38__c1ps with Dissolve(0.35)
        v "Oh.. Hi Julie.. Sorry, I got distracted by this suspicious guy - didn't want to take my eyes off him until he leaves. Is everything okay ?"
        scene bg streets39_gc5ps with fade
        j "Yeah, now when he left and you came it's definitely much better. By the way Vicky, this is my girlfriend Scarlett I told you about."
        scene bg streets39_g1c5ps with dissolve
        s "Hey Vicky, Julie has been telling me a lot about you, but she didn't warn me that you are so hot looking"
        scene bg streets39_v3c7ps with fade
        v "Thanks Scarlett, it's pleasure to meet you. You and Julie both look fantastic, no wonder you get a lot of attention from men, that guy probably wanted to get to know you"
        scene bg streets39_g2c5ps with fade
        j "Nah not exactly, he wanted to use us for personal gain - I didn't like him from the very beginning"
        s "Oh come on Julie, the guy just wanted to have some fun with us - we are young and good looking girls - I mean is it a crime for a man to want to have sex with us ? At least he came up and showed his intention unlike those bunch of creeps who just silently keep peeping thinking we won't notice they are checking us out"
        scene bg streets39_v2c7ps with fade
        v "I didn't get it - could you please tell what exaclty just happened ?"
        j "Scarlett that guy is a jerk, didn't you notice ?! Also I'd want to know why you didn't just ignore him like I did ? I wanted that conversation to stop as quick as possible but you just didn't listen to me and keep flirting with him.."
        s "Julie I didn't mean to hurt your feelings, I love you babe you know it - I just wanted to get some use of this guy, I wasn't flirting at all. He started talking about those privileges and opportunities so I decided to get us some bonuses such as free enter to the club, is it bad ?"
        scene bg streets39_v3c5ps with fade
        j "It seemed like you totally forgot about me and were absolutely elsewhere - like 100 percent of your attention belonged to him, I felt myself like I'm being ignored"
        s "Babe.. It all just a game: we want to go to the club, I'm pretending that I like him - thus making him believe that his 'generous offer' will work for him - he in turn just wants to fuck us. The most important part of the game is keep pretending and eventually we will get what we want."
        j "I don't know Scarlett.. It all sounds wrong to me"
        scene bg streets39_vc7ps with fade
        v "So the guy just wanted to invite you to the local nightclub ? Is it 'Mint Rhinoceros', right ?"
        s "Yeah, you've been there ? How was it ?"
        scene bg streets39_v3c7ps with dissolve
        v "Well, I've heard few stories about it - some of them were good some not - the point is this club is no different from any other one - it's just the newest one so there is a bit of hype and everyone wants to visit it"
        s "See ? What did I tell you babe - there is nothing wrong with that place. I'd really love to visit it - I've never been there"
        scene bg streets39_v2c7ps with dissolve
        j "I don't know, I'm still not sure - I mean if such a guy owns that place - something tells me better not show up there. Vicky do you think it is safe for us to go there ?"
        scene bg streets39_vc7ps with dissolve
        v "Totally, there a lots of people and you girls probably will have a good time out there. Just let me give you a little advice - it will be better if you not use any of those privileges that guy was talking."
        scene bg streets39_v1c7ps with dissolve
        v "Promise me that you will wait in the line like other visitors - don't ask the guard to let you in. Of course such places are always a bit riskier than staying at home - but you are smart girls, I think I don't have to read you lecture about how to safely rest at the nightclub."
        scene bg streets39_v2c7ps with dissolve
        s "Me waiting in a queue is the most dangerous risk for the others.. I hate it!"
        scene bg streets39_v3c7ps with dissolve
        v "I know exaclty what you mean Scarlett, hate it as well"
        j "I think we will come up with something babe"
        scene bg streets39_vc7ps with dissolve
        v "By the way, where are you heading at girls ?"
        scene bg streets39_g3c5ps with fade
        j "We are going to the lingerie store - the one you showed me not so long ago. Scarlett needs some hot outfit for her show, I probably will pick something for myself as well.."
        s "Why don't three of us go there together, I'm totally in, what about you babe ?"
        scene bg streets39_gc5ps with dissolve
        j "Me too, come on Vicky it will be fun, just like the last time ha-ha"
        v "Gladly girls, but not right now - I'm going to work, there are people waiting for me so.. Yeah.. Maybe next time"
        scene bg streets39c8ps with fade
        j "That's unfrotunate that you have to go.. Well, anyway I hope we will hang out together some other time.."
        v "Sure kiddo, I would like that as well - now it's just not the best time - I have tons of other things to do"
        s "It was nice to meet you Vicky, bye.."
        v "Take care girls"
        j "See you.."
        $ renpy.pause()
        $ renpy.music.stop(channel=1, fadeout = 3)
        $ renpy.music.stop(channel=3, fadeout = 3)
        scene black with Dissolve(3.0)
        jump ep8fitroom
        return

    label ep8fitroom:
        $ renpy.notify ("Bir süre sonra..")
        $ renpy.pause()
        $ renpy.music.set_volume(0.35, delay=0, channel=1)
        $ renpy.music.play ("music/lingerieStoreTheme.mp3", channel=1, loop=True, fadein=2)
        scene bg fr12_c1ps with Dissolve(3.0)
        j "This 'Naughty schoolgirl' outfit is the sexiest I've ever seen, babe. I feel like I'm getting wet.."
        s "It's such a turn on, right ? I mean the moment I started to put on this outfit, my pussy instantly made those panties completely wet.."
        j "Your words make me horny even more.. I would go down on you so bad right now Scarlett.."
        scene bg fr13_c6ps with fade
        s "So what's the matter Julie - let's close the cabin and have some fun, shall we ? Come here.."
        j "Gladly babe, but you know we can't do that - if they see us they won't ever let us inside this store. We need to find the store with less strict policy about such things, or at least the one where crew don't pay attention for 'quickies' inside fitting rooms"
        j "Besides [bro] should come any minute, so I'll resist temptaion of eating you out and will wait till we get to your place.."
        scene bg fr13_c8ps with fade
        s "I'm sure he wouldn't mind join us but if you're so serious about it.."
        j "Scarlett!"
        s "As you wish.. By the way, why didn't you put on anything sexy yet ? Didn't find something you like ?"
        scene bg fr14c2ps with fade
        j "No, I just.. Wanted to see your outfit first and then chose something for myself that will correspond to your look.."
        scene bg fr13c2ps with dissolve
        s "Babe.. I just got an idea - what if I invite you to join me in my little performance ?"
        scene bg fr13_c5ps with fade
        j "What ?! Are you asking me to have sex with you on camera in your online show ?"
        s "Yeah, just imagine.."
        j "No, that's way above my limits. I mean you are broadcasting live right ? I don't want that kind of attention and popularity, I don't want images and videos of my naked body spread wide on the internet. It's your show, it's your channel, those are your fans - you are the star and I'm just the girl who fucks this star"
        scene bg fr13c3ps with fade
        s "My community is very friendly and I need something fresh to be honest, because I'm kind of stuck with creating new content - my regular format is masturbating and playing with dildo but I want to try something new, girl-girl scenes are quite popular now.."
        scene bg fr13_c4ps with fade
        j "No offence babe, it was difficult for me but I accepted your job, you're making the money that's okay. But I worry about my privacy, like what would [bro] or my [mom] say when they see me naked on the web ?! They are okay with my sexual orientation but what you're proposing is way too much, sorry"
        s "Come on Julie, it's 2019 outside so much going on everyday - no one cares about webcam models, whole lot of girls worldwide do this thing - do you think people bother stalking girls they saw on the web ?! I can assure you that on the next day like 99%% of them won't remember your face"
        j "That's the point - I don't care whether they recall my face or not - I don't want it to be in the porn at all"
        scene bg fr13_c7ps with fade
        s "Well we could come up with something.. Like what if we shoot our sex the way so that only my face is seen on camera ?"
        j "Babe.."
        s "I'm not asking you to give me direct answer right now, it's easy and good money - just think about it Julie"
        scene bg fr14c3ps with fade
        b "Hey girls, sorry I'm late - closing the account took a bit more time than it should.."
        $ renpy.pause()
        s "Hey big guy.."
        j "Is everything okay [bro]..?"
        b "Yeah.."
        scene bg fr12c2ps with fade
        s "I suggested Julie to pick a sexy lingerie for herself as well, but it seems she still has some doubts about it.."
        j "Uhm.. What do you think about this outfit [bro]..?"
        b "Well, looks like I haven't been to school for a really long time - there are so many changes to the uniform. Seriously anything looks stunning, I'm impressed. But the one thing I can't agree with is the absence of the skirt - that's disgrace!"
        scene bg fr14c2ps with fade
        j "Right, that's too much even for a 'Nauthy schoolgirl'. Scarlett are you sure there is nothing left from the outfit to wear on ?"
        scene bg fr13c2ps with dissolve
        s "Oh, silly me.. I completely forgot about the skirt - shop assistant told me to pick it at the 'Roleplay' section, the skirt sold separately."
        scene bg fr13c3ps with fade
        b "Looks like financial crisis impacted the lingerie industry as well.. Do you still need me girls ?"
        scene bg fr14c3ps with dissolve
        s "Yeah, give me one minute, let me take that skirt, I just want you to see the whole picture when I put the outfit on"
        scene bg fr15c2ps with fade
        j "I'll go get that skirt, don't bother changing the clothes Scarlett"
        s "Thanks babe, I owe you one"
        $ renpy.pause()
        scene bg fr15c4ps with fade
        j "I'll be right back guys.."
        s "It's red square with black strips"
        j "Got it.."
        scene bg fr15_c4ps with Dissolve(1.0)
        b "Scarlett we need to talk.."
        s "Great idea - that's exactly what I wanted to bring up. You start because my mouth will be busy for some time.."
        $ renpy.music.stop(channel=1, fadeout = 2)
        b "..."
        play sound ("music/sounds/jeansZipper.mp3")
        $ renpy.music.set_volume(0.75, delay=0, channel=3)
        $ renpy.music.play ("music/ScarlettTheme.mp3", channel=3, loop=True, fadein=2)
        scene bg fr16c4ps with fade
        $ renpy.pause()
        s "The one thing I love the most is that your cock is always ready and rock solid for me.. "
        b "Fuck baby, I'm starting to get used to this - you're holding my dick in front of your face knowing that we can be caught any minute - I wonder how far you're willing to go this time."
        s "I'll show you how far and how deep I'm willing to go on you [bro].. But I'm afraid with such a huge cock that you have it will be very difficult for me. I need a lot of practice.."
        scene bg fr16c1ps with fade
        s "I've never held in my mouth that big and thick cock so I will be gagging like a dirty slut.. I will need your help with this - promise that you will hold my head tight while you will be shoving your cock balls-deep down my throat"
        b "Don't worry Scarlett - for the first time I won't be judging you too much - but eventually I'll make a good girl out of you and you will learn how to suck my dick"
        scene bg fr17c1ps with dissolve
        s "That's all I'm asking for [bro].. Make me your personal little cock-sucking slut.."
        b "Enough talking Scarlett, show me what your sweet little mouth capable of"
        scene bg fr16c3ps with fade
        s "Sure [bro] but first you have to promise me that you will cum right into my mouth - I want to swallow it really bad.."
        b "We will see how it goes - firstly you have to make me cum babe, Julie can come any minute.."
        play sound ("music/sounds/squish.mp3")
        scene bg fr16_c3ps with kissFlash
        s "{i}Slurp.."
        b "Yeah, that's more like it.."
        scene bg fr17__c2_ps with fade
        $ renpy.pause()
        s "{i}Gag..slurp..suck.."
        b "Careful Scarlett, don't try to take it all the way first time - wrap your soft lips around the glans, just get used to the size of it."
        scene bg fr17__c2ps with dissolve
        s "{i}slurp..slurp.."
        b "Be a good girl and show me what you've got"
        b "I bet you've sucked a lot of dicks, it's written all over face - you just haven't sucked the one that big"
        scene bg fr17_c2ps with dissolve
        b "Your lustful eyes are telling me you crave to suck"
        $ renpy.pause()
        s "{i}suck..suck.."
        b "Yeah, just like that"
        scene bg fr17__c2ps with dissolve
        s "{i}slurp..slurp.."
        b "Babe, don't hide your face, let me look at those beautiful eyes of yours while you're wrapping your luscious lips around my dick"
        scene bg fr16_c2ps with dissolve
        $ renpy.pause()
        b "Good girl. I know it does turns you on Scarlett - sucking my dick in a public place like a cheap whore"
        scene bg fr16_c2_ps with dissolve
        s "{i}Uhmm..suck.."
        b "Oh fuck baby yes, that's the spot - your tongue is amazing, if I knew how high your blowjob skills are I would put my dick in your mouth much earlier"
        scene bg fr16__c2_ps with Dissolve(0.35)
        scene bg fr16__c2_ps with hpunch
        s "{i}Suck..Slurp.."
        scene bg fr16__c2ps with dissolve
        scene bg fr16__c2ps with hpunch
        b "Ah shit babe, what kind of magic is this ?!"
        play sound ("music/sounds/femaleGiggle.mp3")
        scene fr16__c2ps1 with dissolve
        scene bg fr16__c2ps with dissolve
        scene fr16__c2ps1 with dissolve
        scene bg fr16__c2ps with dissolve
        scene fr16__c2ps1 with dissolve
        scene bg fr16__c2ps with dissolve
        scene fr16__c2ps1 with dissolve
        scene bg fr16__c2ps with dissolve
        s "{i}slurp..suck..slurp.."
        scene fr16__c2ps1 with dissolve
        b "Despite you're only sucking the tip, you know how to give an incredibly good blowjob - I'll give you that"
        scene bg fr16__c2ps with dissolve
        b "Now be a good girl and start touching yourself - I want you to enjoy this as much as I do"
        scene fr16__c2ps1 with dissolve
        s "{i}suck..slurp..suck.."
        scene bg fr16__c2ps with dissolve
        $ renpy.pause(0.5)
        scene fr17_c6ps with fade
        b "Don't forget to uncover this little schoolgirl's shirt for me - I want to see those sexy perky tits of yours"
        s "{i}slurp..suck.."
        $ renpy.pause()
        scene fr18c6ps with dissolve
        b "Give it a firm squeeze - I want to know how bouncy they are"
        play sound ("music/sounds/sighLoud.mp3")
        scene fr18c6ps with vpunch
        $ renpy.pause(0.5)
        b "That's a good girl, so a bit of pain turns you on even more - I like it. Now start playing with your pussy and keep sucking the dick like you mean it Scarlett"
        s "{i}slurp..suck.."
        scene bg fr18_c6ps with dissolve
        b "Young, natural and juicy tits - what can be better ?! Fuck babe, you are amazing, if you keep sucking my dick so eagerly and lustfully I will cum soon enough"
        $ renpy.pause()
        scene bg fr19_c1ps with fade
        scene bg fr19__c1ps with dissolve
        scene bg fr19_c1ps with dissolve
        scene bg fr19__c1ps with dissolve
        scene bg fr19_c1ps with dissolve
        scene bg fr19__c1ps with dissolve
        s "{i}suck..suck.."
        scene bg fr19_c1ps with dissolve
        scene bg fr19__c1ps with dissolve
        scene bg fr19_c1ps with dissolve
        scene bg fr19__c1ps with dissolve
        b "Damn girl, you are so good with your mouth that I can't even imagine how your pussy will feel like, when I'll pin you to the wall and start fucking you from behind like a naughty little bitch"
        s "{i}Uhm..mwah..yes..suck..slurp"
        scene bg fr19_c1ps with Dissolve(0.35)
        scene bg fr19__c1ps with Dissolve(0.35)
        scene bg fr19_c1ps with Dissolve(0.35)
        scene bg fr19__c1ps with Dissolve(0.35)
        scene bg fr19_c1ps with Dissolve(0.35)
        scene bg fr19__c1ps with Dissolve(0.35)
        scene bg fr19_c1ps with Dissolve(0.35)
        scene bg fr19__c1ps with Dissolve(0.35)
        $ renpy.pause(0.25)
        play sound ("music/sounds/squish.mp3")
        scene bg fr19c6ps with kissFlash
        s "{i}Oh..mhh..yeah..suck..suck.."
        $ renpy.pause(0.5)
        scene bg fr19_c1ps with fade
        scene bg fr19__c1ps with Dissolve(0.35)
        scene bg fr19_c1ps with Dissolve(0.35)
        scene bg fr19__c1ps with Dissolve(0.35)
        b "Fuck babe, almost there - keep sucking just like that"
        scene bg fr19_c1ps with Dissolve(0.35)
        scene bg fr19__c1ps with Dissolve(0.35)
        scene bg fr19_c1ps with Dissolve(0.35)
        scene bg fr19__c1ps with Dissolve(0.35)
        scene bg fr19_c1ps with Dissolve(0.35)
        scene bg fr19__c1ps with Dissolve(0.35)
        b "Ah, shit here it comes babe, the big load of a hot, rich sperm special for you"
        scene bg fr19_c1ps with Dissolve(0.25)
        scene bg fr19__c1ps with Dissolve(0.25)
        scene bg fr19_c1ps with Dissolve(0.25)
        scene bg fr19__c1ps with Dissolve(0.25)
        scene bg fr19_c1ps with Dissolve(0.25)
        scene bg fr19__c1ps with Dissolve(0.25)
        scene bg fr19_c1ps with Dissolve(0.25)
        scene bg fr19__c1ps with Dissolve(0.25)
        b "Take it, slut !!!"
        menu:
            "Cum in her mouth":
                scene bg fr20c2ps with cumFlash
        b "Take it deeper Scarlett, I know you like it!"
        scene bg fr20c2ps with hpunch
        s "{i}cough..gag..suck..slurp"
        scene bg fr20c2ps with hpunch
        b "Come on slut, you can do better!"
        scene bg fr20c2ps with hpunch
        s "{i}cough..cough..gag.."
        scene bg fr20c1ps with cumFlash
        scene bg fr20c1ps with cumFlash
        b "AAAAAAAAAAAAAAAAARGHHHHHHHHHHHHH"
        scene bg fr20c1ps with cumFlashLong
        scene bg fr20c1ps with vpunch
        scene bg fr20c1ps with vpunch
        scene bg fr20c1ps with vpunch
        $ renpy.pause()
        b "Fuck Scarlett.. That was so intense - you managed to take every single drop of my cum in your warm little mouth - I'm impressed"
        scene bg fr20_c1ps with Dissolve(1.0)
        play sound ("music/sounds/femaleGiggle.mp3")
        s "Mwaahh.."
        b "That's a good girl"
        $ renpy.pause()
        play sound ("music/sounds/swallowSound.mp3")
        scene bg fr21c1ps with Dissolve(0.75)
        $ renpy.pause(0.5)
        scene bg fr21_c1ps with Dissolve(0.75)
        s "Yummy.. Too bad I didn't start sucking your cock earlier.."
        scene bg fr21c1ps with dissolve
        b "Nobody is perferct Scarlett"
        play sound ("music/sounds/femaleGiggle.mp3")
        s "Well I guess I will have to catch up it by sucking you off on a daily basis, I need a lot of practice anyway.."
        $ renpy.music.stop(channel=3, fadeout = 3)
        b "You are the best babe"
        $ renpy.pause()
        jump supportMe
        return

    label gameOver:
        $ renpy.music.play("music/gameOverTheme.mp3", channel=1, loop=False)
        scene black with Dissolve (2.0)
        show gOver at truecenter with Dissolve (1.0)
        show gOver1 at truecenter with Dissolve (1.0)
        hide gOver with Dissolve (1.0)
        show gOver2 at truecenter with Dissolve (1.0)
        hide gOver1 with Dissolve (1.0)
        show gOver3 at truecenter with Dissolve (1.0)
        hide gOver2 with Dissolve (1.0)
        show gOver2 at truecenter with Dissolve (0.5)
        hide gOver3 with Dissolve (0.75)
        show gOver1 at truecenter with Dissolve (1.0)
        hide gOver2 with Dissolve (1.0)
        show gOver at truecenter with Dissolve (1.0)
        hide gOver1 with Dissolve (1.25)
        with Pause (0.75)
        show gOver1 at truecenter with Dissolve (1.0)
        hide gOver with Dissolve (1.0)
        show gOver2 at truecenter with Dissolve (1.0)
        hide gOver1 with Dissolve (1.0)
        show gOver3 at truecenter with Dissolve (1.0)
        hide gOver2 with Dissolve (1.0)
        show gOver2 at truecenter with Dissolve (0.5)
        hide gOver3 with Dissolve (0.5)
        show gOver1 at truecenter with Dissolve (1.0)
        hide gOver2 with Dissolve (1.0)
        show gOver at truecenter with Dissolve (1.0)
        hide gOver1 with Dissolve (2.25)
        $ renpy.pause()
        $ renpy.music.stop(channel=1, fadeout=1.0)
        return

    label supportMe:
        scene black with Dissolve (2.0)
        $ renpy.pause()
        perv "Episode 8 successfully passed. Congratulations !"
        perv "For additional info and future updates please follow my \n{a=https://www.patreon.com/perv2k16}Patreon Page{/a}"
        perv "Yours sincerely..."
        show pervLogo at truecenter with Dissolve (1.0)
        hide pervLogo with Dissolve (1.0)
        show title at truecenter with Dissolve (2.0)
        hide title with Dissolve (2.0)
        return

    return
