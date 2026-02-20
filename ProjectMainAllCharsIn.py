import random
import collections
import math
import tkinter
from time import sleep

"""
Docstring for project 1
"""



"""
personality types


person x: food obscessed, sarcastic, manipulative, peer-
person y: bully, abrasive
person z: meek, needy lil' guy, 


30 distinct ones, 5-10 variable standard


"""

#global variables
startval = 45 #this changes the starting number in MainScore. This is for us to tinker with to adjust difficulty/game length
score = int(startval) + 1
score2 = int(startval) - 1
score3 = int(startval)
finalscore = score + score2 + score3
 
#person1Questions = {"question": [["answer1", score, checkpoint1, 'otherFriendEffects'], ["answer2", score2, checkpoint2, 'otherFriendEffects2'] ["answers3", score3, checkpoint3, 'otherFriendEffects3']] <- example 
person1 = {"Cameron: Hey {player_name}, it’s Cam again. Just leaving you a mess-\nwait a minute… Holy hell, you picked up!": 
           [["1) Yeah... hey buddy!", score], 
            ["2) I would've called back eventually.", score2], 
            ["3) I'm as shocked as you are if I'm being totally real right now.", score3]],
            "Cameron: Dude! It’s been like… I don’t even know actually when the last time\nwe talked was.": 
            [["1) Not that long I don't think.", score], 
            ["2) Oh gee, I wonder why.", score2], 
            ["3) Yeah, it's been a hot minute.", score3]],
            "Cameron: Where have you been? Lemme guess, you also got your life eaten by\nthat really extensive story driven fantasy game that came out a while back?": 
            [["1) Are you saying a look like some kind of nerd?", score], 
            ["2) ... yes. That is exactly what has been happening. Nothing else.", score2], 
            ["3) I mean... no?", score3]],
            "Cameron: Ugh... I wish I had time for games. I’ve had to set it down because\nwork ramped up again.": 
            [["1) Already?", score], 
            ["2) I think I remember you talking about this.", score2], 
            ["3) Oh, wow, bummer.", score3]],
            "Cameron: We're preparing for the seasonal crap six months ahead of time. I’m\nalready tired of hearing about the holidays. Remember enjoying the holidays?": 
            [["1) Oh no... that's the worst.", score], 
            ["2) Mmmhmmm.", score2], 
            ["3) It's not nearly that bad.", score3]],
            "Cameron: You’re still coming to Johnny’s party tonight right? You know it’s\ngonna be good. The guy always says he’s got a few things and then BOOM, whole\nfricken buffet of stuff you’ve never even heard of. Some of it you never\nwanted to hear of.": 
            [["1) Oh shoot... I forgot...", score], 
            ["2) Nah, I'm going to skip it.", score2], 
            ["3) That sounds great but I'm thinking of staying home tonigh.", score3]],
            "Cameron: Hazelnut spread, banana pizza was a bit weird. I think it would’ve\nbeen better with cheese…": 
            [["1) I missed that one, it sounds like a recipe for stomach sadness.", score], 
            ["2) I'm sorry, but what did you just say to me? God no.", score2], 
            ["3) Ugh... sure.", score3]],
            "Cameron: Johnny’s got weird taste but I don’t think he’s a bad guy. Don’t be\nsurprised if you hear from him too.": 
            [["1) Noted...", score], 
            ["2) Yeah, he's an alright guy.", score2], 
            ["3) I genuinely can't stand him. It's why I don't want to go to the party.", score3]],
            "Cameron: He also got a new cat. Have you seen the pictures in the group chat?": 
            [["1) Oh... Good for him.", score], 
            ["2) No, and I don't want to. I hate cats on a fundamental level for complex\n   reasons.", score2], 
            ["3) Why would anyone want a cat?", score3]],
            "Cameron: Wait, you seriously don’t like cats? That’s messed up {player_name}.": 
            [["1) They're just not my favorite things on this planet.", score], 
            ["2) It's a pretty deep rooted dislike, very instinctual.", score2], 
            ["3) They're all a bunch of con artists. They pretend to sound like babies to\n   get you to feed them.", score3]], 
            "Cameron: Well… we’re gonna have some movies on! He’s got a poll going in the\ngroup chat for what we watch.": 
            [["1) Oh, that's fun.", score], 
            ["2) No one's really gonna sit and watch a movie during a party.", score2], 
            ["3) I haven't seen, I've had that thing muted for months.", score3]],
            "Cameron: It's gonna be great! First spot is at a tie between two old horror\nmovies.": 
            [["1) I bet I can guess what kind of movie is in the top spot.", score], 
            ["2) Oh, rad.", score2], 
            ["3) Why are we even bothering with this?", score3]],
            "Cameron: There’s a slasher flick and a werewolf movie.": 
            [["1) Aw damn, I'm gonna miss that.", score], 
            ["2) Of course there is...", score2], 
            ["3) Both are probably lame as hell.", score3]],
            "Cameron: Obviously ‘Guy With Knife III’ is the correct choice.": 
            [["1) Go on... explain your poor choice.", score], 
            ["2) The third anything is when it all goes downhill though.", score2], 
            ["3) I'm a little biased towards the werewolf movie.", score3]],
            "Cameron: Who’s gonna pick a movie about some overgrown pooch when you’ve got the\nclassic horror movie set up that is stupid teenagers get got?":
            [["1) Teenagers get got is so overplayed, it's just a cop out at this point.", score], 
            ["2) But have you considered: big dog go bork?", score2], 
            ["3) Eh, maybe?", score3]],
            "Cameron: Nah dude, werewolves are lame.":
            [["1) Okay. You're wrong, but okay.", score], 
            ["2) That's what makes them fun!", score2], 
            ["3) Slashers are overgrown babies that didn't get enough mommy hugs.", score3]],
            "Cameron: Kinda sad about Sock’s recommendation. They were the only one who\nvoted for ‘The Night is Short, Walk on Girl’. I just don’t think anyone is\ngonna be up for reading subtitles.":
            [["1) I don't even know what that is.", score], 
            ["2) Drunk subtitles leads to puking.", score2], 
            ["3) RIP Sock.", score3]],
            "Cameron: Oh, if movies don’t sell it, there’s also gonna be Karaoke! Everyone\nshould be drunk so no one will care how bad you sound {player_name}.":
            [["1) Oh, rad!", score], 
            ["2) That's cool, I guess.", score2], 
            ["3) My ears are already bleeding.", score3]], 
            "Cameron: Nah, see the way you get ahead of that is to go all in on the most\nridiculous pop song ever. Just give the most hammered performance of your life.":
            [["1) That just seems like a good way to get immortalized for drunk karoake.\n     No thanks.", score], 
            ["2) I'll keep that in mind.", score2], 
            ["3) mmmhmmm.", score3]],
            "Cameron: Oh y’know what I was just thinking about? We never finished that\nboard game from last time.":
            [["1) Proprietorship? I was doing pretty well as the shoe.", score], 
            ["2) Who cares if we didn't finish Apologies?", score2], 
            ["3) I don't think anyone actually gets to the end of Risks.", score3]],
            "Cameron: No, not that one. The one where you build the house and then someone is\na traitor.":
            [["1) Doesn't ring a bell.", score], 
            ["2) Oh yeah! Backstabbing at Shack on the Mountain!", score2], 
            ["3) Sounds like you just hallucinated a memory from your childhood.", score3]],
            "Cameron: Pretty sure Dawn got pissy and scattered the pieces after taking a\nbunch of sanity damage like three times in a row during their turn and then they\nweren’t the traitor.":
            [["1) Classic Dawn.", score], 
            ["2) What a giant baby!", score2], 
            ["3) If they hadn't, I would've.", score3]],
            "Cameron: It could be fun to try it again. We could also play something with a\nrule book that isn’t 45 pages long though.":
            [["1) PLEASE SOMETHING ELSE!", score], 
            ["2) No, I think you're right.", score2], 
            ["3) Maybe see what the room is like first.", score3]],
            "Cameron: So, do you need me to pick you up?":
            [["1) I can't go.", score], 
            ["2) You sneaky bitch, tried to pull a fast one!", score2], 
            ["3) Not in your deathtrap of a car.", score3]],
            "Cameron: Come on dude, my car finally stopped making that sound!":
            [["1) I'm pressing x to doubt.", score], 
            ["2) Neat, your car is still terrifying.", score2], 
            ["3) I'd just rather not.", score3]],
            "Cameron: Well first I thought maybe a racoon or something got in there with\nthe way the speakers were thumping around. Something about the cold and the\nwiring to the radio.":
            [["1) Death. Trap.", score], 
            ["2) This isn't inspiring confidence.", score2],
            ["3) If it's just the radio that was acting up then I guess that's a little\n    less terrifying.", score3]],
            "Cameron: I think it’s unfair to keep calling her a death trap. Her engine hadn’t\nstarted smoking in a good few months!":
            [["1) Oh.... good.", score], 
            ["2) How about we don't?", score2],
            ["3) I CHOOSE LIFE!", score3]],
            "Cameron: Alright, alright. Enough of these lies and slander. Carlotta is a\nfantastic machine and she deserves the world.":
            [["1) She deserves to be buried respectfully.", score], 
            ["2) Fine, I'll tone it down.", score2],
            ["3) Who names their car \'Carlotta\'?", score3]],
            "Cameron: You’re seriously gonna miss out on the party tonight because of \'vague\ntummy troubles\'?":
            [["1) Yeah, unfortunately.", score], 
            ["2) Don't say \'tummy,\' you're a whole ass adult.", score2],
            ["3) It's pretty serious. I'm probably dying.", score3]],
            "Cameron: I mean I can let everyone else know but they’re probably not gonna be\nhappy about it…":
            [["1) They'll find a way to live.", score], 
            ["2) Don't worry about it, I'm probably gonna have to explain to them myself.", score2],
            ["3) I trust you to make me not sound like a complete jackass.", score3]],
            "ENDINGS":
            [["No worries dude, sometimes it just isn’t it. I’ll see you at the next one!", score], 
            ["You’ve been a little on and off this whole time. I’m gonna just stop by to\nmake sure you’re okay.", score2],
            ["Dude. What the hell? Why are you acting like a giant asshole? Forget it. I don’t\ncare what you do.", score3]]}#Cameron - av Joe
