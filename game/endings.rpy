
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
    "I didn't make it home until Monday night."
    scene bg bedroom3
    with fade
    pause
    "My phone had blown up with over a hundred calls, text messages and snaps."
    "But I was too damn tired to answer any of them."
    scene bg black
    with fade
    pause
    "{b}Tuesday Morning{/b}"
    "Leah woke me up before school and tried to give me a blowjob, but she couldn't fit me into her mouth."

    "She was barely able to slip me inside of her."
    image lmr = Movie(play="lmb.webm")
    show lmr
    window hide
    pause
    "But once we got started there was no problem."

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
        "Next, I fucked Ashley."
    else:
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
    pause
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
    "{b}Thursday Morning{/b}"
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
    centered "More to come in future updates."
    jump end




# -------------------------------------------      Laura Ending 2     ------------------------------------------------

label lauraendtwo:
    n "We could go somewhere cheap."
    n "I'll look up cruises."
    scene bg black
    with fade
    "I did some research and found a week long cruise special."
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

    "{b}Thursday Morning{/b}"
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
    "{b}Sunday Evening{/b}"
    "{b}Adults Only Hot Tub{/b}"
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
    pause
    "{b}Monday Morning{/b}"
    with fade
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
            scene backseat
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
    pause
    centered "Thanks for playing the ending!"
    if ashleyswallow:
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
    jump end




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
    "Two Weeks Ago"
    "We cut to a replay of the events at the bowling alley."
    g "Why did we dress up to go bowling?"
    g "It's fucking embarassing."
    g "Who's that guy?"
    l "Who?"
    g "The one you're staring at."
    l "Oh. He was a senior when I was a freshman."
    l "I used to have the biggest crush on him."
    l "Thought he was going to change me or something."

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
    "She cuts herself while cutting a lime and goes to the bathroom for the first aid kit."
    l "What's this?"
    l "Ha! Why are you here?"
    "We cut to Laura catching the MC fuck every girl in the party."
    "She looks distressed."
    l "Fuck this."
    l "I'm grabbing the watch."
    "We watch her hypnotize Leah and Ashley as they leave."
    l "-and you don't like even like [n] anymore."
    l "You are pissed off at him, and you are no longer addicted to him."
    "Leah and Ashley" "Okay."
    with fade
    "Thirty Minutes Ago"
    with fade
    "We see Laura on her phone, looking at her phone and wearing headphones."
    "She is texting before picking up the phone and dialing."
    "We see her have the conversation with Leah and then with the MC."
    "When she hangs up we see her face light up."
    "She dances around her room in excitement."
    "She jumps back into bed and waits for the MC with a giant grin on her face."
    "He lays into bed with her."
    "She kisses him."

    stop sound fadeout 5.0
