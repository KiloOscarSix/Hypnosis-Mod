
# --------------------------------------      Laura Ending 1      ------------------------------------------------------
label lauraendone:
    scene bg watch
    with fade
    pause
    "She dangled my watch in front of me."
    l "You are getting sleepy..."
    scene bg black
    with fade
    pause
    l "You may now wake up."
    "I opened my eyes."
    scene lauranightie9
    with dissolve
    l "Welcome back."
    n "Success?"
    l "Oh yeah."
    l "That was fun!"
    "She handed me back my watch."
    n "Hey, want to cancel the party and spend the rest of the day fucking?"
    l "You read my mind."
    n "I'll meet you out there."
    scene bg black
    with fade
    "I hid the watch in Laura's room."
    "Next, I called Leah and Jenn and told them not to come before heading to the kitchen."

    scene britkit1
    with fade
    pause
    "There I ran into Brittany."
    scene britkit2
    b "Hey."

if brittany:
    scene britkit3
    with dissolve
    pause
    b "So..."

    b "You didn't tell her about last night, right?"
    scene britkit1
    "I pretended to think about it."
    scene britkit2
    b "Seriously!"
    b "I'm supposed to be the good role model big sister."
    scene britkit1
else:
    jump greatbrit

menu:
    "Blackmail":
        n "How much are you going to pay me to keep it quiet?"
        scene britkit3
        with dissolve
        b "Fuck off!"
        b "You can't blackmail me."
        scene britkit4
        n "I wasn't going to ask for money."
        n "Only sexual favors."
        "She sighed."
        b "That's a definite no."
        scene britkit5
        b "Last night was a one time thing."
        n "Oh okay."
        b "Stop."
        n "What?"
        scene britkit6
        b "Stop acting like you don't believe me."
        n "Okay."
        n "I believe you."
        "I turned away."
        scene britkit5
        b "Where are you going?"
        n "Outside."
        b "Hell no."
        n "Why would I stay here if you aren't giving me any reason to?"
        scene britkit3
        "She sighed."
        n "Bathroom?"
        if bcum:
            "She bit her lip."
            b "Fuck yes."
        else:
            "She rolled her eyes."
            b "Fine."
            b "But not a word!"
        n "Lead the way."
        jump britbangbang3
    "Be reasonable":

        n "Hey Brittany."
        n "Where is your fiance?"
        scene britkit2
        with dissolve
        b "Shut up!"
        b "Don't fucking threaten me!"
        scene britkit1
        n "Whoa there!"
        n "Just asking a friendly question."
        n "And curious if we were alone."
        n "Definitely not a threat."
        scene britkit4
        b "Oh."
        b "Yeah, we're alone."
        n "Interesting."
        b "Why?"
        scene britkit5
        n "I was just wondering if I should prepare to meet you in the bathroom in five minutes."
        b "Wow."
        b "Can you just forget that happened?"
        n "Honestly?"
        scene britkit6
        n "No."
        "She sighed."
        b "Me either."
        n "Alright, well I actually have to use the bathroom."
        scene britkit3
        n "See ya."
        "She walked off as I made my way to the bathroom."
        scene bathroom2
        with fade
        "I did my business, washed my hands and turned to leave."
        scene britbr1
        with fade
        pause
        "Brittany stood there in the doorway."
        n "Hey."
        "She pushed me back before locking the door."
        jump britbangbang3
label britbangbang3:
    b "What are you going to do to me?"

    scene britbr2
    with dissolve
    n "Take off your clothes."
    n "I'm going to bend you over the sink and fuck you like the whore you are."
    "She moaned."
    b "You are all talk."


    image britbath1 = Movie(play="britbath1.webm")
    show britbath1
    window hide
    pause
    b "Oh fuck! I'm still sore from yesterday!"
    b "Not so deep!"
    n "Shhhh."
    image britbath2 = Movie(play="britbath2.webm")
    show britbath2
    window hide
    pause
    b "Yes! Give it to me!"
    b "How do you feel this good?"

    b "Mmmm yeah fuck me! Just like that!"
    b "I'm your whore!"

    image britbath3 = Movie(play="britbath3.webm")
    show britbath3
    window hide
    pause

    if bcum:
        b "Are you going to cum inside me?"
        n "Do you want me to?"
        b "Yes!"
    else:
        b "Do whatever you want to me!"
        b "Just don't cum inside of me!"
        n "Where do you want it?"
        b "Cum in my mouth!"

menu:
    "Cum inside her":
        n "Ohh fuck yes!"
        if bcum:
            b "Ah!"
            with vpunch
            b "Yes yes yes!"
            with vpunch
            b "Pump it inside of me!"
            with vpunch
            b "Fill me up!"
            b "Thank you."
        else:
            b "No!"
            with vpunch
            b "No no no!"
            with vpunch
            b "I fucking hate you!"
        $ bcum = True
        n "You're welcome."
        jump greatbrit2
    "Cum on her":
        n "Get on your knees."
        "I pulled out."
        scene britkneel1
        with fade
        pause
        b "Are you going to-"
        b "Oh my-"
        scene britkneel2
        with vpunch
        pause
        b "Ah!"
        b "Fuck!"
        scene britkneel3
        with vpunch
        pause
        b "It's so much!"
        b "Ha!"
        scene britkneel4
        with vpunch
        with dissolve
        pause
        b "Wow."
        b "Thanks for that, I guess."
        n "Anytime."
        jump greatbrit2

    "Cum in her mouth":
        n "Get on your knees."
        "I backed off before shoving my dick in her mouth."
        scene britkneel5
        with fade
        pause
        with hpunch
        "She choked as I started cumming hard down her throat."
        with vpunch
        "Jizz started dripping out of her mouth as she gagged."
        "I pulled off."
        b "*Cough*"
        scene britkneel6
        with dissolve
        pause

        "She spat out a mouthful."
        with hpunch
        b "*Bleh!*"
        scene britkneel7
        with dissolve
        pause
        b "Fuck, dude!"
        b "That was too much."
        scene britkneel8
        pause
        b "You are going to ruin me."
        n "Going to?"
        n "I believe I already did."
        jump greatbrit2
label greatbrit:
    b "Sooo..."
    n "What's up."
    b "Don't even try it."
    n "What?"
    b "My little sister."
    if grace:
        n "Too late."
    else:
        n "What about her?"
        b "Don't fuck around on her with her best friend anymore."
        n "Oh."
        n "But we aren't-"
        b "She thinks you are."
    "She glared at me."
    b "I'm watching you."
    n "Lucky me."
label greatbrit2:


    scene bg black
    with fade
    if gracerom:
        "We all hung out by the pool for a bit."
        "I convinced Grace to sneak away with me to the store to get supplies."
    else:
        "We all hung out by the pool for a bit."
        jump skipgrace
    scene grace out11
    with fade
    n "Ready?"
    g "What? Where?"
    n "You keep talking about how you need to get laid."
    n "Let's go behind that fence."
    g "Ha! Right."
    "She looked at me."
    g "That's someone's yard!"
    scene grace out10
    with dissolve
    n "So?"
    g "We would definitely get caught."
    n "Only one way to find out."
    "She looked up and down the street."
    g "Damn it."
    scene grace out5
    with fade
    pause
    n "Ass or pussy?"
    g "You got a condom?"
    n "Nope."
    "She sighed."
    g "Ass."
    scene grace out4
    with dissolve

menu:
    "Ass":

        $ gcum = False
        n "As you wish."
        scene grace out7
        g "Hold on!"
        g "Let me get you started."
        jump gracesass2
    "Pussy":
        n "Too bad."
        $ gcum = True

        "She was already wet."
        g "[n]!"
        jump gracespussy2
label gracesass2:
    scene grace out6
    pause
    image gracefence3 = Movie(play="grace fence3.webm")
    show gracefence3
    window hide
    pause
    n "Good girl."
    g "*Mmmph!*"
    n "Alright, I'm ready."
    n "Grace?"
label gracespussy2:
    image gracefence1 = Movie(play="grace fence1.webm")
    show gracefence1
    window hide
    pause
    g "Oh fuck!"
    g "Owww!"
    g "That hurts so good!"
    n "Hurry up! We are going to get caught!"
    g "Oh shit!"
    image gracefence2 = Movie(play="grace fence2.webm")
    show gracefence2
    window hide
    pause
    g "Yesss!"
    g "Fuck me!"
    n "Oh shit, I think they are watching us."
    g "Ahhhh!"
    "I felt her shake as she came."
    g "Yessss!"
    "I launched my load as she tightened."
    scene grace out5
    with fade
    if gcum:
        g "No!"
        g "Damn it, [n]!"
    else:
        g "That was good."
    scene grace out1
    with fade
    pause
    g "Fuck me."
    g "I needed that so bad."
    n "Yeah? You are smiling like a fool."
    g "I will say this."
    scene grace out9
    with dissolve
    g "Dick game strong."
    n "Who, me?"
    g "Yep."
    g "Damn, I need a bathroom."
    scene grace out8
    with dissolve
    n "Round two already?"
    g "Nope."
    g "Your cum is dripping down my leg."

label skipgrace:
    scene poolbooze
    with fade
    "When we returned we had enough food and drinks to last the rest of the weekend."
    "Between moments of hanging out by the pool Laura and I kept disappearing."

    "Eventually we gave up on sneaking off and ended up hooking up in front of everyone."
    image tub3 = Movie(play="tub3.webm")
    show tub3
    window hide
    pause
    pause
    scene bg black
    with fade
    "I stayed the night at Laura's house."
    "We spent the entire night fucking."
    "She imagined that each time my dick was a little bit bigger."
    "Turns out she was right."
    scene lauranightie10
    with fade
    label galleryScene46:
    l "Good morning."
    n "Hey sexy."
    l "You know what?"
    l "This was the first night we got to spend the night together."
    n "Did you like it?"
    l "It was everything."
    "She grabbed my dick."
    scene lcock1
    with fade
    l "Oh! Is this for me?"
    n "All for you, Princess!"
    l "Goodie!"
    scene lcock2
    with dissolve
    "She devoured me, taking me down her throat all the way to the balls."
    "She gasped as she pulled off."
    scene lcock3
    with dissolve
    l "How much longer do you think I can do that for?"
    n "I didn't even know you could!"
    "She smirked."
    l "I've been practicing."
    n "Let me guess. Oversized dildo?"
    "She nodded."
    n "What color?"
    scene lcock4
    with dissolve
    l "Pink of course."
    n "Of course."
    n "And when do your parents come home?"
    l "Monday night."
    l "Want to fuck in every room in the house?"
    n "Of course."
    scene lparentsbed1
    with fade
    pause
    "We fucked in her parent's bed."
    "This time she was sore after."
    scene lparentsbed2
    with dissolve
    pause
    l "Stop! I need a break!"
    "We passed out in the bed, me on the dry side and her in the puddle she seemed to create everywhere she went."
    scene bg black
    with fade
    $renpy.end_replay()
    "I didn't make it home until Monday night."
    scene bg bedroom3
    with fade
    pause
    "My phone had blown up with over a hundred calls, text messages and snaps."
    "But I was too damn tired to answer any of them."
    scene bg black
    with fade
    pause
    label galleryScene47:
    "{b}Tuesday Morning{/b}"
    "Leah woke me up before school and tried to give me a blowjob, but she couldn't fit me into her mouth."

    "She was barely able to slip me inside of her."
    image lmr = Movie(play="lmr.webm") # [Mod] Changed filename (orig: "lmb.webm", nonexistent)
    show lmr
    window hide
    pause
    "But once we got started there was no problem."
    $renpy.end_replay()

    scene bg school
    with fade
    pause

    "When I dropped her off at school she limped away like a bowlegged giraffe."
    scene bg house
    with fade
    pause
    "I called Laura that evening."
    n "I'm too big."
    l "Not for me."
    n "Yeah, well, I want to stop before that."
    l "Okay. I'll get a room at my hotel."
    l "I'll tell my parents I had to cover someone's shift."
    l "Meet you there around nine?"
    n "Deal."
    scene bg hotel
    with fade
    pause
    "I brought the watch and met her at the hotel."
    scene laurahoteltf1
    with fade
    pause
    label galleryScene48:
    n "Hey sexy."
    n "Nice room."
    l "Right?"
    l "Nicer than the last time you stayed here, no?"
    scene laurahoteltf2
    with dissolve
    n "Quite a bit."
    n "So..."
    n "I'm too big."
    l "I know what you mean!"
    scene laurahoteltf3
    with dissolve
    l "My back is starting to hurt."
    l "But I think I'm big enough to let you titty fuck me."
    "I didn't waste time taking off my clothes."
    l "Oh shit."
    scene laurahoteltf4
    with dissolve
    "She licked her lips."
    l "Maybe not."
    "I pushed her back on the bed."
    "She practically drooled as she watched my dick bounce in front of her."
    image laurahotel1 = Movie(play="laurahotel1.webm")
    show laurahotel1
    window hide
    pause
    "I didn't let her take off her top before I started thrusting between her tits."
    l "Oh hey there."
    n "Hey yourself."
    l "This is fun, right?"
    l "Couldn't do this back when you were only ten inches."
    n "Only?"
    l "What can I say?"
    l "I'm a greedy girl."
    l "Are you going to cum on me?"
    n "Hell yes."
    l "Good."
    l "I want you to cover me."
    pause
    l "Do it!"
    l "Cum on my tits!"
    scene laurahoteltf5
    with dissolve
    l "Thanks, [n]!"
    n "Anytime."
    scene bg black
    with fade
    "I followed her into the shower."
    image laurahotel2 = Movie(play="laurahotel2.webm")
    show laurahotel2
    window hide
    pause
    l "YES!"
    l "Pound my pussy!"
    l "Oh fuck that hurts!"
    n "Want to stop?"
    l "No!"
    l "Keep going!"
    l "It hurts so good!"
    "I launched multiple loads into her as she screamed."
    "She seemed to love the pain as I kept stuffing my oversized cock into her stretched out pussy."
    l "Okay!"
    l "I can't take it anymore."
    $renpy.end_replay()
    l "Want to titty fuck me again?"
    scene bg black
    with fade
    "{b}Ten Minutes Later{/b}"
    scene laurahoteltf6
    with fade
    pause
    n "Alright. Time to stop me before I'm too big."
    "She pouted."
    l "Just a bit more?"
    n "Hell no."
    l "Fine."
    "We hypnotized each other and tried to pass out."
    scene bg black
    with fade
    pause
    "I was impressed when she still woke me up in the middle of the night."
    pause
    "{b}Wednesday Morning{/b}"
    scene bg school
    with fade
    pause
    if jenn:
        label galleryScene49:
        "After dropping Laura back off at her school I texted Jenn to meet me in my SUV."
        image jennsuv = Movie(play="jennsuv.webm")
        show jennsuv
        window hide
        pause
        j "AHHHH!"
        "Jenn took the fucking like a sport, but by the time we finished her cheeks were wet from tears."
        "I hoped she would be able to adjust."
        scene bg black
        with fade
        $renpy.end_replay()
        "Next, I fucked Ashley."
    else:
        label galleryScene50:
        "After dropping Laura back off at her school I texted Ashley to meet me in the parking lot."

    image ashsuv = Movie(play="ashsuv.webm")
    show ashsuv
    window hide
    pause
    "I couldn't fit halfway in."
    a "*Gasp gasp*"
    a "Hold on!"
    a "Fuuuuuuuck!"
    n "Are you okay?"
    a "No!"
    "Later she texted that she wasn't able to sit for the rest of the day."
    scene bg black
    with fade
    $renpy.end_replay()
    pause
    label galleryScene51:
    "That night I took Grace out to the movies."
    scene gracemovies1
    with dissolve
    pause
    g "No!"
    n "Shhhh!"
    g "You are way too big for my ass!"
    n "That only leaves other option."
    g "Fine!"
    image gmovies = Movie(play="gmovies.webm")
    show gmovies
    window hide
    pause
    n "Good girl."
    g "I hate you."
    g "I hate you so fucking much."
    g "Ahhh but that dick though!"
    n "Shhh!"
    g "I don't-"
    g "FUUUUCK!"
    "Despite her protests, I came inside her."
    "She, like the others, was too sore for a second round."
    scene bg black
    with fade
    $renpy.end_replay()
    "{b}Thursday Morning{/b}"
    label galleryScene52:
    "I woke up with my dick feeling even bigger."
    scene leahtoobig1
    with fade
    pause
    "I spent twenty minutes trying to cram my dick into Leah."
    "She shook her head, her eyes wet from the pain."
    scene leahtoobig2
    with dissolve
    pause
    L "I can't."
    L "My pussy can't handle it."
    n "Fuck."
    scene bg black
    with fade
    $renpy.end_replay()
    "I called Laura."
    scene bg hotel
    with fade
    pause
    "She got a room for us again."
    "She was able to take three rounds before the pain was too much for her."
    scene laurahoteltf7
    with fade
    pause
    n "Why am I still growing?"
    "She bit her lip."
    l "I don't know."
    scene laurahoteltf8
    with dissolve
    pause
    l "Want to try hypnotizing you again?"
    n "We need to."
    "We repeated the process, and this time it worked."
    scene bg black
    with fade
    "My dick never shrank, but it finally stopped at roughly the length and circumference of my forearm."
    "None of the other girls could take it anymore."
    "Despite this, they all continued to chase me down."
    "I ended up avoiding them."
    scene bg hotel
    with fade
    pause
    "I was never at my house."
    "Even with Laura's discount, staying at a hotel most nights was running up my credit card quick."
    scene bg nicehouse
    with fade
    pause
    "I met Laura's parents."
    "They hated me."
    "Despite this, Laura somehow convinced them to let me stay over at her house most nights."
    scene bg black
    with fade
    "Eventually the addictive power of my cum wore off and the other girls were each able to get over my absence."
    "I didn't keep in contact much, but from what I heard each girl tried to fill the hole in their own way."
    "It seemed that I had turned almost her entire class into sluts."
    "That left Laura stuck with taking all of my hyperactive libido."
    "She seemed to love being stretched out until she couldn't take it anymore on the daily."

    scene bg black
    with fade
    pause
    "{b}Three Months Later{/b}"
    scene bg nicehouse2
    with fade
    pause
    l "Hey."
    n "What's up?"
    scene laurapreg1
    with fade
    pause
    l "Well..."
    l "You were right."
    l "I took the test."
    n "And?"
    scene laurapreg2
    with dissolve
    l "Positive."
    l "I'm pregnant."
    n "Told you."
    scene laurapreg3
    with dissolve
    l "What? It's not like a bigger ass or boobs is really an indicator any more."
    n "Your belly."
    l "Screw you!"
    n "You got a bump, girl!"
    scene laurapreg4
    with dissolve
    n "Congratulations."
    l "Aren't you a little freaked out?"
    n "I'm super freaked out."
    n "And I have to say..."
    scene laurapreg5
    with dissolve
    n "What about the birth control?"
    l "We've been having sex, what, three times a day for three months?"
    l "So that's..."
    n "Almost three hundred times."
    scene laurapreg6
    with dissolve
    l "Right."
    l "You've filled me with gallons of cum."
    l "Birth control could probably only do so much."
    if bcum:
        l "Oh! Guess what else?"
        scene laurapreg5
        with dissolve
        n "Tell me."
        l "I figured out why Brittany's boobs keep getting bigger too."
        n "I told you, I never-"
        l "I know you didn't hypnotize her."
        scene laurapreg7
        with dissolve
        l "She's pregnant too."
        n "Oh!"
        l "I know!"
        l "My parents are so pissed!"
        scene laurapreg8
        with dissolve
        l "I haven't even told them about me yet."
        l "Will you be there when I do?"
        n "Can't wait."
    scene bg black
    with fade

    "Her parents reluctantly accepted me."
    "Her dad gave me a job working for him at a salary far higher I would have received otherwise."
    scene laurahouse
    with fade
    pause
    "They put the down payment on our house, provided we get married."
    "I agreed, although they wanted to wait until Laura's sister's wedding before ours was to commence."

    if bcum:
        scene brittanywedding2
        with fade
        pause
        "I found out Brittany had her wedding dress altered to try to hide her own baby bump."
        "Brittany's fiance was surprised that she had gotten pregnant despite them using a condom every time."
    else:
        scene brittanywedding1
        with fade
        pause
    "The wedding was fun."
    "I got to fuck the maid of honor."
    scene bg black
    with fade
    pause
    "They moved into a house a few doors over from ours."

    if brittany:
        "Brittany asked me to come over to talk."
        with fade
        if bcum:
            scene britpreg1
            with fade
        else:
            scene britnotpreg1
            with fade
        pause
        b "And this is the bedroom."
        n "The carpet makes me think of The Shining."
        b "Right? That's basically the reason I bought the house."
        n "You're a weird chick."
        if bcum:
            scene britpreg2
            with dissolve
        else:
            scene britnotpreg2
            with dissolve
        b "Yep. But not your concern!"
        n "Oh yeah?"
        b "Look, I'm sorry, but I don't want there to be anything weird between us."
        b "We are basically family now."
        if bcum:
            scene britpreg3
            with dissolve
        else:
            scene britnotpreg3
            with dissolve
        n "I agree."
        b "I mean, I really enjoyed what we had-"
        if bcum:
            n "-but I have to ask about-"
            b "-but it's over."
        else:
            b "But it's over."
        b "Let the past stay in the past."

        n "You're right."
        n "There is no way I could fit inside of you anyway."
        b "Whatever."
        b "You fit just fine before."
        n "That was before."

        b "Bullshit."
        n "Laura didn't mention it?"
        b "Nope."
        n "Need me to prove it?"
        b "Mmm hmm. But I'm not going to-"
        "I pulled it out."
        if bcum:
            scene britpreg4
            with dissolve
        else:
            scene britnotpreg4
            with dissolve
        pause
        b "HOLY FUCK!"
        n "Makes it easy to stay loyal, doesn't it?"
        b "Totally."
        b "Except..."
        b "I want it."
        if bcum:
            scene britpreg5
            with dissolve
        else:
            scene britnotpreg5
            with dissolve
        n "Yeah, right."
        b "No, seriously."
        b "I need to try it."
        if bcum:
            scene britpreg4
            with dissolve
        else:
            scene britnotpreg4
            with dissolve
        pause
        b "Right now!"

        menu galleryScene26:
            "[gr]Give in":
                n "Yeah?"
                b "I need that thing inside of me."
                if bcum:
                    scene britpreg7
                    with dissolve
                else:
                    scene britnotpreg7
                    with dissolve
                "She climbed onto the bench at the end of her bed."
                n "Smart girl."
                b "What?"
                n "Don't want to mess up the bed, huh?"
                b "Can you blame me?"
                n "Nope."
                b "Go easy."
                image britdoggie = Movie(play="britdoggie.webm")
                show britdoggie
                with fade
                window hide
                pause
                b "OH!"
                b "Holy fuck!"
                "Laura's family must have extra stretchy vaginas because Brittany was still able to take my dick almost as well as her sister."
                "She felt ridiculously tight."
                "Her pussy was the first one I'd been in for several months that I hadn't wrecked."
                "I came in less than thirty seconds."
                "And it took only a little longer than that to wreck her."
                b "HOLY FUCKING SHIT!"
            "Reject her":
                $ brittany = False
                n "Love to. But you're married now."
                b "I know."
                b "I'm sorry."
                b "Well, put it away at least!"
                scene britnotpreg6
                with dissolve
                n "Ha!"
                "She looked down."
                b "Fuck!"
        $ renpy.end_replay()
    scene laurayoga
    with fade
    pause
    "Laura began teaching yoga classes for pregnant women."
    "She found that she quite enjoyed it."
    if brittany:
        "During classes I would often sneak off to fuck her sister."
    scene bg black
    with fade
    pause
    "Our wedding was a pretty big deal."
    scene laurawedding
    with fade
    pause
    "The day was a blur."
    "Both families felt we were young, but were supportive nonetheless."
    if bcum:
        "Laura's baby bump was even more pronounced than her sister's, but her sister had taken most of the heat."
    else:
        "Laura's baby bump was scandalized a bit."
    "But it didn't slow us down on the wedding night."
    scene bg black
    with fade
    pause
    "The honeymoon was a lot of fun."
    scene laurahm1
    with fade
    pause
    "We stayed at a resort."
    scene laurahm2
    with fade
    pause
    "But we spent most of our time in the room."
    scene laurahm3
    with dissolve
    "We found Laura some prescription pain meds and fucked for a week straight."
    "When we returned she had to take a week off from sex."
    scene bg black
    with fade
    if brittany:
        "I saw a lot of her sister that week."
        with fade
    "{b}A Few Months Later{/b}"
    scene lauralac1
    with fade
    pause
    if bcum:
        "After both girls gave birth, their tits continued to swell with milk."
        "They would take turns watching each other's children, and both babies were fed more than they could eat."
    else:
        "After our daughter was born, Laura's tits continued to swell with milk."
    scene lauralac2
    with dissolve
    pause
    n "Good morning, wife."
    l "Good morning."
    scene lauralac3
    with fade
    pause
    n "How did you sleep?"
    l "Great!"
    n "I think you might be dripping there."
    l "Want a taste?"
    menu:
        "Yes [gr]\[Lactate\]":
            $ lactate = True
            scene lauralac4
            with dissolve
            pause
            "I put her nipple to my mouth and sucked gently."
            scene lauralac5
            with dissolve
            "The sensation of a warm spray of Laura's milk hitting the back of my throat was shockingly forceful."
            "I struggled to keep up with swallowing the flow as I suckled."
            l "Damn, you almost finished that one."
            l "What do you think?"
            scene lauralac6
            with dissolve
            pause
            n "Fucking delicious."
            l "Really? I didn't really like the taste."
            n "You tried it?"
            scene lauralac7
            with dissolve
            l "Well yeah."
            n "Without me watching?"
            "She smirked."
            scene bg black
            with fade
            "I threw her on her back and ravaged her."
            scene lauralac10
            with fade
            pause
            l "Where did that come from?"
            n "Must be the nutrients."
            l "Well then, you'd better drink my right one too."
            l "I don't want to end up lopsided."
            scene bg black
            with fade
            "Drinking her milk became part of our routine."
            scene lauralac9
            with dissolve
            pause

            "In the morning I was awakened by a large, swollen breast in my face with droplets of milk dripping out of her nipples."

            scene lauralac8
            with fade
            pause
            "At night I drank from her as a snack before bed."
            "I began to understand the body builders that would buy breast milk."
            scene lauralac11
            with fade
            pause
            "When I would go to the gym I saw instant results. And my energy was off the charts."
            "Her tits grew even larger to keep up with the extra demand."
            scene lauralac12
            with fade
            pause
            l "Are you going to keep this up after your daughter is weaned?"
            n "Stay tuned."

        "No [red]\[Lactate\]":
            n "I'm good."
            l "Suit yourself."
            $ lactate = False
    scene bg black
    with fade
    if bcum:
        "Brittany's husband didn't want more children, and was pissed off when she became pregnant again shortly after."
    "Laura tested pregnant again not long after and continued running her yoga class for pregnant women."
    if bcum:
        with fade
        "{b}Six Months Later{/b}"
        with fade
        "Brittany's husband became more and more suspicious as the child grew, realizing she looked exactly like Laura's daughter and nothing like his side of the family."
        scene bg office
        with fade
        pause
        "I was working in my office when I heard my name."
        scene lauranews1
        with dissolve
        pause
        l "Hey."
        l "I have bad news."
        n "Tell me."
        scene lauranews2
        with dissolve
        l "It finally happened. He left her."
        l "I told Brittany she could move in with us."
        scene lauranews1
        with dissolve
        l "Is that okay?"
        n "Only if you pose for me."
        scene lauranews3
        with dissolve
        l "Like this?"
        n "I'll deal."
        scene bg black
        with fade

        "{b}A Month Later{/b}"
        scene britcon1
        with fade
        pause
        "I lay in Brittany's bed, her naked body spread out next to me."
        "I was watching the sweat drip down her swollen tits as I debated sucking on them."
        scene britcon2
        with dissolve
        b "I love you."
        n "Mmm. Yeah you do."
        "She stared at me."
        b "I've never told you that."
        n "I'm flattered."
        scene britcon3
        with dissolve
        b "So?"
        menu:
            "I love you too {i}[blue]\[Brittany Ending #1\]":
                n "I love you too."
                "She smiled at me."
                scene britcon2
                with dissolve

                b "Really?"
                n "Of course."
                b "More than Laura?"
                n "Different from Laura."
                scene britcon6
                with dissolve
                b "Every moment I'm with you, I'm happy."
                b "Except when she is there."
                n "Yeah."
                b "I don't see you smile around her."
                scene britcon5
                with dissolve
                b "But you always smile around me."
                n "Maybe you have a better sense of humor."
                b "So you like being around me too?"
                n "I love it."
                scene britcon3
                with dissolve
                b "Run away with me."
                n "What?"
                b "You hate your job, you hate your life, you hate your wife."
                scene britcon4
                with dissolve
                n "I don't hate them."
                b "But you hate her."
                scene britcon3
                with dissolve
                n "No."
                b "I can see it."
                b "And you love me."
                n "I do."
                scene britcon2
                with dissolve
                b "Run away with me."
                b "Pack up your shit in your car and let's just drive."
                n "Your family would disown you."
                b "I know."
                scene britcon5
                with dissolve
                b "Laura always was the baby, the favorite."
                menu:
                    "Run away with Brittany [blue]\[Brittany Ending #1\]":
                        n "You really want to do it?"
                        b "More than anything."
                        n "Let's do it."
                        scene britcon2
                        with dissolve
                        b "Really?"
                        n "Really."
                        "She jumped up."
                        scene bg black
                        with fade
                        b "We have two hours!"
                        b "Grab everything you need!"
                        "We did it."
                        "I wrote Laura a note and kissed my daughter goodbye."
                        "We drove across the country, taking frequent stops to make love."
                        "We stopped at a hotel and stayed there a week as we looked for apartments."
                        "I drove for Uber to pay the bills."
                        "The place we moved into was small, but it was all we needed."
                        "Me, Brittany, and our daughter."
                        centered "You have reached Brittany's first ending!"
                        centered "More to come in future updates."
                        jump end


                    "Talk her out of it":
                        n "Aren't you happy with me, right now?"
                        scene britcon2
                        with dissolve
                        b "Yes."
                        n "Isn't that enough?"
                        "She sighed."
                        scene britcon7
                        with dissolve
                        b "If that's what you want."
                        b "Either way, I want you to know something."
                        b "I'm yours."
                        scene britcon8
                        with dissolve
                        b "You own me."
                        n "Don't worry, girl."
                        n "You will be put to good use!"
            "Brush it off":
                n "You're adorable."
                scene britcon2
                with dissolve
                b "Are you going to say it?"
                n "I do love you. As a sister-"
                scene britcon5
                with dissolve
                b "WHAT!"
                n "-in law."
                b "Oh."
                scene britcon6
                with dissolve
                b "Wait, really?"
                n "You're awesome."
                n "But I'm married."
                scene britcon7
                with dissolve
                n "To your sister."
                b "So it's not love?"
                b "It's just lust?"
                n "I guess."
                scene britcon8
                with dissolve
                b "Well, I'm hurt."
                b "You'd better fuck me again until I pass out."
                n "Deal."
    if brittany:
        scene bg black
        with fade
        pause
        "{b}A Month Later{/b}"
        scene britoops1
        with fade
        pause
        b "Yes! Destroy me!"
        scene britoops3
        with dissolve
        pause
        b "Fuck me in my tight little-"
        scene britoops2
        with dissolve
        with vpunch
        l "WHAT THE FUCK!"
        with vpunch
        l "You have been fucking my SISTER?!"
        with vpunch
        scene britoops4
        with fade
        pause
        "There was no denying it."
        "I was currently inside Brittany to the balls."
        scene britoops5
        with dissolve
        n "...yes."
        "She began to cry."
        scene britoops6
        with dissolve
        l "{i}*High pitched whining*{/i}"
        n "What?"
        b "I know, girl. I'm sorry."
        b "But I'm addicted."
        scene britoops7
        with dissolve
        b "You can understand that."
        l "{i}*More crying sounds*{/i}"
        b "I know, I know."
        n "You can understand her?"
        scene britoops8
        with dissolve
        b "She's my sister."
        n "What did she say?"
        b "She asked how long since we started hooking up."
        n "Oh."
        scene britoops9
        with fade
        pause
        if bcum:
            b "He is my baby daddy."
            l "So..."
            l "{i}*Sniff*{/i}"
            l "Since you moved in?"
            b "Both babies."
            l "It was {i}true{/i}?"
        else:
            n "It's been..."
            n "Same time you and I did."

        scene britoops11
        with dissolve
        l "So..."
        l "You are going to leave me?"
        n "No!"
        n "I love you."
        l "What about her?"
        scene britoops10
        with dissolve
        n "I love her too."
        l "Just go."
        l "Leave."
        scene britoops12
        with dissolve
        l "I can't believe you are fucking my sister!"
        l "I want a divorce."
        if bcum:
            scene britoops13
            with fade
            b "I am so sorry."
            n "Wasn't your fault."
            b "Yes it was."
            n "It was both of us."
        scene bg black
        with fade
        "But Laura was too addicted to my cum."
        "I slept on the couch a lot."
        "Made it a point to avoid Brittany for a while."
        "At least when Laura was there."
        "Eventually Laura made peace with sharing me with her sister, although I never managed to get them to join in together."
    "I tried getting with new girls a few times, finding girls online swearing they could take a huge dick."
    "I never found anyone that really could."
    if brittany:
        "Except for the sisters."
    else:
        "Except for my bride."

    with fade
    if brittany:
        "{b}A Year Later{/b}"
    else:
        "{b}Two Years Later{/b}"
    image lauraspoon1 = Movie(play="lauraspoon1.webm")
    show lauraspoon1
    window hide
    with fade
    pause
    l "Come on!"
    l "We were supposed to leave fifteen minutes ago!"
    n "Not until you orgasm."
    l "You can't rush me! You know this!"
    n "Alright, you asked for it."
    l "Wait-"
    n "Jackhammer time!"
    image lauraspoon2 = Movie(play="lauraspoon2.webm")
    show lauraspoon2
    window hide
    pause
    l "Ohhhhh FUCK!"
    l "Oh my oh my-"
    l "[n]!"
    n "Who makes you cum?"
    l "[p] does!"
    n "Damn right."
    l "Yesss!"
    scene bg black
    with fade
    pause
    "{b}Ten Minutes Later{/b}"
    if brittany:
        if bcum:
            scene lbkitpreg1
            with fade
            pause
            l "Brittany! Let's go!"
            b "I'm ready."
            b "I just need to throw a dress on."
            "Laura groaned."
            l "We're going to be late!"
            b "What? I'm as ready as you are."
            scene lbkitpreg2
            with dissolve
            l "It's [n]'s fault!"
            b "Yeah, yeah. I heard."
            scene lbkitpreg1
            with dissolve
            "Laura stared at her sister."

            l "Wow. Are you serious?"
            b "What?"
            scene lbkitpreg3
            with dissolve
            l "There is cum in your hair!"
            l "How long has that been there?"
            scene lbkitpreg1
            with dissolve
            b "Damn it."
            n "I don't know."
            n "We haven't fucked since lunch."
            l "Wait, tell me you didn't fuck on the kitchen table again."
            scene lbkitpreg2
            with dissolve
            pause
            l "Really?"
        else:
            scene lbkit1
            with fade
            l "Brittany! Let's go!"
            b "I'm ready."
            b "Well, more ready than you are."
            scene lbkit2
            with dissolve
            l "It's [n]'s fault!"
            b "Yeah, yeah. I heard."
            scene lbkit1
            with dissolve
            "Laura stared at her sister."
            l "Wow. Are you serious?"
            b "What?"
            scene lbkit3
            with dissolve
            l "There is cum in your hair!"
            l "How long has that been there?"
            b "Damn it."
            scene lbkit1
            with dissolve
            b "Dammit."
            n "I don't know."
            n "We haven't fucked since lunch."
            l "Wait, tell me you didn't fuck on the kitchen table again."
            pause
            scene lbkit2
            with dissolve
            pause
            l "Really?"
    n "Let's get going."
    scene bg cardusk
    with fade
    pause
    l "I can't believe my parents actually like you, [n]."
    l "If they knew half the things you do to their darling daughter on the daily..."
    n "Yeah?"
    l "They would kill you."
    n "I mean, they have an idea."
    l "Yeah."
    if brittany:
        if bcum:
            n "They can't really believe Brittany keeps getting knocked up by magic, right?"
            l "I don't even want to know what they think."
            b "Three times in three years is pretty suspicious, you have to admit."
            b "But I'm done after this!"
            l "Me too."
            n "So you keep saying."
            l "You can't seriously want more."
            l "We will have our fifth and sixth child in a few months!"
        else:
            b "Well, you keep knocking her up."
            l "I'm done after this one."
            n "So you keep saying."
            b "You can't seriously want more."
            b "You're going to have your third child in a few months."
            l "I'm still not convinced he isn't responsible for yours."
            b "Laura!"
            b "Shhh!"
        scene bg black
        with fade
        pause
        "We arrived at the house."
        scene bg nicehousedark
        with fade
        pause
        n "I'm not saying I want more!"
        n "I'm not the one that keeps getting knocked up."
        if bcum:
            b "Then maybe stop knocking us up!"
        else:
            l "Then maybe stop knocking me up!"
        l "And maybe stop having sex with my sister."
        b "We all know that's not going to happen."
        n "I didn't even want kids to start."
        l "But you love fucking pregnant girls."
        if lactate:
            b "And drinking milk."
            n "Yeah, it does give me energy."
            b "That was never a problem."
        b "How did we get so lucky?"
        n "You girls are the only ones that could handle me."
        "They grinned."
        l "Damn right."
        n "Come on, sister wives!"
        l "Oh shut up."
    else:
        n "They know you aren't a virgin, right?"
        n "You are knocked up for the third time in three years."
        "She rolled her eyes."
        l "How did I get so lucky?"
        n "You were the only one that could handle me."
        "She grinned."
        l "Damn right."
    scene bg black
    with fade
    centered "You have reached Laura's first ending!"
    if finished:
        jump endings
    else:
        "Would you rather head back to the main storyline or the opening menu?"
        menu:
            "Main Story":
                jump backtosmallness
            "Opening Menu":
                return