person1keys = list(person1.keys()) # this is for the quesiton indexes. This is so the questions and answers dont get mixed up

#DONT convert questions into an f-string. We format the name into it later.
person2 = {"Dawn: {player_name}, I got a funny text from Cameron. He said you’re not\n going to the party tonight. I told him that was a pretty good joke but he\n says he’s serious, so how about you set the record straight for the both of us.": 
           [["1) Ugh… He’s right?", score2], 
           ["2) Okay first, you’re at an 11 when this should be a 4 conversation, and\n   second, yeah I’m staying in tonight.", score], 
           ["3) I’m just not really feeling it tonight.", score3]], 
           "Dawn: And you thought I was just gonna let that go? C’mon, you know what I’m\nabout right? This is a no fly zone for BS {player_name} Are you gonna try to\npretend you have amnesia now?": 
           [["1) I have been feeling a bit forgetful lately.", score3], 
           ["2) There’s no forgetting an asshole like you.", score], 
           ["3) No BS here, these ducks are neat and orderly in their rows.", score2]],
           "Dawn: Oh for the love of… Why do I hang out with you again?": 
           [["1) Your friend options are limited because you greet people by punching them?", score2], 
           ["2) I ask that same question every day.", score], 
           ["3) Because I make the best damn enchiladas you’ve ever had.", score3]],
           "Dawn: That aside, since when do you skip out on free drinks and bad karaoke?\nDon’t give me any of that ‘I’m not feeling it’ crap. We both know that lie’s\nlike a cheap rug.": 
           [["1) I just don’t want to.", score], 
           ["2) Stomach’s being weird, probably not good for drinking. It’ll lead to puking.", score2], 
           ["3) My karaoke is legendary, thank you.", score3]],
           "Dawn: So I’m just gonna tell you what I think. I think you're actively\navoiding us. You blew Cameron off twice in the past month.": 
           [["1) Hey, woah! Let’s back pedal a bit here, I am not avoiding anyone.", score3], 
           ["2) Alright maybe I did dodge a few hang outs, but you’re reaching pretty far \nhere.", score2], 
           ["3) It’s Sock. He’s just so… Wimpy.", score]],
           "Dawn: You also seem to  find every excuse under the sun not to hang out\nwith Sock.": 
           [["1) What did I just say? Are you hard of hearing or something?", score], 
           ["2) It's not that I don't want to hang out with Sock...", score2], 
           ["3) Yeah, and?", score3]],
           "Dawn: And let’s be very clear, only I am allowed to make fun of sad Sock.\nGot it?":
           [["1) Whatever.", score], 
           ["2) Got it.", score2], 
           ["3) Okay buddy...", score3]],
           "Dawn: You get that privilege when you spend the better part of your last two\nyears of high school pulling straws out of his hair and un-gumming his locker.": 
           [["1) Well aren't you just a saint.", score], 
           ["2) I feel like you also are one of the causes of the gum on his \n    locker.", score2], 
           ["3) That's... surprisingly nice of you. Ya'll go that far back?", score3]],
           "Dawn: If you come to the party you’ll get to hear all about the ancient\nhistory. I’ve got tons of stories about what those two chuckle heads got up\nto. No spoilers, that’s a live event or you wait for the day Cameron or Sock\nMAY tell you.": 
           [["1) Well... guess I gotta wait for one of them to spill the beans.", score], 
           ["2) Not even a little spoiler?", score2], 
           ["3) Oh no... anyway.", score3]],
           "Dawn: Seriously {player_name}, you’re telling me with all that, you’d still\nrather rot in that crap apartment watching shitty reruns than hang out with\nus at one of Johnny's parties?": 
           [["1) No, but I just need to stay home and decompress tonight.", score], 
           ["2) Absolutely.", score2], 
           ["3) It’s a toss up really, kind of worried about my… appetite.", score3]],
           "Dawn: Okay if I’m being for real though, I probably would ditch to if it\nwere to re-watch the last season of 12 Desperate Women and 1 Paid Actor.\nI’m more than certain at least one of those women were also paid actors.": 
           [["1) I. am. shocked.", score], 
           ["2) Nah, no way dude.", score2], 
           ["3) I really don't care.", score3]],
           "Dawn: Pretty sure it was the one with the high cheekbones, sharp jawline, and\ntiny nose. Not that first one that everyone thinks of, the other one.": 
           [["1) That's so specific.", score], 
           ["2) I really really don't care.", score2], 
           ["3) Rebecca? No... Tammy?", score3]],
           "Dawn: I know none of it’s real. I'm not a god damn moron. It’s fun to pick at\nbecause it’s so glaringly fake. Like eating chicken nuggets from Clown Burger.": 
           [["1) That's a weird connection between those two things.", score], 
           ["2) Ugh, now I really want chicken nuggets. Damnit, Dawn.", score2], 
           ["3) At least you're not delusional.", score3]],
           "Dawn: Okaaaaay, trash tv aside. You do need to make some kind of effort here\nto hang out with us.": 
           [["1) I mean I really want to, but just not tonight.", score], 
           ["2) Thank god, you're done going on and on about that.", score2], 
           ["3) I do make the effort!", score3]],
           "Dawn: Pretty sure the last time you hung out with all of us was at the beginning\nof the month. We all tried making breakfast with Cameron’s grandma’s prehistoric\nwaffle pan and it almost burned a hole in the counter.": 
           [["1) That only happened because Cameron’s an idiot.", score], 
           ["2) Y’know, I think waffles are an acceptable reason to cause a house fire.", score2], 
           ["3) That wasn’t our best idea.", score3]], #intended answer weights: 1 = high impact, 2 = light, 3 = medium
           "Dawn: I’ve got half a mind to come down there and drag you out myself. How\nmuch do you weigh again? Nevermind, the exact number doesn’t matter, I’m\npretty sure I can deadlift your ass.": 
           [["1) NO! THAT IS FORBIDDEN! NO LIFTING OF THE ME!", score], 
           ["2) That’s a lot of effort for you to waste on my feeble, pathetic ass.",score2], 
           ["3) Wow.", score3]],
           "Dawn: Actually I’m certain I can. I’m up to 1.5x my own body weight. My new\nmetric is gonna be in how many {player_name}’s I can lift.": 
           [["1) That'd be kind of rad actually.", score], 
           ["2) This is dumb. Why are you dumb?", score2], 
           ["3) No. Absolutely not. Don't ever. Bad!", score3]],
           "Dawn: Then you’re going to show up to prevent that very real possibility?\nCan't do much else to prevent the darkest timeline.": 
           [["1) I can hang up.", score], 
           ["2) What if... we just didn't do that? Eh???", score2], 
           ["3) COME AT ME YOU COWARD!", score3]],
           "Dawn: Okay, I’ve got better. If threatening to chuck your ass like the\nuseless boulder you are doesn't work, then think of all the drunken\ndumbassery that you’re gonna miss out on! ...Not that I keep receipts of this\nstuff or anything.": 
           [["1) We both know that’s a lie. I don't even want to know how many lives\n   you've ruined.", score], 
           ["2) Riiiiiight.", score2], 
           ["3) That's just... kind of awful.", score3]],
           "Dawn: Oh come on. What else keeps people in check other than the irrational\nfear that a stranger might think what they’re currently doing is really\nembarrassing? It makes for great currency.": 
           [["1) Now I am more than certain you run a blackmail ring.", score], 
           ["2) That’s a red flag in a pile of red flags.", score2], 
           ["3) Ugh… getting uncomfortable.", score3]],
           "Dawn: Now you sound like sad Sock, ‘D-dawn that’s mu-mu-mu-mean!’ I can’t\ncarry two perpetual whiners, you need to pick a different role.": 
           [["1) How about the guy that stays home from parties?", score], 
           ["2) Maybe I LIKE being a giant crybaby!", score2], 
           ["3) Or you could stop being such a jerk for five whole minutes?", score3]],
           "Dawn: This again? Shelve it. It’s kind of pathetic.": 
           [["1) Not as pathetic as you.", score], 
           ["2) Alright fine, it’s shelved.", score2], 
           ["3) I’m forgetting what the purpose of this conversation was.", score3]],
           "Dawn: Yucks aside, whole point of this song and dance: You. Party. Tonight\nNon-negotiable. I’m getting tired of repeating the same thing. When is it\ngetting into your thick skull that you’re going to the party?": 
           [["1) I’m. Busy. Tonight. Non-negotiable.", score], 
           ["2) I really can’t Dawn, I’ll try to make it up to you guys another time.", score2], 
           ["3) I just want to watch bad movies by myself and sleep, is that a crime?", score3]],
           "Dawn: Alright, you’ve forced my hand. I’m calling in the big guns. There’s\nno point in trying to stop me. It’s happening.": 
           [["1) What are you doing?", score], 
           ["2) I swear if you show up at my house to try to lift me...", score2], 
           ["3) Dawn, please...", score3]],
           "Dawn: I’m messaging Sock and telling him you’re trying to flake on us. You\nleft me no choice.": 
           [["1) Ugh... why???", score], 
           ["2) You absolute horse's ass! Stop it!", score2], 
           ["3) I mean... oh no?", score3]],
           "Dawn: Aaaaaaand done. Get ready for that because it’s going to be waaaaay\nworse than talking to me or Cameron was.": 
           [["1) You suck.", score], 
           ["2) Thanks... really.", score2], 
           ["3) Okay, that's gonna be a time.", score3]],
           "Dawn: I tried to give you an out. Now you get to explain it to King\nWaterworks why one of his security buddies is going to be MIA.": 
           [["1) AAAAAAAAAAAAAAAAAA-", score], 
           ["2) Yep, now I get to do that. Again, thanks.", score2], 
           ["3) I'm genuinely questioning the basis of our friendship right now.", score3]],
           "Dawn: Is it so hard to believe we’re all doing this because we haven’t seen\nyou in a while and want to hang out with you, {player_name}?": 
           [["1) You have a REALLY funny way of showing THAT.", score], 
           ["2) I think you enjoy being as annoying as possible.", score2], 
           ["3) I mean... kind of with how you've gone about this?", score3]],
           "Dawn: That is the closest you are going to get to me saying anything of that\nsort. I don’t do mush.": 
           [["1) I don't think that can count as \'mush\'.", score], 
           ["2) I guess that was... an attempt made.", score2], 
           ["3) We're aware.", score3]],
           "Dawn: Alright, I’m already regretting trying to appeal to pathos. Retracting\nall sentimentality. Just get your ass to the party.": 
           [["1) No.", score], 
           ["2) Sorry, Dawn. Maybe next time.", score2], 
           ["3) This has been utterly exhausting. I need a nap.", score3]],
           "ENDINGS": 
           [["Dawn: Ugh, fine. Enjoy your night alone or whatever, but you’ve got to come\nout with us next week.", score], #Good ending
           ["Dawn: Y’know what? I don’t know why I’m trying so hard. This is just a giant\nwaste of time", score2], #Neutral/hates you ending
           ["Dawn: Okay, I hear what you’re saying but you’re acting really weird. I’m\ncoming to pick you up. Be ready at 9.", score3]]},
    #Dawn - bully
    #intended answer weights: 1 = high impact, 2 = light, 3 = medium
