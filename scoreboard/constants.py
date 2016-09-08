"""Defines useful constants."""

import re
from collections import namedtuple

Species = namedtuple('Species', ['short', 'full', 'playable'])
Background = namedtuple('Background', ['short', 'full', 'playable'])
God = namedtuple('God', ['name', 'playable'])
Achievement = namedtuple('Achievement',
                         ['key', 'name', 'description', 'hidden', 'players'])

SPECIES = {
    Species('Ce', 'Centaur', True),
    Species('DD', 'Deep Dwarf', True),
    Species('DE', 'Deep Elf', True),
    Species('Dg', 'Demigod', True),
    Species('Dr', 'Draconian', True),
    Species('Ds', 'Demonspawn', True),
    Species('Fe', 'Felid', True),
    Species('Fo', 'Formicid', True),
    Species('Gh', 'Ghoul', True),
    Species('Gr', 'Gargoyle', True),
    Species('HE', 'High Elf', True),
    Species('HO', 'Hill Orc', True),
    Species('Ha', 'Halfling', True),
    Species('Hu', 'Human', True),
    Species('Ko', 'Kobold', True),
    Species('Mf', 'Merfolk', True),
    Species('Mi', 'Minotaur', True),
    Species('Mu', 'Mummy', True),
    Species('Na', 'Naga', True),
    Species('Op', 'Octopode', True),
    Species('Og', 'Ogre', True),
    Species('Sp', 'Spriggan', True),
    Species('Te', 'Tengu', True),
    Species('Tr', 'Troll', True),
    Species('VS', 'Vine Stalker', True),
    Species('Vp', 'Vampire', True),
    # Non-playable species
    Species('El', 'Elf', False),
    Species('Gn', 'Gnome', False),
    Species('OM', 'Ogre-Mage', False),
    Species('HD', 'Hill Dwarf', False),
    Species('MD', 'Mountain Dwarf', False),
    Species('GE', 'Grey Elf', False),
    Species('SE', 'Sludge Elf', False),
    Species('LO', 'Lava Orc', False),
    Species('Dj', 'Djinni', False),
    Species('Pl', 'Plutonian', False),
}

BACKGROUNDS = {
    Background('AE', 'Air Elementalist', True),
    Background('AK', 'Abyssal Knight', True),
    Background('AM', 'Arcane Marksman', True),
    Background('Ar', 'Artificer', True),
    Background('As', 'Assassin', True),
    Background('Be', 'Berserker', True),
    Background('CK', 'Chaos Knight', True),
    Background('Cj', 'Conjuror', True),
    Background('EE', 'Earth Elementalist', True),
    Background('En', 'Enchanter', True),
    Background('FE', 'Fire Elementalist', True),
    Background('Fi', 'Fighter', True),
    Background('Gl', 'Gladiator', True),
    Background('Hu', 'Hunter', True),
    Background('IE', 'Ice Elementalist', True),
    Background('Mo', 'Monk', True),
    Background('Ne', 'Necromancer', True),
    Background('Sk', 'Skald', True),
    Background('Su', 'Summoner', True),
    Background('Tm', 'Transmuter', True),
    Background('VM', 'Venom Mage', True),
    Background('Wn', 'Wanderer', True),
    Background('Wr', 'Warper', True),
    Background('Wz', 'Wizard', True),
    # Non-playable backgrounds
    Background('Cr', 'Crusader', False),
    Background('DK', 'Death Knight', False),
    Background('He', 'Healer', False),
    Background('He', 'Healer', False),
    Background('Pa', 'Paladin', False),
    Background('Pa', 'Paladin', False),
    Background('Pr', 'Priest', False),
    Background('Re', 'Reaver', False),
    Background('St', 'Stalker', False),
    Background('Th', 'Thief', False),
    Background('Jr', 'Jester', False),
}