# -------------------------------------------      Laura Ending 2     ------------------------------------------------

label lauraendtwo:
    n "We could go somewhere cheap."
    n "I'll look up cruises."
    scene bg black
    with fade
    "I did some research and found a week long cruise special."
label cruisending:
    image laurafloat = Movie(play="laurafloat.webm")
    show laurafloat
    with fade
    n "We could go on a seven day cruise."
    l "How much?"
    n "Cheap."
    l "When?"
    n "We could get a last minute cruise that leaves for Mexico tomorrow."
    l "How cheap?"
    n "Both of us for under six hundred."
    l "Seriously?"
    n "I could cover both of us."
    l "You can afford that?"
    n "I'll throw it on a credit card."
    l "That sounds perfect."
    if glthreesome:
        n "Should I invite Grace?"
        l "Why not?"
    else:
        l "Should I invite Grace?"
        n "Why not?"
    l "Can you take off the time from school?"
    n "Yeah, I don't have any tests coming up."
    l "Are we really doing this?"
    n "Hell yeah."
    l "Poor girls."
    l "They are going to have withdrawals."
    n "It's probably better for them in the end."
    n "Get it out of their systems."
    l "Exactly."
    l "Speaking of, do you want to call Grace?"
    n "Sure."
    "I called her."
    g "Hello?"
    n "Congratulations!"
    n "You have won an all access total package dream vacation cruise giveaway!"
    g "Do what now?"
    n "Picture this!"
    n "You."
    n "Me."
    n "Laura."
    n "On a seven day cruise."
    g "When?"
    n "Monday."
    g "Tomorrow?"
    g "I don't have that kind of money."
    n "My treat."
    g "I have school."
    n "Fuck school!"
    n "This is sex, drugs and rock n roll!"
    g "Umm..."
    n "I'm buying us all tickets now."
    n "Get packed."
    g "I'm not going to ditch Daphne."
    n "Bring her!"
    g "No, she goes home tomorrow afternoon."
    l "What is she saying?"
    l "Put it on speaker."
    l "Hey girl."
    l "Daphne will be fine."
    l "We can drop her off at the airport on the way."
    g "What about my dad-"
    l "I don't know, we'll figure out what to tell him tomorrow!"
    l "Be ready for us to pick you up at eight in the morning."
    l "Got it?"
    g "...got it."
    l "That's my girl."

label yeahyeahyeah:
    scene bg black
    with fade

    "{b}Monday Morning{/b}"
    scene bg carmirror2
    with fade
    pause
    "I crammed all the luggage in the back and still managed to fit Grace and Daphne."
    n "Road trip!"
    d "Wooo!"
    d "I'm going to miss you guys."
    d "Will you come visit me?"
    n "As soon as we can afford it!"
    d "Well, start saving now!"
    d "You are all a lot of fun and I'd love it if you came to see me."
    "Laura played an annoying ass playlist on the drive."
    scene bg black
    with fade
    "We stopped for breakfast before dropping Daphne off at the airport."
    "I drove us to the cruise ship and we waited for boarding."
    label glcruise:
    scene dock1
    with fade
    pause
    l "Okay, now I'm kind of excited."
    g "Me too."
    g "I've never been on a cruise before!"
    g "Have you?"
    n "Nope."
    scene dock2
    with dissolve
    g "So it's all you can eat?"
    n "Yep!"
    n "Including room service."
    scene dock3
    with dissolve
    l "That's not going to be good for you."
    g "I know!"
    g "I'm going to grow out of my swimsuit by the end of this!"
    l "I'm just going to drink."
    scene dock4
    with dissolve
    g "So we can drink?"
    l "It's international waters."
    n "It is."
    n "But since we left the US, they still won't let you drink."
    scene dock1
    with dissolve
    g "Are you fucking serious?"
    n "I bought the drinks pass."
    g "Which means?"
    n "I get a maximum of twenty drinks per day."
    g "And you are going to share, right?"
    n "Only what you earn."
    l "Then I'll get all the drinks!"
    pause
    scene dock3
    with dissolve
    g "So you guys are dating now, right?"
    l "Yep."
    g "Then I guess I'm going to be the third wheel?"
    scene dock4
    with dissolve
    l "Poor Grace!"
    if glthreesome:
        l "You didn't think we would bring you if we weren't going to include you, did you?"
        scene dock5
        with dissolve
        g "Oh, this is going to be fun."
        l "Damn right."
    else:
        g "Fuck me."
        "She bit her lip."
        scene dock5
        with dissolve
        g "So, I have to tell you something."
        g "Laura, you know I love you."
        l "Of course."
        g "..."
        scene dock3
        with dissolve
        l "Tell me."
        g "So, you realize that there is no way I can control myself around [n], right?"
        g "I am already having cravings right now."
        "She held up her arm and it was trembling."
        scene dock5
        with dissolve
        g "I haven't had his dick since yesterday."
        l "It's okay. I trust you."
        g "No, you don't seem to understand."
        g "There is no way you can trust me."
        scene dock4
        with dissolve
        l "Yeah, well, I trust [n]."
        g "You aren't listening to me."
        g "I don't want to hurt our friendship."
        g "So I am being completely honest with you."
        scene dock3
        with dissolve
        g "In my mind, I'm fully aware that you guys are together now."
        g "And I support that."
        if jennmean:
            g "But my body still fully thinks of [n] as my boyfriend."
        else:
            g "But my body still fully thinks of [n] as my mortal enemy."
        g "And my body needs to fuck him so fucking bad."
        scene dock2
        with dissolve
        g "It's going to happen."
        "Laura looked nervous."
        g "On our friendship."
        g "I thought I could do this."
        scene dock3
        with dissolve
        g "But I can't."
        g "And if you can't deal with it, I shouldn't come."
        l "Grace, we aren't going to leave you here."
        g "I could take the bus."
        scene dock5
        with dissolve
        l "I am not making you take the bus."
        l "It would probably take you all day to get home, if you even made it."
        g "Then, you are okay with me fucking your boyfriend?"
        scene dock6
        with dissolve
        l "No."
        l "But we'll figure something out."

    scene bg black
    with fade
    pause
    "{b}An Hour Later{/b}"
    with fade
    n "Ladies, welcome to our room."
    scene cruiseroom3
    with fade
    l "Huh."
    n "It's nothing fancy, but I figure we won't spend much time in here anyway."
    l "What makes you think that?"
    l "I'm going to be needing a good dickin' on the regular."
    n "Of course, my dear."
    n "But why would we contain that to our room?"
    g "Ha!"
    g "So we are all sharing a room, huh?"
    g "What is the sleeping situation?"
    scene cruiseroom1
    with dissolve
    n "Two beds."
    n "Isn't it obvious?"
    if glthreesome:
        n "One is the sleep bed, one is the sex bed."
        l "The one by the window should be the sex bed."
        g "Speaking of, you aren't going anywhere near my pussy, [n]."
        g "I am not about to let you knock me up."
    else:
        g "One is the sleep bed, one is the sex bed?"
        l "Ha ha."
        g "Can I have the one by the window?"
        l "It's all yours."
    if glthreesome:
        n "You think I came unprepared?"
        n "Please."
        g "What?"
        "I unzipped my bag and tossed her a thirty-six pack of condoms."
        g "Yes!"
        g "My hero!"
        "She kissed me."
        l "Back off, bitch!"
        l "That there is my man!"
        g "Well you weren't kissing him."
    l "No offense, [n], but couldn't we have found a better room?"
    n "It was last minute."
    n "Plus, this is two above the base level!"
    scene cruiseroom2
    with dissolve
    n "We even have a window."
    g "Works for me."
    g "By the way, I'm freaking out."
    g "What am I going to tell my dad?"
    g "Normally he picks me up from school in an hour."
    l "Tell him I'm feeling super depressed."
    l "You are going to stay a few nights at my house to cheer me up."
    l "It's going to take a while."
    l "Maybe all week?"
    g "That is..."
    g "You are an evil genius!"
    l "I have my moments."
    n "Alright, let's go explore the ship!"
    scene bg black
    with fade
    pause
    "{b}Monday Evening{/b}"
    scene cruisetub1
    with fade
    pause
    n "How you ladies doing?"
    l "Well, I'm tipsy in a hot tub."
    l "Kind of miss my own hot tub though..."
    g "Come on, Laura-"
    l "...because then I could be riding [n]'s dick right now."
    g "Oh. Good point."
    g "But you still could."
    l "I'm not that kind of girl."
    scene bg black
    with fade
    pause
    "{b}Monday Night{/b}"
    scene csit1
    with fade
    pause
    n "Who needs another drink?"
    g "One more and I'm falling off this couch onto the floor."
    n "Laura?"
    l "I'm good."
    scene csit2
    with dissolve
    n "Good. Do you see my point from earlier?"
    n "We haven't even gone back to the room yet."
    l "I guess."
    scene csit3
    with dissolve
    g "[n], it's fine."
    g "We are having a lot of fun."
    g "And the food is good!"
    g "This is going to be an awesome trip."
    scene csit4
    with dissolve
    g "Right, Laura?"
    l "For sure."
    l "I'm not complaining."
    l "But I wouldn't mind another pina colada."

    scene bg black
    with fade
    pause
    "{b}Tuesday Morning{/b}"
    with fade
    g "Aww fuck!"
    n "Shhh."
    n "Sleep time."
    g "My tits grew!"
    scene gcruise4
    with fade
    pause
    l "This is something that sucks about Grace."
    l "She is super loud and annoying in the morning."
    g "I can barely fit in my bra!"
    l "What do you expect?"
    scene gcruise1
    with dissolve
    l "You ate an entire pizza."
    g "Oh yeah."
    n "And that was after the big ass buffet we had for dinner."
    g "Whatever!"
    scene gcruise2
    with dissolve
    g "You had more than I did."
    if glthreesome:
        l "He has to keep up his energy to be able to satisfy the two of us."
    else:
        l "He has to keep up his energy to be able to satisfy me."
    "Grace smirked."
    n "Plus, I didn't eat a pizza."
    scene gcruise3
    with dissolve
    g "Whatever."
    g "This bed sucks."
    g "And I'm fucking starving."
    g "Who wants room service?"
    scene gcruise5
    with dissolve
    l "Shhhh!"
    l "Head hurtie."
    g "Are you really hungover?"
    g "You had like two drinks."
    "Laura sat up."
    scene gcruise6
    with dissolve
    l "Three!"
    g "But that was spread out over eight hours."
    n "It's the sugar that gets you."
    n "You know what the best hangover cure is?"
    scene gcruise7
    with dissolve
    l "Hmm?"
    n "Mimosas."
    n "Grace, grab the bottle of champagne I put in your bag and put it in the fridge."
    n "And order us some OJ with your room service."
    g "I will in a minute."
    scene gcruise8
    with dissolve
    l "Ah!"
    n "What?"
    l "These beds really do suck."
    g "Right?"

    l "No offense, [n]."
    scene gcruise11
    with fade
    pause
    l "My hotel chain owns this cruise line."

    l "I'm going to go to the front desk and see if I can upgrade the room with my employee status."
    n "Good luck."
    scene gcruise10
    with dissolve
    "She hesitated as her cheeks puffed out and she looked green."
    label galleryScene53:
    l "But first... I think I'm gonna throw up."
    scene gcruise12
    with fade

    "She ran into the bathroom."
    scene gcruise9
    with fade
    pause
    "As soon as she closed the door, Grace climbed into my bed."

    "Without a word she slid on top of me."
    if glthreesome:
        "She must not have been as sneaky as she thought, because Laura yelled at her from the bathroom."
        l "You'd better not be trying to fuck my boyfriend when I'm not there!"
        g "I wouldn't dream of it!"
        g "{i}But I would definitely do it.{/i}"
    scene gcruise13
    with fade
    pause
    menu:
        "[gr]Allow it":
            $ gcum = True
            jump sneakygrace

        "Tell her to wait":
            $ gcum = False
            n "{i}Hold the fuck on!{/i}"
            "Grace stopped right as I could feel how slick she was."
            scene gcruise14
            with dissolve
            g "{i}What? I'll be really fast.{/i}"
            n "{i}No!{/i}"
            n "{i}She could come right back!{/i}"
            "She leaned forward to whisper even softer."
            scene gcruise13
            with dissolve
            g "{i}But I'm really fucking wet right now.{/i}"
            n "{i}I'm aware.{/i}"
            g "{i}Do you know how close you are to penetrating me right now?{/i}"
            "I pushed her off."
            n "{i}Let's wait until we have a better moment.{/i}"
            jump goodgrace

        "Stop her":
            $ gcum = False
            n "{i}Come on, Grace.{/i}"
            n "{i}Laura trusts us.{/i}"
            n "{i}Let's not do shit behind her back.{/i}"
            scene gcruise14
            with dissolve
            "Grace rolled her eyes."
            g "{i}Really?{/i}"
            g "{i}Kind of expected you to jump me right now.{/i}"
            "She sighed."
            g "{i}Fine.{/i}"
            jump goodgrace


    label sneakygrace:
    g "{i}You're already hard!{/i}"
    n "{i}Grace-{/i}"
    g "{i}Shhh.{/i}"
    g "{i}I need this.{/i}"
    scene gcruise14
    with dissolve
    "She bottomed herself out on my dick."
    image gride1 = Movie(play="gride1.webm")
    show gride1
    window hide
    pause
    g "{i}Don't hold back!{/i}"
    n "{i}We can't-{/i}"

    if glthreesome:
        g "{i}She'll forgive me.{/i}"
        n "{i}Didn't you get enough last night?{/i}"
        g "{i}Never.{/i}"
    else:
        g "{i}I warned her!{/i}"
    "I heard Laura still throwing up."
    pause
    "Thirty seconds later I came inside of Grace."
    "Hard."
    g "{i}Yesssss!{/i}"
    n "{i}But you aren't even on-{/i}"