person2keys = list(person2())

person3 = {"Sock: Ugh… heeeey {player_name}. Long time no see… or talk…": 
           [["1) Who is this again?", score], 
           ["2) Oh, hey sock.", score2], 
           ["3) Ew, vermin in my dms!", score3]],
           "Sock: Are you really not going to Johnny’s party? It’s supposed to be a\ngood one since… y’know it’s one of *Johnny’s* parties…": 
           [["1) There's so many better things to do at home though...", score], 
           ["2) No.", score2], 
           ["3) Maybe another time.", score3]],
           "Sock: Is it weird if I ask why? I mean, it’s your business and all but… I\ndon’t know {player_name}, I just feel weird going to one of those things without\nthe whole group.": 
           [["1) I want to eat chips and sleep instead.", score], 
           ["2) Ugh... That's a secret...", score2], 
           ["3) Don't be such a wuss.", score3]],
           "Sock: I mean I guess it’s fine if you don’t want to go. It’l just be me,\nCameron, and Dawn…": 
           [["1) I believe in you space cadet.", score], 
           ["2) You'll live.", score2], 
           ["3) Could be so much worse.", score3]],
           "Sock: So would you rather just want to hang out at your place instead? Not that\nI don’t want to go! I love parties!": 
           [["1) Oh no... no no no.", score], 
           ["2) It's okay, you don't have to pretend.", score2], 
           ["3) Cool, have fun then!", score3]],
           "Sock: No I-I really love parties! With how loud everything is and how\neveryone is just in your face slurring…": 
           [["1) Wear headphones.", score], 
           ["2) Aw yeah, it's the best!", score2], 
           ["3) It gets pretty annoying.", score3]],
           "Sock: I mean… It's what everyone likes to do and I want to hang out with\neveryone. I don’t want to muck up what already works.": 
           [["1) I can get that.", score], 
           ["2) Why don't you plan your own thing?", score2], 
           ["3) You're kind of a doormat.", score3]],
           "Sock: I tried making a book club happen. No one actually read the books… I\ndon’t think Dawn even tried.": 
           [["1) Maybe pick better books?", score], 
           ["2) That's rough buddy.", score2], 
           ["3) Sounds like something Dawn would do.", score3]],
           "Sock: It’s just… Why can’t we just do stuff that isn’t so loud and obnoxious?\nWhy does Johnny have to invite a bunch of weird people we’ve never met before?": 
           [["1) The more the merrier!", score], 
           ["2) Have you tried earplugs?", score2], 
           ["3) Whiner, you're a whiner.", score3]],
           "Sock: It would be way better if it were just us. I really don’t like a bunch of\nstrangers looking at me and then I have to make small talk that I’m pretty sure\nthey don’t care about.": 
           [["1) Odds are no one is staring at you as hard as you think.", score],
            ["2) Just talk to people, it's not hard.", score2], 
            ["3) Yeah...", score3]],
           "Sock: I just walk away feeling like I’ve made a giant idiot of myself and now\nthey’re laughing at me with the next person they talk to. \‘Hey see that person\nover there? They’ve never spent a day on earth before.\’":
           [["1) Holy catastrophizing Manbat.", score], 
            ["2) It can be scary putting yourself out there.", score2], 
            ["3) Uhm... you okay buddy?", score3]],
           "Sock: \‘They probably never leave their house that smells like old mustard,\ntheir friends are all carefully constructed lies assigned by the government,\nand they suck at dancing.\’": 
           [["1) Sock, snap out of it!", score], 
            ["2) Holy shit dude.", score2], 
            ["3) You do kinda smell like old mustard.", score3]],
           "Sock: Except the government wouldn’t assign me friends (player_name). You’d all\njust be like… alien surveillance agents here to make sure I don’t spread my\nsocial ineptitude to every actual human on this planet.": 
           [["1) When was the last time you went outside?", score], 
            ["2) Yep, we're just the Sock Survelliance Experts.", score2], 
            ["3) No one would waste that kind of effort.", score3]],
           "Sock: Yeah… actually let’s just forget the whole thing. I’ll come hang out\nwith you tonight instead!": 
           [["1) Abort this mission!", score], 
            ["2) No!", score2], 
            ["3) Let's think of something else to do here.", score3]],
           "Sock: It’ll be way better than whatever happens at Johnny’s place. Cam tried to\nget me excited about the whole thing because I guess Johnny got a new cat?": 
           [["1) Think of the horrible creature you're fond of!", score], 
            ["2) No one would be excited by a cat.", score2], 
            ["3) Maybe it likes to be petted?", score3]],
           "Sock: The poor thing is probably going to be hiding under the couch the entire\ntime…": 
           [["1) Where it belongs.", score], 
            ["2) Oh, poor goblin creature I guess.", score2], 
            ["3) Where it'll need a friend!", score3]],
           "Sock: It’s probably weird being a cat. Animals just blindly trust that we know\nwhat we’re doing and that what we’re doing is the correct thing.": 
           [["1) Pets have it rough.", score], 
            ["2) Ugh... okay?", score2], 
            ["3) Who cares.", score3]],
           "Sock: My dog probably doesn’t even know when or if I’m coming home when I leave.\nHe’s just trusting that the loneliness is only temporary.": 
           [["1) Oh... oh no.", score], 
            ["2) I'm worried about you, Sock.", score2], 
            ["3) Can you cut the crazy talk for five seconds?", score3]],
           "Sock: If I’m being honest… I wish I could just crawl under the furniture during\nthe party. I really don’t want to go if everyone isn’t gonna be there.": 
           [["1) Therapy. Acquire the therapy.", score], 
            ["2) With enough alchohol, you too can crawl under the couch.", score2], 
            ["3) Yikes.", score3]],
           "Sock: Dawn says I should go because I have to at least try not to be a\nsniveling slug for my entire life but it’s just a lot, {player_name}.": 
           [["1) Wow, Dawn sure is a peach.", score], 
            ["2) Yeah, I hear ya.", score2], 
            ["3) Slug Soooooooooock!", score3]],
           "Sock: They’re kind of a jerk but I think they mean well… I hope they do at least. They’re pretty excited about the karaoke.": 
           [["1) I guess...", score], 
            ["2) Say \'potato\' if you need help.", score2],
            ["3) Oh god, not karoake again.", score3]],
           "Sock: We’re probably gonna have to listen to Dawn sing Seasoning Women again and\nthen complain that it wasn’t good because we didn’t want to join them for it.": 
           [["1) They never let me be Scary Spice.", score], 
            ["2) NOOOOOOOO!", score2],
            ["3) It'll be a time.", score3]],
           "Sock: I was hoping maybe the movie thing would pan out but it looks like it’s\njust a bunch of dated horror flicks.": 
           [["1) Let me guess, too spooky for you?", score], 
            ["2) The two Cam mentioned are actually not bad.", score2],
            ["3) It's so lame!", score3]],
           "Sock: They’re just boring, {player_name}. I don’t get why so many people go nuts\nfor the same thing over and over again.": 
           [["1) Something something consumerism.", score], 
            ["2) I know right?", score2],
            ["3) Genuinely shocked that horror movies don't ruffle your feathers but\ntalking to strangers does.", score3]],
           "Sock: I threw in what was basically the movie version of the anime series\nTatami Galaxy. The art style is pretty neat.":
           [["1) What Galaxy?", score], 
            ["2) Are people gonna be able to read subs that fast drunk?", score2],
            ["3) That movie sucks.", score3]],
           "Sock: That show was made over ten years ago though so I don’t know if anyone\ncares about it now.":
           [["1) Might be a bit of a deep cut.", score], 
            ["2) Yeah, no one cares about it.", score2],
            ["3) It's still good even if it isn't recent.", score3]],
           "Sock: Maybe I can run away halfway through the party? Give it just enough time\nfor people to start drinking and then I sneak away. They’ll think the aliens\nfinally came back to take me home.":
           [["1) People are gonna report you as missing.", score], 
            ["2) Sneaking out of a party isn't necessary.", score2],
            ["3) Just leave if you want to like a normal person.", score3]],
           "Sock: So you’re really, really serious about not going? Even though it’ll\nprobably be a giant disaster without you there?":
           [["1) I trust you to weather this storm.", score], 
            ["2) Dead serious.", score2],
            ["3) I really can't tonight.", score3]],
           "Sock: I suppose… I guess I can try to find a way to survive with just Cameron\nand Dawn there…":
           [["1) Good luck!", score], 
            ["2) It's not that bad.", score2],
            ["3) Okay, Sock.", score3]],
           "ENDINGS:":
           [["I mean… I could also just stay at my own house and pretend to be sick… I think\nI’m gonna do that. See you at the next one {player_name}.", score], 
            ["I just… I really need my people around for things to be okay. I guess you\nweren’t one of my people.", score2],
            ["I know you said not to come over and all but I think hanging out with you\ntonight would be a lot less stressful. You won’t even know I’m there and I can\npay for pizza or something. See you later!", score3]]} 