GODS = {
    God('Ashenzari', True),
    God('Atheist', True),
    God('Beogh', True),
    God('Cheibriados', True),
    God('Dithmenos', True),
    God('Elyvilon', True),
    God('Fedhas', True),
    God('Gozag', True),
    God('Hepliaklqana', True),
    God('Jiyva', True),
    God('Kikubaaqudgha', True),
    God('Lugonu', True),
    God('Makhleb', True),
    God('Nemelex Xobeh', True),
    God('Okawaru', True),
    God('Qazlal', True),
    God('Ru', True),
    God('Sif Muna', True),
    God('The Shining One', True),
    God('Trog', True),
    God('Uskayaw', True),
    God('Vehumet', True),
    God('Xom', True),
    God('Yredelemnul', True),
    God('Zin', True),
    # Non-playable gods
    God('Pakellas', False)
}

PLAYABLE_SPECIES = {s for s in SPECIES if s.playable}
PLAYABLE_BACKGROUNDS = {b for b in BACKGROUNDS if b.playable}
PLAYABLE_GODS = {g for g in GODS if g.playable}
NONPLAYABLE_COMBOS = ['FeGl', 'FeAs', 'FeHu', 'FeAM', 'DgBe', 'DgCK', 'DgAK',
                      'GhTm', 'MuTm']
PLAYABLE_COMBOS = ('%s%s' % (rc.short, bg.short)
                   for rc in PLAYABLE_SPECIES for bg in PLAYABLE_BACKGROUNDS
                   if '%s%s' % (rc, bg) not in NONPLAYABLE_COMBOS)
GOD_NAME_FIXUPS = {
    # Actually, the ingame name is 'the Shining One', but that looks
    # ugly since the capitalisation is wrong.
    'the Shining One': 'The Shining One',
    # Old name
    'Dithmengos': "Dithmenos",
    'Iashol': 'Ru',
    'Ukayaw': 'Uskayaw',
    # Nostalgia names
    'Lugafu': 'Trog',
    'Lucy': 'Lugonu',
    'Feawn': 'Fedhas'
}
BACKGROUND_SHORTNAME_FIXUPS = {'Am': 'AM'}
SPECIES_SHORTNAME_FIXUPS = {'Ke': 'Te', 'DS': 'Ds', 'DG': 'Dg', 'OP': 'Op'}
SPECIES_NAME_FIXUPS = {
    'Yellow Draconian': 'Draconian',
    'Grey Draconian': 'Draconian',
    'White Draconian': 'Draconian',
    'Green Draconian': 'Draconian',
    'Purple Draconian': 'Draconian',
    'Mottled Draconian': 'Draconian',
    'Black Draconian': 'Draconian',
    'Red Draconian': 'Draconian',
    'Pale Draconian': 'Draconian',
    'Grotesk': 'Gargoyle',
    'Kenku': 'Tengu',
}
BRANCH_NAME_FIXUPS = {
    # April fool's one year
    'Nor': 'Coc',
    # Rename
    'Vault': 'Vaults',
    'Shoal': 'Shoals'
}