label goodgrace:
    scene bg black
    with fade
    "She climbed off me and ran back over to her bed."
    scene gcruise12
    with fade
    pause
    g "HEY GIRL! How you doin in there?"
    l "Fine."
    g "Need me to hold your hair back?"
    l "I'm good."
    "We heard the toilet flush and she walked out."
    scene gcruise11
    with fade
    l "Alright."
    l "I'm going to get dressed and go visit customer services."
    g "Have fun!"
    scene gcruise10
    with dissolve
    l "How long before room service gets here?"
    g "Should be right about twenty minutes."
    l "Perfect."
    scene gcruise12
    with fade
    "She got dressed."

    "As soon as she closed the door Grace slid back into my bed."
    scene gcruise13
    with fade
    g "Think you can make me cum in twenty minutes?"
    n "You think she will really take that long?"
    g "She is going to get lost at least three times."
    if gcum:
        g "And I want you to fuck me in my ass."
        n "Oh yeah?"
        scene gcruise14
        with fade
        g "One day I want to blow you, too."
        g "Then I could have you creampie all three holes."
        n "Damn, girl."
    else:
        g "You have plenty of time to fuck me in the ass."

    menu:
        "[gr]Fuck her":
            n "Alright, I'll be your horse, cowgirl."
            n "Ride me."
            n "But first, why are you still wearing that bra?"
            "She smirked."
            scene gcruise15
            with dissolve
            g "Yeehaw!"
            if gcum:
                "She slid a finger into her pussy, scooped out some cum and pushed it into her ass for lubrication."
                g "I can't wait to be loud."
                g "Although, having to be quiet is pretty hot."

            else:
                "I slid inside her pussy as she bottomed herself out on top of me."
                g "Oh!"
                n "That's not your ass."
                g "I'm just getting your dick lubricated, genius."
                g "Calm down."
            "She moved her ass on top of my dick and sat down."
            image gride2 = Movie(play="gride2.webm")
            show gride2
            window hide
            pause
            g "Oooof!"
            g "That's the shit."
            g "OH FUCK!"
            n "Shhhh!"
            g "What? She's gone!"
            g "FUCK LAURA!"
            n "But she could be back any moment!"
            g "I know!"
            g "That's what makes it so hot."



        "Turn her down.":
            n "That's going to be a no from me, dawg."
            g "What?"
            g "Come the fuck on!"
            "She groaned before laying down next to me."
            scene gcruise16
            with fade
            pause
            g "Well, I'm not going to force you. I'm not Laura."
            n "What do you mean?"
            g "Nothing."
            g "But just so you know, there is a hot naked girl laying next to you."
            g "And you are letting her simply lay there."
            n "Yep."
            g "You know you are letting down mankind right now?"
            g "Forget mankind. You are letting your future self down."
            g "In twenty years you are going to wish you could come right back to this moment right now."
            n "You are probably right."

    scene bg black
    with fade
    $renpy.end_replay()
    "She was still naked in bed next to me when we heard the key in the door."
    scene gcruise16
    with fade
    pause
    g "Shit!"
    scene bg black
    with fade
    "She jumped up and rolled up into the covers of her bed just in time."
    scene gcruise18
    with fade
    pause
    g "How'd it go?"
    l "We got an upgrade."
    n "Seriously?"
    l "You doubted my skills and influence?"
    scene gcruise17
    with dissolve
    n "The room isn't even in your name."
    n "I don't think they can technically do that without me there to authorize."
    l "Yeah, well."
    l "Have you seen these tits?"
    scene gcruise18
    with dissolve
    n "I have."
    l "There you go."
    l "Wait, Grace!"
    l "Why are you naked?"
    if glthreesome:
        l "You promised not to try to hook up with [n] without me."
    scene gcruise19
    with dissolve
    g "I always sleep naked."
    l "You at least had a bra on when I left the room."
    g "I was going to tease the room service guy."
    "Laura rolled her eyes."
    scene gcruise20
    with dissolve
    l "Grace, don't be such a slut."
    l "You know [n] is a horny bastard, right?"
    l "And you are teasing the poor guy with those funbags of yours."
    n "Yeah, Grace."
    scene gcruise17
    with dissolve
    n "Where will I ever find relief for my poor blue balls?"
    g "I don't know. Oh!"
    g "How about that cum dumpster standing above me?"
    l "Let's get going."
    scene gcruise18
    with dissolve
    g "What about room service?"
    l "No, we can't trust you around the attendant anyway."
    g "Laura! You know I need to get mine, right?"
    l "Now who's the cum addict?"
    scene bg black
    with fade
    pause
    "I gave the room attendant a tip to carry all our luggage to the next room."

    l "This is it."
    scene niceroom1
    with fade
    pause
    g "Holy shit!"
    g "This is more than an upgrade!"
    g "Look at all this space!"
    n "Not too shabby."

    l "What do I get?"
    n "Some sugar."
    "I kissed her cheek."
    l "Good boy."
    scene croom1
    with fade
    pause
    g "Wait, just the one bed?"
    l "It's a king."
    g "Big enough for the two of us?"
    l "Yeah, [n] can sleep on the floor!"
    "They giggled."
    scene croom2
    with dissolve
    n "It's cool."
    n "More drinks for me."
    l "Spoil sport."
    l "Well, should we break this bed in?"
    scene croom1
    with dissolve
    n "Umm..."
    l "Actually, I'm starving."
    g "Thank God."
    g "I'm glad I didn't have to say it."

    scene bg black
    with fade
    "{b}Tuesday Afternoon{/b}"
    scene lawnchairs1
    with fade
    pause
    l "Ahhh."
    g "I think we found our spot."
    n "Here?"
    n "We can come back."
    scene lawnchairs2
    with dissolve
    n "Let's go explore the ship!"
    l "You could go explore the closest bar and bring me back another drink."
    g "Hey, [n]?"
    g "While you're out grabbing drinks, will you bring me back a margarita?"
    scene bg black
    with fade
    "{b}Tuesday Night{/b}"
    scene cview1
    with fade
    pause
    n "Last drinks, ladies."
    g "Really?"
    n "I reached my limit for the day."
    l "That sucks!"
    scene cview2
    with dissolve
    l "So we have to buy drinks now?"
    n "Not necessarily."
    n "We could always head back to the room."
    g "Shouldn't we save some of the champagne for later?"
    scene cview4
    with dissolve
    n "I might have packed something else."
    if glthreesome:
        g "Hey, want to fuck me over the railing?"
    else:
        g "Hey, want to fuck Laura over the railing?"
    l "Grace!"
    scene cview3
    with dissolve
    g "What?"
    g "Never had sex in public?"
    l "Not that public!"
    scene cview4
    with dissolve
    g "Time to teach you new things."
    l "Drinks first."
    scene bg black
    with fade
    pause
    "We headed back for the room."
    g "Whew!"
    scene niceroom1
    with fade
    pause
    g "This room reeks of sex!"

    if glthreesome:
        n "I wonder why?"
        g "We only had sex in the shower though!"
        l "And the bed."
        g "Oh yeah."
    else:
        l "I wonder why?"
        g "I thought you only had sex in the shower though?"
        l "And the bed."
        l "That was like two hours ago."
        g "Oh yeah."
    g "I was pretty drunk."
    "I reached deep into my bag and pulled out a bag filled with a clear liquid."
    scene croom1
    with fade
    pause
    l "What is it?"
    n "Rum!"
    n "Now you can order all the free sodas and virgin daiquiris you want."
    l "Yesss!"
    scene croom2
    with dissolve
    g "What's next?"

    l "Let's go dancing."
    g "Too full."
    l "Too full to dance?"
    scene croom1
    with dissolve
    if glthreesome:
        l "What do you want to do, let [n] split you in half again?"
        g "Too full."
    else:
        g "Definitely."
        l "Hey Grace? I'm proud of you."
        g "Why?"
        l "You've been strong holding out without getting dick."
        scene croom2
        with dissolve
        g "Well, it's not fucking easy."
        l "Still having withdrawals?"
        g "Like you wouldn't believe."
        l "I don't see you shaking."
        label galleryScene54:
        scene croom1
        with dissolve
        g "Yeah, but I'm starting to have shivers."
        l "Really?"
        l "I have an idea."
        l "I'll find you some sperm."
        scene bg black
        with fade
        pause
        g "What?"
        image lcruise1 = Movie(play="lcruise1.webm")
        show lcruise1
        with fade
        window hide
        pause
        "Grace didn't even pretend to hide it as she fingered herself watching me fuck her friend."
        l "Ohhhh!"
        l "Drunk sex is the best sex!"
        g "Fuck yeah."
        g "Give her that dick, [n]."
        g "She fuckin loves it."
        g "Because she's a dirty, dirty whore."
        l "Grace!"
        g "Beg him, bitch!"
        l "No!"
        g "Tell him you need his cock."
        l "Uhh!"
        l "Fine!"
        l "I need your cock, [p]!"
        "Grace giggled."
        pause
        scene bg black
        with fade

        "After I filled up the condom, Laura grabbed it and took it off."
        l "Here, Grace. Give me your drink."
        "Grace handed it to her."
        "Laura filled it up with the contents of the condom and handed it back."
        scene drinkcruise1
        with fade
        pause
        g "Seriously?"
        l "Try it."
        scene drinkcruise2
        with dissolve
        "Grace sipped on her pina colada."
        g "Holy shit!"
        g "That's delicious!"
        "She chugged the rest of it."
        $renpy.end_replay()
        scene drinkcruise3
        with dissolve
        g "Brain freeze."
        l "Feel better?"
        g "I'll let you know in a minute."
        l "So what now?"
    n "There's always the hot tub."
    scene bg black
    with fade

    "{b}That Night{/b}"
    scene cruisenight
    with fade
    pause
    "{i}Huh.{/i}"
    "{i}Do they usually sleep like that?{/i}"
    "{i}I can't tell which one is snoring louder.{/i}"
    scene bg black
    with fade

    label galleryScene55:
    if _in_replay:
        menu:
            "Yes":
                $ glthreesome = True
            "No":
                $ glthreesome = False
            "\[Mod\] Do you want to see the threesome version of this scene ?"
    "{b}Wednesday Morning{/b}"
    g "Ah! My tits!"
    l "Shhhhh!"
    "Grace sat up and began to play with her tits."
    scene gtits1
    with fade
    pause
    g "What size do you think they are now?"
    l "I have no idea."
    l "Maybe G cup?"
    "A moment passed."
    scene gtits2
    with dissolve
    l "Damn it, Grace!"
    g "What?"
    g "I'm being quiet."
    l "You made [n] hard from watching you play with your tits."
    scene gtits3
    with dissolve

    g "So?"
    l "So, he's still inside me."
    scene gtits4
    with dissolve
    g "So let him fuck you."
    l "I can't."
    l "Too nauseous."
    scene bg black
    with fade
    "She stood up."
    l "Be right back."
    scene gtits4
    with fade
    pause
    "Grace smirked."
    scene gtits5
    with dissolve
    pause
    "Before I could react she lay down next to me."
    scene gtits6
    with fade
    g "{i}Hey there lover boy.{/i}"
    image gtan1 = Movie(play="gtan1.webm")
    show gtan1

    window hide
    pause
    g "{i}Imagine meeting you here.{/i}"
    pause
    g "{i}Do you like what you see?{/i}"
    menu:
        "[gr]Fuck Grace":
            if glthreesome:
                "I slid over to Grace and plunged deep inside her in one stroke."
                image gtan2 = Movie(play="gtan2.webm")
                show gtan2
                with fade
                window hide
                pause
                g "OHHHH!"
                g "Fuck yes!"
                l "Hey!"
                l "That was my hard on!"
                g "I don't see you using it, bitch!"
                l "Screw you!"
                pause
                "Less than a minute later I filled her full of cum."
                g "[n]!"
                n "I know, I know."
                n "But it looked like you could use it."
                g "It feels fucking amazing."
                g "I didn't say stop!"
                "She kissed me."
                g "Are you trying to knock me up?"
                g "We probably need to have a conversation about this soon."

            else:

                "I moved as quietly as I could and plunged deep inside the girl in one stroke."
                image gtan2 = Movie(play="gtan2.webm")
                show gtan2
                with fade
                window hide
                pause
                g "Ohhhhh!"
                n "Shhhh!"
                "I began pumping her at full speed."
                g "{i}You like this whole secret affair thing, don't you?{/i}"
                g "{i}You don't have to answer.{/i}"
                g "{i}Your hard dick already told me.{/i}"
                pause
                "Less than a minute later I filled her full of cum."
                g "{i}Did you just cum inside me?{/i}"
                g "{i}Wait! Keep going.{/i}"
                g "{i}I'm almost there!{/i}"
                if preg:
                    g "{i}But why do you keep cumming inside of me?{/i}"
                    g "{i}Are you trying to knock me up?{/i}"
                    n "{i}What if I am?{/i}"
                    g "{i}That's probably something we need to talk about!{/i}"


        "Turn her down":
            n "Sorry, babe."
            g "Suit yourself."
            scene gtits8
            with dissolve
            "She pulled up her nipple to her mouth and began sucking on it."
            if glthreesome:
                n "Fine!"
                image gtan2 = Movie(play="gtan2.webm")
                show gtan2
                with fade
                window hide
                pause
                "I slid over to Grace and plunged deep inside her in one stroke."
                g "Ohhhh!"
                g "Fuck yes!"
                l "Hey!"
                l "That was my hard on!"
                g "I don't see you using it, bitch!"
                l "Screw you!"
                pause
                "Less than a minute later I filled her full of cum."
                g "[n]!"
                n "I know, I know."
                n "But it looked like you could use it."
                g "It feels fucking amazing."
            else:
                "She smirked at me as she caught me watching and realized I had begun jerking off."
                g "{i}Do you have something for me?{/i}"
                pause
                g "{i}You're about to cum, aren't you?{/i}"
                g "{i}Aim it at me!{/i}"
                g "{i}I want it!{/i}"
                n "{i}Open your mouth!{/i}"
                "I began spraying in her direction, getting half of it on her face."
                scene gtits7
                with fade

                "It took another minute for her to finish cleaning herself off."
    scene bg black
    with fade
    "Laura returned."
    scene gtits3
    with fade
    pause
    l "Are you still playing with your tits?"
    g "They are so big!"
    l "You have tan lines now."
    scene gtits5
    with dissolve
    g "I know!"
    g "Hey, do you guys want to get off the ship today?"
    l "Please."
    scene bg black
    with fade
    $renpy.end_replay()
    "{b}Five Hours Later{/b}"
    "We got off the boat and wandered around for a bit before sneaking onto a resort and acting like we owned the place."
    scene mexico4
    with fade
    pause
    l "This country is not so bad."
    g "Don't be disparaging my birth place!"
    l "Wait! You were born in Mexico?"
    g "No."
    scene mexico1
    with dissolve
    n "You really don't know your best friend is Columbian?"
    l "No, I knew that."
    g "Sure."
    l "Either way, it's nice to get off the boat."
    scene mexico4
    with dissolve
    l "Should we do some shopping?"
    l "You could get a few tops that actually fit you."
    g "Yeah, that's a good idea, actually."
    g "I'm seriously running out."
    scene mexico1
    with dissolve
    g "You could use some new ones too."
    l "Think so?"
    g "I'm not the only one blowing up, girl."
    scene mexico2
    with dissolve
    l "Is it that noticeable?"
    l "Damn it!"
    l "I was hoping I was imagining it."
    scene mexico1
    with dissolve
    l "But I'm not eating half of what you are."
    g "Hey!"
    g "Alright, it's true."
    scene mexico2
    with dissolve
    n "It's the drinks."
    l "What?"
    n "Every pina colada is around six hundred calories."
    l "What?"
    scene mexico3
    with dissolve
    n "You had what, six yesterday?"
    n "That's double your daily calories right there."
    l "What."
    n "Then you add-"
    scene mexico4
    with dissolve
    l "Okay, okay!"
    l "I get it!"
    l "It's all going to my tits."
    g "I would say mostly your ass."
    scene mexico1
    with dissolve
    l "Are you serious?"
    l "That's it, let's get up and walk on the beach."
    l "I need to walk off this fat ass."
    scene bg black
    with fade
    "We got up and began walking."
    scene mexico5
    with fade
    pause
    g "Yeah, you are getting thick, girl."
    g "You make me wish [n] made my ass bigger too."
    g "I'm getting super top heavy."
    l "Yeah, I heard a guy call you tits on a stick earlier."
    scene mexico6
    with dissolve
    g "Seriously?"
    g "We need to find that stupid fucking watch."
    l "I know."
    label galleryScene56:
    scene mexico7
    with dissolve
    if glthreesome:
        l "Hey, ever have sex in Mexico?"
        g "Nope."
        l "Me either!"
        l "Let's find a spot."
    else:
        g "Hey, ever have sex in Mexico?"
        l "No."
        l "But that's a really good idea."
        l "You bring a condom?"
        n "I brought three."
        l "Perfect."
        "Grace licked her lips."
    scene mexico6
    with dissolve
    n "Ever have sex in the ocean?"
    "I led the way into the water."
    image lbeach = Movie(play="lbeach.webm")
    show lbeach
    with fade
    pause
    l "This feels so dirty!"
    g "How's that salt water feel in your pussy?"
    g "Not a great lubricant, is it?"
    n "No problems over here."
    l "Why are you here?"
    g "Waiting for mine."
    g "Plus, you like to be watched."
    l "No I don't!"
    g "There are fifty people on the beach over there that can see you."
    g "You get off on watching them let [n] pound you in the water."
    l "They can't- uh!"
    l "They can't tell what we are doing!"
    if glthreesome:
        g "Sure."
        g "But I still call next!"
        pause
        "Laura moaned."
        l "I'm cumming!"
        g "Why do you always have to announce it?"
        l "Shut up."
        g "Hey, [n]. If you want this, chase me!"
        "She dove into the water."
        scene bg black
        with fade
        pause
        "After I finished, I dove in after her."
        scene swim
        with fade
        pause
        "Under the water I found her chasing fish."
        scene swim2
        with dissolve
        pause
        "When she saw me she smiled at me before swimming away."
    else:
        g "Sure."
        pause
        g "Come on!"

        "Laura moaned."
        l "I'm cumming!"
        g "Why do you always have to announce it?"
        l "Shut up."
        l "Cum inside me, [n]!"
        scene bg black
        with fade
        pause
        "I handed the condom to Grace."
        "She poured the contents into her mouth hungrily."
        g "Hey! Fish!"
        "Before Laura and I could react she dove into the water."
        scene swim
        with fade
        pause
        "She swam below the waves, chasing the fish."
        scene swim2
        with dissolve
        pause
        "When she saw me she smiled at me before swimming away."

    scene bg black
    with fade
    $renpy.end_replay()

    "{b}Thursday Morning{/b}"
    label galleryScene57:
    scene lbewbs1
    with fade
    pause
    l "Ahhhh! My boobs!"
    l "They are gigantic!"
    "Grace laughed."
    scene lbewbs2
    with dissolve
    g "That's what you get."
    g "Now I'm not the only one that is going to have lower back problems."
    l "Yeah, yeah."
    scene lbewbs3
    with dissolve
    l "Holy shit, Grace."
    g "I know, they're huge."
    if glthreesome:
        l "I was talking about you!"
        l "You're a mess!"
        scene gmess1
        with dissolve
        g "I know."
        l "You are completely covered in dried cum."
        g "Hey, some of it's yours."
        g "Is it gross?"
        scene lbewbs3
        with dissolve
        l "It's disgusting."
        l "And it's kind of hot."
        g "Actually, some of this must be from an hour ago."
        g "It's still wet."
        scene gmess1
        with dissolve
        g "I think I passed out mid orgasm."
        l "Oh, yeah. [n] fucked you unconscious."
        g "Why did you cum on me then, [n]?"
        n "Because we ran out of condoms."
        scene gmess2
        with dissolve
        g "Seriously?"
        g "We used thirty six condoms in three days?"
        l "Yup."
        g "But there is so much."
        scene gmess1
        with dissolve
        n "Well we fucked like three times."
        g "That's why my pussy hurts so bad."
        n "How's your ass?"
        g "Well my ass has hurt this entire trip."
        scene gmess3
        with dissolve
        g "That's why I can never sit down for long."
        l "Yeah, yeah, We know."
        g "We are seriously out of condoms?"
        g "Oh well. I'm too sore to take [n]'s dick anyway."
        l "More for me."
    else:

        g "Hey, can you guys fuck again?"
        g "I want something to drink."
        scene lbewbs2
        with dissolve
        l "Calm your tits."
        l "You drank like five loads yesterday."
        scene gmess4
        with dissolve
        g "That was then."
        g "This is now."
        l "Well, if he fucks me, he is cumming inside of me."
        l "You can't hog it all."
        scene gmess5
        with dissolve
        g "What happened to using protection?"
        l "My birth control has probably kicked in by now."
        l "The condoms are only an extra precaution."
    scene lbewbs4
    with dissolve
    "Laura stood up."
    l "Shit."
    n "What?"
    l "I think I'm going to throw up again."
    if glthreesome:
        "She stumbled over to the bathroom."
        scene gmess3
        with dissolve
    else:
        l "Why don't you just let [n] titty fuck you?"
        g "What?"
        l "Then he could feed you straight into your mouth."
        "Grace perked up."
        g "Okay!"
        g "So I can-"
        l "Don't use your hands."
        l "If you can't get him off only using your huge tits, what good are they?"
        g "Challenge accepted."
        "Laura got up and stumbled to the bathroom."
        "I wasted no time titty fucking Grace with the green light."
        image gtfuck = Movie(play="gtfuck.webm")
        show gtfuck
        with fade
        pause
    g "You didn't drink at all last night, Laura!"
    l "I know."
    g "I thought you didn't get seasick?"
    l "So did I."
    g "Well you've thrown up every day since we got here."
    g "I've only thrown up when I was super drunk."
    n "Congrats."
    if glthreesome:
        scene gmess2
        with dissolve
        "Grace tried to cuddle with me."
        n "Hell no."
        n "Get your stank ass in the shower!"
        "Grace sighed."
        scene gmess1
        with dissolve
        g "There's only so many showers a girl can take in a day."
        g "Before I do, can you titty fuck me one more time?"
        g "I love the feeling of it on my skin."
        g "And it seriously does help me from getting stretch marks."
        scene gmess6
        with dissolve
        n "Fine."
        g "You're the best!"

    else:
        pause
        l "How's it going in there?"
        g "I'm pretty sure [n] is in titty heaven."
        g "Want to join to make it four titties?"
        l "Maybe."
        "Laura returned."
        l "Mmm."
        l "Make room for me-"
        scene gmess6
        with fade
        pause
        l "Wow, [n]. Couldn't wait, huh?"
        g "I think that even the idea was too much for him."
        l "Holy shit, did you get any of it in your mouth?"
        g "I missed feeling it on my skin."
        g "Plus, I feel like it helps me stay moisturized."
        g "I don't want stretch marks."
        scene gmess7
        with dissolve
        l "That's a good point."
        l "Hey, [n]?"
        n "Yeah?"
        l "Could you titty fuck me later?"
        scene gmess6
        with dissolve
        n "I suppose."

    scene bg black
    with fade
    $renpy.end_replay()
    "{b}Thursday Afternoon{/b}"
    scene tan1
    with fade
    pause
    l "Damn, Grace."
    l "I thought the goal was to get a bigger swimsuit."
    g "The goal was to get something that fit."
    scene tan2
    with dissolve

    g "And this is going to help me lose some of these tanlines."
    g "You know your ass is pale as fuck, right?"
    l "[n] wasn't complaining this morning."
    g "I don't know if you noticed, but [n] doesn't complain much when he is inside of somebody."
    scene tan3
    with dissolve
    g "He barely has the ability to talk."
    n "It takes a lot of blood flow to keep things working."
    g "Oh, trust us, we are aware."
    g "You're doing great, champ."
    scene tan4
    with dissolve
    g "A few grunts to show us you are enjoying it, throw in some dirty talk and we are happy."
    l "Makes me happy I brought you, Grace."
    l "Gives me someone to talk to."
    l "If you weren't here, [n] and I would never leave the room."
    scene tan5
    with dissolve
    g "Yeah, it's really threefold, if you think about it."
    g "Not only do you get to talk to me, you get [n] capable of speech because I help wear him out faster."
    l "That's the thing. He's never worn out."
    l "Look at him. You know exactly why he has only said one sentence this entire conversation."
    scene tan6
    with dissolve
    g "Our tits?"
    l "Our massive, juicy titties."
    l "You can see his dick outline go halfway down his leg."
    g "Wait, do you like tits, [n]?"
    g "I had no idea!"
    scene tan7
    with dissolve
    g "Good thing I happen to have two watermelons attached to my chest."
    l "Honestly, I can't believe how big you've gotten, Grace."
    g "Look who's talking!"
    g "Your top doesn't fit in the slightest."
    scene tan8
    with dissolve
    l "I'm only trying to keep up with you."
    g "Well, mission accomplished."
    g "We really need to find that watch when we get back."
    n "You realize we can't rely on the watch, right?"
    scene tan9
    with dissolve
    g "Say what now?"
    n "When I tried to shrink my dick back, it didn't work."
    g "So?"
    n "So what makes you think it would shrink your tits?"
    scene tan10
    with dissolve
    g "Wait."
    g "What-"
    scene tan11
    with dissolve
    g "Are you SERIOUS?"
    n "This is what I've been telling you."
    g "But- but-"
    g "Fuck me."
    n "Yes please."
    scene tan12
    with dissolve
    l "Behave."
    g "I'm going to be STUCK LIKE THIS?"
    g "I thought-"
    g "You know I was a fat kid, right?"
    scene tan13
    with dissolve
    g "I've been eating like cake was going extinct!"
    l "We're aware."
    g "Fuck."
    n "Maybe we could increase your metabolism, like with Haley."
    scene tan14
    with dissolve
    g "Would that make my tits shrink?"
    n "Probably not."
    pause
    g "Motherfucker."

    scene bg black
    with fade
    "{b}Dinner{/b}"
    scene dinner2
    with fade
    pause
    if glthreesome:

        g "We seriously need to buy some condoms tomorrow."
        n "Not so loud!"
        n "People are trying to eat their lobster tails right now."
        l "Why bother?"
        scene dinner1
        with dissolve
        l "It's not like they would do much at this point."
        g "Not just that!"
        g "I can feel the cum dripping down my leg."
        g "It hasn't stopped since lunch."
        scene dinner3
        with dissolve
        l "I know what you mean."
        l "Wait, I thought he only came up your ass?"
        g "Mostly."
        g "But not every time."
        scene dinner1
        with dissolve
    else:
        g "I'm telling you, anal doesn't count."
        n "Not so loud!"
        n "People are trying to eat their lobster tails right now."
        l "Why would I let him fuck your ass?"
        scene dinner1
        with dissolve
        l "That would just make me have to put stank dick inside of me."
        g "He could use a condom."
        l "But I thought the whole point was that you miss having him cum up your ass."
        scene dinner3
        with dissolve
    n "Come on."
    n "People are trying to eat."
    g "What?"
    scene dinner4
    with dissolve
    if glthreesome:
        g "It's your fault."
        g "But seriously Laura, I can't believe you don't like anal."
        g "You're missing out."
        l "You know what?"
        scene dinner3
        with dissolve
        l "Fine."
        l "I'll try it tonight."
        g "You're going to love it!"
        g "I'll make sure to lick your booty until it's ready."
    else:
        g "Yeah, I do want him to cum up my ass."
        g "I can't believe you don't like anal."
        g "You're missing out."
        l "You know what?"
        scene dinner3
        with dissolve
        l "Fine."
        l "He can stick it up my butt tonight."
        l "And then after, you can have a turn."
        g "You're the best!"

    scene bg black
    with fade
    "We finished our meal."
    g "Now let's go dancing!"
    scene bg black
    with fade
    "{b}Two Hours Later{/b}"
    scene dance1
    with fade
    pause
    "Laura grinded her big ass against me."
    "I was trying to not let her catch me looking at the blonde girl almost as much as I was trying not to make a mess in my pants."
    "Laura stopped dancing."
    scene dance2
    with dissolve
    l "I think you should go check on Grace."
    l "She is giving me the signal."
    n "Okay."
    scene dance3
    with fade
    n "Hey Grace."
    scene dance4
    with dissolve
    n "How is everything over here?"
    scene dance5
    with dissolve
    g "Great!"
    g "Except that this dick won't leave me the fuck alone."
    n "You heard the lady."
    n "What's the matter, never seen a pair of huge, amazing tits before?"
    scene dance6
    with dissolve
    "Dick" "Who is this guy?"
    n "I'm her boyfriend."
    "Dick" "Then who is the girl you have been dancing with all night?"
    scene dance7
    with dissolve
    n "My other girlfriend."
    "Dick" "Yeah, right."
    "Laura joined us."
    scene dance8
    with dissolve
    "Dick" "You are telling me that both of you incredibly sexy ladies are with this one joker here?"
    l "That's right."
    "She kissed me."
    scene dance9
    with dissolve
    pause
    "Dick" "Riiight."
    scene dance11
    with dissolve
    g "Is that so hard to believe?"
    "I kissed Grace."
    scene dance10
    with dissolve
    pause
    "Dick" "Oh, shit."
    if glthreesome:
        scene dance12
        with dissolve
        l "Oh, and also..."
        "The girls began kissing each other."
        scene dance13
        with dissolve

        "Dick" "Oh shit!"
        pause
        scene dance13
        with dissolve
        pause

    n "Now leave the girl alone, alright?"
    scene dance14
    with dissolve
    "Dick" "Who are you, man?"
    l "He's more man than you'll ever be."
    g "He's [n]."
    n "Now kindly fuck off."
    scene bg black
    with fade
    "{b}Friday{/b}"
    with fade
    "Laura limped all around the boat."
    "During the comedy show I couldn't tell if she was laughing or crying."
    scene aftershow1
    with fade
    pause
    g "Wasn't it worth it, though?"
    l "No."
    g "It gets easier."
    g "And it gets better."
    scene aftershow2
    with dissolve
    l "I don't care."
    l "But I will say this..."
    l "That was the hardest I've ever orgasmed."
    scene aftershow3
    with dissolve
    l "But I need to take it easy today."
    n "No problem."
    l "You know I've outgrown almost every outfit I brought on this trip?"
    n "You don't say?"
    scene bg black
    with fade
    pause
    "{b}Friday Night{/b}"
    scene dinner6
    with fade
    pause
    g "Come on, Laura!"
    g "I know your ass can't take any more tonight."
    g "But mine is begging for it."
    l "Grace! Stop asking!"
    scene dinner5
    with dissolve
    l "Are you serious right now?"
    l "I have been so understanding with you this entire trip!"
    l "Who else would share their boyfriend as much as I have?"
    l "No one!"
    scene dinner6
    with dissolve
    l "Now stop begging!"
    g "Okay! Fine!"
    g "I'm sorry."
    "Laura turned to me."
    scene dinner7
    with dissolve
    l "[n], are you okay not having sex tonight?"
    n "Honestly?"
    n "I think my dick needs a break."
    l "We all do."

    scene bg black
    with fade
    "{b}Saturday Morning{/b}"
    with fade
    g "Good morning!"
    scene sleep1
    with fade
    pause
    l "Mmmmmph."
    g "You guys ready to grab the buffet for breakfast?"
    n "Fuck yeah."
    scene sleep2
    with dissolve
    l "Noooo."
    g "Still nauseous?"
    l "Yeah."
    g "I get it. You had a few drinks last night."
    scene sleep3
    with dissolve
    l "I had to. My ass hurt too bad."
    g "Want us to wait for you?"
    l "No, go ahead without me."
    l "I don't even want to think about eating."
    scene bg black
    with fade
    pause
    "{b}Thirty Minutes Later{/b}"
    scene breakfast1
    with fade
    pause
    n "Steak for breakfast, huh?"
    g "Protein fills you up."
    n "I can see that."
    n "How are you doing, by the way?"
    scene breakfast2
    with dissolve
    g "I'm awesome."
    g "This trip has been amazing."
    g "I want to thank you for paying for my ticket."
    g "Want me to crawl under the table right now?"
    scene breakfast1
    with dissolve
    n "Raincheck."
    g "Hey, I offered."
    g "I give a pretty mean BJ."
    n "So I heard."
    scene bg black
    with fade
    pause
    "We started walking back."
    scene lifeboat1
    with fade
    pause
    n "By the way, I think you're handling the situation pretty well."
    g "Why thank you."
    g "So are you."
    scene lifeboat2
    with dissolve
    n "Oh, I have no complaints."
    g "Good."
    g "I know Laura is a bit much, but I think you handle her pretty well."
    g "If you aren't careful, she will make you her bitch."
    scene lifeboat4
    with dissolve
    g "Don't let your guard down for one minute."
    n "I'll keep that in mind."
    label galleryScene58:
    g "Hey! I have an idea."
    n "Uh oh."
    scene lifeboat3
    with dissolve
    g "Want to sneak into this lifeboat and pump a load into me?"
    n "Sounds romantical."
    g "Come on."
    menu:
        "[gr]Do it":
            $ lifeboat = True
            scene bg black
            with fade
            pause
            "She showed more acrobatics than I expected as she climbed in."
            n "Wow."
            g "Hurry up!"
            g "No one is watching!"
            scene lifeboat5
            with fade
            pause
            "I climbed up and she sat on top of me."
            scene lifeboat6
            with dissolve
            g "You did it!"
            "She pulled me in for a tight kiss."
            scene lifeboat7
            with dissolve
            pause
            "She sighed."
            scene lifeboat8
            with dissolve
            g "This sucks."
            n "What?"
            g "You realize I'm totally falling for you right?"
            n "Don't fuck with me."
            scene lifeboat6
            with dissolve
            g "Fuck with you?"
            g "I'm serious."
            g "I'm falling in love with you."
            n "Well, shit."
            scene lifeboat9
            with dissolve
            if gracelove:
                g "Remember when you told me you loved me?"
                g "It seems so long ago, but it was about a week ago."
                g "At Laura's house."
                n "Yeah."
                scene lifeboat8
                with dissolve
                g "I know it was just from an orgasmic high at the time..."
                g "But now I'm serious."
                g "I fucking love you."
                n "Well, shit."
                scene lifeboat9
                with dissolve

            g "You don't have to say anything."
            g "Just fuck me like you love me."
            n "So... make love to you?"
            scene lifeboat6
            with dissolve
            g "That sounds gay."
            g "Like this."
            image glifeboat1 = Movie(play="glifeboat1.webm")
            show glifeboat1
            with fade
            pause
            n "Oh fuck!"
            g "Shhhh!"
            if preg:
                g "So, you know that conversation I've been trying to have with you?"
                n "Uh huh."
                g "I've been waiting until Laura wasn't around."
                n "Okay."
                g "Are you trying to knock me up?"
                n "What?"
                g "You have cum inside me at least ten times now."
                g "You know I'm not on birth control."
                g "So what are you trying to do?"
                menu:
                    "Impregnate you":
                        n "I want to make you pregnant."
                        g "Oh, fuck."
                        n "I want you to have my baby."
                        g "Why..."
                        g "Is that so hot?"
                        n "Really?"
                        g "I don't know, I've never wanted that in the past."
                        g "But now that you say it..."
                        g "Fuck."
                    "Nothing [red]\[Pregnant\]":
                        $ preg = False
                        n "Nothing."
                        g "Really?"
                        g "Then we really need to rethink this."
                        n "Yeah."
                        n "Want me to pull out?"
                        g "No."

            else:
                g "You know, I'm going to lose next time we play never have I ever."
                g "Had sex in a boat, on a boat?"
                g "I can't even keep a finger up for that."
                n "This is what you think about, huh?"
            pause
            n "Hey, Grace?"
            g "Yeah?"
            n "What can I do to get you out of that dress?"
            g "You want to see my giant tits bounce?"
            n "You know I do."
            g "I can't blame you."
            image glifeboat2 = Movie(play="glifeboat2.webm")
            show glifeboat2
            with fade
            pause
            g "Eh?"
            n "Fuck yes."
            g "Aww, now you aren't going to last, are you?"
            n "You know I'm good for another round."
            g "You know what?"
            g "You're the best."
            if preg:
                g "Fine, go ahead and cum inside me."
                n "Why would I do that?"
                g "Because you-"
                g "Oh."
                g "Because I want you to knock me up."
                n "You do?"
                g "I want you to make me a milf."
                n "Damn, girl."
                g "Like it?"
                n "You know I do."
            pause
            "We tried to be quiet, but before I finished we heard a voice call out to us."
            "Voice" "Excuse me!"
            "Voice" "Passengers are not allowed in the lifeboats!"
            "Voice" "The lifeboats are a very important safety requirement, and we are not allowed to have anyone tamper with them."
            "I popped my head up."
            scene lifeboat11
            with fade
            n "Sorry, sir."
            n "Thought we saw an iceberg."
            "Crew Member" "I'm sure."
            "Crew Member" "Now, please get down."
            "Crew Member" "And don't do this again. You only get one warning."
            n "We understand."
            scene bg black
            with fade
            "When we got back to the room I felt a little guilty."
            "The moment I had shared with Grace was almost too intense."
            scene cruisedoor1
            with fade
            pause
            "Before we opened the door I stopped her."
            g "What?"
            g "What were you going to tell me?"
            n "There is cum dripping down your leg."
            scene cruisedoor2
            with dissolve
            "She rolled her eyes."
            pause

        "Decline":
            $ lifeboat = False
            n "Sorry, babe."
            n "But I have a girlfriend now."
            g "You haven't got off in like twelve hours!"
            n "Don't remind me."
            g "Fine."
            g "I just wanted you to myself for a change."
    scene bg black
    with fade
    $renpy.end_replay()
    pause
    "{b}Saturday Night{/b}"
    image clubdance1 = Movie(play="clubdance1.webm")
    show clubdance1
    with fade
    pause
    g "Congratulations, Laura!"
    g "You made it twenty four hours without [n]'s dick."
    l "Congratulations to you, Grace!"
    l "It must be much harder for a total slut like you."
    g "You have no idea."
    g "But the real champion is [n]."
    g "It's very hard for him."
    "Both girls smirked."
    n "Hey, can you blame me?"
    n "I've been dancing with the two hottest girls on the boat."
    g "Alright, enough third wheeling."
    g "Why don't you two go back to the room and give in to your carnal urges?"
    l "What would you do?"
    g "I'll find someone to entertain me."
    l "Are you serious?"
    g "Why not?"
    l "Because we have been sharing my man!"
    l "I don't want you to be off collecting STDs from the dirty dudes on this boat!"
    g "Obviously."
    g "But why do you think I was talking about a dude?"
    l "What?"
    g "I got an invitation from a lovely lady to go back to her room."
    l "Seriously?"
    l "Who?"
    g "Kassie."
    l "Is she a tramp?"
    g "Nah, she's classy and shit."
    g "I'll be right back."
    scene dance15
    with fade
    pause
    l "I have no idea what to expect right now."
    n "Seriously."
    l "Oh!"
    l "I've seen her before."
    scene bg black
    with fade
    "Grace returned."
    image clubdance2 = Movie(play="clubdance2.webm")
    show clubdance2
    with fade
    pause
    $ kassie = False
    c "Hey! I'm Kassie."
    n "I'm [n]."
    c "I saw you handle that guy for Grace the other night."
    c "He was a real creep to me too, so I wanted to thank you."
    n "Glad I could help."
    l "And I'm Laura."
    l "What do you do, Kassie?"
    c "I work at a strip club."
    "Laura chuckled."
    l "Big surprise."
    g "She's not a stripper. She's the accountant."
    c "That's right."
    c "I keep the club running."
    l "And you are into girls?"
    c "Exclusively."
    l "I like you already."
    l "Less competition for me."
    c "Unless you are worried about me stealing Grace from you."
    c "Hey, why am I the only one dancing?"
    c "We're on vacation!"
    if glthreesome:
        "Laura smirked."
        l "I have an idea."
        l "How about the four of us head back to our suite?"
        c "A suite, you say?"
        l "[n] snuck in some rum, and we still have a bottle of champagne."
        c "You make a good pitch."
        "She turned to me."
        c "[n], was it?"
        c "I don't mean to be rude, but I want to get this out of the way."
        c "I don't do dick."
        c "That's not a challenge, it's a statement."
        c "Knowing this, are you okay with me coming back with ya'll?"
        menu:
            "[gr]Yes":

                n "Sounds good to me."
                c "Excellent."
                c "I didn't want to step on your toes."
                c "But I've been told I'm fun to watch."
                n "Excellent."
                g "What are we waiting for?"
                n "I'm going to go to the bar and order my last four drinks of the day."
                n "Meet you girls back at the room?"
                g "See you there."
                c "Need help, [n]?"
                n "Sure."
                scene bg black
                with fade
                "We walked over to the bar and I ordered drinks for everyone."
                scene kassie
                with fade
                pause
                n "What will you have?"
                c "The finest scotch included with the drinks pass, please."
                n "Good girl."
                c "So tell me about Grace."
                scene kassie2
                with dissolve
                c "She walks like she knows what she is doing, but I have the suspicion that's all talk."
                n "You're right on."
                c "Any advice?"
                menu:
                    "No":
                        n "I think you have this."
                        scene kassie
                        with dissolve
                        c "Thanks, [n]."
                        c "This is going to be a fun night."
                        n "Damn right."
                    "Yes":
                        n "Just this: Show her a good time."
                        scene kassie
                        with dissolve
                        c "I can do that."
                        n "She deserves it."
                        c "Has she had someone break her heart recently?"
                        n "Just me."
                scene bg black
                with fade
                "Kassie followed me back to the room."
                scene lez9
                with fade
                pause
                "I handed drinks out to the girls."
                n "Make yourself comfortable, Kassie."
                scene lez8
                with fade
                c "Thanks!"

                "She waited to be approached."
                scene lez7
                with dissolve
                "It didn't take long."
                label galleryScene59:
                scene lez1
                with fade
                c "You don't have to be nervous."
                c "I don't bite."
                c "Well, I don't leave a mark."
                c "At least not where you can see."
                scene lez2
                with dissolve
                g "I'm not nervous."
                c "First time with a girl, huh?"
                g "No."
                "She glanced at Laura."
                scene lez10
                with dissolve
                l "Hey, don't incriminate me in this!"
                l "Although I will say that Grace is great at eating pussy."
                c "That's what I like to hear!"
                scene lez1
                with dissolve
                c "Want to have a contest?"
                g "Well technically, I've never had a girl down there."
                c "Really?"
                c "This is going to be fun."
                scene lez2
                with dissolve
                c "Have you ever had a guy do a halfway decent job?"
                "Grace looked at me."
                scene lez3
                with dissolve
                g "Just one."
                c "Interesting!"
                c "What else should I know about you?"
                g "Well, I can do this."
                scene lez4
                with dissolve
                "She pulled her leg up to perform the standing splits."
                n "Holy shit!"
                scene lez5
                with dissolve
                n "Did you know she could do that, Laura?"
                c "Sounds like you should get to know this girl a little better."
                scene lez6
                with dissolve
                n "Gladly."
                l "Hey [n]."
                scene lez11
                with dissolve
                n "Yes?"
                l "Want to join me for a drink and let the girls do their thing?"
                l "I'll let you do my thing."
                n "I'm not going to say no."
                scene bg black
                with fade
                "{b}Three Drinks Later{/b}"
                g "Oh fuuuuuuuu-"
                l "There is no way she is better than [n]."
                "I paused."
                image kas1 = Movie(play="kas1.webm")
                show kas1
                with fade
                pause
                n "I don't know, Laura."
                n "It seems like you are still capable of speech."
                n "I must be doing something wrong."
                "I dove back in."
                l "OH!"
                l "Yessssss!"
                g "I-"
                g "I can still talk."
                g "And there is no way I am this good at eating pussy."
                g "Kassie, you win."
                c "Don't give up too early, Grace."
                g "Fine! Switch!"
                g "I can't take any more of your tongue right now."
                g "Two orgasms was enough."
                g "Laura, you want to get in on this?"
                l "Is it that good?"
                g "Fuck yes!"
                l "Better than [n]?"
                g "Yeah."
                pause
                g "Or no?"
                g "I don't know."
                g "[n] hasn't given me his tongue in a while."
                g "You tell me."
                l "[n], is that okay with you?"
                menu:
                    "[gr]Sure":
                        n "Sure."
                        c "Get over here, sweet lips."
                        scene bg black
                        with fade
                        "Grace and Laura switched positions."
                        l "Oh!"
                        scene lez27
                        with fade
                        pause
                        g "Hey, my clit is way too sensitive still."
                        g "How about you just put your dick in me?"
                        image kas2 = Movie(play="kas2.webm")
                        show kas2
                        with fade
                        pause
                        n "As you wish."
                        g "Oh!"
                        g "OHHHH!"
                        c "Is he that good?"
                        l "Hey! He is fucking her!"
                        l "No fair."
                        l "Oh!"
                        l "Wow."
                        l "Carry on."
                        g "I love [n]'s dick so much!"
                        l "Kassie's tongue is magic."
                        c "I win!"
                        l "I didn't say that."
                        c "What?"
                        l "You are amazing at this."
                        l "But my boyfriend is better."
                        c "Stroking the male ego, I get it."
                        l "Nah. He wins."
                        l "I'm sure you have a lot of good experience going down on all the strippers for tips but-"
                        c "What the fuck?"
                        g "OH FUCK THAT'S DEEP!"
                        g "Oh! Did I not warn you-"
                        g "-about her?"
                        g "Yeah, Laura is a bitch."
                        c "And she's full of shit."
                        l "Don't believe me?"



                    "No":
                        n "Is it unfair if I don't want to share you?"
                        l "Not at all."
                        l "I'm yours."
                        l "Now how about you stick your dick in me?"
                        n "Don't mind if I do!"
                        $renpy.end_replay()
                        jump nextskies
                l "Hey, [n]?"
                l "When you're done fucking my best friend do you want to come over here and give this lesbian a taste for how good your tongue action is?"
                c "I dunno about that."
                g "Your girlfriend is the coolest."

                menu:
                    "[gr]Go for it":
                        n "I mean, is that really on the table?"
                        c "I have never even kissed a guy."
                        l "This isn't about that."
                        l "Just a friendly competition."
                        l "Tell us who has more tongue skills. [n] or Grace."
                        g "Hold the fuck on!"
                        g "I'm so close I-"
                        g "AHHHHHHHH!"
                        scene lez12
                        with dissolve
                        g "I'm going to need a minute, guys."
                        c "Stupid competitive Kassie!"
                        c "I can't believe I'm going to say this..."
                        c "Show me how inferior a guy is at taking care of a lady, [n]."
                        n "I'll do my best."
                        c "But first..."
                        c "Where's the rum?"
                        scene lez13
                        with fade
                        pause
                        c "You get one minute."
                        c "And don't even think about putting anything inside me."
                        image kas3 = Movie(play="kas3.webm")
                        show kas3

                        pause
                        c "Your chin is so rough!"
                        c "How can you girls stand this?"
                        l "I love it."
                        c "It's like sandpaper!"
                        c "I do like that tongue though."
                        c "I should probably close my eyes and imagine that it's Grace..."
                        g "You'll get me down there soon enough babe."
                        c "I like the sound of that."
                        l "It's been a minute."
                        c "Damn girl, don't rush me!"
                        c "Mmmmm."
                        c "Alright fuck."
                        c "[n], you are really fucking good at this."
                        n "Ready for Grace?"
                        c "Not yet-"
                        c "Oh. Oh!"
                        c "OHHHHHHH!"
                        c "Wow."
                        scene lez13
                        with dissolve
                        pause
                        c "Well done."
                        n "How about now?"
                        c "I am so fucking ready for Grace."

                    "Decline":
                        n "My apologies, ladies."
                        n "But I would rather leave Kassie with the feeling that she is missing out."
                        c "Good try."
                        c "But I'm quite satisfied, thanks."
                        g "Hold on, guys!"
                        g "I am really close right now-"
                        g "Keep going, just like that-"
                        g "AHHHHHHHHH!"
                        g "FUCK! FUCK! FUUUUUUUCK!"
                        l "Still not missing out?"
                        c "Hmm..."
                        c "I think I'll manage."
                        c "But I am really wet right now."
                        c "Grace?"
                        pause
                        $renpy.end_replay()
                        jump nextskies

                l "Come here, [n]."
                l "Kassie got me hungry with her nice appetizer."
                l "But I need the main course."
                n "My pleasure."
                scene bg black
                with fade
                "I got up and let Grace have her turn."
                image kas4 = Movie(play="kas4.webm")
                show kas4
                with fade
                pause
                l "YES!"
                l "Fuck yes!"
                l "By the way-"
                l "How does Grace compare, Kassie?"
                c "Oh, she wins hands down."
                l "Really?"
                c "Oh yeah. She's incredible."
                "We heard Grace moan."
                c "A smooth face is the way to ride."
                l "Agree to disagree."
                n "I'm not surprised."
                n "I hypnotized her to give great head, and I didn't specify gender."
                c "Hypnotize?"
                c "That shit doesn't work."
                l "Would you believe it if I told you that a week ago I was a C cup?"
                c "Not for a second."
                pause
                l "Ohhh I can't wait until you cum inside me."
                l "You have no idea how much I've missed it."
                l "Holy shit, you haven't blown your load in over twenty four hours."
                l "When is the last time you went this long?"
                n "I have no idea."
                l "There is going to be so much!"
                g "Wait!"
                g "Don't waste it."
                g "How about the three of us finish you off?"
                g "And you cover us in a shower?"
                c "Say what now?"
                g "His cum is so delicious."
                c "Hard pass."
                g "Fine, we'll blow him."
                g "But you can kiss us while we do."
                menu:
                    "Cum on the girls":
                        c "Why would I want to do that?"
                        l "Because his cum is fucking delicious."
                        l "Grace and I have been fighting over it this entire trip."
                        l "And it's not like it's even in short supply."
                        l "He cums a lot."
                        c "Gross."
                        c "There's not enough rum in this room to get me to do that."
                        g "I mean, you did cum on his face."
                        g "The least you could do is return the favor."
                        c "Fine!"
                        c "But I'm not sucking it."
                        g "No need."
                        l "Hold on!"
                        l "I'm really close."
                        c "Get that O!"
                        l "Oh!"
                        l "Ohhhhhhhhhh!"
                        pause
                        scene bg black
                        with fade
                        "When I stood up Grace pulled up Kassie and dragged her over."
                        "Without waiting Laura enveloped me in her tits."
                        image kas5 = Movie(play="kas5.webm")
                        show kas5
                        with fade
                        pause
                        c "Oh so that's what big tits are for!"
                        c "Both of your tits are so huge!"
                        c "I don't think I have ever felt flatter."
                        c "And I am around strippers all day!"
                        g "Yeah, never get in a size competition with your bitchy best friend."
                        l "Are you close, [n]?"
                        l "I can't fucking wait for this load."
                        l "It's going to be huge."
                        c "Great."
                        pause
                        g "Come here, [n]."
                        g "I'll finish you off."
                        image kas6 = Movie(play="kas6.webm")
                        show kas6
                        with fade
                        pause
                        n "Ohhhh fuck!"
                        c "He seems to like it."
                        n "I love it."
                        n "Grace's tongue skills are unmatched."
                        c "Damn right."
                        c "She's the tongue master."
                        l "Oh, I know that look."
                        l "He is about five seconds from cumming."
                        "I pulled back."
                        scene lez14
                        with fade
                        pause
                        c "No!"
                        scene lez15
                        with dissolve
                        g "Yes!"
                        "In one of the biggest orgasms of my life, I felt a huge release of pressure as I blasted Kassie right in her face."
                        scene lez16
                        with vpunch
                        c "Ah!"
                        "The next load covered her tits."
                        scene lez17
                        with vpunch
                        c "It's so warm!"
                        "Next I turned to Grace."
                        scene lez18
                        with vpunch
                        g "Yes!"
                        scene lez19
                        with vpunch
                        g "Cum in my mouth!"
                        scene lez20
                        with dissolve
                        l "Me!"
                        scene lez21
                        with vpunch
                        pause
                        scene lez22
                        with vpunch
                        l "Cover me!"
                        scene lez23
                        with vpunch
                        pause
                        scene lez24
                        with dissolve
                        pause
                        c "Eww! Some got in my mouth."
                        scene lez25
                        with dissolve
                        pause
                        g "It's so good, right?"
                        c "It's in my eye!"
                        scene lez26
                        with dissolve
                        pause
                        l "Me too!"
                        c "Damn it!"
                        c "Why is it so good?"
                        n "Damn, Grace."
                        n "You should bring over your friends more often."
                        pause
                        $renpy.end_replay()





                    "Finish in Laura":
                        n "Sorry, Kassie."
                        n "But I think I'm about to cum inside my girlfriend right now."
                        n "I hope I'm not being inhospitable."
                        c "You're a saint, [n]."
                        c "If all guys were like you, I might have let one of you go down on me before now."
                        n "High praise."
                        c "How about I command you from here?"
                        n "How's that?"
                        c "You are going to cum inside your girlfriend right when I tell you to."
                        c "Not a second before, not a moment after."
                        c "Are you ready?"
                        n "Yes."
                        pause
                        c "Not yet."
                        n "Ah!"
                        pause
                        c "Not yet."
                        n "Fuck."
                        pause
                        c "Now."
                        n "AHHHHHH!"
                        $renpy.end_replay()
                        jump nextskies

            "No":
                n "I also don't mean to be rude, Kassie."
                n "You seem very nice. It's just that-"
                c "Say no more, I understand."
                c "Nothing wrong with the vanilla choice sometimes."
                n "Vanilla? I have fucked these two girls-"
                c "Yeah, yeah."
                c "I'm sure you make the strippers I work with look like angels."
                c "Well, it was nice to meet you."
                g "You're missing out, [n]."
                c "Nah, guys don't like to watch sexy ass girls hook up."
                jump kassie


    else:
        label kassie:
        l "Well, Kassie, you seem like a stand up gal."
        l "I don't mind lending Grace to you for the night."
        l "As long as you show her a good time."
        c "I promise."
        l "What about you, [n]?"
        menu:
            "Let Grace leave with Kassie [gr]\[Kassie\]":
                $ kassie = True
                n "I don't see why not."
                n "As long as you are back in time for curfew, missy."
                n "It's a school night."
                g "Yes, Daddy."
                c "Real quick, [n], before I go."
                c "Do you like Rick and Morty?"
                menu:
                    "Yes":
                        n "Sure."
                        c "The show has been getting a bit over the top with the fourth wall breaks."
                        n "Right? The last episode-"
                        c "At the risk of doing the same, I want to tell you something."
                        n "Okay?"
                        c "I'm one of the main girls for the game Endowed."
                        n "Oh yeah?"
                        c "That's the new game the developer of Hypnosis is working on."
                        n "Huh."
                        c "Just thought I'd throw in a little teaser for you."
                        c "It's me. I'm the teaser."
                        n "Thanks?"
                        c "Lubba dubba dub dub!"
                        l "What the fuck?"
                    "No":
                        n "What?"
                        n "No, why?"
                        c "Oh. That's too bad."
                        c "No reason."
                        c "Nice to meet you guys!"
                "Kassie left with Grace and I took Laura back to our room."

            "Tell her not to":
                n "Look, I don't own you, Grace."
                n "But I have to tell you I'm not comfortable letting you leave with this girl."
                if lifeboat:
                    g "Okay."
                    g "Thanks for telling me."
                    g "I won't."
                    c "That's too bad."
                    c "But I don't blame you."
                    c "You girls would both make strippers jealous."
                    l "You're no slouch yourself."
                    c "Real quick, [n], before I go."
                    c "Do you like Rick and Morty?"
                    menu:
                        "Yes":
                            n "Sure."
                            c "The show has been getting a bit over the top with the fourth wall breaks."
                            n "Right? The last episode-"
                            c "At the risk of doing the same, I want to tell you something."
                            n "Okay?"
                            c "I'm one of the main girls for the game Endowed."
                            n "Oh yeah?"
                            c "That's the new game the developer of Hypnosis is working on."
                            n "Huh."
                            c "Just thought I'd throw in a little teaser for you."
                            c "It's me. I'm the teaser."
                            n "Thanks?"
                            c "Lubba dubba dub dub!"
                            l "What the fuck?"
                        "No":
                            n "What?"
                            n "No, why?"
                            c "Oh. That's too bad."
                            c "No reason."
                            c "Nice to meet you guys!"
                    "We said goodbye to Kassie and I took Grace and Laura back to the room, one in each arm."
                else:
                    $ kassie = True
                    g "Good to know."
                    g "But I think I'm going to need a little time apart tonight."
                    g "You two have fun, okay?"
                    l "Love you, girl!"
                    g "Goodnight, [n]."
                    g "Make sure to think of me when you are fucking Laura, okay?"
                    n "I always do."
                    l "Hey!"
                    "Kassie smirked."
                    l "That's fine. I'll be thinking about Kassie."
                    g "You are going to think of her when you are being dicked down?"
                    l "Totally."
                    c "Easy to do!"
                    c "My dick is way bigger than anyone expects."
                    g "What?"
                    c "Kidding."
                    c "Nice to meet you guys!"


    label nextskies:
    scene bg black
    with fade
    "{b}Sunday Morning{/b}"
    image bonegrace1 = Movie(play="bonegrace1.webm")
    show bonegrace1
    with fade
    "Grace was moaning softly as I plowed her."
    pause
    g "Mmmm!"
    g "Just like that, [p]!"
    g "Fuuuuuck."
    image bonegrace2 = Movie(play="bonegrace2.webm")
    show bonegrace2
    with dissolve
    pause
    l "Hey!"
    if kassie:
        l "Welcome back, Grace."
        l "But why are you guys going without me?"
        g "Needed... his cum."
        l "How was your time with Kassie?"
        g "We had fun."
        g "But I need dick."
        l "Yeah, we pretty much fucked all night."
    else:
        l "You guys are going without me?"
        g "Oh, hey."
        l "Let me guess."
        l "You woke up with something hard poking you in the ass?"
        g "Wow, Laura. How would you know?"
    g "Such a slut."
    l "Shut up!"
    l "And get up."
    l "I'm actually feeling like breakfast."
    g "Mmm, no."
    l "Stand up right now, or never fuck my boyfriend again!"
    "Laura reached for Grace's arms and pulled her up."
    scene bg black
    with fade
    pause
    "There was a squishy sound as Grace pulled away from me and stood up."
    scene sexbed2
    with fade
    pause
    "We all heard it at once."
    "The dam broke."
    scene sexbed3
    with dissolve
    l "What-"
    l "Oh my god!"
    l "There's so much!"
    scene sexbed4
    with dissolve
    if kassie:
        l "How is there so much?"
        l "And when did you get back?"
        g "A few hours ago."
        "Grace sat back down."
        scene sexbed5
        with fade
        pause
        l "And you've been fucking ever since?"
        scene sexbed6
        with dissolve
        g "I guess so."
    else:
        l "How many times did you fuck last night?"
        "Grace sat back down."
        scene sexbed5
        with fade
        pause
        g "Umm..."
        g "We kind of..."
        scene sexbed6
        with dissolve
        g "Haven't stopped."
        l "You were fucking each other all night?"
        g "...yeah."
        l "Are you serious?"
        scene sexbed7
        with dissolve
        g "Well, we were all taking turns..."
        g "...but then you fell asleep."
        l "But-"

    "Laura turned to me."
    scene sexbed8
    with dissolve
    l "How many times did you cum inside Grace?"
    n "I don't know."
    n "When I fell asleep I was still inside her."
    scene sexbed7
    with dissolve
    n "I think I've been sleep fucking her."
    l "Holy shit."
    l "I don't even know what to say."
    scene sexbed9
    with dissolve
    l "You are so taking the morning after pill when we get back."
    g "Oh, definitely."
    "Laura sighed."
    scene sexbed10
    with dissolve
    l "We might as well make the most of it now."
    l "It's our last night."
    scene bg black
    with fade
    $ renpy.end_replay()
    "{b}Sunday Evening{/b}"
    "{b}Adults Only Hot Tub{/b}"
    label galleryScene60:
    scene cruisetub8
    with fade
    pause
    l "Why can't these fucking people leave?"
    n "Pretty sure they can hear you."
    l "Good."
    scene cruisetub9
    with dissolve

    l "Then maybe they will get out of here so I can enjoy this sunset properly."
    l "By riding my boyfriend's giant cock."
    g "Eight points for the dirty talk there."
    scene cruisetub10
    with dissolve

    l "I'll give you ten points if you flash your tits."
    g "Yeah?"
    scene cruisetub11
    with dissolve

    g "Done."
    scene cruisetub12
    with dissolve
    l "Nice."
    g "You just wanted to see them, didn't you?"
    l "Nah ah!"
    g "Sure."
    scene cruisetub11
    with dissolve
    g "Did anyone notice?"
    n "They noticed."
    l "Good."
    scene cruisetub10
    with dissolve
    g "You know who I wish was here?"
    n "Kassie?"
    scene cruisetub13
    with dissolve
    g "Kassie."
    l "Call her."
    g "Wish I could."
    g "Alright, I have an idea."
    scene cruisetub11
    with dissolve
    g "THE ORGY BEGINS IN FIVE MINUTES!"
    n "Ha!"
    l "It's working!"
    scene bg black
    with fade
    "As soon as we had the place to ourselves, Laura climbed on top of me."
    pause
    image cruisetubsex = Movie(play="cruisetubsex.webm")
    show cruisetubsex
    with fade
    pause
    g "At least we are being safe now."
    l "Like that is going to change anything after this morning."
    l "You are probably going to be the next octomom."
    g "Oh well."
    l "Are you serious?"
    l "Whatever. I'm not here to talk right now."
    l "Just FUCK ME!"
    l "Yes! [n]! Just like that!"
    g "Alright, five points."
    g "But only because you still sound hot when you are faking it."
    l "I'm not-"
    g "Someone is coming."
    l "Is it Kassie?"
    g "No."
    l "Too bad. That would be hot."
    pause
    g "Laura! Get off him-"
    "Crew Member" "Hey!"
    scene cruisetub4
    with fade
    "Crew Member" "No sex in the hot tub!"

    "Crew Member" "Come on!"
    "Laura pushed off me."
    scene cruisetub5
    with dissolve
    "Crew Member" "People have been complaining."
    scene cruisetub6
    with dissolve

    if lifeboat:
        n "Sorry."
        n "Her leg cramped and I was trying to stretch it out."
        "Crew Member" "Wait, it's you!"
        l "What?"
        "Crew Member" "You're the guy that was fucking in the lifeboat yesterday!"
        l "No-"
        scene cruisetub7
        with dissolve
        "Crew Member" "And you!"
        "Crew Member" "Wasn't he in there with you?"
        "Crew Member" "Ha! Wow."
        scene cruisetub6
        with dissolve
        "Crew Member" "Can't you guys stick to your rooms like everyone else?"
        "Crew Member" "Good thing this trip ends tomorrow or I'd have you kicked off."
    else:
        n "Sorry."
        n "Her leg cramped so we were trying to stretch it out."
    "Crew Member" "Why are you still sitting there?"
    "Crew Member" "Get out of here!"
    if lifeboat:
        scene bg black
        with fade

        "We headed back to the room."
        scene angryl
        with fade
        pause
        l "What was that?"
        g "Oh! Did we tell you?"
        g "We tried out one of those lifeboats."
        g "It was fun!"
        scene angryl2
        with dissolve
        g "You and [n] should try it tonight."
        l "And this was yesterday?"
        g "Yeah."
        l "So you two decided to fuck each other behind my back?"
        scene angryl3
        with dissolve
        n "It wasn't like that-"
        l "How many times?"
        g "Once!"
        scene angryl5
        with dissolve
        g "Just the once."
        l "Wow, Grace."
        l "Every time I give you an inch, you take a mile."

        scene angryl4
        with dissolve
        l "So I can trust you, huh?"
        l "I'm an idiot."



    else:
        scene bg black
        with fade
        "The rest of the night was a drunken blur of tits, sex and bigger tits."
        "Grace and Laura both only had one outfit that fit left for the drive back."
    scene bg black
    with fade
    $ renpy.end_replay()
    pause
    "{b}Monday Morning{/b}"
    with fade
    label galleryScene61:
    "I woke to the sensation of someone sucking my dick."
    "After I came, I smiled before passing back out."
    "The motion of the body riding me woke me back up."
    "I opened my eyes and was surprised with the face on top of me."
    if leahf:
        image leahrider2 = Movie(play="leahrider2.webm")
        show leahrider2
        with fade

    else:
        image leahrider = Movie(play="leahrider.webm")
        show leahrider
        with fade
    pause
    n "Leah?"
    L "Welcome home."
    n "Hey, we can't-"
    L "Oh! Fuck yes!"
    n "I'm with Laura now."
    L "You feel so fucking good!"
    L "You have no idea how much I missed this."
    n "Leah, we can't."
    L "Do you want me to stop?"
    menu:
        "Yes":
            n "Yes."
            if leahf:
                scene leahsmall1
            else:
                scene leahbig1

            L "Oh."
            L "Can we at least finish?"
            L "You have no idea how much I've been craving your cum."
            menu:
                "Fine":
                    n "Fine."
                    L "Oh fuck yeah!"
                    if leahf:
                        show leahrider2
                    else:
                        show leahrider
                    L "You're the best."
                    n "That's what they tell me."
                    L "So- uh!"
                    L "Did you have fun?"
                    n "It was a ton of fun."
                    L "Good!"
                    L "Next time, bring me. Okay?"
                    n "Sure."
                    L "You're the best!"
                    L "The best. The BEST!"
                    L "OH!"
                    L "YESSS!"
                "No":
                    n "No."
                    if leahf:
                        scene leahsmall2
                    else:
                        scene leahbig1
                    with dissolve
                    L "Fuck!"
                    L "You have no idea how much this hurts me to get off you right now."
                    L "But I respect your wishes."
                    n "Thanks, Leah."
                    n "You're a good friend."
                    "She rolled her eyes."
        "No":

            n "No."
            L "Thank God."
            L "Give it to me!"
            L "Yessssss!"
            pause
            L "Okay, I'll admit it."
            L "I didn't just miss your dick."
            L "I missed you too."
            n "You are too sweet."
            L "It's true!"
            L "It wasn't the same without you here."
    $renpy.end_replay()
    L "So Laura?"
    L "Really?"
    L "You chose Laura?"
    n "Yeah, it made sense."
    L "You do realize that as long as you still live here you are going to wake up inside of me every morning, right?"
    menu:
        "Fine [gr]\[Leah\]":
            $ leah = True
            n "Fine by me."
            L "Good."
            "She kissed me."
        "Turn her down":
            $ leah = False
            n "Leah..."
            n "That can't happen."
            L "Hey, I warned you."
            L "What else can you expect from me?"
    L "I don't even remember why I was mad at you."
    scene bg black
    with fade
    if leah:
        "But from then on, every time she tried to fuck me my dick went limp."
        "The only chance she was able to successfully ride me was when she caught my morning wood before I woke up."
        "And even then, half the time I would lose it before she had finished."

    scene bg black
    with fade
    "{b}A Week Later{/b}"
    scene lauranews5
    with fade
    pause
    l "I figured out why I kept throwing up."
    n "Oh yeah?"
    n "You're pregnant?"
    l "Actually..."
    scene lauranews4
    with dissolve

    n "What!"
    l "Yeah."
    n "Holy shit."
    l "Good thing I wasn't drinking much."
    scene lauranews6
    with dissolve
    n "Seriously."
    n "So it was-"
    l "Morning sickness."
    n "Wow."
    scene lauranews4
    with dissolve
    n "What are you going to do?"
    l "What are {i}we{/i} going to do."
    n "Right."
    l "I want to keep it."
    scene lauranews5
    with dissolve
    n "Are {i}we{/i} going to tell your parents?"
    l "Already told them."
    l "They said you can move in."
    l "You can have Brittany's old room."
    if leah:
        scene lauranews4
        with dissolve
        l "You can move in tomorrow."
        n "Okay."
        n "Give me a few weeks."
        l "What?"
        l "Why?"
        n "Cory's parents have been nice enough to let me stay."
        n "I don't want to run out on them."





    if preg:
        scene bg black
        with fade
        "{b}A Month Later{/b}"
        scene bg laurakitchen3
        with fade
        pause
        "Officially I was all moved in."
        "I went to the kitchen to get a drink of water."
        "I was doing my best to win over Laura's parents, but they still seemed pissed off at me for knocking up their daughter."

        scene bg lauraentrance
        with fade
        pause
        "Right as I reached the stairs the doorbell rang."
        "Not wanting to open the front door to a stranger, I checked the peephole and found Grace."
        "I opened the door."
        n "Hey!"
        n "Come in."
        scene gracenews1
        with fade
        pause
        n "Laura isn't-"
        g "Is anyone else here?"
        n "No-"
        scene gracenews2
        with dissolve
        g "I'm pregnant."
        pause
        n "Fuck!"
        n "You're fucking with me, right?"
        scene gracenews1
        with dissolve
        g "I missed my period."
        g "So I took a test."
        n "But-"
        g "It's yours."
        scene gracenews3
        with dissolve
        n "Are you sure?"
        g "I haven't had sex with anyone else."
        n "Does Laura know?"
        g "Not yet."
        scene bg black
        with fade
        "She wiped her eyes"
        scene gracenews4
        with dissolve
        g "I took the Plan B pill when we got back from the cruise."
        g "But you were fucking me that entire week."
        n "Yeah."
        n "Holy shit."
        scene gracenews3
        with dissolve
        g "She's going to hate me!"
        n "This isn't your fault."
        g "I know."
        g "It's yours."
        scene gracenews5
        with dissolve
        "She smiled."
        n "What about your dad?"
        g "He is probably going to kick me out when he finds out."
        n "When are you going to tell him?"
        g "Never!"
        scene gracenews7
        with dissolve
        g "I'm just going to keep getting bigger and bigger until he notices."
        n "Holy shit."
        n "Don't worry."
        n "We are going to figure something out."
        scene gracenews6
        with dissolve
        n "Laura and I are getting our own place soon."
        n "Maybe you can live with us."
        g "This sucks."
        g "I finally stopped growing, then this!"
        scene gracenews8
        with dissolve
        n "Seriously."
        g "But now I know why I keep gaining weight."
        g "You know I gained twenty pounds on the cruise?"
        n "Holy shit."
        if lifeboat:
            scene gracenews7
            with dissolve
            g "Thank you."
            n "For what?"
            g "For taking care of me."
            n "You know I'll do anything for you."
            label galleryScene62:
            scene gracenews6
            with dissolve
            n "What else can I do?"
            "She smiled."
            scene gracenews7
            with dissolve
            g "I think you know."
            n "Bathroom?"
            n "For old time's sake?"
            g "Hell yes."
            scene gracenews8
            with dissolve
            n "Are you sure?"
            n "You've gone almost a week without-"
            g "I'm sure."
            image gracesink = Movie(play="gracesink.webm")
            show gracesink
            with fade
            g "That's it!"
            g "Uhhhh!"
            g "I'm never going a week without this again."
            g "I will choke out Laura if I have to."
            n "I'd watch that."
            g "Fuck me!"
            pause
            g "How excited are you to see me start to show?"
            g "It's just too bad my tits will keep growing..."
            with hpunch
            g "Did you just cum?"
            with hpunch
            n "...no."
            with hpunch
            "I fucked her twice more before she passed out."
            scene bg black
            with fade
            $renpy.end_replay()
            if brittany:
                "The physical exertion made me super thirsty, so I went out to the kitchen."
                scene bg laurakitchen4
                with fade
                pause
                "Deep in thought, I ran right into a small body hard enough to knock her to the ground."
                b "Oww!"
                scene britkit2
                with dissolve
                b "Watch where you're going, motherfucker!"
                n "You scared the shit out of me!"
                "She smirked."
                scene britkit3
                with dissolve
                b "Thought I might be my parents, huh?"
                b "They might be a little pissed off to come home and find loud monkey noises coming from the bathroom."
                b "Who do you have in there, anyway?"
                scene britkit2
                with dissolve
                n "Grace."
                b "What!"
                scene britkit1
                with dissolve
                "She glared at me."
                scene britkit2
                with dissolve
                b "'Only attracted to Laura', huh?"
                b "More like you just aren't attracted to me."
                n "That's not-"
                b "How big are Grace's tits now? Did they pass basketballs?"
                "I sighed."
        else:
            scene bg laurakitchen4
            with fade
            pause
            "Deep in thought, I ran right into a small body hard enough to knock her to the ground."
            b "Oww!"
            scene britkit2
            with dissolve
            b "Watch where you're going, motherfucker!"
            n "I take it your parents aren't home?"
            scene britkit3
            with dissolve
            "She smirked."

            b "Why, because I'm their perfect angel whenever they're around?"
            n "Yep."
            b "I'll have you know, it takes a lot of work being the good sister."
            b "Although it has been easier lately, thanks to you."
            scene britkit5
            with dissolve
            b "Thanks for knocking her up!"
            n "Anything for you."
            scene britkit4
            with dissolve
            "There was an awkward pause."
            b "Why are you weird around me now?"
            n "Me?"
            scene britkit3
            with dissolve
            n "You're the one that always seems pissed off at me."
            b "Can you blame me?"
            n "Why? Because of your sister?"
            scene britkit2
            with dissolve
            b "No, because you have been withholding that good D!"
            "I sighed."

    else:
        if brittany:
            scene bg black
            with fade
            "{b}A Month Later{/b}"
            scene bg laurakitchen4
            with fade
            pause
            "Officially I was all moved in."
            "I went to the kitchen to get a drink of water."
            "I was doing my best to win over Laura's parents, but they still seemed pissed off at me for knocking up their daughter."

            "Deep in thought, I ran right into a small body hard enough to knock her to the ground."
            b "Oww!"
            scene britkit2
            with dissolve
            b "Watch where you're going, motherfucker!"
            scene britkit1
            with dissolve
            n "I take it your parents aren't home?"
            "She smirked."
            scene britkit2
            with dissolve
            b "Why, because I'm their perfect angel whenever they're around?"
            n "Yep."
            b "I'll have you know, it takes a lot of work being the good sister."
            b "Although it has been easier lately, thanks to you."
            scene britkit3
            with dissolve
            b "Thanks for knocking her up!"
            n "Anything for you."
            scene britkit4
            with dissolve
            "There was an awkward pause."
            b "Why are you weird around me now?"
            scene britkit3
            with dissolve
            n "Me?"
            n "You're the one that always seems pissed off at me."
            b "Can you blame me?"
            n "Why? Because of your sister?"
            scene britkit2
            with dissolve
            b "No, because you have been withholding that good D!"
            "I sighed."
    if brittany:
        n "Are you really going to keep blaming me?"
        scene britkit4
        with dissolve
        b "I don't blame your dick for not liking me."
        b "I blame you that we have only tried three times."
        b "I never thought of you as a quitter."
        scene britkit1
        with dissolve
        "I sighed again."
        n "Look, it's embarrassing, okay?"
        n "I've never had issues before."
        scene britkit5
        with dissolve
        b "Yet, you never have an issue with Laura, right?"
        n "Correct."
        n "We went eight rounds the other day."
        "Brittany moaned."
        scene britkit3
        with dissolve
        b "Stop!"
        b "You can't tease me like that!"
        b "Do you have any idea how much I miss your dick?"
        n "Nope."
        scene britkit6
        with dissolve
        b "I want to try again."
        b "But I have an idea."
        n "Tell me."
        b "Maybe you're desensitized, you know?"
        scene britkit5
        with dissolve
        b "You're a tit man."
        b "You are used to them big and nothing else will do."
        b "So I'm going to convince my fiance to pay for my boob job."
        n "Really?"
        scene britkit3
        with dissolve
        b "If you still had the watch, I would just make you use it."
        b "But what other option do I have?"
        menu:
            "Encourage her":
                n "Wow."
                scene britkit4
                with dissolve
                "She rolled her eyes."
                b "Yes, I'm willing to go through surgery for you."
                scene britkit3
                with dissolve
                b "But it's for your dick, not you. Got it?"
                n "Got it."
                b "Good."
                scene bg black

                with fade
                "{b}A Month Later{/b}"
                with fade
                scene backseat
                pause
                "Laura sat with me in the backseat as Laura's parents drove us back home from dinner."
                "Laura's Mom" "Well, I guess I'm going to have to be the one to say it."
                l "You don't have to do anything, Mom."
                "Laura's Mom" "Fine, tell us what you think."
                l "About what?"
                "Laura's mom sighed."
                "Laura's Mom" "About your sister showing up at dinner with blimps on her chest."
                l "Did she?"
                l "I must not have noticed."
                "Laura's Mom" "Sure, dear. I know you have an overabundance. But I didn't realize your sister was jealous of you."
                l "Let her live her life, Mom."
                l "What do you think, Dad?"
                "Laura's Dad" "Your sister can do what she wants with her life."
                l "Agreed."
                "Laura's Mom" "Well, I just don't see why she had to go so large."
                "Laura's Mom" "She looked fine before."
                "Laura's Mom" "And that's enough about that. No one mention it around Brittany when we get home."
                l "I'll try."
                scene bg black
                with fade
                "{b}One Hour Later{/b}"
                scene bg black
                with fade
                pause
                "After hanging out with the family for a bit, Laura insisted we return to her room."
                "Brittany looked disappointed when we wished her a goodnight."
                scene blshowdown1
                with fade
                pause
                l "I can't believe I still stand up for her."
                l "She wants to make her future husband pay for her new boobs?"
                scene blshowdown2
                with dissolve
                l "Fine by me."
                l "I know he has always had a thing for me-"
                "There was a knock on the door."
                scene blshowdown3
                with dissolve
                b "Hey, Laura! It's me."
                l "Come in."
                b "Hey, I have something I need to ask you."
                scene blshowdown4
                with fade
                pause
                l "Yes?"
                scene blshowdown5
                with fade
                pause
                b "Hey, so I don't really know how to talk to you about this."
                b "So let me start by saying, you are super sexy."
                scene blshowdown6
                l "Okay?"
                scene blshowdown5
                with dissolve
                b "Everyone thinks you are the sexier sister."
                b "Yes, I heard you from outside the door."
                b "And maybe my husband does have a thing for you."
                l "Brittany, I-"
                scene blshowdown7
                with dissolve

                b "Would you ever let me fuck your boyfriend?"
                l "What?"
                b "Well, if my future husband wants to fuck you, do you think [n] wants to fuck me?"
                "Laura smirked."
                scene blshowdown10
                with dissolve
                l "I know he doesn't."
                l "He only has eyes for me."
                b "And Grace."
                scene blshowdown9
                with dissolve
                l "What?"
                b "You let him fuck Grace."
                l "Brittany! What are you-"
                scene blshowdown7
                with dissolve
                b "I want to fuck him too."
                b "If that's okay."
                scene blshowdown8
                with dissolve
                l "Are you... what?"
                l "You know I don't want to fuck your future husband, right?"
                b "Yes."
                b "But you do realize that [n] was fucking me before you guys left on the cruise, right?"

                scene blshowdown11
                with dissolve
                l "WHAT?"
                b "You two weren't together yet."
                b "I had never tried that big of a dick before."
                scene blshowdown12
                with dissolve
                b "And I fucking loved it."
                b "And we haven't done anything since then, because you guys are dating."
                b "But I really, really want him to fuck me again."
                scene blshowdown11
                with dissolve
                l "I can't even-"

                b "That's why I got my tits enlarged, okay?"
                scene blshowdown9
                with dissolve
                b "Because it makes me look more like you."
                b "I just went through surgery, and now I know you don't have to, but I really need his dick."
                l "Why?"
                b "You know."
                b "It's fucking amazing."
                "Laura grinned."
                scene blshowdown10
                with dissolve
                l "Yeah it is."
                scene blshowdown9
                with dissolve
                l "What do I get that I would ever let you-"
                b "You get my silence."
                l "What?"
                scene blshowdown7
                with dissolve
                b "If I were to find out something about you..."
                b "...something that you don't want anyone else to know..."
                scene blshowdown8
                with dissolve
                b "...I wouldn't tell them."
                "She gave her sister a look."
                scene blshowdown9
                with dissolve
                l "Really, Brittany?"
                b "Yep."
                l "You know what?"
                l "Fine."
                l "But you only get one time."
                b "Per day."
                l "Ever."
                b "Every other day."
                scene blshowdown8
                with dissolve
                l "A month."
                b "A week."
                l "Deal."
                "The two sisters glared at each other."
                scene blshowdown9
                with dissolve
                b "I know I'm asking a lot, but..."
                b "Can I take him right now?"
                l "You know what, Brit?"
                l "Fine."
                label galleryScene27:
                l "My pussy is too sore right now anyway."
                "She looked at me."
                scene blshowdown11
                with dissolve
                l "What do you have to say for yourself?"
                n "You're the best."
                scene blshowdown10
                with dissolve
                l "Don't fucking forget it."
                "I took Brittany to my room."
                scene britroombig1
                with fade
                pause
                b "So what do you think?"
                b "Now that I finally have you alone."
                n "First off, your tits look amazing."
                n "But also, did you really just convince Laura to let me fuck you?"
                scene britroombig2
                with dissolve
                b "I did, yes."
                b "Are you surprised?"
                n "Maybe!"
                b "Well, you shouldn't be."
                scene britroombig1
                with dissolve
                n "Back to your tits."
                n "Do they look anything as nice as the pictures you sent me?"
                b "Judge for yourself."
                scene britroombig3
                with dissolve
                n "Damn!"
                b "You like?"
                n "Very much."
                b "I tried to go even bigger, but the doctor said this was the biggest amount of CCs he would let me go with."
                scene britroombig4
                with dissolve
                n "You're bangin'."
                b "I'd like to be."
                b "Think we could do something about that?"
                scene britroombig5
                with dissolve
                b "Also, why does my room look exactly the same?"
                n "I don't really spend a lot of time in here."
                b "Clearly."
                n "And why would I want to mess with your stuff, anyway?"
                b "I've got some stuff for you to mess with."
                scene britroombig6
                with dissolve
                "I bent her over."
                b "Oh!"
                "In one motion I ripped off her panties and thrust into her."
                image britcarry1 = Movie(play="britcarry1.webm")
                show britcarry1
                with fade
                b "OH MY-"
                n "SHHHH!"
                b "My-"
                b "Ahhhhh!"
                b "You are so fucking thick!"
                n "Just how you like it."
                b "I fucking love it."
                pause
                b "You know I've never been fucked in this bedroom before?"
                n "Really?"
                b "I was a good girl."
                b "Hey, remember that one time you picked me up while you fucked me?"
                n "Was it like this?"
                image britcarry2 = Movie(play="britcarry2.webm")
                show britcarry2
                with fade
                b "Very close."
                b "Oh shit that's deep!"
                pause
                n "You know what I like about this position?"
                b "My tits in your face?"
                n "Yep!"
                n "And the fact that we aren't moving any furniture around."
                n "Only sound is us breathing and the smacking of my hips on your ass."
                b "I don't hear anything."
                image britcarry3 = Movie(play="britcarry3.webm")
                show britcarry3
                with fade
                b "OH!"
                b "Okay!"
                b "Yeah, now I hear it!"
                b "How long can you keep this up?"
                n "Long enough."
                pause
                b "Oh fuck, I'm going to cum!"
                if preg:
                    n "Are you still into-"
                    b "The idea of you knocking me up?"
                    b "Oh yeah, come inside me, big boy."
                    b "I'll take the attention away from Laura, I don't give a fuck."
                    n "You girls fighting is super attractive."
                    b "Shut up."
                    n "Beg me."
                    b "What?"
                    n "Beg me for it."
                    b "Fine."
                    b "[n], I want you to cum inside me."
                    b "Please?"
                    b "Pretty please?"
                    b "Please put a baby inside me?"
                    with hpunch
                    b "Ah!"
                    with hpunch
                    b "I can feel it-"
                    with hpunch
                    scene bg black
                    with fade
                    "I tossed her on the bed and continued ravaging the girl."

                else:
                    b "And by the way, I'm on birth control now."
                    b "So cum wherever you want."
                    n "How about inside of you?"
                    b "Be my guest!"
                    pause
                    with hpunch
                    b "Oh!"
                    with hpunch
                    b "I can feel it!"
                    with hpunch
                    b "I like it."
                    scene bg black
                    with fade
                    "I tossed her back on the bed and continued ravaging the girl."
                    pause
                $ renpy.end_replay()


            "Turn down the idea [red]\[brittany\]":
                $ brittany = False
                n "Don't do it."
                b "Why?"
                scene britkit2
                with dissolve
                n "Let's move on, okay?"
                n "What we had was fun."
                n "But it's for the best that we stopped."
                scene britkit1
                with dissolve
                n "This way you can still be the good girl."
                b "More like the unsatisfied housewife."


    scene bg black

    with fade
    "{b}Two Months Later{/b}"
    scene backseat
    with fade
    pause
    "Once again I found myself in the back seat of Laura's parents car."
    "I sat between Laura and her sister."
    if brittany:
        "Brittany kept brushing her leg against me as I tried to ignore her."
        if bcum:
            "She was already starting to show with the hint of a baby bump."
            "Her parents were excited to be getting two grandchildren."
            "I was very determined to not let them know that their grandchildren both had the same father."
    "Laura's Mom" "That was a great ceremony, Laura!"
    "Laura's Mom" "I can't believe you and Brittany are both finished with high school now."
    l "Not much confidence in me, huh Mom?"
    "Laura's Mom" "That's not what I mean at all and you know it!"
    "Laura's Mom" "You looked great out there."
    "Laura's Mom" "Although I have to say, I don't know what they were feeding you girls there."
    l "I know, Mom. You already brought it up."
    "Laura's Mom" "I'm just saying! All you girls looked like you were about to fall over! I've never seen a more top heavy class."

    "She was right."
    "Even in their gowns, I could see the difference in the girls as they walked down the aisle to accept their diplomas."
    "After the cruise, Grace had stopped growing."
    "Laura had as well, except for the slight boost from her pregnancy."
    "The other girls, however, had not been as fortunate."
    "I felt bad about it all."
    "I had apologized to the girls several times, but it was hard when each time I saw them they were bigger."
    "I don't know how the watch never turned up."
    "I tried different watches. I tried every idea I could think of."
    "Nothing seemed to work."

    if lifeboat:
        label galleryScene28:
        n "So where is the graduation party?"
        l "About that."
        n "Yeah?"
        l "I don't think I can bring you."
        n "I'm not allowed?"
        l "No, I don't trust the other girls."
        n "Oh."
        l "Brittany isn't doing anything tonight."
        l "Why don't you and my parents all go see a movie or something?"
        n "Sounds like a blast."
        if brittany:
            scene bg black
            with fade
            "{b}Two Hours Later{/b}"
            b "So-"
            if preg:
                image britbentp = Movie(play="britbentp.webm")
                show britbentp
                with fade
            else:
                image britbent = Movie(play="britbent.webm")
                show britbent
                with fade
            "She paused to take a deep breath as I bottomed her out."
            b "Laura didn't want to take you to her graduation party because she doesn't trust you?"
            n "Can you believe it?"
            b "Unnn-"
            b "No!"
            b "Fuck this feels so good!"
            pause
            b "Why don't we do this more, again?"
            n "Come on."
            n "Stay in character."
            b "Oh, right."
            b "Because I have to dress up like my stupid sister each time."
            b "Ah, you're going soft!"
            n "Yep."
            b "Fine."
            b "I'm Laura!"
            b "I'm a bitch with an ass the size of two basketballs and tits that could produce a gallon each!"
            b "Oh!"
            b "Yessss."
        $ renpy.end_replay()

    else:
        scene bg black
        with fade
        "Laura's Graduation Party"
        scene grad1
        with fade
        pause
        l "Thanks for coming."
        n "Of course."
        n "I'm happy to be here to celebrate with you."
        scene grad3
        with dissolve
        l "You know I trust you, right?"
        l "I just don't trust any of these other girls."
        n "Justified, I suppose."
        scene grad2
        with dissolve
        l "So they aren't going to like it, but I'm going to be right here by your side."
        n "My bodyguard?"
        l "I'll protect you alright."
        scene lauragrad1
        with fade
        pause
        n "See? A little rum makes pepsi way better."
        l "I'll never doubt you again."
        scene lauragrad2
        with dissolve
        l "Hmm..."
        n "What?"
        scene lauragrad1
        with dissolve

        l "Something Jenn this way comes."
        scene jenngrad1
        with fade
        n "Hey!"
        j "Hey."
        n "What are you doing over there?"
        n "Come have a seat!"
        scene jenngrad2
        with fade
        pause
        n "How you been, girl?"
        j "Not bad."
        n "Has Laura been treating you well?"
        scene jenngrad3
        with dissolve
        n "Pretend she's not here."
        j "Laura has been a lot better."
        scene jenngrad4
        with dissolve
        j "She hasn't made my cry in months!"
        j "We are even going to take some of the same classes."
        n "Really?"
        j "Yeah, we both want to be fashion designers!"
        scene lauragrad1
        with dissolve
        n "Don't we all?"
        n "So Laura has been nice?"
        scene jenngrad4
        with dissolve
        j "For sure!"
        j "My only complaint is that she keeps you from us."
        scene jenngrad2
        with dissolve
        l "Aww!"
        l "Sorry."
        n "Well, it's good to see you, Jenn."
        scene jenngrad4
        with dissolve
        j "You too!"
        scene bg black
        with fade
        "{b}Ten Minutes Later{/b}"
        scene haleygrad1
        with fade
        pause
        n "Hey-ley!"
        h "Hi."
        scene haleygrad2
        with dissolve
        n "Congratulations on graduating!"
        h "Thanks."
        n "Join us for a minute?"
        scene haleygrad3
        with fade
        pause
        n "How are ya?"
        h "Good."
        n "Why are you so shy all of a sudden?"
        scene haleygrad4
        with dissolve
        h "I'll tell you when it's just the two of us."
        n "You can tell me."
        l "It's fine, [n]. She just wants to tell you she is in love with you."
        scene haleygrad3
        with dissolve
        "Haley blushed."
        scene haleygrad5
        with dissolve
        h "How would I be in love with him?"
        h "We only hung out a few times."
        scene haleygrad3
        with dissolve
        h "And now I haven't seen you in three months."
        n "Well, it's good to see you now."
        h "Likewise."
        h "But I hope it's not another three months before I see you again."
        scene bg black
        with fade

        "{b}Five Minutes Later{/b}"

        a "Holy shit, you're alive!"
        if leahf:
            scene ashleygrad1f
        else:
            scene ashleygrad1
        with dissolve
        n "And in the flesh!"
        a "I'm glad."
        if leahf:
            scene ashleygrad2f
        else:
            scene ashleygrad2
        with dissolve
        a "I was thinking maybe Laura forgot to feed you when she locked you in her basement."
        n "Nope!"
        n "But join us for a seat."
        if leahf:
            scene ashleygrad4f
        else:
            scene ashleygrad4
        with fade
        pause
        a "So there's a rumor that you won't even let him out of your sight."
        l "At this party? Yes."
        if leahf:
            scene ashleygrad5f
        else:
            scene ashleygrad5
        with dissolve
        a "So, no chance of having a private conversation, [n]?"
        n "I'm afraid not."
        a "That's too bad."
        if leahf:
            scene ashleygrad4f
        else:
            scene ashleygrad4
        with dissolve
        a "I was hoping to figure out how Laura tricked you into being with her."
        l "Ashley!"
        if leahf:
            scene ashleygrad5f
        else:
            scene ashleygrad5
        with dissolve
        a "I'm guessing she hypnotized you."
        if leahf:
            l "Ashley!"
            l "I know you're joking, but can you stop with the rumors?"
            scene ashleygrad4f
            with dissolve
            a "Your tits stopped growing."
            l "So did yours!"
            a "Only because of [n]."
            scene ashleygrad6f
            with dissolve
            a "Everyone else around here is starting to look like they are going to fall over."
            l "I don't have the watch."
            a "Well, if you do-"
            l "I don't."
            scene ashleygrad5f
            with dissolve
            a "-do the right thing."

        else:
            a "Laura, if you did, do me a favor."
            a "Use the watch to stop my tits."
            scene ashleygrad5
            with dissolve
            a "I've been eating less than twelve hundred calories a day and yet these things won't stop getting bigger."
            a "I don't want to have to get surgery, Laura."
            l "I don't have it."
            scene ashleygrad6
            with dissolve
            a "I'm serious. I give you full permission to hypnotize me."
        a "Anyway."
        a "It was good to see you, [n]."

        a "I wish things were different."
        if leahf:
            scene ashleygrad3f
        else:
            scene ashleygrad3
        with fade
        pause
        a "One more thing before I go..."
        a "Blink three times if you need us to rescue you."
        scene bg black
        with fade

        "{b}Twenty Minutes Later{/b}"
        if leah:
            if leahf:
                scene leahgradf1
            else:
                scene leahgrad1
            with dissolve
            L "Hey."
            n "Hey!"
            n "Why the long face?"
            L "I need to tell you something."
            n "Well, have a seat."
            if leahf:
                scene leahgradf2
            else:
                scene leahgrad2
            with fade
            pause
            n "What is it?"
            L "..."
            L "I don't want you to hate me."
            if leahf:
                scene leahgradf4
            else:
                scene leahgrad3
            with dissolve
            n "I won't."
            n "I promise."
            pause
            L "I'm pregnant."
            if leahf:
                scene leahgradf3
            else:
                scene leahgrad4
            with dissolve
            n "What?"
            l "And it's yours."
            n "How?"
            if leahf:
                scene leahgradf4
            else:
                scene leahgrad3
            with dissolve
            L "I think it was when I took antibiotics for my strep throat."
            L "I didn't know it could offset birth control."
            n "Holy shit."
            n "When was this?"
            if leahf:
                scene leahgradf5
            else:
                scene leahgrad5
            with dissolve
            L "Umm... two months ago, I guess?"
            L "Right before you went on your cruise with Laura."
            if leahf:
                scene leahgradf4
            else:
                scene leahgrad4
            with dissolve
            L "Remember?"
            "{i}She had strep throat a month ago.{/i}"
            "{i}It was right before I moved in with Laura.{/i}"
            n "Right."
            if leahf:
                scene leahgradf5
            else:
                scene leahgrad5
            with dissolve
            l "Why are you telling us now?"
            L "I wasn't sure what I was going to do."
            l "If you keep it you aren't getting any child support."
            l "Dad has great lawyers."
            if leahf:
                scene leahgradf4
            else:
                scene leahgrad4
            with dissolve
            L "No, that's not what this is about at all."
            l "Then what?"
            L "It's just-"
            if leahf:
                scene leahgradf1
            else:
                scene leahgrad1
            with fade
            pause
            L "I'm sorry."
            L "I was hoping all this would have ended differently."
            L "I just wanted you to know."
        else:
            if leahf:
                scene leahgradf1
            else:
                scene leahgrad1
            with dissolve
            L "Hey!"
            n "Hey! I heard you met your twin?"
            L "Yes! She was here a week ago."
            n "How did it go?"
            if leahf:
                scene leahgradf6
            else:
                scene leahgrad6
            with dissolve
            L "She was amazing!"
            n "Obviously. She's your twin."
            L "Aww! Thank you!"
            if leahf:
                scene leahgradf7
            else:
                scene leahgrad7
            with dissolve
            L "I miss you."
            L "We should all hang out again soon."
            l "Yeah, let's do that."
        scene lauragrad1
        with fade
        pause
        l "How you doin, champ?"
        l "We don't have to stay too much longer."
        l "But in the meantime...."

        if brittany:
            l "Do you want to go home and fuck my sister?"
        else:
            l "Do you want to take Grace in the back room and fuck her real quick?"


    if lifeboat:
        if leah:
            scene bg black
            with fade
            "{b}The Next Morning{/b}"
        else:
            jump toots
        scene blshowdown1
        with fade
        pause
        l "Hey."
        l "Leah is here."
        scene blshowdown3
        with dissolve
        l "She wants to talk to you."
        scene blshowdown4
        with dissolve
        pause
        "We went downstairs."
        if leahf:
            scene leahnewsf1
        else:
            scene leahnews1
        with fade
        pause
        L "Hey."
        n "Hey!"
        if lifeboat:
            n "How was the graduation party?"
            L "It was good."
        if leahf:
            scene leahnewsf2
        else:
            scene leahnews2
        with dissolve
        l "She has something to tell you."
        n "What is it?"
        if leahf:
            scene leahnewsf3
        else:
            scene leahnews3
        with dissolve
        pause
        L "I'm pregnant."
        n "What?"
        l "And it's yours."
        if leahf:
            scene leahnewsf4
        else:
            scene leahnews4
        with dissolve
        n "How?"
        L "I think it was when I took antibiotics for my strep throat."
        L "I didn't know it could offset birth control."
        if leahf:
            scene leahnewsf2
        else:
            scene leahnews2
        with dissolve
        n "Holy shit."
        n "When was this?"
        L "Umm... two months ago, I guess?"
        if leahf:
            scene leahnewsf1
        else:
            scene leahnews1
        with dissolve
        L "Right before you went on your cruise with Laura."
        L "Remember?"
        "{i}She had strep throat a month ago.{/i}"
        "{i}It was right before I moved in with Laura.{/i}"
        if leahf:
            scene leahnewsf3
        else:
            scene leahnews3
        with dissolve
        n "Right."
        l "Why are you telling us now?"
        L "I wasn't sure what I was going to do."
        l "If you keep it you aren't getting any child support."
        if leahf:
            scene leahnewsf5
        else:
            scene leahnews5
        with dissolve
        l "Dad has great lawyers."
        L "No, that's not what this is about at all."
        l "Then what?"
        if leahf:
            scene leahnewsf4
        else:
            scene leahnews4
        with dissolve
        L "It's just-"
        L "I'm sorry."
        L "I was hoping all this would have ended differently."
        if leahf:
            scene leahnewsf1
        else:
            scene leahnews1
        with dissolve
        L "I wanted you to know."
        pause
    label toots:
    scene bg black
    with fade
    "{b}Four Months Later{/b}"
    image lauranobra = Movie(play="lauranobra.webm")
    show lauranobra
    with fade
    pause
    l "My man!"
    l "Yes! Earn it!"
    l "Give me that good dick!"
    "She moaned loud enough for the whole house to hear."
    "I didn't mind."
    "It was our house."
    "After giving me a job, Laura's dad helped us by giving us the down payment."
    l "Where's my bra?"
    n "Who cares? Bras suck."
    l "My tits are starting to hurt from bouncing around!"
    n "Fine."
    n "After you cum, want to take it back to our room?"
    l "Lead the way."
    l "I already came twice."

    image laurabraon = Movie(play="laurabraon.webm")
    show laurabraon
    with fade
    pause
    l "It's official!"
    l "Every room in the house!"
    n "In one hour? You slut!"
    l "I love it."
    n "You love taking my dick?"
    l "You know I do."
    pause
    l "Holy shiiiiit!"
    pause
    scene laurabra1
    with fade
    pause

    n "How was that?"
    l "Alright, I'm confident you have nothing left in your balls."
    $renpy.end_replay()
    l "But I still don't know why you want to go see her."
    n "Because I'm the one responsible for her condition."
    scene laurabra2
    with dissolve
    l "No you aren't."
    l "She asked for it."
    l "It's not your fault she can't walk anymore."
    scene laurabra1
    with dissolve
    if bigtits:
        l "The other girls can still move."
        n "Barely!"
        n "Jenn can't fit through a doorway."
    else:
        n "It kind of is."
        l "Well at least the other girls finally stopped."
        n "There is that."

    scene laurabra3
    with dissolve
    l "Whatever. Go see her if you want to."
    n "Thank you."
    if preg:
        l "But first..."
    else:
        $ gracefuck = False
        jump haleyvisit
    l "Just to be safe, go fuck our roommate for me."
    n "Yes ma'am."
    if brittany:
        n "But which one?"
    label galleryScene63:
    l "GRACE!"
    g "Yeah?"
    l "Could you please take [n] off my hands?"
    if preg:
        scene gracepreg1
        with fade
        pause
        if glthreesome:
            g "Damn it, I was about to come make it a threesome."
            l "You snooze you loose!"
            g "So you're tapping out?"
            l "For now."
            scene laurabra3
            with fade
            g "You should have waited for me!"
        else:
            g "Oh, you're done fucking in my bed?"
            l "For now."
            scene laurabra3
            with fade

        g "You just get off on pissing me off, don't you?"
        l "Yes. But we wanted to fuck in every room in the house."
        g "I thought you did that the day you moved in."
        l "We did. But we wanted to do it in one hour."
        l "And at least one of us had to cum each time."
        scene gracepreg1
        with fade
        g "So that's why there's this trail of semen on the hardwood?"
        if glthreesome:
            g "Next time we are doing it with the three of us."
            l "Hell yeah that would be even better."
            n "And we all have to take a shot each time."
            g "Well played."
        g "So glad I came to live with you guys."
        l "Wait, so why are you naked, anyway?"
        scene gracepreg2
        with dissolve
        g "Why wouldn't I be?"
        g "It's hot."
        l "Whatever."
        l "Will you take [n] now? I'm trying to make sure he can't cum anymore."
        scene gracepreg3
        with dissolve
        g "I already did that this morning."
        scene gracepreg4
        with dissolve
        if jennmean:
            g "Come with me, boyfriend."
        else:
            g "Come with me, enemy."
        scene gracepreg5
        with dissolve
        l "Hey! Where are you going?"
        l "Stay out of the dining room!"
        l "That's where we eat!"
        g "You're one to talk."
        l "I just need a snack. Gotta feed the baby."
        scene leavegrace
        with fade
        pause
        g "I'm ready!"
        menu:
            "Fuck Grace":
                $ gracefuck = True
                jump fuckgracehere
            "Leave [blue]\[Haley Visit\]":
                $ gracefuck = False
                n "Sorry girl, but I'm tapped out."
                n "I'm going to run."
                scene bg black
                with fade
                g "Aww."
                n "Tell Laura I fucked you, okay?"
                g "Totally."
                jump haleyvisit
        label fuckgracehere:
        image gracepreg = Movie(play="gracepreg.webm")
        show gracepreg
        with fade
        pause
        g "You sure you're still- uh!"
        g "-okay with me living here?"
        n "I love having you live with us."

        if lifeboat:
            g "Oh, that's what you love, huh?"
            n "And I love you."
            g "I love you too."
            g "Now fuck me like you mean it."
        else:
            g "Oh, that's what you love, huh?"
            n "And I love your pussy."
            g "You big romantic."

        pause
        g "Hey, you know how sex this morning was pretty epic?"
        n "I recall."
        g "How is this even better?"
        n "Hormones?"
        g "I know how to make it even better than this."
        n "I'm listening."
        image gracetable = Movie(play="gracetable.webm")
        show gracetable
        with fade
        pause
        g "OH FUCK YES!"
        g "Shit! You're leaking out of me!"
        g "Oh no! It's all over where Laura sits to eat!"
        n "Future mother of my child right here."
        pause
    else:
        g "Of course."
    $renpy.end_replay()
    label haleyvisit:
    scene bg black
    with fade
    "{b}An Hour Later{/b}"
    scene haleymom1
    with fade
    pause
    "Debbie" "Come on in!"
    "Debbie" "She is going to be so happy to see you."
    "Debbie" "Haley really loves it when she has visitors!"
    scene haleymom2
    with dissolve
    "Debbie" "The past month she really hasn't been able to leave the house."
    "Debbie" "Her room is down to the right."
    n "Thanks."
    scene haleyhuge1
    with fade
    pause
    n "Hey Haley!"
    scene haleyhuge2
    with dissolve
    pause
    h "Hey."
    n "How's it going?"
    h "Not too bad."
    h "Come have a seat!"
    scene haleyhuge3
    with fade
    pause
    h "Did you bring me anything to eat?"
    n "I'm sorry."
    n "Your parents won't let me."
    h "Next time bring a jacket so you can sneak me in some candy."
    n "You got it."
    n "How are you?"
    scene haleyhuge4
    with dissolve
    h "I'm okay."
    if bigtits:
        h "I guess this is my life now."
        scene haleyhuge5
        with dissolve
        h "The doctors say I will need to have surgery soon while I can still fit through a door, one breast at a time."
        n "Makes sense."
    else:
        h "I keep thinking I'll stop growing like the other girls."
        scene haleyhuge5
        with dissolve
        h "But no such luck."
        n "I'm sorry."
    h "So you're still with Laura, huh?"
    n "Yep."
    scene haleyhuge3
    with dissolve
    h "Does she make you happy?"
    n "I guess so."
    h "Ever cheat on her?"
    n "Well, Grace doesn't count."
    if brittany:
        n "Or her sister."
        scene haleyhuge4
        with dissolve
        h "Her sister?"
        h "I didn't hear about that."
    scene haleyhuge6
    with dissolve
    n "How's Jenn?"
    h "She's pretty good."
    h "Not nearly as big as me."
    h "But she's getting there."
    scene haleyhuge4
    with dissolve
    h "Did you get the pictures she sent you?"
    n "I don't really have a phone-"
    h "I know. She sent them in the mail."
    n "No."
    scene haleyhuge5
    with dissolve
    h "Figures. Laura must have found it."
    h "Jenn sent me a copy with some notes to make me feel better."
    scene haleyhuge6
    with dissolve
    h "Want to see them?"
    menu:
        "[gr]Sure":
            n "Sure."
            h "Here."
            scene jennmissyou
            with fade
            pause
            n "Damn."
            h "Right?"
            h "Still hot."
            n "I'll say."
            h "Keep going."
            scene jennmissya
            with fade
            pause
            h "Is that the one she took when she was smaller?"
            n "Yeah."
            h "Kind of crazy, right?"
            h "There's more."
            scene jennmissyou2
            with fade
            pause
            n "It was nice of her to think of you."
            h "Pretty sure it was you she was thinking of there."
            scene jennmissyou3
            with fade
            pause
            n "Wow."
            h "The one where she is bent over?"
            h "Yeah, that's my favorite."
            scene haleyhuge3
            with fade
            pause
        "No thanks":
            h "Wow, you really are whipped, huh?"
    h "So..."
    h "I know you like big boobs."
    scene haleyhuge7
    with dissolve
    h "But this is too big, even for you, right?"
    menu:
        "No":
            n "The bigger the better."
            h "I'm glad you think so."
            scene haleyhuge6
            with dissolve
            h "But I know you're just being sweet."
            h "Either way, you know my ass has kept growing too, right?"
            n "I suspected."
            h "Want me to stand up and show you?"
            menu:
                "[gr]Sure":
                    n "Sure."
                    scene haleyhuge8
                    with dissolve
                    h "You really do like thick girls, huh?"
                    n "What gave it away?"
                    n "Holy shit."
                    h "I know. I'm huge."
                    if hcum:
                        scene haleyhuge10
                        with dissolve
                        h "Can I confess something?"
                        n "Of course."
                        h "The reason I kept eating..."
                        h "It wasn't just depression."
                        scene haleyhuge9
                        with dissolve
                        h "A part of me was also hoping you would like it and leave Laura for me."
                        n "Haley, you didn't have to-"
                        h "I'm not blaming you."
                        h "And I know you aren't going to leave her, and that you would never want to be with only one girl."
                        h "But you know..."
                        scene haleyhuge11
                        with dissolve
                        h "You could totally fuck me right here."
                        h "You are the only one I know with a dick long enough for my big ass."
                        h "And in case you forgot what it looks like..."
                        scene haleyhuge8
                        with fade
                        pause
                        h "...here it is again, as a reminder."

                        if gracefuck:
                            n "Tempting."
                            n "But I'm afraid I'm tapped out."
                            scene haleyhuge9
                            with dissolve
                            pause
                            h "Shit."
                        else:
                            n "Holy shit."
                            h "Oh yeah?"
                            h "I've fantasized about you taking me from up against the wall."
                            menu:
                                "Fuck her":
                                    n "Show me."
                                "Turn her down":
                                    n "I'm sorry, Haley."
                                    h "Really?"
                                    h "I thought I had you convinced."
                                    scene haleyhuge9
                                    with dissolve
                                    jump haleyhugeno
                            scene bg black
                            with fade
                            h "...like this."
                            scene haleyhuge15
                            with fade
                            pause
                            n "Holy shit."
                            h "What are you waiting for?"
                            h "Take me!"
                            menu:
                                "Fuck her":
                                    n "My pleasure."
                            image haleyhuge = Movie(play="haleyhuge.webm")
                            show haleyhuge
                            pause
                            h "HOLY FUCK!"
                            n "Your mom-"
                            h "I don't care!"
                            h "This is all I've wanted for the past four months!"
                            h "Your dick feels so good!"
                            h "Yes yesssss YESSS!"
                            pause
                            h "Don't you dare pull out!"
                            h "I need to feel you inside me!"
                            h "Cum! Cum with me!"
                            h "Oh! I can feel it!"
                            with hpunch
                            h "THAT FEELS SO GOOD!"
                            with hpunch
                            h "AHH!"
                            with vpunch
                            h "So fucking good!"
                            pause
                            scene haleyhuge12
                            with fade
                            pause
                            n "Did that hold up anywhere close to your fantasy?"
                            h "Above and beyond."
                            scene haleyhuge13
                            with fade
                            pause
                            h "Did I hold up to yours?"
                            n "You have no idea."
                            h "I'm glad to hear it."
                            h "I need to sit back down."
                            scene haleyhuge14
                            with fade
                            pause
                            h "So will you come back and see me again?"
                            n "I-"
                            h "I'll do anything you want."
                            h "I'm your toy."
                            pause
                            jump haleyend


                    else:
                        scene haleyhuge9
                        with dissolve
                        h "I'm just glad someone could appreciate me."
                        n "Girl..."
                "No thanks":
                    label haleyhugeno:
                    n "No thanks."
                    h "Okay."

        "Yes":
            n "I mean..."
            h "Yeah."
    scene haleyhuge10
    with dissolve
    h "Well, I hope you're happy with her."
    h "I hope she doesn't drive you crazy."
    n "That's what marriage is."
    h "I guess so."
    scene haleyhuge9
    with dissolve
    h "But isn't that not supposed to start until you're actually married?"
    n "I guess."
    n "Anything I can do for you?"
    h "Just the obvious answer."
    scene haleyhuge11
    n "Find the watch?"
    h "And make me shrink back down again."
    h "At least to the point where I could walk for longer than it takes to go to the bathroom."
    h "I can't even stand up for a full shower anymore."
    scene haleyhuge10
    with dissolve
    if lifeboat:
        h "Hey, [n]?"
        n "Yeah?"
        h "You know what I'm going to say."
        n "Say it anyway."
        scene haleyhuge9
        with dissolve
        if haley:
            h "I still love you."
        else:
            h "This isn't your fault."
            n "It kind of is."
            h "Yeah, well, I'll survive."
            h "Thanks for checking up on me!"
            n "My pleasure."

    else:
        n "Can I ask you something?"
        h "Of course."
        n "What were you going to tell me at the graduation party?"
        scene haleyhuge9
        with dissolve
        h "Oh that?"
        if haley:
            h "Laura was right."
            h "I was going to tell you that I loved you."
            n "Do you still?"
            h "Yes."
            pause
        else:
            h "I don't blame you for this."
            h "I asked for it."
            n "That's very mature of you."
            h "Thanks for checking up on me."
            n "My pleasure."
    if bigtits:
        h "Hey, before you go."
        h "Do you want to see them?"
        n "Really?"
        scene haleyhuge10
        with dissolve
        h "Why not? You made them."
        menu:
            "[gr]Sure":
                n "Sure."
                h "Okay!"
                h "Close your eyes."
                n "Do I have to?"
                scene bg black
                with fade
                h "Let me get this off..."
                scene haleyhuge14
                with fade
                pause
                h "Tah-dah!"
                n "Holy fuck!"
                h "Right?"
                h "Now think of me whenever you are fucking her."
                pause

            "No thanks":
                n "No thanks."
                scene haleyhuge9
                h "Hey, I offered."
                h "Come back soon, okay?"
                h "But bring candy."

    label haleyend:
    scene bg black
    with fade
    $renpy.end_replay()
    pause
    centered "Thanks for playing the ending!"
    if finished:
        "Would you like to return to play a different ending, or would you rather replay this ending with different variables?"
        menu:
            "Take me back to the endings page":
                jump endings
            "Explore more options":
                jump moreoptionscruise
    if ashleyswallow:
        label moreoptionscruise:
        if glthreesome:
            scene bg black
            with fade
            "This ending had two variations based on choices in previous episodes."
            "The first path is based on you getting with Grace and Laura both in Laura's hot tub in Episode Six."
            "This is the version you just played, because you are good at this game and probably life."
            "The second path is based on you getting with only one of the girls in Episode Six."
            "In this option you would spend the cruise sneaking off and hooking up with Grace behind Laura's back."
            "If you are only planning on playing through once, the path you just finished had the most content."
            "But if you do want to play the other path..."
            "Instead of making you go all the way back to Episode Six to enjoy both of them, you can play it now."
            "Or head back to the choice of dating Laura and turn her down if you want to continue the main storyline."
            menu:

                "Replay the ending with the other path":
                    $ glthreesome = False
                    jump yeahyeahyeah
                "Head back to the main storyline":

                    jump timetraveler
                "Main menu":
                    return
        else:
            scene bg black
            with fade
            "This ending has two variations based on choices back in Episode Six."
            "The first path is based on you getting with Grace and Laura both in Laura's hot tub."
            "This option has you, Laura and Grace all hooking up the entire cruise instead of hooking up behind Laura's back."
            "The second option is based on you getting with only one of the girls in Episode Six."
            "This is the version you just played."
            "The main difference in scenes is that you have the chance to hook up with Kassie in the other version."
            "Instead of making you go all the way back to Episode Six to enjoy both of them, you can play it now."
            "Or head back to the choice of dating Laura and turn her down if you want to continue the main storyline."

            menu:

                "Replay the ending with the other path":
                    $ glthreesome = True
                    jump yeahyeahyeah
                "Head back to the main storyline":
                    jump timetraveler
                "Main menu":
                    return
    jump end

