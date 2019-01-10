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
    "Hero's Journey" : { #TODO THESE NEED MORE CONCISE NAMES
    #TODO FILL THESE OUT WITH SEQUENTIAL OPERATIONS
        "Miraculous or unusual circumstances around the Hero's conception or birth.":# Bonus points if there was a prophecy. Less common in modern stories, which tend to emphasize the role of personal choice in defining a hero, although there may still be a Prophecy Twist involved.
        [],
        "Begins in the ordinary world of the Hero's hometown": # often in one of two flavours:
        # The Good Kingdom, for a story in which the Hero must save the world from impending doom, and
        # The Wasteland, for a story in which the Hero must restore their world.
        # Suburbia can be either, depending on where the story falls on the Sliding Scale of Idealism vs. Cynicism.
        [],
        "The Hero may be dissatisfied with the ordinary and express a desire for adventure.": # In musicals this can be expressed through an "I Want" Song.
        [],
        "The Herald brings a Call to Adventure.": # The Hero learns that they must leave the known world behind and travel into the land of adventure.
        [],
        # The Hero must then decide how to answer the Call:
        "Refusal of the Call": #More common in classic stories. The Call will often try again because The Call Knows Where You Live. Can't Stay Normal and Resigned to the Call are special cases of call refusal.
        [],
        "Jumped at the Call": #, sometimes even in the face of Adventure Rebuff: More common in modern stories. The modern subversion of this is when the hero is Resigned to the Call. They accept it, but only because they feel it would be pointless to resist, and not because they're particularly happy about the thought of adventure. If the hero finds themself abducted by destiny before even knowing what the Call is or even that they were addressed, then they may be a Cosmic Plaything. Resigning oneself to fate becomes easier in these situations. Just like its enthusiastic counterpart, this version of the narrative is more common in modern tales than classic ones.
        [],
        #Frequently, the first step on the Journey is receiving some kind of magical tchotchke or other 
        "Supernatural Aid":
        [],
        "Crossing the First Threshold": #The Hero must make a conscious, willing decision to embark on the adventure and leave the known world behind. This is the First Threshold. The Hero may have to defeat Threshold Guardians, who are not necessarily adversarial but do test the Hero's resolve. Down the Rabbit Hole is a special case for young heroines embarking on supernatural adventures.
        [],
        "The Land of Adventure": #the Hero enters a strange, dreamlike realm, where logic is topsy-turvy and the "rules" are markedly different from the ordinary world. Carl Jung identified the Ordinary Realm with the conscious mind, and the Realm of Adventure with the subconscious mind.
        #One may meet their Hero Partners here and rescue a Damsel in Distress.
        [],
        "The Spiritual Death and Rebirth": # represents a symbolic death for the Hero: the Hero is defeated and killed, their flesh scattered, ready to be reborn and emerge as a new person. If you think the symbolic death ought to come later, don't worry: The Writer's Journey omits this step altogether in favor of a Resurrection step just before the end.
        # Part of this step involves the Hero Losing the Guide.
        [],
        "Road of Trials": #the path out of the Belly of the Whale. Usually the meat of the story; The Writer's Journey calls it Tests, Allies, Enemies, while Booker goes into detail on different types of tests (deadly terrain, monsters, temptations, deadly opposites, and a journey to the underworld). Stops along the way might include:
        # The Shapeshifter: someone you don't trust but nonetheless need for their capabilities or knowledge.
        # The Goddess
        # The Temptress
        # Atonement With the Father: George Lucas loved this step. Oedipus probably didn't. Variants include a final showdown with an Archnemesis Dad (sometimes still ending in atonement if Death Equals Redemption) and Calling the Old Man Out
        # At least one "Leave Your Quest" Test, usually after meeting the Goddess or Temptress.
        [],
        "Night Sea Voyage": #the Hero must sneak into the Big Bad's Elaborate Underground Base and retrieve something or someone. Campbell noted that these Stealth Runs were usually at night and often involved water; hence the name.
        # Link's initial attempt at rescuing Aryll from the Forsaken Fortress in The Legend of Zelda: The Wind Waker is a near-perfect example of one of these.
        # Perhaps the best known example is the infiltration of the Death Star by Luke Skywalker to rescue Princess Leia.
        [],
        "Time out just before the big battle": #the Heroes gather around a campfire and prepare for the battle, tell stories, confess their feelings, etc. It reminds them of what's at stake, and serves as a breather after all the action of the Road of Trials.
        [],
        "Apotheosis / Fight against the Big Bad / Ultimate Boon": #(These are typically very closely related, often intertwined.)
        # Apotheosis: The Hero comes to view the world in a new and radically different way, either because of a critical breakthrough they've made or some crucial information they've uncovered. If it is something to do with themself then this is a good time for an I Am Who?.
        # The Hero confronts the Big Bad: Typically this plays out in a David vs. Goliath fashion. They are usually called upon to sacrifice themself, or something or someone important to them. A Friend or Idol Decision is a common scenario. Note that asked is the key word here—it's usually enough that the Hero be willing to sacrifice something without actually having to do it. Someone else will sacrifice themself in the Hero's stead, or the Hero will prove to have outwitted the Big Bad somehow (so that the apparent sacrifice isn't really a sacrifice), or it was all a Secret Test of Character, or…
        # The Ultimate Boon: getting the reward the hero's been chasing all this time, often but not always a MacGuffin.
        # The Final Temptation is often involved in one or more of these three events: A hero originally motivated by a self-serving goal may receive their Ultimate Boon with the option to take it and run before saving the day. A hero on a Homeward Journey may find a way home, but turn back after their Apotheosis makes them realize their work isn't done. Another may be offered the Ultimate Boon or a tempting substitute by the Big Bad…in exchange for stepping aside. Still another may find that the Ultimate Boon is exactly the sacrifice they are required to make to defeat the Big Bad.
        [],
        "Refusal of the Return": #At this point in the story, the Hero has mastered the strange world they were thrust into. They probably have earned a permanent place here, if they want it. They may even want to stay, but usually there are forces at work that propel them home.
        [],
        "The Return": #Also called the Magic Flight; the Hero now has the boon and high-tails it away, with the villain and/or their forces in hot pursuit, the two parties locked in a battle of wits and magic (especially shapeshifting) during the chase. (See the Celtic story of Taliesin's escape from Cerridwen for a textbook example of this.) The Hero's escape may not require actual magic, but will require all of the new skills they've learned and new allies they've made. Or alternately they could realize the Awful Truth that they can't return home because sometimes Failure Is the Only Option…
        [],
        "Crossing the Return Threshold": #Sometimes a fight against the forces of the Muggle world, which the Hero wins thanks to help from their Muggle allies. This is where the Post-Climax Confrontation happens, as the remaining antagonistic forces have followed the Hero beyond the threshold and attacked them at a time when the plot should be wrapping up. In the absence of any action, it may be a Boring Return Journey instead, a chance for the Hero to reflect on what they've gained and experienced throughout their journey.
        [],
        "Freedom to Live": #The Hero grants the boon to their people.
        [], 
        "Celebration": #A Dance Party Ending is often in order.
        []
    },
    "VladimirPropp" : { #TODO FILL THESE OUT WITH SEQUENTIAL OPERATIONS
        "ABSENTATION": #A member of the hero's community or family leaves the security of the home environment. This may be the hero themselves, or some other relation that the hero must later rescue. This division of the cohesive family injects initial tension into the storyline. This may serve as the hero's introduction, typically portraying them as an ordinary person.
        [],
        "INTERDICTION": # A forbidding edict or command is passed upon the hero ('don't go there', 'don't do this'). The hero is warned against some action.
        [],
        "VIOLATION of INTERDICTION": #The prior rule is violated. Therefore the hero did not listen to the command or forbidding edict. Whether committed by the Hero by accident or temper, a third party or a foe, this generally leads to negative consequences. The villain enters the story via this event, although not necessarily confronting the hero. They may be a lurking and manipulative presence, or might act against the hero's family in his absence.
        [],
        "RECONNAISSANCE": #The villain makes an effort to attain knowledge needed to fulfill their plot. Disguises are often invoked as the villain actively probes for information, perhaps for a valuable item or to abduct someone. They may speak with a family member who innocently divulges a crucial insight. The villain may also seek out the hero in their reconnaissance, perhaps to gauge their strengths in response to learning of their special nature.
        [],
        "DELIVERY": #The villain succeeds at recon and gains a lead on their intended victim. A map is often involved in some level of the event.
        [],
        "TRICKERY": #The villain attempts to deceive the victim to acquire something valuable. They press further, aiming to con the protagonists and earn their trust. Sometimes the villain make little or no deception and instead ransoms one valuable thing for another.
        [],
        "COMPLICITY": #The victim is fooled or forced to concede and unwittingly or unwillingly helps the villain, who is now free to access somewhere previously off-limits, like the privacy of the hero's home or a treasure vault, acting without restraint in their ploy.
        [],
        "VILLAINY or LACKING": #The villain harms a family member, including but not limited to abduction, theft, spoiling crops, plundering, banishment or expulsion of one or more protagonists, murder, threatening a forced marriage, inflicting nightly torments and so on. Simultaneously or alternatively, a protagonist finds they desire or require something lacking from the home environment (potion, artifact, etc.). The villain may still be indirectly involved, perhaps fooling the family member into believing they need such an item.
        [],
        "MEDIATION":  # One or more of the negative factors covered above comes to the attention of the Hero, who uncovers the deceit/perceives the lacking/learns of the villainous acts that have transpired.
        [],
        "BEGINNING COUNTERACTION": # The hero considers ways to resolve the issues, by seeking a needed magical item, rescuing those who are captured or otherwise thwarting the villain. This is a defining moment for the hero, one that shapes their further actions and marks the point when they begin to fit their noble mantle.
        [],
        "DEPARTURE":  #The hero leaves the home environment, this time with a sense of purpose. Here begins their adventure.
        [],
        "FIRST FUNCTION OF THE DONOR": #The hero encounters a magical agent or helper (donor) on their path, and is tested in some manner through interrogation, combat, puzzles or more.
        [],
        "HERO'S REACTION": #The hero responds to the actions of their future donor; perhaps withstanding the rigours of a test and/or failing in some manner, freeing a captive, reconciles disputing parties or otherwise performing good services. This may also be the first time the hero comes to understand the villain's skills and powers, and uses them for good.
        [],
        "RECEIPT OF A MAGICAL AGENT": #The hero acquires use of a magical agent as a consequence of their good actions. This may be a directly acquired item, something located after navigating a tough environment, a good purchased or bartered with a hard-earned resource or fashioned from parts and ingredients prepared by the hero, spontaneously summoned from another world, a magical food that is consumed, or even the earned loyalty and aid of another.
        [],
        "GUIDANCE": #The hero is transferred, delivered or somehow led to a vital location, perhaps related to one of the above functions such as the home of the donor or the location of the magical agent or its parts, or to the villain.
        [],
        "STRUGGLE": #The hero and villain meet and engage in conflict directly, either in battle or some nature of contest.
        [],
        "BRANDING": #The hero is marked in some manner, perhaps receiving a distinctive scar or granted a cosmetic item like a ring or scarf.
        [],
        "VICTORY": #The villain is defeated by the hero – killed in combat, outperformed in a contest, struck when vulnerable, banished, and so on.
        [],
        "LIQUIDATION": #The earlier misfortunes or issues of the story are resolved; object of search are distributed, spells broken, captives freed.
        [],
        "RETURN": #The hero travels back to their home.
        [],
        "PURSUIT": #The hero is pursued by some threatening adversary, who perhaps seek to capture or eat them.
        [],
        "RESCUE":#The hero is saved from a chase. Something may act as an obstacle to delay the pursuer, or the hero may find or be shown a way to hide, up to and including transformation unrecognisably. The hero's life may be saved by another.
        [],
        "UNRECOGNIZED ARRIVAL": #The hero arrives, whether in a location along their journey or in their destination, and is unrecognised or unacknowledged.
        [],
        "UNFOUNDED CLAIMS": #A false hero presents unfounded claims or performs some other form of deceit. This may be the villain, one of the villain's underlings or an unrelated party. It may even be some form of future donor for the hero, once they've faced their actions.
        [],
        "DIFFICULT TASK": #A trial is proposed to the hero – riddles, test of strength or endurance, acrobatics and other ordeals.
        [],
        "SOLUTION": #The hero accomplishes a difficult task.
        [],
        "RECOGNITION": #The hero is given due recognition – usually by means of their prior branding.
        [],
        "EXPOSURE": #The false hero and/or villain is exposed to all and sundry.
        [],
        "TRANSFIGURATION": #The hero gains a new appearance. This may reflect aging and/or the benefits of labour and health, or it may constitute a magical remembering after a limb or digit was lost (as a part of the branding or from failing a trial). Regardless, it serves to improve their looks.
        [],
        "PUNISHMENT": #The villain suffers the consequences of their actions, perhaps at the hands of the hero, the avenged victims, or as a direct result of their own ploy.
        [],
        "WEDDING": #The hero marries and is rewarded or promoted by the family or community, typically ascending to a throne.
        []
    },
    "hi" : {
        "origin": ["#hello.capitalize#, #location#!"],
        "hello": ["hello", "greetings", "howdy", "hey"],
        "location": ["world", "solar system", "galaxy", "universe"]
    }
}

# print(data["adjective"]["origin"])