#Sock - meek
person3keys = list(person3())

#how to call
# person1[person1keys[0]][2][1]  =  #question=idx (does not get the question itself) > answer#=idx > score=1,answerstr=0
# person1keys[0] = #how to get the question itself
MainScore = []

#helper functions
def NextQuestion(score, questionNum):
    question = ""
    answers = []
    question = question + str(person2keys[questionNum]) #temporarry
    answers = person2[person2keys[questionNum]] #temporary
    return(question, answers)

def friendsCnt(numpep, startvalue):
    startloop = "apples"
    while True: #asks for input to do tutorial or not
        try: #this is for input validation
            if startloop == "apples":
                print("Default is set to 2 people. Difficulty scales on number of people. 1= Easy, 2= Medium, 3= Hard")
                numpep = int(input(f"Enter number of friends: 1,2 or 3. Current value is: {numpep}\n->")) #sets number of people for game
                startloop = "pears" #first loop check, this will make it not happen again
            else:
                numpep = int(input("-> "))                
            peoplelist = [1,2,3]
            if numpep not in peoplelist:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, please type exactly \"1\", \"2\", or \"3\"")
    for idx in range(numpep):
        MainScore.append(startvalue)
    return numpep

def nameSet(person_name):
    while True:
        try:
            person_name = input("What should we call you?\n-> ")     
            if len(person_name) != 0:          
                print(f"That's a good name, {person_name}! Your friends will remember it!")
                break
            else:
                raise ValueError
        except ValueError:
            print("Name cannot be empty. Try again")
    return person_name

