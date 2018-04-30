'''
This file will have the lists and dictionaries for the Character Generator file
KEEP IN THE SAME DIRECTORY AS THE CHARACTER GENERATOR
'''

Feats = {
    'Darkvision': 'You can see in dim light within 60 ft as if it was normal, and dark as if it were dim.', 'Dwarven Resiliance': 'You have advantage on saving throws against poison, and resistance to poison damage.', 'Dwarven Combat Training': "You have proficiency with the battleaxe, handaxe, throwing hammer, and warhammer.", 'Tool Proficiency (Dwarven)':'You gain proficiency with smith\'s tools, brewer\'s supplies, or mason\'s tools.', 'Stonecunning':'Whenever you make a History check related to the origin of stonework, you are consider proficient and add double your proficiency to the check.', 'Dwarven Toughness':'Your HP maximum increases by 1 every time you increase a level.', 'Dwarven Armor Training':'You have proficiency with light and medium armor.',
    'Keen Senses':'You have proficiency in the Perception skill.', 'Fey Ancestry':'You have advantage on saving throws against being charmed and magic can\'t put you to sleep.', 'Trance':'You don\'t sleep but instead you meditate.', 'Elf Weapon Training':'You have proficiency with the longsword, shortsword, shortbow, and longbow.', 'Cantrip (High Elf)':'You know one cantrip from the wizard spell list (INT is the spellcasting ability).', 'Fleet of Foot':'Your base walking speed increases to 35 ft.', 'Mask of the Wild':'You can attempt to hide when you are only lightly obscured by natural phenomenon', 'Superior Darkvision':'Your darkvision increases to 120 ft', 'Sunlight Sensitivity':'You have disadvantage on attack rolls and Perception checks that rely on sight when you, the target of you target, or whatever you are seeing are in direct sunlight.', 'Drow Magic':'You know the Dancing Lights cantrip. When you reach 3rd level you can cast Farie Fire with this ability. When you reach 5th level you can cast darkness. You can use these once per long rest. CHA is your spellcasting modifier.', 'Drow Weapon Training':'You have proficiencey with rapiers, shortswords, and hand crossbows.',
    'Lucky':'When you roll a 1 on the d20, you can reroll it but you must use the new roll.', 'Brave':'You have advantage on saving throws against getting frightened.', 'Halfling Nimbleness':'You can move through the space of any creature that is of a size larger than yours.', 'Naturally Stealthy':'You can attempt to hide even when you are obscured only by a creature one size larger than you.', 'Stout Resilience':'You have advantage on saving throws against poison, and you have resistance against poison damage.',
    '':'',
    'Draconic Ancestry':'You have draconic ancestry. Your breath weapon and damage resistance are determined by the dragon type. (table on pg 34 PH)', 'Breath Weapon':'You can use your action to exhale destructive energy. When you use your breath weapon, each creature in the area must make a save determined on the table. The DC is 8 + CON + Proficincey modifier. The creatures take 2d6 on a fail or half on a success. this increases by 1d6 at 6th, 11th, and 16th levels. This can only be used once per short rest.', 'Damage Resistance (Dragonborn)':'You have restistance to your Ancestors type.',
    'Gnome Cunning':'You have advantage on all Int, WIS, and CHA saves against magic.', 'Natural Illusionist':'You know the Minor Illusion cantrip. INT is the ability for it.', 'Speak with Small Beasts':'You can communicate simple ideas with small or smaller beasts.', 'Artificer\'s Lore':'Whenever you make a History check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus instead of any normal proficeincey bonus.', 'Tinker':'You have proficiency with Tinker\'s tools. Using those tools, you can spend 1 hour and 10 gp worth of materials to construc a Tiny clockwork device (AC 5 HP 1). The device ceases to function after 24 hrs unless you spend 1 hr repairing it, or use an action to dismantle it. You can have up to 3 devices at once: Clockwork toy: this toy is a tiny clockwork creature. When placed on the ground, the toy moves 5 ft per turn in a random direction. It makes noise appropriate to the creature it represents. Fire Starter: The device produces a minacture flame that can light a small fire (this takes an action). Music Box: When opened, this music box plays a single song at a moderate volume.',
    'Skill Versatility':'You gain proficiencey in two skills.', 
    'Menacing':'You gain proficiency in the Intimidation skill.', 'Relentless Endurance':'When you are reduced to 0 HP, you can drop to 1 HP instead. You can only use this once per long rest.', 'Savage Attacks':'When you score a critical hit with a melee weapon attack, you can add another one of the weapon\'s dice.',
    'Hellish Resistance':'You have resistance to fire damage.', 'Infernal Legacy':'You know the Thaumaturgy cantrip. When you reach 3rd level you can sat hellish rebuke as a 2nd level spell, and at 5th level you can cast darkness. You can do this once per long rest and CHA is your spell casting ability.',
    'Celestial Resistance':'You have resistance to necrotic damage and radiant damage.','Healing Hands':'As an actoin, you can touch a creature and cause it to regain a number of hit points equal to your level. You can only use this once per long rest.', 'Light Bearer':'You know the Light cantrip. Charisma is your spellcasting ability for it.', 'Radiant Soul':'Starting at 3rd level, you can use your action to unleash divine energy causing your eyes to glow and grow glowing wings. Your transformation lasts for 1 min or until you end it as a bonus action. During it, you have a flying speed of 30 ft and once on each of your turns, you can deal extra radiant damage equal to your level to one target. You can use this once per long rest.', 'Radiant Consumption':'Starting at 3rd level, you can use your action to unleash searing light. Your transformation lasts for 1 min or until you end it as a bonus action. During it, you shed bright light in a 10 ft radius and at the end of each of your turns, you and each creature within 10 ft of you take radiant damage equal to half your level. In addition, you can deal extra radiant damage to one target equal to your level. You can use this once per long rest.', 'Necrotic Shroud':'Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to glow and ghostly wings to apear out of your back. The instant you transform, other creatures within 10 ft of you that can see you must each succeed on a CHA save or become frightened until the end of your next turn. Your transformation lasts for 1 min or until you end it as a bonus action. Once on each of your turns you can deal extra necrotic damage equal to your level. You can use this once per long rest.',
    'Firblog Magic':'You can cast Detect Magic and Disguise Self with this trait using WIS. You can use this once per short rest. You can make yourself appear 3 ft shorter with disguise self.', 'Hidden Step':'As a bonus action, you can magically turn invisible until the start of your next turn or until you attack. You can use this once per short rest. ', 'Powerful Build':'You count as one size larger when determining your carrying capacity and the weight you can push drag and lift.', 'Speech of Beast and Leaf':'You can communicate in a rudimentary way with beast and animals and have advantage on all CHA checks with them.',
    'Natural Athlete':'You have proficiency in Athletics', 'Stone\'s Endurance':'You can focus and shrug off an attack. When you take damage, you can use your reaction to reduce the damage by 1d12 + CON. You can use this once per short rest.', 'Mountain Born':'You are acclimated to high altitudes of 20,000 ft and cold weather.',
    'Expert Forgery':'You can duplicate other creatures\' handwriting. You have advantage on all checks made to produce forgeries or duplicates of existing objects.', 'Kenku Training':'You are proficient in 2 out of Acrobatics, Deception, Stealth, and Sleight of Hand.', 'Mimicry':'You can mimic sounds you have heard, including voices. Creatures can check to see if its believable by making a contested Insight v Deception check. This is the only way you can speak.',
    'Lizardfolk Swimming Speed':'You have a swimming speed of 30 ft.', 'Bite':'Your unarmed attacks deal 1d6 + STR piercing damage.', 'Cunning Artisan':'As part of a short rest, you can harvest bone and hide from a slain creature and craft one of the following items: shield, club, javelin, or 1d4 darts.', 'Hold Breath':'You can hold your breath for up to 15 minutes.', 'Hunter\'s Lore':'You are proficient in two of the following: Animal Handling, Nature, Perception, Stealth, and Survival.', 'Natural Armor':'You have tough, scaly skin. When you arent wearing armor, your AC is 13 + your DEX. You can use your natural armor if it is better than your armor.',
    'Feline Agility':'Your reflexes and agility allow you to move with a burst of speed. When you move on your turn in combat, you can double your speed until the end of your turn. Once you use this trait, you can\'t use it again until you move 0 feet on one of your turns.','Cat\'s Claws':'Because of your claws, you have a climbing speed of 20 ft. In addition, your claws make it so your unarmed attack deals 1d4 + STR slashing damage.','Cat\'s Talent':'You are proficient in Stealth and Proficiencey',
    'Triton Swimming Speed':'You have a swimming speed of 30 ft.', 'Amphibious':'You can breath air and water.', 'Control Air and Water':'As a child of the sea, you can call upon the elements. You can cast Fog Cloud with this trait. Starting at 3rd level you can cast Gust of Wind, and at 5th level you can cast Wall of Water. Once you cast a spell with this trait, you can\'t use it again until you take a long rest. CHA is your spellcasting modifier.', 'Emissary of the Sea':'Aquatic beasts have an extraordinary affinity with your people. You can communicate simple ideas with water based beasts.', 'Guardians of the Depths':'You have resistance to cold damage and ignore drawbacks caused by an underwater enviorment.',
    '':'',
    'Shelter of the Faithful':'',
    'False Identity':'',
    'Criminal Contact':'',
    'By Popular Demand':'',
    'Rustic Hospitality':'',
    'Guild Membership':'',
    'Discovery':'',
    'Postion of Privilege':'',
    'Wanderer':'',
    'Reasearcher':'',
    'Ship\'s Passage':'',
    'Military Rank':''
}