# ------------------------------------------ BE Ending --------------------------------------------------------------

label skiptobending:
    if nowatch:
        "This ending takes place when Laura confronts you at the gym."
    else:
        "This ending takes place on a path where Laura recovered the watch back in Episode Ten."
        "In this path, you would have met up with Brittany at the bar and avoided looking at the video."
        "From there you would get the girls together to go to Laura's house to take the watch back."
        "However, once you recovered the watch, Laura texted Leah and commanded her to steal the watch back and bring it to her."
        "Much of the story remained the same with Laura disappearing."
        "At the end of Episode Thirteen you went to the gym to attempt to find a way to hypnotize the girls without needing the watch."
        "You had the idea to use the video of Laura hypnotizing Leah and Ashley since it worked on Grace when she watched it."
        "To be safe, you first took the precaution of muting the audio and cropping out Laura."

    scene bg black
    scene gymani1
    with fadehold
    pause
    a "So, I'm ready."
    a "What about you girls?"
    j "Ready."
    n "Okay, I'm going to pull out the video."
    n "By the way, it didn't work on me earlier-"
    g "What!"
    g "Then why did we just spend fifteen minutes talking about it instead of testing it?"
    n "Uhh..."
    "I held up my phone and played the video."
    a "Umm..."
    n "It's not working?"
    n "Here, let me bring it closer to you guys..."
    scene bg black
    scene gymani2
    with dissolve
    n "Oh!"
    n "Did it work?"
    pause
    with vpunch
    l "Not exactly."
    with vpunch
    scene bg black
    image gymlaurani2 = Movie(play="gymlaurani2.webm")
    scene gymlaurani2
    with fade
    pause
    n "SHIT!"
    n "Where the fuck-"
    l "Girls, you will listen to me and not [n]."
    scene bg black
    image gymlaurani1 = Movie(play="gymlaurani1.webm")
    scene gymlaurani1
    with dissolve
    pause
    l "Hi, [n]."
    l "Did you miss me?"
    pause
    n "I-"
    l "Look, I'm here to apologize."
    n "Then why are you-"
    l "I know what you want."
    l "Or at least, I know what you {i}really{/i} want."
    n "I want my watch back."
    n "It belonged to my grandfather and I'm very sentimental."