Branch = namedtuple('Branch', ['short', 'full', 'multilevel', 'playable'])
BRANCHES = {
    Branch('D', 'Dungeon', True, True),
    Branch('Lair', 'Lair of the Beasts', True, True),
    Branch('Temple', 'Ecumenical Temple', False, True),
    Branch('Orc', 'Orcish Mines', True, True),
    Branch('Vaults', 'Vaults', True, True),
    Branch('Snake', 'Snake Pit', True, True),
    Branch('Swamp', 'Swamp', True, True),
    Branch('Shoals', 'Shoals', True, True),
    Branch('Spider', 'Spider Nest', True, True),
    Branch('Elf', 'Elven Halls', True, True),
    Branch('Zig', 'Ziggurat', True, True),
    Branch('Depths', 'Depths', True, True),
    Branch('Abyss', 'Abyss', True, True),
    Branch('Sewer', 'Sewer', False, True),
    Branch('Pan', 'Pandemonium', False, True),
    Branch('Crypt', 'Crypt', True, True),
    Branch('Slime', 'Slime Pits', True, True),
    Branch('Zot', 'Realm of Zot', True, True),
    Branch('Ossuary', 'Ossuary', False, True),
    Branch('IceCv', 'Ice Cave', False, True),
    Branch('Hell', 'Vestibule of Hell', False, True),
    Branch('Lab', 'Labyrinth', False, True),
    Branch('Bailey', 'Bailey', False, True),
    Branch('Volcano', 'Volcano', False, True),
    Branch('Tomb', 'Tomb of the Ancients', True, True),
    Branch('Dis', 'Iron City of Dis', True, True),
    Branch('Tar', 'Tartarus', True, True),
    Branch('Geh', 'Gehenna', True, True),
    Branch('Coc', 'Cocytus', True, True),
    Branch('Bazaar', 'Bazaar', False, True),
    Branch('WizLab', "Wizard\'s Laboratory", False, True),
    Branch('Trove', 'Treasure Trove', False, True),
    Branch('Desolation', 'Desolation of Salt', False, True),
    # Non-playable branches
    Branch('Hive', 'Hive', True, False),
    Branch('Blade', 'Hall of Blades', True, False),
    Branch('Forest', 'Enchanted Forest', True, False),
    Branch('Shrine', 'Shrine', False, True),
}
GLOBAL_TABLE_LENGTH = 50
FRONTPAGE_TABLE_LENGTH = 10
PLAYER_TABLE_LENGTH = 10
BLACKLISTS = {'griefers': {},
              'bots':
              {'autorobin', 'xw', 'auto7hm', 'rw', 'qw', 'ow', 'qwrobin', 'gw',
               'notqw', 'jw', 'parabodrick', 'hyperqwbe', 'cashybrid',
               'tstbtto', 'parabolic', 'oppbolic', 'ew', 'rushxxi', 'gaubot',
               'cojitobot', 'paulcdejean', 'otabotab', 'nakatomy', 'testingqw',
               'beemell', 'beem', 'drasked', 'phybot', 'khrogbot'}}
TABLE_CLASSES = "table table-hover table-striped"
LOGFILE_REGEX = re.compile('(logfile|allgames)')
MILESTONE_REGEX = re.compile('milestone')
KTYPS = ("mon",
         "beam",
         "quitting",
         "leaving",
         "pois",
         "winning",
         "acid",
         "cloud",
         "disintegration",
         "wild_magic",
         "starvation",
         "trap",
         "spore",
         "burning",
         "targeting",
         "draining",
         "water",
         "rotting",
         "something",
         "curare",
         "stupidity",
         "bounce",
         "targetting",
         "self_aimed",
         "spines",
         "rolling",
         "lava",
         "barbs",
         "falling_down_stairs",
         "divine_wrath",
         "xom",
         "weakness",
         "clumsiness",
         "being_thrown",
         "wizmode",
         "beogh_smiting",
         "headbutt",
         "mirror_damage",
         "freezing",
         "reflect",
         "collision",
         "petrification",
         "tso_smiting",
         "falling_through_gate", )