def VictoryConditions(score):
    Endgametype = 0
    for victory in EndingGame:
        if 0 <= score <= 30:
            victory == 1 #good ending
        elif 30 < score <= 60:
            victory == 3 #all negative ending
        elif 60 < score <= 90:
            victory == 2 #all eaten ending
    #victory conditions are in the docstring for endinggame()
    #90 total possible points
    return Endgametype

def Updatelog():
    pass
    #next submission

#game functions
def StartGame(name):
    Intro_text = f"""
    Turns out being a werewolf isn’t what fantasy novels chock it up to be, at 
    least not a modern werewolf anyway. There’s no running through the woods 
    and ‘unleashing your inner wolf’ or any of that nonsense depicted in books 
    with scandalous oil paintings for covers. It’s still just like being any 
    other person that has to make it day to day…. except with the ‘fun’ 
    challenge of turning into a murderous beast once a month. You’ve had to 
    learn first hand the issues that come with that ranging from copious 
    amounts of shedding that your vacuum never seems to fully clean up, to the 
    bloody messes that you need to discreetly clean up when you can’t keep 
    yourself locked up during those pesky full moons. It really is a pain to 
    have to change your name and abandon your entire life every time just one 
    teensy little security measure just doesn’t hold up. 

    It’s been a couple months since the last time you’ve had to jump ship, and 
    this time you’re going by {player_name}.

    You’ve managed to settle in quite nicely. You’ve scored a great job and 
    managed to land a spot in a semi-stable group of friends. You’ve finally 
    found the best way to keep from going on a bloodthirsty rampage during the 
    full moons. Thanks to your new iron clad security, courtesy of ‘Trademarked 
    Hardware and Home Improvement’ store, there’s absolutely no way you’re 
    busting through those locks! So now it’s just you, a movie that you 
    probably won’t finish due to your impending transformation, and a supply 
    of tranquilizer laced meat in the fridge all settled in for a completely 
    uneventful evening.

                            So why is your phone ringing? 

    Looking at the number on display, you see Cameron’s name popping up. Before
    you can think to answer it all rushes in: the party and the plans you made 
    with each of your friends. That was tonight! You scheduled that all on the 
    night of the full moon like some giant idiot!

    You’re gonna have to cancel all of your plans and you just know your 
    friends aren’t going to make that easy. The alternative however is 
    potentially eating them at worst, possibly only mauling them at best. It’s
    what you’ve gotta do."""


    print(Intro_text)
    while True: #asks for input to do tutorial or not
        try: #this is for input validation
            tutorialY = input("""                                   1) View Tutorial?
                                   2) Answer the call\n-> """)
            corlist = ["1", "2"]
            if tutorialY not in corlist:
                raise ValueError
            if "1" in tutorialY:
                Tutorial()
            break
        except ValueError:
            print("Invalid input, please type exactly \"1\" or \"2\"")
    MainGame(name) #this goes into the main game
        #block was found in stackoverflow: https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers

def Tutorial():
    Tut_text = """
    Welcome to Stay Home Moon! You’ve found yourself in a bit of a spot,\n 
    haven’t you? The goal of the game is pretty simple: Don’t Eat Your Friends.

    You will have to navigate a series of phone calls with your friends. 
    You’ll be presented with a series of responses that will shape how your 
    friend reacts to the conversation. You will select your response by typing 
    the correlating number into the command line. There are three things to 
    remember when selecting a response:

    -Your words have weight.
    -Some of your options will have a greater impact than others.
    -The ultimate goal is to not eat your friends, but try not to completely 
     ruin your relationships.

    You should really pick up that phone now, Cameron’s waiting, good luck!"""
    print(Tut_text)

def MainGame(name):
    numquestions = len(person1keys) + len(person2keys) + len(person3keys)
    score = 0
    questionnumber = 0
    VictoryCond = 0
    player_name = name
    bugcondition = 0 #for exiting loop if got stuck
    while VictoryCond == 0: #main loop for the game
        bugcondition += 1
        if numquestions == 0:
            VictoryCond = 1
            break
        anslenlist = []
        anslenstr = ""
        curquestion, curanswers = NextQuestion(score, questionnumber)
        curquestion = curquestion.format(player_name = player_name)
        print(f"{curquestion}\n")
        for i in range(len(curanswers)):
            print(curanswers[i][0])
            anslenlist.append(i+1)
        for i in range(len(anslenlist)):
            anslenstr = anslenstr + str(anslenlist[i]) + ", "
        anslenstr = anslenstr[:-3] + f"or {anslenlist[-1]}"
        while True:
            try: #this is for input validation
                choice = input(f"Pick Answers {anslenstr} by typing that number (ex to exit if stuck)\n-> ")
                if choice.isdigit() == True:
                    choice = int(choice)
                    if choice not in anslenlist:
                        raise ValueError
                    break
                else:
                    if "ex" in choice.lower():
                        print("exiting game ... ")
                        exit()
                    raise ValueError
            except ValueError:
                print("Invalid input, please type exactly one of the numbers shown")
            print()

        CurAnswScore = ScoreAnswer(choice, curanswers[choice-1])
        score += CurAnswScore
        questionnumber += 1
        numquestions -= 1 #this prevents endless loops
        if bugcondition > 500:
            print("bugged code, exiting function ....")
            exit()
        VictoryCond = VictoryConditions(score)            
        
    EndingGame(VictoryCond)
    