label redolaura:
    l "Relax, [n]."
    l "I'll give it back to you."
    l "Under two conditions."
    n "And they are?"
    l "First, that you let me command the girls something."
    menu:
        "Allow it":
            n "I'll allow it."
            l "Good!"
            l "Wait, I thought you were here to play the new content?"
            n "I mean..."
            pause
            centered "Rewinding"
            centered "..."
            jump redolaura
        "Cut her off (choose this to continue the ending)":
            n "Fuck no."
            n "Laura, there's no chance of us being together."
            l "I know you think that now, but-"
            n "No."
            n "I'm telling you right now that things are over between us."
            n "Do you understand?"
            l "But-"
            l "Don't you want the watch back?"
            n "Oh, you aren't leaving here without it."
            pause
            l "Please."
            n "I'm not going to lie to you."
            n "And I'm not playing your stupid games."
            n "Give me my watch, Laura."
            scene bg black
            with fade
            "She looked at the ground as she reached for her pocket."
            "I held out my hand."
            "She took a step, putting all her effort into throwing my watch as hard as she could."
            "I watched helplessly as it hit the wall and exploded into a cloud of dust."
            "There was nothing left."
            scene bg black

            scene gymlaurani1
            with fade
            pause
            n "Fuck!"
            "I glared at her."
            n "At the very least, you need to command these girls' boobs to stop growing."
            l "Fine."
            scene bg black
            scene gymlaurani2
            with dissolve
            pause
            l "You are all no longer addicted to [n]."
            l "I free you!"
            l "And that is all."
            l "Now, wake up, bitches."
            "The girls all looked around with various degrees of surprise and confusion."
            scene bg black
            scene gymaniu1
            with fade
            pause
            a "What-"
            l "Hey, ladies."
            l "[n] just guaranteed that you are all going to need parachutes for bras."

            l "Good luck finding wheelbarrows to keep you mobile."
            scene lauragym1
            with fade
            pause
            l "Laura out."
            scene bg black
            with fade
            "I debated running after her before realizing there was no point."
            "My watch was gone."
            scene gymaniu1
            with fade
            pause
            g "That cunt."
            j "Grace!"
            g "What happened, [n]?"
            n "She snuck up behind me when I was showing you all the video."
            n "Out of curiosity, did the video work?"
            g "Not for me."
            j "No."
            L "I don't think so."
            n "Shit."
            a "Why?"
            n "Because she just threw my watch against the wall."
            n "I told her to at least stop your boobs from growing but she refused."
            n "But at least she commanded you to no longer be addicted to me before waking you all up."
            a "That's something."
            h "Still."
            h "What a cunt."
            g "Girl! You and I need to hang out more."
            L "So... what do we do now?"
            n "Can you try this video one more time?"
            scene bg black
            with fade
            "I played the video as I held it up in front of her."
            scene gymalaniu
            with fadein
            pause
            L "I don't feel any different..."
            n "Leah, your boobs will now stop growing."
            L "Yeah..."
            L "I really hope so."
            L "Or we are in for a wild ride."
            scene bg black
            with fadeout
            pause
            with fade
            centered "The Broken Watch"
            with fade
            centered "Or..."
            with fade
            centered "The Tig Ol' Bitty Ending"
            with fade