loSkills = [
    'Strength Save', 'Dexterity Save', 'Constitution Save', 'Inteligence Save', 'Wisdom Save', 'Charisma Save', 
    'Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 
    'Insight', 'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 
    'Performance', 'Persuasion', 'Religion', 'Slieght of Hand', 'Stealth', 'Survival' 
]

loBackground = ['Acolyte','Charlatan','Criminal','Entertainer','Folk_Hero','Guild_Artisan','Hermit','Noble','Outlander','Sage','Sailor','Soldier','Urchin']

loClass = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']

loRace = ['Dwarf','Elf','Halfling','Human','Dragonborn','Gnome','Half_Elf','Half_Orc','Tiefling','Aasimar','Firblog','Goliath','Kenku','Lizardfolk','Tabaxi','Triton','Monstrous']

Alignments = ['Lawful Good','Neutral Good','Chaotic Good','Lawful Neutral','True Neutral','Chaotic Neutral','Lawful Evil','Neutral Evil','Chaotic Evil']

loLanguages = [
    'Common', 'Draconic', 'Dwarvish', 'Elvish', 'Giant', 
    'Gnomish', 'Goblish', 'Halfling', 'Orcish', 'Abyssal', 
    'Celestial', 'Infernal', 'Primordial', 'Sylvan', 'Undercommon' 
]

dAncestry = ['Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White']

GamingSets = ['Dice set','Dragonchess set','Playing Card set','Three-Dragon Ante set']

MusicalInstruments = ['Bagpipes','Drum','Dulcimer','Flute','Lute','Lyre','Horn','Pan Flute','Shawm','Viol']

Tools = ['Alchemist\'s supplies','Brewer\'s supplies','Calligrapher\'s supplies','Carpenter\'s tools','Cartographer\'s tools','Cobbler\'s tools','Cook\'s utensils','Glassblower\'s tools','Jeweler\'s tools','Leatherworker\'s tools','Mason\'s tools','Painter\'s supplies','Potter\'s tools','Smith\'s tools','Tinker\'s tools','Weaver\'s tools','Woodcarver\'s tools']

LightArmor = []

MediumArmor = []

HeavyArmor = []

SimpleWeapons = []

MartialWeapons = []