def EndingGame(victory):
    """
    victory condition 0: not possible, 0 means game is running

    victory condition 1: out of questions. This is good, and can lead into winning flawlessly
        victory condition 1.2: Flawless victory, all friends dont come and dont hate you
        victory condition 1.3: Atleast 1 friend died
        victory condition 1.4: All survived, but at least 1 hates you 
    victory condition 2: All eaten - all friends get eaten
    victory condition 3: All hate you - all friends hate you


    specicial conditions
        these are to figure out later, and will depend on special peramaters like certain answers chosen
        these will start at 100
    """

    
    ending1_text = """
                The full moon rises but the evening remains calm. 

    Your friends are blissfully unaware of the transformation occurring in your
    solitary apartment. The group chat is filling with messages. Pictures and 
    videos of varying clarity or what’s happening at the party. It seems this 
    is how they’re trying to include you, and maybe convince you to come to the
    next one.

    Cameron’s sending pictures of everyone having a good time. You can see Dawn
    standing by while Sock tries to talk to Johnny’s randos. From the still 
    shots it looks like their actually doing pretty well, even if they look 
    like they want to throw up. 

    Dawn of course is sending snippets of people doing dumb things. You’re not 
    surprised in the slightest. There’s clips of Cameron singing Bowie Mercury 
    and it’s a time.

    You don’t get a single SOS message from Sock. They’ve been sending pictures 
    of Johnny’s new cat, apparently named Felicity. For a horrible, free loading 
    furball, she’s actually just a little cute.

    You’re gonna have a lot of catching up to do with them tomorrow.

                                You Win!
                                """
    
    ending2_text = f"""
                Your friends couldn’t be convinced to stay away. 

                            Do you know what that means? 

             That means they’re coming to your house {player_name}. 

                    You failed them in the worst possible way.

    The night of the full moon and subsequently Johnny’s party arrives. 
    Your transformation was interrupted by a knock on the door. It opens and
    concerned gazes of the people you care about witness you hunched over and 
    writhing. They hear your bones snap as they reshape and you are molded into
    a monster.

    Maybe it’s for the best you don’t exactly remember what happened next. 
    You’ll never forget the sight of the remains you left behind though.

    You couldn’t stomach hiding them away like so many other unfortunate 
    bystanders before. You run, leaving this version of your life behind.

                                    Bad End
                                    """
    
    ending3_text = """
       The night of the full moon comes and goes without incident.

               
       The sun rises to a slightly disheveled apartment, but a quick tidy and 
       nothing out of the ordinary appears to have occurred.

       There’s no messages on your phone. No one has checked in on you since 
       yesterday and the group chat is weirdly silent. 

       You may have lost all of your friends, but at least they’re alive! You 
       didn’t just eat a bunch of innocent people! So you stand in your newly 
       re-organized apartment and cling to that small victory. 

       You can’t help but feel a little lonely though…

       
                                       Bad End?
                                """

    if victory == 1:
        print(ending1_text)
        sleep(2) #1.2 conditions, flawless victory- all alive, all positive
    elif victory == 2:
        print(ending2_text)
        sleep(2) #2 conditions- all eaten
    elif victory == 3:
        print(ending3_text)
        sleep(2) #3 conditions- all negative
    else:
        print("unknown ending...\n...\n..")
        print("bugged code srry")

    print("Game end\n...\n...\n...") #placeholder for checking if this will be called
    sleep(2)
    exitgame = input("Do you want to play again or exit? \"Y\" for yes, anything else for no\n-> ")
    if exitgame != "Y":
        print("Thank you for playing")
        exit()