label bending:
    centered "This update assumes you are currently dating the main girls."
    with fade
    centered "This includes Leah, Ashley, Jenn and Grace."
    with fade
    pause
    "{b}Four Days Later{/b}"
    scene market1
    with fadein
    pause
    "I called Grace."
    g "Hey! We're on our way!"
    n "Cool."
    n "Hey, I'm at the store picking up some groceries."
    g "Why? I thought we were going out for dinner."
    n "This is for breakfast."
    g "Oh! Good idea."
    scene market2
    with dissolve
    n "Do you want any snacks?"
    g "[n]! You know we are trying to cut calories."
    n "There are healthy options."
    g "But healthy snacks suck."
    n "I guess you've never had avocado toast."
    g "Really, [n]?"
    scene market3
    with dissolve
    g "You are talking to me about avo-calorie toast?"
    n "But it's the good fats."
    g "That's the kind my tits love!"
    g "Tossing it on carbs? Great idea."
    n "There are some corn dogs here..."
    g "No!"
    scene market5
    with dissolve
    n "Pizza pockets?"
    g "You're killing me!"
    n "Alright, I'm picking up breakfast meat."
    g "Just get some chicken sausage."
    scene market4
    with dissolve
    n "Sounds good."
    g "Alright, see you in a few."
    "I hung up."

    "{i}Alright. Which direction to go?{/i}"
    menu:
        "Chicken sausage":
            $ bacon = False
            "{i}Here we go.{/i}"
            "{i}I don't want the girls thinking I'm trying to make them any bigger.{/i}"
        "Bacon [gr]\[Huge breasts\]":
            $ bacon = True
            "{i}You can't mess up bacon.{/i}"
            "{i}But I'll also grab some chicken sausage.{/i}"
            "{i}And some snacks, obviously.{/i}"
    scene bg black
    with fadeout
    pause
    "{b}Thirty Minutes Later{/b}"

    scene jgentrance1
    with fadein
    pause
    n "Ladies."
    n "You made it!"
    scene jgentrance2
    with dissolve
    pause
    g "Barely."
    if jenn:
        j "[n]!"
        scene jgentrance3
        with dissolve
        "I threw my arms around Jenn and she gave me a big kiss."
    pause
    scene jgentrance4
    with dissolve
    "When I reached for Grace she seemed to pull her face back, so I only gave her a hug."
    pause
    scene jgentrance5
    with dissolve
    pause
    g "Hey."
    n "Did you run into troubles?"
    g "Hey, is that Big Titty Goth Girl?"
    image jgentranceani = Movie(play="jgentranceani.webm")
    scene jgentranceani
    with fade
    "Girl" "Wait, you told them about me?"
    n "Of course."
    g "Do you have a name?"
    "Girl" "Lydia."
    g "Nice to meet you."
    lyd "You must be Leah and Ashley."
    g "Afraid not."
    lyd "Oh."
    lyd "Shit."
    g "I'm Grace, and this is Jenn."
    lyd "Nice to meet you."
    j "You too."
    g "I like your tits."
    lyd "Thank you?"
    g "I don't think my back could support anything that size."
    g "But they are lovely."
    lyd "Yeah, they can be a hassle."
    lyd "But I love them."
    g "That's good."
    g "Because I can't seem to stop growing."
    lyd "I know the feeling."
    lyd "But one day, you will."
    j "Doubt it."
    lyd "Why's that?"
    j "We have... a condition."
    lyd "Macromastia?"
    j "More like gigantomastia."
    lyd "Is that a thing?"
    j "I guess we'll have to find out."
    lyd "Why's that?"
    g "Because every time we suck [n]'s dick, we grow a bit more."
    g "And we can't seem to stop."
    lyd "Interesting."
    g "Would you?"
    lyd "Would I what?"
    g "Would you go bigger if you could?"
    "Lydia was speechless for the first time I knew of."
    lyd "Uhh..."
    g "It's okay, you can tell us."
    g "I know that most girls wouldn't want to admit it in front of polite society."
    g "But you seem like the kind of girl that isn't afraid to show her true colors."
    lyd "Would I have to suck [n]'s dick?"
    g "Sure."
    lyd "Then... no."
    g "Ha!"
    g "Burn!"
    g "Come on, [n]."
    g "Let's go upstairs and give you a double BJ."
    n "Uhh..."
    lyd "Have fun."
    scene jgentrance6
    with fade
    pause
    g "She totally wants to suck your dick."
    n "Pretty sure she heard you."
    g "I'm aware."
    scene aptdoor1
    with fade
    g "So this is it?"
    n "Yep."
    g "The infamous [n] party pad?"
    n "Yep."
    g "Well, are you going to let us in?"
    scene apt1
    with fade
    n "And here we have the entrance."
    n "It's okay if your pants fall off."
    scene apt2
    with dissolve
    g "Nice place."
    n "Thanks."
    scene apt3
    with dissolve
    j "You really haven't been here before?"
    g "No."
    j "I thought you were pulling my leg."
    scene apt4
    with fade
    n "So how was your ride over?"
    g "A couple of guys were staring at us the entire time."
    g "It was creepy."
    image jgaptani2 = Movie(play="jgaptani2.webm")
    scene jgaptani2
    with fade
    j "I'm going to get some pepper spray."
    n "Then I'm glad you came together."
    n "Girl power and all that."
    g "Right."
    g "So what did you guys do last weekend?"
    n "Nothing much."
    j "We went out for pizza."
    g "And?"
    if jennice:
        n "Dessert."
        j "[n]!"
    else:
        j "Dessert."
    g "Sure, sure."
    g "Then you came back here and kept each other up all night?"
    n "Nooooo?"
    g "Right, right."
    g "So you didn't get to explore the city much."
    g "We can do that tonight!"
    g "Maybe go out to a club?"

    j "You want to go dancing?"
    g "Why not?"
    j "I was thinking we could just stay here."
    j "Order some pizza."
    n "There's more to life than pizza, Jenn."
    if jennice:
        g "Like dick?"
        j "Grace!"
    else:
        j "Like dick?"
        g "Jenn!"
    "I laughed."
    g "Alright. Where's the bathroom?"
    n "I believe in you."
    g "You're no help!"
    scene bg black
    with fade
    "Grace went exploring."
    scene apt5
    with fade
    n "So..."
    n "Are you two getting along?"
    scene apt6
    j "Yeah, we have been having fun."
    j "It's a bit weird, her going from bullying me to trying to be my best friend in a couple of weeks."
    scene apt5
    n "Did she actually bully you?"
    scene apt6
    j "She didn't stop it from happening."
    scene apt5
    n "Hmm."
    n "Do you trust her?"
    scene apt6
    j "I trust her as much as I need to."
    j "I don't get bothered by things the same way anymore."
    scene apt5
    n "That's good."
    scene apt6
    j "So...."
    j "Think I could blow you before she gets back?"
    scene apt5
    n "Pretty sure you could just take off your top and I'd start blasting."
    scene apt6
    j "Really?"
    j "Shall we try?"
    scene apt7
    with fade
    pause
    n "Damn."
    scene apt8
    j "You like?"
    scene apt7
    n "I-"
    g "Jenn!"
    g "You have your tits out already?"
    g "We just got here!"
    scene apt9
    with dissolve
    pause
    n "That took too long if you ask me."
    n "In fact, I should instigate a naked rule."
    scene apt10
    g "You first."
    scene apt9
    n "Yeah?"
    j "But Grace!"
    scene apt11
    with dissolve
    j "You are the one that wants to go out."
    j "If we do that, I'm going to need some love."
    scene apt12
    g "Now, Jenn, we talked about this."
    g "You shouldn't confuse love with sex."
    scene apt11
    j "We did?"
    scene apt12
    g "There's a difference between [n] loving you and him loving to fuck you."
    scene apt11
    n "Grace!"
    n "I thought you were done with bullying."
    scene apt12
    g "[n]."
    scene bg black
    image jgaptani1 = Movie(play="jgaptani1.webm")
    scene jgaptani1
    with fade
    g "There is more than one kind of bullying."
    g "Leading a girl on while still fucking all of her friends is one of them."
    n "She is fully aware-"
    g "Oh, I know."
    g "We all are."
    g "But we are going to be stuck with you."
    if hcum:
        g "And do you really think you can take care of five girls?"
    else:
        g "And do you really think you can take care of four girls?"
    n "I've been doing pretty good so far."
    g "Then why have you only given me dick once in almost two weeks?"
    n "What are you talking about?"
    n "You got like five rounds!"
    j "I really don't want to hear this."
    g "It doesn't count when you don't leave the bed!"
    n "We did! There was your entranceway, the staircase, the-"
    j "La la la la!"
    g "I'm just saying."
    g "You have never taken me out on a date."
    n "What?"
    n "Sure I have."
    g "Oh yeah?"
    n "We went to the park..."
    g "Where you fucked me in the dirty ass public bathroom."
    n "We went for coffee-"
    g "Same."
    n "Huh."
    n "Crap."
    n "Alright, let's go out to dinner."
    j "Without me?"
    n "Of course not."
    g "I don't mind sharing."
    g "But I still want a date."
    g "And it includes dancing."
    n "Deal."
    if jennice:
        g "And I'll blow you under the table."
        n "Perfect."
    else:
        g "And Jenn can blow you under the table."
        n "Perfect."
        j "Hey!"

    n "Anyway."
    n "So how's Haley?"
    j "I haven't heard back from her yet."
    n "What do you think the doctors will say?"
    j "I don't know."
    j "But I'm glad one of us is going to get checked out."
    g "Yeah, I hope they find a way to stop us from growing."
    j "Or at least slow us down."
    n "Maybe the command will wear off."
    g "You think?"
    n "Maybe when Laura broke the watch it broke the spell."
    g "Then why have I gained another two cup sizes since then?"
    n "That's a good point."
    g "And even Jenn looks bigger."
    j "What?"
    j "Okay, just a little bit."
    j "Now I'm happy where I'm at."
    j "Honest."
    g "Then are you going to stop eating every meal like it's your last?"
    j "Are you?"
    g "...shut up."
    scene bg black
    with fade
    pause
    "{b}An Hour Later{/b}"
    scene bg black
    image gdinnerani1 = Movie(play="gdinnerani1.webm")
    scene gdinnerani1
    with fadein

    g "So..."
    g "How was your week?"
    n "Not too shabby, considering."
    n "You?"
    g "Almost done with school, so that's a relief."
    n "I bet!"
    pause
    g "Is this why we haven't gone on a real date before?"
    n "Why?"
    g "Are we boring?"
    n "Us?"
    g "If someone was watching us, we might be entertaining from afar."
    g "You never know what we're going to do next."
    g "Are we going to fuck in the bathroom?"
    n "Or are we going to dine and ditch?"
    "Waiter" "Ahem."
    n "Uhh..."
    n "Sorry."
    n "Bad joke."
    "Waiter" "I'm just checking in."
    "Waiter" "Your third is still using the restroom?"
    n "Yeah, but I can order for her."
    "Waiter" "Of course. For the lady?"
    g "I'll have the chicken cajun pasta."
    "Waiter" "Of course. And for the other lady?"
    n "We'll have a large pepperoni pizza."
    "Waiter" "Of course."
    n "Uh... with pineapple."
    "Waiter" "Any drinks?"
    g "I'll have a margarita."
    "Waiter" "May I see your ID?"
    g "Water is fine."
    "He walked off."
    n "Boring, huh?"
    n "So what would your idea of a fun date be?"
    g "I don't know."
    g "I've never been on a real date, I guess."
    n "So you are comparing real life to a movie?"
    g "I guess?"
    n "So you must be pretty disappointed that we've been sitting here for twenty minutes and no one around us has proposed."
    pause
    g "Shut up."
    n "We are about five minutes past a car exploding outside and Batman tackling the bank robbers."
    g "I know!"
    g "Unrealistic expectations, I get it."
    g "I'll try to enjoy myself more."
    n "Glad to hear it."
    n "What can I do to make you enjoy your evening more?"
    g "Your attention would be nice."
    n "You have it."
    g "Do I?"
    n "Of course."
    n "It's just you and me sitting here."
    g "So nothing else is distracting you right now?"
    n "Nope."
    g "Not even Jenn underneath the table with her lips wrapped around your cock?"
    n "Oh, that?"
    n "I forgot she was there."
    g "Your face says otherwise."
    n "I have a perfect poker face."
    g "I've seen you cum, [n]."
    g "I know when you are getting close."
    n "How about right now?"
    g "You look like you're about thirty seconds away."
    n "You're good."
    n "Hey, Jenn?"
    "There was a popping sound."
    j "Yes?"
    n "Don't swallow all of it."
    j "Okay."
    pause
    g "What are you planning?"
    n "You'll see."
    n "Right now, Jenn has me right on the edge."
    n "She has become a damn fine cock sucker."
    g "As good as me?"
    n "In her own way, yes."
    n "You both have different styles..."
    n "But you're both great in your own way."
    g "Very pragmatic answer, [n]."
    g "Are you planning on running for office?"
    g "But I know you think I'm better."
    g "If you don't, keep a straight face for the next ten seconds."
    n "Sure."
    "I did my best not to react."
    "But Jenn's tongue worked its magic and I was soon blasting a full load into the back of her throat."
    with vpunch

    g "Ha!"
    with vpunch
    g "I win!"
    n "Technically, Jenn won this one."
    scene jgdinner1
    with fade
    g "What! No fair."
    n "Good girl."
    scene jgdinner2
    with dissolve
    n "Did you do what I told you?"
    j "Mmm hmm."
    n "Excellent."
    n "Now, kiss Grace."
    scene jgdinner3
    with fade
    g "What?"
    g "No!"
    scene jgdinner4
    with dissolve
    g "Ah!"
    n "That's it."
    n "Share the load."
    n "How's this for a boring date?"
    g "Mmmm."
    n "Yeah, lick her face clean."
    n "She's a good kisser, isn't she?"
    g "Hmm."
    n "Who is the better kisser, you ask?"
    n "Well, I don't know."
    n "Jenn has kissed me several times since she got here."
    scene jgdinner5
    with dissolve
    n "But Grace hasn't kissed me in..."
    g "You're the one that hasn't kissed me, asshole."
    n "Is that it?"
    scene bg black
    scene gdinnerani1
    with fade
    g "Yes."
    g "I'm not Jenn."
    g "You have to come to me."
    g "No offense, Jenn."
    n "Interesting."
    n "I didn't think you were the game playing type."
    g "I'm not."
    g "But sometimes I want to be chased."
    g "Don't you want to be treated special, Jenn?"
    j "Of course."
    g "You can't treat us the same, [n]."
    g "Because we are different people."
    n "Fair point."
    n "So what do you want, Grace?"
    g "..."
    g "I don't want to say."
    j "Come on!"
    j "You can tell us."
    n "I genuinely want to know."
    g "It's stupid."
    n "Tell me."
    g "I want to be on your arm."
    g "I want to sit next to you and... {p}I want everyone to know that I'm your girl."
    n "Sounds good to me."
    n "Is that alright with you, Jenn?"
    j "Of course!"
    j "Get over there."
    scene bg black
    image gdinnerani2 = Movie(play="gdinnerani2.webm")
    scene gdinnerani2
    with fade
    n "How's this?"
    g "It's nice."
    pause
    g "You must think I'm an idiot."
    n "You're a girl."
    n "And you're {i}my{/i} girl."
    n "Sometimes you want your man to show you off."
    "She smiled."
    n "Hey, Grace?"
    g "Yeah?"
    n "Thanks for telling me."
    g "Of course."
    n "And Jenn, what would you like tonight?"
    g "Yeah, Jenn."
    g "I don't mean to hijack the night."
    j "No, it's fine."
    j "I'm on a cum high right now anyway."
    n "So?"
    j "If I could have my way..."
    j "We would skip the dancing."
    g "We know."
    n "And what would we do instead?"
    j "Have you ever swam in the pool in the apartment?"
    n "I have not."
    g "Ohh! Yes!"
    g "I'm down for that!"
    g "As long as I get a massage."
    n "Yeah?"
    g "These boobs are starting to hurt."
    n "That's the nice thing about water."
    j "Yeah?"
    n "It makes your tits weightless."
    g "Mmm."
    g "But I still want a back rub."
    n "And you both shall get one."
    j "Yay!"
    g "Alright, I'm convinced."
    g "Plus, I want Jenn to have fun too."
    n "Excellent."
    j "Oh! Here comes the waiter!"
    "Waiter" "Welcome back, Miss."
    j "Thanks."
    "Waiter" "I wanted you to know that your food will be out shortly."
    "Waiter" "And I don't mean to be rude, but you have something on your chin there."
    j "Wha-"
    j "[n]!"
    scene bg black
    with fadeout
    pause
    label galleryScene66:
    "{b}An Hour Later{/b}"
    scene bg black
    image jgpoolani1 = Movie(play="jgpoolani1.webm")
    scene jgpoolani1
    with fadein

    j "This is nice."
    j "Are you sad we didn't go dancing, Grace?"
    g "I'll deal."
    g "As long as we go tomorrow night."
    j "I'll go!"

    g "Then I have no complaints."
    g "This is pretty perfect."


    j "So, Grace. Did you get enough face time with [n] on the way home?"
    g "I don't know what you're talking about."
    j "Oh yeah?"
    j "No idea why it took us thirty minutes to walk two blocks?"
    j "Don't remember stopping to make out with [n] every three feet?"
    g "Nope."
    j "My mistake."
    n "Alright, ladies."
    n "Who wants a back rub first?"
    g "I'm good for now."
    g "You were right about them feeling weightless."
    n "Jenn?"
    j "Why not."
    scene bg black
    image jgpoolani2 = Movie(play="jgpoolani2.webm")
    scene jgpoolani2
    with fade
    "I began rubbing her neck and shoulders."
    j "Mmmmmmm."
    j "Maybe they are getting too big."
    g "You think?"
    j "I don't even care."
    j "As long as [n] likes them."
    g "I don't think that will ever be a problem."
    j "Right?"
    j "I'm pretty sure these things could be in my lap and he wouldn't be satisfied."
    n "Of course I would."

    j "But are they big enough?"
    n "Sure."
    j "Be honest."
    j "Wouldn't you rather me catch up to Grace?"
    n "I mean..."
    n "She is looking pretty great."
    g "Yeah, yeah."
    j "Hey, what is our sleeping arrangement tonight?"
    n "It's a big bed."
    g "Ooo! I haven't seen it yet."
    j "So... all three of us?"
    n "I call the middle!"
    g "Aww."
    g "I'll flip you for it."
    n "Nope."
    n "My bed, my rules."
    g "Like with your naked rule?"
    n "Hey, yeah!"
    n "That's going on with that?"
    j "Sometimes wearing clothes can be hotter."
    g "Speaking of, doesn't Jenn wear the shit out of my swimsuit?"
    n "I'd still rather you be skinny dipping with me."
    g "But once again... {w}you're clothed."
    n "I can change that."
    j "But if we both take off our bottoms you are going to end up inside me."
    n "Nahhhh."
    scene bg black
    with fadeout
    pause
    "{b}Three Minutes Later{/b}"
    scene bg black
    image jgpoolani3 = Movie(play="jgpoolani3.webm")
    scene jgpoolani3
    with fadein
    pause
    g "See?"
    g "If Jenn was topless, this wouldn't be quite so hot."
    g "It just makes it dirtier."
    n "That's not the top."
    n "It's the fact that in the back of your mind, you feel like we're defiling the flag."
    g "Hmm."
    g "More like waving it proudly."
    n "Let's ask Jenn."
    n "Are you feeling patriotic?"
    j "So much."
    j "But what would happen if I took it off?"
    n "Only one way to find out."
    pause
    scene bg black
    image jgpoolani4 = Movie(play="jgpoolani4.webm")
    scene jgpoolani4
    with fade
    pause
    j "Worth it!"
    n "See my point, Grace?"
    g "Yeahhh..."
    g "I can't stop staring at her rack."
    g "So... {w}bouncy..."
    pause
    g "I'm getting hypnotized."
    g "Quick, [n]!"
    g "Tell my tits to stop growing."
    n "No."
    g "What?"
    n "I can't."
    n "The boobies are telling me not to."
    g "Look away!"
    n "I... can't..."
    j "Shhhh."
    j "Just fuck me."
    pause
    g "That looks fun."
    g "When is it my turn?"
    j "After I'm finished!"
    g "Then hurry up!"
    pause
    j "What-"
    j "Grace?"
    g "I'm just helping things along."
    j "Grace!"
    j "That's your finger!"
    g "Well, yeah."
    g "[n] can't reach you right now because he's busy holding your legs up."
    j "But..."
    j "It feels weird!"
    g "Good, right?"
    j "Really good!"
    g "Excellent."
    g "Now cum for me."
    j "For you?"
    g "So I can have my turn!"
    j "But I like it!"
    g "If you cum, I'll make out with you."
    j "Okay!"
    j "But keep doing that!"
    j "Yesss!"
    with vpunch
    j "Yesssssssss!"
    with vpunch
    j "HOLY FUCK!"
    with vpunch
    pause
    g "My turn!"
    scene bg black
    image jgpoolani5 = Movie(play="jgpoolani5.webm")
    scene jgpoolani5
    with fade
    pause
    j "Mmm!"
    j "Your fingers are magic!"
    g "Mmm."
    g "Not so loud."
    g "[n]'s cock is going to get jealous."
    j "It's not even close."
    g "I know."
    g "Fuck, I missed this thing."
    n "Ladies, ladies."
    n "I'm more than my penis."
    j "And Grace is more than her fingers."
    g "And Jenn is more than her lips."
    j "Mmm."
    pause
    j "Grace, you're a really good kisser."
    g "I know."
    g "I keep trying to tell [n]."
    n "It's not my fault!"
    n "You're the one with the really nice backside."
    g "I got nothing on Jenn."
    g "Her booty is fierce!"
    g "Hey Jenn, remember when [n] was supposed to tell you that?"
    g "Tell her now, [n]."
    n "Don't mind if I do."
    n "Jenn, you have a fat ass."
    g "And it looks gooood!"
    j "Thanks guys!"
    j "I appreciate-"
    g "Shhhh."
    g "Quiet now! I have the floor."
    g "Harder, [n]!"
    g "Fuuuccccckkkkk meeeeeee!"
    with vpunch
    n "Holy shit you feel good!"
    with vpunch
    g "Yahhhhhh!"
    with flash
    j "Oww!"
    with vpunch
    j "You're biting my lip!"
    $renpy.end_replay()
    pause
    scene bg black
    with fadeout
    "{b}The Next Morning{/b}"
    with fade

    "I woke up to the sound of my door knocking."
    n "*mumble mumble*"
    scene hapt2
    with fadein

    h "Hey."
    scene hapt1
    n "Hey! How did you get up here?"
    scene hapt2
    h "The girl at the desk let me up."
    scene hapt3
    n "Nice."
    n "Can I get some sugar?"
    scene hapt4
    with dissolve
    pause
    scene hapt3
    with dissolve
    n "Come in."
    scene hapt5
    with fade
    pause
    n "So how did things go with the doctor?"
    scene hapt6
    h "They checked me out."
    scene hapt5
    n "What did they find?"
    scene hapt6
    h "These."
    scene hapt5
    n "You aren't even going to gesture to your boobs when you talk about them?"
    scene hapt6
    h "No need."
    scene hapt10
    n "Fair enough."
    scene hapt9
    h "They ran some tests and said my hormones were above the normal levels."
    h "But that it should even out soon."
    scene hapt10
    n "Huh."
    scene hapt9
    h "Yeah, I told them that basically all my extra fat had gone right to my boobs and my ass."
    scene hapt10
    n "What did they say?"
    scene hapt6
    h "They really didn't seem concerned."
    scene hapt5
    n "Huh."
    if hcum:
        n "So what else-"
        scene hapt6
        h "[n]."
        scene hapt5
        n "Yeah?"
        label galleryScene64:
        scene hapt8
        h "Sorry for interrupting, but are the girls asleep?"
        scene hapt7
        n "I think so."
        scene hapt8
        h "Then..."
        scene hapt6
        h "Will you fuck me?"
        scene hapt5
        n "Right now?"
        scene hapt6
        h "Yes."
        scene hapt10
        n "On the counter?"
        scene hapt9
        h "Definitely."
        scene hapt10
        n "Uh..."
        menu:
            "Sure!":
                n "Sure!"
                n "Can I eat you out?"
                scene hapt6
                h "No need."
                h "You had me going when you kissed me at the front door."
                scene bg black
                with fade
                "I picked her up and flipped her back onto the counter before pulling down her pants."
                "As promised, she was ready to go."
                "Lucky for her, so was I."
                image haleyaptani1 = Movie(play="haleyaptani1.webm")
                scene haleyaptani1
                with fade
                h "Yessss!"
                pause
                h "Keep sleeping, girls!"
                h "[n] is just going to fuck me on the kitchen counter real quick!"
                h "Then we can have breakfast!"
                pause
                if hcum:
                    n "Ohhh shit."
                    n "I don't think I'm going to last."
                    n "Where do you want me to-"
                    h "Go for it."
                    n "Yeah?"
                    h "It's safe."
                    if preg:
                        h "Even though you'd probably rather I tell you it's not."
                        n "I don't know what you're talking about."
                    h "Oh, okay!"
                    h "[n]?"
                    n "Yeah?"
                    h "I want you to cum inside me."
                    n "Nnnnghhh!"
                    with flash
                    n "Fuck!"
                    with flash
                    n "Wow."
                    pause
                    h "You're still hard?"
                    n "Well, yeah."
                    n "I don't want to be selfish."
                h "Damn, dude!"
                h "I can't believe how fast that I'm-"
                h "Haaaaaa!"
                with vpunch
                h "You big dicked bastard!"
                with vpunch
                pause
                scene hapt6
                with fadehold
                $renpy.end_replay()


            "No":
                n "I uhhh...."
                scene hapt6
                h "Please?"
                scene hapt5
                n "I'm pretty wiped out from last night..."
                scene hapt9
                h "You didn't save any for me?"
                h "Ass."
                scene hapt10
                n "Haley!"
                scene hapt9
                h "What!"
                h "I was ready."
                scene hapt8
                h "Really ready."
                scene hapt7
                n "Sorry."
                scene hapt8

    else:
        scene hapt5
        n "That's good."
        scene hapt6
        h "Yep!"

    h "Should we go upstairs to wake up the others?"
    scene hapt5
    n "I have a better idea."


    if bacon:

        "I went to the fridge and began pulling out eggs, bacon and bread."
        scene bg black
        with fade
        pause
        "{b}Five Minutes Later{/b}"
        scene haleyaptani2
        with fade
        h "Eggs and toast?"
        n "Omelettes and french toast."
    else:

        "I went to the fridge and began pulling out the eggs and chicken sausage."
        scene bg black
        with fade
        pause
        "{b}Five Minutes Later{/b}"
        image haleyaptani2 = Movie(play="haleyaptani2.webm")
        scene haleyaptani2
        with fade
        h "Breakfast?"
        n "Hell yeah."
    n "I went out and grabbed some groceries."
    if bacon:
        h "Mmm I love waking up to the smell of bacon."
    else:
        h "I love waking up to the smell of breakfast."
    n "Then why don't you go upstairs and lay down?"
    n "You can come down in about ten minutes when it's ready."
    h "That sounds good."
    h "But I think I'd rather stay down here with you and watch you cook."
    n "Yeah?"
    h "It's sexy."
    n "Damn, girl!"
    if bacon:
        scene bacon
        with fade
    else:
        scene sausage
        with fade
    n "I'm liking the new confidence."
    h "It's growing."
    h "Just like my boobs."
    "I gave her another appreciative glance."
    scene haleyaptani2
    with fade
    h "You really love them, don't you?"
    n "Your rack?"
    h "Yep."
    n "You know I do."
    h "Me too."
    h "Even if you didn't like them so much, I think I still would."
    n "You're a force to be reckoned with."
    h "And I plan on keeping it that way."
    h "I took the lead, and I plan on keeping it."
    "I smiled at her."
    $ huge = False
    if bacon:
        h "Hey, do you think I could have some of that bacon?"
        n "Looking to start now, huh?"
        h "Oh, I already started."
        n "Here you go."
        scene bg black
        with fade
        image haleyaptani3 = Movie(play="haleyaptani3.webm")
        scene haleyaptani3
        with fade
        h "Mmm."
        h "How much do you have?"
        n "Enough."
        pause
        h "Sooo..."
        h "I'm onto you."
        n "Yeah?"
        h "You love tits."
        n "Sure, who doesn't?"
        h "But you love {i}really big{/i} tits."
        n "Your point?"
        h "I know you want us to keep getting bigger."
        n "My dear Haley, whatever do you mean?"
        h "Sure, play it innocent."
        h "But you have been encouraging us girls to be competitive from the beginning."
        n "Maybe."
        h "I can help, you know."
        n "Oh?"
        h "I could be your secret weapon."
        h "I'll help to make sure all the girls keep outgrowing their bras."
        n "How are you going to do that?"
        h "Competition."
        h "I'll flaunt these big puppies in their faces every chance I get."
        h "And I'll be a bad influence."
        h "Always encouraging the calories."
        n "Interesting."
        h "But there's a condition."
        n "Yeah?"
        h "You have to admit it."
        h "You have to tell me, right now, that you want all of your girls to be huge."
        n "I-"
        h "Not just big."
        h "Huge."
        menu:
            "Admit it [gr]\[Huge breasts\]":
                $ huge = True
                "I smiled at her."
                h "No!"
                h "That's not enough."
                h "I need you to say it."
                n "Fine."
                n "I want all my girls to be huge."
                h "Even me?"
                n "Especially you."
                h "And you want my help?"
                n "Yes."
                if hfavor:
                    h "Okay."
                    h "But I'm going to count this as your favor."
                    n "Hmm?"
                    h "When you first kissed me two weeks ago at Jenn's party."
                    h "We made a bet on how long it would take Jenn to come in when you kissed me."
                    n "Oh!"
                    n "And you lost, so you had to owe me a future favor."
                    h "Exactly."
                    h "So..."
                    h "Are we even?"
                    n "Even Steven."
                else:
                    h "Then beg me."
                    "I smiled at her again."
                    n "No."
                    h "Please?"
                    n "Are you begging me to beg you right now?"
                    h "Maybe."
                    n "Alright."
                    n "Haley, I beg you to help me with your evil plot."
                    h "That's all I needed!"
                h "Consider me your accomplice."
                n "Welcome aboard."
                h "Actually, I'm going to need two more things from you."
                n "Name it."
                h "Bacon."
                n "Here you go, my accomplice."
                n "And?"
                h "Fuck me while you finish making breakfast."
                n "I'd love to, but..."
                h "Come on."
                n "Bacon grease is dangerous."
                h "Oh, I know."
                h "I hear it goes right to your boobs."
                n "I appreciate your faith in my cooking skills, but-"
                h "I believe in you."
                n "Alright, if you're up for it..."

            "Deny it":
                n "Haley, don't get me wrong."
                n "I think you look amazing."
                n "But I'm not here to convince the girls to do anything they don't want to."
                n "Everyone is already top heavy enough for me."
                h "Oh?"
                h "That's disappointing."
                "I smiled at her."
                h "Can I still have some more bacon though?"
                n "Of course."
    scene bg black
    with fadeout
    pause
    "{b}Later That Day{/b}"
    scene 6apt1
    with fadein
    g "Come on! It's a nice day."
    g "And I don't want to go out there by myself."
    n "You know my rules-"
    L "Heyo!"
    scene 6apt2
    with fade
    a "Ashley and the twins are here!"
    L "Now it's a party!"
    scene 6apt3
    with dissolve
    j "Heyyy!"
    g "Sup, bitches!"
    scene 6apt4
    with dissolve
    n "Ladies!"
    A "[n]!"
    image aptani1 = Movie(play="aptani1.webm")
    scene aptani1
    with dissolve
    if huge:
        h "Hell yeah!"
        h "I'll make us some snacks!"
    g "Aww! You guys just missed the orgy."
    a "Orgy? Did you let [n] play?"
    g "No, we made him stand in the corner."
    L "Poor [n]."
    n "It's fine."
    n "I just jerked off into the toilet."
    j "No!"
    L "Don't even joke about that!"
    g "Don't judge us, Aera."
    A "It's far too late for that."
    A "You're all a bunch of deviants."
    j "If we were in your country, would we be in jail?"
    A "You do realize I'm from South Korea, no?"
    j "Umm..."
    A "That's the one that's ran by Samsung, not an evil dictator."
    j "Oh."
    A "We have orgies all the time."
    n "Right."
    a "So what did you guys do last night?"
    g "We went out for dinner."
    g "I had pasta, Jenn had [n]'s dick under the table."
    L "She did not."
    a "Damn, girl!"
    a "You crawled under the table at a restaurant?"
    j "...yeah."
    a "You are going to have to tell me more about that later."
    L "So what are doing tonight?"
    n "I have an idea."
    L "Yeah?"
    n "We could have dinner here."
    n "Six people eating out adds up pretty quick, and I'm afraid I don't have enough cash to pay for everyone."
    n "Starving student, remember."
    g "Yeah, yeah. We know."
    g "But I need to leave this apartment tonight."
    n "And we will."
    g "Where?"
    n "A club."
    g "We don't have fake IDs."
    n "I found an eighteen and over club."
    a "Oh!"
    a "Hell yeah!"
    L "Where we can't drink?"
    n "No need."
    n "We have a bottle of tequila."
    n "What do you girls say?"
    h "To dancing? Shyeah!"
    g "Hell yes."
    "My phone's notification sound went off."
    with vpunch
    j "Who's texting you, [n]?"
    g "Yeah! All your girls are right here."
    L "Probably Big Titty Goth Girl downstairs."
    a "Really?"
    n "It's probably Laura."
    L "Why?"
    n "She's been texting me all week, trying to get me to meet up with her so we can talk."
    g "And you've been ignoring her?"
    n "Yep."
    n "She stole my watch and then destroyed it before I could use it to help any of you stop growing."
    n "I have nothing to say to her."
    g "Huh."
    n "Too harsh?"
    g "No, understandable."
    h "Hey, I don't mean to be the only fat girl here, but..."
    h "What we are making for dinner?"
    n "Who is the best cook?"
    L "I can make spaghetti."
    n "Ashley?"
    a "You've had my pasta."
    n "Mmm."
    g "Pasta? Are you girls kidding?"
    g "I am not trying to carb-load here!"
    a "Good point."
    a "What about you, [n]?"
    menu:
        "Burgers [blue]\[Miss Leah & Ashley sex opportunity\]":
            $ burgers = True
            n "I can make burgers."
            a "Not better."
            n "I could go to the store and get some mushrooms-"
            j "Gross."
            n "-some bacon and avocado-"
            L "Not better!"
            n "-and we'll pick up cheese and veggies."
            n "With something healthy on the side."
            h "That sounds amazing."


        "Tacos":
            $ burgers = False
            n "We already have the tequila. {w}You girls down for some tacos?"
            g "Really?"
            n "What?"
            n "They are cheap, delicious and nutritious."
            g "Fried tortillas, cheese and fatty meat?"
            n "High protein to keep you full, vegetables for your nutrients..."
            L "Sounds good to me. I'm starving."
            j "Me too."
            g "Fiiiine."

        "Taco salad":
            $ burgers = False
            n "How about taco salad?"
            a "Ooo! Yes! Yes!"
            g "Now we're talking!"
            h "Could I have a regular taco?"
            n "Of course."
    h "Cool. I'll go shopping with you."
    n "Make yourselves at home, ladies."
    n "We'll be back."

    scene hwalk1
    with fadehold
    pause
    n "Thanks for coming, Haley."
    h "Of course."
    if huge:
        h "I am your accomplice, after all."
        n "That's why you're the best!"

    n "So tell me something."
    h "What?"
    n "Anything."
    scene hwalk2
    with dissolve
    n "Something you haven't told anyone."
    if hcum:
        h "Oh."
        n "Yeah?"
        h "Okay."
        scene hwalk3
        with dissolve
        h "Can you promise not to tell anyone?"
        n "That would go without saying, but yes."
        h "Okay."
        h "I was supposed to have my period four days ago."
        scene hwalk4
        with dissolve
        n "Oh?"
        h "...yeah."
        n "So you're saying..."
        h "...yeah."
        scene hwalk5
        with dissolve
        pause
        n "Haley, can I see your eyes?"
        image hwalkani1 = Movie(play="hwalkani1.webm")
        scene hwalkani1
        with fade
        pause
        h "I haven't told Jenn because she would be freaking out right now."
        h "She wants you to put a baby in her so bad."
        h "Which is something I do not understand, by the way."
        n "So you wouldn't be happy if-"
        h "No.{w} Definitely not."
        n "Shit."
        n "Well then. {w}Should we pick up a test at this place?"
        n "That way you can rest assured?"
        h "I guess so."
        "She sighed."
        h "I might as well know what I'm in for."
        h "It's probably nothing."
        h "But, for the record-"
        n "You don't want to risk it ever again?"
        h "Exactly."
        n "Then why did you tell me to fill you with jizz earlier?"
        h "Because at this point in my cycle it's impossible."
        n "Really?"
        h "Trust me. It's girl stuff."
        n "If you say so."
    else:
        h "Alright."
        h "I really don't understand why Jenn wants to get pregnant so badly."
        scene hwalk3
        with dissolve
        if preg:
            n "Oh?"
            h "You kissed her for the first time, what, three weeks ago?"
            n "Something like that."
            h "What's the rush?"
            scene hwalk4
            with dissolve
            n "Good point."

            h "And I also don't understand why you want it."

            n "I'm not sure if I can explain it."
            n "I just..."
            scene hwalk5
            with dissolve
            n "It's fucking hot."
            h "That's it?"
            n "That's it."
            h "Lordie."
        else:
            n "She what?"
            h "Yeah."
            h "Watch out for that one."
            n "Seriously."

    scene market6
    with fade
    pause
    n "Alright."
    n "What do we need?"
    h "Not that shit."
    n "Right."
    n "Tomatoes, ground beef, onions, lettuce..."
    scene market7
    with dissolve
    n "What do you want to do for a side?"
    if huge:
        h "Some chips?"
        h "What has a lot of calories?"
        if burgers:
            h "Cheese dip?"
        else:
            h "Sour cream?"
            n "Less than you'd think."
            h "Cheese dip?"
        n "You're evil."
        scene market8
        with dissolve
        h "You like it."
        h "I'll make a dip to go with the chips."
        h "And I'll tell them it's low calorie."
        n "Oh, Haley!"
    else:
        if burgers:
            h "How about barbeque chips?"
        else:
            h "Chips and salsa?"
        n "Sure."
        h "What kind of dip?"
        n "Cheese?"

    scene market10
    with dissolve
    h "What else?"
    scene market9
    n "We should probably grab some more eggs and breakfast food while we're here."
    n "Do you like bagels?"
    scene market10
    h "And cream cheese."
    scene market9
    n "Naturally."
    if huge:
        scene market10
        h "How about donuts?"
    else:
        scene market10
        h "How about muffins?"
    scene bg black
    with fadeout
    "When we returned I started making dinner."
    if burgers:
        scene burgers
        with fadein
    else:
        scene meat
        with fadein
    pause
    n "{b}How do I get back there, to the place where I fell asleep inside you? How do I-{/b}"
    L "Hey! Why is [n] in here cooking?"
    image aptani2 = Movie(play="aptani2.webm")
    scene aptani2
    with dissolve
    L "Can't someone else do it so I can take him upstairs?"
    n "Sorry, Leah."
    n "I'm all tapped out for the night."
    L "For the {i}night{/i}?"
    L "Bullshit!"
    L "I know you wouldn't blow your whole load without saving something for me."
    n "How do you know that?"
    L "Because you are a nice enough guy to appreciate the fact that you've turned us all into addicts."
    L "And denying us the D is something we could never forgive."
    n "That's ominous."
    if burgers:
        n "Does anyone want to take over the burgers?"
        A "I would fuck that up."
        A "They would turn out like hockey pucks."
        n "Sorry, Leah."
        if hcum:
            n "But I'll be right back."
    else:
        n "If anyone wants to volunteer, all they would need to do is finish browning up this beef..."
        A "I could do that."
        A "If you could explain to me how you are using a pan on a countertop?"
        n "You don't have this in fancy Korea?"
        A "We have these things called stoves."
        L "I... didn't even notice."
        n "I don't know."
        n "Something about induction?"
        n "You can control the temperature here."
        A "Okay."
        A "Go stick it in my sister."
        L "Thanks, Aera!"
        L "Shall we?"
        n "Let's!"
        if hcum:
            n "But first, I'm going to use the bathroom."
    scene bg black
    with fade
    if hcum:
        "I went to check on Haley."
        scene htest1
        with fadein
        pause
        n "Good news?"
        scene htest2
        with dissolve
        h "Depends."
        h "What would good news be for you?"
        scene htest3
        n "I want what you want."
        if preg:
            n "It's not about me. It's-"
            scene htest2
            h "Would it make you happy?"
            scene htest3
            n "If you were happy, I would be happy."
            scene htest4
            h "Okay, let's say I would be."
            scene htest3
            n "If you were, I would think it's sexy as fuck."
            scene htest2
            h "Why?"
            scene htest3
            n "Just the fantasy of imagining you swell up with my child is enough to make me hard."
            n "But the concept of it being real?"
            n "I could pick you up right here and fuck you over the sink."
            scene htest2
            h "You could do that anyway."
            scene htest3
            n "So?"
            n "What about what you want?"
        scene htest2
        h "Then..."
        scene htest4
        h "Bad news."
        scene htest3
        n "Wait!"
        n "Don't fuck with me right now."
        scene htest4
        h "I mean, it's only one test, but..."
        h "...see for yourself."
        scene htest5
        with fade
        pause
        scene bg black
        with fade
        "Positive."
        n "Shit!"
        "I hugged her."
        scene htest6
        with fade
        n "Haley, I am really sorry."
        scene htest7
        h "But isn't this what you wanted?"
        h "You do realize how sex works, right?"
        scene htest6
        n "Yes."
        scene htest8
        n "But that wasn't my decision to make."
        n "So I apologize."
        scene htest9
        h "It took both of us to make this choice."
        scene htest10
        n "I suppose."
        scene htest9
        h "So I can't blame you."
        scene htest10
        n "You can."
        scene htest9
        h "Maybe a little bit."
        h "So..."
        if preg:
            h "Now that you don't have to imagine this happening anymore, do you still find it sexy?"
        else:
            h "Is this what you want?"
        scene htest10
        menu:
            "Yes":
                n "Of course."
                scene htest9
                h "Good."
                scene bg black
                with fade
                "She kissed me."
                scene htest3
                with fade
                n "Are you going to tell Jenn?"
                scene htest2
                h "Fuck no."
                scene htest3
                pause
            "No":
                n "No."
                scene htest9
                h "Really?"
                scene htest10
                n "Yeah."
                scene htest8
                n "This is freaking me the fuck out."
                scene htest2
                h "Okay."
                h "I'll take care of it."
                scene htest3
                n "You don't-"
                scene htest4
                h "Don't worry about it."
                "She kissed me."
                scene htest3
                with fade
                n "Are you going to tell Jenn?"
                scene htest2
                h "Fuck no."
        scene bg black
        with fadeout
    if burgers:
        scene apt13
        with fadein
        pause
        n "Who's hungry?"
        g "Hell yeah."
        n "Burgers will be done soon."
        n "But in the mean time, Haley is going to bring you some appetizers."
        j "Yay!"
        scene burgers
        with fade
        g "Wait, what the fuck?"
        n "What?"
        g "We told you we wanted to eat something healthy, and you make us cheese dip?"
        h "I made it."
        g "Haley!"
        h "It's low calorie."
        L "Cheese dip with chips being low calorie is a myth."
        scene apt14
        with dissolve
        g "Does anyone else feel like [n] is trying to fatten us up?"
        a "What do you mean?"
        g "Do you know what a Feeder is?"
        n "The hell?"
        g "It's someone who feeds their girlfriend a bunch of food trying to make them bigger."
        j "Why would they do that?"
        g "Because they are into fat girls."
        j "Really?"
        g "But with us, it's not fat girls he wants."
        L "Just fat tits!"
        scene burgers2
        with fade
        a "Ha!"
        g "Okay, [n]."
        g "Tell us the truth."
        g "Are you trying to make us grow even bigger...{w} even though we have specifically told you that we don't want to?"
        menu:
            "Maybe":
                n "...maybe?"
                L "Wait, really?"
                a "Seriously?"
                scene apt14
                with dissolve
                a "[n], we have gone out of our way to accomodate your tastes."
                a "But when we tell you that we are already bigger than any of us want, you seriously need to respect that."
                j "It's not that big of a-"
                a "I'm still talking."
                a "Look, it was all fun and games when you had the watch and we could stop at any point."
                a "But we're stuck like this."
                a "Even when I don't eat much, I still grow."
                a "This is fucking serious."
                a "And you need to respect us, or we are leaving."
                a "Right?"
                L "Yes."
                g "Yep."
                A "Yes."
                "There were nervous giggles."
                L "Thanks, sis."
                A "No problem!"
                L "But Ashley is right."
                n "Okay."
                n "I hear you."
                scene bg black
                with fade
                "I grabbed the chips and dip off the table."
                scene apt15
                with fade
                n "And you should know, I was kidding-"
                a "I don't think you were."


            "No":
                n "Of course not."
                g "Better not."
                g "We already don't know how much we will keep growing."
                g "And there is no reason to accelerate the process."
                scene apt14
                with dissolve
                n "I just wanted to make a nice meal."
                if huge:
                    g "What about you, Haley?"
                    h "Huh?"
                    g "Are you trying to over feed us?"
                    h "No?"
                    h "Why would I want that?"
                    h "I like being the biggest."
                    g "And I'm perfectly alright with that."
                    g "So let's keep it that way, huh?"
                    h "Of course."
                else:
                    a "Oh, is that all?"
        scene burgers2
        with fade
        if huge:
            h "Are you girls serious right now?"
            a "What?"
            L "Haley, relax."
            h "No!"
            pause
            h "[n] invited all of us over and wanted to make sure everyone gets a nice meal fed."
            h "He went to go shopping to get food for everyone and then made us all something delicious."
            h "By himself, I'll add."
            scene apt16
            with dissolve
            h "Did anyone offer to help?"
            h "Oh, wait. Just me."
            h "And not only are you criticizing me for it, you're threatening [n]?"
            h "Do you really think that if we went out for dinner we find anything healthier than what [n] just made you?"
            h "If you don't like, don't fucking eat it!"
            pause
            g "Holy shit, Haley."
            n "Alright, the burgers are ready."
            n "Who wants to help me serve all this food?"
        else:
            menu:
                "Respond casually":
                    n "Look, I appreciate when you girls call me on my shit."
                    n "But I just spent the past hour going shopping and cooking dinner for you guys."
                    n "I told you what I was going to make, and I asked for suggestions."
                    n "And no one besides Haley even offered to help."
                    n "So if you don't like what I made, you don't have to eat it."
                    scene apt14
                    with dissolve
                    pause
                    n "You are acting like a bunch of seven year olds."
                    n "So either enjoy these burgers, one of the things I make pretty damn well."
                    n "Or go down the street and get something far worse for you."

                "Defend yourself":
                    n "Really?"
                    n "I go out shopping for food after asking what you guys want."
                    n "Then I take the time to cook up dinner for you."
                    n "And now you sit around calling me an asshole for it?"
                    n "See if I offer to make another fucking meal for you."
                    scene apt14
                    with dissolve
                    pause
                    a ">..."
                    a "I'm sorry."
            a "You're right, [n]."
            a "We are just starting to freak out about this whole situation."
            n "Well, I don't know what you want from me."
            scene burgers2
            with fade
            n "I've done everything I could to stop you from growing."
            n "If you have any more ideas, I'm all ears."
            a "Okay."
            a "Could we eat now?"
            n "If one of you gets up off your ass and helps me bring all of this over."


    else:
        label galleryScene65:
        "I went upstairs to meet up with Leah."
        scene lapt1
        with fadein
        pause
        n "Well hello."
        scene lapt2
        with dissolve
        n "Damn, it's good to be me!"
        L "Hey there."
        scene lapt3
        with dissolve
        n "Oh! I see you brought a friend."
        a "Don't mind me."
        a "But Leah took off her top sooo..."
        a "...I'm going to sit here and finger myself while I watch."
        scene lapt4
        with dissolve
        n "...okay?"
        scene lapt2
        L "You think she's joking?"
        scene lapt4
        a "Are you ready to put on a show for me?"
        n "That depends."
        scene lapt3
        with dissolve
        n "Are you going to judge us?"
        a "I'm going to be judging you through orgasm colored glasses."
        n "Fair enough."
        L "So..."
        scene lapt2
        with dissolve
        L "You down?"
        scene lapt4
        menu:
            "Yep":
                n "Do you really need to ask?"
                a "You're the one asking the redundant questions here."
                scene bg black
                image aptani5 = Movie(play="aptani5.webm")
                scene aptani5
                with fade
                pause
                a "I'm just trying to finger myself while I watch you two fuck."

            "No":
                n "Uhhh..."
                a "You want me to leave?"
                scene bg black
                image aptani5 = Movie(play="aptani5.webm")
                scene aptani5
                with fade
                pause
                n "Or... join?"
                a "Nah, that's for later."

        a "You are going to fuck Leah until you cum inside her."
        a "Then I'm going to lick the cum out of her as I eat her out..."
        a "...and you are going to fuck me from behind while I do it."
        a "Then you creampie me, and Leah and I switch."
        a "Sound good?"
        n "I-"
        a "Good."
        a "This is going to be fun to watch."
        image aptani3 = Movie(play="aptani3.webm")
        scene aptani3
        with fade
        pause
        a "Fuck, that's hot."
        L "You like that?"
        a "Leah, your tits are epic."
        a "You're a fucking goddess."
        pause
        a "[n], you look okay too I guess."
        n "Wait your turn, Ashley."
        pause
        a "I can't wait until you fill up her pussy, [n]."
        a "It's going to taste so fucking good."
        L "Mmmm."
        a "It's going to be like mixing my two favorite flavors."
        L "All you need are some gummy bears to dip in there."
        a "Yes!"
        a "Do we have any?"
        pause
        a "Are you close, [n]?"
        n "Very."
        a "Well, come on now."
        a "Fill my girlfriend with your cum."
        a "Pump your load into your best friend's little sister."
        a "Blow your sperm into her tight little pussy so that I can lick it clean!"
        n "Nnnnn!"
        with flash
        L "YESSS!"
        with flash
        a "Fuck yeah!"
        with flash
        n "Fuck, Ashley!"
        a "That's Leah."
        a "And move over!"
        scene lapt5
        with fade
        pause
        a "Mmmm."
        L "FUCK!"
        L "Ash, I'm so sensitive right now!"
        a "Mmmm!"
        L "Slow down!"
        L "Ahhh!"
        L "It's starting to tickle!"
        L "[n], can you get your revenge on the little purple haired girl?"
        n "My pleasure."
        scene bg black
        image aptani4 = Movie(play="aptani4.webm")
        scene aptani4
        with fade
        pause
        L "Mmm."
        L "This is fun to watch."
        a "Fuck, [n]!"
        a "I thought you already took it out on Leah?"
        L "Oh, he did."
        n "But now it's your turn."
        a "You spoil us!"
        n "I do my best."
        pause
        L "Holy shit, Ashley."
        L "I think I can see his dick when it pushes out your stomach."
        a "Can't... talk..."
        a "Taking... dick..."
        L "Yeah you are!"
        L "Like a champ!"
        L "Remember when neither of us could fit [n] inside of us?"
        L "Now look at us."
        n "My girls."
        $renpy.end_replay()
        pause

    scene bg black
    with fadeout
    pause
    "{b}Twenty Minutes Later{/b}"
    image aptani8 = Movie(play="aptani8.webm")
    scene aptani8
    with fadein
    g "That was fucking delicious."
    if burgers:
        g "I'm sorry for snapping at you earlier, [n]."
        g "But my tits are getting so huge it's starting to scare me."
        L "Yeah they are!"
        g "I'll try to learn to cook so I can make something next time."
        n "I'd like that."
    else:
        L "Yeah it was!"
        n "Thank Aera. She cooked the taco meat."
        g "Yeah girl!"
    j "Thanks, [n]."
    n "You're welcome."
    h "Did everyone get enough?"
    scene bg black
    image aptani7 = Movie(play="aptani7.webm")
    scene aptani7
    with dissolve
    h "There's more."
    a "I'm stuffed."
    a "It was very good."
    if burgers:
        a "And [n], I also apologize for teaming up against you."
        a "But there's something else that we need to talk about."
        a "Leah?"
    else:
        L "Hey, Ashley and I have something uncomfortable to address."
    L "Since everyone concerned is here, I think now is a good time to talk about it."
    n "Okay?"
    L "Do you know what I'm going to say?"
    menu:
        "Guess":
            n "Umm..."
            n "You are going to make me decide between you girls?"
            L "Uh..."
            L "Not exactly."

        "Don't guess":
            "{i}I'm not touching this one with a twenty foot pole.{/i}"
            n "I haven't the foggiest."
    L "Ashley?"
    a "You're fucking all of us, [n]."
    A "Not me!"
    L "That's because you're the good sister."
    a "But things have changed."
    a "We are your responsibility now."
    a "Five girls set on a path where we could end up immobile."
    g "You think so?"
    a "We'll probably make it through graduation."
    a "But then what?"
    a "Get jobs as bean bag chairs?"
    n "So you're asking if I'll do everything I can to take care of you?"
    n "Because of course I will."
    L "No."
    L "We need to know if we are enough."
    n "What?"
    L "The five of us right here."
    L "Are we enough for you?"
    n "Of course."
    a "We mean it."

    a "We don't want to worry about you dating anyone else, or what happens when Big Juggs downstairs hits on you."
    a "Leah and I aren't asking you to break it off with any of us."
    a "We only want to know if you are going to be loyal to your girls sitting right here."

    menu:
        "[gr]Of course":
            n "Of course."
            n "You girls are amazing."
            g "So no more other girls, even if they throw themselves at you?"
            n "Right."
            n "Not as long as I have you."
            a "Good."
            a "I think it's good for us all to hear that."
            a "Because we shouldn't have to compete against each other."
            a "I think we can work together."
            a "Jenn, what do you think?"
            scene bg black
            scene aptani8
            with dissolve
            j "If I can be honest..."
            j "I wouldn't mind having [n] to myself."
            j "But if I'm going to be sharing [n] with anyone, I'd choose you girls."
            h "As long as there is enough dick to go around."
            g "Ha!"
            g "I agree."
            g "Keep my pussy satisfied, and I have no complaints."
            g "Plus, I had a great time with Jenn."
            g "I'd rather keep her around anyway."
            j "And Haley is great too."
            n "You should try Ashley and Leah."
            g "Maybe I will."
            n "Well now!"

            n "This conversation wasn't too bad."
            L "I'm glad."
            a "And I'm proud of us."
            a "Look at us all being adults about this."
            A "Too adult for my taste."
            A "You're all a bunch of sex addicts."
            j "Guilty."
            h "Yep, sounds about right."


        "[red]I can't promise that":
            n "I can't promise that."
            scene bg black
            scene aptani7
            with dissolve
            a "No?"
            a "Why not?"
            n "You've never asked that of me."
            n "And it's something I've never promised."
            a "Well, we are asking now."
            n "I understand that."
            L "[n]."
            L "Look at the five faces in front of you."
            L "If this isn't enough for you, then nothing ever will be."
            L "I'm with her."
            n "But-"
            g "Now?"
            a "No."
            a "We can still go out and have fun tonight, if that's what you want."
            a "But after that, I'm going home."
            L "As am I."
            n "Jenn and Haley?"
            h "No, they're right."
            if jennice:
                j "I'm with you girls."
            else:
                j "I'll stay."
                h "Come on, Jenn."
                j "But I'm his slut."
                h "You are more than that."
                j "But-"
                h "I'm making you come with us."
            g "I'm with them."
            n "You really don't have to go."
            n "Nothing has changed."
            n "What's the difference?"
            h "What's the difference?"
            if hcum:
                h "How about the fucking thing I just told you?"
                j "What?"
                h "We'll talk about it later."
            else:
                h "Ashley was right."
                h "If five girls aren't enough for you, then it never will be."
                h "Honestly, every single girl here should be enough for you."

            scene bg black
            with fadeout
            "That wasn't the last I saw of any of the girls."
            "Every single one of them came back for more rides on the ol' magic stick."
            "But true to their word, they all ended things with me."
            "I still fucked the other girls."
            "But I started to miss my main crew."
            "Eventually, I realized what I was missing, so I called them all and promised to be loyal."
            "It was too late."
            "My life became a mess after that."
            "I still had an insatiable appetite, but I could never find a girl who could keep up with me."
            "I spent the majority of my time out on the prowl, getting better at picking up women and bringing them home."
            "Half the time the girl would be too worn out to continue, and I'd head back out to meet a new one."
            "I would skip classes to fuck in the bathroom."
            "I would spend the entire weekend going from one random girl's house to another."
            "My life had only one focus: getting laid."
            "And I couldn't seem to stop."
            with fade
            centered "The End"
            with fade
            pause
            jump afterend

    j "Alright!"
    j "So when are we going dancing?"
    g "My girl!"
    n "We could leave in a couple hours."
    scene bg black
    scene aptani7
    with dissolve
    L "Cool. Let's get ready!"
    L "But before we do, where is everyone sleeping tonight?"
    L "I call bed!"
    n "The master bed is big enough for everyone."
    n "But if anyone wants, there is also a guest room."
    scene bg black
    scene aptani8
    with dissolve
    g "Is the guest room soundproof?"
    n "I doubt it."
    g "Hmm."
    j "I don't think I'd want to hear you fucking Leah and Ashley all night."
    n "Then why not join us?"
    j "Umm..."
    j "No."
    n "Why not?"
    scene bg black
    scene aptani7
    with dissolve
    a "Yeah, why not?"
    a "We are good at sharing."
    j "I already had my time with [n] this morning."
    j "I'll give you the opportunity."
    if burgers:
        a "Okay!"
    else:

        a "We did too."
        j "What!"
        j "When?"
        a "When Aera cooked the taco meat."
        a "You didn't hear us?"
        j "Uhh..."
        j "I guess not."
    scene bg black
    scene aptani8
    with dissolve
    j "But don't forget about Haley."
    h "I'm good."
    j "You don't want to?"
    if huge:
        h "Oh, no. [n] already fucked me in the kitchen."
        L "[n]!"
        L "That's where we eat!"
    else:
        h "Okay, pull my arm!"

    A "I'll happily sleep in the guest room."
    A "I'm not looking to watch everyone have sex all night."
    n "Fair enough."
    g "I'm with Aera."
    g "So I'll take the couch."

    L "Alright!"
    L "Let's get ready!"
    scene bg black
    with fadeout
    pause
    "{b}That Night{/b}"
    scene dance1
    with fadein
    pause
    scene dance2
    with fade
    pause
    scene dance3
    with fade
    pause
    scene dance4
    with fade
    pause
    scene dance5
    with fade
    pause
    scene dance6
    with fade
    pause
    scene dance7
    with fade
    pause
    scene dance8
    with fade
    pause
    scene dance10
    with fade
    pause
    scene dance9
    with fade
    pause

    scene bg black
    with fadeout
    pause
    "{b}The Next Morning{/b}"
    scene apt17
    with fadein
    n "Heyo!"
    g "Hey."
    scene apt18
    with dissolve
    n "How'd you sleep?"
    g "Sound really carries in this place."
    scene apt19
    with dissolve
    pause
    n "Oh yeah?"
    image aptani6 = Movie(play="aptani6.webm")
    scene aptani6
    with fade
    g "I never realized how undignified sex could sound."
    n "Yeah?"
    g "Aww, who am I kidding?"
    g "It was fucking hot."
    n "Yeah? Did you beat off?"
    g "Several times."
    g "I always cum easier after you fuck me."
    n "Good to know."
    n "How did you sleep, Jenn?"
    j "Alright."
    j "Not the same as in your bed."
    n "Hey, the invitation still stands."
    j "I know."
    j "But I would feel like I'm intruding."
    n "Why?"
    j "I just..."
    j "I'm not like them."
    n "Leah and Ashley?"
    j "Yeah."
    n "How so?"
    j "I like boys."
    g "Trust me, girl."
    g "They both like dick just fine."
    j "I know."
    g "You think it was any different than what you and I did the other night?"
    j "Yes."
    n "Why?"
    j "Because I was drunk."
    g "So?"
    g "You didn't like kissing me?"
    j "I did."
    g "So what are you worried about?"
    j "I don't think I want to... {p}...eat it."
    g "You don't have to."
    j "But... wouldn't they want me to?"
    n "Only if you wanted to."
    j "Oh."
    g "But just for the record..."
    g "It tastes amazing."
    j "Eww."
    n "Alright."
    n "Who wants to help me make breakfast?"
    g "I don't really know how."
    n "I'll teach ya."
    g "Fine."
    g "Do we have any tequila?"
    g "My head hurts."
    n "You drank it all last night, I'm afraid."
    n "How about some water?"
    g "Hell yes."
    g "But also, it really helped my headache when I had another drink."
    n "And that, my dear, is a warning sign."
    g "For what?"
    n "A warning that you have had enough to drink."
    g "So your head doesn't hurt?"
    n "Oh, I'm dehydrated as fuck."
    n "But that might not be for the same reasons."
    n "You know what I saw in the kitchen?"
    g "What?"
    n "Champagne."
    if bacon:
        n "I'll pour if you start the bacon."
        g "Mmm."

    scene bg black
    with fadeout
    pause
    "{b}Twenty Minutes Later{/b}"

    if bacon:
        scene bacon
        with fadein
        if burgers:
            a "Really? Bacon?"
            n "Fuck yes, bacon."
        else:
            a "Bacon!"
        a "Do we have any eggs?"
        n "Of course."
    else:
        scene sausage
        with fadein
        a "Whatcha makin?"
        n "Chicken sausage."
    n "There are also bagels."
    h "And muffins!"
    h "Because [n] wouldn't let me get donuts."
    g "Muffins are just as bad!"
    h "There's no way that's true."
    h "Hey, if I heat up that cheese dip from yesterday, who is getting in on it with me?"
    if burgers:
        a "You're killing me, Haley."
    else:
        a "Damn it."
        a "It was really fucking good."
        a "I'm in."


    scene bg black
    with fadeout
    pause
    "{b}Two Hours Later{/b}"
    scene jgentrance5
    with fadein
    n "Thanks for coming!"
    n "Spending the whole weekend with you was pretty great."
    j "Bye, [n]."
    n "I love you guys."
    g "Love you too."
    scene jgentrance3
    with dissolve
    pause
    "I kissed Jenn softly."
    scene jgentrance2
    with dissolve
    pause
    n "Don't think you're getting out of it, Grace!"
    scene jgentrance4
    with dissolve
    pause
    "I gave Grace a big sloppy one."
    scene jgentrance5
    with dissolve
    n "Alright, I heard the horn."
    g "Bye, [n]."
    n "Tell Leah not to crash Cory's car, because I don't want Cory to kill her."
    j "Bye!"
    scene bg black
    scene btggani1
    with fade
    pause
    n "What?"
    pause
    "Girl" "No comment."
    n "Somehow I doubt that."
    n "Hey, what's your name, anyway?"
    "Girl" "No comment."
    n "Really?"
    n "Are you angry with me for some reason?"
    "Girl" "Not at all."
    "Girl" "I'm very amused."
    "Girl" "But I'm also trying to be professional."
    "Girl" "So I'm biting my tongue."
    n "Fair enough."
    n "So how does a guy get your name?"
    "Girl" "I'm sure you'll think of something."
    n "Can I get a hint?"
    scene bg black
    scene btggani2
    with fade
    "Girl" "Sure."
    "Girl" "I already told it to you when your friend asked."
    n "Ah."
    n "I might have been distracted."
    "Girl" "I guessed."
    n "Alright."
    n "I'm going back upstairs."
    "Girl" "You do that."
    menu:
        "Hit on her [gr]\[Big Titty Goth Girl\]":
            n "If you get bored, feel free to come up."
            "Girl" "Tooootally."
            $ btgg = True

        "Leave":
            n "Later."
            "Girl" "Toodles!"


    $ lauraside = False
    $ britside = False
    $ tifside = False
    $ rachelside = False
    $ baileyside = False
    if bcum:
        scene bg black
        with fade
        pause
        "{b}That Evening{/b}"
        with fade
        "I was laying in bed watching TV when I received a phone call."
        scene aptv
        with fadein
        n "Brittany!"
        b "Hey! Where are you?"
        n "At my apartment in the city."
        b "Are you busy?"
        n "Not particularly."
        b "Want company?"
        n "Uhh..."
        menu:
            "Yes [blue]\[Brittany Side\]":
                "I'm not hooking up with any new girls."
                "That should be fine, right?"
                n "Sure."
                n "I'll text you the address."
                b "Good."
                b "Because I'm going to deliver this pussy."
                b "Is this going to put me above all your other sluts?"
                "Nope."
                n "Totally."
                b "Alright, see you in forty."
                label okaybrit:
                $ britside = True
                scene bg black
                with fade
                pause
                "{b}Thirty Minutes Later{/b}"
                scene bapt1
                with fadein
                pause
                n "Damn! You got here quick!"
                scene bapt2
                with dissolve
                b "No time for talky."
                b "Only time for bang bang."
                scene apt1
                with fade
                b "Nice place!"
                b "Where are we fucking first?"
                b "Ohhh!"
                b "Have you already done it on the balcony?"
                scene apt2
                with dissolve
                n "Yep."
                b "Bah."
                scene apt3
                with dissolve
                b "On the staircase?"
                n "No, actually."
                b "Dibs!"
                image baptani1 = Movie(play="baptani1.webm")
                scene baptani1
                with fade
                pause

                b "Nyeeeeaaht!"
                n "I love it when you talk nonsense to me."
                b "Then... keep... hitting... it... like... that!"
                pause
                scene bg black
                image baptani2 = Movie(play="baptani2.webm")
                scene baptani2
                with fade
                pause
                n "So if this is the only time I get with you, how's life?"
                b "Nyeeesh!"
                n "Good, good."
                b "Fuck me, [n]!"
                n "Nice catching up with you."
                pause
                b "I... mmmm... think someone is knocking on your door."
                n "That's too bad."
                b "Yeah! Fuck 'em!"
                n "I kind of hope it wasn't any of the other girl's I'm dating."
                n "I maybe promised them that I wouldn't be fucking anyone else."
                b "Well that sounds like a stupid thing to tell them."
                b "They all know my pussy is the best!"
                n "It's pretty great."
                n "But I'm more about your ass."
                b "You want to do anal?"
                n "I mean..."
                n "Sure?"
                b "Next time."
                n "Deal."
                b "I'm about to hit that deep dick orgasm!"
                b "Riiiiiight there!"
                with vpunch
                b "Fyaaaaaah!"
                with vpunch
                b "Yeeesssss!"
                pause
                scene bapt3
                with fadehold
                pause
                n "It was good to see you."
                n "Are you sure you don't want to stay?"
                scene bapt4
                b "I got my fill."
                $renpy.end_replay()
                b "You gave me my two loads."
                b "That's worth the drive right there."
                scene bapt3
                n "I get it."
                n "Still, it would be nice to be able to spend time with you without there being a rush."
                scene bapt4
                b "I could make that happen."
                b "Goodbye, lover."
                scene bapt5
                with dissolve
                pause
                b "Oh, shit."
                n "What?"
                b "I figured out who was knocking on your door."
                b "And this is where I make my exit."
                scene bapt6
                with fade
                "I peaked my head around the corner to find..."
                image laptani1 = Movie(play="laptani1.webm")
                scene laptani1
                with fade
                pause
                l "Hi."
                n "Hi?"
                n "What are you doing here?"
                l "Discovering new things about my sister."
                n "Didn't expect her in this hallway, huh?"
                l "I didn't expect to find her coming here to get her brains fucked out."
                n "Surprise."
                n "What do you want, Laura?"
                l "You haven't been answering my calls."
                n "Yep."
                l "But I have a couple of important things to tell you."
                n "Don't care."
                l "Apparently."
                n "Yep."
                "She sighed."
                l "Alright, how about this instead."
                l "We don't talk about anything."
                l "In fact, I don't say a word."
                l "But you take me inside and show me how much you hate me by fucking me as hard as you can."
                n "Hmm..."
                n "You might like that too much."
                l "So?"
                scene bg black
                with fade
                pause
                centered "Sorry, guys."
                centered "That's all I have for now."
                pause
                centered "I know, you expect me to say something about a fakeout."
                centered "But I still need to finish up the rest of the ending."
                jump end
                menu:
                    "Deal [blue]\[Laura Side\]":
                        $ lauraside = True
                        n "Deal."
                        n "But only under one more condition."
                        l "Yes?"
                        n "If you want to come back again another time, you stop calling me ten times a day."
                        l "Okay."
                        n "Enter."
                        l "This is nice."
                        n "Shhhhh."
                        n "On your knees."
                        n "Good slut."
                        n "Now, lick my dick."
                        n "If you aren't going to do it, you can leave."
                        n "Yes, I'm aware that it's your sister's cum."
                        n "But you're the one that followed her here, aren't you?"
                        n "So you're going to clean it up."
                        n "There you go."
                        n "Mmmmm."
                        n "You were right, this is hot."
                        n "I enjoy having this kind of control over you."
                        n "Especially when I tell you that I'm not going to fuck you."
                        n "I'm going to let you swallow my cum, but we aren't going to fuck."
                        n "Although you can always come back tomorrow."
                        n "This is turning you on, isn't it?"
                        n "You like being submissive to me."
                        n "That's because this is where you belong."
                        n "On your knees, tasting your sister's pussy on my dick."
                        n "Getting her sloppy seconds."
                        n "But you don't know the half of it."
                        n "Since I last showered, I've fucked... let's see..."
                        n "Leah."
                        n "Ashley."
                        n "Jenn."
                        n "Haley."
                        n "Grace."
                        n "And Brittany."
                        "Laura moaned."
                        n "How does it taste to have all of your friend's juices in your mouth right now?"
                        n "You are drinking Jenn."
                        n "But don't think about it too hard."
                        n "Because you're about to drink me."
                        n "Are you ready?"
                        n "Yessssss."
                        n "Fuck yeah, Laura!"

                        n "Well hot damn you're a good cocksucker!"
                        n "Now get the fuck out of my house."

                        n "Huh."


                    "No deal":
                        n "Fuck off."
            "No":
                n "Actually..."
                n "I'm not sure we should see each other anymore."
                b "Ha, ha."
                b "What's your address?"
                n "I'm serious."
                n "I was talking to the other girls today, and I promised them-"
                b "Them? Like, multiple girls?"
                n "Yeah."
                b "So they are okay with you fucking other girls."
                n "Yes."
                n "But only each other."
                b "This is too damn confusing."
                b "Are you sending me your address or not?"
                n "Uhh..."
                b "I won't tell anyone."
                menu:
                    "Okay [blue]\[Brittany Side\]":
                        n "...fine."
                        b "See you soon."
                        jump okaybrit
                    "Sorry":
                        n "Sorry, Brit."
                        b "Asshole."
                        "She sighed."
                        b "I'm sorry."
                        b "I'm just..."
                        n "I know."
                        b "Call me when you change your mind, okay?"
                        n "I won't."
                        b "Damn it."
                        "I hung up."
                        scene bg black
                        with fade
                        pause
                        "{b}An Hour Later{/b}"
                        jump lauracalling
    else:
        "{b}Three Hours Later{/b}"
        label lauracalling:

        scene aptv
        with fade

        "Laura called me again."
        menu:
            "Answer":
                n "I have nothing to say to you."
                l "I realize that, [n]."
                l "I caught on the twelfth time you ignored my call."
                n "Then why are you still calling?"
                l "I think you can guess."
                n "Nope."
                l "I need you."
                n "Alright, I'll bite."
                n "Why do you need me, Laura?"
                l "I need your dick!"
                l "It's been two weeks, do you realize that?"
                l "I can't think of anything else."
                n "I thought it wore off over time?"
                l "Why did you think that?"
                l "Has it happened with anyone else?"
                n "I guess not."
                l "Right."
                l "So..."
                l "I can come to you."
                l "You can fuck me and I'll leave."
                l "We don't even have to talk."
                n "I don't know..."
                l "Look, you don't have to worry about me knowing where you live."
                l "I'm not going to stalk you or anything."
                l "Plus, I already know you moved into your uncle's place."
                l "I just need... {w}your dick."
                menu:
                    "Okay [blue]\[Laura Side\]":
                        $ lauraside = True
                        n "I guess."
                        if fuckedtif:
                            "There was a knock on my door."
                            n "Hey, someone is here."
                            n "And I'm pretty tired."
                            n "How about you come over tomorrow instead?"
                            l "Okay!"

                            jump ftif
                        if fuckedbailey:
                            "There was a knock on my door."
                            n "And I'm pretty tired."
                            n "How about you come over tomorrow instead?"
                            l "Okay!"
                            jump fbailey
                        n "But honestly, I'm just relaxing today."
                        n "How about you come over tomorrow instead?"
                        l "Okay!"
                    "Hang up":
                        n "Laura, I want to tell you something from the bottom of my heart."
                        n "Fuck off!"
                        "I hung up."
            "Ignore":
                n "Fuck off."
        if fuckedtif:

            "There was a knock on my door."
            label ftif:
            image taptani1 = Movie(play="taptani1.webm")
            scene taptani1
            with fade
            pause
            t "Hey!"
            n "Tiffany!"
            n "To what do I owe the pleasure?"
            t "Oh, no reason in particular."
            t "I had a nice night with you and wanted to see if you wanted to do it again."
            n "Sounds like a pretty good reason to me."
            t "Right?"
            menu:
                "Invite her in [blue]\[Tiffany Side\]":
                    $ tifside = True
                    n "Would you care for a tour?"
                    t "Why, yes!"
                    t "I'm always curious to see how my neighbors live."
                    n "Right this way."
                    scene bg black
                    with fadeout
                    centered "That's all, folks!"
                    centered "I'll have the rest of this update for you as soon as I can."
                    jump afterend

                "Turn her down":
                    n "Well I must say I had a lovely time with you as well."
                    n "Unfortunately, I won't be able to repeat it with you tonight."
                    t "No problem."
                    t "I also simply wanted to come over and say hi."
        if fuckedbailey:
            "There was a knock on my door."
            label fbailey:
            image hbaptani1 = Movie(play="hbaptani1.webm")
            scene hbaptani1
            with fade
            pause
            ba "Hey."
            n "Hey!"
            n "Hottie Bartender!"
            ba "I do have a name."
            n "Bailey!"
            ba "Better."
            n "You came back."
            n "How did you get upstairs?"
            ba "Please."
            n "I guess I'm going to have to raise my security."
            ba "Aren't you more impressed that I found your place again, despite being entirely drunk the last time I was here?"
            n "Kind of, yeah."
            ba "I don't know what it is."
            ba "But I've been craving you all week."
            n "You flatter me!"
            ba "I'm serious."
            ba "I can't seem to get you out of my head."
            menu:
                "Invite her in[blue]\[Bailey Side\]":
                    n "I wouldn't mind getting back in there."
                    ba "What?"
                    label onbailey:
                    $ baileyside = True

                    n "Come on in."
                    ba "Thanks."
                    centered "That's all, folks!"
                    centered "I'll have the rest of the update for you as soon as I can."
                    jump afterend
                "I can't":
                    n "I get that a lot."
                    ba "So, are you going to invite me in?"
                    n "Actually..."
                    n "I can't."
                    ba "Oh?"
                    n "I'm starting to get serious with someone."
                    ba "Is it the blonde?"
                    n "No, actually."
                    n "It's..."
                    n "A few people."
                    ba "Oh?"
                    ba "Then I won't bother you."
                    ba "Unless..."
                    n "Hmm?"
                    ba "We've already had the 'first time ever' sex."
                    ba "I thought it was pretty amazing."
                    n "It was."
                    ba "So we could always have 'last time ever' sex."
                    n "When would we do that?"
                    ba "We could take a vote."
                    ba "I vote now."
                    menu:
                        "Accept":
                            n "Aye."
                            jump onbailey

                        "Decline":
                            n "Looks like a draw."
                            n "Thanks for coming by, Bailey."
                            n "It was fun."
                            ba "It was indeed."
                            ba "Bye, [n]."


    scene bg black
    with fadeout
    pause
    "{b}The Next Day{/b}"
    with fade
    "{i}Knock Knock{/i}"
    scene apartmentbed2
    with fade
    pause
    n "What good is having a doorman if she lets everyone up?"
    image laptani4 = Movie(play="laptani4.webm")
    scene laptani4
    with fade
    pause
    n "Oh!"
    "Girl" "Hey."
    n "I was about to call downstairs and complain about all the visitors coming up unannounced."
    "Girl" "Has that been a problem for you?"
    n "Once or twice."
    "Girl" "Then perhaps I should get back downstairs."
    "Girl" "I wouldn't want to let you down."
    n "Well..."
    n "I'm not {i}that{/i} upset."
    n "What can I do for you?"
    if btgg:
        "Girl" "I don't know, something about a tour?"
    "Girl" "I have an hour lunch break to burn."
    n "So we have Keith downstairs protecting us?"
    "Girl" "Indeed."
    n "Well then."
    n "I feel safe."
    n "How about you?"
    "Girl" "Not around you, no."
    n "Smart."
    menu:
        "Invite her inside [gr]\[Big Titty Goth Girl\]":
            $ btgg = True
            n "So..."
            n "Want a tour?"
            "Girl" "Impress me."
            n "I apologize, but it has to be quick."
            n "I need to leave for class in about twenty minutes."
            "Girl" "No worries."
            "Girl" "This place can't be that big."
            n "Right."
            scene apartment4
            with fade
            pause
            "Girl" "Aha, the pool!"
            "Girl" "It's not that large."
            n "Only as big as it needs to be."
            "Girl" "Right."
            scene apartment5
            with dissolve
            n "So, are you allowed to have a drink on your lunch breaks?"
            "Girl" "I'm not big on drinks."
            "Girl" "I'm more of an edibles kind of girl."
            n "Aha."
            n "That I don't have."
            n "At least, not that I know of."
            "Girl" "That's okay, I had one about twenty minutes ago."
            "Girl" "And it's going to kick in here anytime."
            n "It takes the edge off at work?"
            scene apartment9
            with fade
            "Girl" "And life."
            "Girl" "Plus it gives me the courage to do dumb shit like come up here."
            "Girl" "So, do I get to see the upstairs?"
            n "I'm afraid that section is saved for the forty minute tour."
            "Girl" "Riiight."
            image laptani5 = Movie(play="laptani5.webm")
            scene laptani5
            with fade
            pause
            "Girl" "So I'm confused."
            "Girl" "You haven't made a move on me yet."
            n "That's because I'm a gentleman."
            "She snorted."
            "Girl" "So... you probably don't know this."
            "Girl" "But I've been asking each girl that comes up here what they see in you."
            n "I'm aware."
            n "They all think you're obsessed with me."
            "Girl" "I'm not!"
            "Girl" "But I could see why they would think that."
            n "Oh yeah?"
            "Girl" "I just don't get it."
            "Girl" "They all know about each other."
            "Girl" "So why do they all still deal with your bullshit?"
            n "What do they say?"
            "Girl" "I've heard a few different answers."
            "Girl" "One is that you are packing serious weaponry."
            "Girl" "But the most common one is that your sperm is delicious."
            "Girl" "I think the short one even said it was addictive."
            n "Huh."
            n "No one mentioned my great cooking?"
            n "Or my generosity or conversation skills?"
            n "How depressing."
            "Girl" "So I don't know what I expected coming up here."
            "Girl" "But I was picturing you trying to throw me against the wall, or at least being all grabby and shit."
            n "Only on the weekends."
            "Girl" "Hmm."
            "Girl" "So what would it take to see your aggressive side?"
            n "You want me to drop the gentleman persona?"
            n "Because I don't do that until I learn a girl's name."
            "Girl" "I forgot about that."
            "Girl" "Actually, I'm still kind of pissed that you forgot it."
            "Girl" "How about this:"
            "Girl" "Guess my name right and I'll stay."
            n "Do I get a hint?"
            "Girl" "...no."
            n "It's-"
            "Girl" "You only get one guess."
            menu:
                "Kathy":
                    n "Kathy."
                    "Girl" "Wrong."
                "Lisa Marie":
                    n "Lisa Marie."
                    "Girl" "Yep."
                    n "Yeally?"
                    "Girl" "Yeah, no."
                "Donna":
                    n "Donna."
                    "Girl" "Close."
                "[gr]Lydia":
                    n "Lydia."
                    lyd "See?"
                    lyd "I knew you were fucking with me."
                    n "Totally was."
                    n "I like it."
                    lyd "Thanks."
                    pause
                    lyd "That's it?"
                    lyd "No references to Beetlejuice?"
                    n "Careful! That's twice now!"
                    lyd "Right."
                    lyd "You're different."
                    n "You find me mysterious."
                    n "I almost hate to shatter that for you."
                    lyd "So you are going to turn out to be boring and ordinary?"
                    n "Everyone is when you get to know them."
                    lyd "I disagree."
                    lyd "You have all these girls coming back."
                    lyd "I could get a guy to go home with me."
                    lyd "But getting him to return?"
                    lyd "I had to get really good at giving head."
                    lyd "What did you do?"
                    n "You really want to know?"
                    lyd "That's why I'm here."
                    pause
                    n "Still waiting for me to be the aggressor, huh?"
                    lyd "That's my nature."
                    lyd "I'm a sub."
                    n "I don't believe in the full distinction."
                    n "Every interaction is a dance of submission and domination."
                    n "This time, I'm going to let you be the aggressor."
                    lyd "You want me to dominate you?"
                    n "No."
                    n "I want you to be the one to make the first move."
                    n "And the second. And third."
                    lyd "Oh."
                    n "Are you up for that?"
                    lyd "Somehow, it seems even more submissive."
                    n "It very well could be."
                    lyd "Okay."
                    lyd "Oh, fuck."
                    lyd "Now I'm nervous."
                    lyd "I really don't want to turn into one of your tramps."
                    n "Groupies."
                    lyd "But I'm so fucking curious."
                    n "Alright, here's the only move I'll make."
                    label galleryScene67:
                    "I dropped my pants."
                    lyd "Fuck."
                    lyd "That's for me?"
                    n "Yep."
                    lyd "I am so not going to fuck you."
                    n "No problem."
                    n "Ten minutes wouldn't be enough for that anyway."
                    lyd "Mmm."
                    lyd "I'm going to put that in my mouth."
                    lyd "And I'm going to give you a better blowjob than any of your girls."
                    n "That's what they all say."
                    lyd "Sit."
                    lyd "On the couch."
                    scene bg black
                    image laptani6 = Movie(play="laptani6.webm")
                    scene laptani6
                    with fadehold
                    pause
                    n "Holy!"
                    pause
                    n "Girl, you got talent!"
                    lyd "Mmm."
                    n "You're twisting, you're using your tongue in all the right ways..."
                    n "You even have the right amount of sucking action!"
                    pause
                    n "And you're spoiling me for the other girls."
                    pause
                    n "You aren't even coming up for air!"
                    n "Or giving me witty retorts."
                    pause
                    n "This just might be the best BJ I've ever-"
                    scene bg black
                    image laptani7 = Movie(play="laptani7.webm")
                    scene laptani7
                    with fade
                    pause
                    n "Fuck me!"
                    n "You're taking it deep!"
                    pause
                    n "How is your throat this good?"
                    n "Mother fuck!"
                    n "Lydia!"
                    lyd "Mmm hmm?"
                    n "I'm going to cum!"
                    lyd "Mmm hmm!"
                    n "You got me-"
                    with flash
                    n "AHhhhhhHHHH!"
                    with flash
                    lyd "Mmmmmmm."
                    pause
                    $renpy.end_replay()
                    scene bg black
                    with fadeout
                    centered "That's all, folks!"
                    centered "I'll have the rest of this update out as soon as I can."
                    jump end

                "Moria":
                    n "Moria."
                    "Girl" "You wish."
                "Raven":
                    n "Raven."
                    "Girl" "I like that."
                    "Girl" "But no."
            "Girl" "Thanks for playing."
            "Girl" "Maybe next time."
            n "Nooo!"
            scene bg black
            with fadeout
            centered "That's all, folks!"
            centered "Save her, and I'll have the rest of this update out as soon as I can."
            jump end


        "Send her away":
            $ btgg = False
            n "Well, my apologies, nice Big Titty Goth Girl, but I was just on my way out."
            "Girl" "Oh?"
            n "Gotta get to class."
            "Girl" "That's too bad."
            "Girl" "Maybe another time, then."
            n "Maybe!"
            "Girl" "Interesting."
            n "Oh?"
            "Girl" "Just when I thought I had you figured out..."
            scene bg black
            with fadeout
            centered "That's all, folks!"
            jump end
    jump end
    # What happens next?
    #  Tiffany comes over for a bang. Laura calls and tries to convince you to fuck her as well. Then Lydia comes to try to suck your dick.
    #  If you fucked any of the girls beside Laura, you knock them up and the other girls all leave you.
    #  If burger, the girls grow fairly large by the time of the graduation. Your uncle returns, kicking you out.
    #  You have nowhere to go, so you end up living with Laura again if you decided to fuck her. If not, you quit school get a part time job to get a shitty apartment
    #  If not, you let the girls make a bunch of money and you all are able to move out and get a place together.
    #  There you can watch the girls blow up, fucking them the entire time.
    if huge:
        "{b}A Week Later{/b}"
    else:
        "{b}Two Weeks Later{/b}"

    a "Hey, do my tits look bigger to you?"
    n "Not at all."
    a "That's because you saw them yesterday."


    if huge:
        a "Here, look at this picture from only a week ago."
        n "Huh."
        a "You can see a difference between each day's photo."
    else:
        a "Here, look at this picture from only two weeks ago."
        n "Huh."
        a "You can almost see a difference almost every day."
    n "Wait, you take a topless selfie every day?"
    a "Of course."
    a "Gotta see that progress."
    n "How long have you been doing this?"
    a "Since I started growing."
    n "Huh."
    n "Can I have these?"
    a "You wish."
    n "Wait... why not?"
    a "Because they aren't for you."
    a "I wasn't trying to be sexy in them."
    a "Well, except for the ones I already sent you."
    n "Doesn't matter."
    n "Posing is overrated."
    a "The point is, I'm still growing."
    a "A lot."
    a "All the girls are."
    n "I'm sorry."
    a "Are you?"
    a "I feel like you still enjoy it."
    menu:
        "I do":
            n "I do, yes."
            n "But not if it makes you miserable."
            a "I'm not there yet."
            a "But I am worried."
            if huge:
                a "I'm not saying I've been all that careful about what I'm eating."
                a "But I've reached the point where I should be."

            else:
                a "I've been careful about what I eat."
                a "But all I'm doing is slowing down the growth."

        "I did":
            n "I did, yes."
            n "But you girls are getting top-heavy enough for my taste."
            a "Getting?"
            a "Haven't reached it yet?"


    n "I think you look amazing."
    a "Does that mean I should start dieting and hit the gym?"
    n "If that's what you think you should do."
    a "I do."
    if huge:
        a "But first..."
        a "I need to catch up to Grace."
        n "Oh?"
        a "Did you just get hard?"
        a "Picturing me... {w}bigger?"
        n "Maybe."
        a "Noted."
        n "So you aren't going to beat Haley?"
        a "Oh hell no."
        a "No one is catching up with that girl."

    a "So what's up with you?"
    n "I'm going to need to find a job."
    n "All my savings is used up and I'm starting to regret signing up for a credit card."
    a "What are you thinking?"
    n "Maybe bartending?"
    a "But then you'll be busy on nights and weekends."
    a "Which is the only time I get to see you."
    n "Yep."
    a "Boo."


    a "I have an idea for money."
    n "Yeah?"
    n "Tell me."
    a "We take advantage of these giant freakin' racks."
    n "How do we do that?"
    a "Exactly the way you expect."
    n "Stripping?"
    a "That's old school!"
    a "You know we have been taking pictures of ourselves every day to track our development?"
    n "I heard about that, yeah."
    a "What if we made an Instagram?"
    a "Leah and I could probably get a ton of followers."
    n "Don't you already have one?"
    a "Yeah, but we haven't really posted any recent photos."
    n "So you get a lot of followers. Then what?"
    a "We promote skincare products."
    a "That kind of shit."
    n "Yeah?"
    n "Cool, I'll start promoting you right now."
    n "Hey, everyone!"
    n "Check out Ashley's Instagram!"
    n "You can watch her tits get bigger with every post!"
    a "Yeah, that'll work."
    n "Are you going to have a Twitter account too?"
    a "I dunno. Why?"
    n "Because then you can post nudes."
    a "You might be thinking of OnlyFans."
    n "Right."
    n "But then you could set goals for retweets before you post new photos."
    a "Interesting."
    a "So..."
    a "This is the spot."
    n "Right?"
    a "Do I really have to go back home tonight?"
    n "Not if I wake up early and drive you to school."
    a "You'd do that for me?"
    n "If you made me."
    a "Ha!"
    a "It's okay."
    a "The train is good times."
    n "What happened to convincing your mom to buy you a car?"
    a "What does it matter?"
    a "My tits are going to get so big I won't be able to fit behind a steering wheel soon."
    n "Hmm..."
    a "I can't wait until I graduate."
    n "Yeah?"
    a "Then I could stay here whenever I want."
    n "That sounds awesome."
    a "Actually, how long can you stay here?"
    a "Have you heard from you uncle?"
    n "Yeah, he called to check in last week."
    n "He's taking my aunt down to Africa to go on a safari."
    a "Awesome!"
    a "Did you tell you to do anything?"
    n "Yeah, he asked me not to let anyone come over except for my girlfriend."
    a "I assume you didn't tell him that you have multiple girlfriends?"
    n "Is that not normal?"
    a "Mmm hmm."
    a "Hey, want to go another round?"
    n "You still aren't sore?"
    a "Magic pussy."
    n "That's right!"
    n "So... balcony sex?"
    a "I'm not Leah."
    a "How about you fuck me on the piano?"
    n "Don't tell my uncle."















    # ------------------------------------------Laura's backstory------------------------------------------

    "Three Years Ago"
    with fade
    play sound "fellin.mp3" noloop fadeout 4.0
    "We see Laura and her friend bullying a girl."
    n "What are you ladies doing?"
    l "Oh, we are just trying to help Charlotte with some fashion tips."
    l "Oh my god, Charlotte! We should do a makeover!"
    n "Charlotte, are you okay?"
    "Charlotte" "I- I guess so."
    n "What's your name?"
    l "Laura."
    l "And this is Jasmine."
    n "I recognize you."
    n "I've seen you bully girls before."
    n "Charlotte, don't take this situation personally."
    n "This is about Laura and her friend being a bitch, not about you deserving it."
    "Charlotte" "Oh- okay."
    n "Laura, what's wrong with your life?"
    l "What?"
    n "Did your parents get a divorce?"
    l "No-"
    n "Have you had an abusive childhood?"
    l "No-"
    n "Were you bullied by girls in middle school?"
    l "Yes!"
    n "Then you should know better."
    n "For every shitty situation you get in life, you can do two things."
    n "You can learn from it or you can let it eat you."
    n "Don't let the bullies win, Laura."
    n "Do you know what I'm saying?"
    l "I think so-"
    n "I'm telling you to stop acting like a fucking cunt."
    n "If I see you bullying a girl again, I'm going to personally come after you."
    n "Got it?"
    l "Umm... yes?"
    n "Good."
    "[n] walks away, but we stay with Laura."
    "Jasmine" "Wow, fuck that guy."
    l "No. He's right."
    "Jasmine" "What?"
    l "Why are we doing this, anyway?"
    "Jasmine" "Holy shit! You are crushing on him, aren't you?"
    l "What? No!"
    l "But I'm pretty sure [n] likes me."
    "Jasmine" "How do you know his name?"
    l "I've seen him around."
    l "You know what? You might be right too."
    l "I need a man in my life."
    l "Someone to call me on my shit."
    "Jasmine" "Damn, girl."
    "Three Weeks Ago"
    "We cut to a replay of the events at the bowling alley."
    g "Why did we dress up to go bowling?"
    g "It's fucking embarassing."
    g "Who's that guy?"
    l "Who?"
    g "The one you're staring at."
    l "Oh. He was a senior when I was a freshman."
    l "I used to have the biggest crush on him."
    l "I thought he was going to change me or something."
    g "Change you?"
    g "What a douche."
    g "Wait, what's that smile?"
    l "You wouldn't hit it?"
    g "Hell no."
    l "Huh."
    g "He could mind his fucking business."
    l "Maybe."
    g "All you, girl."

    "Ten Days Ago"
    g "Hey, so you know how you're my best friend, right?"
    l "Yeah?"
    g "Well..."
    g "I have to tell you something."
    g "I asked [n] to hypnotize me."
    l "Why?"
    g "You know."
    g "I wanted to see if it would work."
    l "Your boobs?"
    g "Yeah. Why not?"
    g "Anyway, I wanted you to hear it from me."
    g "I sucked his dick."
    l "What?"
    g "He said if I wanted bigger boobs, I needed to give him head in the bathroom."
    g "This was at a coffee shop."
    l "Grace!"
    l "Did he make you do it?"
    g "No, I think he was joking."
    g "He probably would have hypnotized me either way."
    g "But he pulled it out."
    g "And it was nice."
    g "The only reason I'm telling you is that I know you used to like him."
    g "And I don't want anything to come between us."
    l "Wow."
    l "Okay."
    l "Thanks for telling me."
    l "Have your boobs grown?"
    g "No."
    g "But it's only been an hour."
    l "Wait, you just sucked his dick?"
    g "Yeah, over lunch break."
    l "Damn, girl."
    g "I know."

    "Eight Days Ago"
    "We cut to Laura looking in the mirror with cum on her face."
    "She smiles."
    l "He likes you, girl."
    l "You did it."
    l "He actually likes you."

    "A Week Ago"
    "We catch Laura's POV as she climbs into [n]'s bed."
    l "Hey, it's me."
    l "[n]!"
    l "Wake up!"
    l "I know how to wake you up..."
    l "I'm going to surprise the shit out of you."
    l "Oh! Yes!"
    l "HOLY SHIT!"
    l "You're enormous!"
    n "What-"
    n "Who-"
    l "Mmmm."
    n "I'm going to-"
    n "YES!"
    n "Oh, fuck yeah!"
    n "Mmm... Leah."
    l "Leah?"


    "Five Days Ago"
    "We cut to a replay of the dinner date."
    "We see more of Laura's thoughts in her internal dialogue."

    "Three Days Ago"
    "We cut to a replay of the events of the night when Laura and Grace hook up with [n] in the hot tub."
    l "Holy shit."
    l "I can't believe we fucked."
    g "I can."
    g "Seems like it's exactly what you wanted."
    l "It is!"
    l "I've wanted it for years."
    g "Was it every bit as magical as you expected?"
    l "Yes."
    g "Wow, there was no sarcasm there."
    l "It was magical."
    g "Are we talking about the same guy?"
    l "Yeah."
    l "Wait, it wasn't good for you?"
    g "I'm not saying that!"
    g "The sex was really good."
    l "But?"
    g "But nothing."
    g "I can't be getting too serious with him."
    l "Why not?"
    g "Have you looked at yourself?"
    g "You are serious enough for the both of us!"
    l "Yeah..."
    with fade
    "Yesterday"
    with fade

    "We cut to Laura catching the MC fuck every girl in the party, her face dropping each time."
    "She takes the first aid kit back to the bathroom."
    l "What's this?"
    l "Ha! Why are you here?"
    l "I wonder if it works?"
    "We watch her hypnotize Leah and Ashley as they leave."
    l "-and you don't like even like [n] anymore."
    l "You are pissed off at him, and you are no longer addicted to him."
    "Leah and Ashley" "Okay."

    with fade

    "Laura's Mom" "Honey, what's wrong?"
    "Laura's Mom" "You know you can talk to me about it."
    l "No. I can't."
    "Laura's Mom" "Is it about a boy?"
    l "No."
    l "Yes."
    "Laura's Mom" "It's the one your sister was telling us about, isn't it?"
    "Laura's Mom" "She said you liked him."
    l "Yes."
    l "I wanted him to like me."
    pause
    l "I even-"
    l "I'm so stupid."
    pause
    l "I bought us tickets to go on a cruise together."
    "Laura's Mom" "You did? When?"
    l "For tomorrow."
    "Laura's Mom" "Laura! You have school."
    l "I know."
    pause
    "Laura's Mom" "I have an idea."
    "Laura's Mom" "What if you take me instead?"
    l "What?"
    l "You would let me go?"
    "Laura's Mom" "Not with a boy I've never met! How bad of a mother do you think I am?"
    "Laura's Mom" "But I think we could use a girl's trip."

    "Laura's Mom" "Don't tell your father I'm letting you drink."
    l "Okay, Mom."
    "Laura's Mom" "Speaking of your father, did I ever tell you how I won him over?"
    l "Yes, Mom."
    "Laura's Mom" "I don't think you heard the full story."
    "Laura's Mom" "Your father was a very eligible bachelor back in the day."
    "Laura's Mom" "He had several girls fighting over him."
    "Laura's Mom" "So do you know what I did?"
    l "You sabotaged them?"
    "Laura's Mom" "Damn right."
    "Laura's Mom" "I started a rumor that one of them had herpies."
    l "I remember, Mom."
    "Laura's Mom" "And I told the other one that I would punch her face in."
    l "If you keep telling this story, Dad is going to hear it one day."
    "Laura's Mom" "I'm not worried about that."
    "Laura's Mom" "Men like it when you fight for them."
    l "Not this one."
    "Laura's Mom" "Are you sure?"
    "Laura's Mom" "Maybe you haven't figured out what he really wants yet."
    "Laura's Mom" "Actually, forget about him."
    "Laura's Mom" "We're on a cruise!"
    "Laura's Mom" "There are a hundred boys that would be lucky to get to know my daughter."
    l "No thanks."
    "Laura's Mom" "It would be a great way to take your mind off of him."
    l "Pass."
    "Laura's Mom" "Alright, fine. Let's talk about him."
    "Laura's Mom" "What did you like about this boy, anyway?"
    l "He calls me on my shit."
    "Laura's Mom" "What's that supposed to mean?"
    l "Sometimes I don't feel like I'm all that great of a person, you know?"
    "Laura's Mom" "No, I don't know! I raised my daughter to be an upstanding lady."
    l "Like you're such a great example yourself, Mom."
    "Laura's Mom" "What are you saying?"
    l "You didn't mention where you disappeared for three hours last night."
    "Laura's Mom" "I told you! I was at the Casino."
    l "Odd. Because I was at the Casino."
    "Laura's Mom" "You must haved missed me."
    l "Anyway, I'm not judging you, mom."
    l "I'm judging myself."
    l "And sometimes I'm mean for no reason."
    l "I've bullied girls-"
    "Laura's Mom" "I'm sure they deserved it."
    l "No, Mom."
    l "I didn't deserve it when I was bullied."
    l "And I went to far."
    l "Everyone in my school hates me right now."
    l "Like, really, really hates me."
    "Laura's Mom" "So what are you going to do?"
    l "I don't know."
    "Laura's Mom" "Well, you aren't a quitter."
    "Laura's Mom" "I'll tell you what you are going to do."
    "Laura's Mom" "When we get back, you're going back to that school and you're going to act like nothing has happened."
    "Laura's Mom" "Any time one of those girls in your class are mean to you, you act confused and hurt."
    "Laura's Mom" "Turn their games right back on them."
    l "This is what I'm talking about, Mom."
    "Laura's Mom" "What?"
    l "I don't even know how to explain it."
    l "He's the only one that made me believe I could be better."
    l "Like maybe I don't need to be a bitch all the time."
    "Laura's Mom" "There's nothing wrong with being a bitch."
    "Laura's Mom" "Bitches win."
    l "I don't know."
    l "Maybe."


    "Cut to Laura returning to the school, finding the MC and following him to hypnotize all the girls."
    "Depending on his actions, she is either relieved to see that he used the watch for good or is horrified to see that he doesn't."




    stop sound fadeout 5.0

