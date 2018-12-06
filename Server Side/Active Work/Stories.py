# TODO:
# split data into parts of speech, basic structures, story architectures, and more elaborate story plots.
# Adjectives need to be formatted so that associated nouns aren't integral to the format. Split nouns from adjective structure.

data = {
    "myth" : {
        "origin": [
            "#[#setFantasyLevel#][#setCharacters#]story#"
        ],
        "setCharacters": [
            "[#setHero#][monster:#monsterRaces#]"
        ],
        "setFantasyLevel": [
            "[npcRaces:human][monsterRaces:#terrestrialAnimalLarge#][petRaces:#petAnimalSmall#]",
            "[npcRaces:#humanRaces#][monsterRaces:#terrestrialAnimalLarge#][petRaces:#petAnimalSmall#]",
            "[npcRaces:#fantasticRaces#][monsterRaces:#terrestrialAnimalLarge#][petRaces:#petAnimalSmall#]",
            "[npcRaces:#fantasyRaces#][monsterRaces:#monsterTypes#][petRaces:#petAnimalSmall#]",
            "[npcRaces:#ridiculousRaces#][monsterRaces:#monsterTypes#][petRaces:#petAnimalSmall#]"
        ],
        "setHero": [
            "[#setHeroGender#][heroRace:#npcRaces#][heroPet:#petRaces#]"
        ],
        "setHeroGender": [
            "[heroGender:female][#setHeroFemalePronouns#][heroName:#femaleNames#]",
            "[heroGender:female][#setHeroFemalePronouns#][heroName:#femaleIshNames#]",
            "[heroGender:male][#setHeroMalePronouns#][heroName:#maleNames#]",
            "[heroGender:male][#setHeroMalePronouns#][heroName:#maleIshNames#]"
        ],
        "setHeroFemalePronouns": [
            "[heroThey:she][heroThem:her][heroTheir:her][heroTheirs:hers]"
        ],
        "setHeroMalePronouns": [
            "[heroThey:he][heroThem:him][heroTheir:his][heroTheirs:his]"
        ],
        "setHeroAndrogynousPronouns": [
            "[heroThey:it][heroThem:it][heroTheir:its][heroTheirs:its]"
        ],
        "femaleIshNames": [
            "#femaleNames",
            "#androgynousNames#"
        ],
        "maleIshNames": [
            "#maleNames#",
            "#androgynousNames#"
        ],
        "maleNames": [
            "Steve",
            "Daniel",
            "Terry",
            "Jake"
        ],
        "femaleNames": [
            "Susan",
            "Emma",
            "Mary",
            "Abby"
        ],
        "androgynousNames": [
            "Ash",
            "Reese",
            "Skyler",
            "Robbie"
        ],
        "humanRaces": [
            "scandinavian",
            "african",
            "texan",
            "floridian",
            "indian",
            "native American",
            "asian"
        ],
        "fantasticRaces": [
            "#humanRaces#",
            "ape-men"
        ],
        "fantasyRaces": [
            "#humanRaces#",
            "elf",
            "dwarf"
        ],
        "ridiculousRaces": [
            "#fantasyRaces#",
            "#monsterTypes#"
        ],
        "monsterTypes": [
            '#undeadMonster#',
            '#dragonMonster#',
            '#WereMonster#'
        ],
        # "intelligentEvilOccupation": [
        #     'bandit',
        #     'outlaw',
        #     'thug',
        #     'assassin',
        #     'warlord'
        # ],
        "undeadMonster": [
            'zombie',
            'ghoul',
            'ghost',
            'wight',
            'wraith',
            'lich'
        ],
        "animalSmall": [
            '#petAnimalSmall#',
            'lizard',
            'spider',
            'bee'
        ],
        "petAnimalSmall": [
            'rat',
            'cat',
            'dog',
            'rabbit',
            'fox'
        ],
        "animalLarge": [
            '#terrestrialAnimalLarge#',
            '#aquaticAnimalLarge#'
        ],
        "terrestrialAnimalLarge": [
            '#forestAnimalLarge#',
            '#jungleAnimalLarge'
        ],
        "aquaticAnimalLarge": [
            "whale",
            "squid",
            "octopus",
            "#sharkTypes#"
        ],
        "sharkTypes": [
            "shark",
            "#sharkDescriptor# shark",
            "megalodon"
        ],
        "sharkDescriptor": [
            "great white",
            "tiger",
            "hammerhead",
            "whale"
        ],
        "forestAnimalLarge": [
            'wolf',
            'puma',
            'bear'
        ],
        "jungleAnimalLarge": [
            'gorilla',
            'tiger',
            'jaguar',
            '#reptileAnimalLarge#'
        ],
        "reptileAnimalLarge": [
            'crocodile',
            'alligator',
            '#snake#'
        ],
        "snake": [
            'python',
            'cobra',
            'anaconda'
        ],
        "WereMonster": [
            'were#animalLarge#',
            'vampire'
        ],
        "dragonMonster": [
            'dragon',
            'wyvern',
            'drake',
            'wyrm',
            'hydra',
            'serpent'
        ],
        "prologue": [
            "greetings"
        ],
        "greetings": [
            "Hi#Punctuation#",
            "Hello#Punctuation#"
        ],
        "Punctuation": [
            ".",
            "!"
        ],
        "beginning": [
            "in the beginning there was #heroGender.a# #heroRace.capitalize# named #heroName#.",
            "since time immemorial, there has been #heroGender.a# #heroRace.capitalize# named #heroName#.",
            "once upon a time there was #heroGender.a# #heroRace.capitalize# named #heroName#.",
            "in the void there was #heroGender.a# #heroRace.capitalize# named #heroName#."
        ],
        "middle": [
            "#conflict#"
        ],
        "fought": [
            "fought",
            "wrestled",
            "battled"
        ],
        "conflict": [
            "#heroName.capitalize# #fought# with #monster.a#.",
            "#heroName.capitalize# #fought# with #monster.s#."
        ],
        "end": [
            "fin.",
            "the End.",
            "and then, after many years, you were born."
        ],
        "epilogue": [
            "bye#Punctuation#"
        ],
        "story": [
            # "#prologue.capitalize# #beginning# #middle# #end# #epilogue.capitalize#",
            "#beginning.capitalize# #middle.capitalize# #end.capitalize#"
        ]
    },
    "hero" : {
        "origin": [
            "#[#setSingluarPronouns#][#setOccupation#][hero:#name#]story#"
        ],
        "setSingluarPronouns": ["[heroThey:she][heroThem:her][heroTheir:her][heroTheirs:hers]",
            "[heroThey:he][heroThem:him][heroTheir:his][heroTheirs:his]"
        ],
        "setPluralPronouns": [
            "[heroThey:they][heroThem:them][heroTheir:their][heroTheirs:theirs]",
        ],
        "setOccupation": [
            "[occupation:baker]" +
            "[didStuff:" +
            "baked bread," +
            "decorated cupcakes," +
            "folded dough," +
            "made croissants," +
            "iced a cake]",

            "[occupation:warrior]" +
            "[didStuff:" +
            "fought #monster.a#," +
            "saved a village from #monster.a#," +
            "battled #monster.a#," +
            "defeated #monster.a#]"
        ],
        "monster": [
            "dragon",
            "ogre",
            "witch",
            "wizard",
            "goblin",
            "golem",
            "giant",
            "sphinx",
            "warlord"
        ],
        "name": [
            "Cheri",
            "Fox",
            "Morgana",
            "Jedoo",
            "Brick",
            "Shadow",
            "Krox",
            "Urga",
            "Zelph"
        ],
        "story": [
            "#hero.capitalize# was a great #occupation#, and this song tells of #heroTheir# adventure. #hero.capitalize# #didStuff#, then #heroThey# #didStuff#, then #heroThey# went home to read a book."
        ]
    },
    "tale" : {
        "origin": ["#[heroFavFood:#food#][hero:#character#][villain:#monster#]composition#"],
        "composition": [
            "#heroOrigin# #heroDescription# #heroMeetsVillain# #heroVSVillain# #heroEnd#",
            "#heroOrigin# #heroDescription# #heroDescription# #heroMeetsVillain# #heroVSVillain# #heroEnd#",
            "#heroOrigin# #heroDescription# #heroMeetsVillain# #heroVSVillain# #heroEnd#"
        ],
        "heroOrigin": [
            "Once upon a time, there was #heroADJ.a# #hero#.",
            "In the beginning, there was #hero.capitalize#.",
            "On a #darkADJ# and #stormyADJ# night, #hero.a# appeared."],
        "heroDescription": [
            # "That #hero# was very #heroADJ#.",
            "The #hero# liked #heroFavFood#."
            # "The #hero# was very #goodADJ#."
        ],
        "heroMeetsVillain": [
            "Then the #hero# met a #adj# #adj# #villain#."
        ],
        "heroVSVillain": [
            "And she killed the #villain#."
        ],
        "heroEnd": [
            "And then the #hero# ate #heroFavFood# and she was so #adj# and she was #adj#."
        ],
        "often": [
            "rarely",
            "never",
            "often",
            "almost always",
            "always",
            "sometimes"
        ],
        "darkADJ": [
            'dark',
            'pitch-black',
            'shadowy'],
        "stormyADJ": [
            'stormy',
            'wild',
            'blustery'],
        "character": [
            "#fantasyAnimalSmall#",
            "#fantasyAnimalLarge#",
            "#youngRoyalty#",
            "#animalLarge#",
            "#membersOfCourt#"
        ],
        "youngRoyalty": [
            'princess',
            'prince'
        ],
        "membersOfCourt": [
            'knight',
            'duchess',
            'duke'
        ],
        "adj": [
            '#goodADJ#',
            '#emotiveADJ#',
            '#badADJ#'
        ],
        "goodADJ": [
            '#intelligentADJ#',
            '#strongADJ#',
            '#robustADJ#', # High constitution
            '#dextrousADJ#',
            '#wiseADJ',
            '#charismaticADJ#',
            '#beautyADJ#',
            '#funnyADJ#',
            '#heroADJ#'
        ],
        "heroADJ": [
            'brave',
            'bold',
            'amazing',
            'incredible'
        ],
        "emotiveADJ": [
            # anger, contempt, disgust, fear, joy, sadness and surprise
            '#angryADJ#',
            '#contemptADJ#',
            '#disgustADJ#',
            '#fearADJ#',
            '#happyADJ#',
            '#sadADJ#',
            '#surpriseADJ#'
        ],
        "badADJ": [
            '#odourousADJ#',
            '#weirdADJ#',
            '#evilADJ#'
        ],
        "intelligentADJ": [
            'smart',
            'intelligent',
            'witty',
            'cunning'
        ],
        "strongADJ": [
            'strong'
        ],
        "robustADJ": [
            'robust',
            'hardy'
        ],
        "dextrousADJ": [
            'dextrous',
            'limber'
        ],
        "wiseADJ": [
            'wise'
        ],
        "charismaticADJ": [
            'charismatic',
            'charming',
            'appealing',
            'influential',
            'entertaining',
            'magnetic',
            'enticing',
            'alluring'
        ],
        "beautyADJ": [
            'pretty',
            'beautiful',
            'attractive',
            'stunning',
            'georgeuos'
        ],
        "funnyADJ": [
            'funny',
            'humorous'
        ],
        "angryADJ": [
            'angry',
            'furious'
        ],
        "contemptADJ": [
            'contemptuous'
        ],
        "disgustADJ": [
            'disgusted'
        ],
        "fearADJ": [
            'afraid',
            'scared',
            'terrified'
        ],
        "happyADJ": [
            'happy',
            'overjoyed'
        ],
        "sadADJ": [
            'sad',
            'morose'
        ],
        "surpriseADJ": [
            'surprised'
        ],
        "odourousADJ": [
            'smelly',
            'stinky',
            'foul-smelling'],
        "weirdADJ": [
            'weird',
            'strange',
            'curious',
            'odd',
            'perplexing'
        ],
        "evilADJ": [
            'evil',
            'wicked',
            'malicious',
            'malevolent',
            'unholy',
            'heinous',
            'depraved',
            'vile'
        ],
        "foodGoodADJ": [
            'delicious',
            'delectable',
            'scrumptious',
            'tasty',
            'sumptuous',
            'savoury'
        ],
        "food": [
            '#foodGroups#',
            '#foodGoodADJ# #foodGroups#'
        ],
        "foodGroups": [
            '#soup#',
            '#entree#',
            '#snack.s#'
        ],
        "entree": [
            'steak',
            'pork chop',
            'shrimp',
            'salmon'
        ],
        "snack": [
            'pretzel',
            'fry',
            'chip'
        ],
        "soup": [
            'soup',
            'stew',
            'broth',
            'bisque',
            'chowder'],
        "monster": [
            '#undeadMonster#',
            '#dragonMonster#',
            '#WereMonster#',
            '#humanMonster#'
        ],
        "humanMonster": [
            'bandit',
            'outlaw',
            'thug',
            'assassin'
        ],
        "undeadMonster": [
            'zombie',
            'ghoul',
            'ghost',
            'wight',
            'wraith',
            'lich'],
        "animalSmall": [
            'rat',
            'cat',
            'dog',
            'rabbit',
            'lizard',
            'spider',
            'bee'
        ],
        "animalLarge": [
            'wolf',
            'bear',
            'crocodile',
            'alligator',
            '#snake#',
            'giant squid'
        ],
        "snake": [
            'python',
            'cobra',
            'anaconda'
        ],
        "fantasyAnimalLarge": [
            'unicorn',
            '#dragonMonster#'
        ],
        "fantasyAnimalSmall": [
            'fairy'
        ],
        "WereMonster": [
            'were#animalLarge#',
            'vampire'
        ],
        "dragonMonster": [
            'dragon',
            'wyvern',
            'drake',
            'wyrm',
            'hydra',
            'serpent']
    },
    "quest" : {
        "origin": [
            "#plea##[#setQuestAmount#][#setQuestPeople#][#setPlaces#][#setDeliverable#][#setCraft#][#setQuestType#]quest#",
            "#[#setQuestAmount#][#setQuestPeople#][#setPlaces#][#setDeliverable#][#setCraft#][#setQuestType#]quest#"
        ],
        "setQuestAmount": [
            "[amount:#rangeTwoToTenText#]"
        ],
        "rangeTwoToTenText": [
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten"
        ],
        "setQuestPeople": [
            "[person1:#name#][person2:#name#]"
        ],
        "name": [
            "#maleNames#",
            "#femaleNames#",
            "#androgynousNames#"
        ],
        "femaleIshNames": [
            "#femaleNames",
            "#androgynousNames#"
        ],
        "maleIshNames": [
            "#maleNames#",
            "#androgynousNames#"
        ],
        "maleNames": [
            "Steve",
            "Daniel",
            "Terry",
            "Jake"
        ],
        "femaleNames": [
            "Susan",
            "Emma",
            "Mary",
            "Abby"
        ],
        "androgynousNames": [
            "Ash",
            "Reese",
            "Skyler",
            "Robbie"
        ],
        "setPlaces": [
            "[currentPlace:#placeName#][destination:#placeName#]"
        ],
        "placeName": [
            "#cityModifier# #cityName.capitalize#",
            "#cityName.capitalize#",
            "#cityName.capitalize#",
            "#wondersName#"
        ],
        "cityModifier": [
            "the village of",
            "the city of",
        ],
        "cityName": [
            "#cityNamePartOne##cityNamePartTwo#"
        ],
        "cityNamePartOne": [
            "river",
            "haver",
            "ivar",
            "midden",
            "olter",
            "fen"
        ],
        "cityNamePartTwo": [
            "wood",
            "stead",
            "guard",
            "run",
            "lond"
        ],
        "wondersName": [
            "the #environ.capitalize# of #environModifier.capitalize#",
            "the #environ.s.capitalize# of #environModifier.capitalize#",
            "the #environModifier.capitalize# #environ.s.capitalize#",
        ],
        "environ": [
            "tree",
            "cliff",
            "swamp",
            "cave",
            "mountain",
            "hill",
            "river",
            "lake"
        ],
        "environModifier": [
            "life",
            "souls",
            "insanity",
            "power",
            "purity"
        ],
        "setDeliverable": [
            "[deliverable:#item#]"
        ],
        "setCraft": [
            "[make:#brewVerb#][craftable:#brewable#]",
            "[make:#smithVerb#][craftable:#smithable#]",
            "[make:#enchantVerb#][craftable:#smithable#]"
        ],
        "brewVerb": [
            "brew",
            "mix",
            "cook"
        ],
        "smithVerb": [
            "smith",
            "craft"
        ],
        "enchantVerb": [
            "enchant"
        ],
        "setQuestType": [
            "[questType:#travel#][reason:#travelReason#]", #go to [place]
            "[questType:#escort#][reason:#escortReason#]", # #travel# #interact# #guard#
            "[questType:#deliver#][reason:#deliverReason#]", #bring [noun] to [person] at [place] [in [place]]
            "[questType:#fetch#][reason:#fetchReason#]", #get [thing:noun] from [place] and bring #thing# to [other place]

            "[questType:#destroy#][reason:#destroyReason#]", #destroy something
            "#setGuardQuestType#", #guard something, and if threat: destroy threat.

            # "[questType:#skill#][reason:#skillReason#]", #perform [action] using only N skill(s).
            "[questType:#craft#][reason:#craftReason#]", #make [thing]

            "[questType:#solve#][reason:#solveReason#]" #bypass or complete puzzle/test
        ],
        #amount(of times), person1, person2, currentPlace, destination, deliverable
        "travel": [ #quest
            "#travelVerb# #travelDescription#"
        ],
        "travelVerb": [
            "go",
            "travel",
            "journey",
            "venture"
        ],
        "travelDescription": [
            "to #destination#",
            "from #currentPlace# to #destination#",
            "from #currentPlace.capitalize# to #destination#",
            "from #currentPlace# to #destination.capitalize#",
            "from #currentPlace.capitalize# to #destination.capitalize#",
        ],
        "travelReason": [
            "you need to see #destination#",
            "#destination# will change your life",
            "#destination# needs people like you"
        ],
        "escort": [ #quest
            "#get# #person1# #travelDescription#",
            "#travel# with #person1#",
            "take #person1# and #person2# with you when you #travel#",
            "take #person1# and #person2# #travelDescription#",
            "#travel# with #person1# and #person2#"
        ],
        "escortReason": [
            "#person1# needs to see the world",
            "#destination# needs #person1#",
            "#person1# and #person2# are inseparable",
        ],
        "deliver": [ #quest
            "#deliverVerb# #rangeTwoToTenText# #deliverable.s# to #destination#",
            "#deliverVerb# #deliverable.a# to #destination#"
        ],
        "deliverVerb": [
            "deliver",
            "bring",
            "present"
        ],
        "item": [
            "#weapon#",
            "#armor#",
            "#jewelry#",
            "#brewable#",
            "#book#",
            "#food#"
        ],
        "smithable": [
            "#unEnchantedWeapon#",
            "#unEnchantedarmor#",
            "#jewelry#"
        ],
        "unEnchantedWeapon": [
            "#craftsmanship# #weaponMaterial# #weaponType#",
            "#weaponMaterial# #weaponType#",
            "#sharpened# #weaponMaterial# #weaponType#",
            "#sharpened# #weaponType#"
        ],
        "unEnchantedarmor": [
            "#armorType#",
            "#craftsmanship# #armorType#",
            "#weaponMaterial# #armorType#",
            "#craftsmanship# #weaponMaterial# #armorType#"
        ],
        "brewable": [
            "#potion#",
            "#poison#"
        ],
        "weapon": [ # sharpened craftsmanship oiled poisoned weaponMaterial weaponType weaponEnchantDescription
            "#oiled# #weaponMaterial# #weaponType# of #weaponEnchantDescription.capitalize#",
            "poisoned #weaponMaterial# #weaponType# of #weaponEnchantDescription.capitalize#",
            "#craftsmanship# #weaponMaterial# #weaponType# of #weaponEnchantDescription.capitalize#",
            "#weaponMaterial# #weaponType# of #weaponEnchantDescription.capitalize#",
            "#unEnchantedWeapon#"
        ],
        "oiled": [
            "well-oiled",
            "oiled",
            "rusty"
        ],
        "weaponMaterial": [
            "copper",
            "iron",
            "steel",
            "mithril",
            "adamantine",
            "obsidian",
            "titanite"
        ],
        "weaponType": [
            "dagger",
            "sword",
            "axe",
            "club",
            "maul",
            "longsword",
            "battle axe",
            "war hammer"
        ],
        "weaponEnchantDescription": [
            "#iceWeaponEnchantDescription#",
            "#fireWeaponEnchantDescription#",
            "#shockWeaponEnchantDescription#"
        ],
        "iceWeaponEnchantDescription": [
            "frost",
            "ice",
            "blizzards"
        ],
        "fireWeaponEnchantDescription": [
            "flames",
            "scorching",
            "inferno"
        ],
        "shockWeaponEnchantDescription": [
            "shocks",
            "thunder",
            "lightning"
        ],
        # "weaponStyle":[
        #     "#cityName#ian",
        #     "#cityName#",
        #     # "#placeName#",
        #     # "#placeName#ian"
        # ],
        # "forged":[
        #     "#race#-forged"
        # ],
        # "race":[
        #     "dwarf",
        #     "orc",
        #     "goblin",
        #     "elf"
        # ],
        "craftsmanship": [
            "Fine",
            "Superior",
            "Expert",
            "Legendary",
            "Mythic"
        ],
        "sharpened": [
            "sharp",
            "keen",
            "sharpened",
            "honed",
            "razor sharp"
        ],
        "armor": [ #craftsmanship weaponMaterial
            "#unEnchantedarmor#"
        ],
        "armorType": [
            "#head#",
            "#neck#",
            "#fullBody#",

            "#shoulders#",
            "#wrists#",
            "#hands#",
            "#fingers#",

            "#waist#",

            "#legs#",
            "#shins#",
            "#ankles#",
            "#feet#"
        ],
        "head": [
            "helmet",
            "cap",
            "helm"
        ],
        "neck": [
            "throat guard",
            "gorget"
        ],
        "fullBody": [
            "chain-mail",
            "chest plate",
            "armor"
        ],
        "shield": [
            "shield",
            "tower shield",
            "buckler"
        ],
        "shoulders": [
            "pauldrons"
        ],
        "wrists": [
            "wrist-guards"
        ],
        "hands": [
            "gauntlets",
            "gloves"
        ],
        "fingers": [
            "claws"
        ],
        "waist": [
            "belt",
            "bandolier"
        ],
        "legs": [
            "trousers"
        ],
        "shins": [
            "shin-guards"
        ],
        "feet": [
            "boots"
        ],
        "jewelry": [
            "necklace",
            "circlet",
            "crown",
            "ring",
            "bracelet",
            "anklet"
        ],
        "potion": [
            "#brewStrength# #potionDescription# #brewModifier# potion",
            "#brewStrength# #brewModifier# potion",
            "#potionDescription# #brewModifier# potion",
            "#brewModifier# potion"
        ],
        "brewStrength": [
            "weak",
            "potent"
        ],
        "potionDescription": [
            "restore",
            "regenerate"
        ],
        "brewModifier": [
            "health",
            "mana",
            "spirit",
            "courage",
            "stamina"
        ],
        "poison": [
            "#brewStrength# #poisonDescription# #brewModifier# poison",
            "#brewStrength# #brewModifier# poison",
            "#poisonDescription# #brewModifier# poison",
            "#brewModifier# poison"
        ],
        "poisonDescription": [
            "damage",
            "ravage",
            "deteriorate"
        ],
        "book": [
            "The Bard and the Bee", #The #Occupation# and the #smallAnimal#
            "An Idiot's Guide to Killing Everyone Except For The Sentient Creatures You Like",
            "The Apple"
        ],
        "food": [
            "#soupContainer# of #soup#",
            "#starch#",
            "#fruit#"
        ],
        "soupContainer": [
            "bowl",
            "cup"
        ],
        "soup": [
            "soup",
            "stew",
            "broth",
            "bisque"
        ],
        "starch": [
            "bread"
        ],
        "fruit": [
            "#appleModifier# apple",
            "banana"
        ],
        "appleModifier": [
            "green",
            "red",
            "golden"
        ],
        "deliverReason": [
            "#deliverable#",
            "they ordered #deliverable.s# specifically. I'm not sure why. I didn't ask."
        ],
        "fetch": [ #quest
            "#get# #rangeTwoToTenText# #deliverable.s# from #destination#",
            "#get# #deliverable.a# from #destination#"
        ],
        "get": [
            "get",
            "bring",
            "take"
        ],
        "fetchReason": [
            "We need it",
            "I'd really like that"
        ],
        "destroy": [ #quest
            "kill #person1#"
        ],
        "destroyReason": [
            "#genericReason#",
            "if you have a problem with that, tell me now",
            "I want them dead",
            "make them suffer",
            "they need to die"
        ],
        "setGuardQuestType": [
            "[reason:#genericPresentReason#]#guard#",
            "[questType:#guardPerson#][reason:#guardPersonReason#]",
            "[questType:#guardPlace#][reason:#guardPlaceReason#]",
            "[questType:#guardThing#][reason:#guardThingReason#]"
        ],
        "guard": [ #quest
            "[questType:#guardPerson#]",
            "[questType:#guardPlace#]",
            "[questType:#guardThing#]"
        ],
        "guardReason": [
            "#genericPresentReason#"
        ],
        "guardPersonReason": [
            "#person1# can't handle #simpleTask# so they need to be #guardedVerb#",
            "#genericPresentReason#"
        ],
        "guardPerson": [
            "#guardVerb# #person1#",
            "#guardVerb# #person1#",
        ],
        "guardPlace": [
            "#guardVerb# #currentPlace#"
        ],
        "guardPlaceReason": [
            "there have been reports of #intelligentEvilOccupation.s#",
            "#intelligentEvilOccupation.capitalize.s are roaming the area",
            "The army took most of the warriors",
            "#genericPresentReason#"
        ],
        "intelligentEvilOccupation": [
            'bandit',
            'outlaw',
            'thug',
            'assassin',
            'warlord'
        ],
        "guardThing": [
            "#guardVerb# the #thingToBeGuarded#"
        ],
        "guardThingReason": [
            "there have been reports of #intelligentEvilOccupation.s#",
            "#intelligentEvilOccupation.capitalize.s# are roaming the area",
            "#intelligentEvilOccupation.capitalize.s# are notorious near #currentPlace#",
            "we don't want to lose any #craftable.s#",
            "#genericPresentReason#"
        ],
        "thingToBeGuarded": [
            "caravan",
            "ship",
            "shipment",
            "warehouse",
            "storeroom"
        ],
        "guardVerb": [
            "guard",
            "protect",
            "watch",
            "defend"
        ],
        "simpleTask": [
            "sticking their head in a river",
            "holding a weapon without hurting themselves",
            "the simplest task",
            "cleaning up their own mess",
            "cutting butter with a hot knife",
            "staying still and being quiet for more than a minute"
        ],
        "guardedVerb": [
            "babied",
            "watched",
            "looked after"
        ],
        # "skill":[],
        "craft": [ #quest
            "#make# #craftable.a#",
            "#make# #rangeTwoToTenText# #craftable.s#"
        ],
        "craftReason": [
            "#genericReason#"
        ],
        "solve": [ #quest
            "#puzzleSolve# the #puzzle# of #currentPlace#",
            "#puzzleSolve# this #puzzle#"
        ],
        "puzzleSolve": [
            "solve",
            "figure out",
            "think your way through"
        ],
        "puzzle": [
            "#maze#"
        ],
        "maze": [
            "maze",
            "labyrinth"
        ],
        "solveReason": [
            "#genericReason#"
        ],
        "genericReason": [
            "#excuse#",
            "#need#",
            "#need# and #excuse#",
            "#excuse# and #need#"
        ],
        "genericPresentOrFutureReason": [
            "#excuse#",
            "#presentOrFutureNeed#",
            "#presentOrFutureNeed# and #excuse#",
            "#excuse# and #presentOrFutureNeed#"
        ],
        "genericPresentReason": [
            "#excuse#",
            "#presentNeed#",
            "#presentNeed# and #excuse#",
            "#excuse# and #presentNeed#",
        ],
        # "until":[
        #     "#neededBy# the #season#",
        #     "#neededBy# the #timeOfDay#",
        #     "#neededBy# the #calendarMeasure#"
        # ],
        # "calendarMeasure":[
        #     "hour",
        #     "day",
        #     "week",
        #     "month"
        # ],
        # "neededBy":[
        #     "You'll only need to do it #timeConstraint#",
        #     "I need someone #timeConstraint#"
        # ],
        # "timeConstraint":[
        #     "until the end of",
        #     "for"
        # ],
        "need": [
            "#presentNeed#",
            "#pastNeed#",
            "#futureNeed#"
        ],
        "presentOrFutureNeed": [
            "#presentNeed#",
            "#futureNeed#"
        ],
        "presentNeed": [
            "#it# needs to be done", #need
            "#it# has to be done"
        ],
        "pastNeed": [
            "#it# should have been done ages ago"
        ],
        "futureNeed": [
            "#it# #futureNeedTense# by #season#'s end",
            "#it# #futureNeedTense# partway through #season#",
            "#it# #futureNeedTense# by the end of #season#",
            "#it# #futureNeedTense# by the middle of #season#",
            "#it# #futureNeedTense# by the beginning of #season#"
        ],
        "it": [
            "it",
            "this"
        ],
        "futureNeedTense": [
            "will need to happen",
            "has to happen",
            "should be done"
        ],
        "season": [
            "winter",
            "summer",
            "spring",
            "autumn"
        ],
        "excuse": [
            "#sicknessExcuse#",
            "#ageExcuse#",
            "#busyExcuse#",
            "#fearExcuse#",
            "#importanceExcuse#"
        ],
        "sicknessExcuse": [
            "I've been #sicknessSymptom# all #timeOfDay# so I'm too sick",
            "I've been #sicknessSymptom# all #timeOfDay#",
            "I'm too sick",
            "I need to get over this sickness"
        ],
        "timeOfDay": [
            "night",
            "day",
            "morning",
            "evening"
        ],
        "sickness": [
            "#diarrheaModifier# diarrhea",
            "diarrhea",
            "fever",
            "flu"
        ],
        "diarrheaModifier": [
            "explosive",
            "bloody",
            "runny",
            "projectile"
        ],
        "sicknessSymptom": [
            "vomiting",
            "feverish",
            # "waking up and fainting",
            "having seizures"
        ],
        "fearExcuse": [
            "lately I've been too scared to move. I'm anxious all the time"
        ],
        "ageExcuse": [
            "I would do it myself if I were a few decades younger", #age
            "These old bones are too frail to handle it"
        ],
        "busyExcuse": [
            "I need someone that's not busy" #busy-ness
        ],
        "importanceExcuse": [
            "I need to oversee the other operations" #social order
        ],
        "plea": [
            "Please, ",
            "I'm begging you, ",
            "Help me, please! "
        ],
        "quest": [
            "#questType.capitalize#. #reason.capitalize#.",
            "#questType.capitalize#."
        ],
    },
    "adjective" : {
        "origin":[
            "#[quantity:#adjQuantity#][opinion:#adjOpinion#][size:#adjSize#][age:#adjAge#][shape:#adjShape#][colour:#adjColour#][origin:#adjOrigin#][material:#adjMaterial#][purpose:#adjPurpose#]adjectiveOrderList#"
        ],
        "adjectiveOrderList": [ #(2^numAdjCategories) - 1, 2^8-1 = 255
            "#adjectiveQuantity# #noun#"
        ],
        "noun":[
            "knife"
        ],
        "adjectiveQuantity":[
            "[noun:#noun.s#]#quantity# #adjectiveOpinion#",
            "#adjectiveOpinion#"
        ],
        "adjectiveOpinion":[
            "#opinion# #adjectiveSize#",
            "#adjectiveSize#"
        ],
        "adjectiveSize":[
            "#size# #adjectiveAge#",
            "#adjectiveAge#"
        ],
        "adjectiveAge":[
            "#age# #adjectiveShape#",
            "#adjectiveShape#"
        ],
        "adjectiveShape":[
            "#shape# #adjectiveColour#",
            "#adjectiveColour#"
        ],
        "adjectiveColour":[
            "#colour# #adjectiveOrigin#",
            "#adjectiveOrigin#"
        ],
        "adjectiveOrigin":[
            "#origin# #adjectiveMaterial#",
            "#adjectiveMaterial#"
        ],
        "adjectiveMaterial":[
            "#material# #adjectivePurpose#",
            "#adjectivePurpose#"
        ],
        "adjectivePurpose":[
            "#purpose#",
            ""
        ],
        "adjQuantity":[
            "many"
        ],
        "adjOpinion": [
            "lovely"
        ],
        "adjSize": [
            "little"
        ],
        "adjAge": [
            "old"
        ],
        "adjShape": [ #including height and weight
            "rectangular"
        ], 
        "adjColour": [
            "green"
        ],
        "adjOrigin": [ #nationality/planetality/systemality
            "French"
        ], 
        "adjMaterial": [
            "silver"
        ],
        "adjPurpose":[ # or qualifier
            "whittling"
        ] 
    },
    "hi" : {
        "origin": ["#hello.capitalize#, #location#!"],
        "hello": ["hello", "greetings", "howdy", "hey"],
        "location": ["world", "solar system", "galaxy", "universe"]
    }
}

# print(data["adjective"]["origin"])