def Menuscreen(): #unsure about the function input, this could be wrong
    player_name = ""
    nonamechecknum = 2
    numofPeople = 2
    global startval #this is bad form, ill try to fix this later. This was just an easy fix
    
    Menu_text = """
                ┌── ⋆⋅☆⋅⋆ ──.·:*¨༺ ☾ ༻¨*:·.── ⋆⋅☆⋅⋆ ──┐


                            Stay Home Moon

                            Play
                            Set Name
                            Friends Count
                            Exit
                
                
                └── ⋆⋅☆⋅⋆ ──•,¸,.·'  '·.,¸,•── ⋆⋅☆⋅⋆ ──┘
        """
    #ascii pattern made from https://www.aestheticsymbols.me/dot.html
    print(Menu_text)
    while True:
        try: #this is for input validation

            menuinput = input("What do you want to do? Type \"Play\", \"Name\", \"Friends\", or \"Exit\"\n-> ").upper()
            inputcheck = ["PL", "NA", "FR", "EX"] #checking substrings for higher chance of getting right thing
            
            if any(substring in menuinput for substring in inputcheck) == False:
                raise ValueError
            if "PL" in menuinput: #play
                if len(player_name) == 0:
                    if nonamechecknum == 0: #this is a funny easteregg
                        print("Fine, name has been set to 'Billybob'. You win")
                        player_name = "Billybob"
                        StartGame(player_name)
                    else:
                        print("Please set a name first")
                        nonamechecknum -= 1
                else:
                    StartGame(player_name)
            elif "NA" in menuinput:
                player_name = nameSet(player_name)
            elif "FR" in menuinput: #sets friends
                numofPeople = friendsCnt(numofPeople, startval)
            elif "EX" in menuinput: #exits program
                leaveY = input("Do you really want to leave? Type \"Y\" if you do, or anything else for no\n-> ")
                if leaveY == "Y":    
                    print("Thank you for playing")
                    exit()
            else: #this is for wrong inputs not caught
                print("how did you get here. bad !!@%$@#@#!!!$#@#@#@\n")
                raise KeyError
        except ValueError:
            print("Invalid input, please type one of the four options\n")    
        except KeyError:
            exit()






if __name__ == '__main__':
    # Write all functions in here that will be called when running the program
    Menuscreen()