KTYP_FIXUPS = {
    # Renames
    'divine wrath': 'divine_wrath',
    'wild magic': 'wild_magic',
    'self aimed': 'self_aimed',
    'falling down stairs': 'falling_down_stairs'
}
ACHIEVEMENTS = (
    Achievement('won1', 'It belongs in a Museum!',
                'Escape with the Orb of Zot.', False, tuple()),
    Achievement('wondur2.5hr', 'Under 9000',
                'Win a game in under two and a half hours.', False, tuple()),
    Achievement('fivebyfive', 'Five by Five',
                'Win a game in under 55,555 turns.', False, tuple()),
    Achievement('gselfkill', 'Unnatural Selection', 'Die to your own ghost.',
                False, tuple()),
    Achievement('lostwith3+runes', 'Hubris', 'Die with at least three runes.',
                False, tuple()),
    Achievement('75tdam', 'Annihilated',
                'Die after taking 75 damage (or more).', False, tuple()),
    Achievement('all_species', 'Xenophiliac',
                'Win a game with every playable species.', False, tuple()),
    Achievement('all_backgrounds', 'Jack of all Trades',
                'Win a game with every playable background.', False, tuple()),
    Achievement('all_gods', 'Polytheist',
                'Win a game with every playable god.', False, tuple()),
    Achievement('0.18_first', '0.18 Tournament: First Place',
                'First place in the 0.18 tournament, May 2016.', True,
                ('Yermak', )),
    Achievement('0.18_second', '0.18 Tournament: Second Place',
                'Second place in the 0.18 tournament, May 2016.', True,
                ('Demise', )),
    Achievement('0.18_third', '0.18 Tournament: Third Place',
                'Third place in the 0.18 tournament, May 2016.', True,
                ('Ultraviolent4', )),
    Achievement(
        '0.18_clan_first', '0.18 Tournament: First Place (Clan)',
        'Part of the first placed clan in the 0.18 tournament, May 2016.',
        True, ('WalkerBoh', 'MorganLeah', 'Snack', 'moose', 'n1000', 'Lasty')),
    Achievement(
        '0.18_clan_second', '0.18 Tournament: Second Place (Clan)',
        'Part of the second placed clan in the 0.18 tournament, May 2016.',
        True, ('Demise', 'BobtheCannibal69', 'Megaslime', 'Ultraviolent4',
               'chequers', 'krfreak')),
    Achievement(
        '0.18_clan_third', '0.18 Tournament: Third Place (Clan)',
        'Part of the third placed clan in the 0.18 tournament, May 2016.',
        True,
        ('irum', 'Dowan', 'SilvereR', 'mooon', 'sheltermaker01', 'thrrja')),
    Achievement('0.17_first', '0.17 Tournament: First Place',
                'First place in the 0.17 tournament, November 2015.', True,
                ('cosmonaut', )),
    Achievement('0.17_second', '0.17 Tournament: Second Place',
                'Second place in the 0.17 tournament, November 2015.', True,
                ('johnnyzero', )),
    Achievement('0.17_third', '0.17 Tournament: Third Place',
                'Third place in the 0.17 tournament, November 2015.', True,
                ('iafm', )),
    Achievement(
        '0.17_clan_first', '0.17 Tournament: First Place (Clan)',
        'Part of the first placed clan in the 0.17 tournament, November 2015.',
        True,
        ('tasonir', 'SaintRoka', 'Sharkman1231', 'Sphara', 'glosham', 'mopl')),
    Achievement(
        '0.17_clan_second', '0.17 Tournament: Second Place (Clan)',
        'Part of the second placed clan in the 0.17 tournament, November 2015.',
        True, ('Vidiiot', 'banto', 'Wizzzargh', 'ayayaya', 'bart', 'emiel')),
    Achievement(
        '0.17_clan_third', '0.17 Tournament: Third Place (Clan)',
        'Part of the third placed clan in the 0.17 tournament, November 2015.',
        True,
        ('MorganLeah', 'Kramin', 'Lasty', 'Suckerboh', 'moose', 'rchandra')),
    Achievement('0.16_first', '0.16 Tournament: First Place',
                'First place in the 0.16 tournament, May 2015.', True,
                ('DrKe', )),
    Achievement('0.16_second', '0.16 Tournament: Second Place',
                'Second place in the 0.16 tournament, May 2015.', True,
                ('Zooty', )),
    Achievement('0.16_third', '0.16 Tournament: Third Place',
                'Third place in the 0.16 tournament, May 2015.', True,
                ('Yermak', )),
    Achievement(
        '0.16_clan_first', '0.16 Tournament: First Place (Clan)',
        'Part of the first placed clan in the 0.16 tournament, May 2015.',
        True,
        ('BLOAX', '4thArraOfDagon', 'Vidiiot', 'Yermak', 'Zooty', 'timbw')),
    Achievement(
        '0.16_clan_second', '0.16 Tournament: Second Place (Clan)',
        'Part of the second placed clan in the 0.16 tournament, May 2015.',
        True, ('elmdor', 'Happylisk', 'HilariousDeathArtist', 'NilsBloodaxe',
               'Zalbag', 'zarzak')),
    Achievement(
        '0.16_clan_third', '0.16 Tournament: Third Place (Clan)',
        'Part of the third placed clan in the 0.16 tournament, May 2015.',
        True,
        ('MorganLeah', 'Glenstorm', 'Lasty', 'Snack', 'WalkerBoh', 'Rast')),
    Achievement('0.15_first', '0.15 Tournament: First Place',
                'First place in the 0.15 tournament, August 2014.', True,
                ('Tolias', )),
    Achievement('0.15_second', '0.15 Tournament: Second Place',
                'Second place in the 0.15 tournament, August 2014.', True,
                ('Yermak', )),
    Achievement('0.15_third', '0.15 Tournament: Third Place',
                'Third place in the 0.15 tournament, August 2014.', True,
                ('johnnyzero', )),
    Achievement(
        '0.15_clan_first', '0.15 Tournament: First Place (Clan)',
        'Part of the first placed clan in the 0.15 tournament, August 2014.',
        True, ('Tolias', 'MrPlanck', 'Tabstorm', 'Tedronai', 'Yermak',
               'magicpoints')),
    Achievement(
        '0.15_clan_second', '0.15 Tournament: Second Place (Clan)',
        'Part of the second placed clan in the 0.15 tournament, August 2014.',
        True, ('DrKe', 'Roarke', 'Sky', 'agentgt', 'johnnyzero',
               'perunasaurus')),
    Achievement(
        '0.15_clan_third', '0.15 Tournament: Third Place (Clan)',
        'Part of the third placed clan in the 0.15 tournament, August 2014.',
        True,
        ('MorganLeah', 'Glenstorm', 'Lasty', 'Snack', 'WalkerBoh', 'caleba')),
    Achievement('0.14_first', '0.14 Tournament: First Place',
                'First place in the 0.14 tournament, April 2014.', True,
                ('Tolias', )),
    Achievement('0.14_second', '0.14 Tournament: Second Place',
                'Second place in the 0.14 tournament, April 2014.', True,
                ('johnnyzero', )),
    Achievement('0.14_third', '0.14 Tournament: Third Place',
                'Third place in the 0.14 tournament, April 2014.', True,
                ('Yermak', )),
    Achievement(
        '0.14_clan_first', '0.14 Tournament: First Place (Clan)',
        'Part of the first placed clan in the 0.14 tournament, April 2014.',
        True, ('ebarrett', 'Ayutzia', 'Ragdoll', 'ToastyP', 'jeanjacques',
               'johnnyzero')),
    Achievement(
        '0.14_clan_second', '0.14 Tournament: Second Place (Clan)',
        'Part of the second placed clan in the 0.14 tournament, April 2014.',
        True, ('Yermak', '4thArraOfDagon', 'BLOAX', 'Tolias', 'Vidiiot',
               'hurdos')),
    Achievement(
        '0.14_clan_third', '0.14 Tournament: Third Place (Clan)',
        'Part of the third placed clan in the 0.14 tournament, April 2014.',
        True, ('DrKe', 'Roarke', 'ackack', 'agentgt', 'cszzzz', 'wheals')),
    Achievement('0.13_first', '0.13 Tournament: First Place',
                'First place in the 0.13 tournament, October 2013.', True,
                ('bmfx', )),
    Achievement('0.13_second', '0.13 Tournament: Second Place',
                'Second place in the 0.13 tournament, October 2013.', True,
                ('78291', )),
    Achievement('0.13_third', '0.13 Tournament: Third Place',
                'Third place in the 0.13 tournament, October 2013.', True,
                ('elliptic', )),
    Achievement(
        '0.13_clan_first', '0.13 Tournament: First Place (Clan)',
        'Part of the first placed clan in the 0.13 tournament, October 2013.',
        True, ('dck', 'Basil', 'Implojin', 'Infected', 'Sar', 'pubby')),
    Achievement(
        '0.13_clan_second', '0.13 Tournament: Second Place (Clan)',
        'Part of the second placed clan in the 0.13 tournament, October 2013.',
        True, ('WalkerBoh', 'Glenstorm', 'MorganLeah', 'Snack', 'rast',
               'rzimodnar')),
    Achievement(
        '0.13_clan_third', '0.13 Tournament: Third Place (Clan)',
        'Part of the third placed clan in the 0.13 tournament, October 2013.',
        True, ('n1000', 'blazinghand', 'bmfx', 'ogaz', 'rchandra', 'tewe')),
    Achievement('0.12_first', '0.12 Tournament: First Place',
                'First place in the 0.12 tournament, May 2013.', True,
                ('jeanjacques', )),
    Achievement('0.12_second', '0.12 Tournament: Second Place',
                'Second place in the 0.12 tournament, May 2013.', True,
                ('elliptic', )),
    Achievement('0.12_third', '0.12 Tournament: Third Place',
                'Third place in the 0.12 tournament, May 2013.', True,
                ('Tolias', )),
    Achievement(
        '0.12_clan_first', '0.12 Tournament: First Place (Clan)',
        'Part of the first placed clan in the 0.12 tournament, May 2013.',
        True, ('Cheibrodos', 'Arrhythmia', 'Spectrina', 'Tolias', 'Wahaha',
               'magicpoints')),
    Achievement(
        '0.12_clan_second', '0.12 Tournament: Second Place (Clan)',
        'Part of the second placed clan in the 0.12 tournament, May 2013.',
        True, ('elliptic', 'MarvinPA', 'mikee', 'pivotal', 'reid', 'simm')),
    Achievement(
        '0.12_clan_third', '0.12 Tournament: Third Place (Clan)',
        'Part of the third placed clan in the 0.12 tournament, May 2013.',
        True,
        ('elliott', '78291', 'Elynae', 'Swiss', 'VizerT', 'jeanjacques')),
    Achievement('0.11_first', '0.11 Tournament: First Place',
                'First place in the 0.11 tournament, November 2012.', True,
                ('theglow', )),
    Achievement('0.11_second', '0.11 Tournament: Second Place',
                'Second place in the 0.11 tournament, November 2012.', True,
                ('jeanjacques', )),
    Achievement('0.11_third', '0.11 Tournament: Third Place',
                'Third place in the 0.11 tournament, November 2012.', True,
                ('bmfx', )),
    Achievement('0.10_first', '0.10 Tournament: First Place',
                'First place in the 0.10 tournament, March 2012.', True,
                ('elliptic', )),
    Achievement('0.10_second', '0.10 Tournament: Second Place',
                'Second place in the 0.10 tournament, March 2012.', True,
                ('jeanjacques', )),
    Achievement('0.10_third', '0.10 Tournament: Third Place',
                'Third place in the 0.10 tournament, March 2012.', True,
                ('pivotal', )),
    Achievement('0.9_first', '0.9 Tournament: First Place',
                'First place in the 0.9 tournament, August 2011.', True,
                ('theglow', )),
    Achievement('0.9_second', '0.9 Tournament: Second Place',
                'Second place in the 0.9 tournament, August 2011.', True,
                ('mikee', )),
    Achievement('0.9_third', '0.9 Tournament: Third Place',
                'Third place in the 0.9 tournament, August 2011.', True,
                ('jeanjacques', )),
    Achievement('0.8_first', '0.8 Tournament: First Place',
                'First place in the 0.8 tournament, May 2011.', True,
                ('mikee', )),
    Achievement('0.8_second', '0.8 Tournament: Second Place',
                'Second place in the 0.8 tournament, May 2011.', True,
                ('elliptic', )),
    Achievement('0.7_first', '0.7 Tournament: First Place',
                'First place in the 0.7 tournament, August 2010.', True,
                ('elliptic', )),
    Achievement('0.7_second', '0.7 Tournament: Second Place',
                'Second place in the 0.7 tournament, August 2010.', True,
                ('Jaeger', )),
    Achievement('0.7_third', '0.7 Tournament: Third Place',
                'Third place in the 0.7 tournament, August 2010.', True,
                ('78291', )),
    Achievement(
        '0.7_clan_first', '0.7 Tournament: First Place (Clan)',
        'Part of the first placed clan in the 0.7 tournament, August 2010.',
        True,
        ('casmith789', 'MarvinPA', 'Pseudonut', 'elliptic', 'nht', 'ogaz')),
    Achievement(
        '0.7_clan_second', '0.7 Tournament: Second Place (Clan)',
        'Part of the second placed clan in the 0.7 tournament, August 2010.',
        True, ('Jaeger', 'Sastopher', 'ToastyP', 'henryci', 'nmf', 'reid')),
    Achievement(
        '0.7_clan_third', '0.7 Tournament: Third Place (Clan)',
        'Part of the third placed clan in the 0.7 tournament, August 2010.',
        True, ('valrus', 'Morri', 'PigVomit', 'daftfad', 'herself', 'nrook')),
    Achievement('0.5_first', '0.5 Tournament: First Place',
                'First place in the 0.5 tournament, August 2009.', True,
                ('78291', )),
    Achievement('0.5_second', '0.5 Tournament: Second Place',
                'Second place in the 0.5 tournament, August 2009.', True,
                ('mikee', )),
    Achievement('0.5_third', '0.5 Tournament: Third Place',
                'Third place in the 0.5 tournament, August 2009.', True,
                ('elliptic', )),
    Achievement(
        '0.5_clan_first', '0.5 Tournament: First Place (Clan)',
        'Part of the first placed clan in the 0.5 tournament, August 2009.',
        True, ('Jeff', 'Grivan', 'MadDasher', 'heteroy', 'mikee', 'rob')),
    Achievement(
        '0.5_clan_second', '0.5 Tournament: Second Place (Clan)',
        'Part of the second placed clan in the 0.5 tournament, August 2009.',
        True, ('doy', '78291', 'Grimm', 'Stabwound', 'cbus', 'elliptic')),
    Achievement(
        '0.5_clan_third', '0.5 Tournament: Third Place (Clan)',
        'Part of the third placed clan in the 0.5 tournament, August 2009.',
        True, ('LordSloth', 'CatEater', 'ZaurenTour', 'eternal', 'pointless',
               'trucutru')),
    Achievement('0.4_first', '0.4 Tournament: First Place',
                'First place in the 0.4 tournament, August 2008.', True,
                ('Stabwound', )),
    Achievement('0.4_second', '0.4 Tournament: Second Place',
                'Second place in the 0.4 tournament, August 2008.', True,
                ('78291', )),
    Achievement('0.4_third', '0.4 Tournament: Third Place',
                'Third place in the 0.4 tournament, August 2008.', True,
                ('Dingir', )),
    Achievement(
        '0.4_clan_first', '0.4 Tournament: First Place (Clan)',
        'Part of the first placed clan in the 0.4 tournament, August 2008.',
        True, ('doy', '78291', 'Stabwound', 'cbus', 'duke', 'wasp')),
    Achievement(
        '0.4_clan_second', '0.4 Tournament: Second Place (Clan)',
        'Part of the second placed clan in the 0.4 tournament, August 2008.',
        True, ('rax', 'Enne', 'Iaido', 'Shiori', 'modicum', 'violetj')),
    Achievement(
        '0.4_clan_third', '0.4 Tournament: Third Place (Clan)',
        'Part of the third placed clan in the 0.4 tournament, August 2008.',
        True, ('Eronarn', 'Foggy', 'Tag', 'Voiks', 'eternal', 'pointless')), )
GHOST_KILL_VERBS = {'drained of all life', 'hit from afar', 'blown up by',
                    'incinerated', 'blasted', 'slain'}
